from tkinter import *

#Window declaration
root = Tk()

#Window Sepcifications
root.title("Xylo Ren Control")
root.geometry('275x250')

#Labels defined
welcomeTxt = Label(root, text = "Welcome!")
lbl = Label(root, text = "Now Playing: Nothing")
emptyTxt = Label(root, text = " ")

cSharp = OutputDevice(17)

def cSharpNote():
	cSharp.on()
	sleep(1)
	cSharp.off()

#Functions
def closeWindow():
	root.destroy()

def showElement(event):
	event.grid()

def hideElement(event):
	event.grid_forget()

def none():
	pass

def playSong1():
	lbl.configure(text = "Now Playing: Song 1")
	cSharpNote()
	sleep(3)
	#Play other notes

def playSong2():
	lbl.configure(text = "Now Playing: Song 2")

def playSong3():
	lbl.configure(text = "Now Playing: Song 3")

def playSong4():
	lbl.configure(text = "Now Playing: Song 4")

def playMenu():
	btnSong1.configure(text = "Play", command=none)
	btnSong2.configure(text = "Pause", command=none)
	btnSong3.configure(text = "Stop", command=returnMenu)
	hideElement(btnSong4)

def returnMenu():
	lbl.configure(text = "Now Playing: Nothing")
	btnSong1.configure(text = "Play Song 1", command= lambda: [playSong1(), playMenu()])
	btnSong2.configure(text = "Play Song 2", command= lambda: [playSong2(), playMenu()])
	btnSong3.configure(text = "Play Song 3", command= lambda: [playSong3(), playMenu()])
	showElement(btnSong4)
	btnSong4.configure(text = "Play Song 4", command= lambda: [playSong4(), playMenu()])
	btnSong4.grid(column=1, row=5)

#Buttons
btnSong1 = Button(root, text = "Play Song 1", fg = "red", command= lambda: [playSong1(), playMenu()])
btnSong2 = Button(root, text = "Play Song 2", fg = "red", command= lambda: [playSong2(), playMenu()])
btnSong3 = Button(root, text = "Play Song 3", fg = "red", command= lambda: [playSong3(), playMenu()])
btnSong4 = Button(root, text = "Play Song 4", fg = "red", command= lambda: [playSong4(), playMenu()])
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