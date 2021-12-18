from PIL import Image


class Develar:
    
    def decodifica(img):
        """
        Lee la imágen obteniendo el LSB de cada nivel. 
        
        Toma los datos de la imágen extrayendo los valores 
        de cada 3 bytes (donde cada byte corresponde al canal RGB) 
        y pasando a su representación decimal para obtener 
        el mensaje codificado. Así recorre la imágen hasta que 
        el último valor sea impar y el mensaje haya terminado.
        """
        img = Image.open(img, 'r')
        mensaje = ''
        datos = iter(img.getdata())
        # Tomamos tres pixeles a la vez
        while (True):
            pixels = [valor for valor in datos.__next__()[:3] +
                                datos.__next__()[:3] + 
                                datos.__next__()[:3]]

            # Obtenemos la representación binaria del mensaje oculto.
            rep_bin = ''
            for lsb in pixels[:8]:
                if (lsb % 2 == 0):
                    rep_bin += '0'
                else:
                    rep_bin += '1'
 
            mensaje += Develar.repAscii(Develar.binADec(rep_bin))
            # Fin del mensaje, el último valor es impar.
            if (pixels[-1] % 2 != 0):
                return mensaje
                
    def binADec(rep_bin):
        """
        Transforma un byte a su representación decimal.

        """
        return int(rep_bin, 2)
    
    def repAscii(rep_dec):
        """
        Obtiene caracteres a partir de su código ASCII.

        """
        return chr(rep_dec)
