import "package:flutter/material.dart";

class Notificaciones extends StatefulWidget {
  const Notificaciones({super.key});

  @override
  State<Notificaciones> createState() => _NotificacionesState();
}

class _NotificacionesState extends State<Notificaciones> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 100,
        title: const Text(
          "Notificaciones",
          style: TextStyle(fontSize: 35),
        ),
      ),
      body: const Center(
        child: Text(
          "Configurar Notificaciones",
          style: TextStyle(fontSize: 25),
        ),
      ),
    );
  }
}
