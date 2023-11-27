# #funcion que se autoejecuta.
# hola=lambda a,b:print(a+b)
# #funcion normal:
# def suma(a,b):
#      print (a+b)
# suma(2,3)
# hola(20,20)

# # if ternario
# ternario="soy verdad ternario" if True else "soy falso ternario"
# print(ternario)

# # if normal
# if True:
#      print("holi")
# else:
#      print("soy mentira")

list_alumnos=[
    {
        'NOMBRE':'Edwin',
        'EDAD':19,
        'HOBBY':'danza'
    },

     {
        'NOMBRE':'Orlando',
        'EDAD':20,
        'HOBBY':'Canto'
    },

     {
        'NOMBRE':'Cristians',
        'EDAD':30,
        'HOBBY':'pintura'
    },

     {
        'NOMBRE':'Jhonatan',
        'EDAD':25,
        'HOBBY':'danza'
    },
     {
        'NOMBRE':'Antony',
        'EDAD':25,
        'HOBBY':'danza'
    }

]
# print(f" Todos los alumnos: {list_alumnos}")
# hobbies=list(filter(lambda par:par['HOBBY']=='danza',list_alumnos))
# edad=list(filter(lambda e:e['EDAD']> 20, list_alumnos))
# print(f" Los alumnos que tiene el hobbie de {hobbies}")
# print(f" Los alumnos que tiene mayor de {edad}")

nuevo=list(map(lambda par:{'Nombre_Alumno':par['NOMBRE'],'DANZA':par['HOBBY']},list_alumnos))
print(nuevo)


