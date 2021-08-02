import time
from random import randint
from tkinter import *
from random_color import random_color

class App(Tk):

    def __init__(self):
        super().__init__()
        self.title("Poop clicker")
        self.color = random_color()
        self.start()
        self.config(bg=self.color)
        self.resizable(height=False, width=False)
        self.geometry("800x800")
        self.nbr_poop = 0
        self.a = True
        self.b = False


    def start(self):
        try:
            print(self.nbr_poop)
        except:
            self.nbr_poop = 0
        self.a = True
        self.commencer_button = Button(self, text="Commencer", font=("Arial", 50), bg=self.color, command=self.c_parti)
        self.commencer_button.pack(expand=YES)
        if self.nbr_poop != 0:
            self.label_score = Label(self, text="Bravo, ton dernier score était " + str(self.nbr_poop), font=("Arial", 40),
                                     bg=self.color)
            self.label_score.pack(expand=YES)
            self.b = True
        self.nbr_poop = 0

    def c_parti(self):
        if self.b:
            self.label_score.destroy()
        self.commencer_button.destroy()
        self.label_regle = Label(self, text="Vous devez clique sur le plus de caca en 30s !", font=("Arial", 28),
                                 bg=self.color)
        self.label_regle.pack()
        self.button_ready = Button(self, text="Compris", font=("Arial", 28), bg=self.color, command=self.ready)
        self.button_ready.pack()

    def ready(self):
        self.start_time = time.perf_counter()
        self.label_regle.destroy()
        self.button_ready.destroy()
        self.label_compteur = Label(self, text=str(self.nbr_poop), font=("Arial", 20), bg=self.color)
        self.label_compteur.place(x=760, y=0)
        self.img = PhotoImage(file='img/poop.png').subsample(16)
        self.button_poop = Button(self, image=self.img, bg=self.color, bd=0, command=self.add_poop)
        self.button_poop.place(x=randint(0, 750), y=randint(0, 750))

    def add_poop(self):
        if self.a:
            self.nbr_poop += 1
            self.label_compteur['text'] = str(self.nbr_poop)
            self.button_poop.destroy()
            self.button_poop = Button(self, image=self.img, bg=self.color, bd=0, command=self.add_poop)
            self.button_poop.place(x=randint(0, 800), y=randint(0, 800))
            if not (time.perf_counter() - 30) <= self.start_time:
                self.a = False

        else:
            self.button_poop.destroy()
            self.start()
            self.label_compteur.destroy()







App().mainloop()