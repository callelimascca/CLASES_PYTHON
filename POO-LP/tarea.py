tiendas=[
    {
        "Nombre": "Tienda 1",
        "RUC": "12335-35453",
        "Gerente": "Edwin",
        "Categoria": ["abarrotes","bodega"],
        "Horario_atencion":{
            "dia": "7 am - 12 m",
            "tarde": "2 pm - 8 pm"
        },

    },
    {
        "Nombre": "Tienda 2",
        "RUC": "12335-35453",
        "Gerente": "Edwin",
        "Categoria": ["abarrotes","farmacia"],
        "Horario_atencion":{
            "dia": "7 am - 12 m",
            "tarde": "2 pm - 8 pm"
        },

    },
    {
        "Nombre": "Tienda 3",
        "RUC": "12335-35453",
        "Gerente": "Nadine",
        "Categoria": ["abarrotes","bodega"],
        "Horario_atencion":{
            "dia": "7 am - 12 m",
            "tarde": "2 pm - 8 pm"
        },

    },
    {
        "Nombre": "Tienda 4",
        "RUC": "12335-3534",
        "Gerente": "Cristian",
        "Categoria": ["farmacia", "abarrotes"],
        "Horario_atencion":{
            "dia": "7 am - 12 m",
            "tarde": "2 pm - 8 pm"
        },

    },
    {
        "Nombre": "Tienda 5",
        "RUC": "12335-35453",
        "Gerente": "China",
        "Categoria": ["farmacia","abarrotes"],
        "Horario_atencion":{
            "dia": "7 am - 12 m",
            "tarde": "2 pm - 8 pm"
        },

    },
    {
        "Nombre": "Tienda 6",
        "RUC": "1235-37653",
        "Gerente": "Nadinde",
        "Categoria": ["abarrotes","bodega"],
        "Horario_atencion":{
            "dia": "7 am - 12 m",
            "tarde": "2 pm - 8 pm"
        },

    },
    {
        "Nombre": "Tienda 7",
        "RUC": "12335-35453",
        "Gerente": "Edwin",
        "Categoria": ["abarrotes","bodega"],
        "Horario_atencion":{
            "dia": "7 am - 12 m",
            "tarde": "2 pm - 8 pm"
        },

    },
    {
        "Nombre": "Tienda 8",
        "RUC": "12335-38753",
        "Gerente": "China",
        "Categoria": ["bodega","farmacia"],
        "Horario_atencion":{
            "dia": "7 am - 12 m",
            "tarde": "2 pm - 8 pm"
        },

    },
    {
        "Nombre": "Tienda 9",
        "RUC": "12335-35454",
        "Gerente": "China",
        "Categoria": ["abarrotes","bodega"],
        "Horario_atencion":{
            "dia": "7 am - 12 m",
            "tarde": "2 pm - 8 pm"
        },

    },
    {
        "Nombre": "Tienda 10",
        "RUC": "12335-35453",
        "Gerente": "Cristian",
        "Categoria": ["abarrotes","bodega","farmacia"],
        "Horario_atencion":{
            "dia": "7 am - 12 m",
            "tarde": "2 pm - 8 pm"
        },

    }
]

class Tienda:
           
    def __init__(self,nombre,ruc,gerente,categoria,horario_atencion="dia: 7 am - 12 m,tarde: 2 pm - 8 pm"):
        self.nombre=nombre
        self.ruc=ruc
        self.gerente=gerente
        self.categoria=categoria
        self.horario_atencion=horario_atencion
