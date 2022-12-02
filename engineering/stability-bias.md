---
title: Stability Bias
tagline: Optimizing for past and future users
date: 2022-12-02
---

Stability Bias
==============

We often optimize more for current users than future users.

Stability often arises as a concern when proposing changes:

-   *We're seeing some performance regressions so we shouldn't release*
-   *This API change might confuse existing users*
-   *We can't remove that feature because it's used by group X*

These statements are common in managing software and are often used to motivate
not deviating from the stable norm.  However, they discount the benefits of
moving forward.

-   **Concern:** *We're seeing some performance regressions so we shouldn't release*

    **Response:** We're also seeing many more performance enhancements.
    By not releasing we're accepting regressions in reverse.

-   **Concern:** *This API change might confuse existing users*

    **Response:** But this API is confusing as it is.
    By not making this change we're making things confusing for new and future
    users.

-   **Concern:** *We can't remove that feature because it's used by group X*

    **Response:** But that feature slows down all of our development.
    By not removing it we're rejecting the improvements we could make by being
    more efficient and nimble.

Valuing Future Users
--------------------

Most design decisions include some trade-off.  Mostly I want people to weigh
and value future users when making these calculations.

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
start off with a strong bias towards dynamism and having broad impact, and then
should eventually crystallize and become more stable, and then should eventually
die.

If your project is young and has captured only a small fraction of the
possible userbase then I think that stability bias is not an optimal strategy.
