from repositorio import *
from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route('/api/autores', methods=['GET'])
def obtener_autores():
    autores = obtener_autores_db()
    return jsonify(autores), 200

@app.route('/api/autores', methods=['POST'])
def crear_autor():
    datos = request.get_json(silent=True)
    if not datos or "nombre" not in datos or "nacionalidad" not in datos:
        return jsonify({"error": "Faltan campos obligatorios: nombre, nacionalidad"}), 400
    nuevo_id = insertar_autor_db(datos['nombre'], datos['nacionalidad'])
    autor = obtener_autor_db(nuevo_id)
    return jsonify(autor), 201

@app.route("/api/libros", methods=["GET"])
def info_libros():
    datos = obtener_libros_db()
    return jsonify(datos), 200

@app.route('/api/libros/<int:id>', methods=['GET'])
def obtener_libro(id):
    libro = obtener_libro_db(id)
    if libro:
        return jsonify(libro), 200
    return jsonify({'error': 'Libro no encontrado'}), 404

@app.route("/api/libros", methods=["POST"])
def subir_libro():
    datos = request.get_json(silent=True)
    if not datos or "titulo" not in datos or "anio" not in datos or "autor_id" not in datos:
        return jsonify({"error": "Faltan campos obligatorios: titulo, anio, autor_id"}), 400
    if not obtener_autor_db(datos["autor_id"]):
        return jsonify({"error": "Autor no encontrado"}), 404
    nuevo_id = insertar_libro_db(datos["titulo"], datos["anio"], datos["autor_id"])
    libro = obtener_libro_db(nuevo_id)
    return jsonify(libro), 201

@app.route('/api/libros/<int:id>', methods=['PUT'])
def actualizar_libro(id):
    datos = request.get_json(silent=True)
    if not datos:
        return jsonify({"error": "El cuerpo debe ser un JSON con los campos a modificar"}), 400 
    libro = obtener_libro_db(id)
    if not libro:
        return jsonify({"error": "Libro no encontrado"}), 404
    titulo = datos.get("titulo", libro["titulo"])
    anio = datos.get("anio", libro["anio"])
    autor_id = datos.get("autor_id", libro["autor_id"])
    actualizar_libro_db(id, titulo, anio, autor_id)
    return jsonify(obtener_libro_db(id)), 200

@app.route('/api/libros/<int:id>', methods=['DELETE'])
def eliminar_libro(id):
    filas = eliminar_libro_db(id)
    if filas == 0:
        return jsonify({"error": "Libro no encontrado"}), 404
    return jsonify({"mensaje": "Libro eliminado"}), 200 

if __name__ == '__main__':
    inicializar_db()
    app.run(debug=True, port=5000)