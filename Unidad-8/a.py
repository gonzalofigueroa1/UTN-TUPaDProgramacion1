with open("productos.txt","r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        producto = datos[0]
        precio = datos[1]
        cantidad = datos[2]
        print(f"Producto: {producto} | Precio: ${precio} | Cantidad: {cantidad}")
# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.
with open("productos.txt","a") as archivo:
    nuevo_producto = input("Ingrese un nuevo producto (nombre,precio,cantidad): ")
    archivo.write("\n" + nuevo_producto)
# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.
productos_diccionario = []
with open("productos.txt","r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        diccionario_productos = {
            "nombre": datos[0],
            "precio": datos[1],
            "cantidad": datos[2]
        }
        productos_diccionario.append(diccionario_productos)
# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.
buscado = input("Ingrese el nombre del producto a buscar: ")
encontrado = False
for producto in productos_diccionario:
    if producto["nombre"].lower() == buscado.lower():
        print(f"| Nombre: {producto["nombre"]} | Precio: {producto["precio"]} | Cantidad: {producto["cantidad"]} |")
        encontrado = True
        break
if encontrado == False:
    print("No se encontró el producto solicitado")
# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.
with open("productos.txt", "w") as archivo:
    for producto in productos_diccionario:
        linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        archivo.write(linea)
print("Archivos guardados")


# Al terminar, probá tu programa varias veces:
# ● ¿Se puede agregar más de un producto? # No se puede agregar mas de un producto, hay que iniciarlo otra vez cuando se quiere añadir otro. Esto se podria hacer con un bucle while
# ● ¿Se guarda todo correctamente? #Si, se guarda todo correctamente
# ● ¿Se muestra bien el resultado? #Si, se muestra todo bien