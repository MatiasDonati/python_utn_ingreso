import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Matias
Apellido: Donati

Enunciado:

A) Al presionar el botón ‘Agregar' se debera cargar el nombre* y el precio** en sus respectivas listas.

* SOLO LETRAS MAYUSCULAS (A-Z)
** Enteros positivos

Si existe error al validar indicarlo mediante un Alert, cambiar el fondo del campo de texto con error
Si se cargo correctamente indicarlo con un Alert

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI AMBOS SON CORRECTOS --

B) Al precionar el boton mostrar se deberan listar los articulos, sus precios y su posicion en la lista (por terminal)

C) Informar
    1- Articulo mas caro
    2- Articulo mas barato
    3- Precio promedio
    4- Articulos que son mas caros que el promedio
    5- Articulos que son mas baratos que el promedio

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.txt_nombre_articulo = customtkinter.CTkEntry(master=self, placeholder_text="Nombre Articulo")
        self.txt_nombre_articulo.grid(row=0, padx=20, pady=20)

        self.txt_precio_articulo = customtkinter.CTkEntry(master=self, placeholder_text="Precio")
        self.txt_precio_articulo.grid(row=1, padx=20, pady=20)

        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.lista_nombre_articulo = []
        self.lista_precio_articulo = []
        self.artiulo_mas_caro = 0
        self.artiulo_mas_barato = 0
        self.flag_precio = True
        self.indice_mas_barato = 0
        self.indice_mas_caro = 0

    def btn_agregar_on_click(self):

            articulo = self.txt_nombre_articulo.get()
            precio = self.txt_precio_articulo.get()

            if articulo == None or articulo.isalpha() == False or articulo.isupper() == False and precio == None or precio.isdigit() == False:
                self.txt_nombre_articulo.delete(0, 9999999)
                self.txt_precio_articulo.delete(0, 9999999)
                self.txt_nombre_articulo.insert(0, "Error")
                self.txt_precio_articulo.insert(0, "Error")
                alert(message="😲 😲 😲\nIngrese Articulo en MAYUSCULAS\nY Precio en NUMEROS ENTEROS!")
            else:
                self.lista_nombre_articulo.append(articulo)
                self.lista_precio_articulo.append(precio)
                alert(message="😀*😀*😀*😀\n Se Cargo Correctamente!")
                self.txt_nombre_articulo.delete(0, 9999999)
                self.txt_precio_articulo.delete(0, 9999999)

    def btn_mostrar_on_click(self):
        for indice, prodcuto in enumerate(self.lista_nombre_articulo):
            mensaje = f"{indice + 1} - {prodcuto}"
            print(mensaje)
        for indice, precio in enumerate(self.lista_precio_articulo):
            mensaje = f"{indice + 1} - {precio}"
            print(mensaje)

            if self.flag_precio:
                self.artiulo_mas_barato = precio
                self.indice_mas_barato = indice
                self.artiulo_mas_caro = precio
                self.indice_mas_caro = indice
                self.flag_precio = False

            if precio < self.artiulo_mas_barato:
                self.indice_mas_barato = indice
            if precio > self.artiulo_mas_caro:
                self.indice_mas_caro = indice


    def btn_informar_on_click(self):
        mensaje = f"""El producto mas barato es: {self.lista_nombre_articulo[self.indice_mas_barato]}
con un precio de ${self.lista_precio_articulo[self.indice_mas_barato]}\n\n
El producto mas caro es: {self.lista_nombre_articulo[self.indice_mas_caro]}
con un precio de ${self.lista_precio_articulo[self.indice_mas_caro]}"""

        print(mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x400")
    app.mainloop()