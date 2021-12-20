# Usamos cv2 para leer y transformar nuestras imagenes con facilidad
import cv2

class Develar:

    def leeImg(archivo_img):
        """
        Lee la imagen recibida.
        
        Añade un canal alfa si la imagen no lo contenía 
        y regresa la matriz con los pixeles de esta.

        Parametros:
        archivo_img -- la imagen a codificar

        """
        pixeles = cv2.imread(archivo_img, cv2.IMREAD_UNCHANGED)
        if pixeles.shape[2] < 4:
            pixeles = cv2.cvtColor(pixeles, cv2.COLOR_RGB2RGBA)
        return pixeles

    def decodificaBin(cadena_bin):
        """
        Regresa el mensaje original.

        Obtiene valor de cada byte y la representación 
        ASCII del mensaje oculto regresandolo sin el caracter final.

        Parametros:
        cadena_bin -- cadena binaria a convertir
        
        """
        cadena = ''.join(chr(int(cadena_bin[i*8:i*8+8],2)) for i in range(len(cadena_bin)//8))
        ind = cadena.find("#END#")
        if (ind == -1):
            ind = cadena.find("#")
            if (ind == -1):
                return ""
        cad_dev = cadena[:ind]      
        return cad_dev

    def devela(imagen):
        """
        Decodifica la imagen recibida.

        Después de leer la imagen, lee el bit menos 
        significativo de cada canal obteniendo la 
        representación binaria del mensaje para después
        obtener su representación en codigo ASCII.

        Parametros:
        imagen -- imagen a develar

        """
        img_pixeles = Develar.leeImg(imagen)        
        cadena = ""

        canalR = img_pixeles[:,:,0]
        canalG = img_pixeles[:,:,1]
        canalB = img_pixeles[:,:,2]
        canalA = img_pixeles[:,:,3]

        ancho, alto, dim = img_pixeles.shape

        for x in range(0, ancho):
            for y in range(0, alto):
                    cadena += f'{canalR[x,y]:08b}'[-1]
                    cadena += f'{canalG[x,y]:08b}'[-1]
                    cadena += f'{canalB[x,y]:08b}'[-1]                
                    cadena += f'{canalA[x,y]:08b}'[-1]                
        return Develar.decodificaBin(cadena)  

