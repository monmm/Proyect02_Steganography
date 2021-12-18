import cv2
from PIL import Image
import numpy as np

def decrypt():
    # load the image and convert it into a numpy array and display on the GUI.
    load = Image.open("src/test/data/msg.png")
    #load.thumbnail(image_display_size, Image.ANTIALIAS)
    load = np.asarray(load)
    load = Image.fromarray(np.uint8(load))
    #render = ImageTk.PhotoImage(load)
    #img = Label(app, image=render)
    #img.image = render
    #img.place(x=100, y=50)

    # Algorithm to decrypt the data from the image
    img = cv2.imread("src/test/data/msg.png")
    data = []
    stop = False
    for index_i, i in enumerate(img):
        i.tolist()
        for index_j, j in enumerate(i):
            if((index_j) % 3 == 2):
                # first pixel
                data.append(bin(j[0])[-1])
                # second pixel
                data.append(bin(j[1])[-1])
                # third pixel
                if(bin(j[2])[-1] == '1'):
                    stop = True
                    break
            else:
                # first pixel
                data.append(bin(j[0])[-1])
                # second pixel
                data.append(bin(j[1])[-1])
                # third pixel
                data.append(bin(j[2])[-1])
        if(stop):
            break

    message = []
    # join all the bits to form letters (ASCII Representation)
    for i in range(int((len(data)+1)/8)):
        message.append(data[i*8:(i*8+8)])
    # join all the letters to form the message.
    message = [chr(int(''.join(i), 2)) for i in message]
    message = ''.join(message)
    print(message)

if __name__ == "__main__":
    decrypt()