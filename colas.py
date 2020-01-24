class Cola:

    def __init__(self):
        self.items = []
        
    def encolar(slef, x):
        self.items.append(x)
        
    def desencolar(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola esta vacia")
        
    def es_vacia(self):
        return self.items == []