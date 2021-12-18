import unittest
from sys import path
path.append("../..")
from src.main.myp.develar import Develar

class TestDevelar(unittest.TestCase):

    img = "src/test/data/msg.png"
    msg = "Probando el segundo metodo"
    
    def test_setData(self):
        """
        Test cuando develamos una imagen.

        Verificamos que funcione correctamente comparando 
        el mensaje obtenido con el mensaje que se oculto originalmente.
        Excepciones a verificar:
        SystemExit
    
        """         
        self.assertEqual(Develar.decodifica(self.img), self.msg)

    if __name__ == "__main__":
        unittest.main()