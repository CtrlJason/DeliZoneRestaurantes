import "package:flutter/material.dart";
import './src/pages/login.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: "Restaur App",
      home: Login(),
    );
  }
}
