import subprocess
import tkinter as tk


################ Comandos #################
comando = 'mkdir Prueba'

def ejecutar(comandos):
    subprocess.run(comandos, shell=True)

#ejecutar(comando)


##############      GUI     ##############

window = tk.Tk()
window.geometry('300x120')
mensaje = tk.Label(text="Inserte tiempo de ejecución")
mensaje.pack()

entry1 = tk.Entry(fg='black',bg='white',width=20)
entry1.pack()

mensaje = tk.Label(text="Inserte tiempo de muestreo")
mensaje.pack()

entry2 = tk.Entry(fg='black',bg='white',width=20)
entry2.pack()

##def handle_keypress(event):
##    """Print the character associated to the key pressed"""
##    print(event.char)




def handle_click(event):
    tiempoEjec = entry1.get()
    tiempoMues = entry2.get()

button = tk.Button(text="Ejecutar")
button.pack()

button.bind("<Button-1>", handle_click)

# Bind keypress event to handle_keypress()
##window.bind("<Key>", handle_keypress)

window.mainloop()
