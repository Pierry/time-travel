# The recorded terminal session

The clip at the top of the README is this run: an interactive Claude Code session in a real terminal, recorded with [VHS](https://github.com/charmbracelet/vhs) from [`video/terminal/demo.tape`](../../../video/terminal/demo.tape).

| | |
|---|---|
| Date | 2026-10-25, 22:16:42 to 22:19:20 UTC |
| Claude Code | v2.1.310, interactive, `claude --plugin-dir <repo>` |
| Model | `claude-opus-5-5`, effort medium |
| Input | [`../plan.md`](../plan.md), typed `/time-travel:premortem plan.md` |
| Time on screen | "Cogitated for 2m 37s" |
| Gate | 7 `trip_lint` results, 7 `ok`, no repair round |
| Files | [`trip.md`](trip.md) as written by the run, [`reply.md`](reply.md) the final reply taken from the session transcript |

## Videos

| File | What it is |
|---|---|
| [`docs/demo-full.mp4`](../../../docs/demo-full.mp4) | the whole session in real time, 178 s, only the idle screen after the reply trimmed |
| [`docs/demo.mp4`](../../../docs/demo.mp4) and [`docs/demo.gif`](../../../docs/demo.gif) | the same session, 83 s: the four waits where only the thinking spinner moves are cut to 2 s each, with a label on screen saying how many seconds were removed (48, 27, 15, 6). Nothing is sped up |

Hidden from the clip: the shell setup line (clean environment variables, `TIME_TRAVEL_HOME=/tmp/nudge/.time-travel`, and an alias adding `--setting-sources project --allowedTools Bash Read Write Edit Glob Grep Skill` so no permission prompt and none of the recorder's personal settings enter the run).

This session and the headless run in [`../run.md`](../run.md) used the same plan and gave different text: 47 customers by April here, 17 there; a different checklist; launch moved to 2027-01-12 here, 2027-01-17 there. Both trips pass the same gate, which is the point: the wording varies, the structure and its checks do not.
