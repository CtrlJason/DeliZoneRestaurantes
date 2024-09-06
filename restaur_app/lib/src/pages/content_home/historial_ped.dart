import 'package:flutter/material.dart';

class HistorialPed extends StatefulWidget {
  const HistorialPed({super.key});

  @override
  State<HistorialPed> createState() => _HistorialPedState();
}

class _HistorialPedState extends State<HistorialPed> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 100,
        title: const Text(
          "Historial",
          style: TextStyle(fontSize: 35),
        ),
      ),
      body: const Center(
        child: Text(
          "Bienvenido al historial",
          style: TextStyle(fontSize: 25),
        ),
      ),
    );
  }
}
