import json
from collections import Counter

from red_social.usuario import Usuario


class RedSocial:
    """Clase para la red social. Tiene usuarios y publicaciones.

    Atributos:
        usuarios, publicaciones

    Métodos:
        anadir, registrar, publicar, timeline, tendencias, mostrar_timeline

    Constructor alternativo:
        desde_json

    Métodos especiale:
        __len__, __iter__, __contains__, __getitem__
    """

    def __init__(self):
        """Constructor de la clase RedSocial. No recibe ningún parámetro"""

        # Diccionario donde se almacenaran los usuarios "alias": "Usuario"
        self.usuarios = {}

        # Se almacenaran las publicaciones en esta lista.
        self.publicaciones = []

    @classmethod
    def desde_json(cls, ruta: str):
        """Constructor alternativo de la clase RedSocial donde crea la
        red a partir de un fichero JSON.

        Args:
            ruta: Ruta del fichero JSON."""

        with open(ruta, encoding="utf-8") as f:
            datos = json.load(f)

        red = cls()

        # Creamos los usuarios con el el desde_dict de la clase Usuario
        for datos_usuario in datos["usuarios"]:
            red.anadir(Usuario.desde_dict(datos_usuario))

        # Hacemos los seguimientos con seguir de la clase Usuario
        for quien_sigue, a_quien in datos["seguimientos"]:
            red[quien_sigue].seguir(red[a_quien])

        return red

    def anadir(self, usuario):
        """Método de la clase RedSocial para guardar los usuarios al
        diccionario.

        Args:
            usuario: Usuario que se va a añadir."""

        # Lanzamos ValueError si el alias ya existe
        if usuario.alias in self.usuarios:
            raise ValueError(f"El usuario '{usuario.alias}' ya existe.")

        self.usuarios[usuario.alias] = usuario
        return usuario

    def registrar(self, nombre: str, alias: str):
        """Método de la clase RedSocial crea al usuario y lo añade a la red

        Args:
            nombre: Nombre del usuario.
            alias: Alias del usuario."""

        return self.anadir(Usuario(nombre, alias))

    def publicar(self, publicacion):
        """Método de la clase RedSocial para guardar las publicaciones

        Args:
            publicacion: Post que va a publicarse"""

        self.publicaciones.append(publicacion)
        return publicacion

    def timeline(self, usuario) -> list:
        """Método de la clase RedSocial que devuelve las publicaciones
        de los usuarios a los que sigue.

        Args:
            usuario: Usuario del que se quiere obtener los posts.
        """

        return [
            publicacion
            for publicacion in self.publicaciones[::-1]
            if usuario.sigue_a(publicacion.autor)
        ]

    def tendencias(self, n: int = 3) -> list:
        """Método de la clase RedSocial que devuelve los hashtags más
        usados como lista de tuplas de mayor a menor.

        Args:
            n: Número de hashtags que se devuelven."""

        # Metemos en una lista los hashtags de las publicaciones.
        hashtags = []
        for publicacion in self.publicaciones:
            hashtags += publicacion.hashtags

        # most_common nos devuelve los n que más se ha repetido.
        return Counter(hashtags).most_common(n)

    def mostrar_timeline(self, alias: str):
        """Método de la clase RedSocial que nos muestra el timeline del
        usuario.

        Args:
            alias: Alias del usuario del que se mostrará el timeline.
        """

        usuario = self[alias]

        print(f"\nTimeline de {usuario}:")
        for publicacion in self.timeline(usuario):
            print(f"    {publicacion}   ♥ {publicacion.me_gusta}")

    def __len__(self) -> int:
        """Método especial de RedSocial que nos devuelve la len del
        número de usuario en la red."""

        return len(self.usuarios)

    def __iter__(self):
        """Método especial de RedSocial que indica que recorre al hacer
        un for sobre la red: Los usuarios ordenador por alias."""

        return iter([self.usuarios[alias] for alias in sorted(self.usuarios)])

    def __contains__(self, alias: str) -> bool:
        """Método especial de RedSocial para indicar que devuelve cuando
        usamos 'in'.
        Ejemplo: '@ana' in red

        Args:
            alias: Alias que se quiere ver si está en usuarios.
        """

        return alias in self.usuarios

    def __getitem__(self, alias: str):
        """Método especial de RedSocial que indica lo que devuelven los
        corchetes. Ejemplo: red['@ana']

        Args:
            alias: Alias del usuario que se quiere obtener."""

        return self.usuarios[alias]
