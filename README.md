# Proyect02
## Steganografia

*Aplicación en la línea de comandos para ocultar o develar mensajes ocultos en imágenes.*

### Prerequisitos

-  Python
-  PyPI - Pillow, filetype
-  Python-stepic

Asegúrese de de tener `python3`, `stepic` y `pip` en su computadora:

```sh
$ sudo apt-get install python3-pip
$ sudo apt-get install python-stepic
```

Luego, debe instalar la paquetería Pillow y filetype:

```sh
$ pip install Pillow
$ pip install filetype
```

### Ejecutar el Programa

Para ejecutar el programa sólo debe escribir en la línea de comandos:

```sh
$ python3 src/main/myp/main.py
```

### Pruebas Unitarias

Para ejecutar los test del programa sólo debe escribir en la línea de comandos:

```sh
$ python3 -m unittest discover src/test/ -p "*.py"
```

