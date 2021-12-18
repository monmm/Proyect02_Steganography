from PIL import Image

class Codificar:

    def codifica(img, msg, des):
        imagen = Image.open(img, 'r')

        if (len(msg) == 0):
            raise ValueError('Introduce un mensaje válido')
    
        img_mod = imagen.copy()
        n = img_mod.size[0]
        (x, y) = (0, 0)
 
        for pixel in Codificar.modifica(img_mod.getdata(), msg): 
            img_mod.putpixel((x, y), pixel)
            if (x == n - 1):
                x = 0
                y += 1
            else:
                x += 1

        Codificar.guardaImg(img_mod, des)
 

    def guardaImg(img_mod, des):
        img_mod.save(des, str(des.split(".")[1].upper()))

    # Convert encoding data into 8-bit binary
    # form using ASCII value of characters
    def repUnicode(data):
        data = []
        for i in data:
            data.append(format(ord(i), '08b'))
        return data
 
    # Pixels are modified according to the
    # 8-bit binary data and finally returned
    def modifica(pix, data):
        datalist = Codificar.repUnicode(data)
        lendata = len(datalist)
        imdata = iter(pix)
 
        for i in range(lendata):
 
        # Extracting 3 pixels at a time
            pix = [value for value in imdata.__next__()[:3] +
                                imdata.__next__()[:3] +
                                imdata.__next__()[:3]]
 
        # Pixel value should be made
        # odd for 1 and even for 0
            for j in range(0, 8):
                if (datalist[i][j] == '0' and pix[j]% 2 != 0):
                    pix[j] -= 1
 
                elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                    if(pix[j] != 0):
                        pix[j] -= 1
                    else:
                        pix[j] += 1
                        # pix[j] -= 1
 
        # Eighth pixel of every set tells
        # whether to stop ot read further.
        # 0 means keep reading; 1 means thec
        # message is over.
            if (i == lendata - 1):
                if (pix[-1] % 2 == 0):
                    if(pix[-1] != 0):
                        pix[-1] -= 1
                    else:
                        pix[-1] += 1
 
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1
 
            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]