from guizero import App, Text, TextBox, PushButton


def calcular_promedio():
    n1 = int(input_num_1.value)
    n2 = int(input_num_2.value)
    n3 = int(input_num_3.value)
    suma:int = n1 + n2 + n3
    resultado.value = (f"el promedio:es {suma/3}")

app = App(title="promedio de tres numeros App")

resultado= Text(app, text="")

message = Text(app, text="Dame el primer numero")
input_num_1 = TextBox(app, width=20)
message = Text(app, text="Dame el segundo numero")
input_num_2 = TextBox(app, width=20)
message = Text(app, text="Dame el tercer numero")
input_num_3 = TextBox(app, width=20)
button = PushButton(app, text="Calcular el promedio", command=calcular_promedio)
app.display()