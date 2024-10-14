//--================ BOTONES MODULO - MENU NAVEGACION ================--//

// Carrito de compras
const mostrarCarritoBtn1 = document.getElementById('mostrarCarrito-1');
const mostrarCarritoBtn2 = document.getElementById('mostrarCarrito-2');
const mostrarVentanaCarrito = document.getElementById('mostrarVentanaCarrito');
const ocultarVentanaCarritoBtn = document.getElementById('ocultarVentanaCarrito');

// Funcion para mostrar y ocultar el carrito de compras
// Boton 1
mostrarCarritoBtn1.addEventListener('click', () => {
    mostrarVentanaCarrito.classList.toggle('mostrar-ventana-carrito');
})
// Boton 2
mostrarCarritoBtn2.addEventListener('click', () => {
    mostrarVentanaCarrito.classList.toggle('mostrar-ventana-carrito');
})

// Funcion para ocultar la ventana del carrito
ocultarVentanaCarritoBtn.addEventListener('click', () => {
    mostrarVentanaCarrito.classList.add('.ocultar-ventana-carrito');
    mostrarVentanaCarrito.classList.remove('mostrar-ventana-carrito');
})
// -------------------------------------------------------------------- //

const botonVentanaUsuarioNav1 = document.getElementById('botonVentanaUsuarioNav-1');
const botonVentanaUsuarioNav2 = document.getElementById('botonVentanaUsuarioNav-2');
const VentanaUsuarioNav1 = document.getElementById('VentanaUsuarioNav-1');
const VentanaUsuarioNav2 = document.getElementById('VentanaUsuarioNav-2');

botonVentanaUsuarioNav1.addEventListener('click', () => {
    VentanaUsuarioNav1.classList.toggle('mostrar-ventana-usuario');
})

botonVentanaUsuarioNav2.addEventListener('click', () => {
    VentanaUsuarioNav2.classList.toggle('mostrar-ventana-usuario');
})
//--==================================================================--//