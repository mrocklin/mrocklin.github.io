---
title: Stability Bias
tagline: Optimizing for past and future users
date: 2022-12-02
blogpost: true
author: Matthew Rocklin
category: engineering
---

Stability Bias
==============

We often optimize more for current users than future users.

Stability often arises as a concern when proposing changes.  I often hear
statements like the following:

-   *We're seeing some performance regressions so we shouldn't release*
-   *We shouldn't include this breaking API change because it might confuse existing users*
-   *We can't remove that feature because it's used by group X*

These statements are common in managing software and are often used to motivate
not deviating from the stable norm.  However, they discount the benefits of
moving forward.  One might respond as follows:

-   **Concern:** *We're seeing some performance regressions so we shouldn't release*

    **Response:** We're also seeing many more performance enhancements.
    By not releasing we're accepting regressions in reverse.

-   **Concern:** *We shouldn't include this breaking API change because it might confuse existing users*

    **Response:** But this API is confusing as it is.
    By not making this change we're making things confusing for new and future
    users.

-   **Concern:** *We can't remove that feature because it's used by group X*

    **Response:** But that feature slows down all of our development.
    By not removing it we're rejecting the improvements we could make by being
    more efficient and nimble.

Making these decisions often comes down to determining the ratio of current to
future users you have, and how much you value future users.

Valuing Future Users
--------------------

Most design decisions include some trade-off.  Mostly I want people to weigh
and value future users when making these calculations.  This isn't easy or
natural to do.

Stability mindsets mostly value current users.  This is a common mindset
because we get much of our perspective from current users.  Future users don't
have much of a voice.

This is common in tech, but also in government, public
policy, etc..  Imagine if future generations could vote today on climate
change policy, or future residents of a city could vote on high
density residential zoning laws.

Evolve Into Stability
---------------------

Stability does have inherent value though.  Being the project that existing
users can rely on long-term is useful.  My sense is that most project should
start off with a strong bias towards dynamism and having broad impact,
especially when the current user count is far smaller than the potential user
count.  And then, as the project becomes more adopted, it should crystallize
and become more stable.

If your project is young and has captured only a small fraction of the
possible userbase then I think that one should embrace dynamism and rapid
evolution over stability.  This will, over time, improve overall user
satisfaction.
