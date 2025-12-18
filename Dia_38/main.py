# ==================================================== #
# -------------Testes unitários básicos--------------- #
# Escreva testes para funções simples usando unittest. #
# ==================================================== #

import unittest


def soma(a, b):
    return a + b


def eh_par(numero):
    return numero % 2 == 0


class TestFuncoesSimples(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(0, 0), 0)

    def test_eh_par(self):
        self.assertTrue(eh_par(4))
        self.assertFalse(eh_par(5))
        self.assertTrue(eh_par(0))


if __name__ == "__main__":
    unittest.main()

# ================================= #
# Para rodar: python -m Dia_38.main #
# ================================= #
