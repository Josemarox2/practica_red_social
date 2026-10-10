class Usuario:
    """Clase para la gestión de usuarios

    Atributos:
        nombre, alias, seguidos

    Métodos:
        seguir, sigue_a, a_dict

    Properties:
        numero_seguidos

    Constructor alternativo:
        desde_dict

    Métodos especiales:
        __str__, __eq__
    """

    def __init__(self, nombre: str, alias: str):
        """Constructor de la clase Usuario.

        Args:
            nombre: Nombre del usuario.
            alias: Nombre del usuario que comienza por @.
            Se le añade si no lo tiene.
            seguidos: Lista vacía donde se almacenan los usuarios que sigue.
        """

        self.nombre = nombre

        # Revisamos si el alias tiene @, si no lo tiene, se le añade.
        if alias[0] == "@":
            self.alias = alias
        else:
            self.alias = "@" + alias

        # Lista vacía donde se almacenan los usuarios que sigue.
        self.seguidos = []

    def seguir(self, otro):
        """Método de la clase Usuario que nos permite seguir a otro usuario.

        Args:
            otro: Usuario al que se le va a seguir.
        """

        # Lanzamos ValueError si el usuario se intenta seguir a sí mismo
        # o a uno que ya sigue.
        if otro == self:
            raise ValueError("El usuario no se puede seguir a sí mismo")
        elif self.sigue_a(otro):
            raise ValueError(f"Ya estás siguiendo al usuario '{otro.alias}'")
        else:
            self.seguidos.append(otro)

    def sigue_a(self, otro) -> bool:
        """Método de la clase Usuario. Devuelve un boolean para saber
        si el usuario indicado está siendo seguido.

        Args:
            otro: Usuario al que se quiere confirmar si se le sigue o no.
        """

        return otro in self.seguidos

    def a_dict(self) -> dict:
        """Método de la clase Usuario que nos devuelve un diccionario
        con el nombre y el alias del usuario.
        """

        return {"nombre": self.nombre, "alias": self.alias}

    @property
    def numero_seguidos(self) -> int:
        """Property de la clase Usuario que nos devuelve el numero
        de seguidos que tiene el usuario."""

        return len(self.seguidos)

    @classmethod
    def desde_dict(cls, datos: dict):
        """Constructor alternativo de la clase Usuario que crea un
        usuario a partir de un diccionario.

        Args:
            datos: Diccionario con las keys 'nombre' y 'alias'
        """

        return cls(datos["nombre"], datos["alias"])

    def __str__(self) -> str:
        """Método especial __str__ de la clase Usuario que se utiliza para
        mostrar el usuario al usar print."""

        return f"{self.nombre} ({self.alias})"

    def __eq__(self, otro) -> bool:
        """Método especial __eq__ de la clase Usuario para saber cuando
        dos usuarios son iguales, revisado por el alias

        Args:
            otro: Usuario con el que se hace la comparación."""

        return self.alias == otro.alias
