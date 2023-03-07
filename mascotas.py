# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    mascotas.py                                          ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/03/07 09:07:52 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/03/07 09:46:28 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

class Mascota:
    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre
        self._especie = self.__class__.__name__.lower()
        self._edad = edad

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def especie(self) -> str:
        return self._especie

    @property
    def edad(self) -> int:
        return self._edad

    def __str__(self) -> str:
        return f"{self.nombre} es un {self.especie} de {self.edad} años"

    def ver_nombre(self) -> None:
        print(self.nombre)

    def ver_especie(self) -> None:
        print(self.especie)

    def ver_edad(self) -> None:
        print(self.edad)

class Gato(Mascota):
    pass

class Canario(Mascota):
    pass

class Perro(Mascota):
    def __init__(self, nombre: str, edad: int, persigue_gatos: bool):
        super().__init__(nombre, edad)
        self._persigue_gatos = persigue_gatos

    @property
    def persigue_gatos(self) -> bool:
        return self._persigue_gatos

    def __persigue_gatos__(self) -> bool:
        return self.persigue_gatos

def print_data(data: list) -> None:
    print(f"{'nombre':8} | {'especie':7} | {'edad':4} | Persigue")
    for m in data:
        extra = ""
        if isinstance(m, Perro):
            extra = "persigue gatos"
            if not m.persigue_gatos:
                extra = "no " + extra
        print(f"{m.nombre:8} | {m.especie:7} |   {m.edad}  | {extra}")

def print_all(data: list) -> None:
    print("Todos los datos:")
    print_data(data)

def print_cats(data: list) -> None:
    print("Todos los gatos:")
    print_data(filter(lambda m: isinstance(m, Gato), data))

def print_oldest(data: list) -> None:
    print("La mascota con mayor edad:")
    m = data[0]
    for n in data:
        if n.edad > m.edad:
            m = n
    print(m)

def print_dogs(data: list) -> None:
    print("Información de los perros:")
    print_data(filter(lambda m: isinstance(m, Perro), data))

if __name__ == "__main__":
    '''
    Escribe un programa en Python llamado mascotas.py que contenga una Clase
    llamada Mascota que permita crear mascotas con un nombre, una especie y una
    edad. La aplicación guardará toda la información de las mascotas creadas.

    En la Clase se definirán los métodos para ver el nombre ver_nombre(), ver
    la especie ver_especie(), y ver la edad ver_edad().
    Además, la Clase tendrá un método __str__ () que devolverá un mensaje del
    tipo:    "%s es un %s" % (nombre, especie)

    Crea otra Clase llamada Perro que va a heredar de la clase Mascota, para
    poder ver este comportamiento particular en diferentes perros
    (objetos Perro).
    Algunas mascotas pueden ser perros y a la mayoría de ellos les gusta
    perseguir gatos y, tal vez, queramos saber a qué perro le gusta perseguir
    gatos y a qué perro no. Añade un método llamado __persigue_gatos__() que
    muestre si a un Perro determinado le gusta perseguir gatos o no.
    Crea las siguientes mascotas con sus datos:

    nombre     especie   edad    Persigue  
    Tobi        Perro     3      persigue gatos 
    Persi       Gato      1
    Moli        Perro     2      no persigue gatos 
    Cani       Canario    4
    Anki        Gato      2
    Chuski      Perro     3      persigue gatos 

    Una vez creadas las mascotas y guardados sus datos en la aplicación,
    se realizarán las siguientes acciones de forma automática:
        1. El programa mostrará todos los datos (nombre, especie, edad)
        introducidos anteriormente.
        2. El programa mostrará sólo la información completa asociada
        a los gatos.
        3. El programa mostrará sólo los datos completos de la mascota más 
        vieja de forma automática.
        4. El programa mostrará si a una mascota Perro le gusta perseguir gatos
        o no.
    '''
    data = [
        Perro("Tobi", 3, True),
        Gato("Persi", 1),
        Perro("Moli", 2, False),
        Canario("Cani", 4),
        Gato("Anki", 2),
        Perro("Chuski", 3, True)
    ]
    print_all(data)
    print("\n")
    print_cats(data)
    print("\n")
    print_oldest(data)
    print("\n")
    print_dogs(data)
