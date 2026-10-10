from abc import ABC, abstractmethod

# Número máximo de caracteres para los posts
LIMITE_CARACTERES = 280

# Signos para quitar la puntuación final del hashtag
PUNTUACION_FINAL = ",.;:!?¡¿"


class Publicacion(ABC):
    """Clase abstracta que usarán todas las publicaciones como plantilla.

    Atributos:
        autor, texto, me_gusta

    Métodos:
        dar_me_gusta

    Properties:
        hashtags

    Método estático:
        extraer_hashtags

    Métodos especiales:
        __str__
    """

    def __init__(self, autor, texto: str):
        """Constructor de la clase Publicacion.

        Args:
            autor: Usuario que escribe la publicación
            texto: Texto de la publicación.
        """

        # Damos ValueError si el texto está vacío o solo tiene espacios.
        if texto.strip() == "":
            raise ValueError("No se puede publicar sin texto.")
        if len(texto) > LIMITE_CARACTERES:
            raise ValueError(f"El texto supera los {LIMITE_CARACTERES} caracteres")

        self.autor = autor
        self.texto = texto

        # Número de me gusta que tiene la publicación, empieza por 0.
        self.me_gusta = 0

    def dar_me_gusta(self):
        """Método de la clase Publicacion que incrementa los me gusta."""
        self.me_gusta += 1

    @property
    def hashtags(self) -> list:
        """Property de la clase Publicacion que devuelve los hashtags
        del texto de la publicación."""

        return self.extraer_hashtags(self.texto)

    @staticmethod
    def extraer_hashtags(texto: str) -> list:
        """Método estático de la clase Publicacion que devuelve la lista
        de hashtags de un texto.

        El hashtag debe comenzar por #, en minúscula, sin puntuación
        final, sin repetidos y en orden de aparición.

        Args:
            texto: Texto del que se quiere sacar los hashtags.
        """
        # Lista vacía en la que iremos guardando los hashtag.
        hashtags = []

        # Revisamos si el texto cumple con las condiciones indicadas en el método.
        for palabra in texto.split():
            if palabra[0] == "#":
                hashtag = palabra.rstrip(PUNTUACION_FINAL).lower()

                if len(hashtag) > 1 and hashtag not in hashtags:
                    hashtags.append(hashtag)

        return hashtags

    @abstractmethod
    def __str__(self):
        """Método especial abstracto donde cada clase hija deberá indicar
        como se muestra."""


class Tweet(Publicacion):
    """Clase para los tweets que hereda de Publicacion y utiliza su
    constructor.

    Métodos especiales:
        __str__
    """

    def __str__(self) -> str:
        """Método especial que muestra el tweet de la siguiente manera:

        Ejemplo:
        @ana: Hola a todos #python #pytest
        """
        return f"{self.autor.alias}: {self.texto}"


class Respuesta(Publicacion):
    """Clase para realizar respuesta a las publicaciones.
    Hereda de Publicacion.

    Atributos:
        autor, texto, me_gusta, original

    Métodos especiales:
        __str__
    """

    def __init__(self, autor, texto: str, original):
        """Constructor de la clase Respuesta.

        Args:
            autor: Usuario publicante de la respuesta.
            texto: Texto de la respuesta a publicar.
            original: Publicación a la que se está respondiendo.
        """

        super().__init__(autor, texto)
        self.original = original

    def __str__(self) -> str:
        """Método especial que muestra la respuesta con el siguiente formato:
        @luis ↩ @ana: ¡Bienvenida! #Python
        """

        return f"{self.autor.alias} ↩ {self.original.autor.alias}: {self.texto}"


class Retweet(Publicacion):
    """Clase para los retweets que hereda de Publicacion.

    Atributos:
        autor, texto, me_gusta, original

    Métodos especiales:
        __str__
    """

    def __init__(self, autor, original):
        """Constructor de la clase Retweet.

        Args:
            autor: Usuario que hace el retweet
            original: Publicación que se comparte.
        """

        super().__init__(autor, original.texto)
        self.original = original

    def __str__(self) -> str:
        """Método especial que muestra el retweet en el siguiente formato:
        @marta 🔁 @ana: Hola a todos #python #pytest
        """

        return f"{self.autor.alias} 🔁 {self.original}"
