import os
import shutil
import getpass
import time
from os import path


def ls_lin(dir=os.curdir):
    type_o = {
        '40': 'd',
        '10': '-',
        '12': 'l'
    }

    perm = {
        '0': '---',
        '1': '--x',
        '2': '-w-',
        '3': '-wr',
        '4': 'r--',
        '5': 'r-x',
        '6': 'rw-',
        '7': 'rwx'
    }
    obj_t = type_o[oct(os.stat(dir).st_mode)[2:4]]
    for elem in os.scandir(path.normpath(dir)):
        print("{0}{1} {2} {3} {3} {4:>6} {5} {6}".format(
            type_o[oct(elem.stat().st_mode)[2:4]],
            "".join(perm[x] for x in oct(os.stat(dir).st_mode)[-3:]),
            elem.stat().st_nlink,
            getpass.getuser(),
            elem.stat().st_size,
            time.strftime('%b %d %H:%M', time.gmtime(int(str(elem.stat().st_mtime_ns)[0:10]))),
            elem.name))

def man(cmd=''):
    usage = {
        'ls': "Standart list of directory. There's no arguments required",
        'll': "Extended list of directory. There's no arguments required",
        'cd': 'Use to change current dir.\n'
              'Usage: cd new_dir',
        'cp': "Use to copy file.\n"
              "Usage: cp file copy_location",
        'touch': "Use to create file.\n"
                 "Usage: touch file",
        'mv': "Use it to rename file or move it to another directory.\n"
              "Usage: mv old_name new_name",
        'rm': "Use it ti delete file.\n"
              "Usage: rm file",
        'pwd': "Shows current location. There's no arguments required"
    }

    print(usage.get(cmd, "Wrond command!"))


def main():
    command = {
        'ls': lambda dir=os.curdir: [print(elem.name) for elem in os.scandir(path.normpath(dir))],
        'll': ls_lin,
        'cd': lambda dir: os.chdir(path.normpath(dir)),
        'cp': lambda src, dest: shutil.copy2(path.normpath(src), path.normpath(dest)),
        'touch': lambda name: open(path.normpath(name), 'w').close(),
        'mv': lambda src, dest: os.rename(path.normpath(src), path.normpath(dest)),
        'rm': lambda file: os.remove(path.normpath(file)),
        'pwd': lambda: print(os.getcwd()),
        'exit': exit,
        'man': man
    }

    print('Available commands:', *command.keys(), '', sep='\n')
    while True:
        comd = input('root@localhost# ').split()
        if not comd: continue
        try:
            command.get(comd[0])(*comd[1:])
        except KeyError:
            print('Invalid command!')
            print('Available commands: ', *command.keys())

if __name__ == '__main__':
    main()



