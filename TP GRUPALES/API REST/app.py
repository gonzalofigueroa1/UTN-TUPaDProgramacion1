"""
Ejercicio 2: Definicion e Implementacion de Endpoints HTTP
Ejercicio 3: Manejo de Errores y Validaciones

API REST con Flask sobre la base biblioteca.db. Las sentencias SQL estan en
repositorio.py; aca se reciben las peticiones HTTP, se validan los datos y
se devuelve JSON con el codigo de estado que corresponde.

Ejecutar:  python app.py      ->  http://127.0.0.1:5000
"""

from flask import Flask, jsonify, request

import repositorio

app = Flask(__name__)


# 1. Recursos de Autores

# GET: Obtener todos los autores
@app.route('/api/autores', methods=['GET'])
def obtener_autores():
    autores = repositorio.obtener_autores_db()
    return jsonify(autores), 200


# GET: Obtener un autor por ID
@app.route('/api/autores/<int:id>', methods=['GET'])
def obtener_autor(id):
    autor = repositorio.obtener_autor_db(id)
    if autor is None:
        return jsonify({'error': 'Autor no encontrado'}), 404
    return jsonify(autor), 200


# POST: Crear un nuevo autor
@app.route('/api/autores', methods=['POST'])
def crear_autor():
    datos = request.get_json(silent=True)
    if not isinstance(datos, dict) or 'nombre' not in datos or 'nacionalidad' not in datos:
        return jsonify({'error': 'Datos incompletos'}), 400
    if not isinstance(datos['nombre'], str) or not datos['nombre'].strip():
        return jsonify({'error': 'El nombre no puede quedar vacio'}), 400

    nuevo_id = repositorio.insertar_autor_db(datos['nombre'], datos['nacionalidad'])
    nuevo_autor = repositorio.obtener_autor_db(nuevo_id)
    return jsonify(nuevo_autor), 201


# 2. Recursos de Libros

# GET: Obtener todos los libros
@app.route('/api/libros', methods=['GET'])
def obtener_libros():
    libros = repositorio.obtener_libros_db()
    return jsonify(libros), 200


# GET: Obtener un libro por ID
@app.route('/api/libros/<int:id>', methods=['GET'])
def obtener_libro(id):
    libro = repositorio.obtener_libro_db(id)
    if libro is None:
        return jsonify({'error': 'Libro no encontrado'}), 404
    return jsonify(libro), 200


# POST: Crear un nuevo libro
@app.route('/api/libros', methods=['POST'])
def crear_libro():
    datos = request.get_json(silent=True)
    if not isinstance(datos, dict) or 'titulo' not in datos or 'anio' not in datos or 'autor_id' not in datos:
        return jsonify({'error': 'Datos incompletos'}), 400

    if not isinstance(datos['titulo'], str) or not datos['titulo'].strip():
        return jsonify({'error': 'El titulo no puede quedar vacio'}), 400

    if not str(datos['anio']).isdigit() or not str(datos['autor_id']).isdigit():
        return jsonify({'error': 'anio y autor_id tienen que ser numeros enteros'}), 400

    anio = int(datos['anio'])
    autor_id = int(datos['autor_id'])

    # autor_id es clave foranea: si ese autor no existe, el pedido esta mal
    if repositorio.obtener_autor_db(autor_id) is None:
        return jsonify({'error': 'Autor no encontrado'}), 400

    nuevo_id = repositorio.insertar_libro_db(datos['titulo'], anio, autor_id)
    nuevo_libro = repositorio.obtener_libro_db(nuevo_id)
    return jsonify(nuevo_libro), 201


# PUT: Actualizar un libro
@app.route('/api/libros/<int:id>', methods=['PUT'])
def actualizar_libro(id):
    libro = repositorio.obtener_libro_db(id)
    if libro is None:
        return jsonify({'error': 'Libro no encontrado'}), 404

    datos = request.get_json(silent=True)
    if not isinstance(datos, dict) or not datos:
        return jsonify({'error': 'Datos incompletos'}), 400

    # Los campos que no vienen en el JSON quedan con el valor que ya tenian
    titulo = datos.get('titulo', libro['titulo'])
    anio = datos.get('anio', libro['anio'])
    autor_id = datos.get('autor_id', libro['autor']['id'])

    if not titulo:
        return jsonify({'error': 'El titulo no puede quedar vacio'}), 400

    if not str(anio).isdigit() or not str(autor_id).isdigit():
        return jsonify({'error': 'anio y autor_id tienen que ser numeros enteros'}), 400

    anio = int(anio)
    autor_id = int(autor_id)

    if repositorio.obtener_autor_db(autor_id) is None:
        return jsonify({'error': 'Autor no encontrado'}), 400

    repositorio.actualizar_libro_db(id, titulo, anio, autor_id)
    libro_actualizado = repositorio.obtener_libro_db(id)
    return jsonify(libro_actualizado), 200


# DELETE: Eliminar un libro
@app.route('/api/libros/<int:id>', methods=['DELETE'])
def eliminar_libro(id):
    filas = repositorio.eliminar_libro_db(id)
    if filas == 0:
        return jsonify({'error': 'Libro no encontrado'}), 404
    return jsonify({'mensaje': 'Libro eliminado correctamente'}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
