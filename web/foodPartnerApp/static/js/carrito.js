const btnCarrito = document.getElementById('btnCarrito');
const modalCarrito = document.getElementById('modalCarrito');
const span = document.getElementsByClassName("close")[0];
const contadorCarrito = document.querySelector('.contador-productos');
let contador = 0;

// Función para abrir/cerrar el carrito
function toggleCarrito() {
    const displayStyle = window.getComputedStyle(modalCarrito).display;
    if (displayStyle == "none") {
        modalCarrito.style.display = "block";
    } else {
        modalCarrito.style.display = "none";
    }
}

// Evento para el botón que abre/cierra el carrito
btnCarrito.onclick = toggleCarrito;

// Evento para cerrar el carrito con la 'x'
span.onclick = function () {
    modalCarrito.style.display = "none";
}

// Evento para abrir/cerrar el carrito cuando se haga clic en el número del contador
document.querySelector('.contador-productos').onclick = toggleCarrito;

// Selecciona todos los botones con la clase 'bttn'
const botones = document.querySelectorAll('.bttn.incrementar');

// Itera sobre cada botón y le agrega un evento 'click'
botones.forEach((boton) => {
    boton.onclick = function () {
        contador++;
        contadorCarrito.textContent = contador;

        if (contador >= 10) {
            // Modifica el tamaño del texto cuando el contador es mayor o igual a 10
            contadorCarrito.style.fontSize = "10px";
        }
    };
});