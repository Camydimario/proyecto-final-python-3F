from .conexiondb import ConexionDB

def crear_tabla():
    conn = ConexionDB()
    
    sql_modalidad = """
        CREATE TABLE IF NOT EXISTS Modalidades (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Tipo TEXT NOT NULL UNIQUE
        );
    """
    
    sql_profesores = """
        CREATE TABLE IF NOT EXISTS Profesores (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL,
            Cursos TEXT NOT NULL,
            Modalidad_ID INTEGER,
            FOREIGN KEY (Modalidad_ID) REFERENCES Modalidades(ID)
        );
    """
    
    sql_cursos = """
        CREATE TABLE IF NOT EXISTS Cursos(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre VARCHAR(150),
        Profesor_ID INTEGER,
        Fecha TEXT NOT NULL,
        Modalidad_ID INTEGER,
        Estado BOOLEAN NOT NULL,
        FOREIGN KEY (Profesor_ID) REFERENCES Profesores(ID),
        FOREIGN KEY (Modalidad_ID) REFERENCES Modalidades(ID)
        );
    """

    try:
        conn.cursor.execute(sql_modalidad)
        conn.cursor.execute(sql_profesores)
        conn.cursor.execute(sql_cursos)
        conn.cerrar_conexion()
    except:
        print("No se pudo crear correctamente las tablas!")
    
class Cursos:
    def __init__(self, nombre, profesor, fecha, modalidad_id, estado):
        self.nombre = nombre
        self.profesor = profesor
        self.fecha = fecha
        self.modalidad_id = modalidad_id
        self.estado = estado

    def __str__(self):
        return f'Cursos[{self.nombre}, {self.profesor}, {self.fecha}, {self.modalidad_id}, {self.estado}]'

#Función para mostrar los datos en el treeview
def listar_cursos():
    conn = ConexionDB()
    sql = """
        SELECT c.ID, c.Nombre, p.Nombre, c.Fecha, m.Tipo,
               CASE c.Estado WHEN 1 THEN 'Sí' ELSE 'No' END
        FROM Cursos c
        JOIN Profesores p ON c.Profesor_ID = p.ID
        JOIN Modalidades m ON c.Modalidad_ID = m.ID
    """
    try:
        conn.cursor.execute(sql)
        cursos = conn.cursor.fetchall()
        conn.cerrar_conexion()
        return cursos
    except:
        return []

# Función para obtener todas las modalidades registradas (ID y tipo)
def listar_modalidades():
    conn = ConexionDB()
    conn.cursor.execute("SELECT ID, Tipo FROM Modalidades")
    modalidades = conn.cursor.fetchall()
    conn.cerrar_conexion()
    return modalidades

# Guarda un nuevo curso. Si el profesor o la modalidad no existen, los crea.    
def guardar_campos(curso):
    conn = ConexionDB()

    # Buscar o insertar modalidad
    conn.cursor.execute("SELECT ID FROM Modalidades WHERE Tipo = ?", (curso.modalidad_id,))
    modalidad_row = conn.cursor.fetchone()

    if modalidad_row:
        modalidad_id = modalidad_row[0]
    else:
        conn.cursor.execute("INSERT INTO Modalidades (Tipo) VALUES (?)", (curso.modalidad_id,))
        modalidad_id = conn.cursor.lastrowid

    # Buscar o insertar profesor
    conn.cursor.execute("SELECT ID FROM Profesores WHERE Nombre = ?", (curso.profesor,))
    row = conn.cursor.fetchone()
    if row:
        profesor_id = row[0]
    else:
        conn.cursor.execute("INSERT INTO Profesores (Nombre, Cursos, Modalidad_ID) VALUES (?, ?, ?)",
                            (curso.profesor, curso.nombre, modalidad_id))
        profesor_id = conn.cursor.lastrowid

    # Guardar curso
    conn.cursor.execute("""
        INSERT INTO Cursos (Nombre, Profesor_ID, Fecha, Modalidad_ID, Estado)
        VALUES (?, ?, ?, ?, ?)""",
        (curso.nombre, profesor_id, curso.fecha, modalidad_id, int(curso.estado)))

    conn.cerrar_conexion()


# Actualiza un curso existente, insertando modalidad/profesor si no existen
def editar_campos(curso, id):
    conn = ConexionDB()

    # Buscar o insertar modalidad
    conn.cursor.execute("SELECT ID FROM Modalidades WHERE Tipo = ?", (curso.modalidad_id,))
    modalidad_row = conn.cursor.fetchone()

    if modalidad_row:
        modalidad_id = modalidad_row[0]
    else:
        conn.cursor.execute("INSERT INTO Modalidades (Tipo) VALUES (?)", (curso.modalidad_id,))
        modalidad_id = conn.cursor.lastrowid

    # Buscar o insertar profesor
    conn.cursor.execute("SELECT ID FROM Profesores WHERE Nombre = ?", (curso.profesor,))
    row = conn.cursor.fetchone()
    if row:
        profesor_id = row[0]
    else:
        conn.cursor.execute("INSERT INTO Profesores (Nombre, Cursos, Modalidad_ID) VALUES (?, ?, ?)",
                            (curso.profesor, curso.nombre, modalidad_id))
        profesor_id = conn.cursor.lastrowid

    # Actualizar curso
    conn.cursor.execute("""
        UPDATE Cursos
        SET Nombre = ?, Profesor_ID = ?, Fecha = ?, Modalidad_ID = ?, Estado = ?
        WHERE ID = ?
    """, (curso.nombre, profesor_id, curso.fecha, modalidad_id, int(curso.estado), id))

    conn.cerrar_conexion()

# Elimina un curso según su ID. No elimina profesores ni modalidades asociadas.
def borrar_campos(id):
    conn = ConexionDB()
    
    sql = f"""
            DELETE FROM Cursos WHERE ID = {id};
    """
    
    conn.cursor.execute(sql)
    conn.cerrar_conexion()