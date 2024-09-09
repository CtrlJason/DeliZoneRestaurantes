import 'package:flutter_local_notifications/flutter_local_notifications.dart';

// Inicializar el plugin
final FlutterLocalNotificationsPlugin flutterLocalNotificationsPlugin =
    FlutterLocalNotificationsPlugin();

Future<void> initNotifications() async {
  const AndroidInitializationSettings initializationSettingsAndroid =
      AndroidInitializationSettings("icono_notificacion");

  const DarwinInitializationSettings initializationSettingsIOS =
      DarwinInitializationSettings();

  const InitializationSettings initializationSettings = InitializationSettings(
    android: initializationSettingsAndroid,
    iOS: initializationSettingsIOS,
  );

  await flutterLocalNotificationsPlugin.initialize(initializationSettings);
}

Future<void> mostrarNotificaciones() async {
  const AndroidNotificationDetails androidNotificationDetails =
      AndroidNotificationDetails("your channel Id", "your channel Name");

  const NotificationDetails notificationDetails = NotificationDetails(
    android: androidNotificationDetails,
  );

  await flutterLocalNotificationsPlugin.show(
      1,
      "Se ha realizado un nuevo pedido",
      "Notificacion de prueba",
      notificationDetails);
}
