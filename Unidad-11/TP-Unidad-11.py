import sqlite3
class Autor:
    def __init__(self, id_autor, nombre, nacionalidad):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad
    def __str__(self):
        return f"Autor [{self.id_autor}]: {self.nombre} ({self.nacionalidad})"

class Libro:
    def __init__(self, id_libro, titulo, anio_publicacion, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.autor = autor  # objeto de tipo Autor
 
    def __str__(self):
        return (f"Libro [{self.id_libro}]: '{self.titulo}, año:({self.anio_publicacion}) - Autor: {self.autor.nombre}")

conexion = sqlite3.connect('biblioteca.db')
cursor = conexion.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS autores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        nacionalidad TEXT NOT NULL
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS libros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        anio INTEGER,
        autor_id INTEGER NOT NULL,
        FOREIGN KEY (autor_id) REFERENCES autores(id)
    )
''')
def registrar_autor(nombre, nacionalidad):
    cursor.execute('''
        INSERT INTO autores (nombre, nacionalidad)
        VALUES (?, ?)
    ''', (nombre, nacionalidad))
    conexion.commit()
    return cursor.lastrowid

def registrar_libro(titulo, anio, autor_id):
    cursor.execute('''
            INSERT INTO libros (titulo, anio, autor_id)
            VALUES (?, ?, ?)
        ''', (titulo, anio, autor_id))
    conexion.commit()

def listar_libros():
    cursor.execute('''
    SELECT libros.titulo, libros.anio, autores.nombre
    FROM libros
    JOIN autores ON libros.autor_id = autores.id
    ''')
    filas = cursor.fetchall()
    for fila in filas:
        print(f"Título: {fila[0]} | Año: {fila[1]} | Autor: {fila[2]}")
listar_libros()

def actualizar_titulo_libro(id_libro, nuevo_titulo):
    cursor.execute(
        'UPDATE libros SET titulo = ? WHERE id = ?',
        (nuevo_titulo, id_libro)
    )
    conexion.commit()

def eliminar_libro(id_libro):
    cursor.execute(
        'DELETE FROM libros WHERE id = ?', 
        (id_libro,)
    )
    conexion.commit()

def inicializar_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS autores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            nacionalidad TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            anio INTEGER,
            autor_id INTEGER NOT NULL,
            FOREIGN KEY (autor_id) REFERENCES autores(id)
        )
    ''')
    conexion.commit()
def registrar_libro(titulo, anio, autor_id):
    cursor.execute('''
        INSERT INTO libros (titulo, anio, autor_id)
        VALUES (?, ?, ?)
    ''', (titulo, anio, autor_id))
    conexion.commit()
    return cursor.lastrowid
if __name__ == '__main__':
    # Inicializar la base de datos
    inicializar_db()

    # Registrar 2 autores y 3 libros
    id_autor1 = registrar_autor("Jorge Luis Borges", "Argentino")
    id_autor2 = registrar_autor("Julio Cortázar", "Argentino")

    id_libro1 = registrar_libro("El Aleph", 1949, id_autor1)
    id_libro2 = registrar_libro("Ficciones", 1944, id_autor1)
    id_libro3 = registrar_libro("Rayuela", 1963, id_autor2)

    # Listar todos los libros
    print("--- Libros registrados ---")
    listar_libros()

    # Actualizar un título y verificar el cambio
    actualizar_titulo_libro(id_libro3, "Rayuela (edición revisada)")
    print("\n--- Después de actualizar ---")
    listar_libros()

    # Eliminar un libro y mostrar el listado resultante
    eliminar_libro(id_libro2)
    print("\n--- Después de eliminar ---")
    listar_libros()

    conexion.close()