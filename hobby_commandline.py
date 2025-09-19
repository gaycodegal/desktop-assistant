import argparse
import subprocess
import json
import sys
import os

import start_activity

def get_env_or(value, default):
    try:
        return os.environ[value]
    except KeyError:
        return default

HOBBY_CMD_SAY = get_env_or("HOBBY_CMD_SAY", "spd-say").split(" ")

def say(args):
    text = " ".join(args)
    print(text)
    subprocess.run(HOBBY_CMD_SAY + ['--wait', text], shell=False, check=True)

def command_quit(args):
    pass

def sendMediaButtonAction(args):
    button = json.loads(str(args))[0]
    start_activity.dispatch([{
        "action":"action.MEDIA_CONTROL",
        "intExtras": {
            "button": button,
        },
    }])

def stopMusic(args):
    start_activity.dispatch([{
        "action":"action.MEDIA_CONTROL",
        "stringExtras": {
            "button": "KEYCODE_MEDIA_STOP",
        },
    }])

def forceQuit(args):
    sys.exit()

command_map = {
    "quit": command_quit,
    "say": say,
    "result": say,
    "startActivity": start_activity.dispatch,
    "sendMediaButtonAction": sendMediaButtonAction,
    "stopMusic": stopMusic,
    "forceQuit": forceQuit,
}

def main(voice_command):
    voice_command = voice_command.strip()
    if len(voice_command) == 0:
        return
    cmd = voice_command.split(" ")[0]
    if not os.path.exists(os.path.join('lua/actions', cmd + ".lua")):
        return print(f"Command '{cmd}' not found")
    
    with subprocess.Popen(["lua", "lua/desktop-actions/intent-runner.lua", voice_command], stdout=subprocess.PIPE) as proc:
        while line := proc.stdout.readline().decode():
            response = json.loads(line)
            action = response[0]
            action_method = command_map.get(action, None)
            args = response[1:]
            if action_method == None:
                print(action, json.dumps(args))
                continue
            action_method(args)
            

if __name__ == "__main__":
    main(sys.argv[1])
