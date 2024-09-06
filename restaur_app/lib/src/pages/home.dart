import "package:flutter/material.dart";
import 'content_home/botones_footer.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
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
        child: Text("Pedidos de la app"),
      ),
      backgroundColor: const Color.fromRGBO(253, 240, 213, 1),
      persistentFooterButtons: [BotonesFooter()],
    );
  }
}
