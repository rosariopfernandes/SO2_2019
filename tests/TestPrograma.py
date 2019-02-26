import unittest
from Programa import Programa


class TestPrograma(unittest.TestCase):

    def test_can_generate_list(self):
        processos = Programa().gerar_lista_processos(5)
        self.assertIsInstance(processos, list)

    def test_generates_list_with_specified_size(self):
        processos = Programa().gerar_lista_processos(20)
        self.assertEqual(20, len(processos))

    def test_processes_are_not_null(self):
        processos = Programa().gerar_lista_processos(10)
        for processo in processos:
            self.assertNotEqual(processo, None)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
