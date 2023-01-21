import os
import platform
import socket
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
    return ("*shrugs shoulders*") # all options that support windows use ctypes, gross

def getTotalPackages():
    return ("*shrugs shoulders*") #`help("modules")` takes 999 years so i need to figure out how to do this

def getShell():
    return (os.environ.get("SHELL")) # returns "None" for me on windows, maybe works on linux need to check

def getScreenRes(): # stolen from stackoverflow, i hate tk
    root = tkinter.Tk()
    screen_width = str(root.winfo_screenwidth())
    screen_height = str(root.winfo_screenheight())
    return (screen_width + " X " + screen_height) # shit way to do it, dont care

def getCPU(): # really shit, should find a better way
    return platform.processor()