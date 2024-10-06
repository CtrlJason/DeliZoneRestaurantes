from firebase import db

class UsuarioAdministrador():
    
    # imagen
    def imagen_admin():
        docs = db.collection('restaurante1').document('usuarios').collection('administradores').stream()
        administrador = []
        for doc in docs:
            usuarios_data = (doc.to_dict())
            usuarios_data['id'] = doc.id
            administrador.append(usuarios_data)
            imagen_administrador = administrador[0]['imagen']
        return imagen_administrador