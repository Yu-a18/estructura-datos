class Nodo:

    def __init__(self, data):
        self.data = data
        self.next = None

    def show(self):
        print(f"Titulo {self.data[0]}")
        print(f"Artista: {self.data[1]}")
        print(f"Año: {self.data[2]}")
        print(f"Genero: {self.data[3]}")
        print("")
        print("-" * 20)



class linked_list:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_first(self, data):
        new_node = Nodo(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def insert_last(self, data):
        new_node = Nodo(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def insert_at(self, data, position):
        if position < 0 or position > self.size:
            print("invalid position")
        elif position == 0:
            self.insert_first(data)
        elif position == self.size:
            self.insert_last(data)
        else:
            previous = self.head
            k = 0
            while k < position - 1:
                previous = previous.next
                k += 1
            new_node = Nodo(data)
            new_node.next = previous.next
            previous.next = new_node
            self.size += 1

    def show(self):
        print(f"Head = {self.head} ---- Tail = {self.tail} ---- Size = {self.size}")
        print("Nodos:")
        current = self.head
        while current is not None:
            current.show()
            current = current.next



    def search(self, search):
        current = self.head
        encontrado = False
        while current is not None:
            if search in current.data[0] or search in current.data[1]:
                print("Cancion enconcontrada")
                current.show()
                encontrado = True
            current = current.next
        if not encontrado:
            print("No se encontro la cancion")


# ---Menu----
lista = linked_list()

while True:
    print("--- REPRODUCTOR DE MUSICA ---")
    print("1. insetar cancion ")
    print("2. buscar cancion")
    print("3. mostrar canciones")
    print("4. salir")


    opcion = input("Elija una opcion: ")


    if opcion == "1":
        titulo = input("Titulo: ")
        artista = input("Artista: ")
        año = input("Año: ")
        genero = input("Genero: ")

        cancion = [titulo, artista, año, genero]


        print("1. Al inicio")
        print("2. Al final")
        print("3. En una posicion")
        tipo = input("Donde insertar (1-3): ")

        if tipo == "1":
            lista.insert_first(cancion)
        elif tipo == "2":
            lista.insert_last(cancion)
        elif tipo == "3":
            pos = int(input("Posicion: "))
            lista.insert_at(cancion, pos)

    elif opcion == "2":
        buscar_texto = input("Ingrese titulo o artistas a buscar: ")
        lista.buscar(buscar_texto)

    elif opcion == "3":
        lista.show()
    
    elif opcion == "4":
        print("Saliendo del programa")
        break

    else:
        print("Opcion invalida")


 
