import unittest
from sys import path
path.append("../..")
from src.main.myp.uso import Uso

class TestUso(unittest.TestCase):

    archivo = "src/test/data/msg.txt"
    imagen = "src/test/data/heart.png"
    destino_u = "final.txt"
    destino_h = "cript.png"
    doc = "Ocultar: h texto_ocultar imagen_ocultar nombre_destino \n" 
    doc += "Develar: u imagen_develar nombre_destino"
    
    def test_verificaOcultar(self):
        """Test para los datos recibidos.
        Verificamos que se lance la excepción correspondiente 
        con archivos inexistentes,    
        cuando la imagen a codificar o develar no existe,
        cuando el archivo de texto a ocultar no existe,        
        cuando no tenemos las banderas o el orden adecuado.
        Excepciones a verificar:
        SystemExit
    
        """                 
        with self.assertRaises(SystemExit) as exception_info:
            Uso.verificaOcultar([self.archivo, self.destino_h, self.imagen])
        self.assertEqual (self.doc, str(exception_info.exception))
        with self.assertRaises(SystemExit) as exception_info:
            Uso.verificaDevelar([self.destino_h, self.destino_u])
        self.assertEqual (self.doc, str(exception_info.exception))

    if __name__ == "__main__":
        unittest.main()