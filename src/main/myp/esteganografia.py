"""
Clase para validar los argumentos de entrada.
"""
from develar import Develar
from codificar import Codificar

# Usamos sys para leer la entrada de terminal
import sys
# Usamos os para verificar la existencia de nuestros archivos
import os
# Usamos filetype para verificar que las imagenes son válidas
import filetype

from ocultar import oculta

class Main:

    def __init__(self):
        pass
        
    def imprimeUso(mensaje):
        """
        Indica los argumentos que se esperan recibir 
        para que el programa funcione.
                
        """
        print (mensaje)
        doc = "Ocultar: h texto_ocultar.txt imagen_ocultar.png nombre_destino.png \n" 
        doc += "Develar: u imagen_develar.png nombre_destino.png"
        sys.exit(doc)

    def verifica():
        """
        Verifica que la entrada sea correcta.
        
        Que tenga las banderas adecuadas 
        - h para oculta
        - u para develar
        y reciba los argumentos correspondientes.

        En caso contrario, imprime el modo de uso del programa.
        """
        if len(sys.argv) <= 1:        
            Main.imprimeUso("%s" % sys.argv[0])
        elif (sys.argv[1] == "h"):        
            if len(sys.argv) != 5:
                Main.imprimeUso("Se requieren 4 argumentos, usted introdujo %d" % (len(sys.argv) - 1))
            else:
                Main.verificaOcultar(sys.argv[2:5])        
        elif (sys.argv[1] == "u"):
            if len(sys.argv) != 4:
                Main.imprimeUso("Se requieren 3 argumentos, usted introdujo %d" % (len(sys.argv) - 1))
            else:
                Main.verificaDevelar(sys.argv[2:4]);            
        elif (sys.argv[1] != "u" and sys.argv[1] != "h"):
            Main.imprimeUso("La entrada es incorrecta")

    def verificaOcultar(arr):
        """
        Verifica que la entrada para ocultar sea correcta.
        
        Que el archivo y la imagen para ocultar existan, 
        en caso de que no, imprime el modo de uso.

        Asume que el metodo es destructivo y no verifica 
        si el nombre de destino ya existe.
        """
        if not os.path.isfile(arr[0]):
            Main.imprimeUso("Archivo a ocultar no válido")
        try:
            filetype.is_image(arr[1])                        
        except FileNotFoundError:
            Main.imprimeUso("Imagen destino no válida")
        else:
            f = open(arr[0])
            mensaje = f.read()
            print(mensaje)
            oculta(arr[1], mensaje, arr[2])
            print ("Se guardo en: ", arr[2])
            
    
    def verificaDevelar(arr):
        """
        Verifica que la entrada para develar sea correcta.
        
        Que la imagen a develar exista, en caso de que no
        imprime el modo de uso de nuestro programa.

        Asume que el metodo es destructivo y no verifica 
        si el nombre de destino ya existe.
        """
        try:
            filetype.is_image(arr[0])                        
        except FileNotFoundError:
            Main.imprimeUso("Imagen de origen no válida")
        else:
            msg = Develar.decodifica(arr[0])
            f = open(arr[1], "w")             
            f.write(msg)
            f.close()
            print ("Se guardo en: ", arr[1])

if __name__ == "__main__":
        Main.verifica()