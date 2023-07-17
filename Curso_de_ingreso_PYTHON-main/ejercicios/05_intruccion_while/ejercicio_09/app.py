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
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.txt_minimo = customtkinter.CTkEntry(master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):

        flag_ingresa_numero = True

        self.txt_minimo.delete(0, 10000)
        self.txt_maximo.delete(0, 10000)

        lista_de_numeros = []

        while flag_ingresa_numero:
            entrada = prompt("", "INGRESA NUMERO \n !!! SOLO NUMERO !!")
            if entrada:
                lista_de_numeros.append(int(entrada))
            else:
                flag_ingresa_numero = False
                self.numero_mayor = lista_de_numeros[0]
                self.numero_menor = lista_de_numeros[0]
                for el in lista_de_numeros:
                    if el > self.numero_mayor:
                        self.numero_mayor = el
                for el in lista_de_numeros:
                    if el < self.numero_menor:
                        self.numero_menor = el

        self.txt_minimo.insert(0, self.numero_menor)
        self.txt_maximo.insert(0, self.numero_mayor)

if __name__ == "__main__":
    app = App()
    app.mainloop()
