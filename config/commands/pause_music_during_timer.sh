#!/usr/bin/bash
CHECK_FILE=/tmp/hobby_vli_music_status.txt
if [ ! -f $CHECK_FILE ]; then
    playerctl status > $CHECK_FILE
fi

pause_music() {
	WAS_RUNNING="$(cat $CHECK_FILE)"
	if [ "Playing" = "$WAS_RUNNING" ]; then
		playerctl pause
	fi
}

pause_music
