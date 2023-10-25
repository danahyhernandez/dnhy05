from guizero import App, Text, TextBox, PushButton

def años_persona():
    a_actual = int(input_a_actual.value)>2023
    a_nacimiento = int(input_a_nacimiento.value)<2023
    a_persona = a_actual - a_nacimiento
    edad = a_persona + 1
    resultado.value = (f"Vas a cumplir {edad} años")


app = App(title="calculadora App")

resultado= Text(app, text="")

message = Text(app, text="Dame el año actual:")
input_a_actual = TextBox (app, width=20)
message = Text(app, text="Dame el año de nacimiento:")
input_a_nacimiento = TextBox(app, width=20)
calcular_button = PushButton(app, text="obtener la edad que va a cumpli", command=años_persona)
app.display()