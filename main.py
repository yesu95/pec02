import logging, os
from app.operations import *
from app.models import *
from app.colors import *

logging.basicConfig(
    filename="gestor.log", 
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

gestorActive = True
task_list = []

os.system("cls")

while gestorActive:
    print(B + "========================================")
    print(B + "         GESTOR DE TAREAS v1.0          ")
    print(B + "========================================\n")
    print(Y + "[1]" + RA + " Crear tarea.")
    print(Y + "[2]" + RA + " Ver tareas.")
    print(Y + "[3]" + RA + " Modificar tareas.")
    print(Y + "[4]" + RA + " Eliminar tarea.")
    print(Y + "[5]" + RA + " SALIR.\n" + RA)

    action = input(Y + "Elige opción (1, 2, 3, 4 o 5): " + RA).strip()

    if action == "1":
        add_task(task_list)

    elif action == "2":
        show_tasks(task_list)

    # elif action == "3":
    #     pass

    # elif action == "4":
    #     pass

    elif action == "5":
        print("\nSaliendo del gestor...")
        logging.info("La aplicación se ha detenido.")
        gestorActive = False

    else:
        print(R + "\nOpción no válida. Intenta de nuevo.")
        logging.error("Opción no válida seleccionada en el menú principal.")

    if gestorActive:
        input(M + "\nPresiona Enter ↵ para continuar...")
        os.system("cls")