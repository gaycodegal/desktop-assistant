import os

def get_eng_or(value, default):
    try:
        return os.environ[value]
    except KeyError:
        return default

def get_hobby_home():
    hobby_home = get_eng_or('HOBBY_CMD_HOME', None)
    #if hobby_home is not None:
    #    return hobby_home
    #home = get_eng_or('HOME', None) or '/HOME'
    #return os.path.join(home, '/.config/hobby-commandline')
    return os.path.join(os.getcwd(), 'config')

def get_hobby_command(command_name):
    return os.path.join(get_hobby_home(), 'commands', command_name)
