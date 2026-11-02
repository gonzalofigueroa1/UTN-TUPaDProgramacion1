from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
def crear_tablas():
    conexion = sqlite3.connect("taller.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS servicios (
            codigo TEXT PRIMARY KEY,
            descripcion TEXT NOT NULL,
            precio_hora REAL NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()
@app.route("/api/servicios", methods=["GET"])
def obtener_servicios():
    conexion = sqlite3.connect("taller.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT codigo, descripcion, precio_hora FROM servicios")
    servicios = cursor.fetchall()
    conexion.close()
    lista = []
    for s in servicios:
        print(f"| Codigo: {s[0]} | Descripción: {s[1]} | Precio hora: {s[2]} |")
        lista.append({
            "codigo": s[0],
            "descripcion": s[1],
            "precio_hora": s[2]
        })
    return jsonify(lista), 200

@app.route("/api/servicios", methods=["POST"])
def crear_servicio():
    datos = request.get_json()
    if not datos or "codigo" not in datos or "descripcion" not in datos or "precio_hora" not in datos:
        return jsonify({"error": "Datos incompletos"}), 400
    conexion = sqlite3.connect("taller.db")
    cursor = conexion.cursor()
    cursor.execute('''
            INSERT INTO servicios (codigo, descripcion, precio_hora)
            VALUES (?, ?, ?)
        ''', (datos["codigo"], datos["descripcion"], datos["precio_hora"]))
    conexion.commit()
    conexion.close()
    return jsonify(datos), 201

if __name__ == "__main__":
    crear_tablas()
    app.run(debug=True, port=5000)