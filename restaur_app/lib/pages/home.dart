import "package:flutter/material.dart";
import 'content/ped_recibidos.dart';
import 'extra/derechos.dart';

class HomeScreen extends StatefulWidget {
  // Creacion del constructor (opcional)
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Expanded(
            child: Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Text(
                    "Restaur App",
                    style: TextStyle(
                        fontSize: 40,
                        color: Colors.redAccent,
                        fontWeight: FontWeight.bold),
                  ),
                  const SizedBox(
                    height: 20,
                  ),
                  TextButton(
                    onPressed: () {
                      Navigator.pushReplacement(
                        context,
                        MaterialPageRoute(
                          builder: (context) => const PedRecibidos(),
                        ),
                      );
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
                          'Entrar',
                          style: TextStyle(fontSize: 20),
                        ), // Texto
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ),
          const Derechos(), // Aquí agregamos el widget de "Derechos reservados"
        ],
      ),
    );
  }
}
