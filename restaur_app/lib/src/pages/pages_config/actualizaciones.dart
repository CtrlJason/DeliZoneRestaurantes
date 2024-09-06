import "package:flutter/material.dart";

class Actualizaciones extends StatefulWidget {
  const Actualizaciones({super.key});

  @override
  State<Actualizaciones> createState() => _ActualizacionesState();
}

class _ActualizacionesState extends State<Actualizaciones> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 100,
        title: const Text(
          "Notificaciones",
          style: TextStyle(fontSize: 20),
        ),
      ),
      body: Text("Contenido de las actualizaciones"),
    );
  }
}
