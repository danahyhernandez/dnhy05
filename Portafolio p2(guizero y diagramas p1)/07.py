import random
from guizero import App, Text, TextBox, PushButton

def suma_c():
 n = random.randint(1, 20)
 suma_cuadrados = 0
 for _ in range(1, n):
  num_pos = int(input_num_pos.value)
  num_pos = random.randint(1, 100)
  cuadrado = num_pos**2
  cuadrado = (f"({num_pos}^2 = {cuadrado})")
  resultado_1.value= (f"La suma de los cuadrados es: {cuadrado}")
  cuadrado = cuadrado/2 # type: ignore
  resultado_2.value= (f"el promedio es: {cuadrado/2}")

app = App(title="calculadora App")

resultado_1= Text(app, text="")
resultado_2= Text(app, text="")

message = Text(app, text="numero:")
input_num_pos = TextBox(app, width=20)
message = Text(app, text="numero:")
input_num_pos = TextBox(app, width=20)
calcular_button = PushButton(app, text="obtener suma", command=suma_c)
calcular_button = PushButton(app, text="obtener cuadrado", command=suma_c)
app.display()