class Pila:

    def __init__(self):
        self.items=[]

    def apilar(self, x):
        self.items.append(x)

    def desapilar(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("Lapila Esta Vacia")

    def es_vacia(self):
        return self.items == []

    def mostrar_pila(self):
        print(self.items)
                
