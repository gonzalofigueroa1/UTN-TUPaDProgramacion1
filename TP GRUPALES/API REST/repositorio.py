"""
Ejercicio 1: Reutilizacion de la Base de Datos SQLite

Funciones repositorio que ejecutan las sentencias SQL sobre la biblioteca.db
que ya habiamos hecho en el TP de Acceso a Datos (tablas autores y libros).

Mismo flujo de siempre: conectar -> cursor -> execute -> commit -> close.
Las funciones devuelven diccionarios porque son los que despues jsonify
convierte a JSON en app.py.
"""

import os
import sqlite3

# Ruta junto al .py, no al directorio desde donde se ejecuta.
DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "biblioteca.db")


def conectar():
    """Abre la conexion y activa las claves foraneas."""
    conexion = sqlite3.connect(DB)
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion


# Autores

def obtener_autores_db():
    """READ: retorna la lista completa de autores."""
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute('SELECT id, nombre, nacionalidad FROM autores ORDER BY id')
    filas = cursor.fetchall()

    conexion.close()

    autores = []
    for fila in filas:
        autores.append({
            'id': fila[0],
            'nombre': fila[1],
            'nacionalidad': fila[2]
        })
    return autores


def obtener_autor_db(id):
    """READ: retorna un autor por su ID, o None si no existe."""
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        'SELECT id, nombre, nacionalidad FROM autores WHERE id = ?',
        (id,)
    )
    fila = cursor.fetchone()

    conexion.close()

    if fila is None:
        return None

    return {
        'id': fila[0],
        'nombre': fila[1],
        'nacionalidad': fila[2]
    }


def insertar_autor_db(nombre, nacionalidad):
    """CREATE: inserta un autor y retorna el ID que genero SQLite."""
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        'INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)',
        (nombre, nacionalidad)
    )

    conexion.commit()
    nuevo_id = cursor.lastrowid
    conexion.close()
    return nuevo_id


# Libros

def obtener_libros_db():
    """READ: retorna todos los libros con los datos de su autor (JOIN)."""
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute('''
        SELECT l.id, l.titulo, l.anio, a.id, a.nombre, a.nacionalidad
        FROM libros AS l
        JOIN autores AS a ON a.id = l.autor_id
        ORDER BY l.id
    ''')
    filas = cursor.fetchall()

    conexion.close()

    libros = []
    for fila in filas:
        libros.append({
            'id': fila[0],
            'titulo': fila[1],
            'anio': fila[2],
            'autor': {
                'id': fila[3],
                'nombre': fila[4],
                'nacionalidad': fila[5]
            }
        })
    return libros


def obtener_libro_db(id):
    """READ: retorna un libro por su ID con su autor, o None si no existe."""
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute('''
        SELECT l.id, l.titulo, l.anio, a.id, a.nombre, a.nacionalidad
        FROM libros AS l
        JOIN autores AS a ON a.id = l.autor_id
        WHERE l.id = ?
    ''', (id,))
    fila = cursor.fetchone()

    conexion.close()

    if fila is None:
        return None

    return {
        'id': fila[0],
        'titulo': fila[1],
        'anio': fila[2],
        'autor': {
            'id': fila[3],
            'nombre': fila[4],
            'nacionalidad': fila[5]
        }
    }


def insertar_libro_db(titulo, anio, autor_id):
    """CREATE: inserta un libro vinculado a un autor y retorna su ID."""
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        'INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)',
        (titulo, anio, autor_id)
    )

    conexion.commit()
    nuevo_id = cursor.lastrowid
    conexion.close()
    return nuevo_id


def actualizar_libro_db(id, titulo, anio, autor_id):
    """UPDATE: actualiza los datos de un libro. Retorna las filas modificadas."""
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        'UPDATE libros SET titulo = ?, anio = ?, autor_id = ? WHERE id = ?',
        (titulo, anio, autor_id, id)
    )

    conexion.commit()
    filas = cursor.rowcount
    conexion.close()
    return filas


def eliminar_libro_db(id):
    """DELETE: borra un libro por su ID. Retorna las filas borradas."""
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute('DELETE FROM libros WHERE id = ?', (id,))

    conexion.commit()
    filas = cursor.rowcount
    conexion.close()
    return filas
