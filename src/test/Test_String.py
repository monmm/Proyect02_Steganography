import unittest
from sys import path
path.append("../..")
from src.main.myp.string import String

bin = "1000111 1000110 1000111"

class TestString(unittest.TestCase):
    
    def test_strToBinary(self):
         """Test para el texto transformado a su equivalente binario.

         Verificamos que nuestra función funcione de manera correcta.

         """
         self.assertEqual(String.strToBinary("GFG"), bin)

    def test_isASCII(self):
         """Test para el texto transformado a su equivalente en ASCII.
         
         Verificamos que el valor de cada palabra en nuestro texto 
         se mantenga entre 32 y 127.

         """
         self.assertTrue(String.isASCII("GFG"))
         self.assertFalse(String.isASCII("♥O◘♦♥O◘♦"))

    if __name__ == "__main__":
        unittest.main()