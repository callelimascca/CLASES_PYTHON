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

def insertarAlumno(nombre,edad):
    conn=connect("./base_datos/tecnologico.db")
    cursor=conn.cursor()
    sentencia=f"INSERT INTO Alumnos(nombre,edad) VALUES ('{nombre}',{edad})"
    cursor.execute(sentencia)
    conn.commit()
    conn.close()
if __name__=="__main__":
    # # crearTablaAlumnos()
    # crearTablaCursos()
    insertarAlumno('Jory', 20)
    insertarAlumno('China', 20)

def insertAlumno(lista):
    conn=connect("./base_datos/tecnologico.db")
    cursor=conn.cursor()
    sentencia=f"INSERT INTO Alumnos(nombre,edad) VALUES (?,?)"
    cursor.executemany(sentencia,lista)
    conn.commit()
    conn.close()

def actualizarAlumno(id_alumno, nuevo_nombre, nueva_edad):
    conn = connect("./Base_datos/tecnologico.db")
    cursor = conn.cursor()

 
    sentencia = f"UPDATE Alumnos SET nombre = ?, edad = ? WHERE id = ?"
    data = (nuevo_nombre, nueva_edad, id_alumno)

    cursor.execute(sentencia, data)
    conn.commit()
    conn.close()

def eliminarAlumnoPorID(id_alumno):
    conn = connect("./Base_datos/tecnologico.db")
    cursor = conn.cursor()


    sentencia = "DELETE FROM Alumnos WHERE id = ?"
    data = (id_alumno,)

    cursor.execute(sentencia, data)
    conn.commit()
    conn.close()

if __name__=="__main__":
    # crearConexion()
    # crearTablaAlumno()
    # crearTablaCurso()
    # insertarAlumno("jory",20)
    # insertarAlumno("chinita",12)
    # alum=[
    #     ("jorycha",50),
    #     ("chinita",60),
    #     ("nidincita",18),
    #     ("viuda negra",300)
    # ]
    # insertAlumnos(alum)
    # id_alumno_a_actualizar = 1  
    # nuevo_nombre = "Nuevo Nombre"
    # nueva_edad = 25

    # actualizarAlumno(id_alumno_a_actualizar, nuevo_nombre, nueva_edad)
    id_alumno_a_eliminar = 25 

    eliminarAlumnoPorID(id_alumno_a_eliminar)
