# Importamos el SDK de firebase
import firebase_admin
from firebase_admin import credentials, firestore, storage

# Le damos acceso a las configuraciones a Django para que pueda acceder a Firebase
# Guardamos la ruta de las configuraciones para brindarle el acceso a Django
cred = credentials.Certificate('config/firebase-config.json')

# Inicializamos la conexion de Django con Firebase con las con las configuraciones (cred), 
# y realizamos la configuracion del storage con stroageBucket y el storage que queremos usar de Firebase
firebase_admin.initialize_app(cred, {'storageBucket': 'foodpartner-717d3.appspot.com'})

# Inicializar Firestore
db = firestore.client()

# Inicializamos Fire Storage
# bucket representa ese espacio del almacenamiento
bucket = storage.bucket()