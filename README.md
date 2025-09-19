# Desktop Assistant

This project is the voice assistant I use on desktop,
it's a shell around the voice assistant I wrote for mobile.

It's packaged nicely or intended for public use, but if
you wanted to hook it up like I do, it can be useful for
setting timers etc while doing laundry.

## How it works

1. run_mic.py uses vosk to turn spoken words into text
1. hobby_commandline.py starts lua/desktop-actions/intent-runner.lua
1. intent-runner.lua picks an action from lua/actions/
1. the action communicates with hobby_commandline.py to execute
1. usually start_activity.py will then select an action from
   desktop-intents/ to interpret the json output of the lua action
1. the desktop intent will select a bash program from config/commands/
   to execute, having decided the command line parameters needed

The path where the contents of the config/ path live can be set with
the `HOBBY_CMD_HOME` environment variable. Ideally if you wanted
to set up your own variants of commands you could set that variable
and copy the contents of config/ to that path, only modifying
the bash programs.

This being said, the number of commands that are supported is rather
bare bones at the moment, so you'll probably need to modify the whole
stack starting in the lua/actions/ folder.

Commands are based solely on the first word of the invocation
- "timer for five minutes and thirty seconds" would choose the
  lua/actions/timer.lua to execute

## Current idiosyncrasies

- Expects /HOME/Documents/git/Alarms to contain https://github.com/gaycodegal/LinuxAlarm
- Expects linux
- Expects music to be handled by a "quod libet" instance
- Only music and timer and license commands really work
- Speech handled by speech-dispatcher
  - I personally recommend using the RHVoice snap with
  the "SLT" voice, but it's up to you to figure out how
  to install that and make it work with speech-dispatcher
  (the config should be in `~/.config/speech-dispatcher/`)


## Pip requirements for venv

See [pip3-list.txt](./pip3-list.txt)

## Origin

This work is a derivative of another project I published at:
https://github.com/hobbycommandline/Hobby-Voice-Command-Line
