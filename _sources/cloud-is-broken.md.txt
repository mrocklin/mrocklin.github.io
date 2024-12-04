---
title: Cloud Computing is Broken
date: 2024-12-03
description: Let's strive towards excellence on boring problems
blogpost: true
author: Matthew Rocklin
image: 3
---

# Cloud Computing is Broken

```{admonition} Famous Quote

*This AWS API is so intuitive it’s fucking awesome.  My entire team uses it.*

*-– no one ever*
```

## Introduction

Recently I was chatting with an investor about the market and they asked:

> ***What do you see coming** for the world of Data/Cloud/Compute Infrastructure?*<br/>
> *Is there some new dataframe library?*<br/>
> *LLM applications?*<br/>
> *What hunger are you seeing on the ground?*<br/>

My answer, after thinking about it for a while, was this:

> *Boring shit.*<br/>
> *The people I talk to struggle most with the **basics of cloud computing.***

This article explores this answer in more depth, drawing on undelivered promises, and the launch of the iPod.

## Promise of Cloud Computing, Undelivered

The promise of cloud computing for data developers goes like this:

- Infinite scalability
- Any place any time
- Turned on in about a minute
- Pay for only what you use
- No need to maintain hardware

This promise is valuable to companies today.  Developers want this.  Companies need this.  Especially those people for whom SQL doesn't suffice and who have to roll their own computations.

Yet most developers we see either don’t use the cloud, or don’t use it well.
We see two common architectures today:

::::{grid} 1 1 2 2
:::{grid-item} **Overused Big VM**

- They get one Big VM
- They leave it on all the time
- Maintenance needs are surprisingly demanding
- It’s really expensive

:::
:::{grid-item} **Underused Kubernetes Cluster**

- They deploy Kubernetes
- Experts use it for 1-2 applications
- Normal users never really get on board
- Maintenance costs and non-use eventually kill it

:::
::::

What people want is simple.  They want to turn on a bunch of computers, run arbitrary code on those computers, have those computers turn off reliably, and eventually get logs easily.  They want user and cost management without having to set much up.

## Don’t AWS/Databricks/Sagemaker already provide these features?

*But this stuff already exists, right?*

On paper, yes.  AWS Batch/Lambda, Databricks jobs, Snowflake’s Snowpark all provide arbitrary code execution on lots of ephemeral machines with exactly those features.
In theory, they deliver on this promise.

However in practice we don’t see this.  People are still rolling their own with the EC2 and EKS APIs.  I’ll bet that if you surveyed data professionals in organizations with access to modern compute platforms you’d find that the majority who would want to use such a tool don’t use them regularly. I’d guess penetration is in the 10-20% range.

Providing functionality is easy.  Making functionality useful is hard.

Cloud computing today is like MP3 players before the iPod.

- Huge potential demand (mp3s were everywhere)
- Theoretical delivery of that product (many products on the market)
- Complete market failure to actually deliver on the promise.

## MP3 Players and the iPod

*MP3 players existed, but only kinda.*

Imagine you’re Steve Jobs and you want to propose the iPod in year 2000.  Your marketing team tells you that the iPod isn't innovative.  Loads of MP3 players are already on the market and doing poorly.

Anyone above the age of 35 knows this history.  Recall the RIO 500 and Archos Jukebox.

::::{grid} 1 1 2 2

:::{grid-item} **Rio 500**
```{figure} https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Rio_500.jpg/1280px-Rio_500.jpg
:width: "73%"
```
:::

:::{grid-item} **Archos Jukebox**

```{figure} https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/B%C3%A4rbar_mp3-spelare_Archos_typ_Jukebox_6000.jpg/1280px-B%C3%A4rbar_mp3-spelare_Archos_typ_Jukebox_6000.jpg
:width: "70%"
```
:::

::::

They store songs, let you play them, fast forward, rewind, and show you what’s going on.  On paper they do everything the iPod will do, and yet market penetration was tiny, less than 1% of what it would be.  Looking at the lack of success of these products you’d conclude that humans don’t like listening to music.

*The majority of people who would have wanted an MP3 player didn't use any of these products.*

Eventually, the iPod was released, and it changed our listening habits forever

```{figure} images/ipod.png
:width: "60%"

iPod Generation One delivered the same functionality, but designed well enough for everyone to want.
```

Same exact functionality, just better in an indescribable and yet obvious way.  The combination of ease of use, pocketability, storage capacity, iTunes integration, and straight-up style made the iPod a must-have item years after equivalent products launched and failed to create and claim the market.

## Compute Technology has Outpaced UX and Adoption

*We as a technology movement have gotten ahead of ourselves.*

I believe in the innovation of the Startup \+ VC process.  Yet I think that in striving to climb the technology sophistication ladder (cloud computing \-\> ML \-\> Model management \-\> LLMs \-\> Agentic systems) we’ve outpaced our users and their ability to follow us.

We’ve chased the few truly sophisticated users out there, the geeky early adopters, rather than the majority of ignorant humans we should be serving.  We’ve been building for Steve Wozniak.

<iframe width="560" height="315" src="https://www.youtube.com/embed/hFD3tZSB7l4?si=kG3kKKMYgPclekjQ&amp;start=183" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Watch 50s of the video above about Steve's cool watch. <br/>
Then see ChatGPT explain how to run "Hello, world" on AWS Batch below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Xk_lEt_08Hs?si=7yM7Fi1VIxLvGGcx" title="YouTube video player" frameborder="0"               allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;    picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

No compassionate human can watch that and think "Yes, the potential of the cloud has been realized".<br/>
We're not done innovating yet.  There's more to do.

## Where does this lead us?

*Let’s strive towards excellence on boring problems*

I think that there’s huge untapped potential in solving some of these boring
problems well.  This work is hard and finicky, but I think the data
infrastructure space has pushed sufficiently far ahead that we've built up
substantial potential behind our frontier.

I’d love to see UX become as strong a focus as AI for the industry.  I’d encourage technology leaders everywhere to ask the following question:

> What important and common problems today lack products that inspire rabid loyalty?

Those problems may be ripe for iPod-style solutions.<br/>
Cloud and compute platforms are certainly among them.
