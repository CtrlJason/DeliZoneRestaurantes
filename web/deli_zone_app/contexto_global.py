def excluir_paths_sitio(request):
    excluir_paths = [
        "/acceso/iniciar_sesion/",
        "/acceso/iniciar_sesion_admin/",
        "/acceso/registro/",
        "/carrito/",
        "/compra/",
        "/seleccionar_tienda/realizar_pago/",
        "/acceso/",
        "/seleccionar_tienda/",
        "/dashboard/",
        "/dashboard/admin/productos/",
        "/dashboard/admin/contacto/",
        "/dashboard/admin/configuracion/sitio/",
        "/dashboard/admin/usuarios/",
    ]
    return {"excluir_paths": excluir_paths}
