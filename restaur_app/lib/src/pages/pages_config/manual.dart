import "package:flutter/material.dart";
import 'package:flutter/services.dart' show rootBundle;
import 'package:path_provider/path_provider.dart';
import 'package:open_file/open_file.dart';
import 'dart:io';
import 'dart:typed_data';

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
        onPressed: _openLocalPDF,
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
Future<void> _openLocalPDF() async {
  // Obtén el directorio de documentos
  final directory = await getApplicationDocumentsDirectory();
  final filePath = '${directory.path}/manual.pdf';

  // Copia el archivo desde los assets al directorio de documentos
  final file = File(filePath);
  if (!await file.exists()) {
    final ByteData data = await rootBundle.load('assets/manual.pdf');
    final List<int> bytes = data.buffer.asUint8List();
    await file.writeAsBytes(bytes);
  }

  // Abre el archivo
  OpenFile.open(filePath);
}
