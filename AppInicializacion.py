import subprocess
import tkinter as tk

################ Comandos #################
comando = 'mkdir Prueba'

def ejecutar(comandos):
    subprocess.run(comandos, shell=True)

#ejecutar(comando)


##############      GUI     ##############

##  Funciones

def handle_click(event):
    tiempoEjec = entry1.get()
    #print(type(tiempoEjec))
    tiempoMues = entry2.get()
    #print(type(tiempoEjec))
    verificacion(tiempoEjec)
    verificacion(tiempoMues)


##def verificacion(tiempoEjec,tiempoMues):
##    if (type(int(tiempoEjec)) != int or type(tiempoMues) != int):
##        mensaje2 = tk.Label(text="Error en los datos introducidos")
##        mensaje2.config(font=("Courier", 12))
##        mensaje2.pack()
##        mensaje2 = tk.Label(text="Vuelva a ejecutar la aplicación")
##        mensaje2.config(font=("Courier", 12))
##        mensaje2.pack()
##    else:
##        ejecutar(comando)

def verificacion(entrada):
    try:
        (int(entrada))
        
    except:
        mensaje2 = tk.Label(text="Error en los datos introducidos")
        mensaje2.config(font=("Courier", 12))
        mensaje2.pack()
        mensaje2 = tk.Label(text="Vuelva a ejecutar la aplicación")
        mensaje2.config(font=("Courier", 12))
        mensaje2.pack()



## MAIN

window = tk.Tk()
window.geometry('400x153')
mensaje = tk.Label(text="Inserte tiempo de ejecución")
mensaje.pack()

entry1 = tk.Entry(fg='black',bg='white',width=20)
entry1.pack()

mensaje = tk.Label(text="Inserte tiempo de muestreo")
mensaje.pack()

entry2 = tk.Entry(fg='black',bg='white',width=20)
entry2.pack()

button = tk.Button(text="Ejecutar")
button.pack()

button.bind("<Button-1>", handle_click)

window.mainloop()


        
    
