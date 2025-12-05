---
title: Python Support is Socially Complex
date: 2024-12-09
description: Ambiguity of responsibility makes support difficult for everyone
blogpost: true
author: Matthew Rocklin
---

Python Support is Socially Complex
==================================

Supporting a Python product is difficult because it’s hard to draw a line between your product and the rest of the ecosystem.  This creates confusion, especially when it comes to triage and attributing failure to one product or another.

When a complex product like a Python-based data workflow fails, most of the work in fixing it is in diagnosing the problem.  When the product is self-contained and supported by one company, like a car for example, it’s clear whose responsibility it is to diagnose and fix the problem.

However, when a product is complex and ownership is jointly distributed among many different responsible entities, diagnostics become fraught.  No individual entity has clear responsibility to solve any particular problem, and no entity has responsibility to triage the problem as a whole.

Easy Case
---------

When you buy a self-contained product, like a car, it’s obvious when a part becomes defective whose fault it is.  The entire car was assembled by the same manufacturer which takes full responsibility over all parts, so it’s clearly something to do with their work.

**Problem:** Have an issue with your car under warranty?<br/>
**Solution:** Take it to the dealer.

Difficult case
--------------

But in an ecosystem like Python, you use hundreds of tools simultaneously, each of which has complex interactions with each other, and each of which is managed by a different team.  It becomes difficult to attribute a particular failure to any particular tool.  The burden of diagnosis is on you.

This is like if you didn’t buy your car from a manufacturer like Honda or Ford, but instead assembled it piece by piece, having purchased parts from individual factories.  No individual factory is going to do the work to figure out why your car died until you prove that it was their part that was at fault.

**Problem:** Have an issue with the complex jumble of software systems you’ve glued together?<br/>
**Solution:** 😩

As an example, here is a recent support request and response from our support team:

### Example: Support Request

*I'm trying to get started with your product, however after pip installing I get the following error:*

*raise ClientConnectorCertificateError(req.connection\_key, exc) from exc aiohttp.client\_exceptions.ClientConnectorCertificateError: Cannot connect to host [cloud.coiled.io:443](http://cloud.coiled.io:443/) ssl:True \[SSLCertVerificationError: (1, '\[SSL: CERTIFICATE\_VERIFY\_FAILED\] certificate verify failed: unable to get local issuer certificate (\_ssl.c:1007)')\]*

*Could you let me know if you have a suggested solution to try? Thanks\!*

### Example: Support Response

… after some other back-and-forth with the user diagnosing their situation …

*It looks to me like HTTPS is broken for your local install of Python \- I don't think it's related to our product.  For example, I expect this would fail in the same way (you can check):*

```py
from urllib import request
request.urlopen("https://google.com").read()
```

*We generally suggest that folks not use the "built-in" MacOS install of Python for this kind of work. Installing Python with [miniconda](https://docs.anaconda.com/miniconda/) is my favorite option, but I'd probably need to know more about how folks on your team usually work with Python to make a good suggestion.*

### Example: Analysis

The user’s failure has absolutely nothing to do with our product, and yet we spent non-trivial time tracking down what was going on.  From the perspective of the people providing support, this felt like an abuse of the support relationship.

However, at the same time, the user is unlikely to be able to diagnose an issue like this on their own (SSL errors are not often taught in data-scientist school) and on the surface it totally appears to be related to our product.  It’s both totally reasonable for them to want help from us, and totally reasonable for us to refuse to help.  This causes tension on both sides.  This raises the question …

**Question:** Whose responsibility is it to triage complex issues?<br/>
**Answer:** Unfortunately, no one.  For users, this sucks.

What can you do?
----------------

Really big companies buy “Data Science” from large integrators and those large integrators take on responsibility.  However, in my experience, the support they offer is simplistic and rarely helpful.

More often, teams depend on the good will of support teams of the individual products they buy, along with lots of effort from within their own team.  This isn’t great, but can be ok if you’re both hardworking and nice about asking for help.

**Main lesson:** Be hardworking and ask nicely.

Support teams are made of people, and people everywhere enjoy helping other people (we’re genetically programmed to do this) especially people who have put in the work and are nice.

See [Craft Minimal Bug Reports](https://matthewrocklin.com/minimal-bug-reports.html), which gives tips on how to nicely ask for help in an OSS context.

Our approach
------------

We try to be nice and help when we have time (as happened in the SSL example above) but we assume no formal responsibility to help with problems that aren’t clearly the sole fault of our software.

Sometimes people get upset when we don’t spend the time to diagnose ambiguous issues and we all have to live with that outcome.  In those cases we typically back off from that client, or point them to this post to better clarify our understanding of support expectations.  Sometimes that leads to the client backing away (they need more consultative help) and sometimes it leads to a deeper paid support relationship.

Programming is cool because you can glue together lots of different systems and get a totally new and wonderful system out.  That’s also what makes programming really hard though.  Gluing together systems that were never designed to work together results in all sorts of unexpected interactions, and *Interactions* are the hard part of systems development.

We’re here to help navigate, but ultimately you’re responsible for the system you construct.
