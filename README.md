# Proyect02
## Steganografia

*Aplicación en la línea de comandos para ocultar o develar mensajes ocultos en imágenes.*

### Prerequisitos

-  Python3
-  PyPI - OpenCV, 

Asegúrese de de tener `python3` y `pip` en su computadora:

```sh
$ sudo apt-get install python3-pip
```

Luego, debe instalar las siguientes paqueterías:

```sh
$ pip install filetype
```
```sh
$ pip install opencv-python
```
```sh
$ pip install unidecode
```

### Ejecutar el Programa

Para ejecutar el programa sólo debe escribir en la línea de comandos:

```sh
$ python3 src/main/myp/esteganografia.py
```

Seguido de la opción **h** para ocultar, 
* el nombre del archivo que contiene el texto a ocultar, 
* el nombre del archivo de imagen, 
* el nombre del archivo de imagen resultante con los datos ocultos.
```sh
$ python3 src/main/myp/esteganografia.py h archivo_ocultar imagen_ocultar nombre_destino
```

O bien, la opción **u** para develar, 
* el nombre del archivo con la imagen que contiene los datos ocultos, 
* el nombre del archivo en el que se guardará el texto develado.
```sh
$ python3 src/main/myp/esteganografia.py u imagen_develar nombre_destino
```

### Ejemplo
- Ocultar
```sh
$ python3 src/main/myp/esteganografia.py h src/data/msg.txt src/data/neon_rosa.jpg src/data/ejemplo.png
Imagen codificada exitosamente:  src/data/ejemplo.png
```
- Develar
```sh
$ python3 src/main/myp/esteganografia.py u src/data/ejemplo.png src/data/ejemplo.txt
Mensaje obtenido en:  src/data/ejemplo.txt
```

### Pruebas Unitarias

Para ejecutar los test del programa sólo debe escribir en la línea de comandos:

```sh
$ python3 -m unittest discover src/test/ -p "*.py"
```

