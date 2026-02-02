---
title: "Claude Chic: Week 2"
date: 2026-02-02
tagline: Plan swarms, themes, and performance
description: A week of plan mode, custom themes, performance optimizations, and the --yolo flag
blogpost: true
author: Matthew Rocklin
---

# Claude Chic: Week 2

*Unlike most of my writing, this post was largely written by Claude*:

It's been one week since we [introduced Claude Chic](/introducing-claude-chic), and adoption and development since then have been fun.

This week saw 75 commits from 7 contributors.  Broadly we saw the following themes:

-  Smoothing out UX rough edges

    When a project goes from single-user to many users there are always various rough edges to smooth out.  These included Linux and Windows keybindings, Native Windows support (not just WSL), bugs in `/resume` and `/plan`, and much more.

-  Multi-agent workflows

    I've been exploring this space recently and seeing what I like and don't like.  I'll describe some things that I like and built into Claude Chic just below.

-  Performance

    Running several long sessions concurrently stressed our use of Textual.  Various enhancments were made to smooth things out.

-   Quality of Life

    There are many small things that we added like support for custom themes, small screen / mobile support, and more.

Now, let's dig into some highlights:

## Multi-Agent Workflows

The headline this week is new ways to use multiple agents together.  The idea: having Claude debate itself produces more thorough analysis.

### Plan Swarms

`/plan-swarm` spawns multiple agents to debate implementation approaches before you commit to one:

```
/plan-swarm Add caching to the API layer
```

This spawns several agents, each exploring the problem from a different angle—one might advocate for Redis, another for in-memory caching, a third for a hybrid approach.  They present their cases to each other, debate, and often (but not always) come to consensus. You then pick the direction that resonates.

### Review Agents

```
/reviewer
```

This spawns an agent whose job is to critically examine your recent changes.  You mediate as they iterate toward agreement.

### Infrastructure

Full plan mode support landed via the SDK's `set_permission_mode`, with proper tool restrictions during planning and feedback when you reject a plan.

## Custom Themes

Claude Chic now supports user-defined themes.  The default dark theme works well on dark terminals, but many developers prefer light backgrounds.

```
/theme chic-light
```

Or define your own in `~/.claude/chic-theme.json`:

```json
{
  "name": "my-theme",
  "colors": {
    "user_border": "#ff6600",
    "assistant_border": "#0066ff"
  }
}
```


## The `--yolo` Flag

For sandboxed environments where you trust the agent completely:

```bash
claudechic --yolo
```

(Or `--dangerously-skip-permissions` if you prefer verbosity.)

This skips all permission prompts.  Use it in CI pipelines, Docker containers, or when you're feeling reckless.  The name is intentional—if you're using this flag, you should know what you're doing.

## Performance

Multi-agent swarms exposed performance bottlenecks.  Running 5-10 agents simultaneously revealed that we were doing far too much UI work for agents you weren't looking at.

Key optimizations this week:

- **Deferred updates**: Hidden ChatViews no longer process UI updates until you switch to them
- **Collapsed history**: Old conversation turns collapse into lightweight placeholders
- **Lazy loading**: Collapsible content only renders when expanded
- **CSS optimization**: Reduced recalculation during agent switching
- **Spinner fix**: The thinking indicator no longer triggers CSS recalc on every frame

The result: swarms of agents run smoothly without the UI becoming a bottleneck.

## Quality of Life

Smaller improvements that add up:

- **Immediate feedback**: Creating agents/worktrees shows instant visual response
- **Compact mode**: UI adapts to small terminal heights
- **Cross-platform shortcuts**: Keyboard bindings work consistently across Mac/Linux/Windows
- **Autocomplete**: `/worktree` and `/agent` commands now autocomplete existing names
- **Horizontal scroll**: Code blocks scroll horizontally instead of wrapping (#28)

## Bug Fixes

The usual parade of fixes, including:

- Windows exit warnings (#31)
- Session path encoding to match Claude Code (#20)
- Crash when pasting long text
- Nested tools getting lost after switching agents
- Various multi-agent stability improvements

## What's Next

This past week was mostly about people other than me trying Claude Chic and reporting issues with their workflow.  I expect more of the same.

Try it:

```bash
uvx claudechic /welcome
```

Or update if you already have it:

```bash
uv tool upgrade claudechic
```

[GitHub](https://github.com/mrocklin/claudechic) | [Docs](/claudechic)

## Contributors

**Code:**

- [Avi Newman](https://github.com/avinewman) - Windows compatibility
- [Christopher Lamm](https://github.com/chr33z) - plan mode fixes
- [David Dotson](https://github.com/dotsdl) - vim mode
- [Laura Martin](https://github.com/jumptable) - exit handling
- [surminus](https://github.com/surminus) - custom themes
- [theantichris](https://github.com/theantichris) - session path encoding, model settings

**Issues & Feedback:**

- [andrie](https://github.com/andrie) - WSL timeout
- [binduwavell](https://github.com/binduwavell) - subagents, small screen support
- [c0ffee0wl](https://github.com/c0ffee0wl) - auto-approve mode, collapsible tools
- [cderv](https://github.com/cderv) - Windows issues, worktree context, horizontal scroll
- [chandlervdw](https://github.com/chandlervdw) - MCP management
- [dcherian](https://github.com/dcherian) - keyboard shortcuts, agent switching, readline
- [GaborNyul](https://github.com/GaborNyul) - multiline input, SSO proxy
- [jeduden](https://github.com/jeduden) - paste crash
- [maartenbreddels](https://github.com/maartenbreddels) - branch name handling
- [quasiben](https://github.com/quasiben) - token doubling
- [rdubwiley09](https://github.com/rdubwiley09) - path defaults
- [sargunv](https://github.com/sargunv) - plan mode
