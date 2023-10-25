from guizero import App, Text, TextBox, PushButton

def calcular_cuadrado():
    cuadrado = str(int(numero.value)**2)
    resultado.value = f"el cuadrado es:{cuadrado}"

app = App(title="calculadora App")

resultado= Text(app, text="")

message = Text(app, text="Dame un numero:")
numero = TextBox(app, width=20)
calcular_button = PushButton(app, text="obtener cuadrado", command=calcular_cuadrado)
app.display()
