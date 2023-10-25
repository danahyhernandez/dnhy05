from guizero import App, Text, TextBox, PushButton

def suma_ncapturados():
    numero_1 = int(input_numero_1.value)
    numero_2 = int(input_numero_2.value)
    numero_3 = int(input_numero_3.value)
    suma = numero_1 + numero_2 + numero_3
    resultado.value = (f"la suma es:{suma}")

app = App(title="calculadora App")

resultado= Text(app, text="")

message = Text(app, text="Dame el numero:")
input_numero_1 = TextBox(app, width=20)
message = Text(app, text="Dame el numero:")
input_numero_2 = TextBox(app, width=20)
message = Text(app, text="Dame el numero:")
input_numero_3 = TextBox(app, width=20)
calcular_button = PushButton(app, text="obtener suma ", command=suma_ncapturados)
app.display()