import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Matias
Apellido: Donati

=== TP 6 (WHILE) Elecciones Paso ===
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar:
    A. Nombre del candidato con más votos.
    B. Nombre y edad del candidato con menos votos.
    C. El promedio de edades de los candidatos.
    D. Total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=1, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):

        contador = 0
        inicio_votos_ganador = 0
        inicio_votos_perdedor = 0
        ganador = ""
        perdedor = ""
        edad_perdedor = 0
        suma_edades = 0
        promedio = 0
        total_votos = 0
        flag = True
        seguir_cargando_candidatos = True

        while seguir_cargando_candidatos:
            contador += 1
            candidato = prompt("", "Nombre del Candidato")
            while candidato == None or candidato == "" or candidato.isdigit() == True or len(candidato) < 4:
                candidato = prompt("", "Nombre del Candidato")
            edad_candidato = prompt("", "Edad del Candidato")
            while edad_candidato == None or edad_candidato.isdigit() == False or int(edad_candidato) < 25:
                edad_candidato = prompt("", "Edad del Candidato")
            edad_candidato = int(edad_candidato)
            votos_candidato = prompt("", "Votos Candidato")
            while votos_candidato == None or votos_candidato.isdigit() == False or int(votos_candidato) < 0:
                votos_candidato = prompt("", "Votos Candidato")
            votos_candidato = int(votos_candidato)

            seguir_cargando_candidatos = question("", "Desea seguir ingresando Candidatos??")

            if flag:
                inicio_votos_ganador = votos_candidato
                inicio_votos_perdedor = votos_candidato
                ganador = candidato
                perdedor = candidato
                edad_perdedor = edad_candidato
                flag = False

            if votos_candidato > inicio_votos_ganador:
                inicio_votos_ganador = votos_candidato
                ganador = candidato

            if votos_candidato < inicio_votos_perdedor:
                inicio_votos_perdedor = votos_candidato
                perdedor = candidato
                edad_perdedor = edad_candidato

            suma_edades += edad_candidato
            promedio = suma_edades / (contador + 1)
            total_votos = total_votos + votos_candidato

        mensaje = f"{ganador} es el Ganador.\n\n{perdedor} con edad de {edad_perdedor} años es el Perdedor.\n\nEl promedio en edad de los candidatos es de {promedio}.\n\nEl total de votos emitidos fue de {total_votos} votos"

        alert(message=mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()