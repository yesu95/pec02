# Gestor de Tareas CLI

Una aplicación de consola desarrollada en Python para la gestión de tareas (**CRUD**), con  sistema de **registros (logging)** y validación avanzada de entradas.

---

## Disclaimer (IMPORTANTE)

He realizado la mayoría de commits con una cuenta eliminada (JeFr95) mediante VSCODE con la cual me ha dejado subir archivos sin ningún problema a pesar de que había sido eliminada. 
Por ningún lado estoy viendo que salgan dichos commits en la web ya que el único contributor que se muestra soy yo (yesu95) pero mediante comandos se pueden llegar a ver. Espero que esto no sea un problema, cualquier cosa me escribe por classroom.

### Ver el historial del repositorio

```bash
git log --all --graph --oneline --decorate
```

![Logo]([https://ibb.co/FqBRjZJY](https://i.ibb.co/NnLcHDpN/commits.png))

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
