main(){

  String correo;
  String mensaje;
  
  correo = "yeisondamosquera@gmail.com ";

  print(correo.contains("@"));
  print(correo.endsWith(".com"));

  mensaje = correo.contains("@") && correo.trim().contains(".com") ? "Esto es un correo electronico" : "No es un correo electronico";
  print(mensaje);
  print("EL correo tiene una longitud de ${correo.length}");
  //trim() elimina todos los espacios
  //Datos numericos

// int numero = -3;
// double decimal = 3.2;
// print("Estos son los datos numericos: numero $numero decimal $decimal");
  //Cadenas de texto
  /*Esto es un comentario*/
  /**
   * 
   * 
   *Esto 
   *es 
   *otro 
   *comentario
   *
   *
   */
  // String nombre = "Yeison";
  // print("Mi nombre es: $nombre");
  
  // //Buleanos
  // bool encendido = true;
  // bool apagado = false;
  // print("Los datos primitivos son: Encendido $encendido y Apagado $apagado");
  // //Datos dinamicos

  // var algo = 10.9;
  // dynamic variableDinamica = 3;
  // variableDinamica = "hola";
  // print("Variables: variable $algo - variable dinamica $variableDinamica");
}