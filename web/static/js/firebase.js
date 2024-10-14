// import firebase from 'firebase/app';
// import 'firebase/firestore';

// // Configuración de Firebase (reemplaza con tus credenciales)
// const firebaseConfig = {
//     "type": "service_account",
//     "project_id": "foodpartner-717d3",
//     "private_key_id": "5e6e8dba8e11e42dc0bdb293eec15bbbdde9570d",
//     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDwOxjIRx5nWxV/\n6CuI1mn1buat/KdMyFayHdMtVpFFoqjwMqgb6Dp3w+cKbMhC6j1yHnF2AjNcaqYB\nsTNAKdJlNQ9wRVeW2vy/T2NlMf8YxHetUxaL8E3+H5lVZ3kNqfvRnbxfHbmw+IQd\nbH6RvLYgeeUmscYMaudir508Tua5zwhP/4xnKxpMbwJYjT0fRg1v5ocaADSXaAc4\ng9BWma/oMP4RQLqenRPKViR6/G8nuimsHwUjQ/Qatzol3Dj/duOVjGAKB65lbGwZ\nl7tdHLJRJhmSMVGz0fO+R/+QONeVvPIZWp8SD5UPTMBu8C9c7DzdQ58vqKnmS445\njPUGwP8JAgMBAAECggEAA9Gkr2ELYjA9U2xg7iAed24yZkIAdNowdUy/voDu9puY\nh5epOtGtGu9MfSAalORoDVLfkd/aFNYwhRFd6QoL1AZiaZyolkzX52tUf1d/9dMA\nZgsj7h3oAioFbtP3cC4Aw1B4c035KuTge3Pt6n+EqQKBuo+T6umeJmBNUG1JV1sj\nz20zsLp5DyUjGDq/PHKPTEdonGY4u4LSnERa6DkM914bA4CBMDVdWZfpSsfV16En\nW3dF+wepQkylLUm8EGuFgHZ0+QPWP9PQUH0IRspcYdLNPo8T1TPkeaRQ5RuOl5CA\nonG+JdJ8CPxfxKCtF4GTZUW208G0Nj2+lx52c/PR8wKBgQD8PJizjrcZlPaFTfL0\nP8miU+13G/YtPb7dVjqdCoSZ8g3EzfxlX5ueAqK37XDKziZLthe72tOEd55tLeo8\n2U77EZfkfC85pMTkR9yOcH48CL5/jPImVtQgt+18uLhEP8FWPZjkA38BhGBAM+5u\nMX8Pe4q5h95utQBOx1Ogqow/IwKBgQDz0KUGz/oDg3PXvsE9ZjDr/QsRbpRWStJ0\nrw/IJNGBz96S7KVYjUuxvwlU4CiBI3qkmMlLv1/HaPdt7pax8cFhSoHpJwRqg8g3\nrlgVv0pskpExlR55ZIM0+h5sYItWknKnDUI4UUlPuyX6ZOp648H5nOn5z8s4yi8S\ng0nbZ5Ch4wKBgC+zngVHFiWGYGCxbyL19UH3sU73QMUpijD9n7QXSyB6AFSZyAO7\n4wgs42z5QH16Iw/qbe6e4aWJobJwHn5HcoJUv278dUnneTzawkFF0Pm1haFFnH3X\nqeJOJmGR5Xcyv3N5zrJAXwKAcFtz9sFsJuVcrc2MfmpdXKOJWq1l04QVAoGAeHRq\nM5VolXfKMZqCac0k+lIHt9MD4iYRF6itiVn3T8Tc14Wmorsb3HLfL1mXaUWX/92k\nBZJExYXsSBmJxdwEiAaBbCjkm6MDtc6iogvhvwYiSXa8mYi48eFoSm7gKCMuFa4N\nOzmdmJCDUNOurIv9d064obyxUBtDakgGoyjlYbUCgYAecQEQt1nGMYpakjQdyQog\ngDlwosWKxf8osK+sYxnM4cGikhnbpc6pKKLAFtx0/6l7O3oQBuntIDVIuhM5EXHM\nt0HCjNta/iWPxhIxOh3xfk00Lw4rHOJtwywe2ii6n4KCimqmey1ppddoumbpwj38\n8+MPuAuOjpkkvHxpaVzTGA==\n-----END PRIVATE KEY-----\n",
//     "client_email": "firebase-adminsdk-a8acj@foodpartner-717d3.iam.gserviceaccount.com",
//     "client_id": "105610341686083135935",
//     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
//     "token_uri": "https://oauth2.googleapis.com/token",
//     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
//     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-a8acj%40foodpartner-717d3.iam.gserviceaccount.com",
//     "universe_domain": "googleapis.com"
// };

// // Inicializar Firebase
// firebase.initializeApp(firebaseConfig);

// // Obtener una referencia a la colección "carrito"
// const db = firebase.firestore();
// export const carritoRef = db.collection('carrito');