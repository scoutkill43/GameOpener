from tkinter import *
import winsound
class Crack:
    def play_sound(self):
        winsound.PlaySound('Crack.wav', winsound.SND_FILENAME)
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.slogan = Button(frame,
                                text='Crack',
                                fg="red",
                                command=self.play_sound)
        self.slogan.pack(side=LEFT)


root = Tk()
crack = Crack(root)
root.mainloop()
