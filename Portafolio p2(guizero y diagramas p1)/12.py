from guizero import App, Text, TextBox, PushButton

def día_semana():
    dia = int(input_dia.value)
    dia = ("lunes","martes","miercoles","jueves","viernes","sabado","domingo") 

    resultado.value = (f"el día es: {dia}")

app = App(title="dia de la semana app")
resultado = Text(app, text="")

message = Text(app, text="dame el dia")
message = Text(app, text="menor que 7")
input_dia = TextBox(app, width=20)
calcular_button = PushButton(app, text="buscar", command=día_semana)
app.display()