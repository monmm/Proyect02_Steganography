from PIL import Image
import cv2
import stepic

from develar import Develar

class Codificar:

    def decABin(cadena):
        mensaje = ''.join([format(ord(i), "08b") for i in cadena])
        return mensaje
    
    def leeImg(img):
        pixeles = cv2.imread(img)
        if pixeles.shape[2] < 4:
            pixeles = cv2.cvtColor(pixeles, cv2.COLOR_BGR2BGRA)
            pixeles[:,:,3] = 254
            return pixeles

    def encode(image_pixels, bin_message):
        width, height, dim = image_pixels.shape
        cont = 0
        r = image_pixels[:,:,0]
        g = image_pixels[:,:,1]
        b = image_pixels[:,:,2]
        a = image_pixels[:,:,3]

        w, h, z = image_pixels.shape

        m_len = len(bin_message)

        for c in range(0, m_len):
            for x in range(0, w):
                for y in range(0, h):
                    if c == m_len:
                        break
                    r[x,y] = f'{r[x,y]:08b}'[:7] + bin_message[c]
                    g[x,y] = f'{g[x,y]:08b}'[:7] + bin_message[c+1]
                    b[x,y] = f'{b[x,y]:08b}'[:7] + bin_message[c+2]
                    a[x,y] = f'{a[x,y]:08b}'[:7] + bin_message[c+3]
                    c += 4
                break
            break
        cv2.imwrite("salida2.png", image_pixels)

    def get_image(image_location):
        img = cv2.imread(image_location)
        return img
    
    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    def decode_image(img_loc):
        img = Codificar.get_image(img_loc)
        pattern = Codificar.gcd(len(img), len(img[0]))
        message = ''
        for i in range(len(img)):
            for j in range(len(img[0])):
                if (i-1 * j-1) % pattern == 0:
                    if img[i-1][j-1][0] != 0:
                        message = message + chr(img[i-1][j-1][0])
                    else:
                        return message

if __name__ == "__main__":
    img = Codificar.leeImg("newxd.jpg")
    msg = Codificar.decABin("HOLAMONICAXD")
    Codificar.encode(img, msg)
    im1 = Image.open('salida2.png').convert(mode='RGB')
    s = stepic.decode(im1)
    print (s)
    #data = s.decode()
    #print (data)