from guizero import App, Text, TextBox, PushButton

def generador_s():
    n = int(input_n.value)
    n = n
    a = int(input_a.value)
    a = a
    b = int(input_b.value)
    b = b
    secuencia = (a,b) * n
    resultado.value = (f"la secuencia es:{secuencia}")

app = App(title="secuenciador app")

resultado = Text(app, text="")

message = Text(app, text="cuantos numeros:")
input_n = TextBox(app,width=20)
message = Text(app, text="añade el numero:")
input_a = TextBox(app,width=20)
message = Text(app, text="añade el numero:")
input_b = TextBox(app,width=20)
calcular_button = PushButton(app, text="obtener secuencia", command=generador_s)
app.display()