import "package:flutter/material.dart";
import 'package:syncfusion_flutter_pdfviewer/pdfviewer.dart'; // Paquete para visualizar pdfs

class Manual extends StatelessWidget {
  const Manual({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 100,
        title: const Text(
          "Manual de usuario",
          style: TextStyle(fontSize: 30),
        ),
      ),
      // Manual de usuario
      body: SfPdfViewer.asset("assets/documents/manual.pdf"),
    );
  }
}
