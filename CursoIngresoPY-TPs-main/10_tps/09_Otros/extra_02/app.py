import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
Nombre: Matias
Apellido: Donati

Enunciado:

La UTN nos solicita la creación de una aplicación para obtener información 
estadistica de las evaluaciones.

1. Al presionar el botón "Ingresar notas", se deberá solicitar mediante prompt 
las notas del los alumn@s. 

	A - Se deberá repetir la solicitud hasta que el usuario haga clic en el botón  
    "Cancelar" del prompt
	B - Se deberá validar que la nota sea un numero entero entre el 0 y el 10.
	C - Las notas ingresadas se deberán ir guardando en una lista.

2. Al presionar el botón "Mostrar notas" debemos mostrar por la terminal el 
listado de las notas, primero indicando su posición en la lista y luego el 
valor de la nota. Con el siguiente formato:

        "1 - Nota: 8"
        "2 - Nota: 4"
        "3 - Nota: 10"
        ...

3. Al presionar el botón "Generar Informe" se deberá mostrar mediante alert 
la siguiente información:

	A - Nota mas baja
	B - Nota mas alta
	C - Promedio de todas las notas
	D - Cantidad de evaluaciones con nota 10
	E - En el caso que el promedio sea menor a 3, informar con la leyenda: "El promedio desaprobo"
	En el caso que el promedio sea mayor a 4: "El promedio aprobo"
	En el caso que el promedio sea mayor a 7: "El promedio promocionó"

	Para el punto E se deberá utilizar match.

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_ingresar_notas = customtkinter.CTkButton(master=self, text="Ingresar Notas", command=self.btn_ingresar_notas_on_click)
        self.btn_ingresar_notas.grid(row=0, pady=20, columnspan=2, sticky="news")

        self.btn_mostrar_notas = customtkinter.CTkButton(master=self, text="Mostrar Notas", command=self.btn_mostrar_notas_on_click)
        self.btn_mostrar_notas.grid(row=1, pady=20, columnspan=2, sticky="news")

        self.btn_generar_informe_notas = customtkinter.CTkButton(master=self, text="Generar Informe de Notas", command=self.btn_generar_informe_notas_on_click)
        self.btn_generar_informe_notas.grid(row=2, pady=20, columnspan=2, sticky="news")

    def btn_ingresar_notas_on_click(self):

        self.lista_notas = []
        self.contador = 0
        flag = True
        self.suma_notas = 0
        self.cantidad_10 = 0

        while flag:
            self.contador += 1
            nota_ingresada = prompt("", f"Ingrese Nota nro{self.contador}")
            if nota_ingresada == None:
                break
            while nota_ingresada == "" or nota_ingresada.isalpha() == True or int(nota_ingresada) < 0 or int(nota_ingresada) > 10:
                nota_ingresada = prompt("", f"Ingrese Nota nro{self.contador} ..  entre 0 y 10")
                if nota_ingresada == None:
                    flag = False
                    break

            nota_ingresada = int(nota_ingresada)
            self.lista_notas.append(nota_ingresada)
        # alert(message=self.lista_notas)

    def btn_mostrar_notas_on_click(self):
        for indice in range(len(self.lista_notas)):
            numero = self.lista_notas[indice]
            print(f"{indice + 1} - Nota: {numero}")

    def btn_generar_informe_notas_on_click(self):
        flag_nota = True
        for nota in self.lista_notas:
            if flag_nota:
                self.nota_mas_baja = nota
                self.nota_mas_alta = nota
                flag_nota = False
            if nota < self.nota_mas_baja:
                self.nota_mas_baja = nota
            if nota > self.nota_mas_alta:
                self.nota_mas_alta = nota
            self.suma_notas = self.suma_notas + nota
            if nota == 10:
                self.cantidad_10 += 1
        promedio = self.suma_notas / len(self.lista_notas)
        promedio_redondeado = round(promedio, 2)

        match promedio_redondeado:
            case 0 | 1| 2 | 3:
                mensaje = "El promedio desaprobo"
            case 4 | 5 | 6:
                mensaje = "El promedio aprobo"
            case _:
                mensaje = "El promedio promociono"

        # if promedio_redondeado < 3:
        #     mensaje = "El promedio desaprobo"
        # elif promedio_redondeado >= 4 or promedio_redondeado <= 7:
        #     mensaje = "El promedio aprobo"
        # else:
        #     mensaje = "El promedio promociono"

        alert(message=mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
