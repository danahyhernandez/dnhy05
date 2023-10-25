from guizero import App, Text, TextBox, PushButton
import random

def calcular_aprobados():
    n:int = 25
    a_aprobados: int = 0
    for _ in range(1, n+1): 
     a_aprobados = int(input_a_aprobados.value)
     cal = random.randint(5, 10)
     if cal >= 7:
        a_aprobados += 1
    (f"alumnos reprobados: {n - a_aprobados}")
    a_aprobados = a_aprobados
    resultado.value = (f"los alumnos aprobados son:{a_aprobados}")
  

app = App(title="calculadora App")

resultado= Text(app, text="")

message = Text(app, text="calificación:")
input_a_aprobados = TextBox(app, width=20)
calcular_button = PushButton(app, text="obtener alumnos aprobados", command=calcular_aprobados)
app.display()