from guizero import App, Text, TextBox, PushButton

def promedio_n():
    n: int = 10
    suma_numeros: int = 0
    numeros = int(input_numeros.value)
    suma_numeros: int = suma_numeros + numeros
    promedio_numeros: float = suma_numeros/n
    resultado.value = (f"el promedio es: {promedio_numeros}")

app = App(title="calculadora de promedio App")

resultado = Text(app, text="")

message = Text(app, text="numero:")
input_numeros = TextBox(app, width=20)
calcular_button = PushButton(app, text="obtener promedio", command=promedio_n)
app.display()