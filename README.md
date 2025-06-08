🐍 FastAPI CRUD - Proyecto de Prueba
Este es un proyecto de ejemplo para implementar un CRUD (Create, Read, Update, Delete) utilizando Python y FastAPI.

Despliegue de API RESTful con FastAPI en entorno de producción utilizando Render

Tecnologías utilizadas: Python, FastAPI, Uvicorn, Render.

🚀 Requisitos
Antes de ejecutar el proyecto, asegúrate de tener instalado:

Python 3.8 o superior
pip
Instala las dependencias necesarias con:

pip install -r requirements.txt

🛠️ Ejecución del servidor
Para iniciar el servidor localmente, ejecuta el siguiente comando en la terminal:

uvicorn main:app --reload

Esto levantará el servidor en tu entorno local.

📄 Documentación interactiva
FastAPI genera automáticamente documentación para tu API. Puedes acceder a ella desde:

Swagger UI: /docs
Redoc: /redoc
Una vez que el servidor esté corriendo, abre tu navegador y visita esas rutas.

☁️ Despliegue en Render
Puedes desplegar esta API fácilmente en Render siguiendo estos pasos:

1.Crea una cuenta en Render.
2.Crea un nuevo servicio web y conecta tu repositorio de GitHub.
3.Configura los siguientes parámetros:
Build Command: pip install -r requirements.txt
Start Command: uvicorn main:app --host 0.0.0.0 --port 10000
4.Asegúrate de que el puerto esté configurado correctamente (Render usa el puerto 10000 por defecto).
5.¡Listo! Render te dará una URL pública para acceder a tu API.

Link de mi despligue en Render
https://primer-proyecto-fastapi.onrender.com/
https://primer-proyecto-fastapi.onrender.com/docs