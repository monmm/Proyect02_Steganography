import unittest
from sys import path
path.append("../..")
from src.main.myp.codificar import Codificar

import numpy as np
import cv2

bin = "100011110001101000111"
binario = "010001110100011001000111"
img = "src/test/data/prueba.png"
pix = cv2.imread(img, cv2.IMREAD_UNCHANGED)
msg = "src/test/data/prueba.txt"

class TestCodificar(unittest.TestCase):

    def test_decABin(self):
        self.assertEqual(Codificar.decABin("GFG"), binario)

    def test_codifica(self):
        pass
        #img_des = "src/test/data/prueba2.png"
        #Codificar.codifica(img, msg, img_des)
        #pixeles = cv2.imread(img_des, cv2.IMREAD_UNCHANGED)
        #self.assertTrue(pixeles == pix)
        
     
if __name__ == "__main__":
    unittest.main()