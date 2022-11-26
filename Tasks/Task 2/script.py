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