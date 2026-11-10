class Archivo:
    def __init__(self, nombre: str, tamano_bytes: int):
        self.nombre = nombre
        self.tamano_bytes = tamano_bytes

class Directorio:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.archivos = []
        self.subdirectorios = []

#funcion 1
def calcular_tamano_total(directorio: Directorio) -> int:
    total = 0
    for archivo in directorio.archivos: #caso base
        total += archivo.tamano_bytes
    for sub in directorio.subdirectorios: #recursividad
        total += calcular_tamano_total(sub)   
    return total                              

#funcion 2
def buscar_por_extension(directorio: Directorio, extension: str) -> list[str]:
    rutas = []
    for archivo in directorio.archivos: #caso base
        if archivo.nombre.endswith(extension):
            rutas.append(directorio.nombre + "/" + archivo.nombre)
    for sub in directorio.subdirectorios: #recursividad
        for ruta in buscar_por_extension(sub, extension):   
            rutas.append(directorio.nombre + "/" + ruta)
    return rutas

# Punto 3:

def limpiar_archivos_vacios(directorio: Directorio) -> int:
    eliminados = 0

    for archivo in directorio.archivos[:]:
        if archivo.tamano_bytes == 0:
            directorio.archivos.remove(archivo)
            eliminados += 1

    for subdirectorio in directorio.subdirectorios:
        eliminados += limpiar_archivos_vacios(subdirectorio)

    return eliminados

# Punto 4:

root = Directorio("root")
imagenes = Directorio("imagenes")
proyectos = Directorio("proyectos")
temp = Directorio("temp")

root.archivos.append(Archivo("documento.pdf", 1500))
root.archivos.append(Archivo("config.txt", 0))

imagenes.archivos.append(Archivo("foto1.png", 2000))
imagenes.archivos.append(Archivo("foto2.png", 3500))

proyectos.archivos.append(Archivo("avance.pdf", 800))
temp.archivos.append(Archivo("log.txt", 0))

root.subdirectorios.append(imagenes)
root.subdirectorios.append(proyectos)
proyectos.subdirectorios.append(temp)
root.archivos.append(Archivo("excel.xls", 10000))


print(calcular_tamano_total(root))
print(buscar_por_extension(root, ".pdf"))
print(limpiar_archivos_vacios(root))