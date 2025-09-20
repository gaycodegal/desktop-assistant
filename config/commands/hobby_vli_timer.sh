#!/usr/bin/bash

CHECK_FILE=/tmp/hobby_vli_music_status.txt

resume_music() {
	WAS_RUNNING="$(cat $CHECK_FILE)"
	rm $CHECK_FILE
	if [ "Playing" = "$WAS_RUNNING" ]; then
		playerctl play
	fi
}


handler()
{
    kill $PID
	resume_music
}

'/HOME/Documents/git/Alarms/alarm_slint/run_alarm_ui.sh' "$@" &
PID=$!

trap handler SIGINT
trap handler SIGTERM

wait $PID
resume_music
