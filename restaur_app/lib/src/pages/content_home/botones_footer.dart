import 'package:flutter/material.dart';
import './ped_recibidos.dart';
import './ped_enviados.dart';
import './ped_entregados.dart';
import './historial_ped.dart';

class BotonesFooter extends StatelessWidget {
  const BotonesFooter({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          // Boton de pedidos recibidos
          _buildIconButton(
              icon: Icons.notifications,
              context: context,
              route: PedRecibidos()),
          // Boton de pedidos enviados
          const SizedBox(width: 20),
          _buildIconButton(
              icon: Icons.two_wheeler, context: context, route: PedEnviados()),
          // Boton de pedidos entregados
          const SizedBox(width: 20),
          _buildIconButton(
              icon: Icons.how_to_reg, context: context, route: PedEntregados()),
          // Boton del historial
          const SizedBox(width: 20),
          _buildIconButton(
            icon: Icons.history,
            context: context,
            route: HistorialPed(),
          ),
        ],
      ),
    );
  }

  Widget _buildIconButton({
    required IconData icon,
    required BuildContext context,
    required Widget route,
  }) {
    return IconButton(
      icon: Icon(icon),
      onPressed: () {
        Navigator.push(context, MaterialPageRoute(builder: (context) => route));
      },
      style: const ButtonStyle(
        iconColor: WidgetStatePropertyAll(Colors.white),
        shape: WidgetStatePropertyAll(RoundedRectangleBorder(
            borderRadius: BorderRadius.horizontal(
                left: Radius.circular(20), right: Radius.circular(20)))),
        backgroundColor: WidgetStatePropertyAll(Colors.red),
      ),
      iconSize: 40,
    );
  }
}
