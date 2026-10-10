import pytest

from red_social.publicacion import Tweet
from red_social.red import RedSocial
from red_social.usuario import Usuario


@pytest.fixture
def ana() -> Usuario:
    return Usuario("Ana", "@ana")


@pytest.fixture
def luis() -> Usuario:
    return Usuario("Luis", "@luis")


@pytest.fixture
def tweet(ana) -> Tweet:
    return Tweet(ana, "Hola a todos #python #pytest")


@pytest.fixture
def red() -> RedSocial:
    # Creamos algunos usuarios dentro de la red
    red = RedSocial()
    red.registrar("Ana", "@ana")
    red.registrar("Luis", "@luis")
    red.registrar("Marta", "@marta")

    # Luis sigue a Ana
    red["@luis"].seguir(red["@ana"])
    return red
