import unittest
from sys import path
path.append("../..")
from src.main.myp.esteganografia import Inicio

class TestEsteganografia(unittest.TestCase):

    archivo = "src/test/data/msg.txt"
    imagen = "src/test/data/neon_rosa.jpg"
    destino_u = "final.txt"
    destino_h = "cript.png"
    doc = "Ocultar: h texto_ocultar imagen_ocultar nombre_destino \n" 
    doc += "Develar: u imagen_develar nombre_destino"
    
    def test_verificaOcultar(self):
        """
        Test para los agumentos recibidos para h.
        Verificamos que se imprima el modo de uso 
        con archivos inexistentes,    
        cuando la imagen a codificar no existe,
        cuando el archivo de texto a ocultar no existe.
        Excepciones a verificar:
        SystemExit
    
        """                 
        with self.assertRaises(SystemExit) as exception_info:
            Inicio.verificaOcultar([self.archivo, self.destino_h, self.imagen])
        self.assertEqual(self.doc, str(exception_info.exception))
    
    def test_verificaDevelar(self):
        """
        Test para los agumentos recibidos para u.
        Verificamos que se imprima el modo de uso            
        cuando la imagen a develar no existe.
        Excepciones a verificar:
        SystemExit
    
        """
        with self.assertRaises(SystemExit) as exception_info:
            Inicio.verificaDevelar([self.destino_h, self.destino_u])
        self.assertEqual(self.doc, str(exception_info.exception))

    if __name__ == "__main__":
        unittest.main()