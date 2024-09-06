import 'package:flutter/material.dart';

class PedEnviados extends StatefulWidget {
  const PedEnviados({super.key});

  @override
  State<PedEnviados> createState() => _PedEnviadosState();
}

class _PedEnviadosState extends State<PedEnviados> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 100,
        title: const Text(
          "Pedidos Enviados",
          style: TextStyle(fontSize: 35),
        ),
      ),
      body: const Center(
        child: Text(
          "Pedidos Enviados",
          style: TextStyle(fontSize: 25),
        ),
      ),
    );
  }
}
