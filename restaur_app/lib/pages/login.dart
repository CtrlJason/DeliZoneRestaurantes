import 'package:firebase_auth/firebase_auth.dart';
import "package:flutter/material.dart";
import "package:restaur_app/pages/home.dart";
import 'extra/derechos.dart';
import 'package:restaur_app/utils/auth_service.dart';

AuthService authService = AuthService();

class Login extends StatefulWidget {
  const Login({super.key});

  @override
  State<Login> createState() => _LoginState();
}

class _LoginState extends State<Login> {
  final _formKey = GlobalKey<FormState>();
  TextEditingController correo = TextEditingController();
  TextEditingController password = TextEditingController();
  bool isButtonEnabled = false;

  @override
  void initState() {
    super.initState();
    // Escuchamos los cambios en los controladores
    correo.addListener(_checkFields);
    password.addListener(_checkFields);
  }

  void _checkFields() {
    // Habilitar o deshabilitar el botón
    setState(() {
      isButtonEnabled = correo.text.isNotEmpty && password.text.isNotEmpty;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color.fromRGBO(235, 77, 75, 1),
      body: Center(
        child: Form(
          key: _formKey,
          child: Column(
            children: [
              Expanded(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    // Titulo del login
                    const Text(
                      "Iniciar Sesion",
                      style: TextStyle(
                          fontSize: 35,
                          fontWeight: FontWeight.w600,
                          color: Colors.white),
                    ),
                    Container(
                      // Inputs de login
                      margin:
                          const EdgeInsets.only(top: 40, left: 50, right: 50),
                      child: Column(
                        children: [
                          // Integracion de los inputs
                          _textFieldCorreo(),
                          const SizedBox(height: 20),
                          _textFieldPassword(),
                          // Boton de login
                          const SizedBox(height: 40),
                          // Boton de inicio de sesion
                          TextButton(
                            onPressed: isButtonEnabled
                                ? () async {
                                    if (_formKey.currentState!.validate()) {
                                      showDialog(
                                        context: context,
                                        barrierDismissible: false,
                                        builder: (context) => const Center(
                                            child: CircularProgressIndicator()),
                                      );

                                      User? user = await authService
                                          .signInWithEmailAndPassword(
                                        correo.text,
                                        password.text,
                                      );

                                      Navigator.of(context)
                                          .pop(); // Cerrar el indicador de carga

                                      if (user != null) {
                                        Navigator.pushReplacement(
                                          context,
                                          MaterialPageRoute(
                                            builder: (context) =>
                                                const HomeScreen(),
                                          ),
                                        );
                                        // Limpiar campos
                                        correo.clear();
                                        password.clear();
                                      } else {
                                        // Mostrar mensaje de error
                                        ScaffoldMessenger.of(context)
                                            .showSnackBar(
                                          const SnackBar(
                                              content: Text(
                                                  'Inicio de sesión fallido. Verifica tus credenciales.')),
                                        );
                                      }
                                    }
                                  }
                                : null,
                            style: TextButton.styleFrom(
                              foregroundColor: Colors.red,
                              iconColor: const Color.fromRGBO(235, 77, 75, 1),
                              padding: const EdgeInsets.only(right: 50),
                              backgroundColor: Colors.white,
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

  // Creacion de los inputs del usuario
  // Input correo electronico
  Widget _textFieldCorreo() {
    return Container(
      decoration: const BoxDecoration(
        color: Color.fromARGB(255, 245, 245, 245),
        borderRadius: BorderRadius.all(Radius.circular(15)),
      ),
      child: TextFormField(
        controller: correo,
        decoration: const InputDecoration(
          contentPadding: EdgeInsets.only(left: 15),
          suffixIcon: Icon(Icons.email),
          labelText: "Correo electronico",
          labelStyle: TextStyle(
              color: Colors.black,
              fontSize: 20,
              backgroundColor: Colors.white24),
          hintText: "nombre@email.com",
          hintStyle: TextStyle(fontSize: 20),
          enabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.all(Radius.circular(15)),
              borderSide: BorderSide(color: Colors.black)),
          focusedBorder: OutlineInputBorder(
              borderRadius: BorderRadius.all(Radius.circular(15))),
        ),
        keyboardType: TextInputType.emailAddress,
        validator: (value) {
          if (value == null || value.isEmpty) {
            return 'Por favor ingresa un correo electrónico';
          }
          final emailRegex = RegExp(r'^[^@]+@[^@]+\.[^@]+');
          if (!emailRegex.hasMatch(value)) {
            return 'Por favor ingresa un correo electrónico válido';
          }
          return null;
        },
      ),
    );
  }

  // Input contraseña
  Widget _textFieldPassword() {
    return Container(
      decoration: const BoxDecoration(
        color: Color.fromARGB(255, 245, 245, 245),
        borderRadius: BorderRadius.all(Radius.circular(15)),
      ),
      child: TextFormField(
        controller: password,
        obscureText: true,
        decoration: const InputDecoration(
          contentPadding: EdgeInsets.only(left: 15),
          suffixIcon: Icon(Icons.lock),
          labelText: "Contraseña",
          labelStyle: TextStyle(
              color: Colors.black,
              fontSize: 20,
              backgroundColor: Colors.white24),
          hintText: "acb123456@",
          hintStyle: TextStyle(fontSize: 20),
          enabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.all(Radius.circular(15)),
              borderSide: BorderSide(color: Colors.black)),
          focusedBorder: OutlineInputBorder(
              borderRadius: BorderRadius.all(Radius.circular(15))),
        ),
      ),
    );
  }
}
