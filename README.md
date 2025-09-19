# Desktop Assistant

This project is the voice assistant I use on desktop,
it's a shell around the voice assistant I wrote for mobile.

It's packaged nicely or intended for public use, but if
you wanted to hook it up like I do, it can be useful for
setting timers etc while doing laundry.

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
