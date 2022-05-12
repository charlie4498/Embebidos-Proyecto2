import subprocess
import tkinter as tk


################ Conados #################
comando = 'mkdir Prueba'

def ejecutar(comandos):
    subprocess.run(comandos, shell=True)

#ejecutar(comando)


##############      GUI     ##############

window = tk.Tk()
mensaje = tk.Label(text="Inserte tiempo de ejecución")
mensaje.pack()

entry1 = tk.Entry(fg='black',bg='white',width=20)
entry1.pack()
tiempoEjec = entry1.get()

mensaje = tk.Label(text="Inserte tiempo de muestreo")
mensaje.pack()

entry1 = tk.Entry(fg='black',bg='white',width=20)
entry1.pack()
tiempoMues = entry1.get()

window.mainloop()
