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
          "Actualizaciones",
          style: TextStyle(fontSize: 35),
        ),
      ),
      body: const Center(
        child: Text(
          "Mostrar Actualizaciones",
          style: TextStyle(fontSize: 25),
        ),
      ),
    );
  }
}
