from os import system as com
from random import randint
from time import sleep

print("   CODE INITIATED")
sleep(1)
print(" INSTALLING SOFTWARE")
sleep(2)

for i in range (50):
    for j in range(randint(30, 80)):
        text = randint(1, 9)
        print(text, end="")
    print("")
    sleep(0.1)

sleep(2)
print("\n")
print("PROCESS FINISHED")
sleep(0.5)
print("\n")
print("Press Any Key To Exit >> ", end="")
sleep(3)
print("\n")
print("CODE RED")
sleep(0.5)
print("PROCESS FAILED")
sleep(0.5)
print("INITIATING SELF-DESTRUCT SEQUENCE")
sleep(2)

for i in range(10):
    com("start")
com('shutdown /s /t 10 /c "CRITICAL ERROR DETECTED"')