import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Matias
Apellido: Donati

Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de los televidentes y saber cuál será el participante que deberá abandonar la casa más famosa del mundo.
Los participantes en la placa son: Giovanni, Gianni y Facundo. Fausto no fue nominado y Marina no está en la placa esta semana por haber ganado la inmunidad.

Cada televidente que vota deberá ingresar:

Nombre del votante
Edad del votante (debe ser mayor a 13)
Género del votante (Masculino, Femenino, Otro)
El nombre del participante a quien le dará el voto negativo (Debe estar en placa)
No se sabe cuántos votos entrarán durante la gala.

Se debe informar al usuario:

El promedio de edad de las votantes de género Femenino
Cantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo.
Nombre del votante más joven qué votó a Gianni.
Nombre de cada participante y porcentaje de los votos qué recibió.
El nombre del participante que debe dejar la casa (El que tiene más votos)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):
        seguir_cargando_datos = True
        edades_femenino = []
        lista_facundo_gianni = []
        lsita_votos_gral = []
        suma_edades_fem = 0
        votos_facundo = 0
        votos_giovanni = 0
        votos_gianni = 0
        edad_inicial_votante_mas_chico_gianni = 0
        nombre_votante_mas_chico_gianni = ""
        flag_gianni = True

        while seguir_cargando_datos:

            nombre = prompt("", "Nombre Votante")
            while nombre == None or nombre == "" or nombre.isdigit() == True or len(nombre) < 4:
                nombre = prompt("", "Nombre Votante, LETRAS minimo 4")
            edad = prompt("", "Edad Votante")
            while edad == None or edad == "" or edad.isdigit() == False or int(edad) < 14:
                edad = prompt("", "Edad Votante.. NUMERO MAYOR A 13")
            edad = int(edad)
            genero = prompt("", "Genero").upper()
            while genero == None or genero == "" or genero.isdigit() == True or genero != "M" and genero != "F" and genero != "OTRO":
                genero = prompt("", "Genero .. M, F u OTRO").upper()
            nombre_participante = prompt("", "Voto negativo para ...").upper()
            while nombre_participante == None or nombre_participante == "" or nombre_participante.isdigit() == True or nombre_participante != "GIOVANNI" and nombre_participante != "GIANNI" and nombre_participante != "FACUNDO":
                nombre_participante = prompt("", "Voto negativo para Giovanni, Gianni o Facundo").upper()

            if genero == "F":
                edades_femenino.append(edad)

            if genero == "M" and edad >= 25 and edad <=40 and nombre_participante == "FACUNDO" or nombre_participante == "GIOVANNI":
                lista_facundo_gianni.append(nombre_participante)

            lsita_votos_gral.append(nombre_participante)

            if nombre_participante == "FACUNDO":
                votos_facundo = votos_facundo + 1
            elif nombre_participante == "GIANNI":
                votos_gianni = votos_gianni +1
            else:
                votos_giovanni = votos_giovanni + 1

            seguir_cargando_datos = question("", "Seguir cargando votantes?")

        for el in edades_femenino:
            suma_edades_fem = suma_edades_fem + el

        for el in lsita_votos_gral:

            if el == "GIANNI":
                if flag_gianni:
                    edad_inicial_votante_mas_chico_gianni = edad
                    nombre_votante_mas_chico_gianni = nombre
                    flag_gianni = False
                if edad < edad_inicial_votante_mas_chico_gianni:
                    nombre_votante_mas_chico_gianni = nombre
                votos_gianni = votos_gianni + 1
            elif el == "FACUNDO":
                votos_facundo = votos_facundo + 1
            else:
                votos_giovanni = votos_giovanni + 1

        suma_votos = votos_facundo + votos_gianni + votos_giovanni

        porcetaje_facundo = (votos_facundo / suma_votos) * 100
        porcentaje_facundo_redondeado = round(porcetaje_facundo, 2)

        porcetaje_gianni = (votos_gianni / suma_votos) * 100
        porcetaje_gianni_redondeado = round(porcetaje_gianni, 2)

        porcentaje_giovanni = (votos_giovanni / suma_votos) * 100
        porcentaje_giovanni_redondeado = round(porcentaje_giovanni, 2)


        if votos_gianni > votos_facundo and votos_gianni > votos_giovanni:
            perdedor = f"Gianni con {votos_gianni}"
        elif votos_facundo > votos_giovanni:
            perdedor = f"Facundo con {votos_facundo}"
        else:
            perdedor = f"Giovanni con {votos_giovanni}"

        cantidad_votos_facu_gianni = len(lista_facundo_gianni)

        promedio_edad_femenino = suma_edades_fem / len(edades_femenino)

        mensaje = f"""Promedio Edad Votantes Femenino: {promedio_edad_femenino}\n
        Cantidad Masculino entre 25 y 40 que Votaron a Giovanni o Facundo: {cantidad_votos_facu_gianni}\n
        Nombre Votante más joven qué votó a Gianni: {nombre_votante_mas_chico_gianni}\n
        Porcentaje votos totales:\n Gianni: {porcetaje_gianni_redondeado}\n
        Facundo {porcentaje_facundo_redondeado}\n Giovanni {porcentaje_giovanni_redondeado}\n
        El participante que debe dejar la casa es {perdedor}"""

        alert(message=mensaje)

    def btn_mostrar_estadisticas_on_click(self):
        pass

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()