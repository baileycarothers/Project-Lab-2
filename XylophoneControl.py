#GUI Stuff
from tkinter import *

#GPIO setup for non-expander ports
import RPi.GPIO as GPIO
import time

#Haven't gotten around to figuring this out
#import multiprocessing

#port Expander stuff
import board
import busio
from digitalio import Direction
from adafruit_mcp230xx.mcp23008 import MCP23008

#Port expander setup
i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23008(i2c)

#Port expander declarations
fSharp6 = mcp.get_pin(0)
gSharp6 = mcp.get_pin(1)
aSharp6 = mcp.get_pin(2)
cSharp7 = mcp.get_pin(3)
dSharp7 = mcp.get_pin(4)
fSharp7 = mcp.get_pin(5)
gSharp7 = mcp.get_pin(6)
aSharp7 = mcp.get_pin(7)

#Port expanders as output
fSharp6.direction = Direction.OUTPUT
gSharp6.direction = Direction.OUTPUT
aSharp6.direction = Direction.OUTPUT
cSharp7.direction = Direction.OUTPUT
dSharp7.direction = Direction.OUTPUT
fSharp7.direction = Direction.OUTPUT
gSharp7.direction = Direction.OUTPUT
aSharp7.direction = Direction.OUTPUT

#Window declaration
root = Tk()

#Window Sepcifications
root.title("Xylo Ren Control")
root.geometry('300x250')

#Note port definitions
gSharp5 = 4
aSharp5 = 17
cSharp6 = 27
dSharp6 = 22
g5 = 10
a5 = 9
b5 = 11
c6 = 0
d6 = 5
e6 = 6
f6 = 13
g6 = 19
a6 = 26
b6 = 21
c7 = 20
d7 = 16
e7 = 12
f7 = 1
g7 = 7
a7 = 8
b7 = 25
c8 = 24


#Labels defined
welcomeTxt = Label(root, text = "Welcome!")
lbl = Label(root, text = "Now Playing: Nothing")
emptyTxt = Label(root, text = " ")

#Functions
def closeWindow():
    root.destroy()

def showElement(event):
    event.grid()

def hideElement(event):
    event.grid_forget()

def none():
    pass

def playMenu():
    #btnSong1.configure(text = "Play", command=none)
    #btnSong2.configure(text = "Pause", command=none)
    #btnSong3.configure(text = "Stop", command=returnMenu)
    hideElement(btnSong1)
    hideElement(btnSong2)
    hideElement(btnSong3)
    hideElement(btnSong4)
    time.sleep(1)

#PlayNote passes in note (GPIO port number- we'll fix that later) and duration (note length in seconds)
def playNote(note, duration):
    if(note == fSharp6 or gSharp6 or aSharp6 or cSharp7 or dSharp7 or fSharp7 or gSharp7 or aSharp7):
        note.value = True
        time.sleep(0.1)
        note.value = False
        time.sleep(duration)
    else:
        GPIO.output(note, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(note, GPIO.LOW)
        time.sleep(duration)

#This is the test code i'm (Paul) using for song 3
def Song3():
    
    #For some reason you have to set the ports up everytime you call flashLED
    #GPIO.setmode(GPIO.BCM) deals with the port numbers I think? Anyway it works don't look at me
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)

    playNote(4, 0.47)
    playNote(17, 1.88)
    playNote(27, 0.47)
    playNote(4, 0.47)
    playNote(17, 1.43)
    playNote(27, 0.89)
    playNote(4, 0.48)
    playNote(17, 0.958)
    playNote(27, 0.418)
    playNote(4, 0.958)
    playNote(17, 0.477)
    playNote(27, 1.435)
    playNote(4, 0.958)
    playNote(17, 0.444)
    playNote(27, 1.41)

    GPIO.cleanup()
    returnMenu()

def playSong1():
    lbl.configure(text = "Now Playing: Imperial March")

def playSong2():
    lbl.configure(text = "Now Playing: Ode to Joy")

def playSong3():
    lbl.configure(text = "Now Playing: Nocturne in Eb Major Op. 9 No. 2")
    time.sleep(1)
    Song3()

def playSong4():
    lbl.configure(text = "Now Playing: He's a Pirate")

def returnMenu():
    lbl.configure(text = "Now Playing: Nothing")
    showElement(btnSong1)
    showElement(btnSong2)
    showElement(btnSong3)
    showElement(btnSong4)
    btnSong1.configure(text = "Play Song 1", command= lambda: [playMenu(), playSong1()])
    btnSong2.configure(text = "Play Song 2", command= lambda: [playMenu(), playSong2()])
    btnSong3.configure(text = "Play Song 3", command= lambda: [playMenu(), playSong3()])
    btnSong4.configure(text = "Play Song 4", command= lambda: [playMenu(), playSong4()])
    welcomeTxt.grid(column=0, row=0)
    lbl.grid(column=1, row=1)
    btnSong1.grid(column=1, row=2)
    btnSong2.grid(column=1, row=3)
    btnSong3.grid(column=1, row=4)
    btnSong4.grid(column=1, row=5)
    emptyTxt.grid(column=1, row=6)
    btn_quit.grid(column=1, row=7)

#Buttons
btnSong1 = Button(root, text = "Play Song 1", fg = "red", command= lambda: [playMenu(), playSong1()])
btnSong2 = Button(root, text = "Play Song 2", fg = "red", command= lambda: [playMenu(), playSong2()])
btnSong3 = Button(root, text = "Play Song 3", fg = "red", command= lambda: [playMenu(), playSong3()])
btnSong4 = Button(root, text = "Play Song 4", fg = "red", command= lambda: [playMenu(), playSong4()])
btn_quit = Button(root, text = "Quit", command=closeWindow)

#Packing
btnSong1.grid()
btnSong2.grid()
btnSong3.grid()
btnSong4.grid()

#Grid Layout
welcomeTxt.grid(column=0, row=0)
lbl.grid(column=1, row=1)
btnSong1.grid(column=1, row=2)
btnSong2.grid(column=1, row=3)
btnSong3.grid(column=1, row=4)
btnSong4.grid(column=1, row=5)
emptyTxt.grid(column=1, row=6)
btn_quit.grid(column=1, row=7)

# End of file
root.mainloop()