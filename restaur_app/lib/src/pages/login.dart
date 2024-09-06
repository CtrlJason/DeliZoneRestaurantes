import "package:flutter/material.dart";
import "package:flutter/services.dart";
import "package:restaur_app/src/pages/home.dart";

class Login extends StatefulWidget {
  const Login({super.key});

  @override
  State<Login> createState() => _LoginState();
}

class _LoginState extends State<Login> {
  TextEditingController cedula = TextEditingController();
  TextEditingController password = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              // Titulo del login
              const Text(
                "Iniciar Sesion",
                style: TextStyle(fontSize: 35),
              ),
              Container(
                  // Inputs de login
                  margin: const EdgeInsets.only(top: 40, left: 50, right: 50),
                  child: Column(
                    children: [
                      // Input numero de cedula
                      TextField(
                        controller: cedula,
                        decoration: const InputDecoration(
                          hintText: "Numero de Cedula",
                          hintStyle: TextStyle(fontSize: 20),
                          enabledBorder: OutlineInputBorder(
                              borderRadius:
                                  BorderRadius.all(Radius.circular(15)),
                              borderSide: BorderSide(color: Colors.black)),
                          focusedBorder: OutlineInputBorder(
                              borderRadius:
                                  BorderRadius.all(Radius.circular(15)),
                              borderSide: BorderSide(color: Colors.red)),
                        ),
                        maxLength: 15,
                        keyboardType: TextInputType
                            .number, // Convierte el teclado a numerico
                        // Elimina todo lo que no sea texto
                        inputFormatters: <TextInputFormatter>[
                          FilteringTextInputFormatter.digitsOnly,
                        ],
                      ),
                      // Input contraseña
                      TextField(
                        controller: password,
                        obscureText: true,
                        decoration: const InputDecoration(
                          hintText: "Contraseña",
                          hintStyle: TextStyle(fontSize: 20),
                          enabledBorder: OutlineInputBorder(
                              borderRadius:
                                  BorderRadius.all(Radius.circular(15)),
                              borderSide: BorderSide(color: Colors.black)),
                          focusedBorder: OutlineInputBorder(
                              borderRadius:
                                  BorderRadius.all(Radius.circular(15)),
                              borderSide: BorderSide(color: Colors.red)),
                        ),
                      ),
                      // Boton de login
                      const SizedBox(
                        height: 40,
                      ),
                      TextButton(
                        onPressed: () {
                          Navigator.pushReplacement(
                              context,
                              MaterialPageRoute(
                                  builder: (context) => const HomeScreen()));
                        },
                        style: TextButton.styleFrom(
                          foregroundColor: Colors.black,
                          iconColor: Colors.white, // Color del texto e ícono
                          padding: const EdgeInsets.only(right: 50), // Padding
                          backgroundColor: Colors.red,
                          shape: RoundedRectangleBorder(
                            borderRadius:
                                BorderRadius.circular(20), // Bordes redondeados
                          ),
                        ),
                        child: const Row(
                          mainAxisSize:
                              MainAxisSize.min, // Ajusta el tamaño al contenido
                          children: [
                            Icon(
                              Icons.arrow_circle_left,
                              size: 40,
                            ), // Ícono
                            SizedBox(
                                width: 24), // Espacio entre el ícono y el texto
                            Text(
                              'Login',
                              style: TextStyle(fontSize: 20),
                            ), // Texto
                          ],
                        ),
                      ),
                    ],
                  )),
            ],
          ),
        ),
      ),
    );
  }
}
