"""
Ejercicio 4: Script de Prueba

Consume la API con la libreria requests y hace la secuencia completa:
GET -> POST autor -> POST libro -> PUT -> DELETE.

Primero levantar el servidor en otra terminal:  python app.py
Despues ejecutar:  python test_api.py
"""

import requests

BASE = 'http://127.0.0.1:5000/api'


def mostrar(paso, respuesta):
    """Imprime el resultado de cada peticion."""
    print(f"\n{paso}")
    print(f"  Codigo: {respuesta.status_code}")
    print(f"  Cuerpo: {respuesta.json()}")


# 1. Hacer GET a /api/libros

respuesta = requests.get(f"{BASE}/libros")
mostrar("1) GET /api/libros", respuesta)
assert respuesta.status_code == 200
cantidad_inicial = len(respuesta.json())


# 2. Hacer POST para crear un autor y luego un libro

respuesta = requests.post(f"{BASE}/autores", json={
    'nombre': 'Ursula K. Le Guin',
    'nacionalidad': 'Estados Unidos'
})
mostrar("2a) POST /api/autores", respuesta)
assert respuesta.status_code == 201
id_autor = respuesta.json()['id']

respuesta = requests.post(f"{BASE}/libros", json={
    'titulo': 'Los desposeidos',
    'anio': 1974,
    'autor_id': id_autor
})
mostrar("2b) POST /api/libros", respuesta)
assert respuesta.status_code == 201
id_libro = respuesta.json()['id']


# 3. Hacer PUT para actualizar el titulo del libro recien creado

respuesta = requests.put(f"{BASE}/libros/{id_libro}", json={
    'titulo': 'Los desposeidos (edicion revisada)'
})
mostrar("3) PUT /api/libros/<id>", respuesta)
assert respuesta.status_code == 200
assert respuesta.json()['titulo'] == 'Los desposeidos (edicion revisada)'
assert respuesta.json()['anio'] == 1974  # el anio no se envio y no se perdio


# 4. Hacer DELETE y verificar que el libro ya no esta

respuesta = requests.delete(f"{BASE}/libros/{id_libro}")
mostrar("4a) DELETE /api/libros/<id>", respuesta)
assert respuesta.status_code == 200

respuesta = requests.get(f"{BASE}/libros/{id_libro}")
mostrar("4b) GET del libro eliminado", respuesta)
assert respuesta.status_code == 404

respuesta = requests.get(f"{BASE}/libros")
assert len(respuesta.json()) == cantidad_inicial


# 5. Pruebas de los errores del Ejercicio 3

respuesta = requests.post(f"{BASE}/libros", json={'titulo': 'Sin anio ni autor'})
mostrar("5a) POST sin campos obligatorios -> 400", respuesta)
assert respuesta.status_code == 400

respuesta = requests.put(f"{BASE}/libros/9999", json={'titulo': 'Fantasma'})
mostrar("5b) PUT con un id inexistente -> 404", respuesta)
assert respuesta.status_code == 404

respuesta = requests.delete(f"{BASE}/libros/9999")
mostrar("5c) DELETE con un id inexistente -> 404", respuesta)
assert respuesta.status_code == 404


print("\nTodas las pruebas pasaron correctamente.")
