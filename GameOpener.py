from tkinter import *
import winsound, os
class Crack:
    def open_app3(self):
        os.startfile('C:\Program Files (x86)\Cube World\CubeLauncher.exe')
    def open_app2(self):
        os.startfile('C:\Program Files (x86)\Steam\steamapps\common\Arma 3\Arma3launcher.exe')
    def open_app(self):
        os.startfile('D:\SteamLibrary\steamapps\common\DARK SOULS III\Game\DarkSoulsIII.exe')
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.slogan = Button(frame,
                                text='Dark Souls III',
                                fg="red",
                                command=self.open_app)
        self.slogan.pack(side=TOP)
        self.button = Button(frame,
                             text='Arma III',
                             fg="green",
                             command=self.open_app2)
        self.button.pack(side=TOP)
        self.button = Button(frame,
                             text='Cube World',
                             fg="blue",
                             command=self.open_app3)
        self.button.pack(side=TOP)


root = Tk()
crack = Crack(root)
root.mainloop()
