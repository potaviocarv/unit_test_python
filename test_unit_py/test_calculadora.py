
# test_calculadora.py

import unittest

from calculadora import dividir, multiplicar, somar, subtrair, potencia


class TestCalculadora(unittest.TestCase):
    """Classe de testes para as funções do arquivo calculadora.py."""

    def test_somar(self):
        """Testa se a função somar está funcionando corretamente."""
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(0, 0), 0)

    def test_subtrair(self):
        """Testa se a função subtrair está funcionando corretamente."""
        self.assertEqual(subtrair(10, 5), 5)
        self.assertEqual(subtrair(5, 10), -5)
        self.assertEqual(subtrair(0, 0), 0)

    def test_multiplicar(self):
        """Testa se a função multiplicar está funcionando corretamente."""
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(5, 0), 0)
        self.assertEqual(multiplicar(-2, 3), -6)

    def test_dividir(self):
        """Testa se a função dividir está funcionando corretamente."""
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(9, 3), 3)
        self.assertEqual(dividir(5, 2), 2.5)

    def test_dividir_por_zero(self):
        """Testa se a divisão por zero gera erro."""
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

    def test_potencia(self):
        """Testa se a função potencia está funcionando corretamente."""
        self.assertEqual(potencia(2, 3), 8)
        self.assertEqual(potencia(5, 0), 1)
        self.assertEqual(potencia(10, 2), 100)

    def test_potencia_expoente_negativo(self):
        """Expoente negativo deve gerar o inverso da potência."""
        self.assertAlmostEqual(potencia(2, -2), 0.25)

    def test_potencia_base_negativo_impar(self):
        """Base negativa com expoente ímpar resulta em negativo."""
        self.assertEqual(potencia(-2, 3), -8)

    def test_potencia_base_negativo_par(self):
        """Base negativa com expoente par resulta em positivo."""
        self.assertEqual(potencia(-2, 2), 4)

    def test_potencia_expoente_fracionario(self):
        """Expoente fracionário (raiz) retorna float esperado."""
        self.assertAlmostEqual(potencia(9, 0.5), 3.0)

    def test_potencia_tipo_invalido(self):
        """Entrada com tipo inválido deve levantar TypeError."""
        with self.assertRaises(TypeError):
            potencia('a', 2)


if __name__ == "__main__":
    unittest.main()
