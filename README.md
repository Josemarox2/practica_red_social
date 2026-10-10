# PROGRAMACIÓN AVANZADA Y BUENAS PRÁCTICAS

Entrega del proyecto final del módulo de Programación Avanzada y Buenas Prácticas del Máster en Data Engineering, MLOps y Arquitectura Cloud en PontIA.

El proyecto consiste en crear una red social a partir del enunciado que aportó el docente utilizando lo aprendido en las clases.

La estructura de carpetas solicitada es la siguiente:
>   ```
>   red_social/            # raíz del proyecto
>   ├── pyproject.toml
>   ├── main.py            # el que te damos, sin tocar
>   ├── datos/usuarios.json
>   ├── red_social/        # el paquete que tienes que escribir
>   │   ├── usuario.py
>   │   ├── publicacion.py
>   │   └── red.py
>   └── tests/
>       ├── conftest.py
>       ├── test_usuario.py
>       ├── test_publicacion.py
>       └── test_red.py
>   ```

Utilizamos `uv` para la creación del proyecto con solo los datos de `usuarios.json` y el `main.py` aportados como parte del material para este proyecto.