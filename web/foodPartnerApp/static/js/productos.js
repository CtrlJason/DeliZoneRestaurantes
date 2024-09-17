function mostrarFormulario(productoId) {
    // Ocultar todos los formularios primero
    document.querySelectorAll('.formulario-edicion').forEach(form => form.style.display = 'none');
    
    // Mostrar el formulario correspondiente al producto
    document.getElementById('formulario-' + productoId).style.display = 'block';
}

function ocultarFormulario(productoId) {
    // Ocultar el formulario de edición del producto actual
    document.getElementById('formulario-' + productoId).style.display = 'none';
}