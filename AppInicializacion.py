import subprocess



def cmd(comando):
    resultado = subprocess.run(comando, shell=True)
    resultado.check_returncode()
    return 0

cmd('mkdir Prueba')
