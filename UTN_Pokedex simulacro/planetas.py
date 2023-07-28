# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
################# INTRODUCCION #################
#? El profesor OAK de pueblo paleta quiere que construyas un segundo modelo prototipico 
#? de pokedex con 10 pokemones de prueba.
'''
NOMBRE = 'Matias Donati' # Completa tu nombre completo solo en esa variable
'''


#?################ ENUNCIADO #################


Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:

    * El nombre del pokemon.
    * El tipo de color (azul , amarillo, blanco , otro).
    * La altura del pokemon en centimetros (validar que sea mayor a 10 y menor a 200).

B)  Al presionar el boton "Mostrar Pokedex" se deberan listar los pokemones y su posicion en la 
    lista (por terminal), adicionalmente mostrar el informe del punto C.

#!################ ACLARACION IMPORTANTE #################
Del punto C SOLO debera realizar DOS informes.
Para determinar que informe hacer, tenga en cuenta lo siguiente:

    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)
    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
        Realiza el informe correspondiente al numero obtenido.

EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR.
C)
    #! 0) - Cantidad de pokemones de color amarillo.
    #! 1) - Cantidad de pokemones de color blanco.

    #! 2) - Nombre, color y altura del pokemon mas alto.
    #! 3) - Nombre, color y altura del pokemon mas bajo.

    #! 4) - Cantidad de pokemones con mas de 100 cm de altura.
    #! 5) - Cantidad de pokemones con menos de 100 cm de altura.

    #! 6) - color de los pokemones del color que mas pokemones posea.
    #! 7) - color de los pokemones del color que menos pokemones posea.

    #! 8) - el promedio de altura de todos los pokemones ingresados.
    #! 9) - el promedio de altura de todos los pokemones azules.
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title(f"UTN FRA - Pokedex de {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Pokedex de {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        # self.image = tk.PhotoImage(file='Logo_UTN_App.png')

        # self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
        # self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Pokedex", command=self.btn_mostrar_pokedex_on_click)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        # Cargar aca los pokemones
        self.lista_nombre_planetas = ["Saturno", "Marte", "Venus", "Neptuno", "Júpiter", "Mercurio", "Urano", "Tierra", "Plutón", "Ceres",
        "Eris", "Haumea", "Sedna", "Makemake", "Orcus", "Quaoar", "Varuna", "Ixion", "Huya", "Salacia",
        "Gonggong", "Vesta", "Juno", "Pallas", "Palas", "Caronte", "Ganimedes", "Calisto", "Europa", "Ganímedes",
        "Deimos", "Fobos", "Ganimedes", "Oberón", "Titania", "Caliban", "Belinda", "Larissa", "Miranda",
        "Proteo", "Rosalinda", "Setebos", "Perdita", "Ceres", "Miranda", "Elara", "Titania", "Phobos", "Palas",
        "Makemake"]
        self.lista_distancia_planetas = [78900, 40650, 52100, 20100, 45000, 98000, 75230, 67900, 31500, 23400,
        56780, 45600, 89000, 77700, 61000, 30000, 80000, 95400, 42100, 99300,
        25000, 34500, 43200, 99999, 20001, 88888, 34567, 98765, 54321, 78901,
        87654, 65432, 98765, 67890, 54321, 90123, 21098, 45678, 12345, 87654,
        23456, 78901, 78900, 87650, 23400, 56780, 90120, 12340, 60123, 90876]
        self.lista_color_planetas = ["NARANJA", "AMARILLO", "VIOLETA", "GRIS", "VIOLETA", "NARANJA", "AMARILLO", "NARANJA", "VIOLETA", "GRIS",
        "NARANJA", "GRIS", "AMARILLO", "NARANJA", "VIOLETA", "GRIS", "VIOLETA", "NARANJA", "AMARILLO", "VIOLETA",
        "NARANJA", "GRIS", "NARANJA", "AMARILLO", "GRIS", "NARANJA", "VIOLETA", "NARANJA", "GRIS", "AMARILLO",
        "NARANJA", "VIOLETA", "GRIS", "VIOLETA", "NARANJA", "AMARILLO", "GRIS", "VIOLETA", "NARANJA", "AMARILLO",
        "NARANJA", "VIOLETA", "GRIS", "NARANJA", "VIOLETA", "AMARILLO", "GRIS", "NARANJA", "AMARILLO", "VIOLETA"]

    def btn_cargar_pokedex_on_click(self):
        for indice in range(100):
            nombre = prompt("",f"Nombre del Planeta {indice + 1}")
            while nombre == None or nombre == "" or len(nombre) < 4:
                nombre = prompt("",f"Nombre del Planeta {indice + 1} 4 LETRAS MINIMO")
            self.lista_nombre_planetas.append(nombre)

            distancia = prompt("", "Tamaño")
            while int(distancia) < 20000 or int(distancia) > 100000:
                distancia = prompt("", "Tamaño .. entre 20.000 y 100.000")
            distancia = int(distancia)
            self.lista_distancia_planetas.append(distancia)

            color = prompt("", "Color").upper()
            while color != "NARANJA" and color != "AMARILLO" and color != "VIOLETA" and color != "GRIS":
                color = prompt("", "Color ... NARANJA AMARILLO VIOLETA O GRIS").upper()
            self.lista_color_planetas.append()

    def btn_mostrar_pokedex_on_click(self):

        menos_de_70000 = 0
        menos_de_70_naranja = 0
        menos_de_70_amarillo = 0
        menos_de_70_violeta = 0
        menos_de_70_gris = 0
        acumulador_menos_de_70 = 0

        contador_naranja = 0
        contador_amarillo = 0
        contador_violeta = 0
        contador_gris = 0

        contador_entre_80_y_90 = 0
        suma_entre_80_y_90 = 0

        contador_contiene_letra_S = 0
        acum_80_90_empiezan_con_S = 0

        maxima_distancia = None
        minima_distancia = None

        suma_distancia = 0

        lista_planetas_contienen_S= []

        for indice in range(len(self.lista_nombre_planetas)):

            if self.lista_distancia_planetas[indice] < 70000:
                menos_de_70000 += 1
                acumulador_menos_de_70 += 1

                match self.lista_color_planetas[indice]:
                    case "NARANJA":
                        menos_de_70_naranja += 1
                    case "AMARILLO":
                        menos_de_70_amarillo += 1
                    case "VIOLETA":
                        menos_de_70_violeta += 1
                    case _:
                        menos_de_70_gris += 1

            suma_distancia += self.lista_distancia_planetas[indice]

            match self.lista_color_planetas[indice]:
                case "NARANJA":
                   contador_naranja += 1
                case "AMARILLO":
                    contador_amarillo += 1
                case "VIOLETA":
                        contador_violeta += 1
                case _:
                    contador_gris += 1

            if maxima_distancia == None or self.lista_distancia_planetas[indice] > maxima_distancia:
                nombre_maxima_distancia = self.lista_nombre_planetas[indice]
                color_maxima_distancia = self.lista_color_planetas[indice]
                maxima_distancia = self.lista_distancia_planetas[indice]

            if minima_distancia == None or self.lista_distancia_planetas[indice] < minima_distancia:
                nombre_minima_distancia = self.lista_nombre_planetas[indice]
                color_minima_distancia = self.lista_color_planetas[indice]
                minima_distancia = self.lista_distancia_planetas[indice]

            if self.lista_distancia_planetas[indice] > 80000 and self.lista_distancia_planetas[indice] < 90000:

                contador_entre_80_y_90 += 1
                suma_entre_80_y_90 += self.lista_distancia_planetas[indice]

                for indice_letra in range(len(self.lista_nombre_planetas[indice])):
                    informe = f"""Nombre "{self.lista_nombre_planetas[indice]}"\nLa letra "{self.lista_nombre_planetas[indice][indice_letra]}" esta en el indice {indice_letra} """
                    # print(informe)
                    if self.lista_nombre_planetas[indice][0] == "S":
                        acum_80_90_empiezan_con_S += 1
                        self.informe_primer_letra = f"Hay {acum_80_90_empiezan_con_S} planetas que empiezan con la letra S q estan entre 80.000 y 90.000"
                    if self.lista_nombre_planetas[indice][indice_letra] == "S" or self.lista_nombre_planetas[indice][indice_letra] == "s":
                        contador_contiene_letra_S += 1
                        lista_planetas_contienen_S.append(self.lista_nombre_planetas[indice])

        informe_2 = f"Hay {contador_contiene_letra_S} planetas que contiene en su nombre la letra 'S' y son {lista_planetas_contienen_S}"
        print(informe_2)

        if contador_naranja > contador_amarillo and contador_naranja > contador_violeta and contador_naranja > contador_gris:
            color_predominante = "Naranja"
        elif contador_amarillo > contador_violeta and contador_amarillo > contador_gris:
            color_predominante = "Amarillo"
        elif contador_violeta > contador_gris:
            color_predominante = "Violeta"
        else:
            color_predominante = "Gris"

        if contador_naranja < contador_amarillo and contador_naranja < contador_violeta and contador_naranja < contador_gris:
            menor_color = "Naranja"
        elif contador_amarillo < contador_violeta and contador_amarillo < contador_gris:
            menor_color = "Amarillo"
        elif contador_violeta < contador_gris:
            menor_color = "Violeta"
        else:
            menor_color = "Gris"

        if menos_de_70_naranja > menos_de_70_amarillo and menos_de_70_naranja > menos_de_70_violeta and menos_de_70_naranja > menos_de_70_gris:
            color_predominante_menor_70_color = "Naranja"
        elif menos_de_70_amarillo > menos_de_70_violeta and menos_de_70_amarillo > menos_de_70_gris:
            color_predominante_menor_70_color = "Amarillo"
        elif menos_de_70_violeta > menos_de_70_gris:
            color_predominante_menor_70_color = "Violeta"
        else:
            color_predominante_menor_70_color = "Gris"

        if menos_de_70_naranja < menos_de_70_amarillo and menos_de_70_naranja < menos_de_70_violeta and menos_de_70_naranja < menos_de_70_gris:
            menos_color_menor_70_color = "Naranja"
        elif menos_de_70_amarillo < menos_de_70_violeta and menos_de_70_amarillo < menos_de_70_gris:
            menos_color_menor_70_color = "Amarillo"
        elif menos_de_70_violeta < menos_de_70_gris:
            menos_color_menor_70_color = "Violeta"
        else:
            menos_color_menor_70_color = "Gris"

        gral_promedio_distancia = suma_distancia / len(self.lista_distancia_planetas)

        promedio_distancia_menos_de_70000 = menos_de_70000 / acumulador_menos_de_70

        informe = f""" Hay {menos_de_70000} planetas a menos de 70.000 minutos del sol y el color predominante de ese grupo es el {color_predominante_menor_70_color}.. del que menos color hay es {menos_color_menor_70_color}.
Y el promedio de distancia los planetas a menos de 70000 minutos del sol es de {promedio_distancia_menos_de_70000} \n
El promedio gral de distancia es de {gral_promedio_distancia}\nEl color predominante en total es {color_predominante} y el que menos hay es {menor_color}\n
El planeta mas lejos del sol es "{nombre_maxima_distancia}" con una distancia de {maxima_distancia} y es de color {color_maxima_distancia}\n
El planeta mas cerca del sol es "{nombre_minima_distancia}" con una distancia de {minima_distancia} y es de color {color_minima_distancia}\n """

        print(informe)

if __name__ == "__main__":
    app = App()
    app.mainloop()

