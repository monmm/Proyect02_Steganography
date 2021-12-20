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
        Obtiene la representación ASCII del mensaje oculto.

        Obtiene el valor de cada byte y regresa el mensaje 
        original sin el caracter final.

        Parametros:
        cadena_bin -- cadena binaria a convertir
        
        """
        cad_dev = ""
        caracter_final = "========"
        lista_bytes = [cadena_bin[i:i+8] for i in range(0, len(cadena_bin), 8)]

        for byte in lista_bytes:
            cad_dev += ''.join(chr(int(byte, 2)))
            if cad_dev[-8:] == caracter_final:
                break
        return cad_dev[:-8]        

    def devela(imagen):
        """
        Decodifica la imagen recibida.

        Después de leer la imagen, lee el bit menos 
        significativo de cada canal concatenando su 
        representación binaria para después
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

