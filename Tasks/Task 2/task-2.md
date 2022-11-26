# Task 2
### Session 1
This time were automatic

### Session 2
This time the number was imputed by the user

Code:
```python
from pyfirmata import Arduino
import time

board = Arduino('/dev/cu.usbserial-1410')
print("Communication Successfully started")
def configboard(a,b,c):
    board.digital[12].write(a)
    board.digital[5].write(b)
    board.digital[9].write(c)
    time.sleep(0.5)

i = "start"
while True:
    while not i.isdigit():
        if i == "start":
            print("Welcome to the LED configurator!")
            i = input("Enter a number between 0 - 7 to configure the LED : ")
        elif i == "exit":
            print("Exiting...")
            break
        elif i == "skip":
            i = input("Enter a number between 0 - 7: ")
        else:
            message =i + " is not a number. Enter a number: "
            i = input(message)
    i = int(i)
    if i > 7:
        i = input("Enter a number between 0 - 7: ")
    else:
        configboard((i//4),((1%4) // 2),(i % 2))
        i = "skip"
```

Proof:


### Session 3
```python
import pyfirmata
from pyfirmata import Arduino
import time

board = Arduino('/dev/cu.usbserial-1410')
print("Communication Successfully started")

it = pyfirmata.util.Iterator(board)
it.start()

buttonA = board.digital[9]
buttonB = board.digital[5]
buttonA.mode = pyfirmata.INPUT
buttonB.mode = pyfirmata.INPUT
button_state = False

LED = board.digital[12]


# create dictionnary for true of false computer science themed questions
questions = {
    "Is Creeper the name of the first computer virus?": "True",
    "Is a computer virus a living organism?": "False",
    "Reaper is the name of the first computer worm?": "True",
    "Is Back Orifice the name of the first computer Trojan horse?": "True",
    "Is your computer infected with a virus?": "True",
    "Is dns tunnels a way to bypass firewalls?": "True",
    "Can rubber ducky do bad things?": "True",
    "Is kali linux a good operating system?": "True",
    "Are you a depressed Computer Science Student?": "True",
    "Is the internet a good place to learn about computer science?": "True"
}

score = 0
for i in questions:
    time.sleep(1)
    print(i)
    while True:
        if buttonA.read() == True:
            print("True")
            if questions[i] == "True":
                print("Correct!")
                score += 1
                break
            else:
                print("Incorrect!")
                break
        elif buttonB.read() == True:
            print("False")
            if questions[i] == "False":
                print("Correct!")
                score += 1
                break
            else:
                print("Incorrect!")
                break
        else:
            pass

if score == len(questions):
    print("You won!")
    while True:
        LED.write(1)
        time.sleep(0.5)
        LED.write(0)
        time.sleep(0.5)
```

Proof:
![](proof-3.MOV)

### Session 4
```python
import pyfirmata
from pyfirmata import Arduino
import time

board = Arduino('/dev/cu.usbserial-14230')
print("Communication Successfully started")

it = pyfirmata.util.Iterator(board)
it.start()

buttonA = board.digital[9]
buttonB = board.digital[5]
buttonA.mode = pyfirmata.INPUT
buttonB.mode = pyfirmata.INPUT
button_state = False

LED = board.digital[12]


# create dictionnary for true of false computer science themed questions
questions = {
    "Is Creeper the name of the first computer virus?": "True",
    "Is a computer virus a living organism?": "False",
    "Is Computer Science the best subject?": "True",
    "Is Back Orifice the name of the first computer Trojan horse?": "True",
    "Is your computer infected with a virus?": "False",
    "Is 0xsomething in base 16?": "True",
    "Can computer have soul": "False",
    "Is kali linux a good operating system?": "True",
    "Are you a depressed Computer Science Student?": "True",
    "Is the internet a good place to learn about computer science?": "True"
}

def point():
    LED.write(1)
    time.sleep(0.5)
    LED.write(0)
    time.sleep(0.5)

score = 0
for i in questions:
    time.sleep(1)
    print(i)
    while True:
        if buttonA.read() == True:
            print("True")
            if questions[i] == "True":
                print("Correct!")
                score += 1
                point()
                break
            else:
                print("Incorrect!")
                break
        elif buttonB.read() == True:
            print("False")
            if questions[i] == "False":
                print("Correct!")
                score += 1
                point()
                break
            else:
                print("Incorrect!")
                break
        else:
            pass

if score == len(questions):
    print("You won!")
    while True:
        LED.write(1)
        time.sleep(0.5)
        LED.write(0)
        time.sleep(0.5)
```
Proof
![](proof-4.MOV)