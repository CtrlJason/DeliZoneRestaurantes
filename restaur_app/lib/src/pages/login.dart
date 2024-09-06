import "package:flutter/material.dart";
import "package:flutter/services.dart";
import "package:restaur_app/src/pages/home.dart";
import './extra/derechos.dart';

class Login extends StatefulWidget {
  const Login({super.key});

  @override
  State<Login> createState() => _LoginState();
}

class _LoginState extends State<Login> {
  TextEditingController cedula = TextEditingController();
  TextEditingController password = TextEditingController();
  bool isButtonEnabled = false;

  void initState() {
    super.initState();
    // Escuchamos los cambios en los controladores
    cedula.addListener(_checkFields);
    password.addListener(_checkFields);
  }

  void _checkFields() {
    // Habilitar o deshabilitar el botón
    setState(() {
      isButtonEnabled = cedula.text.isNotEmpty && password.text.isNotEmpty;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        child: Center(
          child: Column(
            children: [
              Expanded(
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
                      margin:
                          const EdgeInsets.only(top: 40, left: 50, right: 50),
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
                            keyboardType: TextInputType.number,
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
                          // Boton de inicio de sesion
                          TextButton(
                            onPressed: isButtonEnabled // Condicional
                                ? () {
                                    Navigator.pushReplacement(
                                        context,
                                        MaterialPageRoute(
                                            builder: (context) =>
                                                const HomeScreen()));
                                  }
                                : null,
                            style: TextButton.styleFrom(
                              foregroundColor: Colors.black,
                              iconColor: Colors.white,
                              padding: const EdgeInsets.only(right: 50),
                              backgroundColor: Colors.red,
                              shape: RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(20),
                              ),
                            ),
                            child: const Row(
                              mainAxisSize: MainAxisSize.min,
                              children: [
                                Icon(
                                  Icons.arrow_circle_left,
                                  size: 40,
                                ),
                                SizedBox(width: 24),
                                Text(
                                  'Login',
                                  style: TextStyle(fontSize: 20),
                                ),
                              ],
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
              const Derechos(),
            ],
          ),
        ),
      ),
    );
  }
}
