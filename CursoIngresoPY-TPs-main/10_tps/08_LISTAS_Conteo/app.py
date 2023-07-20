import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre:
Apellido:

=== TP 8 (LIST) Conteo ===
Enunciado:
Al presionar el botón "Comenzar ingreso", solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt).
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. El minimo de los negativos
    G. El maximo de los positivos
    H. El promedio de los negativos

Informar los resultados mediante alert.
'''

class App(customtkinter.CTk):
   
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
   
        self.btn_cargar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.lista = []
        self.suma_negativos = 0
        self.suma_positivos = 0
        self.acumulador = 0
        self.cantidad_positivos = 0 
        self.cantidad_negativos = 0 
        self.cantidad_ceros = 0 
        self.negativo_menor = None
        self.positivo_mayor = None
        self.contador_negativos = 0

    def btn_comenzar_ingreso_on_click(self):

        # VALIDAR SI NO HAY INGRESO DE ALGUN TIPO DE NUMEROS POSITIVO, NEGATIVO O CERO !!
        # VALIDAR SI NO HAY INGRESO DE ALGUN TIPO DE NUMEROS POSITIVO, NEGATIVO O CERO !!
        # VALIDAR SI NO HAY INGRESO DE ALGUN TIPO DE NUMEROS POSITIVO, NEGATIVO O CERO !!

        while True:
            numero = prompt("", "Ingresar numero")
            #pongo isdigit despues de alpha para evitar que se rompa con signos como "-" etc.
            while numero == None or numero == "" or numero.isalpha() == True or numero.isdigit() == False:
                numero = prompt("", "Ingresar numero.. NUMERO!")
            numero = int(numero)
            self.lista.append(numero)

            seguir_cargando_numeros = question("", "Ingresa mas numeros?")
            if seguir_cargando_numeros is False:
                break
                     
        for i in self.lista:
            if i > 0:
                print("MAYOR a CERO")
                self.suma_positivos = self.suma_positivos + i
                self.cantidad_positivos = self.cantidad_positivos + 1

                if self.positivo_mayor == None:
                    self.positivo_mayor = i
                if i > self.positivo_mayor:
                    self.positivo_mayor = i
   
            elif i < 0:
                print("MENOR a CERO")
                self.suma_negativos = self.suma_negativos + i 
                self.cantidad_negativos = self.cantidad_negativos + 1

                if self.negativo_menor == None:
                    self.negativo_menor = i

                if i < self.negativo_menor:
                    self.negativo_menor = i
               
                self.contador_negativos = self.contador_negativos + 1
            else:
                print("Es CERO")
                self.cantidad_ceros = self.cantidad_ceros + 1

        self.promedio_negativos = self.suma_negativos / self.contador_negativos

        print(self.lista)

    def btn_mostrar_estadisticas_on_click(self):

        mensaje = f"""La suna de los negativos es {self.suma_negativos},
        \nLa suma de los positivos es {self.suma_positivos},
        \nLa cantidad de numeros positivos es {self.cantidad_positivos},
        \nLa cantidad de numero negativos es {self.cantidad_negativos},
        \nLa cantidad de ceros es {self.cantidad_ceros},
        \nEl minimo de los numeros negativos es {self.negativo_menor},
        \nEl maximo de los positovos es {self.positivo_mayor},
        \nEl promedio de los negativos es {self.promedio_negativos}."""

        alert(message=mensaje)
   
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()