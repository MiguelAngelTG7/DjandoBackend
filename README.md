# Notes App

Una aplicación web que permite a los usuarios autenticados crear, leer, actualizar y eliminar notas. Esta aplicación utiliza un backend construido en Django REST Framework y un frontend en React para proporcionar una experiencia de usuario intuitiva.

---

## Índice

- [Descripción](#descripción)
- [Características](#características)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Procesos de Desarrollo](#procesos-de-desarrollo)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Capturas de Pantalla](#capturas-de-pantalla)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

---

## Descripción

Esta aplicación permite a los usuarios gestionar notas personales de manera eficiente. Los usuarios pueden registrarse, iniciar sesión y realizar todas las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre sus notas. 

La API backend está desarrollada con Django REST Framework y utiliza autenticación basada en JSON Web Tokens (JWT). El frontend está desarrollado en React, lo que permite una experiencia de usuario moderna y fluida.

---

## Características

1. **Crear notas**: Los usuarios pueden añadir nuevas notas.
2. **Editar notas**: Actualización de notas existentes.
3. **Eliminar notas**: Borrado de notas seleccionadas.
4. **Visualizar notas**: Listado de todas las notas del usuario.
5. **Autenticación**: Registro e inicio de sesión mediante JWT.

---

## Requisitos Previos

- **Python** (>= 3.8)
- **Node.js** (>= 16.x)
- **npm** o **yarn**
- **Django** (>= 4.x)
- **Django REST Framework** (>= 3.x)
- **React** (>= 18.x)

---

## Instalación

### Backend

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/notes-app.git
   cd notes-app/backend
2. Crea un entorno virtual y actívalo:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt

4. Realiza las migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. Inicia el servidor de desarrollo:
   ```bash
    python manage.py runspiperver

### Frontend

1. Navega al directorio de frontend:
   ```bash
   cd notes-app/frontend

2. Instala las dependencias:
   ```bash
   npm install
   npm install axios react-router-dom jwt-decode

---
## Uso

  1. Accede a la aplicación en http://localhost:5173/register
  2. Regístrate o inicia sesión con un usuario existente.
  3. Gestiona tus notas:
     - Crear nuevas notas.
     - Editar notas existentes.
     - Eliminar notas que ya no necesitas.

  ---
  ## Estructura del Proyecto

    notes-app/
    ├── backend/
    │   ├── api/
    │   │   ├── models.py
    │   │   ├── serializers.py
    │   │   ├── views.py
    │   │   ├── urls.py
    │   └── backend/
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   ├── manage.py
    │   └── urls.py
    ├── env/
    ├── frontend/
    │   ├── src/
    │   │   ├── components/
    │   │   │   ├── Form.jsx
    │   │   │   ├── LoadingIndicator.jsx
    │   │   │   ├── Note.jsx
    │   │   │   └── ProtectedRoute.jsx
    │   │   ├── pages/
    │   │   │   ├── Home.jsx
    │   │   │   ├── Login.jsx
    │   │   │   ├── NotFound.jsx
    │   │   │   └── Resgister.jsx
    │   │   ├── styles/
    │   │   │   ├── Form.css
    │   │   │   ├── Home.css
    │   │   │   ├── LoadingIndicator.css 
    │   │   │   └── Note.css
    │   │   ├── api.js
    │   │   ├── App.jsx
    │   │   ├── constant.js
    │   │   └── main.jsx
    └── README.md
---
## Procesos de Desarrollo

1. Diseño inicial del backend:

  - Creación del proyecto Django.
  - Configuración del modelo Note.
  - Creación de serializadores, vistas y rutas para operaciones CRUD.
  - Configuración de JWT para la autenticación.
  - Desarrollo del frontend:

2. Configuración inicial del proyecto React.
  - Creación de componentes como Note y vistas como Home.
  - Implementación de la comunicación con el backend usando Axios.

3. Integración backend y frontend:
  - Pruebas con solicitudes GET, POST, PUT y DELETE.
  - Manejo de errores y validación.

4. Estilización:
  - Uso de CSS para diseño responsivo y moderno.

---
##Tecnologías Utilizadas

  - Backend: Django, Django REST Framework
  - Frontend: React, Axios
  - Base de datos: SQLite (desarrollo), PostgreSQL (producción)
  - Autenticación: JSON Web Tokens (JWT)

---
##Capturas de Pantalla

![Ventana de Registro](frontend/src/assets/registro.png)

![Ventana de Acceso](frontend/src/assets/acceso.png)

![Ventana de Crear Nota](frontend/src/assets/crearnota.png)

![Ventana de Actualizar Nota](frontend/src/assets/editarnota.png)

---
Licencia
Este proyecto está licenciado bajo la MIT License.

Este archivo `README.md` está listo para ser copiado y pegado. Incluye todo lo necesario para proporcionar una visión general de tu proyecto, cómo configurarlo, usarlo y contribuir.

