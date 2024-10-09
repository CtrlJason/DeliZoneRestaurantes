def estado_login_usuario(request):
    if "clientes_id" in request.session:
        print("Sesión iniciada")
        return {'verificar_login_usuario': True}
    else:
        print("Sesión no iniciada")
        return {'verificar_login_usuario': False}
