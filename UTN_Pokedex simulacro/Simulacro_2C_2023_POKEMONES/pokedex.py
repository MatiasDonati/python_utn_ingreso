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
MATIAS DONATI
DNI 33.102.952
======

#El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con algunos pokemones de prueba.

A) Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Psiquico, Fuego)
    * Poder de ataque (validar que sea mayor a 50 y menor a 200)
B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal)

Del punto C solo debera realizar 3 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:

    Informe 1- Tome el ultimo numero de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)
    3

    Informe 2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). En caso de que su DNI
    finalice con el numero 0, debera realizar el informe 9.
    6

    Informe 3- Tome la suma de los ultimos dos numeros de su DNI personal, en caso de ser un numero par, tomara el numero par
    mas chico que su ultimo digito del DNI (en caso de que su ultimo digito sea 2, resolvera el ejercicio 8). En caso contrario
    , si es impar,
    tomara el numero impar posterior (en caso de que su ultimo digito sea 9, resolvera el ejercicio 1)
    En caso de que el numero sea el mismo obtenido en el informe 2, realizara el siguiente informe en la lista.

    Realizar los informes correspondientes a los numeros obtenidos. EL RESTO DE LOS INFORMES LOS DEBE IGNORAR.
C)
    #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
    #! 1) - Cantidad de pokemones de tipo Psiquico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.
    #! 2) - Nombre y Poder del pokemon de tipo Agua con el poder mas alto.
    #! 3) - Nombre y Poder del pokemon de tipo Psiquico con el poder mas bajo.
    #! 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).
    #! 5) - Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados).
    #! 6) - tipo de los pokemones del tipo que mas pokemones posea.
    #! 7) - tipo de los pokemones del tipo que menos pokemones posea.
    #! 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.
    #! 9) - el promedio de poder de todos los pokemones de tipo Psiquico.

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
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=6, pady=10, columnspan=2, sticky="nsew")
        # Cargar aca los pokemones
        self.lista_nombre_pokemones =["Squirtle", "Psyduck", "Cloyster", "Charmander", "Drowzee", "Gyarados", "Squirtle", "Mewtwo", "Charizard", "Magikarp"]
        self.lista_poder_pokemones = [90, 150, 150, 95, 70, 90, 150, 80, 50, 103]
        self.lista_tipo_pokemones = ["agua", "psíquico", "agua", "fuego", "psíquico", "agua", "agua", "psíquico", "fuego", "agua"]

    def btn_mostrar_todos_on_click(self):
        for indice in range(len(self.lista_nombre_pokemones)):
            print(f""" En el indice {indice} esta {self.lista_nombre_pokemones[indice]} con un poder de {self.lista_poder_pokemones[indice]} y es de tipo {self.lista_tipo_pokemones[indice]}""")

    def btn_mostrar_informe_1(self):
        #! 2) - Nombre y Poder del pokemon de tipo Agua con el poder mas alto.
        maximo_tipo_agua = None

        for indice in range(len(self.lista_nombre_pokemones)):
            if self.lista_tipo_pokemones[indice] == "agua":
                if maximo_tipo_agua == None or self.lista_poder_pokemones[indice] > maximo_tipo_agua:
                    nombre_maximo_poder_tipo_agua = self.lista_nombre_pokemones[indice]
                    poder_maximo_poder_tipo_agua = self.lista_poder_pokemones[indice]

        informe_1 = f"{nombre_maximo_poder_tipo_agua} es el pokemon de Tipo Agua con el maximo poder, siendo este: {poder_maximo_poder_tipo_agua}"
        print(informe_1)

    def btn_mostrar_informe_2(self):
        #! 7) - tipo de los pokemones del tipo que menos pokemones posea.
        cantidad_agua = 0
        cantidad_psíquico = 0
        cantidad_fuego = 0

        for indice in range(len(self.lista_tipo_pokemones)):
            match self.lista_tipo_pokemones[indice]:
                case "agua":
                    cantidad_agua += 1
                case "psíquico":
                    cantidad_psíquico += 1
                case _:
                    cantidad_fuego += 1

        if cantidad_agua < cantidad_psíquico and cantidad_agua < cantidad_fuego:
            menor_cantidad = "Agua"
        elif cantidad_psíquico < cantidad_fuego:
            menor_cantidad = "Psíquico"
        else:
            menor_cantidad = "Fuego"

        informe_2 = f"Los pokemones de tipo {menor_cantidad} son el tipo que menos cantidad hay."
        print(informe_2)

    def btn_mostrar_informe_3(self):
        #! 3) - Nombre y Poder del pokemon de tipo Psiquico con el poder mas bajo.
        minimo_poder_psiquico = None

        for indice in range(len(self.lista_tipo_pokemones)):
            if self.lista_tipo_pokemones[indice] == "psíquico":
                if minimo_poder_psiquico == None or self.lista_poder_pokemones[indice] < minimo_poder_psiquico:
                    nombre_minimo_poder_tipo_psiquico = self.lista_nombre_pokemones[indice]
                    poder_minomo_poder_tipo_psiquico = self.lista_poder_pokemones[indice]

        informe_3 = f"{nombre_minimo_poder_tipo_psiquico} es el pokemon de Tipo Psíquico con el minimo poder, siendo este: {poder_minomo_poder_tipo_psiquico}"
        print(informe_3)



        # EXTRA ejercicio 0

        cantidad_fuego_mas_10porciento_supera_100 = 0

        for indice in range(len(self.lista_tipo_pokemones)):
            if self.lista_tipo_pokemones[indice] == "fuego" and self.lista_poder_pokemones[indice] +  self.lista_poder_pokemones[indice] * 0.1 > 100:
                cantidad_fuego_mas_10porciento_supera_100 += 1

        print(cantidad_fuego_mas_10porciento_supera_100)

    def btn_cargar_pokedex_on_click(self):
    # * El nombre del pokemon
    # * El tipo de su elemento (Agua, Psiquico, Fuego)
    # * Poder de ataque (validar que sea mayor a 50 y menor a 200)

            for indice in range(5):
                nombre = prompt("", f"Ingrese el PokeNombre {indice + 1}")
                tipo = prompt("", "tipo de pokemon")
                while tipo != "agua" and tipo != "psíquico" and tipo != "fuego":
                    tipo = prompt("", "tipo de pokemon . agua, psíquico, o fuego")
                poder = prompt("", "Cantidad de podder")
                while int(poder) < 50 or int(poder) > 200:
                    poder = prompt("", "Cantidad de podder.. numero entre 50 y 200")
                poder = int(poder)

                self.lista_nombre_pokemones.append(nombre)
                self.lista_poder_pokemones.append(poder)
                self.lista_tipo_pokemones.append(tipo)

if __name__ == "__main__":
    app = App()
    app.mainloop()