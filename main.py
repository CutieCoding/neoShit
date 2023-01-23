import functions
from functions import *

print(topBit()) # eventually put everything in one print statement
print("-" * len(topBit())) # the lines under the top bit
print("OS:", getOS())
print("Host:", getHost())
print("Kernel:", getKernel())
print("Uptime:", getUptime())
print("Packages:", getTotalPackages())
print("Shell:", getShell())
print("Resolution:", getScreenRes())
print("CPU:", getCPU())
print("GPU:", getGPU())
print("RAM:", getRAM())

input() # should remove this later