import os
import time
#from adb_android import adb_android

print("-------------------------------------------------")
os.system("adb start-server")
print("Available Device")
os.system("adb devices")
time.sleep(3)
print("Flashing Custom Recovery")
time.sleep(1)
print("\n3")
time.sleep(1)
print("\n2")
time.sleep(1)
print("\n1")
time.sleep(1)
os.system("flash_tool -s TWRP/TWRP_scatter.txt -c download")
print("Unplug and plug the cable")
time.sleep(5)
print("Custom Recovery Flashed")
time.sleep(10)
print("-------------------------------------------------")
os.system("adb shell >file.txt")
if '$' in open('file.txt').read():
    print "ADB Connected"
    os.system("exit")
print("The device is going into recovery mode")
os.system("adb reboot recovery")
if '$' in open('file.txt').read():
    print "ADB Connected"
os.system("exit")
print("-------------------------------------------------")
os.system("adb sideload Supersu.zip")
time.sleep(17)
os.system("adb reboot system --twrp")
print("Device is rebooting.")
time.sleep(10)
if '$' in open('file.txt').read():
    print "ADB Connected"
os.system("exit")
print("Flashing Stock Recovery")
os.system("flash_tool -s Stock/Stock_scatter.txt -c download")
time.sleep(3)
print("Unplug and Plug the cable")
time.sleep(5)
print("Stock Recovery Flashed")
print("Root Succeded!!")



