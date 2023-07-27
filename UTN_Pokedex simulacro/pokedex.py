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
    #! 0) - Cantidad de pokemones de tipo Fuego                          ===========
    #! 1) - Cantidad de pokemones de tipo Electrico                         ===========

    #! 2) - Nombre, tipo y Poder del pokemon con el poder mas alto           ===========

    #! 3) - Nombre, tipo y Poder del pokemon con el poder mas bajo          ============
    #! 4) - Cantidad de pokemones, con mas de 100 de poder.                 ============
    #! 5) - Cantidad de pokemones, con menos de 100 de poder               ============
    #! 6) - tipo de los pokemones del tipo que mas pokemones posea
    #! 7) - tipo de los pokemones del tipo que menos pokemones posea
    #! 8) - el promedio de poder de todos los ingresados                    ==========
    #! 9) - el promedio de poder de todos los pokemones de Electrico         =============
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
        self.poder_mas_alto = None
        self.poder_mas_bajo = None
        self.indice_poder_mas_alto = None
        self.indice_poder_mas_bajo = None
        self.suma_poderes = 0
        self.cantidad_poke_fuego = 0
        self.cantidad_poke_electrico = 0
        self.poder_mas_de_100 = 0
        self.poder_menos_de_100 = 0
        self.agua = 0
        self.tierra = 0
        self.psiquico = 0
        self.fuego = 0
        self.electrico = 0
        self.suma_poder_electrico = 0
        self.cantidad_poder_electrico = 0
        self.mayor_tipo = ""
        self.contador = 0

    def btn_cargar_pokedex_on_click(self):

        for i in range (5):
            self.contador =+ 1
            nombre_pokemon = prompt("", f"Ingrese el PokeNombre {i + 1}")
            tipo_pokemon = prompt("", "tipo de pokemon").upper()
            while tipo_pokemon != "AGUA" and tipo_pokemon != "TIERRA" and tipo_pokemon != "PSIQUICO" and tipo_pokemon != "FUEGO" and tipo_pokemon != "ELECTRICO":
                tipo_pokemon = prompt("", "tipo de pokemon . Agua, Tierra, Psiquico, Fuego o Agua ").upper()
            cantidad_de_poder = prompt("", "Cantidad de podder")
            while int(cantidad_de_poder) < 50 or int(cantidad_de_poder) > 200:
                cantidad_de_poder = prompt("", "Cantidad de podder.. numero entre 50 y 200")
            cantidad_de_poder = int(cantidad_de_poder)

            self.lista_nombre_pokemones.append(nombre_pokemon)
            self.lista_poder_pokemones.append(tipo_pokemon)
            self.lista_tipo_pokemones.append(cantidad_de_poder)

            if self.poder_mas_alto == None and self.poder_mas_bajo == None:
                self.poder_mas_alto = cantidad_de_poder
                self.poder_mas_bajo = cantidad_de_poder
                self.indice_poder_mas_alto == self.contador
                self.indice_poder_mas_bajo == self.contador
            else:
                if cantidad_de_poder > self.poder_mas_alto:
                    self.poder_mas_alto = cantidad_de_poder
                    self.indice_poder_mas_alto == self.contador
                elif cantidad_de_poder < self.poder_mas_bajo:
                    self.poder_mas_bajo = cantidad_de_poder
                    self.indice_poder_mas_bajo == self.contador

            alert(message=self.indice_poder_mas_alto)
            alert(message=self.indice_poder_mas_bajo)

            if tipo_pokemon == "ELECTRICO":
                self.suma_poder_electrico += cantidad_de_poder
                self.cantidad_poder_electrico += 1

            match tipo_pokemon:
                case "AGUA":
                    self.agua += 1
                case "TIERRA":
                    self.tierra += 1
                case "PSIQUICO":
                    self.psiquico += 1
                case "FUEGO":
                    self.fuego += 1
                case _ :
                    self.tierra += 1

    def btn_mostrar_pokedex_on_click(self):
        for i in range(len(self.lista_nombre_pokemones)):
            mensaje = f"{self.lista_nombre_pokemones[i]} esta en la posicion {i + 1}"
            print(mensaje)
            mensaje2 =  f"""El pokemon con mas poder es {self.lista_nombre_pokemones[self.indice_poder_mas_alto]}
                        es de tipo {self.lista_tipo_pokemones[self.indice_poder_mas_alto]}
                        y tiene un poder de {self.lista_poder_pokemones[self.indice_poder_mas_alto]}
                        y el pokemon con menos poder es {self.lista_nombre_pokemones[self.indice_poder_mas_bajo]},
                        es de tipo {self.lista_tipo_pokemones[self.indice_poder_mas_bajo]}
                        y tiene un poder de {self.lista_poder_pokemones[self.indice_poder_mas_bajo]}"""
            print(mensaje2)

        for i in self.lista_poder_pokemones:
            self.suma_poderes += i
            if i > 100:
                self.poder_mas_de_100 = self.poder_mas_de_100 = 1
            elif i < 100:
                self.poder_menos_de_100 = self.poder_menos_de_100 + 1

        promedio_poderes = self.suma_poderes / len(self.lista_poder_pokemones)
        mensaje = f"El promedio de poderes es de {promedio_poderes}"
        print(mensaje)

        for i in self.lista_tipo_pokemones:
            if i == "FUEGO":
                self.cantidad_poke_fuego += 1
            elif i == "ELECTRICO":
                self.cantidad_poke_electrico =+ 1
        mensaje2 = f"Hay {self.cantidad_poke_fuego} pokemones de Fuego y {self.cantidad_poke_electrico} eléctricos"
        print(mensaje2)

        mensaje3 = f"Hay {self.poder_mas_de_100} pokemos con un poder mayor a 100 y {self.poder_menos_de_100} con menos de 100"
        print(mensaje3)

        promedio_poder_pokemones_electricos = self.suma_poder_electrico / self.cantidad_poder_electrico
        mensaje4 = f"El promedio de poder de los pokemones electrivos es {promedio_poder_pokemones_electricos}"
        print(mensaje4)

if __name__ == "__main__":
    app = App()
    app.mainloop()