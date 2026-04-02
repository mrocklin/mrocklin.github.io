---
title: Stepping Back
date: 2026-04-02
tagline: Pulling back from day to day work
description: I'm stepping back from Coiled, Dask, and Python OSS to make space for what's next.
blogpost: true
author: Matthew Rocklin
---

# Stepping Back

I'm stepping back from my current commitments (Coiled, Dask, Python OSS generally) to make some space for myself.  This post details concrete implications of that choice, and then explores some of my thinking.

## Coiled

We've transformed Coiled into a pragmatic but less ambitious version of the company.

Coiled is no longer actively marketing itself and we're saying no to long enterprise sales processes.  We're focused instead on serving existing customers and simplifying internal operations.  The company is now much smaller, consisting of two engineers who keep things humming nicely for customers. Fortunately the Coiled architecture makes this low-effort to maintain long-term.

Financially, while Coiled is unlikely to ever become the next trillion-dollar company, it is now nicely profitable and can continue indefinitely.  We had a pile of cash in the bank which has gone towards buying out preferred shareholders.  The company is now owned exclusively by common shareholders.

If you're a current customer of Coiled fear not, we're not planning to go anywhere and, unlike before, you're our current focus.  If you have concerns I'm happy to chat.

## Dask

With Coiled no longer pushing on Dask, and with me stepping back from both, there isn't a strong innovative force behind Dask today.

That's ok.  Like lots of well-used open source, Dask today is more focused more on stability than on pushing new features.  Dask continues to be maintained, albeit with less vigor.  Community members wanting new features for free may be disappointed, but users hoping that Dask continues cranking away should remain satisfied.

## Personal Situation

I loved my time building up Dask, especially in the early days when I'd wake up every morning to dozens of emails from excited users building their own things with Dask.  Collaborating with those people, incorporating feedback, designing new systems, and together pushing forward transformative change in science and industry has been the highlight of my career.

It feels amazing to work hard and see our work have an increasingly broad impact in the world.

However, work no longer feels that way.  At some point turning the crank of productivity turns to grinding, becoming less productive/fun/satisfying.  I stopped having fun a while ago, both because I've been at it a while, and because I ran into problems that I didn't know how to solve (Coiled problems were harder than Dask problems, and when issues like marketing became our biggest challenge they started to feel intractable).

Time is finite, and there's a tradeoff between cranking and exploring.  I'm in the fortunate financial position to be able to step back and assess what I want from life.  I don't know what my next path is yet (start a new company? get a job? get a life?) but I look forward to finding out.

## Final Thought

In the meantime, I'm not doing much, and oddly that seems like the most interesting and challenging path for me.

To end, here's a quote I like from T.S. Eliot

> **I said to my soul, be still and wait without hope,**<br/>
> **for hope would be hope for the wrong thing**;<br/>
> wait without love, for love would be love of the wrong thing;<br/>
> there is yet faith, but the faith and the love are all in the waiting.<br/>
> **Wait without thought, for you are not ready for thought**:<br/>
> So the darkness shall be the light, and the stillness the dancing

Which I interpret as "sometimes you have to do nothing for a while, and that's ok".

---

---


For a treatment of this same information, but in a more casual tone, there are some details below:

# FAQ

(just kidding, no one asked these questions, but I thought I'd answer them anyway)

??? faq "How is Coiled Financially?"
    We make about $1M annually (a little less).  We don't seem to be able to grow this substantially, or at least not faster than just waiting around for people to show up.  No marketing effort has had much effect.  Rather than burn more cycles, it makes more sense to us to just let Coiled do its thing organically.  It's also way less effort.

    Investors lost confidence that we'd make it big (quite reasonably) and so we came to an agreement where they were able to exit with most of the remaining cash.  Not all though; we've a healthy buffer and the service itself is pretty cheap to run thanks to its architecture.

    David and Nat work now on Coiled part time, mostly just tracking customer issues and making sure things run smoothly.  They don't spend much time on non-paying users or with enterprise procurement teams (sorry, not sorry), and no one spends time evangelizing.  I handle the occasional legal issue.

??? faq "Is Dask Dead?"
    Usage (as measured by my favorite measure of API docs hits) has been flat for a few years.  I don't expect Dask to take over the world, but it doesn't seem to be going anywhere.

    Some folks are still doing some mild maintenance (Jacob, James, Tom, Florian, Guido) but it's no one's full time job.  It'll be interesting to see how effective community open source is these days at supporting the community.

    There are some technical projects I've been wanting to do on Dask for the last few years (query planning for arrays, rewriting in a compiled language, working with high performance hardware).  I might get to those at some point?

    To be honest though (maybe too honest) I've been feeling conflicted about Dask/OSS work recently.  Historically my motivation has come from positive user engagement and community collaboration but over the last few years that relationship hasn't felt as rewarding.  Mostly I get the sense that people have started to expect a lot of free work without a sense of collaboration or working together, which doesn't feel good.  I suspect that users have been trained by all the for-profit companies throwing free things at them for their attention.  While Dask isn't dead, to me it feels like community OSS has died a little.

??? faq "What will you do?"
    Yeah, good question.  There are a few possibilities.  I could ...

    - **Start a new company:** I like work, and while making the first company was arduous, there's lots I'd like to experiment in doing this again.  I'm especially curious about how lean one can go with AI today.  Unfortunately for me though, I don't have a driving project or mission, which puts this plan on hold.

    - **Get an actual job:** Maybe someone else has a mission I could believe in, or some lessons I could learn, or piles of money (I'm not above working for piles of money).  Fortunately for me though, I'm in a financial situation where I don't need a job, so the bar here is pretty high.

    - **Get a life:** I've spent the last two decades immersed in building software, communities, and a company.  I've not thought much about the rest of my life.

    Right now I'm focused on **getting a life**.  It's hard though.  Shifting from "super busy" to "how can I fill up my time today?" is a big lifestyle shift.  I've enjoyed speaking to older retirees who have gone through something similar.  Right now I'm trying to build a social community, build my legs back up for some running and long-distance walking, and reading in my downtime.  Book recommendations are very welcome.

??? faq "How are you feeling?  Is this a big shock?"
    I'm feeling bored, but generally pretty good, and no, this isn't a big shock.

    This has been a gradual transition over many months.  We started exploring the small-but-profitable company configuration back in Q4 of 2025, and the company has been operating with current staff since the new year.  There's been some work to enact the transition, but overall it's been an easy last few months.

??? faq "You were doing AI stuff for a bit.  What happened to that?"
    After the decision to transition to small-but-profitable Coiled I spent a couple months playing intensively with AI, making projects like [claudechic](https://github.com/mrocklin/claudechic) (along with several others that never saw the light of day beyond personal use).  This was super-fun, but ended up not holding my attention, both because of all the noise/hype in the area, and because there wasn't anything that I was really passionate about building.  I was just building to build.

    I like building things, but I find I need to care deeply about the thing that I'm building in order to stick with it, and I haven't found such a thing.

    I'm still very pro-AI, but only in the service of building real things.  I'd love to see the world build fewer AI products, and more products with AI.
