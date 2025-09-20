import json
import sys
import time
import subprocess
import env

def main(intents):
    alarm_length_seconds = intents["intExtras"]["android.intent.extra.alarm.LENGTH"]
    #alarm_length_minutes = alarm_length_seconds // 60
    #spare_seconds = alarm_length_seconds % 60
    #time.sleep(spare_seconds)
    subprocess.run([
        env.get_hobby_command('hobby_vli_timer.sh'),
        '--alarm', str(alarm_length_seconds),
        '--alarm-sound', '/HOME/Music/alarm.mp3',
        '--command', env.get_hobby_command('pause_music_during_timer.sh'),
        '--no-escape-quits'])
    
    
if __name__ == "__main__":
    main(json.loads(sys.argv[1]))
