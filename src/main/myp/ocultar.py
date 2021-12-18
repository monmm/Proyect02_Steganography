import cv2

from PIL import Image
import stepic

def oculta(img, msg, des):
    im = Image.open (img)
    im2 = stepic.encode(im, msg)
    im2.save(des)

def readImage(imagePath):
    pixels = cv2.imread(imagePath)
    cv2.imwrite("newxd.jpg", pixels)
def main():
    readImage("src/test/data/msg.png")

def encrypt_data_into_image():
    # Step 2
    global path_image
    #data = txt.get(1.0, "end-1c")
    # load the image
    img = cv2.imread(path_image)
    # break the image into its character level. Represent the characyers in ASCII.
    data = [format(ord(i), '08b') for i in data]
    _, width, _ = img.shape
    # algorithm to encode the image
    PixReq = len(data) * 3

    RowReq = PixReq/width
    RowReq = math.ceil(RowReq)

    count = 0
    charCount = 0
    # Step 3
    for i in range(RowReq + 1):
        # Step 4
        while(count < width and charCount < len(data)):
            char = data[charCount]
            charCount += 1
            # Step 5
            for index_k, k in enumerate(char):
                if((k == '1' and img[i][count][index_k % 3] % 2 == 0) or (k == '0' and img[i][count][index_k % 3] % 2 == 1)):
                    img[i][count][index_k % 3] -= 1
                if(index_k % 3 == 2):
                    count += 1
                if(index_k == 7):
                    if(charCount*3 < PixReq and img[i][count][2] % 2 == 1):
                        img[i][count][2] -= 1
                    if(charCount*3 >= PixReq and img[i][count][2] % 2 == 0):
                        img[i][count][2] -= 1
                    count += 1
        count = 0
    # Step 6
    # Write the encrypted image into a new file
    cv2.imwrite("encrypted_image.png", img)

if __name__ == "__main__":
    main()