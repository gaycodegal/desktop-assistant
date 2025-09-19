import json
import sys
import time
import subprocess
import env

def main(intents):
    query = intents.get('extras',{}).get('query', {})
    if query == 'quit':
        subprocess.run([
            env.get_hobby_command('music_quit.sh'),
        ])
    else:
        subprocess.run([
            env.get_hobby_command('music.sh'),
        ])
    
    
if __name__ == "__main__":
    main(json.loads(sys.argv[1]))
