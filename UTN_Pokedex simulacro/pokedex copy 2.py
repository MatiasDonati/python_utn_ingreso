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
import os
#! No tocar
command = 'py' if os.name in ['ce', 'nt', 'dos'] else 'python3'
os.system(f'{command} -m pip install -r requirements.txt')
#! No tocar
import customtkinter

'''
MATIAS DONATI

#? El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con 
#? algunos pokemones de prueba.

Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Tierra, Psiquico, Fuego, Electrico)
    * La cantidad de poder (validar que sea mayor a 50 y menor a 200)

B) Al presionar el boton "Mostrar Pokedex" se deberan listar los pokemones y su posicion en la lista (por terminal)
y mostrar el informe del punto C.

ACLARACION:
Del punto C SOLO debera realizar DOS informes.
Para determinar que informe hacer, tenga en cuenta lo siguiente:

    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5).
        Realiza el informe correspondiente al numero obtenido.

EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR.
C)
    #! 0) - Cantidad de pokemones de tipo Fuego
    #! 1) - Cantidad de pokemones de tipo Electrico 

    #! 2) - Nombre, tipo y Poder del pokemon con el poder mas alto
    #! 3) - Nombre, tipo y Poder del pokemon con el poder mas bajo

    #! 4) - Cantidad de pokemones, con mas de 100 de poder
    #! 5) - Cantidad de pokemones, con menos de 100 de poder

    #! 6) - tipo de los pokemones del tipo que mas pokemones posea
    #! 7) - tipo de los pokemones del tipo que menos pokemones posea

    #! 8) - el promedio de poder de todos los ingresados
    #! 9) - el promedio de poder de todos los pokemones de Electrico
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Pokedex", font=("Arial", 20, "bold"))
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
        self.lista_poder_pokemones = []
        self.lista_tipo_pokemones = []


    def btn_cargar_pokedex_on_click(self):
        for indice in range(3):
            nombre = prompt("", f"Nombre {indice + 1}")
            tipo = prompt("", f"Tipo {indice+1}").upper()
            while tipo != "AGUA" and tipo != "TIERRA" and tipo != "PSIQUICO" and tipo != "FUEGO" and tipo != "ELECTRICO":
                tipo = prompt("", f"Tipo {indice+1}\nAgua, Tierra, Psiquico, Fuego, Electrico").upper()
            poder = prompt("", "Poder")
            while poder.isdigit() == False or int(poder) < 50 or int(poder) > 200:
                poder = prompt("", "Poder\nMayor a 50 y menor a 200")
            poder = int(poder)

            self.lista_nombre_pokemones.append(nombre)
            self.lista_tipo_pokemones.append(tipo)
            self.lista_poder_pokemones.append(poder)

    def btn_mostrar_pokedex_on_click(self):

        contador_agua = 0
        contador_tierra = 0
        contador_psiquico = 0
        contador_fuego = 0
        contador_electrico = 0

        poderes_mayor_a_100 = 0
        poderes_menor_a_100 = 0
        maximo_poder = None
        minimo_poder = None

        suma_poderes = 0

        suma_poderes_electricos = 0
        cantidad_poderes_electricos = 0

        for indice in range(len(self.lista_nombre_pokemones)):
            print(f"El pokemon {self.lista_nombre_pokemones[indice]} es de tipo {self.lista_tipo_pokemones[indice]} y tiene un poder de {self.lista_poder_pokemones[indice]}")

            match self.lista_tipo_pokemones[indice]:
                case "AGUA":
                    contador_agua += 1
                case "TIERRA":
                    contador_tierra += 1
                case "PSIQUICO":
                    contador_psiquico += 1
                case "FUEGO":
                    contador_fuego += 1
                case _:
                    contador_electrico += 1

            if self.lista_poder_pokemones[indice] > 100:
                poderes_mayor_a_100 += 1
            elif self.lista_poder_pokemones[indice] < 100:
                poderes_menor_a_100 += 1

            if maximo_poder == None or self.lista_poder_pokemones[indice] > maximo_poder:
                maximo_poder = self.lista_poder_pokemones[indice]
                nombre_maximo_poder = self.lista_nombre_pokemones[indice]
                tipo_maximo_poder = self.lista_tipo_pokemones[indice]

            if minimo_poder == None or self.lista_poder_pokemones[indice] < minimo_poder:
                minimo_poder = self.lista_poder_pokemones[indice]
                nombre_minimo_poder = self.lista_nombre_pokemones[indice]
                tipo_minimo_poder = self.lista_tipo_pokemones[indice]

            if self.lista_tipo_pokemones[indice] == "ELECTRICO":
                suma_poderes_electricos += self.lista_poder_pokemones[indice]
                cantidad_poderes_electricos += 1


        if contador_agua > contador_tierra and contador_agua > contador_psiquico and contador_agua > contador_fuego and contador_agua > contador_electrico:
            mayor_tipo = "AGUA"
        elif contador_tierra > contador_psiquico and contador_tierra > contador_fuego and contador_tierra > contador_electrico:
            mayor_tipo = "TIERRA"
        elif contador_psiquico > contador_fuego and contador_psiquico > contador_electrico:
            mayor_tipo = "PSIQUICO"
        elif contador_fuego > contador_electrico:
            mayor_tipo = "FUEGO"
        else:
            mayor_tipo = "ELECTRICO"

        if contador_agua < contador_tierra and contador_agua < contador_psiquico and contador_agua < contador_fuego and contador_agua < contador_electrico:
            menor_tipo = "AGUA"
        elif contador_tierra < contador_psiquico and contador_tierra < contador_fuego and contador_tierra < contador_electrico:
            menor_tipo = "TIERRA"
        elif contador_psiquico < contador_fuego and contador_psiquico < contador_electrico:
            menor_tipo = "PSIQUICO"
        elif contador_fuego < contador_electrico:
            menor_tipo = "FUEGO"
        else:
            menor_tipo = "ELECTRICO"

        for elemento in self.lista_poder_pokemones:
            suma_poderes += elemento


        promedio_poderes = suma_poderes / len(self.lista_poder_pokemones)

        if cantidad_poderes_electricos > 0:
            promedio_poderes_electricos = suma_poderes_electricos / cantidad_poderes_electricos

        informe = f"""  """

if __name__ == "__main__":
    app = App()
    app.mainloop()
