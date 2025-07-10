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
            Apellido TEXT NOT NULL,
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

# Para precargar los valores de modalidades
# def precargar_modalidades():
#     conn = ConexionDB()
#     modalidades = ['Presencial', 'Virtual', 'Híbrido']
#     try:
#         for tipo in modalidades:
#             conn.cursor.execute("INSERT OR IGNORE INTO Modalidades (Tipo) VALUES (?)", (tipo,))
#         conn.cerrar_conexion()
#     except Exception as e:
#         print("Error al precargar modalidades:", e)


# def conectar_bd():
#     crear_tabla()
#     precargar_modalidades()
    
class Cursos:
    def __init__(self, nombre, profesor, fecha, modalidad, estado):
        self.nombre = nombre
        self.profesor = profesor
        self.fecha = fecha
        self.modalidad = modalidad
        self.estado = estado
    
    def __str__(self):
        return f'Cursos[{self.nomnbre}, {self.profesor},{self.fecha},{self.modalidad},{self.estado}]'
    
    def guardar_cursos(curso):
        conn = ConexionDB()
        
        sql = f"""
            INSERT INTO Cursos(Nombre, Profesor,Fecha, Modalidad, Estado)
            VALUES('{curso.nombre}','{curso.profesor}','{curso.fecha}',{curso.modalidad}, '{curso.estado});
        """
        
        conn.cursor.execute()
        conn.cerrar_conexion()
