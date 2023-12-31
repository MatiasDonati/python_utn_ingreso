import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
==========
Matias Donati
==========
Al presionar el botón Mostrar 5 veces un mensaje (utilizando el Dialog Alert) con números ASCENDENTES, desde el 1 al 5.
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        decrementador = 5

        for _ in range(5):
            alert(message=decrementador)
            decrementador = decrementador -1

        # numeros = [1, 2, 3, 4, 5]

        # for el in numeros:
        #     alert(message=el)
        #     if  el == 5:
        #         alert(message="ULTIMO BUCLE, CHAU!!")

if __name__ == "__main__":
    app = App()
    app.mainloop()