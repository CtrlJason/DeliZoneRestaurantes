
# Proyecto de Plataforma Web para Restaurantes

Este proyecto es una plataforma web diseñada para restaurantes que permite la gestión de productos, pedidos y subdominios personalizados para mejorar la experiencia del cliente. El proyecto utiliza **Firebase** para la gestión de datos y **Django** como framework principal.

## Requisitos

- **Python 3.8 o superior**
- **pip** (para instalar las dependencias)
- **Firebase** (para la gestión de la base de datos y almacenamiento)

## Configuración del Proyecto

### Variables de Entorno

1. Copia el archivo `.env.example` a `.env`
2. Completa las variables con tus propias credenciales:
   - Crea un proyecto en Firebase
   - Genera una nueva clave de servicio en Firebase Console
   - Copia las credenciales al archivo `.env`

### Pasos para configurar Firebase

1. Ve a Firebase Console (https://console.firebase.google.com/)
2. Crea un nuevo proyecto
3. Crea tu FireStore Database en compilacion en el menú izquierdo
4. Crea tu Storage en compilacion en el menú izquierdo y copia el enlace al archivo `.env`
5. Ve a Configuración del Proyecto > Cuentas de Servicio
6. Genera una nueva clave privada
7. Copia los detalles al archivo `.env`

## Instalación

Sigue los pasos a continuación para instalar y configurar el proyecto localmente.

### 1. Clonar el repositorio

```bash
git clone https://github.com/CtrlJason/DeliZoneRestaurantes
cd repositorio
```

### 2. Crear un entorno virtual (opcional pero recomendado)

Si deseas aislar las dependencias del proyecto en un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

Instala las dependencias necesarias utilizando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
```
# 
cp .env.example .env
# Edita .env con tus credenciales
```

#### 4.1 Ejecutar migraciones
```
python manage.py migrate
```

### 5. Ejecutar el proyecto

Una vez que hayas configurado todo, puedes ejecutar el servidor de Django:

```bash
python manage.py runserver
```

Accede al proyecto en tu navegador a través de `http://localhost:8000`.

---

## Contacto

Si tienes alguna pregunta o inquietud, no dudes en contactarme a través del correo electrónico **yeisondamosquera@gmail.com**.
