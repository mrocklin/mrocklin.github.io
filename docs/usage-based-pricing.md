---
title: Usage Based Pricing
date: 2024-09-04
blogpost: true
author: Matthew Rocklin
category: startups
---

Pivoting away from Usage Based Pricing
======================================

We're moving away from usage based pricing.

This post talks about the pros and cons of usage based pricing in our
situation, and then talks through alternatives.

<img src="https://i.imgflip.com/92vpi1.jpg" alt="Usage based pricing meme"
width="40%" align="center"/>

Where we are today
------------------

People who follow my blog may recall that ...

1.  We have a product people love
2.  But we weren't selling it well
3.  So we hired AEs (new!)
4.  They're working out fantastically well (new!)

Hooray 🎉!  The bottom of our funnel now flows decently and our revenue is
dramatically increasing (easy to increase dramatically when it starts low 🙂)

However, now we have a different problem.  Pricing!  Today our biggest problem
is figuring out how to capture more of the value we generate for customers
while also making them feel good about paying us.  This problem is tricky.

Today, we do usage-based pricing.  This was good for a while, but ended up
being a bit of a dead end for us.  Let's talk through why.

Why Usage Based Pricing was Great
---------------------------------

Previously, we charged $0.05 per CPU-Hour, the same as major clouds or
Databricks.  We liked this when getting started for a few reasons.

-  **It’s simple** and it’s easy to understand quickly
-  **It’s standard** in our space and so familiar to buyers
-  **It starts small** so on-boarding isn't focused on financials
-  **It’s on-par** with other things the customer is already paying for (the cloud in this case)
    so we know that they have budget for bills like this
-  **It’s unbounded** so if a company does really really well, we can make a lot of money

Mostly it was a simple default choice, and a good basis for a pricing scheme.
It’s minimally scary, and so good at getting people in the door.

But eventually it broke down.  Let’s talk about how, and then we’ll talk about what we do today.


Why Usage Based Pricing was Terrible (for us)
---------------------------------------------

There were a few fail cases:

-  Customers for whom our product was critical infrastructure (high value) but whose usage was
   really small (low price)
-  Customers where we optimized their workloads 10-100x, and so reduced our
   revenue 10-100x (misaligned priorities)
-   Customers who didn't like percentage increases on their usage
    (like how paying $10 for a bottle of water feels bad at an event)

Consider the following conversation as an example:

-  **Customer**: You charge a 100% markup.  That’s too high.

    I was expecting closer to 30-40%.  I’m paying $2,000 monthly to AWS and $2,000 to you

-  **Us**: Yes, but before using us you ...

    -   were paying $20,000 to AWS because you were so inefficient
    -   were spending half an FTE maintaining that terrible  infrastructure

        (costing 50% * $200k == $100,000/year)
    -   had a data science team of five was spending 20% of their time fighting
        that terrible infrastructure

        (costing 5 * 20% * $200k == $200,000 / year)
    -   couldn't finish that project that was critical to your business
        and which you were just able to finish in a couple weeks since using us

        (the value of which only you can determine, but is probably higher than the rest)

-  **Customer**: Oh yeah, I guess that's right.  I guess this is worth the
   $2,000 you're asking for

-  **Us:** actually, now that I think about it, we should probably be charging
   you much more

    (I never actually said this last part, but it was a frequent thought).

There were two problems here:

1.  **We captured only a small fraction** of the benefit we provided to users
2.  **Users felt bad** about the small fraction that we did capture

Something was clearly wrong here.  Users value our product beyond what
they pay (they’re getting a great deal!) but they feel like they’re
getting screwed, and that's not good for anyone.

I've learned that pricing is as much about psychology as about aligning cost and value.

Why did this not work out for us?
---------------------------------

Usage-based pricing is the norm for computational cloud products.  Why does it
work for others (like AWS or Databricks) but not for us?

I have a few theories:

1.  **Efficiency** we're just much better at making users efficient.

    Users often come in with $100,000 annual cloud bills, but after using the
    product realize they only need to spend $5,000-10,000.

    The vast majority of cloud usage today is misuse and our product stops
    misuse.  Stopping misuse is great for the user (🎉) and bad for the cloud (🎉).
    However, it's also bad for us (😞) under usage based pricing.

2.  **Python** is more prone to these 100x efficiency swings than other
    technologies, like SQL, where 2-5x is more common.

    Python can be either incredibly efficient or inefficient based on
    expertise.  With our product novices are less cost-prone, both because of
    the product itself, and because of our incredible support team (more on
    this later)

    We could make the product worse or stop giving good support and we'd
    probably earn more but this doesn't feel great.  There's clearly a lot of
    value that we can generate and would like to capture.

3.  **SMBs** for velocity reasons we mostly focus on Small and Medium
    Businesses (SMBs) rather than large enterprises.

    SMBs tend to value human performance more than cloud spend (humans and
    speed are more expensive than cloud at this scale).  Maybe our focus here
    puts us in a strange place where the main value we provide isn't aliged
    with cloud cost, but rather human acceleration.

After seeing the $100,000 -> $5,000 transition a few times and cursing the
efficiency of our product we started rethinking how we price the product.

So let's look at some possible new solutions.  Before that though, let's talk
briefly about what we sell.

What do we sell?
----------------

In general people like using Coiled because they get to operate at larger
scale more smoothly than before.  This is due to a couple of things:

-   **Product:** the Coiled product is powerful and has a UX that feels good
    to Python data devs.  It's a powerful tool that's comfortable to wield.

-   **Support:** the product also tells *us* a lot about what users do, and our
    support team reaches out proactively as we see users struggle.
    One Coiled support engineer easily unblocks a dozen users daily.

    Users *love* our support team, and describe it as unlike anything else
    they've experienced.
    It's like we've constructed a platform that enables us to do lots of high
    impact micro-consulting.  Unfortunately, the market isn't used to this.

The product is hard to price because of the efficiency issues with Python
(we often make people 10x more efficient and so shoot ourselves in the foot).

The support is hard to price because we're trapped in between two things people
are used to:

1.  **Typical (bad) product support** most SaaS products have some support tier
    that costs 20% on top of usage and offers access to a mediocre support
    experience.  I've personally never found value in SaaS support teams.

    This is like what we do, but cheaper and worse.

2.  **Professional Services** consulting firms charge by the hour to unblock
    customers.  This is much more valuable, but a way of working that's also
    pretty distracting and that we're not set up to do (I'm done counting
    hours).

    This is more like the value we provide, but operationally quite different
    (we dont bill hourly and we only work on what we want to).

Our support is similar enough that we get pattern matched to existing
offerings, but different enough that those approaches don't make sense for us.

Objectives for a good pricing scheme
------------------------------------

So let's say we want to invent something new?  What are some objectives?

1.  **Easy to start** using the product without worrying

    (we want the customer to see the value of the product before thinking about money)

2.  **Total price** matches the value the customer sees and can pay, so if a customer
    ...

    -   is unable to pay anything (like a student) it should be free
    -   is getting a lot of value and is able to pay, it should cost a lot
        (but less than the value they experience)

3.  **Mentally easy for the customer** to connect price to value

    We want the customer to be able to easily understand the price and connect
    it to the value they're getting.  So for example if most of our value is
    accelerating their people, then we should charge per person.

What we're trying today
-----------------------

Today we're rolling out a change to [our pricing](https://www.coiled.io/pricing).

-  **For basic/individual users not much changes**.  It's still usage-based which
   makes it easy to test things out without thinking too hard.  We are putting
   some seat-caps on this tier though.

-  **For larger teams we switch to usage + seat based pricing.**  We charge
   some very small percentage of an FTE cost per seat.  This is big enough to
   be meaningful to us, while small enough that when the customer asks
   themselves "How much more efficient is my team with this tool?" they come up
   with an answer that is far larger than the percentage we charge.

Future work
-----------

This feels better but still not great.

-   It feels good that we're shifting to human-based pricing (to match the human-based value we think we generate)
-   But human-based value feels *squishy* and hard to quantify, which requires
    more thinking on the user's part, and more conversation on ours.

We have our work cut out for us.  I look forward to seeing how this lands.
