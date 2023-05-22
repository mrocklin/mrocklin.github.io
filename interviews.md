---
title: How I Conduct an Interview
og:title: How I Conduct an Interview
date: 2023-01-06
blogpost: true
author: Matthew Rocklin
category: startups
---

Interviews
==========

Interviewing is hard.  It's also important to do well.

A good/bad match can be transformative/terrible for both the company and the
candidate.  This article describes my current approach.  It may be useful for
others who are conducting interviews, or for people who plan to interview with
me (transparency is good).

My interviews are typically in 45 minute calendar slots.
After saying "hi" and being friendly for a minute or two I lead the
conversation through the following stages:

## I talk about the company and what we're looking for

*This typically takes five minutes*

First, I give information about the company, the teams within the company and
where we think the candidate might fit, and what kinds of candidates we think
work well with us.

In our case I say things like the following ...

-   We're a commercial company based around the open source Dask project

-   Engineering-wise we do two things

    -   Work on Dask and push it forward
    -   Build a cloud SaaS deployment platform

    Given your background, we think that you're a good fit for one or the
    other, but our most impactful folks end up being able to cross both.

-   Historically we've found that we work well with senior engineers who are
    professional (can deliver things on time, even in complex situations), know
    open source culture, but also care about commercialization (we're a
    for-profit company and culturally lean into that).  This is what we're
    looking for.

On the last bit I like to be explicit.  People need to opt-in to both our
strengths and our constraints:

-   **Seniority:** we're bad at management and don't mentor people well when they're early in their careers
-   **Professionalism:** there are so many interesting problems around us that it's
    easy to get distracted (we all suffer from this).  We prefer important work
    to interesting work, prioritize intentionally, and feel good about setting
    commitments and working to timelines.  This is typically hard for academics.
-   **Commercial OSS:** we believe in the power of open source communities.  We
    also understand their limitations.  We are excited about commercial impact
    and and using that energy to both make money and have social impact.

There are *very good people* who don't fit that culture.  We like to be explicit
to avoid mismatches.  Alignment is good for anyone.

## Learn more about the candidate

*This typically takes twenty minutes*

Next, it's time to figure out if the candidate knows what they're talking
about.  There are many ways to do this, none of which are particularly good.

Personally, I like to ask them what they know about us and if they have
relevant experience.  I then like to dig into that experience and test
different situations to probe a bit.

-   Interviewer: "Have you used Dask or anything like it before?"
-   Candidate: "I haven't, but I did use Spark at my last job"
-   Interviewer: "Oh cool, what did you use it for?"
-   Candidate: "We did a lot of machine learning and AI"
-   Interviewer: "Oh interesting, what kinds of models were you training?"

    *Get to probe their understanding of technical work*
-   Candidate: "We tried using XGBoost, but really most of it was logistic regression"
-   Interviewer: "I'm curious, I don't know much about this field, but my understanding is that it's commonly better to just sample and train locally.  Why use distributed computing at all?"

    *See how they react to a challenge.  See their ability to critically analyze their own directions*.

-   ...

-   Interviewer: "Why were you training these models?"

    *Probe their understanding of how their work affects the rest of the
    business*

-   ...

## Candidate asks questions of us

My usual line here is "I have a couple more questions to ask, but first, do you
have any questions for us?"

What they ask here is telling.  Sometimes people are ask generic questions. These look like the following:

1.  What are your biggest challenges?
2.  How is company culture?
3.  Where do you see yourself in five years?

More informed candidates usually have more specific questions for us:

1.  How are you balancing between the cloud platform and OSS work?  Are those
    teams siloed?  Is there space to work on both?
2.  Tech companies are in a bad way these days.  How secure is my job here?
3.  I'm really interested in application X.  Is that something that there would
    be space to work on while here?

Often I'm not judging them at this point.  I'm probably trying to sell them.
It's good and healthy to have the tables turned.  Interviewing is
bi-directional in any good relationship.

## Logistics questions

At the end I keep about five minutes to ask the following:

1.  **What's your risk tolerance?**

    Mostly I'm trying to scare them:

    *We're an early stage startup.  We're not shy about changing direction.  We have a history of firing people.
    You seem great and we're picky about who we bring on,
    but we like to be upfront about the possibility of separation.*

    *Typically people in this space can get a new job within our typical
    severance period (one month historically) but are you comfortale with this
    sort of dynamic?*

2.  **What are your payment expectations?**

    This is an awkward conversation to bring up.  My usual phrasing is
    something like the following:

    *You can totally pass on this next question, but roughly what your are you looking to make here salary-wise.*

    *The reason I ask is that we've gone through interview cycles with
    candidates only to find, at the end, that they're expecting $300k+, and
    we're nowhere near that.  I just want to make sure that we're somewhere in
    the same neighborhood.*

    I then wait a bit, and typically the candidate either ...

    1.  Just tells me what they're making now
    2.  Gives a general range for what they'd expect someone in this role could make
    3.  Does a hard-pass (although this is surprisingly rare)

    Most often there is also a conversation at this point about equity,
    vacation expectations, other benefits, which is good to have.  I'm also
    open to sharing a broad distribution of what our engineers make.

3.  **Possible start date**

    Some folks have long notice periods (looking at you Europeans) others just
    got let go and want to start next week.

## Next steps

If I'm leading the process I'll maybe mention a few folks that I'm going to
want them to meet.  If I'm not leading the process I say "I'm going to share my
notes with the team and the person who's leading this process should get back
to you shortly after your last interview".

## Timing

Speed is key.  Especially in tech.  Especially in startups.  Sometimes we're
great at this.  Sometimes we're terrible.  It's always something to work on.
Some tips:

1.  Early-reachout once they apply, if only to acknowledge the application
2.  Panel interviews with lots of folks at once
3.  Pre-schedule a meeting with the interviewing team for right after their
    last interview

