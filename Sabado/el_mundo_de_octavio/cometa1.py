import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk
import math

'''
La juguetería El MUNDO DE OCTAVIO nos encarga un programa para conocer qué cantidad de materiales se necesita para la fabricación de distintos juguetes.

COMETA: 

AB = Diámetro mayor (se debe calcular)
DC = diámetro menor (se ingresa por prompt)
BD y BC = lados menores (se ingresa por prompt)
AD y AC = lados mayores (se ingresa por prompt)

Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.
El cometa estará construido con papel de alta resistencia.
La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.
Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="El Cometa 🪁", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.label_diametro_menor = customtkinter.CTkLabel(master=self, text="Diametro Menor DC")
        self.label_diametro_menor.grid(row=1, column=0, padx=20, pady=10)

        self.txt_diametro_menor= customtkinter.CTkEntry(master=self)
        self.txt_diametro_menor.grid(row=1, column=1)

        self.label_lados_menores = customtkinter.CTkLabel(master=self, text="Lados Menores BD y BC")
        self.label_lados_menores.grid(row=2, column=0, padx=20, pady=10)

        self.txt_lados_menores = customtkinter.CTkEntry(master=self)
        self.txt_lados_menores.grid(row=2, column=1)

        self.label_lados_mayores = customtkinter.CTkLabel(master=self, text="Lados Mayores AD y AC")
        self.label_lados_mayores.grid(row=3, column=0, padx=20, pady=10)

        self.txt_lados_mayores = customtkinter.CTkEntry(master=self)
        self.txt_lados_mayores.grid(row=3, column=1)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        diametro_dc = prompt(title='Diametro menor', prompt='Ingrese el diametro menor DC')
        lado_menor_bd_bc = prompt(title='Medida lado menor', prompt='Ingrese la medida del lado menor BD y BC')
        lado_mayor_ad_ac = prompt(title='Medida lado mayor', prompt='Ingrese la medida del lado mayor AD y AC')

        # parsear datos
        diametro_dc_int = int(diametro_dc)
        lado_menor_bd_bc_int = int(lado_menor_bd_bc)
        lado_mayor_ad_ac_int = int(lado_mayor_ad_ac)

        # calculos
        perimetro_cometa = (lado_mayor_ad_ac_int + lado_menor_bd_bc_int) * 2
        # En cm2 que va a reperesentar la cantidad de papel necesaria para el cuerpo del cometa.
        area_cometa = lado_mayor_ad_ac_int * lado_menor_bd_bc_int
        cola_cometa = area_cometa * 0.1

        # Encontramos la cantidad de papapel necesaria para el cometa
        cantidad_total_papel_cometa = area_cometa + cola_cometa

        # Podemos usar pitágoras.
        base_triangulo = lado_mayor_ad_ac_int
        altura_triangulo = lado_menor_bd_bc_int

        hipotenusa_triangulo_al_cuadrado = lado_mayor_ad_ac_int **2 + lado_menor_bd_bc_int **2
        # math.sqrt() devuelve la raiz cuadrada
        hipotenusa_triangulo = math.sqrt(hipotenusa_triangulo_al_cuadrado)

        centimetros_varillas = hipotenusa_triangulo + perimetro_cometa + diametro_dc_int

        mensaje = "Cantidad para un cometa: Varillas {0} cms Papel {1} cms2".format(centimetros_varillas, cantidad_total_papel_cometa)

        mts_varillas = (centimetros_varillas * 10) / 100
        papel_para_10 = cantidad_total_papel_cometa * 10
        mensaje_2 = "{0}\ny para 10 cometas: Varillas {1} mts y Papel: {2} cms2".format(mensaje, mts_varillas, cantidad_total_papel_cometa)

        self.txt_diametro_menor.delete(0, 'end')
        self.txt_diametro_menor.insert(0, diametro_dc)

        self.txt_lados_menores.delete(0, 'end')
        self.txt_lados_menores.insert(0, lado_menor_bd_bc)

        self.txt_lados_mayores.delete(0, 'end')
        self.txt_lados_mayores.insert(0, lado_mayor_ad_ac)

        alert(title='Resultado', message=mensaje_2)


if __name__ == "__main__": 
    app = App()
    app.mainloop()