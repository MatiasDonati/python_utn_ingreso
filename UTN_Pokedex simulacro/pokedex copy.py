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
        for indice in range(5):
            nombre = prompt("", f"Ingrese el PokeNombre {indice + 1}")
            tipo = prompt("", "tipo de pokemon").upper()
            while tipo != "AGUA" and tipo != "TIERRA" and tipo != "PSIQUICO" and tipo != "FUEGO" and tipo != "ELECTRICO":
                tipo = prompt("", "tipo de pokemon . Agua, Tierra, Psiquico, Fuego o Agua ").upper()
            poder = prompt("", "Cantidad de podder")
            while int(poder) < 50 or int(poder) > 200:
                poder = prompt("", "Cantidad de podder.. numero entre 50 y 200")
            poder = int(poder)

            self.lista_nombre_pokemones.append(nombre)
            self.lista_poder_pokemones.append(poder)
            self.lista_tipo_pokemones.append(tipo)

    def btn_mostrar_pokedex_on_click(self):

        contador_fuego = 0
        contador_electrico = 0
        contador_agua = 0
        contador_tierra = 0
        contador_psiquico = 0

        acumulador_de_poder = 0
        acumulador_poder_electrico = 0
        suma_poder_electrico = 0

        maximo_poder = None
        minimo_poder = None

        contador_mayores_a_100 = 0
        contador_menores_a_100 = 0

        for indice in range (len(self.lista_nombre_pokemones)):
            print(f"""el pokemon {self.lista_nombre_pokemones[indice]}
                  es de tipo {self.lista_tipo_pokemones[indice]}
                  y su poder {self.lista_poder_pokemones[indice]}""")

            if maximo_poder == None or self.lista_poder_pokemones[indice] > maximo_poder:
                maximo_poder = self.lista_poder_pokemones[indice]
                nombre_maximo = self.lista_nombre_pokemones[indice]
                tipo_maximo = self.lista_tipo_pokemones[indice]
            if minimo_poder == None or self.lista_poder_pokemones[indice] < minimo_poder:
                minimo_poder = self.lista_poder_pokemones[indice]
                nombre_minimo = self.lista_nombre_pokemones[indice]
                tipo_minimo = self.lista_tipo_pokemones[indice]

            if self.lista_poder_pokemones[indice] > 100:
                contador_mayores_a_100 += 1
            elif self.lista_poder_pokemones[indice] < 100:
                contador_menores_a_100 += 1

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

            #PROMEDIO DE PODER DE LOS POKEMONES ELECTRICOS
            if self.lista_tipo_pokemones[indice] == "ELECTRICO":
                acumulador_poder_electrico = acumulador_poder_electrico + 1
                suma_poder_electrico = suma_poder_electrico + self.lista_poder_pokemones[indice]

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

        #para promedio de poder
        for elemento in self.lista_poder_pokemones:
            acumulador_de_poder += elemento

        promedio_poderes = acumulador_de_poder / len(self.lista_poder_pokemones)

        #promedio de poder de todos los electricos
        promedio_poderes_electricos = suma_poder_electrico / acumulador_poder_electrico


        mensaje_final = f"""Cantidad Tipo Fuego es {contador_fuego} y Tipo Electrico es {contador_electrico}\n
Pokemon con poder mas alto es {nombre_maximo} de tipo {tipo_maximo} y poder de {maximo_poder}\n 
Pokemon con menor poder es {nombre_minimo} de tipo {tipo_minimo} y poder de {minimo_poder}\n\n
Pokemones con poder mayor a 100 hay {contador_mayores_a_100} y menores a 100 hay {contador_menores_a_100}\n
El tipo predominante es {mayor_tipo} y el inferior es {menor_tipo}\n
El promedio de poderes ingresados es {promedio_poderes}\n
Y el promedio de poderes de Electricos es {promedio_poderes_electricos}"""

        alert(message=mensaje_final)

if __name__ == "__main__":
    app = App()
    app.mainloop()
