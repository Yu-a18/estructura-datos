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

    def show_list(self):
        #print(f"Head = {self.head} ---- Tail = {self.tail} ---- Size = {self.size}")
        #print("Nodos: ")
        current = self.head
        while current is not None:
            print(f"Titulo: {current.data[0] } \n Artista: {current.data[1]} \n Año: {current.data[2]} \n Genero: {current.data[3]} ")
            print("-" * 20)
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



new_list = linked_list()

while True:
    print("--- Menu principal ---")
    print("1. insetar cancion ")
    print("2. buscar cancion")
    print("3. mostrar canciones")
    print("4. salir")


    opcion = input("Elija una opcion: ")


    if opcion == "1":
        titulo = input("Inserte el Titulo: ")
        artista = input("Inserte el artista: ")
        año = input("Insertte el año de la cancion: ")
        genero = input("Insertar el genero de la cancion: ")

        new_list.insert_last([titulo, artista, año, genero])

    elif opcion == "2":
        buscar_texto = input("Ingrese titulo o artistas a buscar: ")
        new_list.search(buscar_texto)

    elif opcion == "3":
        print("\n")
        new_list.show_list()
    
    elif opcion == "4":
        print("Saliendo del programa")
        break

    else:
        print("Opcion invalida")


 