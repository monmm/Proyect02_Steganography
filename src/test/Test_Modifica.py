import unittest
from sys import path
path.append("../..")
from src.main.myp.modifica import Modifica

bin = "1000111 1000110 1000111"

class TestModifica(unittest.TestCase):
    
    def test_strToBinary(self):
         """Test para el texto transformado a su equivalente binario.

         Verificamos que nuestra función funcione de manera correcta.

         """
         self.assertEqual(Modifica.strToBinary("GFG"), bin)

    def test_isASCII(self):
         """Test para el texto transformado a su equivalente en ASCII.
         
         Verificamos que el valor de cada palabra en nuestro texto 
         se mantenga entre 32 y 127.

         """
         self.assertTrue(Modifica.isASCII("GFG"))
         self.assertFalse(Modifica.isASCII("♥O◘♦♥O◘♦"))

    if __name__ == "__main__":
        unittest.main()