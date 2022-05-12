import subprocess

comando = 'ipconfig'

def cmd(coamndo):
    subprocess.run(coamndo, shell=True)
    return
