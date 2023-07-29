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

    # Cargar de Datos // Planetas 

        self.nombres = [ "Juan", "María", "Luis", "Ana", "Carlos", "Jose", "Pedro", "Sofía", "Miguel", "Valentina",
        "Andrés", "Lucía", "Fernando", "Gabriela", "Diego", "Martina", "Jorge", "Camila", "Ricardo", "Isabella",
        "José", "Paula", "Manuel", "Alejandra", "Santiago", "Daniela", "Gustavo", "Carolina", "Emilio", "Antonella",
        "Pablo", "Valeria", "Eduardo", "Florencia", "Alberto", "Agustina", "Raul", "Rocio", "Javier", "Marina",
        "Sebastian", "Catalina", "Rafael", "Carmen", "Rodrigo", "Elena", "Oscar", "Pilar", "Hugo", "Juana",
        "Guillermo", "Natalia", "Francisco", "Constanza", "Hector", "Adriana", "Victor", "Anita", "Lorenzo", "Estela",
        "Enrique", "Diana", "Fabian", "Patricia", "Felipe", "Claudia", "Camilo", "Teresa", "Samuel", "Rosa",
        "Joaquin", "Monica", "Lucas", "Ines", "Omar", "Gloria", "Mariano", "Silvia", "Nicolas", "Alicia",
        "Federico", "Olga", "Arturo", "Amparo", "Julio", "Elsa", "Alfredo", "Beatriz", "Elias", "Rita",
        "Benjamin", "Margarita", "Agustin", "Dolores", "Dario", "Lourdes", "Gerardo", "Manuela", "Feliciano", "Marta"]

    # Lista de edades (mayores o iguales a 16)
        self.edades = [
        25, 33, 20, 29, 50, 40, 22, 28, 35, 18,
        26, 21, 30, 32, 19, 27, 24, 38, 31, 23,
        29, 17, 28, 34, 20, 25, 22, 33, 40, 16,
        19, 37, 24, 28, 31, 21, 33, 18, 29, 26,
        35, 20, 23, 39, 30, 27, 22, 36, 28, 32,
        31, 19, 24, 20, 25, 33, 40, 27, 21, 39,
        29, 22, 36, 30, 19, 25, 21, 38, 34, 17,
        32, 18, 23, 27, 22, 40, 36, 29, 20, 33,
        31, 35, 24, 19, 28, 30, 26, 37, 33, 21,
        25, 29, 16, 38, 40, 50, 27, 30, 32, 24
    ]

    # Lista de géneros (Masculino, Femenino u Otro)
        self.generos = [
        "Masculino", "Femenino", "Masculino", "Femenino", "Otro", "Masculino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino"
    ]

    # Lista de tipo de entrada (General, Campo delantero, Platea)
        self.tipo_entrada = [
        "General", "Campo delantero", "Platea", "General", "Platea", "General", "General", "Platea", "Campo delantero", "General",
        "Campo delantero", "Platea", "General", "General", "Campo delantero", "Platea", "Platea", "Campo delantero", "General", "Platea",
        "Campo delantero", "Platea", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
        "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea",
        "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
        "General", "Platea", "General", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea",
        "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
        "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea",
        "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
        "Campo delantero", "Platea", "Platea", "Campo delantero", "General", "Platea", "Campo delantero"
    ]

    # Lista de medio de pago (Credito, Debito, Efectivo)
        self.medio_pago = [
        "Credito", "Debito", "Efectivo", "Credito", "Efectivo", "Debito", "Credito", "Debito", "Efectivo", "Credito",
        "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
        "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
        "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito",
        "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
        "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
        "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito",
        "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
        "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
        "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito"
    ]

        # Lista de precios correspondientes a cada tipo de entrada
        self.precios = [16000, 30000, 25000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
        25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
        30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
        16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
        25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
        30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
        16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
        25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
        30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
        16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000
    ]

    def btn_cargar_pokedex_on_click(self):
        for indice in range(5):
            nombre = prompt("",f"Nombre del Compradoe {indice + 1}")
            while nombre == None or nombre == "" or len(nombre) < 4:
                nombre = prompt("",f"Nombre del Planeta {indice + 1} 4 LETRAS MINIMO")
            self.nombres(nombre)

            edad = prompt("", "Edad")
            while int(edad) < 16:
                edad = prompt("", "Edad.. no menor a 16")
            edad = int(edad)
            self.edades.append(edad)

            genero = prompt("", "genero")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = prompt("", "genero ... Masculio, Femenino, Otro")
            self.generos.append(genero)

            tipo_entrada = prompt("", "tipo_entrada")
            while tipo_entrada != "General" and tipo_entrada != "Campo delantero" and tipo_entrada != "Platea":
                tipo_entrada = prompt("", "tipo_entrada ... NARANJA AMARILLO VIOLETA O GRIS")
            self.tipo_entrada.append(tipo_entrada)

            medio_de_pago = prompt("", "medio_de_pago")
            while medio_de_pago != "Credito" and medio_de_pago != "Efectivo" and medio_de_pago != "Debito":
                medio_de_pago = prompt("", "medio_de_pago ... Credito, Efectivo, Debito")
            self.medio_pago.append(medio_de_pago)

            match self.tipo_entrada[indice]:
                case "General":
                    precio_entrada = 16000
                case "Campo delantero":
                    precio_entrada = 25000
                case _:
                    precio_entrada = 30000

            if self.medio_pago[indice] == "Credito":
                precio_entrada = precio_entrada - precio_entrada * 0.2
            elif self.medio_pago[indice] == "Debito":
                precio_entrada = precio_entrada - precio_entrada * 0.15

            self.precios.append(precio_entrada)

    def btn_mostrar_pokedex_on_click(self):

        suma_precio_entradas = 0
        cantidad_general = 0
        cantidad_campo_delantero = 0
        cantidad_platea = 0

        suma_edades_platea = 0
        cantidad_edades_platea = 0

        cantidad_masculino_campo_delantero = 0
        cantidad_femenino_campo_delantero = 0
        cantidad_otro_campo_delantero = 0

        cantidad_general_credito = 0
        suma_edades_general_credito = 0

        cantidad_entradas_mayores_de_30 = 0
        suma_entradas_mayores_de_30 = 0

        cantidad_platea_debito = 0

        monto_entradas_general_debito_edades_multiplo_de_5 = 0

        nombres_mayor_de_edad_masculino_entrada_gral = []

        maxima_edad = None
        nombres_maxima_edad_masculino_entrada_gral = []

        cantidad_platea_edad_numero_primo = 0

        for indice in range(len(self.nombres)):

            suma_precio_entradas += self.precios[indice]

            match self.tipo_entrada[indice]:
                case "General":
                    cantidad_general += 1
                    if self.medio_pago[indice] == "Credito":
                        cantidad_general_credito += 1
                        suma_edades_general_credito += self.edades[indice]
                case "Campo delantero":
                    cantidad_campo_delantero += 1
                    if self.generos[indice] == "Masculino":
                        cantidad_masculino_campo_delantero += 1
                    elif self.generos[indice] == "Femenino":
                        cantidad_femenino_campo_delantero += 1
                    else:
                        cantidad_otro_campo_delantero += 1
                case _:
                    cantidad_platea += 1
                    if self.medio_pago[indice] == "Debito":
                        cantidad_platea_debito +=1
                        # Ver si es numero primo...
                        lista_numeros = []
                        for numero in range(self.edades[indice]):
                            if numero > 0:
                                if self.edades[indice] % numero == 0:
                                    lista_numeros.append(numero)
                                if len(lista_numeros) == 2:
                                    cantidad_platea_edad_numero_primo += 1
            if self.tipo_entrada[indice] == "Platea":
                suma_edades_platea += self.edades[indice]
                cantidad_edades_platea += 1

            if self.edades[indice] > 18 and self.generos[indice] == "Masculino" and self.tipo_entrada[indice] == "General":
                nombres_mayor_de_edad_masculino_entrada_gral.append(self.nombres[indice])

            if self.edades[indice] > 30:
                cantidad_entradas_mayores_de_30 += 1
                suma_entradas_mayores_de_30 += self.precios[indice]

            if self.tipo_entrada[indice] == "General" and self.medio_pago[indice] == "Debito" and self.edades[indice] % 5 == 0:
                monto_entradas_general_debito_edades_multiplo_de_5 =+ self.precios[indice]

            if maxima_edad == None or self.edades[indice] > maxima_edad:
               maxima_edad = self.edades[indice]
            if self.edades[indice] == maxima_edad and self.generos[indice] == "Masculino" and self.tipo_entrada[indice] == "General":
                nombres_maxima_edad_masculino_entrada_gral.append(self.nombres[indice])

        cantidad_entradas_vendidas = cantidad_general + cantidad_campo_delantero + cantidad_platea
        porcentaje_entradas_general = cantidad_general / cantidad_entradas_vendidas * 100
        porcentaje_entradas_general_redondeado = round(porcentaje_entradas_general, 2)


        porcentaje_platea_debito = cantidad_platea_debito / cantidad_entradas_vendidas * 100
        porcentaje_platea_debito_redondeado = round(porcentaje_platea_debito, 2)


        promedio_edades_platea = suma_edades_platea / cantidad_edades_platea
        promedio_edades_platea_redondeado = round(promedio_edades_platea, 2)

        if cantidad_general > cantidad_campo_delantero and cantidad_general > cantidad_platea:
            entradas_mas_vendida = "General"
        elif cantidad_campo_delantero >  cantidad_platea:
            entradas_mas_vendida = "Campo delantero"
        else:
            entradas_mas_vendida = "Platea"

        if cantidad_masculino_campo_delantero > cantidad_femenino_campo_delantero and cantidad_masculino_campo_delantero > cantidad_otro_campo_delantero:
            mayor_genero_campo_delantero = "Masculino"
        elif cantidad_femenino_campo_delantero > cantidad_otro_campo_delantero:
            mayor_genero_campo_delantero = "Femenino"
        else:
            mayor_genero_campo_delantero = "Otro"

        promedio_tipo_general_credito = suma_edades_general_credito / cantidad_general_credito
        promedio_tipo_general_credito_redondeado = round(promedio_tipo_general_credito, 2)

        promedio_entradas_mayores_30_anos = suma_entradas_mayores_de_30 / cantidad_entradas_mayores_de_30
        promedio_entradas_mayores_30_anos_redondeo = round(promedio_entradas_mayores_30_anos, 2)


        informe = f"""La recaudacion total es de {suma_precio_entradas}\nSe vendieron {cantidad_general} Genral, {cantidad_campo_delantero} campo delantero y {cantidad_platea} platea\n\n
        El promedio de edades de los compradores de platea es {promedio_edades_platea_redondeado}\n El porcentaje de entradas General es {porcentaje_entradas_general_redondeado}
        Quienes son mayores de edad, de genero masculino y compraron entradas General son {nombres_mayor_de_edad_masculino_entrada_gral}\n
        Las personas que mas edad tiene son {len(nombres_maxima_edad_masculino_entrada_gral)} y son los siguientes: {nombres_maxima_edad_masculino_entrada_gral}\n\n
        Las entradas mas vendidas son de tipo {entradas_mas_vendida}
        El genero mas frecuente q compraron 'Campo delantero' son {mayor_genero_campo_delantero}
        El promedio de edades de los que sacaron entrada General y compraron con tarjeta de Crecito es: {promedio_tipo_general_credito_redondeado}
        El promedio de entradas compradas por personas mayores a 30 años es de {promedio_entradas_mayores_30_anos_redondeo}
        El porcentaje que compraron platea con debito es de {porcentaje_platea_debito_redondeado}
        Las personas que compraron Platea y su edad es numero primo son {cantidad_platea_edad_numero_primo}\n
        La suma de entradas General compradas con Debito por persona con edad multiplo de 5 son {monto_entradas_general_debito_edades_multiplo_de_5}"""

        print(informe)

if __name__ == "__main__":
    app = App()
    app.mainloop()