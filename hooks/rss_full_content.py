"""Post-process RSS feed to add content:encoded with full content."""
import os
import re
import yaml


def on_post_build(config):
    """Move full content to content:encoded, use frontmatter description for description."""
    site_dir = config['site_dir']

    # Get article descriptions from frontmatter
    docs_dir = config['docs_dir']
    descriptions = {}
    for filename in os.listdir(docs_dir):
        if not filename.endswith('.md'):
            continue
        filepath = os.path.join(docs_dir, filename)
        try:
            with open(filepath, 'r') as f:
                content = f.read()
            if not content.startswith('---'):
                continue
            end = content.find('---', 3)
            if end == -1:
                continue
            front_matter = yaml.safe_load(content[3:end])
            if front_matter and front_matter.get('description'):
                url_slug = filename.replace('.md', '') + '/'
                descriptions[url_slug] = front_matter['description']
        except Exception:
            continue

    # Process each RSS feed
    for feed_name in ['feed_rss_created.xml', 'feed_rss_updated.xml']:
        feed_path = os.path.join(site_dir, feed_name)
        if not os.path.exists(feed_path):
            continue

        with open(feed_path, 'r') as f:
            xml_content = f.read()

        # Add content namespace if not present
        if 'xmlns:content=' not in xml_content:
            xml_content = xml_content.replace(
                '<rss ',
                '<rss xmlns:content="http://purl.org/rss/1.0/modules/content/" '
            )

        # Process each item
        def process_item(match):
            item = match.group(0)

            # Extract link to get slug
            link_match = re.search(r'<link>([^<]+)</link>', item)
            if not link_match:
                return item
            url = link_match.group(1)
            slug = url.rstrip('/').split('/')[-1] + '/'

            # Extract current description (full content)
            desc_match = re.search(r'<description>(.*?)</description>', item, re.DOTALL)
            if not desc_match:
                return item
            full_content = desc_match.group(1)

            # Strip headerlink anchors (pilcrows)
            full_content = re.sub(r'&lt;a class=&#34;headerlink&#34;.*?&lt;/a&gt;', '', full_content)

            # Create content:encoded element
            content_encoded = f'<content:encoded>{full_content}</content:encoded>'

            # Replace description with frontmatter description or stripped content
            if slug in descriptions:
                new_desc = descriptions[slug].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            else:
                new_desc = full_content  # Already has pilcrows stripped
            item = re.sub(
                r'<description>.*?</description>',
                f'<description>{new_desc}</description>',
                item,
                flags=re.DOTALL
            )

            # Insert content:encoded before </item>
            item = item.replace('</item>', f'{content_encoded}</item>')
            return item

        xml_content = re.sub(r'<item>.*?</item>', process_item, xml_content, flags=re.DOTALL)

        with open(feed_path, 'w') as f:
            f.write(xml_content)
