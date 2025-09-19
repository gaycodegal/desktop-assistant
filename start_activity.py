import subprocess
import json
import sys

def dispatch(args):
    execute(args[0])

def execute(intent):
    action = intent["action"]
    try:
        process = subprocess.Popen(['python3', 'desktop-intents/' + action + ".py", json.dumps(intent)])
        
    except:
        pass


if __name__ == "__main__":
    execute(json.loads(sys.argv[1]))
