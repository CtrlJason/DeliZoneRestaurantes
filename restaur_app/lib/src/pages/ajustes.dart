import "package:flutter/material.dart";
import "package:restaur_app/src/pages/login.dart";
import './pages_config/notificaciones.dart';
import './pages_config/manual.dart';
import './pages_config/actualizaciones.dart';

class Ajustes extends StatelessWidget {
  const Ajustes({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 100,
        title: const Text(
          "Ajustes",
          style: TextStyle(fontSize: 20),
        ),
      ),
      body: Container(
        child: Center(
          child: Container(
              padding: const EdgeInsets.only(bottom: 100),
              child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    // Boton Notificaciones
                    TextButton(
                      onPressed: () {
                        {
                          Navigator.push(
                              context,
                              MaterialPageRoute(
                                  builder: (context) =>
                                      const Notificaciones()));
                        }
                      },
                      style: TextButton.styleFrom(
                        foregroundColor: Colors.black,
                        iconColor:
                            Colors.red, // Color del texto e ícono// Padding
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
                            'Notificaciones',
                            textScaler: TextScaler.linear(1.7),
                          ), // Texto
                        ],
                      ),
                    ),
                    const SizedBox(height: 60.0),
                    // Boton del Manual
                    TextButton(
                      onPressed: () {
                        {
                          Navigator.push(
                              context,
                              MaterialPageRoute(
                                  builder: (context) => const Manual()));
                        }
                      },
                      style: TextButton.styleFrom(
                        foregroundColor: Colors.black,
                        iconColor:
                            Colors.red, // Color del texto e ícono // Padding
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
                            'Manual',
                            textScaler: TextScaler.linear(1.7),
                          ), // Texto
                        ],
                      ),
                    ),
                    const SizedBox(height: 60.0),
                    // Boton Actualizaciones
                    TextButton(
                      onPressed: () {
                        {
                          Navigator.push(
                              context,
                              MaterialPageRoute(
                                  builder: (context) =>
                                      const Actualizaciones()));
                        }
                      },
                      style: TextButton.styleFrom(
                        foregroundColor: Colors.black,
                        iconColor:
                            Colors.red, // Color del texto e ícono // Padding
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
                            'Actualizaciones',
                            textScaler: TextScaler.linear(1.7),
                          ), // Texto
                        ],
                      ),
                    ),
                    const SizedBox(height: 60.0),
                    // Boton, Salir
                    TextButton(
                      onPressed: () {
                        Navigator.pushAndRemoveUntil(
                          context,
                          MaterialPageRoute(
                              builder: (context) => const Login()),
                          (Route<dynamic> route) =>
                              false, // Elimina todas las rutas anteriores
                        );
                      },
                      style: TextButton.styleFrom(
                        foregroundColor: Colors.black,
                        iconColor:
                            Colors.red, // Color del texto e ícono // Padding
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
                            'Salir',
                            textScaler: TextScaler.linear(1.7),
                          ), // Texto
                        ],
                      ),
                    ),
                  ])),
        ),
      ),
    );
  }
}
