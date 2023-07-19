import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Matias
Apellido: Donati

=== TP 7 (FOR) UTN Factory ===
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F - M - NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
A. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
B. Nombre del postulante Jr con menor edad.
C. Promedio de edades por género.
D. Tecnologia con mas postulantes (solo hay una).
E. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=1, pady=20, columnspan=2, sticky="nsew")


    def btn_validar_on_click(self):
        postulantes = 3
        contador = 0
        nombre = ""
        edad = ""
        genero = ""
        tecnologia = ""
        puesto = ""
        nb_js_asp = 0
        flag_junior = True
        edad_jr = 0

        while contador < postulantes:
            contador += 1
            nombre = prompt("", f"Nombre postulante {contador}")
            while nombre == None or nombre == "" or nombre.isdigit() == True or len(nombre) <4:
                nombre = prompt("", f"Nombre postulante {contador}")

            edad = prompt("", f"Edad postulante {contador}")
            while edad == None or edad.isdigit() == False or int(edad) < 18:
                edad = prompt("", f"Edad postulante {contador}")
            edad = int(edad)

            genero = prompt("", f"Género postulante {contador}").upper()
            while genero == None or genero == "" or genero.isdigit() == True:
                genero = prompt("", f"Género postulante {contador}").upper()
            while genero != "M" and genero != "F" and genero != "NB":
                genero = prompt("", f"Género... M, F ó NB \n postulante {contador}").upper()

            tecnologia = prompt("", f"Tecnología postulante {contador}").upper()
            while tecnologia == None or tecnologia == "" or tecnologia.isdigit() == True:
                tecnologia = prompt("", f"Tecnología postulante {contador}").upper()
            while tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET":
                tecnologia = prompt("", f"Tecnología... PYTHON, JS ó ASP.NET \n postulante {contador}").upper()

            puesto = prompt("", f"Puesto postulante {contador}").upper()
            while puesto == None or puesto == "" or puesto.isdigit() == True:
                puesto = prompt("", f"Puesto postulante {contador}").upper()
            while puesto != "JR" and puesto != "SSR" and puesto != "SR":
                puesto = prompt("", f"Puesto... Jr, Ssr ó Sr \n postulante {contador}").upper()

            if edad >= 25 and edad <= 40 and genero == "NB" and tecnologia == "JS" or tecnologia == "ASP.NET" and puesto == "SSR":
                nb_js_asp = nb_js_asp + 1

            if puesto == "JR":
                while flag_junior:
                    edad_jr = edad
                    flag_junior = False
                if edad_jr > edad:
                    edad_jr = edad


        mensaje = f"La cantidad de postulantes de genero no binario que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr es de {nb_js_asp}\n\n El postulando Jr. con menor edad es de {edad_jr}"

        alert(message=mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()