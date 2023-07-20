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

e. se pide ingresar el sexo (M , F , NB) , informar cuantos candidatos hay de cada sexo

f. se pide ingresar nivel de aceptacion de imagen del candidato (entre -100 y 100) informar el
nombre y sexo del que mejor nivel tiene

g.de las personas de sexo femenino ,informar cuanta hay mayores a 50 y cuantas menores a esa edad

h. de que sexo hubo mas candidatos

Todos los datos se ingresan por prompt y los resultados por consola (print)

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
        genero_masculino = 0
        genero_femenino = 0
        genero_no_binario = 0
        candidato_mejor_nivel = ""
        sexo_candidato_mejor_nivel = ""
        femenino_mayor_a_50 = 0
        femenino_menor_a_50 = 0
        masculinos = 0
        femeninos = 0
        no_binario = 0
        genero_predominante = ""

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
            genero = prompt("", "Genero del candidato").upper()
            while genero == None or genero == "" or genero.isdigit() == True or genero != "M" and genero != "F" and genero != "NB":
                genero = prompt("", "Genero del candidato... M, F o NB").upper()
            nivel_de_aceptacion = prompt("", "Nivel de aceptacion")
            while nivel_de_aceptacion == None or nivel_de_aceptacion == "" or nivel_de_aceptacion.isdigit() == False or int(nivel_de_aceptacion) < -100 or int(nivel_de_aceptacion) > 100:
                nivel_de_aceptacion = prompt("", "Nivel de aceptacion... entre -100 y 100")
            nivel_de_aceptacion = int(nivel_de_aceptacion)

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

            if genero == "M":
                genero_masculino += 1
            elif genero == "F":
                genero_femenino += 1
            else:
                genero_no_binario += 1

            if nivel_de_aceptacion > -100:
                candidato_mejor_nivel = candidato
                sexo_candidato_mejor_nivel = genero

            if genero == "F":
                femeninos += 1
                if edad_candidato > 50:
                    femenino_mayor_a_50 += 1
                else:
                    femenino_menor_a_50 += 1
            elif genero == "M":
                masculinos += 1
            else:
                no_binario += 1

            suma_edades += edad_candidato
            total_votos = total_votos + votos_candidato

        if masculinos > femeninos and masculinos > no_binario:
            genero_predominante = "Masculino"
        # elif femeninos > masculinos and femeninos > no_binario:
        elif femeninos > no_binario:
            genero_predominante = "Femenino"
        else:
            genero_predominante = "No Binario"

        promedio = suma_edades / contador

        mensaje = f"""{ganador} es el Ganador.\n\n{perdedor} con edad de {edad_perdedor}
        años es el Perdedor.\n\nEl promedio en edad de los candidatos es de {promedio}.\n\n
        El total de votos emitidos fue de {total_votos} votos\n\n Hay {genero_masculino} candidatos de genero Masculino, 
        hay {genero_femenino} candidatos de genero femenino y hay {genero_no_binario} de genero no Binario.\n\n
        El candidato con mejor imagen es {candidato_mejor_nivel} y es de genero {sexo_candidato_mejor_nivel}\n\n
        De los candidatos de genero Femenino hay {femenino_mayor_a_50} mayores a 50 años y {femenino_menor_a_50} menores a 50 años.\n\n
        El genero predominante de todos los candidatos es {genero_predominante}"""

        alert(message=mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()