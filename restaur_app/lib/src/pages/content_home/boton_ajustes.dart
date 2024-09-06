import 'package:flutter/material.dart';
import '../ajustes.dart';

class BotonAjustes extends StatelessWidget {
  const BotonAjustes({super.key});

  @override
  Widget build(BuildContext context) {
    return IconButton(
      icon: const Icon(Icons.settings),
      onPressed: () {
        {
          Navigator.push(context,
              MaterialPageRoute(builder: (context) => const Ajustes()));
        }
      },
      style: const ButtonStyle(
        iconSize: WidgetStatePropertyAll(25),
        iconColor: WidgetStatePropertyAll(Colors.white),
        backgroundColor:
            WidgetStatePropertyAll(Color.fromARGB(255, 207, 87, 78)),
      ),
    );
  }
}
