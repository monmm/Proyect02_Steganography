import unittest
from sys import path
path.append("../..")
from src.main.myp.develar import Develar

class TestDevelar(unittest.TestCase):

    img = "src/test/data/neon_rosa.jpg"
    bin = "01000000"
    
    def test_setData(self):
        """
        Test cuando develamos una imágen.

        Verificamos que funcione correctamente comparando 
        el mensaje obtenido con el mensaje que se oculto originalmente.
        Excepciones a verificar:
        SystemExit
    
        """         
        self.assertEqual(Develar.decodifica(self.img), "Ä")
    
    def test_binADec(self):
        """
        Test para transformar de binario a decimal.
        """
        self.assertEqual(Develar.binADec(self.bin), 64)

    def test_repAscii(self):
        """
        Test para transformar de decimal a ASCII.
        """
        self.assertEqual(Develar.repAscii(64), "@")

    if __name__ == "__main__":
        unittest.main()