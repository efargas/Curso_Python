import os

PATH = './2-ConceptosBasicos/Ejercicio_2/a_renombrar/'
archivos = os.listdir(PATH)
for archivo in archivos:
    fd = open(PATH+archivo)
    fn = fd.read()
    fd.close()
    newfn = os.rename(PATH+archivo,PATH+fn)