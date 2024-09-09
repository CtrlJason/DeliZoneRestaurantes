import 'package:flutter/material.dart';
import 'botones_footer.dart';
import 'boton_ajustes.dart';

class PedEntregados extends StatefulWidget {
  const PedEntregados({super.key});

  @override
  State<PedEntregados> createState() => _PedEntregadosState();
}

class _PedEntregadosState extends State<PedEntregados> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 100,
        title: const Text(
          "Pedidos Entregados",
          style: TextStyle(fontSize: 35),
        ),
        actions: const [BotonAjustes()], // Boton de ajustes externo
      ),
      body: const Center(
        child: Text(
          "Pedidos Entregados",
          style: TextStyle(fontSize: 25),
        ),
      ),
      persistentFooterButtons: const [BotonesFooter()],
    );
  }
}
