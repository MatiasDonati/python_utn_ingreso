import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
Nombre:
Apellido:

Piedra, Papel o Tijera (v 1.0):
    Al comenzar el juego generaremos un número RANDOM del 1 al 3 para la selección de la máquina, siendo 1 para “piedra”, el 2 para “papel” y 3 para “tijera”.
    El jugador seleccionará mediante uno de los botones su opción y le informaremos si ganó, empató o perdió
'''

class App(customtkinter.CTk):
     
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_piedra = customtkinter.CTkButton(master=self, text="Piedra", command=self.btn_piedra_on_click)
        self.btn_piedra.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_papel = customtkinter.CTkButton(master=self, text="Papel", command=self.btn_papel_on_click)
        self.btn_papel.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_tijera = customtkinter.CTkButton(master=self, text="Tijera", command=self.btn_tijera_on_click)
        self.btn_tijera.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_restart = customtkinter.CTkButton(master=self, text="RESTART", command=self.btn_restart_on_click, fg_color="red")
        self.btn_restart.grid(row=5, pady=20, columnspan=2, sticky="nsew")
       
        self.cpu_elije()  

    def deshabilitar_botones(self):
        self.btn_piedra.configure(state="disabled")
        self.btn_papel.configure(state="disabled")
        self.btn_tijera.configure(state="disabled")

    def btn_restart_on_click(self):
        self.btn_piedra.configure(state="normal")
        self.btn_papel.configure(state="normal")
        self.btn_tijera.configure(state="normal")
        self.cpu_elije()

    def cpu_elije(self):
        self.numero_random = random.randrange(1, 4)
        print(self.numero_random)

    def btn_piedra_on_click(self):
        self.deshabilitar_botones()
        if self.numero_random == 1:
            mensaje = "FELICITACIONES!"
        else:
            mensaje = "PERDEDOR!"
        alert(message=mensaje)

    def btn_papel_on_click(self):
        self.deshabilitar_botones()
        if self.numero_random == 2:
            mensaje = "FELICITACIONES!"
        else:
            mensaje = "PERDEDOR!"
        alert(message=mensaje)

    def btn_tijera_on_click(self):
        self.deshabilitar_botones()
        if self.numero_random == 3:
            mensaje = "FELICITACIONES!"
        else:
            mensaje = "PERDEDOR!"
        alert(message=mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()