const contadorCarrito1 = document.querySelector('#contador-1');
const contadorCarrito2 = document.querySelector('#contador-2');
let contador = 0;

// Selecciona todos los botones con la clase 'bttn'
const botones = document.querySelectorAll('.bttn.incrementar');

// Itera sobre cada botón y le agrega un evento 'click'
botones.forEach((boton) => {
    boton.onclick = function () {
        contador++;
        contadorCarrito1.textContent = contador;
        contadorCarrito2.textContent = contador;

        if (contador >= 10) {
            // Modifica el tamaño del texto cuando el contador es mayor o igual a 10
            contadorCarrito1.style.fontSize = "10px";
            contadorCarrito2.style.fontSize = "10px";
        }
    };
});