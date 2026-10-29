# Para aclarar:
# actualice el codigo de la unidad 11 para que este mas adaptada a este trabajo, la otra unidad queda con el codigo original

import sqlite3
nombre_datos = 'biblioteca.db'

def get_conexion():
    conexion = sqlite3.connect(nombre_datos)
    conexion.row_factory = sqlite3.Row
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion

def inicializar_db():
    conexion = get_conexion()
    conexion.execute('''
        CREATE TABLE IF NOT EXISTS autores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            nacionalidad TEXT NOT NULL
        )
    ''')
    conexion.execute('''
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            anio INTEGER,
            autor_id INTEGER NOT NULL,
            FOREIGN KEY (autor_id) REFERENCES autores(id)
        )
    ''')
    conexion.commit()
    conexion.close()

def obtener_autores_db():
    conexion = get_conexion()
    filas = conexion.execute(
        'SELECT id, nombre, nacionalidad FROM autores'
    ).fetchall()
    conexion.close()
    return [dict(fila) for fila in filas]

def obtener_autor_db(id):
    conexion = get_conexion()
    fila = conexion.execute(
        'SELECT id, nombre, nacionalidad FROM autores WHERE id = ?',
        (id,)
    ).fetchone()
    conexion.close()
    return dict(fila) if fila else None

def insertar_autor_db(nombre, nacionalidad):
    conexion = get_conexion()
    cursor = conexion.execute(
        'INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)',
        (nombre, nacionalidad)
    )
    conexion.commit()
    nuevo_id = cursor.lastrowid
    conexion.close()
    return nuevo_id

def obtener_libros_db():
    conexion = get_conexion()
    filas = conexion.execute('''
        SELECT libros.id, libros.titulo, libros.anio, libros.autor_id,
               autores.nombre AS autor_nombre,
               autores.nacionalidad AS autor_nacionalidad
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
    ''').fetchall()
    conexion.close()
    return [dict(fila) for fila in filas]

def obtener_libro_db(id):
    conexion = get_conexion()
    fila = conexion.execute('''
        SELECT libros.id, libros.titulo, libros.anio, libros.autor_id,
               autores.nombre AS autor_nombre,
               autores.nacionalidad AS autor_nacionalidad
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
        WHERE libros.id = ?
    ''', (id,)).fetchone()
    conexion.close()
    return dict(fila) if fila else None

def insertar_libro_db(titulo, anio, autor_id):
    conexion = get_conexion()
    cursor = conexion.execute(
        'INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)',
        (titulo, anio, autor_id)
    )
    conexion.commit()
    nuevo_id = cursor.lastrowid
    conexion.close()
    return nuevo_id

def actualizar_libro_db(id, titulo, anio, autor_id):
    conexion = get_conexion()
    cursor = conexion.execute(
        'UPDATE libros SET titulo = ?, anio = ?, autor_id = ? WHERE id = ?',
        (titulo, anio, autor_id, id)
    )
    conexion.commit()
    filas_afectadas = cursor.rowcount
    conexion.close()
    return filas_afectadas  # 1 si actualizo, 0 si el id no existe

def eliminar_libro_db(id):
    conexion = get_conexion()
    cursor = conexion.execute('DELETE FROM libros WHERE id = ?', (id,))
    conexion.commit()
    filas_afectadas = cursor.rowcount
    conexion.close()
    return filas_afectadas  # 1 si elimino, 0 si el id no existe

if __name__ == '__main__':
    inicializar_db()
    print("Base de datos inicializada.")