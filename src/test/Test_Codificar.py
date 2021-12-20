import unittest
from sys import path
path.append("../..")
from src.main.myp.codificar import Codificar

import cv2
from unidecode import unidecode

class TestCodificar(unittest.TestCase):

    binario = "010001110100011001000111"
    img = "src/test/data/prueba.png"
    origen = "src/test/data/neon_rosa.jpg"
    texto = "src/test/data/prueba.txt"
    arch_or = open(texto, 'r')
    msj = arch_or.read()
    arch_or.close()
    mensaje = unidecode(msj)

    def test_decABin(self):
        """
        Verifica que se obtenga la representación binadria 
        de una cadena de manera correcta.

        Compara el la represetación con la cadena binaria esperada.

        """
        self.assertEqual(Codificar.decABin("GFG"), self.binario)

    def test_codifica(self):
        """        
        Verifica que el codificado funcione correctamente.
        
        Manda a codificar una imagen con un texto predeterminado y 
        compara la lista de los pixeles de esta con una imagen 
        previamente codificada.
    
        """        
        arr1 = cv2.imread(self.img, cv2.IMREAD_UNCHANGED)
        
        img_des = "src/test/data/prueba2.png"
        Codificar.codifica(self.origen, self.mensaje, img_des)
        arr2 = cv2.imread(img_des, cv2.IMREAD_UNCHANGED)
        
        self.assertTrue((arr1 == arr2).all())
        
     
if __name__ == "__main__":
    unittest.main()