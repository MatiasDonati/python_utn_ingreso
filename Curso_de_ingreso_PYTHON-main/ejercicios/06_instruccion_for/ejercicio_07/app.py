import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_elegido = int(prompt("", "Ingresa un numero"))
        lista_de_numeros = []
        contador = 0

        for _ in range(numero_elegido):
            contador += 1
            match(numero_elegido % contador):
                case 0:
                    lista_de_numeros.append(contador)

        cantidad_de_divisores = len(lista_de_numeros)
        mensaje = f"Los numeros divisores de {numero_elegido} son {cantidad_de_divisores} y son: {lista_de_numeros}"

        alert(message=mensaje)




if __name__ == "__main__":
    app = App()
    app.mainloop()