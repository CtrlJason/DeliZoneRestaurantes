import 'package:flutter/material.dart';

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
      ),
      body: const Center(
        child: Text(
          "Pedidos Entregados",
          style: TextStyle(fontSize: 25),
        ),
      ),
    );
  }
}
