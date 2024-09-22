const contadorCarrito = document.querySelector('.contador-productos');
let contador = 0;

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