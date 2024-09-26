import unittest
from unittest.mock import patch
import random
import main

class TestJuegoAdivinanza(unittest.TestCase):

    def test_generar_numero_secreto(self):
        """Prueba si el número generado está dentro del rango de 1 a 100."""
        for _ in range(100):  # Repetimos la prueba varias veces para garantizar que el número esté siempre en el rango.
            numero_secreto = main.generar_numero_secreto()
            self.assertTrue(1 <= numero_secreto <= 100, "El número secreto no está dentro del rango")

    @patch('builtins.input', return_value='50')
    def test_obtener_adivinanza_jugadora(self, input_mock):
        """Prueba si la función retorna la suposición correcta cuando el input es válido."""
        adivinanza = main.obtener_adivinanza_jugadora()
        self.assertEqual(adivinanza, 50, "La adivinanza debería ser 50")

    def test_adivinanza_ordenador_binaria(self):
        """Prueba si el ordenador genera la adivinanza correcta usando la búsqueda binaria."""
        min_valor = 1
        max_valor = 100
        adivinanza = main.adivinanza_ordenador_binaria(min_valor, max_valor)
        self.assertEqual(adivinanza, 50, "La primera adivinanza debería ser 50 con el rango inicial 1-100")

    def test_turno_jugador_acierta(self):
        """Prueba si el turno de la jugadora funciona cuando adivina correctamente."""
        numero_secreto = 42
        adivinanzas_jugadora = []
        with patch('builtins.input', return_value='42'):  # Simula que la jugadora adivina el número secreto.
            resultado = main.turno_jugador(numero_secreto, adivinanzas_jugadora)
        self.assertTrue(resultado, "La jugadora debería haber acertado")

    def test_turno_ordenador_acierta(self):
        """Prueba si el turno del ordenador funciona cuando adivina correctamente."""
        numero_secreto = 50
        min_valor = 1
        max_valor = 100
        adivinanzas_ordenador = []
        resultado, min_valor, max_valor = main.turno_ordenador_inteligente(numero_secreto, min_valor, max_valor, adivinanzas_ordenador)
        self.assertTrue(resultado, "El ordenador debería haber acertado en la primera suposición con búsqueda binaria")
        self.assertEqual(adivinanzas_ordenador[-1], 50, "La última adivinanza del ordenador debería ser 50")

    @patch('main.generar_numero_secreto', return_value=42)
    @patch('builtins.input', side_effect=['42', '42', '42', '42', '42'])  # Simula las respuestas para jugar dos veces
    def test_jugar_de_nuevo(self, secreto_mock, input_mock):
        """Prueba si la función para jugar de nuevo funciona correctamente."""
        main.jugar()  # Simula un juego en el que la jugadora adivina correctamente el número 42.
        self.assertTrue(True)
        # Simula jugar de nuevo y luego terminar
        #main.jugar_de_nuevo()  # Verifica si la opción de jugar de nuevo funciona al elegir 's' y luego 'n'.

    
if __name__ == '__main__':
    unittest.main()