#!/usr/bin/env python

# WARNING
# WARNING
# WARNING
# --------
# IN THE CASE THAT ESH IS SET TO YOUR USER SHELL AND YOU HAVE MADE A MISTAKE IN THIS FILE DO THE FOLLOWING:
# 1. Log into TTY2 as your root user.
# 2. Fix the issue using a terminal editor. Otherwise, use the install script.
# Reboot.


import os
import subprocess
import sys
import time
import getpass
import toml
import socket
from stat import *

try:
    import readline
    readline.read_history_file(f"/home/{getpass.getuser()}/.config/esh/.eshhistory")
except:
    pass

# Functions for returning ANSI colours manually.
def _256(color_, string):
    num1 = str(color_)
    if color_ % 16 == 0:
        return(f"\033[38;5;{num1}m{string}\033[0;0m\n")
    else:
        return(f"\033[38;5;{num1}m{string}\033[0;0m")


# Configuration
config = toml.load(f'/home/{getpass.getuser()}/.config/esh/eshconfig.toml')


# Called when a comamnd is not found
def n(c):
    print(f"EccentriciShell: could not find the specified command: {c}")

# Piping
def exCmd(command):
    try:
        if "|" in command:
            s_in, s_out = (0, 0)
            s_in = os.dup(0)
            s_out = os.dup(1)
            fdin = os.dup(s_in)
            for i in command.split("|"):
                os.dup2(fdin, 0)
                os.close(fdin)
                if i == command.split("|")[-1]:
                    fdout = os.dup(s_out)
                else:
                    fdin, fdout = os.pipe()
                os.dup2(fdout, 1)
                os.close(fdout)
                try:
                    p = subprocess.run(i.strip().split())
                except Exception:
                    n(i.strip())

            os.dup2(s_in, 0)
            os.dup2(s_out, 1)
            os.close(s_in)
            os.close(s_out)

        else:
            p = subprocess.run(command.split(" "))

    except Exception:
        n(command)

# Change Directory
## 'cmd_*' means that this function is a command.
def cmd_kd(path):
    try:
        if config['system']['usetilde'] == True:
            if path.startswith("~"):
                hpath = path.replace("~", f"/home/{getpass.getuser()}")
                os.chdir(os.path.abspath(hpath))
            else:
                os.chdir(os.path.abspath(path))
        else:
            os.chdir(os.path.abspath(path))
    except Exception:
        print(f"EccentriciShell: could not find '{path}' as a valid directory.")

# Return Current Directory.
## Note that this function does not contain 'cmd_*', this means it will not be called directly by the user. 
def dir(cwd):
    path = os.path.abspath(cwd)
    if os.path.dirname(path) == path:
        return "/"
    elif config['system']['usetilde'] == True:
        if path.startswith(f"/home/{getpass.getuser()}"):
            return path.replace(f"/home/{getpass.getuser()}","~")
    else:
        return os.path.abspath(cwd)

# Highlighting
## Used for highlighting data.
def highlighting(data):
    if config['colours']['enabled'] == True:
        if os.path.isfile(data)== True:
            file = f"{_256(9, data)}"
        elif os.path.isdir(data):
            file = f"{_256(11, data)}"
        else:
            file = f"{data}"
        return file
    return data

# Listing all directories and files within the current directory
def cmd_ls(p):
    try:
        if p == "":
            path = os.getcwd()
        else:
            path = os.path.abspath(p)
        files = os.listdir(path)
        # Iterating over the array and performing the code below - given that the current element is not the last
        if len(files) >= 2: #Fix1
            for f in sorted(files)[:-1]:
                # Printing two spaces prior to the next element on the same line.
                print(f"{highlighting(f)}", end="  ")
            print(highlighting("".join(sorted(files)[-1:])))
        else:
            print(highlighting("".join(sorted(files))))
    except Exception:
        print(f"{colours.red}EccentriciShell: something went wrong while executing this comamnd.{colours.end}")

# Creating a counter.
## This counter will be useful for single based events.

counter = 0
def main():
    while True:
        try:
            global counter
            # If counter is 0 - in other words, if this is the first command in the terminal session - then run a startup command.
            if counter == 0:
                exCmd(f"sh /home/{getpass.getuser()}/.config/esh/start.sh")
            # Prompt
            print(f"{_256(15, getpass.getuser())}{_256(117, '@')}{_256(15, socket.gethostname())} [{_256(15, dir(os.getcwd()))}]")
            inp = input(f"{_256(197, '🦓 $ ')}")

            # Outcomes.
            if inp == "exit":
                break
            elif inp == "quit":
                break
            elif inp[:2] == "cd":
                cmd_kd(inp[3:])
            elif inp[:1] == "":
                return
            elif inp[:2] == "ls":
                cmd_ls(inp[3:])
            elif inp[:4] == "exec":
                exCmd(inp[5:])
            else:
                exCmd(inp)
            counter += 1
            readline.write_history_file(f"/home/{getpass.getuser()}/.config/esh/.eshhistory")
            readline.parse_and_bind("tab: complete")
        except KeyboardInterrupt:
            counter +=1
            print()
            main() # STOPS ALL KEYBOARD INTERRUPTIONS.
        
if __name__ == '__main__':
    try:
        main()
    except:
        print("Something went wrong!")
