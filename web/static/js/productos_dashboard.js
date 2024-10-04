const verProductosBtn = document.getElementById('btn-ver-productos')
const agregarProductosBtn = document.getElementById('btn-agregar-productos')
const tiendaProductos = document.getElementById('ver-productos')
const formularioProductos = document.getElementById('ver-formulario')

verProductosBtn.addEventListener('click', () => {
    tiendaProductos.style.display = 'flex'
    formularioProductos.style.display = 'none'
})

agregarProductosBtn.addEventListener('click', () => {
    tiendaProductos.style.display = 'none'
    formularioProductos.style.display = 'flex'
})