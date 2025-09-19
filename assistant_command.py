import sys
import hobby_commandline

def execute(command):
    if command == None or len(command.strip()) == 0:
        return
    try:
        hobby_commandline.main(command)
    except Exception as e:
        print("exception", e)
        pass
