def estado_login(request):
    if "clientes_id" in request.session:
        print("Sesión iniciada")
        login = True
    else:
        print("Sesión no iniciada")
        login = False
    return login
