#!/usr/bin/bash

handler()
{
    kill $PID
}

'/HOME/Documents/git/Alarms/alarm_slint/run_alarm_ui.sh' "$@" &
PID=$!

trap handler SIGINT
trap handler SIGTERM

wait $PID
