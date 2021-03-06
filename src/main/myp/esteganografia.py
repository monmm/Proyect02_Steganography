"""
Clase de inicio para nuestro programa, valida los argumentos de entrada 
y manda a llamar los métodos correspondientes según la opción indicada 
por las banderas de entrada con los argumentos recibidos.

"""
from codificar import Codificar
from develar import Develar

# Usamos sys para leer la entrada de terminal
import sys
# Usamos os para verificar la existencia de nuestros archivos
import os
# Usamos filetype para verificar que las imagenes son válidas
import filetype
# Usamos unidecode para simplicar el texto a ocultar
from unidecode import unidecode

class Inicio:

    def __init__(self):
        pass            

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
            Inicio.imprimeUso("%s" % sys.argv[0])
        elif (sys.argv[1] == "h"):        
            if len(sys.argv) != 5:
                Inicio.imprimeUso("Se requieren 4 argumentos, usted introdujo %d" % (len(sys.argv) - 1))
            else:
                Inicio.verificaOcultar(sys.argv[2:5])        
        elif (sys.argv[1] == "u"):
            if len(sys.argv) != 4:
                Inicio.imprimeUso("Se requieren 3 argumentos, usted introdujo %d" % (len(sys.argv) - 1))
            else:
                Inicio.verificaDevelar(sys.argv[2:4]);            
        elif (sys.argv[1] != "u" and sys.argv[1] != "h"):
            Inicio.imprimeUso("La entrada es incorrecta")

    def imprimeUso(mensaje):
        """
        Imprime cuáles son los argumentos que 
        se esperan recibir para que el programa funcione.
        
        Parametros:
        mensaje -- error de entrada capturado

        """
        print (mensaje)
        doc = "Ocultar: h texto_ocultar imagen_ocultar nombre_destino \n" 
        doc += "Develar: u imagen_develar nombre_destino"
        sys.exit(doc)

    def verificaOcultar(arr):
        """
        Verifica que la entrada para ocultar sea correcta y 
        llama al metodo correspondiente para ocultar.
        
        Verifica que el arch_or y la imagen para ocultar existan, 
        en caso de que no, imprime el modo de uso.

        Asume que el metodo es destructivo y no verifica 
        si el nombre de destino ya existe.

        Parametros:
        arr -- la entrada con los argumentos recibidos

        Excepciones:
        FileNotFoundError -- Si la imagen recibida no es válida

        """
        if not os.path.isfile(arr[0]):
            Inicio.imprimeUso("Archivo de texto a ocultar no válido")            
        try:
            filetype.is_image(arr[1])                        
        except FileNotFoundError:
            Inicio.imprimeUso("Imagen de origen no válida")
        else:
            Inicio.llamaOcultar(arr)

    def llamaOcultar(arr):
        """
        Obtiene el mesaje del archivo correspondiente y
        llama al metodo para ocultar el mensaje con la 
        imagen de origen en la imagen de destino.

        Parametros:
        arr -- la entrada con los argumentos recibidos

        """        
        arch_or = open(arr[0], 'r')
        if not arch_or.readable():
            "No pude leer el archivo"
        msj = arch_or.read()
        arch_or.close()
        mensaje = unidecode(msj)    
        Codificar.codifica(arr[1], mensaje, arr[2])            
    
    def verificaDevelar(arr):
        """
        Verifica que la entrada para develar sea correcta y 
        llama al metodo correspondiente para develar.
        
        Verifica que la imagen a develar exista, en caso 
        de que no imprime el modo de uso.

        Asume que el metodo es destructivo y no verifica 
        si el nombre de destino ya existe.

        Parametros:
        arr -- la entrada con los argumentos recibidos

        Excepciones:
        FileNotFoundError -- Si la imagen recibida no es válida

        """
        try:
            filetype.is_image(arr[0])                        
        except FileNotFoundError:
            Inicio.imprimeUso("Imagen de origen no válida")
        else:
            Inicio.llamaDevelar(arr)            

    def llamaDevelar(arr):
        """
        Llama al metodo correspondiente para develar y 
        guarda el mensaje decodificado en el archivo 
        con el nombre indicado por la entrada.

        Parametros:
        arr -- la entrada con los argumentos recibidos

        """
        mensaje_dev = Develar.devela(arr[0])
        des = arr[1]
        if "." not in des: 
            des += ".txt" 
        else:
            des = "".join(arr[1].split(".")[0:-1]) + ".txt"
        arch_des = open(des, "w")             
        arch_des.write(mensaje_dev)
        arch_des.close()
        print ("Mensaje obtenido en: ", des)

if __name__ == "__main__":
    Inicio.verifica()