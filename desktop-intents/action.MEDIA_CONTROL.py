import json
import sys
import time
import subprocess

def play():
    subprocess.run("flatpak run io.github.quodlibet.QuodLibet --play-pause".split(" "))

def previous_song():
    subprocess.run("flatpak run io.github.quodlibet.QuodLibet --force-previous".split(" "))

def next_song():
    subprocess.run("flatpak run io.github.quodlibet.QuodLibet --next".split(" "))

def stop():
    subprocess.run("flatpak run io.github.quodlibet.QuodLibet --stop".split(" "))



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
