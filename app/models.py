class To_do:
    def __init__(self, title, **kwargs):
        self.title = title
        self.description = kwargs.get("description", "")
        self.completed = kwargs.get("completed", False)
        self.prioridad = kwargs.get("prioridad", None)
        
        for clave, valor in kwargs.items():
            setattr(self, clave, valor)

    def __str__(self):
        prio_str = f" [Prioridad: {self.prioridad}]" if self.prioridad else ""
        desc_str = f" - {self.description}" if self.description else ""
        
        return f"{self.title}{desc_str}{prio_str}"