from django.shortcuts import render, redirect
from firebase import db, storage
from .forms import PruebaForm

# Create your views here.

# En esta funcion creamos y luego obtenemos los datos y al final eliminamos un documento espesifico

def crud(request):
#     doc_ref = db.collection("empleados").document("7p6c1dINeG5FqRKT47Pz")
    
#     # for empleado in doc.to_dict():
#     #     empleados.append(empleado)
#     # Crear datos
#     # <------------------------------------------------>
#     doc_ref.set({
#         "nombre" : "Allan",
#         "apellido": "Gomez",
#         "numero de telefono": 3142880412,
#         "correo electronico": "gomelandiaroco@gmail.com"
#     })
#     # <------------------------------------------------>
    
#     # Leer datos
#     # <------------------------------------------------>
#     # Para obtener los datos de un documento usamos el metodo get()
#     doc = doc_ref.get()
#     # El metodo exist solo aparece al usar el metodo get() o delete()
#     if doc.exists:
#         # El metodo to_direct se usa para ver el contenido del documento
#         print(f"EL documento existe y tiene los siguientes datos: {doc.to_dict()}")
#         print(f"El id del documento es: {doc.id}")
#     else:
#         print("El documento no existe")
#     # <------------------------------------------------>
    
# #     # Eliminar datos
# #     # <------------------------------------------------>
# #     # Para eliminar un documento se usa el metodo delete
# #     doc = doc_ref.delete()
# #     doc = doc_ref.get()
    
# #     if doc.exists:
# #         print(f"EL documento existe y tiene los siguientes datos: {doc.to_dict()}")
# #         print(f"El id del documento es: {doc.id}")
# #     else:
# #         print("El documento no existe o fue eliminado")

#     # Actualizar datos
#     # <------------------------------------------------>
#     doc = doc_ref.update({
#         "nombre" : "nombre actualizado",
#         "apellido" : "apellido actualizado"
#     })
#     doc = doc_ref.get()
#     if doc.exists:
#         print(f"EL documento existe y tiene los siguientes datos: {doc.to_dict()}")
#         print(f"El id del documento es: {doc.id}")
#     else:
#         print("El documento no existe o fue eliminado")
    
        
    return render(request, "pruebas.html")

# En esta funcion obtenemos todos los documentos de la base de datos

def lista_documentos(request):
    # el metodo stream() obtiene todos los documentos como objetos
    documentos = db.collection("empleados").stream()
    empleados = []
    # el metodo to_dict() muestra el contenido del documento
    # si usamos stream debemos iterar la coleccion para ver los objetos y obtener su contenido con el metodo dict()
    for documento in documentos:
        empleados.append(documento.to_dict())
    # print(f"La cantidad de documentos creados es de {len(documentos)}") # Solo se puede usar len cuando usamos el metodo get() en la coleccion
    print(f"Empleados: {empleados}")
    return render(request, "pruebas.html")

# En esta funcion mostramos los documentos en el template
def mostrar_formulario(request):
    documentos = db.collection("empleados")
    formulario = PruebaForm(request.POST)
    if request.method == "POST":
        datos =({
            "nombre" : formulario["nombre"],
            "celular" : formulario["celular"],
            "correo" : formulario["correo"],
            "password" : formulario["password"],
        })
        
        documentos.add(datos)
    return render(request, "pruebas.html", {"formulario" : formulario})
