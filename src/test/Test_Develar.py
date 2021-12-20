import unittest
from sys import path
path.append("../..")
from src.main.myp.codificar import Codificar
from src.main.myp.develar import Develar

class TestDevelar(unittest.TestCase):

    img = "src/test/data/prueba.png"
    msg = "Probando el segundo metodo"
    cad_b = Codificar.decABin("GFG#END#")

    def test_decodificaBin(self):
        """
        Verifica que a partir de una cadena binaria 
        obtenemos la representación ASCII correctamente.

        Compara que su representacion sea la misma que el mensaje original.
        
        """
        self.assertEqual(Develar.decodificaBin(self.cad_b), "GFG")
    
    def test_devela(self):
        """        
        Verifica que el develado funcione correctamente.
        
        Compara el mensaje obtenido con el mensaje que se oculto originalmente.        
    
        """
        self.assertEqual(Develar.devela(self.img), self.msg)

    if __name__ == "__main__":
        unittest.main()