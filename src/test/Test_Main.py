import unittest
from sys import path
path.append("../..")
from main.myp.main import Main

class TestMain(unittest.TestCase):
    
    def test_setData(self):
        """Test para los datos recibidos.
        Verificamos que se lance la excepción correspondiente 
        con archivos inexistentes,    
        cuando la imagen a codificar o develar no existe,
        cuando el archivo de texto a ocultar no existe,        
        cuando no tenemos las banderas en el orden adecuado.
        Excepciones a verificar:
        SystemExit
    
        """         
        with self.assertRaises(SystemExit) as exception_info:
            Main.setData(self.text)
        self.assertEqual ("Algo salió mal con el archivo", str(exception_info.exception))
        with self.assertRaises(SystemExit) as exception_info:
            Main.setData(self.img)
        self.assertEqual ("Algo salió mal con el archivo", str(exception_info.exception))

    if __name__ == "__main__":
        unittest.main()