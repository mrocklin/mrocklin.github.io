---
title: Rethinking My Website and Blog
og:title: Rethinking My Website and Blog
date: 2023-01-02
blogpost: true
author: Matthew Rocklin
category: writing
---

Rethinking My Website and Blog
==============================

*How we read and write shapes how we think*

Twitter chaos made us rethink our engagement on the web.
Personally, I felt smarter and happier pre-Twitter.
During this period I engaged by reading and writing blogs.
I drifted away from my practice of blogging,
but I'm intentionally turning back to that direction.

With this in mind I rebuilt my personal website and blog.
This article discusses the reasoning behind the new design.

I had a few objectives in this transition:

-   Optimize for slightly longer attention spans
-   Mix evergreen and timely content
-   Flatten organizational hierarchy
-   Experiment with automation to integrate with social media

Motivation
----------

### Why I Stopped Blogging

I used to blog a lot more,
but I stopped for a few reasons:

1.  My Twitter follower count increased, encouraging me to engage directly there

2.  I grew multiple blogging venues (personal blog, community project blog, company blog)
    which had longer review periods and delays, which discouraged writing

    *I find that I write 10x more if publication is instantaneous*

3.  My blogging infrastructure was embarrassingly out of date

    *this was ancient, didn't have https, metadata for social sharing, good style, etc..*

But I miss it for a few reasons

### Longer Attention Spans

I write [short posts](write-short-blogposts.md) to a [short attention span](brevity.md).
However, I think that the 280 character limit of Twitter goes too far.
Twitter encourages punchy communication devoid of depth or complex thinking and
forces lots of skimming.  I feel that my brain is largely inactive when on the web.
**I'm pushing against this.**

I'd like to author more thoughtful content.
I'd like to encourage readers towards deeper thought.
Blogging helps.

### Evergreen content

I frequently point colleagues to posts I wrote years ago.
Here are a few:

-   [Why I Avoid Slack](slack-github.md)
-   [Minimal Bug Reports](minimal-bug-reports.md)
-   [Biased Benchmarks](biased-benchmarks.md)
-   [Avoid Indirection](avoid-indirection.md)

And also some more recent posts I've made:

-   [Startup Best Practices](startup-best-practices.md)
-   [Startup Revenue](startup-revenue.md)
-   [Meetings](meetings.md)

I value these posts 100x more than any Tweet because I get continuous value from them.
I've shared these manually with hundreds of people,
and they get plenty of traffic from strangers.

New Blog Implementation
-----------------------

I have a new website and blog! 🎉

Source lives at
[https://github.com/mrocklin/mrocklin.github.io](https://github.com/mrocklin/mrocklin.github.io) and is hosted at [https://matthewrocklin.com](https://matthewrocklin.com).

There are a few choices I made.  Let's go through them and why.


### Basics: Sphinx and Markdown

I am most familiar with Markdown to author documents and Sphinx to render them.
I stole my baseline implementation from
[Chris Holdgraf](https://chrisholdgraf.com).
This uses various technologies like the
[PyData Sphinx Theme](https://github.com/pydata/pydata-sphinx-theme),
[MyST](https://myst-parser.readthedocs.io/en/latest/)
and [ablog](https://ablog.readthedocs.io/en/stable/),
which
I'll [let Chris describe](https://chrisholdgraf.com/blog/2020/sphinx-blogging/).

### Blog posts (timely) v. Docs (evergreen)

Looking at my old blog there are two different categories of articles:

-   **Timely:** One-off content describing a recent experiment or thought that I wanted to
    share right away

    Examples:
    -   [First Impressions of GPUs and PyData](https://matthewrocklin.com/blog/work/2018/12/17/gpu-python-challenges) published my first week after moving to NVIDIA
    -   [Dask Release 0.18](https://matthewrocklin.com/blog/work/2018/06/14/dask-0.18.0) (there are many of these)

-   **Evergreen:** Deeper thoughts where I'm trying to communicate with / teach colleagues

    Examples:

    -   [Role of a maintainer](maintainer.md) aimed at people taking on
        developer/reviewer/maintainer roles in OSS
    -   [Avoid Indirection](avoid-indirection.md) aimed at contributors to OSS
        projects.

Both categories are important to how I work, but are typically served
differently.

-   Timely/ephemeral content is well served by blog infrastructure with chronological ordering, tags, and RSS feeds.
-   Evergreen/educational content is well served by a layout more similar to the documentation of a software
project.

I want both.  I have both.

If you're reading this on my website you'll see a sidebar to the left, similar
to what you would find in the documentation for a software project.  This
sidebar lays out the evergreen content.  New posts don't go here automatically,
I have to place them in the sidebar intentionally.  This whole site could be
seen as **"documentation to working with matt".**

At the same time, every post does have appropriate blog metadata to be included
in the top-level [articles](articles.md) page, which lists things
chronologically, as well as the [Atom/RSS feed](https://matthewrocklin.com/atom.xml).
It's like a documentation site where every new page gets an RSS entry.

### Atom/RSS Feed

I miss Google Reader.  This technology encouraged people to read and share
long-form articles.  It made the content and sharing primary while
commenting/liking was an after thought.

I don't use an RSS feed reader today, but I'd like to start again.
I know that others do and so I'm resurrecting an Atom/RSS feed is at
[https://matthewrocklin.com/atom.xml](https://matthewrocklin.com/atom.xml).

### Flat directory structure

One of the things I disliked about my Jekyll blog (and lots of static site
generator default configurations) was the focus on chronology and dates in
titles and URLs.  URLs looked like this:

-  https://matthewrocklin.com/blog/work/2022/07/19/scipy-mission

I then shaped this site to be in categories with URLs like the following:

-   https://matthewrocklin.com/engineering/scipy-mission

I don't care about the dates of things that I read.
They just get in the way.
But then I realized that I didn't care about categories either,
and so now everything is just flat.

-   [https://matthewrocklin.com/scipy-mission](https://matthewrocklin.com/scipy-mission)

As a reader you probably don't care (you got here by clicking a link) but
flat structures appeal to me personally.

### Automated Social Sharing

I've hooked up [IFTTT](https://ifttt.com/) to Twitter and LinkedIn.
I haven't found a good Mastodon solution yet.

The results here aren't as good as I would do for Twitter, but it does mean I don't have to log in.
Also, I never used to engage at all on LinkedIn, and so this will help greatly over there.

Final Thoughts
--------------

This is an experiment.  It may fail!  That's ok!

People should experiment more with how they communicate.
I encourage you to give your own communication habits some consideration.
