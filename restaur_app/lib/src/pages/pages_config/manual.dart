import "package:flutter/material.dart";

class Manual extends StatelessWidget {
  const Manual({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 100,
        title: const Text(
          "Manual",
          style: TextStyle(fontSize: 35),
        ),
      ),
      body: const Center(
          child: TextButton(
        onPressed: null,
        style: ButtonStyle(
          iconColor: WidgetStatePropertyAll(Colors.white),
          backgroundColor:
              WidgetStatePropertyAll(Color.fromARGB(255, 207, 87, 78)),
        ),
        child: Text(
          "Manual",
          style: TextStyle(color: Colors.white, fontSize: 25),
        ),
      )),
    );
  }
}

// funcion para abrir el pdf y hacerla privada
