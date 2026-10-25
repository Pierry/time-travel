# A real, unedited terminal session of time-travel, recorded with VHS.
#   vhs video/terminal/demo.tape
# Hidden setup: a clean folder with plan.md, trips written next to it, and
# Claude Code started with project settings only so the recorder's personal
# settings stay out of the run.

Output video/out/terminal.mp4

Set Shell "bash"
Set FontFamily "Menlo"
Set FontSize 18
Set Width 1600
Set Height 1000
Set Padding 28
Set Framerate 24
Set TypingSpeed 55ms
Set Theme { "name": "cloud-dancer-ink", "background": "#23211C", "foreground": "#F0EEE9", "cursor": "#E4572E", "selection": "#4A463D", "black": "#23211C", "red": "#E4572E", "green": "#8FBF7F", "yellow": "#E9C46A", "blue": "#8FB3D9", "magenta": "#C9A0DC", "cyan": "#86C5C1", "white": "#F0EEE9", "brightBlack": "#8A8578", "brightRed": "#F08A6A", "brightGreen": "#A9D49A", "brightYellow": "#F2D58C", "brightBlue": "#AFC9E6", "brightMagenta": "#DBBDE8", "brightCyan": "#A6D8D4", "brightWhite": "#FFFFFF" }

Hide
Type "unset CLAUDECODE CLAUDE_PID CLAUDE_EFFORT ${!CLAUDE_CODE_*}; cd /tmp/nudge && export TIME_TRAVEL_HOME=/tmp/nudge/.time-travel PS1='\[\e[38;2;228;87;46m\]~/nudge \$\[\e[0m\] ' TT=/Users/pierryborges/Development/time-travel && alias claude='command claude --setting-sources project --allowedTools Bash Read Write Edit Glob Grep Skill' && clear"
Enter
Sleep 1s
Show

Type "cat plan.md"
Sleep 400ms
Enter
Sleep 5s

Type "claude --plugin-dir $TT"
Sleep 400ms
Enter

Wait+Screen@60s /shift\+tab|for shortcuts/
Sleep 1.5s

Type "/time-travel:premortem plan.md"
Sleep 1.2s
Enter

# Real time from here: legs, gate calls and the reply as they happen.
# A fixed, generous window instead of waiting on screen text, so the
# recording is never discarded; the idle tail is trimmed afterwards.
Sleep 540s
