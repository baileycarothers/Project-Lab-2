#GUI Stuff
from tkinter import *

#GPIO setup for non-expander ports
import RPi.GPIO as GPIO
import time

#port Expander stuff
import board
import busio
from digitalio import Direction
from adafruit_mcp230xx.mcp23008 import MCP23008

#Port expander setup
i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23008(i2c)

#Port expander declarations
fsharp6 = mcp.get_pin(7)
gsharp6 = mcp.get_pin(6)
asharp6 = mcp.get_pin(5)
csharp7 = mcp.get_pin(4)
dsharp7 = mcp.get_pin(3)
fsharp7 = mcp.get_pin(2)
gsharp7 = mcp.get_pin(1)
asharp7 = mcp.get_pin(0)

#Port expanders as output
fsharp6.direction = Direction.OUTPUT
gsharp6.direction = Direction.OUTPUT
asharp6.direction = Direction.OUTPUT
csharp7.direction = Direction.OUTPUT
dsharp7.direction = Direction.OUTPUT
fsharp7.direction = Direction.OUTPUT
gsharp7.direction = Direction.OUTPUT
asharp7.direction = Direction.OUTPUT

#Window declaration
root = Tk()

#Window Sepcifications
root.title("Xylo Ren Control")
root.geometry('300x250')

#Note port definitions
gsharp5 = 4
asharp5 = 17
csharp6 = 27
dsharp6 = 22
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
g7 = 23
a7 = 18
b7 = 25
c8 = 24

#Labels defined
welcomeTxt = Label(root, text = "Welcome!")
lbl = Label(root, text = "Choose a song below to play!")
emptyTxt = Label(root, text = " ")

#Functions
def closeWindow():
    root.destroy()

def portDeclarations():
    
    #GPIO.setmode(GPIO.BCM) deals with the port numbers
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(g5, GPIO.OUT)
    GPIO.setup(gsharp5, GPIO.OUT)
    GPIO.setup(a5, GPIO.OUT)
    GPIO.setup(asharp5, GPIO.OUT)
    GPIO.setup(b5, GPIO.OUT)
    GPIO.setup(c6, GPIO.OUT)
    GPIO.setup(csharp6, GPIO.OUT)
    GPIO.setup(d6, GPIO.OUT)
    GPIO.setup(dsharp6, GPIO.OUT)
    GPIO.setup(e6, GPIO.OUT)
    GPIO.setup(f6, GPIO.OUT)
    GPIO.setup(g6, GPIO.OUT)
    GPIO.setup(a6, GPIO.OUT)
    GPIO.setup(b6, GPIO.OUT)
    GPIO.setup(c7, GPIO.OUT)
    GPIO.setup(d7, GPIO.OUT)
    GPIO.setup(e7, GPIO.OUT)
    GPIO.setup(f7, GPIO.OUT)
    GPIO.setup(g7, GPIO.OUT)
    GPIO.setup(a7, GPIO.OUT)
    GPIO.setup(b7, GPIO.OUT)
    GPIO.setup(c8, GPIO.OUT)    


#PlayNote passes in note and duration (note length in seconds)
def playNote(note, duration):
     if(note == fsharp6 or note == gsharp6 or note == asharp6 or note == csharp7 or note == dsharp7 or note == fsharp7 or note == gsharp7 or note == asharp7):
         note.value = True
         time.sleep(0.1)
         note.value = False
         time.sleep(duration - 0.1)
     else:
        GPIO.output(note, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(note, GPIO.LOW)
        time.sleep(duration - 0.1)
        

#Song 1 is Imperial March
def Song1():
    
    portDeclarations()

    for i in range(3):
        
        #Measure 3
        playNote(g6, 0.624)
        playNote(g6, 0.624)
        playNote(g6, 0.624)
        playNote(dsharp6, 0.468)
        playNote(asharp6, 0.148)

        #Measure 4
        playNote(g6, 0.624)
        playNote(dsharp6, 0.468)
        playNote(asharp6, 0.148)
        playNote(g6, 1.249)

        #Measure 5
        playNote(d7, 0.624)
        playNote(d7, 0.624)
        playNote(d7, 0.624)
        playNote(dsharp7, 0.468)
        playNote(asharp6, 0.148)

        #Measure 6
        playNote(fsharp6, 0.624)
        playNote(dsharp6, 0.468)
        playNote(asharp6, 0.148)
        playNote(g6, 1.249)

        #Measure 7
        playNote(g7, 0.624)
        playNote(g6, 0.468)
        playNote(g6, 0.148)
        playNote(g7, 0.624)
        playNote(fsharp7, 0.468)
        playNote(f7, 0.148)

        #Measure 8
        playNote(e7, 0.148)
        playNote(dsharp7, 0.148)
        playNote(e7, 0.312)
        time.sleep(0.312)
        playNote(gsharp6, 0.312)
        playNote(csharp7, 0.624)
        playNote(c7, 0.468)
        playNote(b6, 0.148)

        #Measure 9
        playNote(asharp6, 0.148)
        playNote(a6, 0.148)
        playNote(asharp6, 0.312)
        time.sleep(0.312)
        playNote(dsharp6, 0.312)
        playNote(fsharp6, 0.624)
        playNote(dsharp6, 0.468)
        playNote(g6, 0.148)

        #Measure 10
        playNote(asharp6, 0.624)
        playNote(g6, 0.468)
        playNote(asharp6, 0.148)
        playNote(d7, 1.249)

        #Measure 11
        playNote(g7, 0.624)
        playNote(g6, 0.468)
        playNote(g6, 0.148)
        playNote(g7, 0.624)
        playNote(fsharp7, 0.468)
        playNote(f7, 0.148)

        #Measure 12
        playNote(e7, 0.148)
        playNote(dsharp7, 0.148)
        playNote(e7, 0.312)
        time.sleep(0.312)
        playNote(gsharp6, 0.312)
        playNote(csharp7, 0.624)
        playNote(c7, 0.468)
        playNote(b6, 0.148)

        #Measure 13
        playNote(asharp6, 0.148)
        playNote(a6, 0.148)
        playNote(asharp6, 0.312)
        time.sleep(0.312)
        playNote(dsharp6, 0.312)
        playNote(fsharp6, 0.624)
        playNote(dsharp6, 0.468)
        playNote(asharp6, 0.148)

        #Measure 14
        playNote(g6, 0.624)
        playNote(dsharp6, 0.468)
        playNote(asharp6, 0.148)
        playNote(g6, 1.249)

    GPIO.cleanup()
    returnMenu()
    
#Song 2 is Ode 2 joy by Beethoven     
def Song2():
    
    portDeclarations()

    #Pick up (Measure 1) 
    playNote(e6, 0.857) 
    playNote(e6, 0.857) 
    playNote(f6, 0.857) 
    playNote(g6, 0.857) 
 
    #Measure 2 
    playNote(g6, 0.857) 
    playNote(f6, 0.857) 
    playNote(e6, 0.857) 
    playNote(d6, 0.857) 
 
    #Measure 3 
    playNote(c6, 0.857) 
    playNote(c6, 0.857) 
    playNote(d6, 0.857) 
    playNote(e6, 0.857) 
 
    #Measure 4 
    playNote(e6, 1.31) 
    playNote(d6, 0.429) 
    playNote(d6, 1.63) 
 
    #Measure 5 
    playNote(e6, 0.857) 
    playNote(e6, 0.857) 
    playNote(f6, 0.857) 
    playNote(g6, 0.857) 
       
    #Measure 6 
    playNote(g6, 0.857) 
    playNote(f6, 0.857) 
    playNote(e6, 0.857) 
    playNote(d6, 0.857) 
 
    #Measure 7 
    playNote(c6, 0.857) 
    playNote(c6, 0.857) 
    playNote(d6, 0.857) 
    playNote(e6, 0.857)   
 
    #Measure 8 
    playNote(d6, 1.31) 
    playNote(c6, 0.429) 
    playNote(c6, 1.63) 
 
    #Measure 9 
    playNote(d6, 0.857) 
    playNote(d6, 0.857) 
    playNote(e6, 0.857) 
    playNote(c6, 0.857)   
 
    #Measure 10 
    playNote(d6, 0.857) 
    playNote(e6, 0.429) 
    playNote(f6, 0.429) 
    playNote(e6, 0.857)   
    playNote(c6, 0.857) 
 
    #Measure 11 
    playNote(d6, 0.857) 
    playNote(e6, 0.429) 
    playNote(f6, 0.429) 
    playNote(e6, 0.857) 
    playNote(d6, 0.857) 
 
    #Measure 12 
    playNote(c6, 0.857) 
    playNote(d6, 0.832) 
    playNote(g5, 1.714) 
 
    #Measure 13 
    playNote(d6, 0.857) 
    playNote(d6, 0.857) 
    playNote(e6, 0.857) 
    playNote(c6, 0.857) 
 
    #Measure 14 
    playNote(d6, 0.857) 
    playNote(e6, 0.429) 
    playNote(f6, 0.429) 
    playNote(e6, 0.857) 
    playNote(c6, 0.857) 
     
    #Measure 15 
    playNote(d6, 0.857) 
    playNote(e6, 0.429) 
    playNote(f6, 0.429) 
    playNote(e6, 0.857) 
    playNote(d6, 0.857) 
     
    #Measure 16 
    playNote(c6, 0.857) 
    playNote(d6, 0.832) 
    playNote(g5, 1.714) 

    #Measure 17 
    playNote(e6, 0.832)
    playNote(e6, 0.832) 
    playNote(f6, 0.857) 
    playNote(g6, 0.857)   
     
    #Measure 18
    playNote(g6, 0.857)
    playNote(f6, 0.857) 
    playNote(e6, 0.857) 
    playNote(d6, 0.857) 
 
    #Measure 19 
    playNote(c6, 0.857)
    playNote(c6, 0.857)
    playNote(d6, 0.857)
    playNote(e6, 0.857)
    
     
    #Measure 20 
    playNote(e6, 1.31) 
    playNote(d6, 0.429) 
    playNote(d6, 1.63)
 
    #Measure 21  
    playNote(e6, 0.857) 
    playNote(e6, 0.857) 
    playNote(f6, 0.857) 
    playNote(g6, 0.857) 
  
    #Measure 22 
    playNote(g6, 0.857) 
    playNote(f6, 0.857) 
    playNote(e6, 0.857) 
    playNote(d6, 0.857) 
  
    #Measure 23  
    playNote(c6, 0.857) 
    playNote(c6, 0.857) 
    playNote(d6, 0.857) 
    playNote(e6, 0.857) 
 
    #Measure 24 
    playNote(d6, 0.857) 
    playNote(c6, 0.300) 
    playNote(c6, 1.63) 


    GPIO.cleanup()
    returnMenu()
    
    
        
#Song 3 is nocturne by chopin
def Song3():
    
    portDeclarations()

    #Pick up (Measure 1)
    playNote(asharp5, 0.47)

    #Measure 2
    playNote(g6, 1.88)
    playNote(f6, 0.47)
    playNote(g6, 0.47)
    playNote(f6, 1.43)
    playNote(dsharp6, 0.89)
    playNote(asharp5, 0.48)

    #Measure 3
    playNote(g6, 0.958)
    playNote(c6, 0.418)
    playNote(c7, 0.958)
    playNote(g6, 0.477)
    playNote(asharp6, 1.435)
    playNote(gsharp6, 0.958) 
    playNote(g6, 0.444)

    #Measure 4
    playNote(f6, 1.41)
    playNote(g6, 0.958)
    playNote(d6, 0.444)
    playNote(dsharp6, 1.41)
    playNote(c6, 1.41)

    #Measure 5
    playNote(asharp5, 0.47)
    playNote(d7, 0.47)
    playNote(c7, 0.47)
    playNote(asharp6, 0.23)
    playNote(gsharp6, 0.23)  
    playNote(g6, 0.23)
    playNote(gsharp6, 0.23)
    playNote(c6, 0.23)
    playNote(d6, 0.23)
    playNote(dsharp6, 1.33)
    time.sleep(1.013)
    playNote(asharp5, 0.47)

    #Measure 6
    playNote(g6, 1.43)
    playNote(f6, 0.23)
    playNote(g6, 0.23)
    playNote(f6, 0.23)
    playNote(e6, 0.23)  
    playNote(f6, 0.23)
    playNote(g6, 0.23)
    playNote(f6, 0.23)
    playNote(dsharp6, 1.19)
    playNote(f6, 0.33)
    playNote(d6, 0.23)
    playNote(dsharp6, 0.23)
    playNote(f6, 0.23)

    #Measure 7
    playNote(g6, 0.23)
    playNote(b5, 0.23)
    playNote(c6, 0.23)
    playNote(csharp6, 0.23)  
    playNote(c6, 0.23)
    playNote(f6, 0.23)
    playNote(e6, 0.23)
    playNote(gsharp6, 0.23)
    playNote(g6, 0.23)  
    playNote(csharp6, 0.23)
    playNote(c6, 0.23)
    playNote(g6, 0.23)
    playNote(asharp6, 1.43)
    playNote(gsharp6, 0.444)
    playNote(g6, 0.444)

    #Measure 8
    playNote(f6, 0.932)
    time.sleep(0.47)
    playNote(g6, 0.23)
    time.sleep(0.23)
    playNote(g6, 0.47)
    time.sleep(0.47)
    playNote(d6, 1.41)
    playNote(dsharp6, 1.38)
    playNote(c6 ,1.41)

    #Measure 9
    playNote(asharp5, 0.47)
    playNote(d7, 0.47)
    playNote(c7, 0.47)
    playNote(asharp6, 0.23)  
    playNote(gsharp6, 0.23)
    playNote(g6, 0.23)
    playNote(gsharp6, 0.23)
    playNote(c6, 0.23)
    playNote(d6, 0.23)
    playNote(dsharp6, 1.88)
    playNote(d6, 0.47)
    playNote(dsharp6, 0.47)

    #Measure 10
    playNote(f6, 1.41)
    playNote(g6, 0.958)
    playNote(f6, 0.444)
    playNote(f6, 1.43)  
    playNote(c6, 1.41)

    #Measure 11
    playNote(dsharp6, 0.444)
    playNote(dsharp6, 0.444)
    playNote(dsharp6, 0.444)
    playNote(dsharp6, 0.444)
    playNote(d6, 0.23)
    playNote(dsharp6, 0.23)
    playNote(f6, 0.466)
    playNote(dsharp6, 1.41)
    playNote(asharp5, 1.41)

    #Measure 12
    playNote(asharp6, 1.43)
    playNote(a6, 0.958)
    playNote(g6, 0.444)
    playNote(f6, 1.41)
    playNote(d6, 1.41)

    #Measure 13
    playNote(dsharp6, 1.43)
    playNote(d6, 0.444)
    playNote(c6, 0.444)
    playNote(d6, 0.444)
    playNote(asharp5, 0.444)
    playNote(b5, 0.444)
    playNote(b5, 0.444)
    playNote(c6, 0.444)
    playNote(c6, 0.444)
    playNote(d6, 0.444)

    #Measure 14
    playNote(g6, 0.958)
    playNote(a5, 0.23)
    playNote(asharp5, 0.23)
    playNote(b5, 0.23)
    playNote(asharp5, 0.23)
    playNote(csharp6, 0.23)
    playNote(d6, 0.23)
    playNote(g6, 0.444)
    playNote(f6, 0.958)
    playNote(dsharp6, 0.705)
    playNote(f6, 0.23)
    playNote(dsharp6, 0.23)
    playNote(d6, 0.23)
    playNote(dsharp6, 0.23)
    playNote(f6, 0.23)
    
    #Measure 15
    playNote(g6, 0.23)
    playNote(b5, 0.23)
    playNote(c6, 0.23)
    playNote(csharp6, 0.23)
    playNote(c6, 0.23)
    playNote(f6, 0.23)
    playNote(e6, 0.23)
    playNote(gsharp6, 0.23)
    playNote(g6, 0.23)
    playNote(csharp7, 0.23)
    playNote(c7, 0.23)
    playNote(g6, 0.23)
    playNote(asharp6, 1.43)
    playNote(gsharp6, 0.958)
    playNote(g6, 0.444)

    #Measure 16
    playNote(f6, 0.958)
    time.sleep(0.444)
    playNote(g6, 0.958)
    playNote(d6, 0.444)
    playNote(dsharp6, 1.41)
    playNote(c6, 1.41)

    #Measure 17
    playNote(asharp5, 0.444)
    playNote(d7, 0.444)
    playNote(csharp7, 0.444)
    playNote(c7, 0.135)
    playNote(b6, 0.135)
    playNote(asharp6, 0.135)
    playNote(a6, 0.135)
    playNote(gsharp6, 0.135)
    playNote(f6, 0.135)
    playNote(d6, 0.135)
    playNote(b5, 0.135)
    playNote(asharp5, 0.135)
    playNote(d6, 0.135)
    playNote(g6, 0.135)
    playNote(f6, 0.135)
    playNote(dsharp6, 1.88)

    GPIO.cleanup()
    returnMenu()
    
def Song4():
    
    portDeclarations()
        
    for i in range(2):

        #Pick up (Measure 1) 
        playNote(b5, 0.304) 
        playNote(csharp6, 0.304) 
        playNote(d6, 0.304) 
        playNote(e6, 0.304) 
        playNote(fsharp6, 0.304) 
        playNote(d6, 0.304) 
        playNote(fsharp6, 0.608) 
     
        #Measure 2 
        playNote(f6, 0.304) 
        playNote(csharp6, 0.304) 
        playNote(f6, 0.608) 
        playNote(e6, 0.304) 
        playNote(c6, 0.304) 
        playNote(e6, 0.566) 
     
        #Measure 3 
        playNote(b5, 0.304) 
        playNote(csharp6, 0.304) 
        playNote(d6, 0.304) 
        playNote(e6, 0.304) 
        playNote(fsharp6, 0.304) 
        playNote(d6, 0.304) 
        playNote(fsharp6, 0.304) 
        playNote(b6, 0.304) 
     
        #Measure 4 
        playNote(a6, 0.304) 
        playNote(fsharp6, 0.304) 
        playNote(d6, 0.304) 
        playNote(fsharp6, 0.304) 
        playNote(a6, 1.13) 
     
        #Measure 5 
        playNote(b5, 0.304) 
        playNote(csharp6, 0.304) 
        playNote(d6, 0.304) 
        playNote(e6, 0.304) 
        playNote(fsharp6, 0.304) 
        playNote(d6, 0.304) 
        playNote(fsharp6, 0.608) 
     
        #Measure 6 
        playNote(f6, 0.304) 
        playNote(csharp6, 0.304) 
        playNote(f6, 0.608) 
        playNote(e6, 0.304) 
        playNote(c6, 0.304) 
        playNote(e6, 0.566) 
     
        #Measure 7 
        playNote(b5, 0.304) 
        playNote(csharp6, 0.304) 
        playNote(d6, 0.304) 
        playNote(e6, 0.304) 
        playNote(fsharp6, 0.304) 
        playNote(d6, 0.304) 
        playNote(fsharp6, 0.304) 
        playNote(b6, 0.304) 
     
        #Measure 8 
        playNote(a6, 0.304) 
        playNote(fsharp6, 0.304) 
        playNote(d6, 0.304) 
        playNote(fsharp6, 0.304) 
        playNote(a6, 1.13) 
     
        #Measure 9 
        playNote(fsharp6, 0.304) 
        playNote(gsharp6, 0.304) 
        playNote(asharp6, 0.304) 
        playNote(b6, 0.304) 
        playNote(csharp7, 0.304) 
        playNote(asharp6, 0.304) 
        playNote(csharp7, 0.608) 
     
        #Measure 10 
        playNote(d7, 0.304) 
        playNote(asharp6, 0.304) 
        playNote(d7, 0.608) 
        playNote(csharp7, 0.304) 
        playNote(asharp6, 0.304) 
        playNote(csharp7, 0.566) 
     
        #Measure 11 
        playNote(fsharp6, 0.304) 
        playNote(gsharp6, 0.304) 
        playNote(asharp6, 0.304) 
        playNote(b6, 0.304) 
        playNote(csharp7, 0.304) 
        playNote(asharp6, 0.304) 
        playNote(csharp7, 0.608) 
     
        #Measure 12 
        playNote(d7, 0.304) 
        playNote(asharp6, 0.304) 
        playNote(d7, 0.608) 
        playNote(csharp7, 1.13)
        
        #Measure 13 
        playNote(fsharp6, 0.304) 
        playNote(gsharp6, 0.304) 
        playNote(asharp6, 0.304) 
        playNote(b6, 0.304) 
        playNote(csharp7, 0.304) 
        playNote(asharp6, 0.304) 
        playNote(csharp7, 0.608) 
     
        #Measure 14 
        playNote(d7, 0.304) 
        playNote(asharp6, 0.304) 
        playNote(d7, 0.608) 
        playNote(csharp7, 0.304) 
        playNote(asharp6, 0.304) 
        playNote(csharp7, 0.566) 
     
        #Measure 15 
        playNote(fsharp6, 0.304) 
        playNote(gsharp6, 0.304) 
        playNote(asharp6, 0.304) 
        playNote(b6, 0.304) 
        playNote(csharp7, 0.304) 
        playNote(asharp6, 0.304) 
        playNote(csharp7, 0.608) 
     
        #Measure 16 
        playNote(d7, 0.304) 
        playNote(asharp6, 0.304) 
        playNote(d7, 0.608) 
        playNote(csharp7, 1.13)
        
        #Measure 17 
        playNote(b6, 0.304) 
        playNote(csharp7, 0.304) 
        playNote(d7, 0.304) 
        playNote(e7, 0.304) 
        playNote(fsharp7, 0.304) 
        playNote(d7, 0.304) 
        playNote(fsharp7, 0.608) 
     
        #Measure 18 
        playNote(f7, 0.304) 
        playNote(csharp7, 0.304) 
        playNote(f7, 0.608) 
        playNote(e7, 0.304) 
        playNote(c7, 0.304) 
        playNote(e7, 0.566)
        
        #Measure 19 
        playNote(b6, 0.304) 
        playNote(csharp7, 0.304) 
        playNote(d7, 0.304) 
        playNote(e7, 0.304) 
        playNote(fsharp7, 0.304) 
        playNote(d7, 0.304) 
        playNote(fsharp7, 0.304) 
        playNote(b7, 0.304) 
     
        #Measure 20 
        playNote(a7, 0.304) 
        playNote(fsharp7, 0.304) 
        playNote(d7, 0.304) 
        playNote(fsharp7, 0.304) 
        playNote(a7, 1.13)
        
        #Measure 21
        time.sleep(0.304)
        playNote(asharp7, 0.114)
        playNote(b7, 0.306)
        time.sleep(1.13)
        
        #Measure 22
        time.sleep(0.304)
        playNote(asharp7, 0.114)
        playNote(b7, 0.306)
        time.sleep(1.13)
    
    #Measure 45 
    playNote(asharp6, 0.304) 
    playNote(c7, 0.304) 
    playNote(csharp7, 0.304) 
    playNote(dsharp7, 0.304) 
    playNote(f7, 0.304) 
    playNote(csharp7, 0.304) 
    playNote(f7, 0.304) 
    playNote(asharp7, 0.304) 
 
    #Measure 46 
    playNote(a7, 0.304) 
    playNote(f7, 0.304) 
    playNote(a7, 0.304) 
    playNote(c8, 0.304) 
    playNote(asharp7, 1.13)


    GPIO.cleanup()
    returnMenu()

#Buttons

btnSong1 = Button(root, text = "Imperial March", fg = "red", command= Song1())
btnSong2 = Button(root, text = "Ode to Joy", fg = "red", command= Song2())
btnSong3 = Button(root, text = "Nocturne in Eb Major Op. 9 No. 2", fg = "red", command= Song3())
btnSong4 = Button(root, text = "In the Hall of the Mountain King", fg = "red", command= Song4())
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