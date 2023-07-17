import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
==============
 Matias Donati
==============

Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_limpiar = customtkinter.CTkButton(master=self, text="Limpiar", command=self.btn_limpiar_on_click)


    def btn_comenzar_ingreso_on_click(self):
        self.btn_limpiar_on_click()
        lista_de_numeros = []
        contador = 0
        suma = 0
        self.flag_btn_limpiar = False

        while contador < 5:
            contador += 1
            numero_ingresado = int(prompt("", "Ingresa un número"))
            lista_de_numeros.append(numero_ingresado)

        for numero in lista_de_numeros:
            suma = suma + numero

        promedio = suma / len(lista_de_numeros)

        self.txt_suma_acumulada.insert(0, suma)
        self.txt_promedio.insert(0, promedio)

        self.flag_btn_limpiar = True

        if(self.flag_btn_limpiar):
            self.btn_limpiar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")

    def btn_limpiar_on_click(self):
        self.txt_suma_acumulada.delete(0, 10000)
        self.txt_promedio.delete(0, 10000)
        self.btn_limpiar.grid_remove()


if __name__ == "__main__":
    app = App()
    app.mainloop()



lista = [2, 3, 4, "asd", True]
len(lista)