import subprocess
import tkinter as tk
import time

################ Comandos #################
comando = 'mkdir Prueba'
comando2 = 'mkdir Prueba2'

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
    ver1 = verificacion(tiempoEjec)
    ver2 = verificacion(tiempoMues)
    ver3 = verificacion2(tiempoEjec,tiempoMues)
    if (ver1 and ver2 and ver3):
        ejecutar(comando)
        tiempoEjec = int(tiempoEjec)
        time.sleep(tiempoEjec + 10)
        ejecutar(comando2)
    

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
    else:
        return True

def verificacion2(tiempoEjec,tiempoMues):
    if tiempoEjec < tiempoMues:
        mensaje2 = tk.Label(text="El tiempo de ejecución debe")
        mensaje2.config(font=("Courier", 12))
        mensaje2.pack()
        mensaje2 = tk.Label(text="ser mayor que el de muestreo")
        mensaje2.config(font=("Courier", 12))
        mensaje2.pack()
        return False
    else: return True
    
        

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


        
    
