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
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt) o el usuario ingrese cero. 
Calcular la suma acumulada de los positivos y multiplicar los negativos. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_producto

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_producto = customtkinter.CTkEntry(master=self, placeholder_text="Producto")
        self.txt_producto.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):

        flag_ingresa_numero = True

        self.txt_suma_acumulada.delete(0, 10000)
        self.txt_producto.delete(0, 10000)

        lista_de_numeros_positivos = []
        lista_de_numeros_negativos = []

        suma_positivos = 0
        multiplicacion_negativos = 1

        while flag_ingresa_numero:
            entrada = prompt("", "INGRESA NUMERO \n !!! SOLO NUMERO !!")
            if entrada:
                # si hay entrada lo paso a int y veo q numero es
                entrada_int = int(entrada)
                if entrada_int == 0:
                    flag_ingresa_numero = False
                    for elemento in lista_de_numeros_positivos:
                        suma_positivos = suma_positivos + elemento
                    for elemento in lista_de_numeros_negativos:
                        multiplicacion_negativos = multiplicacion_negativos * elemento
                    self.txt_suma_acumulada.insert(0, suma_positivos)
                    self.txt_producto.insert(0, multiplicacion_negativos)
                elif entrada_int > 0:
                    lista_de_numeros_positivos.append(entrada_int)
                else:
                    lista_de_numeros_negativos.append(entrada_int)
            else:
                flag_ingresa_numero = False
                for elemento in lista_de_numeros_positivos:
                    suma_positivos = suma_positivos + elemento
                for elemento in lista_de_numeros_negativos:
                    multiplicacion_negativos = multiplicacion_negativos * elemento
                self.txt_suma_acumulada.insert(0, suma_positivos)
                self.txt_producto.insert(0, multiplicacion_negativos)


if __name__ == "__main__":
    app = App()
    app.mainloop()
