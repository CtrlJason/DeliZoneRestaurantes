import "package:flutter/material.dart";

class Manual extends StatelessWidget {
  const Manual({super.key});

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
      body: Text("Contenido del manual"),
    );
  }
}
