import streamlit as st

menu_opciones = ["Inicio", "Suma de dos números", "Área de un triángulo", "Calculadora de descuento", "Suma de una lista de números", "Producto", "números pares e impares", "multiplicación", "Información de una persona", "Calculadora flexible",]
selected_option = st.sidebar.selectbox("Opciones", menu_opciones)

match selected_option:
    case "inicio":
        st.subheader("bienvenid@ a CDH")
        
        nombre = st.text_input
        saludo = st.sidebar.selectbox("Añade tu nombre", nombre)
        st.write = (f"Hola {saludo}")

    case "suma de dos números":
        st.title("Calcular suma de dos números")

        a = st.number_input(min_value = 0.00, step = 1.00)
        b = st.number_input(min_value = 0.00, step = 1.00)
        st.sidebar.selectbox("Añade un numero", a)
        st.sidebar.selectbox("Añade un numero", b)
        resultado = a + b
        st.write(f"La suma es: {resultado}")
        
    case "Area de un triangulo":
        st.title("Calcular área de un triángulo")

        
        base = st.number_input(min_value = 0.00, step = 1.00)
        altura = st.number_input(min_value = 0.00, step = 1.00)
        st.sidebar.selectbox("Añade un numero", base)
        st.sidebar.selectbox("Añade un numero", altura)
        área = 0.5 * base * altura
        st.write(f"El área del triangulo es: {área} ")

    case "Calculadora de descuento":
        st.title("Calculadora de descuento")

        descuento = 10
        impuesto = 16
        producto = st.text_input
        st.sidebar.selectbox("Añade el nombre del producto", producto)

        precio_original = st.number_input(min_value = 0.00, step = 1.00)
        precio_con_descuento = precio_original * (1 - descuento / 100)
        calcular_precio_final = precio_con_descuento * (1 + impuesto / 100)

        st.write(f"El precio final de {producto} es: {calcular_precio_final}")

    case "Suma de una lista de números":
        st.title("Suma de una lista de números")

    case "Producto":    
        st.title("producto")

        producto = st.text_input
        st.sidebar.selectbox("añade nombre del producto", producto)

        cantidad = st.number_input(min_value= 1.00, step= 1.00)
        precio = st.number_input
        st.sidebar.selectbox("Añade el precio del producto", precio)
        precio_total = cantidad * precio
        st.write(f"El precio total de {cantidad} {producto}(s) es: {precio_total}")

    case "Números pares e impares":
        st.title("números pares e impares")

        def numeros_pares_e_impares(numeros):
            pares = []
            impares = []
            for numero in numeros:
                if numero % 2 == 0:
                    pares.append(numero)
                else:
                    impares.append(numero)
            return pares, impares

        lista_numeros = [st.number_input]
        st.sidebar.selectbox("Añade una lista de numeros mayor a 0", lista_numeros)
        pares, impares = numeros_pares_e_impares(lista_numeros)
        st.write(f"los números pares son: {pares}")
        st.writw(f"Los números impares son: {impares}")