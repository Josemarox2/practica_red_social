import json

from red_social.publicacion import Tweet
from red_social.red import RedSocial


def test_timeline_solo_tiene_publicaciones_de_los_seguidos(red):
    ana = red["@ana"]
    luis = red["@luis"]
    marta = red["@marta"]

    # Creamos 2 posts de Ana
    primer_post = red.publicar(Tweet(ana, "Primer tweet de Ana"))
    segundo_post = red.publicar(Tweet(ana, "Segundo tweet de Ana"))

    # Como Luis no sigue a marta ni a sí mismo, no deberían de salir
    red.publicar(Tweet(marta, "Tweet de Marta"))
    red.publicar(Tweet(luis, "Tweet de Luis"))

    assert red.timeline(luis) == [segundo_post, primer_post]
    assert red.timeline(ana) == []


def test_desde_json_construye_usuarios_y_seguimientos(mocker):
    contenido = json.dumps(
        {
            "usuarios": [
                {"nombre": "Ana", "alias": "@ana"},
                {"nombre": "Luis", "alias": "@luis"},
            ],
            "seguimientos": [["@luis", "@ana"]],
        }
    )

    open_mocker = mocker.patch("builtins.open", mocker.mock_open(read_data=contenido))

    red = RedSocial.desde_json("datos/mocker.json")

    open_mocker.assert_called_once_with("datos/mocker.json", encoding="utf-8")
    assert len(red) == 2
    assert red["@luis"].sigue_a(red["@ana"]) is True
    assert red["@ana"].sigue_a(red["@luis"]) is False
