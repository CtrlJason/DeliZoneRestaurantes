import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:audioplayers/audioplayers.dart';

final _player = AudioPlayer();

final Map<String, String> _sounds = {
  'Sonido predeterminado': 'sounds/sonido_principal.mp3',
  'Sonido 1': 'sounds/sonido1.mp3',
  'Sonido 2': 'sounds/sonido2.mp3',
};

class Notificaciones extends StatefulWidget {
  const Notificaciones({super.key});

  @override
  _NotificacionesState createState() => _NotificacionesState();
}

class _NotificacionesState extends State<Notificaciones> {
  bool _notificacionesActivadas = true;
  String _sonidoSeleccionado = 'Sonido predeterminado';

  @override
  void initState() {
    super.initState();
    _cargarPreferencias();
  }

  Future<void> _cargarPreferencias() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    setState(() {
      _notificacionesActivadas =
          prefs.getBool('notificacionesActivadas') ?? true;
      _sonidoSeleccionado =
          prefs.getString('sonidoSeleccionado') ?? 'Sonido predeterminado';
    });
  }

  Future<void> _guardarPreferencias() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    await prefs.setBool('notificacionesActivadas', _notificacionesActivadas);
    await prefs.setString('sonidoSeleccionado', _sonidoSeleccionado);
  }

  Future<void> _reproducirSonido(String sonido) async {
    String? path = _sounds[sonido];
    if (path != null) {
      try {
        await _player.play(AssetSource(path));
      } catch (e) {
        print("Error al reproducir el sonido: $e");
      }
    } else {
      print("El sonido no está definido.");
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Configurar Notificaciones'),
      ),
      body: Container(
        margin: const EdgeInsets.symmetric(vertical: 10),
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Switch para activar o apagar las notificaciones
            SwitchListTile(
              title: const Text(
                'Activar Notificaciones',
                style: TextStyle(fontSize: 25),
              ),
              value: _notificacionesActivadas,
              onChanged: (bool value) {
                setState(() {
                  _notificacionesActivadas = value;
                });
                _guardarPreferencias();
              },
              activeTrackColor: const Color.fromRGBO(235, 77, 75, 1),
            ),
            const SizedBox(height: 50),
            // Condicional de switch
            if (_notificacionesActivadas)
              Container(
                margin: const EdgeInsets.only(left: 20),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const Text(
                      'Sonido de Notificaciones',
                      style: TextStyle(fontSize: 20),
                    ),
                    DropdownButton<String>(
                      value: _sonidoSeleccionado,
                      items: <String>[
                        'Sonido predeterminado',
                        'Sonido 1',
                        'Sonido 2',
                      ].map((String value) {
                        return DropdownMenuItem<String>(
                          value: value,
                          child: Text(value),
                        );
                      }).toList(),
                      onChanged: (String? newValue) {
                        setState(() {
                          _sonidoSeleccionado = newValue!;
                        });
                        _guardarPreferencias();
                        _reproducirSonido(newValue!);
                      },
                    ),
                  ],
                ),
              ),
          ],
        ),
      ),
    );
  }
}
