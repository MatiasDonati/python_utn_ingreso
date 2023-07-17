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
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        flag_ingresa_numero = True

        lista_de_numeros = []
        suma_positivos = 0
        suma_negativos = 0
        cantidad_numeros_positivos = 0
        cantidad_numeros_negativos = 0
        cantidad_de_ceros = 0
        diferencia_entre_negativos_y_positivos = 0


        while flag_ingresa_numero:
            entrada = prompt("", "INGRESA NUMERO \n !!! SOLO NUMERO !!")
            if entrada:
                lista_de_numeros.append(int(entrada))
            else:
                flag_ingresa_numero = False
                for el in lista_de_numeros:
                   if el > 0:
                        cantidad_numeros_positivos = cantidad_numeros_positivos + 1
                        suma_positivos = suma_positivos + el
                   if el < 0:
                        cantidad_numeros_negativos = cantidad_numeros_negativos + 1
                        suma_negativos = suma_negativos + el
                   if el == 0:
                        cantidad_de_ceros = cantidad_de_ceros + 1

                diferencia_entre_negativos_y_positivos = cantidad_numeros_positivos - cantidad_numeros_negativos
                if(diferencia_entre_negativos_y_positivos < 0):
                    diferencia_entre_negativos_y_positivos = abs(diferencia_entre_negativos_y_positivos)

        mensaje = f"La suma acumulada de los positivos es: {suma_positivos} \n\n La suma acumulada de los negativos es: {suma_negativos} \n\n  Cantidad de números positivos ingresados: {cantidad_numeros_positivos} \n\n Cantidad de números negativos ingresados: {cantidad_numeros_negativos} \n\n Cantidad de ceros: {cantidad_de_ceros} \n\n Diferencia entre la cantidad de los números positivos ingresados y los negativos es: {diferencia_entre_negativos_y_positivos}"

        alert(message=mensaje)

if __name__ == "__main__":
    app = App()
    app.mainloop()
