import datetime
import os
import platform
import psutil
import socket
import subprocess
import time
import tkinter # gay

def topBit(): # gets the first line and makes it look like how it does in neofetch
    return (getUsername() + "@" + getHostname())

def getUsername(): # stolen from stackoverflow
    return (os.environ.get("USER", os.environ.get("USERNAME"))) # should be cross plat between windows and linux bcs it gets the env vars for each os

def getHostname():
    return (socket.gethostname()) # why doesnt the platform or OS module have this

def getOS(): # this is a really shitty way to do it but i literally dont care
    return (platform.system() + " " + platform.release())

def getHost():
    return ("*shrugs shoulders*") # need to figure out how to return like the pc model name? idk what u call it lol

def getKernel():
    return (platform.version())

def getUptime():
    return str(datetime.timedelta(seconds=(time.time() - psutil.boot_time()))) # this is weird af but it works

def getTotalPackages(): # my friend made this, shoutout to him
    ipackages = subprocess.check_output(["pip", "freeze"])
    packagecount = len(ipackages.splitlines())
    return packagecount

def getShell():
    return (os.environ.get("SHELL")) # returns "None" for me on windows, maybe works on linux need to check

def getScreenRes(): # stolen from stackoverflow, i hate tk
    root = tkinter.Tk()
    screen_width = str(root.winfo_screenwidth())
    screen_height = str(root.winfo_screenheight())
    root.destroy() # so there isnt a whole ass tk window on screen
    return (screen_width + " X " + screen_height) # shit way to do it, dont care

def getCPU(): # really shit, should find a better way
    return platform.processor()

def getGPU(): # stolen from stackoverflow, only supports nvidia gpus lmao
    line_as_bytes = subprocess.check_output("nvidia-smi -L", shell=True)
    line = line_as_bytes.decode("ascii")
    _, line = line.split(":", 1)
    line, _ = line.split("(")
    return line.strip()

def getRAM(): # this is absolutely awful but it works
    return (str(int(psutil.virtual_memory().used / 1024 / 1024)) + " MiB / " + str(int(psutil.virtual_memory().total / 1024 / 1024)) + " MiB")