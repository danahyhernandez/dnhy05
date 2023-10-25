from guizero import App, Text, TextBox, PushButton
from re import I
import random

def calcular_edad():
 n: int= 0
 a_actual: int= 2023
 suma_edades: int= 0
 for _ in range(1, n+1):
     a_nacimiento= random.randint(2000, a_actual)
     a_nacimiento = int(input_a_nacimiento.value)
     n= int(input_n.value)
     edad: int = a_actual - a_nacimiento
     suma_edades = suma_edades + edad
     (f"año de nacimiento: {a_nacimiento} | edad {I}: {edad}")
     promedio_edades: float = suma_edades/n
     resultado.value = (f"el promedio de edades es: {promedio_edades}")


app = App(title="calculadora promedio App")

resultado= Text(app, text="")

message = Text(app, text="Dame el numero de personas:")
input_n = TextBox(app, width=20)
message = Text(app, text="Dame el año de nacimiento:")
input_a_nacimiento = TextBox(app, width=20)
calcular_button = PushButton(app, text="obtener promedio", command=calcular_edad)
app.display()