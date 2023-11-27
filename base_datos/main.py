from sqlite3 import *
def crearConexion():
    conn = connect("./base_datos/tecnologico.db")
    conn.commit()
    conn.close()

def crearTablaAlumnos():
    conn=connect("./base_datos/tecnologico.db")
    cursor=conn.cursor()
    sentencia="""
        CREATE TABLE IF NOT EXISTS Alumnos(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT(250), edad INTEGER
        )
    """
    cursor.execute(sentencia)
    conn.commit()
    conn.close()
if __name__=="__main__":
    # crearConexion()
    crearTablaAlumnos()

def crearTablaCursos():
    conn=connect("./base_datos/tecnologico.db")
    cursor=conn.cursor()
    sentencia="""
        CREATE TABLE IF NOT EXISTS Cursos(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT(250), id_alumno INTEGER, 
            FOREIGN KEY(id_alumno) REFERENCES Alumnos(id)
        )
    """
    cursor.execute(sentencia)
    conn.commit()
    conn.close()
if __name__=="__main__":
    # crearTablaAlumnos()
    crearTablaCursos()

def insertAlumno(nombre,edad):
    conn=connect("./base_datos/tecnologico.db")
    cursor=conn.cursor()
    sentencia=f"INSERT INTO Alumnos(nombre,edad) VALUES ('{nombre}',{edad})"
    cursor.execute(sentencia)
    conn.commit()
    conn.close()
if __name__=="__main__":
    # # crearTablaAlumnos()
    # crearTablaCursos()
    insertAlumno('Jory', 20)
    insertAlumno('China', 20)
def insertAlumno(nombre,edad):
    conn=connect("./base_datos/tecnologico.db")
    cursor=conn.cursor()
    sentencia=f"INSERT INTO Alumnos(nombre,edad) VALUES (?,?)"
    cursor.executemany(sentencia,lista)
    conn.commit()
    conn.close()
if __name__=="__main__":
    # crearTablaAlumnos()
    # crearTablaCursos()
    # insertAlumno('Jory', 20)
    # insertAlumno('China', 20)
    alum=[
        ('jory',50)
        ('china',19)
        ('nadine',18)
        ('mochi',23)
    ]
    insertAlumno(alum)
