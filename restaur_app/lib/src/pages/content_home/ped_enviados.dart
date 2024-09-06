import 'package:flutter/material.dart';
import 'botones_footer.dart';
import 'boton_ajustes.dart';

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
        actions: const [BotonAjustes()], // Boton de ajustes externo
      ),
      body: const Center(
        child: Text(
          "Pedidos Enviados",
          style: TextStyle(fontSize: 25),
        ),
      ),
      persistentFooterButtons: const [BotonesFooter()],
    );
  }
}
