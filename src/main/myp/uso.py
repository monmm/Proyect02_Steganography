"""
Clase para validar los argumentos de entrada.
"""
import sys
import os

class Uso:

    def __init__(self):
        pass
        
    def imprimeUso(mensaje):
        """
        Indica los argumentos que se esperan recibir 
        para que el programa funcione.
                
        """
        print (mensaje)
        doc = "Ocultar: h texto_ocultar imagen_ocultar nombre_destino \n" 
        doc += "Develar: u imagen_develar nombre_destino"
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
            Uso.imprimeUso("%s" % sys.argv[0])
        elif (sys.argv[1] == "h"):        
            if len(sys.argv) != 5:
                Uso.imprimeUso("Se requieren 4 argumentos, usted introdujo %d" % (len(sys.argv) - 1))
            else:
                Uso.verificaOcultar(sys.argv[2:5])        
        elif (sys.argv[1] == "u"):
            if len(sys.argv) != 4:
                Uso.imprimeUso("Se requieren 3 argumentos, usted introdujo %d" % (len(sys.argv) - 1))
            else:
                Uso.verificaDevelar(sys.argv[2:4]);            
        elif (sys.argv[1] != "u" and sys.argv[1] != "h"):
            Uso.imprimeUso("La bandera es incorrecta")

    def verificaOcultar(arr):
        """
        Verifica que la entrada para ocultar sea correcta.
        
        Que el archivo y la imagen para ocultar existan, 
        en caso de que no, imprime el modo de uso.

        Asume que el metodo es destructivo y no verifica 
        si el nombre de destino ya existe.
        """
        if not os.path.isfile(arr[0]):
            Uso.imprimeUso("Archivo de origen no válido")
        elif not os.path.isfile(arr[1]):
            Uso.imprimeUso("Imagen destino no válida")
        else:            
            print ("El archivo a ocultar es '" + arr[0] + "' en la imagen: " + arr[1])
            print ("Se guardo en: ", arr[2])
    
    def verificaDevelar(arr):
        """
        Verifica que la entrada para develar sea correcta.
        
        Que la imagen a develar exista, en caso de que no
        imprime el modo de uso de nuestro programa.

        Asume que el metodo es destructivo y no verifica 
        si el nombre de destino ya existe.
        """
        if not os.path.isfile(arr[0]):
            Uso.imprimeUso("Imagen de origen no válida")
        else :
            print ("El archivo a develar es: ", arr[0])
            print ("Se guardo en: ", arr[1])

if __name__ == "__main__":
        Uso.verifica()