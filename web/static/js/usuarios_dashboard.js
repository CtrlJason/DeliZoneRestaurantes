const BtnVerUsuarios = document.getElementById("boton-ver-usuarios")
const BtnRegistroEmpleado = document.getElementById("boton-registro-empleado")
const BtnRegistroAdministrador = document.getElementById("boton-registro-administrador")
const VerUsuarios = document.getElementById("ver-usuarios")
const RegistroEmpleado = document.getElementById("registro-empleado")
const RegistroAdministrador = document.getElementById("registro-administrador")

BtnVerUsuarios.addEventListener('click', () => {
    VerUsuarios.style.display = "block"
    RegistroEmpleado.style.display = "none"
    RegistroAdministrador.style.display = "none"
})

BtnRegistroEmpleado.addEventListener('click', () => {
    VerUsuarios.style.display = "none"
    RegistroEmpleado.style.display = "flex"
    RegistroAdministrador.style.display = "none"
})

BtnRegistroAdministrador.addEventListener('click', () => {
    VerUsuarios.style.display = "none"
    RegistroEmpleado.style.display = "none"
    RegistroAdministrador.style.display = "flex"
})