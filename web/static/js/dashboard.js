// -------------------- BOTONES MODULO - DASHBOARD -------------------- //
const botonCerrarDashboard = document.getElementById('botonCerrarDashboard');
const menuLateral = document.getElementById('menuLateral');
const iconoBoton = document.getElementById('iconoBoton');

botonCerrarDashboard.addEventListener('click', () => {
    menuLateral.classList.toggle('mostrar-ventana-dashboard');

    if (botonCerrarDashboard.style.left === '-20px' || botonCerrarDashboard.style.left === '') {
        botonCerrarDashboard.style.left = '260px';
        iconoBoton.style.transform = 'rotate(0deg)';
    } else {
        botonCerrarDashboard.style.left = '-20px';
        iconoBoton.style.transform = 'rotate(180deg)';
    }
});
// -------------------------------------------------------------------- //

const botonNotificacion = document.getElementById('botonNotificacion');
const botonUsuario = document.getElementById('botonUsuario');
const ventanaNotificacion = document.getElementById('ventanaNotificacion');
const ventanaUsuario = document.getElementById('ventanaUsuario');

botonNotificacion.addEventListener('click', () => {
    if (ventanaNotificacion.style.display === 'none') {
        ventanaNotificacion.style.display = 'block';
        ventanaUsuario.style.display = 'none';
    } else {
        ventanaNotificacion.style.display = 'none';
    }
});

botonUsuario.addEventListener('click', () => {
    if (ventanaUsuario.style.display === 'none') {
        ventanaUsuario.style.display = 'block';
        ventanaNotificacion.style.display = 'none';
    } else {
        ventanaUsuario.style.display = 'none';
    }
});