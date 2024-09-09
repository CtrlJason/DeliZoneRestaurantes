import 'package:cloud_firestore/cloud_firestore.dart';

// Instanciamos la base de datos de Firebase
FirebaseFirestore db = FirebaseFirestore.instance;

// Funcion que trae la informacion de la base de datos
Future<List> getEmpleados() async {
  List empleados = [];

  CollectionReference referenciaEmpleados = db.collection("empleado");

  QuerySnapshot queryEmpleados = await referenciaEmpleados
      .get(); // Esto nos trae toda la informacion del documento

  for (var documento in queryEmpleados.docs) {
    empleados.add(documento.data()); // Agregamos la data del documento
  }

  return empleados;
}
