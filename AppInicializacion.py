import subprocess

comando = 'mkdir Prueba'

def ejecutar(comandos):
    subprocess.run(comandos, shell=True)

ejecutar(comando)
