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

        nb_js_asp = 0
        flag_junior = True
        nombre_junior = ""
        lista_masculinos = []
        lista_femeninos = []
        lista_no_binarios = []
        python = 0
        js = 0
        asp_net = 0
        tecnologia_ganadora = ""

        for i in range(10):

            nombre = prompt("", f"Nombre postulante {i + 1}")
            while nombre == None or nombre == "" or nombre.isdigit() == True or len(nombre) <4:
                nombre = prompt("", f"Nombre postulante {i + 1}")

            edad = prompt("", f"Edad postulante {i + 1}")
            while edad == None or edad.isdigit() == False or int(edad) < 18:
                edad = prompt("", f"Edad postulante {i + 1}")
            edad = int(edad)

            genero = prompt("", f"Género postulante {i + 1}").upper()
            while genero == None or genero == "" or genero.isdigit() == True:
                genero = prompt("", f"Género postulante {i + 1}").upper()
            while genero != "M" and genero != "F" and genero != "NB":
                genero = prompt("", f"Género... M, F ó NB \n postulante {i + 1}").upper()

            tecnologia = prompt("", f"Tecnología postulante {i + 1}").upper()
            while tecnologia == None or tecnologia == "" or tecnologia.isdigit() == True:
                tecnologia = prompt("", f"Tecnología postulante {i + 1}").upper()
            while tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET":
                tecnologia = prompt("", f"Tecnología... PYTHON, JS ó ASP.NET \n postulante {i + 1}").upper()

            puesto = prompt("", f"Puesto postulante {i + 1}").upper()
            while puesto == None or puesto == "" or puesto.isdigit() == True:
                puesto = prompt("", f"Puesto postulante {i + 1}").upper()
            while puesto != "JR" and puesto != "SSR" and puesto != "SR":
                puesto = prompt("", f"Puesto... Jr, Ssr ó Sr \n postulante {i + 1}").upper()

            if edad >= 25 and edad <= 40 and genero == "NB" and tecnologia == "JS" or tecnologia == "ASP.NET" and puesto == "SSR":
                nb_js_asp = nb_js_asp + 1

            if puesto == "JR":
                while flag_junior:
                    edad_jr = edad
                    nombre_junior = nombre
                    flag_junior = False
                if edad < edad_jr:
                    nombre_junior = nombre
           
            if genero == "M":
                lista_masculinos.append(edad)
            elif genero == "F":
                lista_femeninos.append(edad)
            else:
                lista_no_binarios.append(edad)

            if tecnologia == "ASP.NET":
                asp_net = asp_net + 1
            elif tecnologia == "JS":
                js = js + 1
            else:
                python = python + 1
       
        if asp_net > js and asp_net > python:
            tecnologia_ganadora = "ASP.NET"
        elif js > python:
            tecnologia_ganadora = "JavaScrpit"
        else:
            tecnologia_ganadora = "Python"

        suma_masculinos = 0
        for i in lista_masculinos:
            suma_masculinos = suma_masculinos + i
           
        suma_femeninos = 0
        for i in lista_femeninos:
            suma_femeninos = suma_femeninos + i
           
        suma_no_binarios = 0
        for i in lista_no_binarios:
            suma_no_binarios = suma_no_binarios + i
       
        promedio_edad_masculinos = suma_masculinos / len(lista_masculinos)
        promedio_edad_femeninos = suma_femeninos / len(lista_femeninos)
        promedio_edad_no_binarios = suma_no_binarios / len(lista_no_binarios)
           
        total_generos = suma_femeninos + suma_masculinos + suma_no_binarios


        porcentaje_masculino = (suma_masculinos / total_generos) * 100
        porc_masc_redondeado = round(porcentaje_masculino, 2)
   
        porcentaje_femenino = (suma_femeninos / total_generos) * 100
        porc_fem_redondeado = round(porcentaje_femenino, 2)

        porcentaje_no_binario = (suma_no_binarios / total_generos) * 100
        porc_no_bin_redondeado = round(porcentaje_no_binario, 2)

   
        mensaje = f"""La cantidad de postulantes de genero no binario que programan en ASP.NET o JS cuya edad este entre 25 y 40,
        que se postularon para un puesto Ssr es de un total de {nb_js_asp} personas.\n\n El postulante Jr. con menor edad es {nombre_junior}.
        El promedio de edades de genero Masculino es de {promedio_edad_masculinos}
        El promedio de edades de genero Femenino es de {promedio_edad_femeninos}
        El promedio de edades de genero No Binario es de {promedio_edad_no_binarios}
        La tencologia con mas postulantes es {tecnologia_ganadora}
        El porcentaje de postulantse masculinos es de %{porc_masc_redondeado}
        El porcentaje de postulantse femenino es de %{porc_fem_redondeado}
        El porcentaje de postulantse no_binario es de %{porc_no_bin_redondeado}"""

        alert(message=mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()