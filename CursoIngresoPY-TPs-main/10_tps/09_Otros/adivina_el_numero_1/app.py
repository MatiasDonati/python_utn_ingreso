import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random
import time


'''
Nombre: Matias 
Apellido: Donati

Adivina el número (v 1.0):
Al comenzar el juego generamos un número secreto del 1 al 100, en la pantalla del juego dispondremos de un cuadro de texto 
para ingresar un número y un botón “Verificar”, si el número ingresado es el mismo que el número secreto se dará por terminado
el juego con un mensaje similar a este: 

“Ganaste en X intentos”.
de no ser igual se debe informar si 
“falta…” para llegar al número secreto o si 
“se pasó…” del número secreto.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.txt_numero = customtkinter.CTkEntry(master=self)
        self.txt_numero.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Chequear", command=self.btn_mostrar_on_click)
        # self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.btn_reset = customtkinter.CTkButton(master=self, text="Reset", command=self.btn_reset_on_click)
        # self.btn_reset.grid(row=3, pady=20, columnspan=2, sticky="nsew")

        self.inicio_juego()

        self.after(2500, self.mostrar_botones)

        alert(message="Bienvenido, tenes que adivivnar un numero azaroso.\n Tenes UN MINUTO! \n YA CORRE EL TIEMPO \n Que tengas suerte!")


    def mostrar_botones(self):
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        self.btn_reset.grid(row=3, pady=20, columnspan=2, sticky="nsew")
        self.after(60000, self.mensaje_perdedor)

    def mensaje_perdedor(self):
        self.borrar_boton()
        alert(message='Perdiste, paso un minuto... \n Volve a intentarlo')

    def borrar_boton(self):
        self.btn_mostrar.grid_remove()
        # ó grid.forget()


    def btn_reset_on_click(self):
        self.mostrar_botones()
        self.inicio_juego()

    def btn_mostrar_on_click(self):


        if(self.flag_play):
            numero_jugador_texto = self.txt_numero.get()
            numero_jugaror_numero = int(numero_jugador_texto)
            self.numero_intento += 1


            if  (numero_jugaror_numero == self.numero_secreto):
                ts_fin_juego = time.time()
                tiempo_de_juego = int(ts_fin_juego - self.ts_inicio_juego)
                mensaje = f"Felicitaciones! Ganaste en {self.numero_intento} intentos en {tiempo_de_juego} segundos \n Reset para volver a Jugar!."
                self.borrar_boton()
                self.flag_play = False
            elif(numero_jugaror_numero > self.numero_secreto):
                mensaje = "Se pasó!!"
            else:
                mensaje="Falta!!"

            self.txt_numero.delete(0, 1000)
            alert(message=mensaje)


    def inicio_juego(self):
        self.numero_intento = 0
        self.numero_secreto = random.randrange(1, 100)
        self.flag_play = True
        print(self.numero_secreto)
        self.ts_inicio_juego = time.time()



if __name__ == "__main__":
    app = App() 
    app.geometry("300x300")
    app.mainloop()