import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
==========
Matias Donati
==========

Al presionar el botón Mostrar pedir valores por prompt hasta que el usuario ingrese el valor 9 (se deberá utilizar 'BREAK').

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        for _ in range(99999999999):
            valor_ingresado = int(prompt("", "Ingrese un Valor"))
            if valor_ingresado == 9:
                alert(message=f"ACERTASTE {valor_ingresado}!!")
                break

if __name__ == "__main__":
    app = App()
    app.mainloop()