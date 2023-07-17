import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_ingresado = int(prompt("", "Ingresa un numero"))
        numeros_pares_hasta_numero_elegido = []
        contador = 0

        for _ in range(numero_ingresado):
            contador += 1
            if contador % 2 == 0:
                numeros_pares_hasta_numero_elegido.append(contador)

        cantidad_de_numeros_pares = len(numeros_pares_hasta_numero_elegido)

        mensaje = f"Los numeros pares desde el 1 hasta el {numero_ingresado} son {cantidad_de_numeros_pares}, siendo {numeros_pares_hasta_numero_elegido} numeros."

        alert(message=mensaje)


if __name__ == "__main__":
    app = App()
    app.mainloop()