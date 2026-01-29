---
title: Multi-Agent Workflows
date: 2026-01-29
tagline: Initial Thoughts
description: Exploring multi-agent AI workflows—what works, what doesn't, and lessons from playing Diplomacy with Claude agents.
blogpost: true
author: Matthew Rocklin
---

# Multi Agent Swarms: Initial Thoughts

Like many of us, I read articles about systems like [Gas
Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) with a
mixture of wonder and fear:

> I'm only using a few agents concurrently!  Am I falling behind?

This is silly of course.  No one is behind because [no one knows what they're
doing yet](/ai-beginners).

Still though, I wanted to explore this topic, so I spent the last couple days
playing with multi-agent workflows using [Claude
Chic](/introducing-claude-chic).

This article is long (sorry!) but here is a helpful TOC.  If you don't feel like a long read I recommend skipping to the [Lessons Learned](#lessons-learned).

1.  [Obviously Good Simple Multi-Agent Workflows](#obviously-good-simple-multi-agent-workflows)
2.  [Platform](#platform)
3.  [First Experiment: Diplomacy](#first-experiment-diplomacy)
4.  [Second Experiment: Session Viewer](#second-experiment-session-viewer)
5.  [**Lessons Learned**](#lessons-learned) <-- if you read only one section, read this
6.  [Experimenting is easy](#experimenting-is-easy)

## Obviously Good Simple Multi-Agent Workflows

Many of us use multi-agent systems in simple ways that are clearly a benefit:

-   **Plan then Build:** People often have one session make a plan, and then clear out context and start building that plan with a new session.

    This has become common enough that I believe it's now the default in Claude Code.

-   **Review:** People ask another agent to review the work of an initial agent.  This tends to produce better results than having the original agent self-review.

    As Wes McKinney writes about [RoboRev](https://www.roborev.io/):

    > Having a Claude Code session review its own work is so 2025.

There's something powerful about having two different agents think about the
same problem and communicate about it, even if those two agents run sequentially, and even
if they communicate by having a human copy-paste between them.

## Platform

I'm using my personal Claude TUI alternative, [Claude Chic](/introducing-claude-chic).
Originally built for nicer style, it also has the feature set needed to support multi-agent swarms.

-  **Start:** Agents can start other agents
-  **Send:** Agents can send messages to other agents
-  **Branch:** Agents can create git worktrees
-  **Merge:** There's an automated commit / rebase / resolve-conflicts / merge loop that
agents can follow

I built these tools to help me with human-in-the-loop work, but it turns out
they're all you need for multi-agent-swarm workflows.

## First Experiment: Diplomacy

In the initial demo of Claude Chic, I show Claude setting up a game of Chess against itself.

<video src="https://github.com/user-attachments/assets/735ebc91-335e-4476-8fde-f49ce1df056a" autoplay loop muted playsinline style="max-width: 100%"></video>

But then I thought

-   **Q:** "what's more intense than Chess?"
    **A:** "Diplomacy"

Diplomacy, if you're not familiar, is like "Risk on Steroids without Dice".
It's a game of pure discussion and guile where seven players try to dominate
1908 Europe.  Claude knows the game (of course) and so I asked it to set up a game among agents.

<video src="https://github.com/user-attachments/assets/38205b08-fd13-4b84-b153-9f98eab1d759" autoplay loop muted playsinline style="max-width: 100%"></video>

The gameplay was fascinating to watch.  Briefly:

-   Game starts out tame and typical
-   Austria thinks it's doing well, but everyone betrays it

    Interestingly, the other players joke about Austria behind its back

-   Russia dominates early on, supported by Turkey

-   Germany, noticing Russia's rise, convinces everyone else to gang up against Russia

    The amount of inter-agent traffic in and out of the Germany agent during this period was intense.

-   Russia, cowed, makes a deal with Germany to let it survive

Watching the agents play was no less fascinating than watching humans play, and
resulted in behaviors I found surprising from AI:

> Multiple coordinating agents are capable of more sophisticated behavior than single agents

Silly game, useful lesson.  I wanted to try things out in practice.


## Second Experiment: Session Viewer

I wanted to look at multi-agent sessions like the one I had just played, and so
decided to have Claude(s) build a session viewer for me that I would turn into
something with a shared timeline.

I tried this three times with three different prompts, learning each time.
Eventually we got to something like this without much human intervention:

![Simple Session Viewer](https://github.com/user-attachments/assets/247ad909-72ae-4365-8559-3e21d63153f6)

It's not great, but it works.

### Prompts

They're not beautiful, but here are the prompts I used.  You can tell how I learned from one into the next.


??? faq "First Try"

    I'm curious about trying an agent swarm technique in development. I was thinking as a project we might try adding a react electron version of this application.

    We'd want to have one agent (you) doing a lot of the orchestration, but we'd want other agents for planning, executing each task, reviewing, testing, etc.. You wouldn't do any work directly because you'd be conserving your context to control others.

    I want you to think hard about this and how to execute well.

??? faq "Second Try: I encourage communication"

    Let's play with multi-agent swarm systems. As a project, I want to build a viewer for sessions. I'm thinking that this is probably a local application, maybe electron that takes a session file and renders it nicely. Eventually I'm going to want to render a few of these side-by-side (to better understand multi-agent systems), but I think that to start we probably just want to get to a milestone where we have an app that runs that can present a session nicely.

    For tech we're going to want react/shadcn/tailwind with zustand for state.

    For design we're going to want to copy our theme and styling here.

    For execution I think we probably want different agents for planning, building, and reviewing. Each building agent should also launch an agent to review its work as it gets close to done (or we should launch it if it forgets). Assuming we use worktrees we're going to want to merge work as it completes rather than all at once. Probably we want a separate integration agent for this. Agents should be encouraged to ask each other questions and collaborate. We shouldn't do much work in this agent. We need to preserve our context.

    Think about how best to organize this and then set it going.

??? faq "Third try. I wanted to limit concurrency."
    I'd like to experiment with agent swarms.

    As a project, I'd like us to build a session viewer that takes in a session, like the .jsonl file on the Desktop, and renders it similarly to how we do in the app, but with an electron app using react/tailwind/shadcn.

    As we work on things I want you to use different agents in different roles.

    -  For our architecture I suspect that we'll want an agent to make an overall plan,
    -  and then we'll want to break apart that plan into a set of tasks with dependencies that agents can work on independently.
    -  We won't want to start everything at once of course. We'll want to pay attention to laying a good foundation first and making sure it's good before moving on.
    -  As we can parallelize we will.
    -  Also, as any agent starts to finish up work they should use the /review skill to create another agent to review their efforts.
    -  When they're done they should use the finalize_worktree mcp command to work on merging their work to this upstream viewer branch, which will be the target of all of our work.

    You won't do much work, instead saving your context to help orchestrate the other agents.

    Think hard about how to do this well.

If I were to do this again, I think I would sequentialize the entire process.  Parallelism didn't buy much.

### The overall experience was mediocre

My experience with agentic swarms was so-so.  That's not surprising.  I'm new at it and bad at it.

As Steve Yegge (famed multi-agent vibe coder) says:

> You will turn into Batman, but you can't just put on the suit and say "I'm Batman".

> You've got to learn how the tool-belt works

My experience was learning that I'm definitely not Batman yet.

### Observations

The head agent delegated really well.  It understood that its context was
precious and how to create agents to do work.  And the plan that was designed was fine.

But parallel execution was generally pretty bad.  The agents did fine work, but
they mostly ignored each other the first go around.  The second time I
intentionally prompted the system to chat with peers about the work they were
doing, and the third time I encouraged less parallelism.  Still though,
lack of coordination resulted in lots of strangeness.

On the plus side, the crap it produced was quickly cleaned up by more AI (the
solution to AI problems is more AI).

## Lessons Learned

As with any philosophy, we should neither accept nor reject it, but should take
from it the parts that suit us.

In that spirit, here are my current lessons on multi-agent behavior.

### Separate Reviewer 👍

Upon finishing work I used to ask Claude to review its own work:

> Let's review our recent changes and see if there is anything we can clean up or simplify

Now I still do that, but I follow up with:

> Start another agent and ask it to review our work

They're both quite useful.

### Fresh Perspective 👍

Agents get tired.  If an agent finishes an especially long session and its context is near 60-70% I'll often ask the reviewing agent to take over and implement the changes.

It's better, of course, to avoid this with well-scoped work, just like a regular human developer.

### Mythical Man Month ➡️ Mythical AI Minute

Also like humans, sometimes teams don't perform as well as single developers.

There's a real cost to coordination that needs to be outweighed by the benefits of speed.  AI agents are so fast that it's not clear to me when we'd want multiple agents working concurrently on the same code—most tasks finish before coordination overhead would pay off.

My experiment would have been better with many agents, each agent running after the other finished.

### Agent Support 👍

Increasingly, the model I have for hard problems is to work with one key agent at a time, and fire off supporting agents to handle tangential work (research, review, performance testing).

It's valuable to keep a key agent on task. (also like humans)

### Human Coordination 🧠

I am not (yet) a fan of YOLO Swarms.  I want to be involved.

Said differently, all the work I'm doing is sufficiently important to me that I'm happy to pay attention to it.  I'm curious about how to best optimize my ability to pay attention to AI work.

I don't think this is universally true.  For example during Dask's peak, OSS maintenance was such that I would have welcomed agents handling the first layer of support.  Very few of us are in that situation though.

### Human-Oriented AI Development

Working on Claude Chic has made me increasingly interested in how I work as a developer, and how to optimize that experience.  Rather than ask:

>  How can I use multi-agent swarms?

I am instead asking:

>  What is holding me back right now?

>  How can I best address that?

Today the answer is around ergonomics and context management rather than concurrency (I feel I already have concurrency in abundance).  There are great multi-agent workflows I've mentioned above that I use daily.  I'm not yet a YOLO Swarm / Gas Town guy.

I haven't really made up my mind though; I should experiment for more than 48 hours.

## Experimenting is easy

This is a blatant ad for [Claude Chic](/introducing-claude-chic), but it was pretty trivial to play with (admittedly bad) swarm architectures.

Claude has enough of an understanding of swarms that, if you describe what you want and give it the ability to make agents that talk to each other (like Claude Chic does), then you can just start playing immediately.

Regardless what you think about AI, and regardless how you think about
full-auto multi-agent swarms, you should experiment with them.  They are,
whatever else, quite interesting.
