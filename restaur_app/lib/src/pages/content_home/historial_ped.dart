import 'package:flutter/material.dart';
import 'boton_ajustes.dart';
import 'botones_footer.dart';

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
        actions: const [BotonAjustes()], // Boton de ajustes externo
      ),
      body: const Center(
        child: Text(
          "Bienvenido al historial",
          style: TextStyle(fontSize: 25),
        ),
      ),
      persistentFooterButtons: const [BotonesFooter()],
    );
  }
}
