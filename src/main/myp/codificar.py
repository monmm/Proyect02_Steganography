# Usamos cv2 para leer y transformar nuestras imagenes con facilidad
import cv2

class Codificar:    
    
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

    def decABin(cadena):
        """
        Convierte una cadena de texto en su representación binaria.

        Parametros:
        cadena -- cadena a convertir

        """        
        return ''.join([format(ord(i), "08b") for i in cadena])       

    def codifica(imagen, mensaje, destino):
        """
        Codifica el mensaje y la imagen recibida 
        guardando todo en un archivo con el nombre de destino.

        Después de leer la imagen, toma el mensaje a 
        ocultar y le concatena un caracter final para 
        saber donde termina, luego modifica el bit menos 
        significativo de cada canal de acuerdo con el texto
        que se quiere ocultar y crea o sobreescribe la 
        imagen de destino con el mensaje oculto.

        Parametros:
        imagen -- imagen de origen
        mensaje -- mensaje a ocultar
        destino -- nombre de la imagen donde se guardará 
                   el texto codificado

        Excepciones:
        ValueError -- Si el mensaje no cabe en la imagen

        """
        img_pixeles = Codificar.leeImg(imagen).copy()
        caracter_final = "#END#"
        mensaje += caracter_final
        mensaje_bin = Codificar.decABin(mensaje)

        canalR = img_pixeles[:,:,0]
        canalG = img_pixeles[:,:,1]
        canalB = img_pixeles[:,:,2]
        canalA = img_pixeles[:,:,3]
        
        capacidad = img_pixeles.shape[0]*img_pixeles.shape[1]*3//8
        if (len(mensaje) > capacidad):
            raise ValueError("No hay suficiente espacio en la imagen")

        ancho, alto, dim = img_pixeles.shape
        m_long = len(mensaje_bin)

        for i in range(0, m_long):
            for x in range(0, ancho):
                for y in range(0, alto):
                    if i >= m_long:
                        break
                    canalR[x,y] = int((f'{canalR[x,y]:08b}'[:-1] + mensaje_bin[i]), 2)
                    canalG[x,y] = int((f'{canalG[x,y]:08b}'[:-1] + mensaje_bin[i+1]), 2)
                    canalB[x,y] = int((f'{canalB[x,y]:08b}'[:-1] + mensaje_bin[i+2]), 2)
                    canalA[x,y] = int((f'{canalA[x,y]:08b}'[:-1] + mensaje_bin[i+3]), 2)                    
                    i += 4
                break
            break
        if "." not in destino: 
            destino += ".png" 
        else:
            destino = "".join(destino.split(".")[0:-1]) + ".png"
        cv2.imwrite(destino, img_pixeles)
        print ("Imagen codificada exitosamente: ", destino)