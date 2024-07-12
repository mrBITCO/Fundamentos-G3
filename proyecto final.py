class Libro:
    def __init__(self, titulo, autor, genero, año):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.año = año
        self.prestado = False

    def prestar(self):
        self.prestado = True

    def devolver(self):
        self.devolver = False

    def __str__(self): 
        return f"{self.libro} {self.estado} Prestado/Disponible "
    

class Biblioteca:
    def __init__(self):
        self.libros = []
        
    def agregar_libros(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, titulo):
        self.libros =[libro for libro in self.libros if libro.titulo != titulo]

    def buscar_titulo(self, titulo):
        self.libros =[libro for libro in self.libros if libro.titulo == titulo]

        
    def buscar_autor(self, autor):
        self.libros =[libro for libro in self.libros if libro.autor == autor]

    def buscar_genero(self, genero):
        self.libros =[libro for libro in self.libros if libro.genero == genero]

    def listar_libros(self):
        return self.libros

        
def menu ():
    print("BIBLIOTECA")
    print("1 Agregar Libro")
    print("2 Eliminar Libro")
    print("3 Buscar Libro por Titulo")
    print("4 Buscar libro por Autor")
    print("5 Buscar libro por Genero")
    print("6 Listar todos los Libros")
    print("7 Prestar Libros")
    print("8 Devolver Libros")
    print("9 Guardar y Salir")

biblioteca = Biblioteca()

while True:
    menu()
    opcion = input("\nSeleccione una opcion: ")
    if opcion == "1":
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        genero = input("Genero: ")
        año = input("Año: ")
        libro = Libro(titulo, autor, genero, año)

    elif opcion == "2":
        titulo = input("Titulo del Libro a eliminar es: ")
        biblioteca.eliminar_libro(titulo)
       

    elif opcion == "3":
        titulo = input("Titulo del libro a buscar es: ")
        busqueda = biblioteca.buscar_titulo(titulo)
        for libro in busqueda:
            print(libro)

    elif opcion == "4":
        autor = input("Autor del libro a buscar es: ")
        busqueda = biblioteca.buscar_autor(autor)
        for libro in busqueda:
            print(libro)

    elif opcion == "5":
        genero = input("genero del libro a buscar es: ")
        busqueda = biblioteca.buscar_genero(genero)
        for libro in busqueda:
            print(libro)    

    elif opcion == "6":
        for libro in biblioteca.listar_libros():
            print(libro)

    elif opcion == "7":
        titulo = input("Titulo del libro a Prestar: ")
        resultado = biblioteca.buscar_titulo(titulo)
        if resultado:
            resultado[0].prestar()
            print(f"El Libro '{titulo}', ha sido prestado ")
        else:
            print("Libro no encontrado")

    elif opcion == "8":
        titulo = input("Titulo del libro a devolver: ")
        resultado = biblioteca.buscar_autor(titulo)
        if resultado:
            resultado[0].devolver()
            print(f"El Libro '{titulo}', ha sido devuelto ")
        else:
            print("Libro no encontrado")

    elif opcion == "9":
        print("Datos guardados. Saliendo del Programa")
        break

    else:
        print("Opcion no valida, Intente Nuevamente")

  


    
        

    


    



