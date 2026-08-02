# Gestor de Tareas CLI

Una aplicación de consola desarrollada en Python para la gestión de tareas (**CRUD**), con  sistema de **registros (logging)** y validación avanzada de entradas.

---

## Estructura del Proyecto

```text
mi-gestor-tareas/
│
├── app/
│   ├── __init__.py      # Inicializador del paquete
│   ├── colors.py        # Códigos ANSI para colores en consola
│   ├── models.py        # Definición de la clase To_do
│   └── operations.py    # Lógica CRUD
│
├── venv/                # Entorno virtual de Python
├── main.py              # Punto de entrada principal del programa
├── requirements.txt     # Librerías del proyecto
└── README.md            # Documentación del proyecto (Estás aquí)