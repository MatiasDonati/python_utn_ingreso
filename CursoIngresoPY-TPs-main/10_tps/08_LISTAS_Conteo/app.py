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

    def btn_comenzar_ingreso_on_click(self):
        pass

    def btn_mostrar_estadisticas_on_click(self):
        pass

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
