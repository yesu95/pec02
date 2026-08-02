from app.colors import *

class To_do:
    def __init__(self, title, **kwargs):
        self.title = title
        self.description = kwargs.get("description", "")
        self.priority = kwargs.get("priority", None)
        
        for clave, valor in kwargs.items():
            setattr(self, clave, valor)

    def __str__(self):
        prio_str = f" [Prioridad: {self.priority}]" if self.priority else ""
        desc_str = f" - {self.description}" if self.description else ""
        
        return f"{G}{self.title}{RA}{desc_str}{prio_str}{RA}"