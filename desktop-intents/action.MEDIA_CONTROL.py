import json
import sys
import time
import subprocess
import env

def play():
    subprocess.run(["bash", env.get_hobby_command("play.sh")])

def previous_song():
    subprocess.run(["bash", env.get_hobby_command("previous.sh")])

def next_song():
    subprocess.run(["bash", env.get_hobby_command("next.sh")])

def stop():
    subprocess.run(["bash", env.get_hobby_command("stop.sh")])


def main(intents):
    button = intents.get("intExtras", {}).get("button", None)

    if button == 4:
        return play()
    elif button == 16:
        return previous_song()
    elif button == 32:
        return next_song()
    print("unknown button: ", button)

    string_command = intents.get("stringExtras", {}).get("button", None)

    if string_command == "KEYCODE_MEDIA_STOP":
        return stop()
        
    #alarm_length_minutes = alarm_length_seconds // 60
    #spare_seconds = alarm_length_seconds % 60
    #time.sleep(spare_seconds)
    
    
if __name__ == "__main__":
    main(json.loads(sys.argv[1]))
