import unittest
from Maestro import Maestro
from Programa import Programa


class TestMaestro(unittest.TestCase):

    def test_can_get_formatted_process_list(self):
        lista = Programa().gerar_lista_processos(5)
        output = Maestro().__get_formatted_process_list__(lista)
        print(output)

    def test_can_write_file(self):
        maestro = Maestro()
        content = "hello world"
        filename = maestro.__write_file__(content)
        written_file = open(filename, "r")
        line = written_file.readline()
        written_file.close()
        self.assertEqual(line, content)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
