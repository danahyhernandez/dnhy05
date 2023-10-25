from guizero import App, Text, TextBox, PushButton

def calcular_edad():
        a_actual = int(input_a_actual.value)
        a_nacimiento = int(input_a_nacimiento.value)
        resultado.value = (f"edad: tienes {a_actual - a_nacimiento} años")


app = App(title="calculadora ICI App")

resultado = Text(app, text="")

message = Text(app, text="Dame el año actual:")
input_a_actual= TextBox(app, width=20)
message = Text(app, text="Dame el año de nacimiento:")
input_a_nacimiento = TextBox(app, width=20)
calcular_button = PushButton(app, text="obtener la edad", command=calcular_edad)
app.display()