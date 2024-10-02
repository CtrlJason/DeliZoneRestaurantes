// ----------------- BOTONES MODULO - COMPRA - TIENDA ----------------- //
const mostrarDireccionBtn = document.getElementById('mostrarDireccion');
const mostrarMapaBtn = document.getElementById('mostrarMapa');
const formularioDireccion = document.getElementById('formularioDireccion');
const mapa = document.querySelector('.mapa');

// Función para mostrar el formulario de dirección
mostrarDireccionBtn.addEventListener('click', () => {
    formularioDireccion.style.display = 'block'; // Mostrar formulario
    mapa.style.display = 'none';                 // Ocultar mapa
});

// Función para mostrar el mapa
mostrarMapaBtn.addEventListener('click', () => {
    mapa.style.display = 'block';                // Mostrar mapa
    formularioDireccion.style.display = 'none';  // Ocultar formulario
});
// -------------------------------------------------------------------- //