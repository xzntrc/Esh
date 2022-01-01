import os
import subprocess
import sys
import time
import getpass
# Defining some ANSI escape codes
class colours:
    black = '\033[30m'
    red = '\033[91m'
    yellow = '\033[93m'
    fileC = '\033[93m'
    end = '\033[0m'

# Called when a comamnd is not found
def n(c):
    print(f"EccentriciShell: could not find the specified command: {c}")

# Running external commands, forgot who wrote this segment.
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
                    subprocess.run(i.strip().split())
                except Exception:
                    n(i.strip())

            os.dup2(s_in, 0)
            os.dup2(s_out, 1)
            os.close(s_in)
            os.close(s_out)
        else:
            subprocess.run(command.split(" "))

    except Exception:
        n(command)

# Change Location.
## 'cmd_*' means that this function is a command.
def cmd_cl(path):
    try:
        if path.startwith("~"):
            print("test")
            hpath = path.replace("~", f"/home/{getpass.getuser()}")
            print(hpath)
            os.chdir(os.path.abspath(hpath))
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
    elif path.startswith(f"/home/{getpass.getuser()}"):
        return path.replace(f"/home/{getpass.getuser()}","~")
    else:
        return os.path.abspath(cwd)

# Highlighting
## Used for highlighting data.
def highlighting(data):
    if os.path.isfile(data) == True:
        file = f"{colours.red}{data}{colours.end}"
    elif os.path.isdir(data):
        file = f"{colours.yellow}{data}{colours.end}"
    else:
        file = f"{data}"
    return file

# Listing all directories and files within the current directory
def cmd_ls():
    try:
        files = os.listdir(os.getcwd())
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
def main():
    while True:
        inp = input(f"{dir(os.getcwd())} → ")
        if inp == "exit":
            break
        elif inp[:2] == "kd": #basically CD 
            cmd_cl(inp[3:])
        elif inp[:1] == "":
            cmd_cl()
        elif inp == "help":
            cmd_cl()
        elif inp == "pf":
            cmd_ls()
        else:
            exCmd(inp)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print(f"{colours.red}EccentriciShell recieved KeyboardInterrupt.{colours.end}")
        time.sleep(.7)
        print("Exiting")
        time.sleep(1.2)
        sys.exit(0)

