import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
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

        if len(lista_de_numeros) == 2:
            mensaje = f"El {numero_elegido} es un numero PRIMO"
        else:
            mensaje = f"El {numero_elegido} NO es un numero PRIMO"

        alert(message=mensaje)

if __name__ == "__main__":
    app = App()
    app.mainloop()