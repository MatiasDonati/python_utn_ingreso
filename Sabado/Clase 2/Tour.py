import math
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk

# Nombre y Apellido: Matias Donati

# Se deben pedir los siguientes datos de un tour  de vacaciones a un destino en particular:

# 1 -nombre , edad y género de una persona, mostrar el mensaje , "usted es  xxxx tiene xx de edad y su género es xxx"

# 2 -pedir la altura de la persona e informar si es bajo: menor a 140 cm,
# medio entre 140 y 170 cm , alto hasta 190 cm y muy alto para mayores a esa altura.

# 3- Validar todos los datos.

# 4- En las vacaciones se pueden seleccionar distintas excursiones para realizar. Se pueden hacer desde 0 excursiones a 11 excursiones.

# 5- Una vez ingresada la cantidad se debe pedir por cada excursión
# el importe y el tipo de excursión (caminata  o vehículo).
# informar cual es el precio más caro, el más barato y el promedio

# 6- Informar cual es el tipo de excursión (caminata  o vehículo) más seleccionada o si se seleccionó las mismas veces (caminata  o vehículo)

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Tour", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):

        nombre = prompt("", "Nombre")
        while nombre == None or nombre == "" or nombre.isalpha() == False or len(nombre) < 4:
            nombre = prompt("", "Nombre Ingresa Algo y en Letras!! y mayor a 4 caracteres")

        edad = prompt("", "Edad")
        while edad == None or edad == "" or edad.isdigit() == False:
            edad = prompt("", "Ingrese Edad y en Numeros!")
        edad_int = int(edad)

        genero = prompt("", "Género: 'Masculino' - 'Femenino' - 'Otro'").upper()
        while genero != "MASCULINO" and genero != "FEMENINO" and genero != "OTRO":
            genero = prompt("", "Elija alguno de los sugeridos: 'Masculino' - 'Femenino' - 'Otro'").upper()

        altura = prompt("", "Altura en cm... Ej.: 160")
        while altura == None or altura == "" or altura.isdigit() == False:
            altura = prompt("", "NUMEROS!!!..Altura en cm... Ej.: 160")
        altura = int(altura)

        if altura < 140:
            mensaje_altura = "bajo"
        elif altura <= 170:
            mensaje_altura = "medio en altura"
        elif altura < 190:
            mensaje_altura = "alto"
        else:
            mensaje_altura = "muy alto, alístese en la NBA!"

        excursiones = prompt("", "Cantidad de excursiones:")
        while excursiones == None or excursiones == "" or excursiones.isdigit() == False or int(excursiones) <= 0 or int(excursiones) >= 11:
            excursiones = prompt("", "NUMEROS! ... Cantidad de excursiones: de 0 a 11!!")
        excursiones = int(excursiones)

        precio_caro = None
        tipo_mas_caro = ''
        precio_barato = None
        tipo_mas_barato = ''
        promedio_precios = 0
        suma_precios = 0
        contador_excursion_caminata = 0
        contador_excursion_vehiculo = 0
        solo_una_excursion = ""

        contador_excursiones = 0

        while contador_excursiones < excursiones:
            importe = prompt("", "Importe")
            while importe == None or importe == "" or importe.isdigit() == False:
                importe = prompt("", "Ingrese Importe y en Numeros!")
            importe_int = int(importe)

            tipo = prompt("", "tipo de excursion").upper()
            while tipo != 'CAMINATA' and tipo != 'VEHICULO' and tipo != 'VEHÍCULO':
                tipo = prompt("", "tipo de excursion").upper()
            if tipo == 'CAMINATA':
                contador_excursion_caminata +=1
            else:
                contador_excursion_vehiculo +=1

            if precio_barato == None or importe_int < precio_barato:
                precio_barato = importe_int
                tipo_mas_barato = tipo

            if precio_caro == None or importe_int  > precio_caro:
                precio_caro = importe_int
                tipo_mas_caro = tipo

            suma_precios = suma_precios + importe_int
            contador_excursiones += 1

        mensaje_excursion = f"Se elgieron {contador_excursion_caminata} excursiones de tipo Caminata y {contador_excursion_vehiculo} de tipo Vehículo"

        if contador_excursion_vehiculo == excursiones or contador_excursion_caminata == excursiones:
            if contador_excursion_caminata > contador_excursion_vehiculo:
                mensaje_excursion = "Solo se eligieron excursiones de tipo 'Caminata'"
            else:
                mensaje_excursion = "Solo se eligieron excursiones de tipo 'Vehículo'"

        promedio_precios = suma_precios / excursiones

        mensaje = f"Usted es {nombre}, tiene {edad} de edad y su género es {genero} \n Usted es {mensaje_altura}\n\n"
        mensaje_2 = f"La excursion mas barata vale ${precio_barato} y es de tipo {tipo_mas_barato} \n La excursion mas cara vale $ {precio_caro} y es de tipo{tipo_mas_caro} \n\n El promedio de precios de las excursiones es de ${promedio_precios} \n\n"

        alert(message=mensaje+mensaje_2+mensaje_excursion)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

