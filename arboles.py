# Definición del nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


# Recorrido Inorden (Izquierda - Raíz - Derecha)
def inorden(nodo):
    if nodo:
        inorden(nodo.izquierda)
        print(nodo.valor, end=" ")
        inorden(nodo.derecha)


# Recorrido Preorden (Raíz - Izquierda - Derecha)
def preorden(nodo):
    if nodo:
        print(nodo.valor, end=" ")
        preorden(nodo.izquierda)
        preorden(nodo.derecha)


# Recorrido Postorden (Izquierda - Derecha - Raíz)
def postorden(nodo):
    if nodo:
        postorden(nodo.izquierda)
        postorden(nodo.derecha)
        print(nodo.valor, end=" ")


# Crear el árbol
raiz = Nodo(10)
raiz.izquierda = Nodo(5)
raiz.derecha = Nodo(20)

raiz.izquierda.izquierda = Nodo(3)
raiz.izquierda.derecha = Nodo(7)

raiz.derecha.izquierda = Nodo(15)
raiz.derecha.derecha = Nodo(25)


# Mostrar recorridos
print("Recorrido Inorden:")
inorden(raiz)

print("\nRecorrido Preorden:")
preorden(raiz)

print("\nRecorrido Postorden:")
postorden(raiz)
