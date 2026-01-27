---
title: Introducing Claude Chic
date: 2026-01-26
tagline: Claude Code, but stylish
description: A Claude code drop-in with updated UX and multi-agent support
blogpost: true
author: Matthew Rocklin
---

# Introducing Claude Chic

[Claude Chic](/claudechic) is an alternative Claude Code UI that provides the following:

-  [**Style:**](#1-style) visually organizes the message stream for legibility
-  [**Git Worktrees:**](#git-worktrees) organizes concurrent worktrees
-  [**Multiple Agents:**](#multiple-agents) runs many sessions from the same window
-  [**Quality of Life:**](#quality-of-life) loads of other features like diff viewer, shell commands, and more

The official docs are [here](/claudechic), but I wanted to share my personal motivation and experience building this.

Or, if you prefer to jump right in, Claude Chic can explain itself:

```bash
uvx claudechic /welcome
```

<video src="https://github.com/user-attachments/assets/bbdae8ac-9ddb-455b-8282-b52cfb73c4e8" autoplay loop muted playsinline style="max-width: 100%"></video>


## 0. Motivation

I've been deep in AI joy/psychosis the last couple months.  The world is super fun right now.

However, as AI speeds up my workflow I find new bottlenecks, and increasingly those bottlenecks are part of my interactions with Claude itself.  I wrote about this in [AI Zealotry](/ai-zealotry); AI can feel dehumanizing when our primary contribution is administrative, like granting permission.

Beyond permissions, various administrative interactions with Claude became tiresome, and so I worked to improve what I could about the interface for my workflow so that I could feel more human.

Claude Chic is an early result of that endeavor.

## 1. Style

Let's start with visual design.  Claude is functionally great, but stylistically pretty terrible.

Here's a screenshot of Claude Code:

<img alt="Claude Code" src="https://github.com/user-attachments/assets/e6caa10a-0696-43f3-a1f3-10d9f620a389" style="max-width: 100%" />

I find this difficult to parse.  Everything feels muddled:

-   **No visual distinction** between messages
-   **Too wide** for comfortable reading (moreso in full-screen)
-   **Lost information** - I want to dig into edits before they get summarized away

We don't expect modern design in terminal applications, but maybe we should, especially with [Textual](https://textual.textualize.io/).

Textual made it easy to design a skin for Claude code that was, for me, much easier to consume.

### Comparison

To me, Claude Code looks muddled.

=== "Claude Code"

    ![Claude Code](https://github.com/user-attachments/assets/e6caa10a-0696-43f3-a1f3-10d9f620a389){ style="width: 100%" }

=== "Claude Chic"

    ![Claude Chic](https://github.com/user-attachments/assets/229f3904-4dee-4f97-8fc7-d65fb78ac9cd){ style="width: 100%" }

To me, Claude Chic organizes the conversation so my eyes can parse it immediately without feeling drowned.

Tool use in particular is interesting.  There are *more* tool use lines in the Chic version (Claude code omits many tool use lines), but they don't get in the way, and each is expandable for full context.

Additionally, Markdown renders properly.

=== "Claude Code"

    ![Claude Code expanded](https://github.com/user-attachments/assets/c09c35af-8f62-417e-b7d9-f9bc0f78070a){ style="width: 100%" }

=== "Claude Chic"

    ![Claude Chic expanded](https://github.com/user-attachments/assets/ebdee1a5-9700-4149-8e97-1fbe420852ca){ style="width: 100%" }

Key styling choices:

1.  **Color:** User (orange), Claude (blue), Tools (grey)
2.  **Expansion:** Tool messages collapse by default, click to expand
3.  **Width:** Constrained to 100 characters
4.  **Markdown:** Proper rendering
5.  **Streaming:** Responses appear as they generate

To be honest, this ended up being a deeper rabbit hole than I anticipated.  Totally worth it though.  We're still early (definitely beta software), but it feels much better to me than Claude's default interface, or similar tools like Codex, Gemini, and other CLI tools.  Everyone should be using Textual for TUIs.

## 2. Git Worktrees

Git worktrees are underused.  They let multiple Claude agents work on the same repository in parallel.

Unfortunately, none of us know how they work.  People I've spoken to have all seen an article or Youtube video showing them in action, but in practice they feel foreign.  That's ok; AI tooling is great at foreign workflows.

### User Experience

Previously, when I had a new idea it went on a TODO list while Claude finished its current task.  Ideas would linger on that TODO list for a *long* time, even simple and easy ones.  Coordinating the shared resource of the repository was an annoying bottleneck.

Git worktrees solve this by marrying a git branch with a fresh copy of the repository directory.

```
~/projects/
├── myrepo/            # Main worktree (main branch)
├── myrepo-feature-1/  # Some feature you're working on
├── myrepo-feature-2/  # Some feature you're working on
├── ...
└── myrepo-feature-n/  # Some feature you're working on
```

Now you can have `n` Claude agents working, one in each directory.  When I have a new idea, I create a new worktree and have Claude start on it immediately:

```
/worktree my-idea

I want you to explore ...
```

This creates a new worktree (directory + branch) and a new agent working in that directory in the background.  The agent starts working concurrently while I go back to my main task.  In practice I have 2-10 of these going at once.

Now I focus on whatever ongoing thread interests me most while Claude pushes the others forward.  I no longer wait for Claude; Claude waits for me.

### Cleaning up

With concurrent git development comes conflicts.  To address this, my git flow looks like the following:

1.  **Commit** work in a branch
2.  **Rebase** Rebase on our upstream branch (for linear history)
3.  **Resolve** any conflicts
3.  **Fast-forward merge** branch into upstream
4.  **Delete** worktree

Claude handles rebases and conflicts fine (and asks when it can't), so the workflow above got baked into the `/worktree finish` command.  Concurrent git managemet is, for me, fully managed now.

Now that all of my TODO items can run at once, worktrees shift the decision from "what thread should we start next?" to "which ongoing session most deserves my attention?"  This decision, coming later in the workflow, comes with more and richer information.

## 3.  Multiple Agents

Multiple agents run concurrently in one session and can talk to each other.  Here they play chess:

<video src="https://github.com/user-attachments/assets/735ebc91-335e-4476-8fde-f49ce1df056a" autoplay loop muted playsinline style="max-width: 100%"></video>

This is a cute demo, but in practice I use multiple agents with prompts like the following:

-  **Reviewing:** "Start an agent to review our changes critically"
-  **Research:** "Start an agent to explore this topic further"
-  **Dogfooding:** Recently when adding a profiler, I spawned an agent to use it and suggest improvements back to the agent building it

There are intense multi-agent systems out there like [Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) and [OhMyOpenCode](https://github.com/code-yeongyu/oh-my-opencode).  I haven't needed that level of automation yet, but I find this space interesting.

## 4. Quality of Life

Claude Chic comes with myriad other niceties like a `/diff` viewer, vim keybindings (`/vim`), shell commands (`!ls`, `!nvim README.md`), and more.

### Diff Review

Review uncommitted changes before asking Claude to commit:

<video src="https://github.com/user-attachments/assets/3c0c262b-2a23-4486-92c4-b97705a0819d" autoplay loop muted playsinline style="max-width: 100%"></video>

I used to switch back and forth to a terminal to run `git diff`.  Now I get something that I like more than `git diff` and without context switching.

### Shell Access

Run shell commands without leaving the UI:

<video src="https://github.com/user-attachments/assets/85f3dbe0-9a88-436e-aa9d-c1ba012c1f0e" autoplay loop muted playsinline style="max-width: 100%"></video>

I typically use this for `git log` and `vim`, but it's nice generally.

There are loads more small features in Claude Chic, and more coming daily.  It's exciting to work on.

## Relationship to other projects

Related (and more mature) work:

-  **Claude Code:** More robust.  Claude Chic uses the same [`claude-agent-sdk`](https://github.com/anthropics/claude-agent-sdk-python) logic as Claude Code.

-  [**OpenCode:**](https://opencode.ai/) Beautiful wrapper supporting any major LLM with its own agent logic.

-  [**Toad**](https://willmcgugan.github.io/announcing-toad/): LLM CLI in Textual by [Will McGugan](https://willmcgugan.github.io/), Textual's creator.

-  [Conductor](https://docs.conductor.build/): Mac App that provides many of the same features (design, worktrees, multi-agent)

## Alpha Status

This software is *early*, and *full of bugs*.  It crashes regularly when we encounter new situations.  Even-so, I encourage adventurous `claude` users to put it through its paces and [raise issues](https://github.com/mrocklin/claudechic/issues/new).  Development on this project is (as of 2026-01-25) extremely fast.

## Final thoughts

For users: AI is fast; we need to avoid becoming Amdahl's bottleneck.  Our developer tooling warrants a lot of reimagining today.

For LLM providers: Please check out Textual.  It's a great technology.  (I have no financial stake in Textual)

```bash
# If you use uv
uvx claudechic /welcome

# If you use pip
pip install claudechic
claudechic /welcome
```

## Video

If you prefer video, here's one of me explaining this project:

<div class="video-container">
<iframe src="https://www.youtube-nocookie.com/embed/2HcORToX5sU?autoplay=0&mute=0&loop=0&playlist=2HcORToX5sU" title="Claude Chic Introduction" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
