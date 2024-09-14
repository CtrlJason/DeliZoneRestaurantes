import firebase_admin
from firebase_admin import credentials, firestore, storage

# Ruta al archivo JSON de credenciales
cred = credentials.Certificate('config/firebase-config.json')
firebase_admin.initialize_app(cred, {'storageBucket': 'foodpartner-717d3.appspot.com'})

# Inicializar Firestore
db = firestore.client()
bucket = storage.bucket()