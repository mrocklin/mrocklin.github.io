---
title: AI Zealotry
date: 2025-12-31
description: How I write with AI today
blogpost: true
author: Matthew Rocklin
---

# AI Zealotry

I develop with AI today.  It's great.

There are many articles you can read on why AI is great (or terrible) or how to
use it.  This is mine.  I focus on the experience of a fairly senior engineer
(and why we in particular should use it), on my experience operating within the
OSS Python Data world, and on practical suggestions that I've found myself
repeating to colleagues.

This article contains learned lessons of two types:

-  **Big Ideas:** Grand(iose) philosophy on why AI is great for experienced programmers
-  **Tips:** Taken from my workflow using Claude Code

We'll interleave these two.  I'm hopeful that this approach will make this more fun.

## Why AI

AI development is more fun.  I do more of what I like (think, experiment, think
more) and less of what I don't like (wrestle with computers).

I feel both that I can move faster and operate in areas that were previously
inaccessible to me (like frontend).
Experienced developers should all be doing this.  We're good enough to avoid AI
Slop, and there's so much we can accomplish today.

I like this quote from [this blog](https://www.stochasticlifestyle.com/a-guide-to-gen-ai-llm-vibecoding-for-expert-programmers/)
> I get it, you’re too good to vibe code. You’re a senior developer who has been doing this for 20 years and knows the system like the back of your hand.

> ...

> No, you’re not too good to vibe code. In fact, you’re the only person who should be vibe coding.

I think that really good engineers, the kind that think hard before writing,
can have a tremendous amount of impact and fun while developing with AI.  I
wouldn't ever want to go back.

## Why Not

That being said, there are some serious costs and reasonable reservations to AI
development.  Let's start by listing those concerns:

-   LLMs generate junk
-   LLMs generate *a lot* of junk
-   Writing code ourselves builds understanding
-   Reviewing code for correctness is the slow part, not writing it
-   AI workflows are dehumanizing, just pressing "yes, allow" over and over again

These are super-valid concerns.  They're also concerns that I suspect came
around when we developed compilers and people stopped writing assembly by hand,
instead trusting programs like `gcc` to pump out instruction after instruction
of shitty machine code.

We lost a deeper understanding as developers when we stopped writing assembly
but we gained a ton too.  As in any transition, we need to navigate the
situation to capture the advantages while losing only a little, balancing the
costs and benefits of a new technology.

This article is how I've been navigating this transition personally.

## Big Idea: Minimize Interruptions / Climb Abstraction Hierarchy

Early in using Claude Code (or Cursor) many of my interactions were saying
"Yes, it's ok to run that".  This was **frustrating and dehumanizing**.  Mostly my
job was to enable AI, rather than the other way around.

There are many tricks to resolve this (see below), but more broadly **"stop doing
simple shit"** has been a mantra that I've found myself constantly coming
back to. The more I reject simple tasks and add automation to my workflow, the
higher an abstraction I'm able to climb to and the more effectively I'm able to
work. Our goal in programming is to climb an abstraction ladder and gain more
intellectual leverage. This requires thought and consistent attention.

Fortunately AI can help with this.  If you complain and say "I'm always doing
X" it'll suggest solutions like what I'll talk about below, but more tailored
to your situation.


## Tip: Hooks

AI developers, like human developers, benefit from structure.

Most people start with an `AGENTS.md` or `CLAUDE.md` file.  This is a great
start, but I find that the AI agent often forgets what's in there.  The real
solution here (at least for Claude Code) is Hooks.

First, let's outline a couple of annoyingly common problems.

### Example Problem: Ignoring instructions in CLAUDE.md

Let's say you tell AI that you want to run tests with `uv`:

> when running tests, use `uv run pytest tests`

While this works sometimes, it often decides to run

```
$ pytest tests/
command not found: pytest
```

While the agents read CLAUDE.md, they don't always follow the instructions.
And so you're stuck saying "no, use `uv`"  over and over again. Gah.

### Solution: Hooks

Here's a hook that catches pytest commands missing uv run.  You could put
something like this in `~/.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python ~/.claude/hooks/check-uv-pytest.py"
          }
        ]
      }
    ]
  }
}
```

```python
#!/usr/bin/env python3
import json
import sys

data = json.load(sys.stdin)
cmd = data.get("tool_input", {}).get("command", "")

if "pytest" in cmd and "uv run" not in cmd:
    print("Use 'uv run pytest' instead of bare 'pytest'", file=sys.stderr)
    sys.exit(2)
```

There, we've just automated that annoying task for you forever.

I don't actually do this though (I allow Claude to fail and then it finds the
right approach.)  Mostly this works because I've gotten good at giving Claude
fairly broad-yet-safe **permissions**, which is coming up next.

### Example Problem: Incomplete Permissions

Even worse, Claude often asks for permission to do things that are just
slightly different from what you've already granted.
You allow `uv run pytest *`, but Claude keeps finding variants:

```
timeout 60 uv run pytest ...
timeout 40 uv run pytest ...
uv run pytest ... | head
.venv/bin/pytest ...
```

Claude Code's permission language sucks.  It only supports prefixes, while we
wish it could handle regexes, or maybe even just arbitrary Python code.

### Solution: Hooks for permissions

I have a complex Python script as a hook which overrides the permission
system.  It uses regexes, but also arbitrary Python code as logic.  This allows
me to encode arbitrary combinations of rules.  It's great.

On the rare occasion when Claude asks me for permission for something totally
safe, I ask Claude to update the permission script accordingly.


### Solution: Hooks for sounds

My personal favorite hooks though are these:

```json
"Stop": [
  {
    "hooks": [
      {
        "type": "command",
        "command": "afplay -v 0.40 /System/Library/Sounds/Morse.aiff"
      }
    ]
  }
],
"Notification": [
  {
    "hooks": [
      {
        "type": "command",
        "command": "afplay -v 0.35 /System/Library/Sounds/Ping.aiff"
      }
    ]
  }
]
```

They play subtle little sounds whenever Claude is either done, or needs input
from me.  This lets me ignore Claude when it's busy.  Previously I found that I
was constantly checking back in with Claude to see if it was done, and that
action was dehumanizing, so I automated it by asking Claude to play a sound.

Hooks are great.  There are more ways to provide structure (Skills, Commands)
but I've found that Hooks are the most dependable, a great starting place, and
often augment any other structure that I put in place (like Skills).

## Big Idea: Build Confidence Without Looking at Code

In a recent large PR of mine a somewhat frustrated reviewer said the following:

> To me, this [size of PR] implies that either

> - reviewers should blindly trust Claude, or
> - reviewers should spend the months worth of effort going through Claude's changes, without the developer bothering to do the same first.

It's a valid problem, even in single-person projects.  **We're able to generate
code far more quickly than we're able to read it**.  How should we handle
review?  Everyone needs to figure this out for themselves, but my answer is
"find other ways to build confidence".

We already do this today with human-written code.  I review some code very
closely, and other code less-so.  Sometimes I rely on a combination of tests,
familiarity of a well-known author, and a quick glance at the code to before
saying "sure, seems fine" and pressing the green button.

Trusting code without reading all of it isn't new, we're just now in a state
where we need to review 10x more code, and so we need to get much better at
establishing confidence that something works without paying human attention all
the time.

We can augment our ability to write code with AI.  We can augment our ability
to review code with AI too.

## Tip: Self-review

### Testing

Mostly I establish confidence on AI-generated work by investing heavily in
tests and benchmarks, the same as I would with humans, just moreso.  TDD is
baked into most of the prompting structure I have with agents.

Remember that this is way cheaper than it used to be.  Now rather than write a
benchmark I can type

> How does this compare in performance to the old version?  I'm particularly
> interested in memory use.

And that's it.  If it's bad, the agent will say so (and then probably go work
to make it good).

### Grilling

Additionally, if I'm nervous about something subtle like "Is it possible this change
might unexpectedly affect performance in this other feature?" then I'll ask the
AI exactly that question:

> Is it possible this change might unexpectedly affect performance in this other feature?

And it'll just go and investigate exactly that question.  Unlike human authors,
the AI has no ego at stake in its work, and isn't in the least bit lazy.  It's
our job to ask "have you thought of X" and its job to go learn if that might
be an issue.  Don't trust its answer?  Ask it to prove it to you.

AI has flaws, but it is diligent, and it lacks ego.  If you question it, it'll
investigate thoroughly and critique its own work honestly.

### Simplifying

Also, my favorite command:

> Let's review our work and see if there is anything we can simplify or clean up

Before Opus 4.5 came out this was essential.  Now it's merely nice.  I've
turned this into a `/cleanup` command and integrated it into most of my Skills
as a final phase in development.

### Tech debt

From time to time I also ask a fresh agent to do a full review of the project,
with an eye to cleaning up technical debt.  I tell it to review everything and
think hard.  It takes a while, but it often comes back with a nice list of work
for itself, which it then of course diligently performs.

AI creates technical debt, but it can clean some of it up too.
(at least at a certain granularity)

## Feedback

In general we want to give our agents good automated feedback.  Tests do this,
benchmarks do this, prompting them to assess themselves does this, asking them
to explain things to us and have us weigh in on high level topics does this.

LLMs are smart enough today that if they're given enough of the right feedback
they converge to a good solution as-well-or-better-than a senior human engineer
(that's my experience at least).

Our job is to construct a system that gives them the right feedback at the
right time, hopefully without our intervention.  This is the same job we have
when we build human teams; now it's just more important to do well.

## Cursor vs Terminal Tools

I started AI development with Cursor.  It was great having the AI experience
inside a VSCode-like editor, where I could see everything that was going on.
When I saw terminal-based tools like Claude Code I
thought "whoa, that doesn't seem sensible, I need to see what's going on".

Today I code with Claude Code, `git diff`, and occasionally `vim`.  I don't
feel a need or desire to OK every change in the diff.  I've got more important
things to do.  I suspect that you do too.

## Big Idea: Drop Python. Use Rust and TypeScript.

I deeply respect the philosophical position of Python, which I'll state as
follows:

> Prioritize human performance over compute performance.

> By optimizing for ease and iteration speed we're able to search solution
> space more broadly and more quickly, finding *much* better solutions, making
> that 100x drop in performance negligible.

Python was a bold bet, and a bet that paid off amazingly well.  No one expected
this silly dynamic language originally designed for education to become the
world's juggernaut in performance software.

With AI though, the usability benefits of Python no longer apply as strongly,
and we're more free to choose different ecosystems.

Personally, I use ...

-  **Rust** for computational development, using PyO3 to connect to
Python, where I still do most of my testing
-  **TypeScript** for frontend development, which I'm leaning into more deeply

Regarding TypeScript, I still love easy interaction tools like `rich` and
`textual`, but when the entire React ecosystem is a sentence away and when you
get to use things like, you know, fonts, there's really no comparison.  Every
computational developer should learn React, and we should put dashboards on
everything.

Of course, I still hook into Python for the ecosystem.  Everything is
Python-importable and I still use the protocols and design patterns developed
by the Python data community.  Those are the durable assets of Python.  Not the
code or the language; those will die.  Rest in peace dear friend.

## Big Idea: Think Hard.  Write Clearly.

As an introductory project, I rewrote [Numpy in Rust](https://github.com/mrocklin/rumpy).
It was great fun.

It was also much easier than I expected (I expected it to be impossible).
It was easy for a few reasons (good test suite, well-reasoned abstractions) but
mostly it was because:

> **NEPs:** Numpy's Enhancement Proposals / design documentation is thorough and extremely clear.

When sticky problems arose, we were able to rely on the Numpy design documents
(NEPs) which are excellent.

The Numpy team **thought hard** and **wrote clearly**, two hallmarks of
excellent developers.  This made the job of implementation relatively trivial.
The Numpy development community is famous for doing this well.  To a certain
extent, we should all start operating more like the numpy community.

## Tip: plans/ and designs/ directories

Reading on Reddit, I think that this is common, but I keep two directories in
each repository,

-  `designs/` which contains brief motivation and high level design of a feature
-  `plans/` which contains ephemeral planning documents that the LLMs work through over many sessions as they implement a major feature.

Plans end up being very useful during development, while designs end
up being useful to point other agents to in the future.

In longer lived projects I've started to migrate away from `designs/` and
towards using Claude Code's Skills (context that gets automatically loaded in
based on the topic at hand) but I'm honestly still learning how I like to work
here, so I don't have anything to say here with confidence.

## Big Idea: Take Long Walks

Historically software engineers had to both think well and execute well.
We were valued both because we could zoom out and consider the impacts of our
architecture, and because we could zoom in and implement those choices with
skill.

**Our ability to zoom in and implement code is now obsolete.  Our ability to zoom
out and think well is not.**  On the contrary, our ability to think well is now
10x more valuable than it was before, because implementation is now mostly
free.

And so it's now more important than ever to hone our craft of thought.  This
probably means less caffeine and more walks through the park.

## Final Thoughts

The craft of authoring code has transformed time and time again during our
lives. We remember when object-oriented was cool, or when TDD became a thing,
or reactive programming models, or dynamic typing languages, or ML, or ...

As programmers we've opted into a system which changes by its very nature.
**Our job is to automate our job**, and to continuously climb the ladder of
abstraction.  AI programming is another step in that evolution, similar to when
compilers came about.  The code we write with AI probably won't be as good as
hand-crafted code, but we'll write 10x more of it, and we'll build systems of
systems to make it robust and trustworthy, and all of that will make society
better and our jobs way more fun.

I'm looking forward to having way more fun.
