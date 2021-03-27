import subprocess
import os


try:
    choice = int(input("Number of qr code to create > "))
except:
    print("error a number is required")


for i in range(int(choice)):

    proccess = subprocess.Popen(["python", "./server.py", "no", str(i)])
os.system("cls")
#, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT
