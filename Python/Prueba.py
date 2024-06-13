sum1=1
sum2=2
resultado= sum1+sum2
print(resultado)

import tkinter as tk

def mostrar_mensaje():
    etiqueta.config(text="¡Hola, esta es tu primera aplicación de escritorio en Python!")

def center_window(window, width, height):
    # Obtiene el ancho y alto de la pantalla
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calcula las coordenadas X e Y para centrar la ventana
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Ubica la ventana en el centro de la pantalla
    window.geometry(f"{width}x{height}+{x}+{y}")    

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Primera Aplicación de Escritorio")
width = 800
height = 200

# Centrar la ventana
center_window(ventana, width, height)

# Crear etiqueta
etiqueta = tk.Label(ventana, text="¡Bienvenido a tu aplicación de escritorio!", font=("Arial", 16))
etiqueta.pack(pady=20)

# Crear botón
boton = tk.Button(ventana, text="Haz clic aquí", command=mostrar_mensaje)
boton.pack()

# Iniciar el bucle del evento principal
ventana.mainloop()

#declaramos una funcion
def suma(valor1, valor2):
    resultado = valor1 + valor2
    return resultado

#print(f"el resultado es : {suma(1,5)}" )
#esto es un array
numeros = [1,2,3,4]

#recorremos el array
for numero in numeros:
    print(f"ciclo for {numero}")
   
i = 0
while i < len(numeros):
    print(f"ciclo while {numeros[i]}")
    i += 1

#variable = "un string"

#resultado = sum1 + sum2
#print(resultado)
#print(variable)


edad=18
if edad >= 18:
    print("eres mayor de edad")
else:
    print("no eres mayor")