import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
Nombre: Matias
Apellido: Donati

Piedra, Papel o Tijera (v 2.0):
    Al comenzar el juego generaremos un número RANDOM del 1 al 3 para la selección de la máquina, siendo 1 para “piedra”, el 2 para “papel” y 3 para “tijera”.
    El jugador seleccionará mediante uno de los botones su opción  y le informaremos si ganó, empató o perdió

Ahora debemos informar cuantas veces se ganó, perdió o empató
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

        self.btn_restart = customtkinter.CTkButton(master=self, text="FIN DE JUEGO\nEstadisticas", command=self.btn_fin_on_click, fg_color="green")
        self.btn_restart.grid(row=6, pady=20, columnspan=2, sticky="nsew")

        self.cpu_elije()

        self.contador_vitorias_cpu = 0 
        self.contador_vitorias_player_1 = 0 


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
            self.contador_vitorias_player_1 = self.contador_vitorias_player_1 + 1
        else:
            self.contador_vitorias_cpu = self.contador_vitorias_cpu + 1
            mensaje = "PERDEDOR!"
        alert(message=mensaje)

    def btn_papel_on_click(self):
        self.deshabilitar_botones()
        if self.numero_random == 2:
            mensaje = "FELICITACIONES!"
            self.contador_vitorias_player_1 = self.contador_vitorias_player_1 + 1
        else:
            self.contador_vitorias_cpu = self.contador_vitorias_cpu + 1
            mensaje = "PERDEDOR!"
        alert(message=mensaje)

    def btn_tijera_on_click(self):
        self.deshabilitar_botones()
        if self.numero_random == 3:
            mensaje = "FELICITACIONES!"
            self.contador_vitorias_player_1 = self.contador_vitorias_player_1 + 1
        else:
            self.contador_vitorias_cpu = self.contador_vitorias_cpu + 1
            mensaje = "PERDEDOR!"
        alert(message=mensaje)

    def btn_fin_on_click(self):
        if self.contador_vitorias_player_1 > self.contador_vitorias_cpu:
            mensaje = f"""FELICITACIONES!!\n\n
            Le ganaste al PC !
            Ganate {self.contador_vitorias_player_1} veces y el Pc gańo {self.contador_vitorias_cpu}"""
        else:
             mensaje = f"""LOOSER!\n\n
            Gano el PC
            PC ganó {self.contador_vitorias_cpu} veces y vos {self.contador_vitorias_player_1}."""
        alert(message=mensaje)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()