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
        self.image = tk.PhotoImage(file='Logo_UTN_App.png')

        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Pokedex", command=self.btn_mostrar_pokedex_on_click)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        # Cargar aca los pokemones
        self.lista_nombre_pokemones = []
        self.lista_altura_pokemones = []
        self.lista_color_pokemones = []

    def btn_cargar_pokedex_on_click(self):
        for indice in range(10):
            nombre = prompt("", f"Ingrese el PokeNombre {indice + 1}")
            color = prompt("", "Color de pokemon").upper()
            while color != "AZUL" and color != "AMARILLO" and color != "BLANCO" and color != "OTRO":
                color = prompt("", "Color...azul , amarillo, blanco , otro ").upper()
            altura = prompt("", "Altura")
            while int(altura) < 10 or int(altura) > 200:
                altura = prompt("", "Altura. numero entre 10 y 200")
            altura = int(altura)

            self.lista_nombre_pokemones.append(nombre)
            self.lista_color_pokemones.append(color)
            self.lista_altura_pokemones.append(altura)

    def btn_mostrar_pokedex_on_click(self):

        maxima_altura = None
        minima_altura = None

        contador_azul = 0
        contador_amarillo = 0
        contador_blanco = 0
        contador_otro = 0

        mayores_a_100 = 0
        menores_a_100 = 0

        suma_altura = 0
        suma_altura_azules = 0
        acumulador_azules = 0


        for indice in range(len(self.lista_altura_pokemones)):

            if maxima_altura == None or self.lista_altura_pokemones[indice] > maxima_altura:
                nombre_mas_alto = self.lista_nombre_pokemones[indice]
                maxima_altura = self.lista_altura_pokemones[indice]
                maximo_color = self.lista_color_pokemones[indice]

            if minima_altura == None or self.lista_altura_pokemones[indice] < minima_altura:
                nombre_mas_bajo = self.lista_nombre_pokemones[indice]
                minima_altura = self.lista_altura_pokemones[indice]
                minimo_color = self.lista_color_pokemones[indice]

            match self.lista_color_pokemones[indice]:
                case "AZUL":
                    contador_azul += 1
                case "AMARILLO":
                    contador_amarillo += 1
                case "BLANCO":
                    contador_blanco += 1
                case _:
                    contador_otro += 1

            if self.lista_altura_pokemones[indice] > 100:
                mayores_a_100 += 1
            elif self.lista_altura_pokemones[indice] < 100:
                menores_a_100 += 1

            if self.lista_color_pokemones[indice] == "AZUL":
                suma_altura_azules += self.lista_altura_pokemones[indice]
                acumulador_azules += 1

        if contador_azul < contador_amarillo and contador_azul < contador_amarillo and contador_blanco < contador_azul < contador_otro:
            menor_color = "AZUL"
        elif contador_amarillo < contador_blanco and contador_amarillo < contador_otro:
            menor_color = "AMARILLO"
        elif contador_blanco < contador_otro:
            menor_color = "BLANCO"
        else:
            menor_color = "OTRO"

        if contador_azul > contador_amarillo and contador_azul > contador_amarillo and contador_blanco > contador_azul > contador_otro:
            mayor_color = "AZUL"
        elif contador_amarillo > contador_blanco and contador_amarillo > contador_otro:
            mayor_color = "AMARILLO"
        elif contador_blanco > contador_otro:
            mayor_color = "BLANCO"
        else:
            mayor_color = "OTRO"

        for i in self.lista_altura_pokemones:
            suma_altura += i

        promedio_altura =  suma_altura / len(self.lista_altura_pokemones)

        promedio_altura_azules =  suma_altura_azules / acumulador_azules

        informe = f"""  El pokemon mas alto es {nombre_mas_alto}, con una altura de {maxima_altura} cm. y es de color {maximo_color}\n
                        El color de pokemones que menos hay es {menor_color}\n
                        El color predominantes es el {mayor_color}\n
                        La cantidad de pokemones de color amarllo es de {contador_amarillo}\n
                        La cantidad de pokemones de color blanco es de {contador_blanco}\n
                        Hay {mayores_a_100} mayores a 100 cm y {menores_a_100} menores a 100 cm.\n
                        El pokemon con menos altura es {nombre_mas_bajo}, con una altura de {minima_altura} cm. y es de color {minimo_color}\n
                        El promedio total de altura es de {promedio_altura}\n
                        Y el promedio de altura de color Azul es {promedio_altura_azules}"""

        print(informe)

if __name__ == "__main__":
    app = App()
    app.mainloop()

