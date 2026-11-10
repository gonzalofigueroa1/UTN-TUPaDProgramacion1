"""
TP Grupal - Acceso a Datos
Sistema de Gestion de Biblioteca (POO + SQLite)

Sigue el flujo de la Guia Practica de la catedra:
conectar -> cursor -> execute -> commit -> close
"""

import os
import sqlite3

# Ruta junto al .py, no al directorio desde donde se ejecuta:
# asi la base es siempre la misma sin importar el cwd de la terminal.
DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "biblioteca.db")


def conectar():
    """Abre la conexion y activa las claves foraneas (SQLite las ignora por defecto)."""
    conexion = sqlite3.connect(DB)
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion


# Ejercicio 1: Modelado de Clases (POO)


class Autor:
    def __init__(self, id_autor, nombre, nacionalidad):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad})"


class Libro:
    def __init__(self, id_libro, titulo, anio_publicacion, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.autor = autor  # agregacion: un Libro "tiene un" Autor

    def __str__(self):
        return f'"{self.titulo}" ({self.anio_publicacion}) - {self.autor}'


# Ejercicio 2: Creacion del Esquema en Base de Datos

def inicializar_db():
    """Crea biblioteca.db con las tablas autores y libros (DDL)."""
    conexion = conectar()
    try:
        cursor = conexion.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS autores (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre        TEXT NOT NULL,
                nacionalidad  TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS libros (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo    TEXT NOT NULL,
                anio      INTEGER,
                autor_id  INTEGER,
                FOREIGN KEY (autor_id) REFERENCES autores(id)
            )
        ''')

        conexion.commit()
    finally:
        conexion.close()


# Ejercicio 3: Repositorio CRUD

def registrar_autor(nombre, nacionalidad):
    """CREATE: inserta un autor y retorna el ID que genero SQLite."""
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        nuevo_autor = (nombre, nacionalidad)

        cursor.execute('''
            INSERT INTO autores (nombre, nacionalidad)
            VALUES (?, ?)
        ''', nuevo_autor)

        conexion.commit()
        return cursor.lastrowid
    finally:
        conexion.close()


def registrar_libro(titulo, anio, autor_id):
    """CREATE: inserta un libro vinculado a un autor y retorna su ID."""
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        nuevo_libro = (titulo, anio, autor_id)

        cursor.execute('''
            INSERT INTO libros (titulo, anio, autor_id)
            VALUES (?, ?, ?)
        ''', nuevo_libro)

        conexion.commit()
        return cursor.lastrowid
    finally:
        conexion.close()


def listar_libros():
    """READ: SELECT con JOIN. Devuelve una lista de objetos Libro."""
    conexion = conectar()
    try:
        cursor = conexion.cursor()

        cursor.execute('''
            SELECT l.id, l.titulo, l.anio, a.id, a.nombre, a.nacionalidad
            FROM libros AS l
            JOIN autores AS a ON a.id = l.autor_id
            ORDER BY l.id
        ''')
        filas = cursor.fetchall()
    finally:
        conexion.close()

    # Convertimos cada fila (tupla) en los objetos del Ejercicio 1
    libros = []
    for fila in filas:
        autor = Autor(fila[3], fila[4], fila[5])
        libros.append(Libro(fila[0], fila[1], fila[2], autor))
    return libros


def actualizar_titulo_libro(id_libro, nuevo_titulo):
    """UPDATE: cambia el titulo de un libro. Retorna cuantas filas se modificaron."""
    conexion = conectar()
    try:
        cursor = conexion.cursor()

        cursor.execute(
            'UPDATE libros SET titulo = ? WHERE id = ?',
            (nuevo_titulo, id_libro)
        )

        conexion.commit()
        return cursor.rowcount
    finally:
        conexion.close()


def eliminar_libro(id_libro):
    """DELETE: borra un libro por su ID. Retorna cuantas filas se borraron."""
    conexion = conectar()
    try:
        cursor = conexion.cursor()

        cursor.execute('DELETE FROM libros WHERE id = ?', (id_libro,))

        conexion.commit()
        return cursor.rowcount
    finally:
        conexion.close()


def mostrar_libros(titulo_seccion):
    """Imprime el listado en consola."""
    print(f"\n--- {titulo_seccion} ---")
    for libro in listar_libros():
        print(f"  [{libro.id_libro}] {libro}")


# Ejercicio 4: Integracion y Prueba Integral

if __name__ == "__main__":
    # 1) Inicializar la base (arrancamos de cero para que la prueba sea repetible)
    if os.path.exists(DB):
        os.remove(DB)
    inicializar_db()
    print("Base de datos inicializada.")

    # 2) Registrar 2 autores y 3 libros
    id_cortazar = registrar_autor("Julio Cortazar", "Argentina")
    id_borges = registrar_autor("Jorge Luis Borges", "Argentina")

    id_rayuela = registrar_libro("Rayuela", 1963, id_cortazar)
    id_bestiario = registrar_libro("Bestiario", 1951, id_cortazar)
    id_ficciones = registrar_libro("Ficciones", 1944, id_borges)

    print(f"Autores registrados con ID: {id_cortazar}, {id_borges}")
    print("Libros registrados: 3")

    # 3) Listar todos los libros
    mostrar_libros("Listado inicial")
    assert len(listar_libros()) == 3

    # 4) Actualizar un titulo y verificar el cambio
    assert actualizar_titulo_libro(id_rayuela, "Rayuela (edicion revisada)") == 1
    mostrar_libros("Despues del UPDATE")
    titulos = [libro.titulo for libro in listar_libros()]
    assert "Rayuela (edicion revisada)" in titulos

    # 5) Eliminar un libro y mostrar el listado resultante
    assert eliminar_libro(id_bestiario) == 1
    mostrar_libros("Despues del DELETE")
    assert len(listar_libros()) == 2

    print("\nTodas las verificaciones pasaron correctamente.")
