
# Proyecto de Plataforma Web para Restaurantes

Este proyecto es una plataforma web diseñada para restaurantes que permite la gestión de productos, pedidos y subdominios personalizados para mejorar la experiencia del cliente. El proyecto utiliza **Firebase** para la gestión de datos y **Django** como framework principal.

## Requisitos

- **Python 3.8 o superior**
- **pip** (para instalar las dependencias)
- **Firebase** (para la gestión de la base de datos y almacenamiento)

## Instalación

Sigue los pasos a continuación para instalar y configurar el proyecto localmente.

### 1. Clonar el repositorio

```bash
git clone https://github.com/CtrlJason/DeliZone/tree/Dev_web
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

### 4. Configuración de Firebase

Para que el proyecto funcione correctamente, es necesario configurar las credenciales de Firebase. Esto requiere un archivo JSON que contiene las llaves de acceso.

#### 4.1 Crear una carpeta llamada `config`

En la raíz del proyecto, crea una carpeta llamada `config`:

```bash
mkdir config
```

#### 4.2 Obtener el archivo de configuración de Firebase

El archivo `config.json` contiene las llaves de acceso de Firebase necesarias para la autenticación y el uso de la base de datos. Para obtener este archivo, comunícate con el desarrollador a través del correo:

```
yeisondamosquera@gmail.com
```

Coloca el archivo `config.json` dentro de la carpeta `config`.

### 5. Ejecutar el proyecto

Una vez que hayas configurado todo, puedes ejecutar el servidor de Django:

```bash
python manage.py runserver
```

Accede al proyecto en tu navegador a través de `http://localhost:8000`.

---

## Contacto

Si tienes alguna pregunta o inquietud, no dudes en contactarme a través del correo electrónico **yeisondamosquera@gmail.com**.
