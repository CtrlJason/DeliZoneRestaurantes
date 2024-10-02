lista_estuadiantes = ["juan", "carlos", "laura"]

diccionario_estudiantes = {
    1:{
        "nombre":"juan",
        "apellido":"gonazales",
        "materias": {
            "nombre": "matematicas"
        }
    },
    2:{
        "nombre":"laura",
        "apellido":"gonazales",
    },
}

print(diccionario_estudiantes[1]["materias"])