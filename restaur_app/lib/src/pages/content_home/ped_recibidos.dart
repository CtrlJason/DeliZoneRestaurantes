import 'package:flutter/material.dart';

class PedRecibidos extends StatefulWidget {
  const PedRecibidos({super.key});

  @override
  State<PedRecibidos> createState() => _PedRecibidosState();
}

class _PedRecibidosState extends State<PedRecibidos> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 100,
        title: const Text(
          "Pedidos Recibidos",
          style: TextStyle(fontSize: 35),
        ),
      ),
      body: const Center(
        child: Text(
          "Pedidos Recibidos",
          style: TextStyle(fontSize: 25),
        ),
      ),
    );
  }
}
