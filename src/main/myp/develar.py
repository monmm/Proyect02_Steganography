import sys
from PIL import Image
import cv2
import stepic


class Develar:
    
    def leeImg(img):
        pixeles = cv2.imread(img)
        #pixeles = cv2.imread(img, cv2.IMREAD_UNCHANGED)
        if pixeles.shape[2] < 4:
            pixeles = cv2.cvtColor(pixeles, cv2.COLOR_BGR2BGRA)
            pixeles[:,:,3] = 254
            return pixeles

    def binario_a_ascii(binario):
        # Convertir binario a decimal
        valor = int(binario, 2)
        # Convertir el decimal a su representación ASCII
        return chr(valor)

    def binario_a_texto(texto_binario):
        texto_plano = ""
        for binario in texto_binario.split(" "):
            texto_plano += Develar.binario_a_ascii(binario)
        return texto_plano

    def decode_binary_string(s):
        return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

    def decodifica(image_pixels):
        cadena = ""
        r = image_pixels[:,:,0]
        g = image_pixels[:,:,1]
        b = image_pixels[:,:,2]
        a = image_pixels[:,:,3]

        w, h, z = image_pixels.shape

        for x in range(0, w):
            for y in range(0, h):
                cadena += f'{r[x,y]:08b}'[7]
                cadena += f'{g[x,y]:08b}'[7]
                cadena += f'{b[x,y]:08b}'[7]
                cadena += f'{a[x,y]:08b}'[7]
            break
        print(Develar.decode_binary_string(cadena))
        print(Develar.binario_a_texto(cadena))
        #print(cadena)

if __name__ == "__main__":
    img = Develar.leeImg("salida2.png")
    print(Develar.decodifica(img))

