# ⚡ FastAPI CRUD - Proyecto de Prueba

Este es un proyecto de ejemplo para implementar un CRUD (Create, Read, Update, Delete) utilizando Python y FastAPI.

---

## 🚀 Despliegue en entorno de producción con Render

Tecnologías utilizadas: Python, FastAPI, Uvicorn, Render.

---

## 📝 Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

- Python 3.8 o superior
- pip

Luego, instala las dependencias necesarias con:

```bash
pip install -r requirements.txt
```

---

## 💻 Ejecución del servidor local

Para iniciar el servidor localmente, ejecuta en la terminal:

```bash
uvicorn main:app --reload
```

Esto levantará el servidor en tu entorno local. Accede a: [http://localhost:8000](http://localhost:8000)

---

## 📄 Documentación interactiva

FastAPI genera automáticamente documentación para tu API. Puedes acceder a ella desde:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

Cuando tu servidor esté corriendo en producción, estos enlaces serán:

- Swagger UI: [https://primer-proyecto-fastapi.onrender.com/docs](https://primer-proyecto-fastapi.onrender.com/docs)
- Redoc: [https://primer-proyecto-fastapi.onrender.com/redoc](https://primer-proyecto-fastapi.onrender.com/redoc)

---

## ☁️ Despliegue en Render

Puedes desplegar esta API en Render siguiendo estos pasos:

1. Crea una cuenta en [Render](https://render.com/).
2. Crea un nuevo servicio web y conecta tu repositorio de GitHub.
3. Configura los parámetros:
   * Build Command: `pip install -r requirements.txt`
   * Start Command: `uvicorn main:app --host 0.0.0.0 --port 10000`
   * Asegúrate de que el puerto sea `10000`.
4. Ilustra que el puerto está correctamente configurado.
5. ¡Listo! Render te dará una URL pública para acceder a tu API.

---

## 🔗 Link de mi despliegue en Render

- [API desplegada](https://primer-proyecto-fastapi.onrender.com)
- [Documentación Swagger](https://primer-proyecto-fastapi.onrender.com/docs)

