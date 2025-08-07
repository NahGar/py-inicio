import unittest
import Cambia_texto

class ProbarCambiaTexto(unittest.TestCase):

    # el nombre debe comenzar con test
    def test_mayusculas(self):
        palabra = "hola comO estáS"
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado,"HOLA COMO ESTÁS")

    def test_primera_letra_mayusculas(self):
        palabra = "hola comO estáS"
        resultado = cambia_texto.primera_letra_mayusculas(palabra)
        self.assertEqual(resultado, "Hola Como Estás")

if __name__ == '__main__':
    unittest.main()
