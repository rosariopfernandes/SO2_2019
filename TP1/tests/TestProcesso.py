import unittest
from TP1.Processo import Processo


class TestProcesso(unittest.TestCase):
    def test_can_create_processo(self):
        processo = Processo()
        self.assertNotEqual(processo, None)

    # alínea a)
    def test_pid_is_unique(self):
        processo1 = Processo()
        processo2 = Processo()
        processo3 = Processo()
        self.assertNotEqual(processo1.pid, processo2.pid)
        self.assertNotEqual(processo2.pid, processo3.pid)
        self.assertNotEqual(processo1.pid, processo3.pid)

    # alínea b)
    def test_chegada_and_duracao_less_than_ten(self):
        processo = Processo()
        self.assertLess(processo.chegada, 10)
        self.assertLess(processo.duracao, 10)

    # alínea d)
    def test_getters(self):
        processo = Processo()
        self.assertEqual(processo.pid, processo.get_id())
        self.assertEqual(processo.chegada, processo.get_chegada())
        self.assertEqual(processo.duracao, processo.get_duracao())
        self.assertEqual(processo.tempo_espera, processo.get_tempo_espera())
        self.assertEqual(processo.tempo_resposta, processo.get_tempo_resposta())

    def test_setters(self):
        processo = Processo()
        processo.set_id(1)
        processo.set_chegada(2)
        processo.set_duracao(3)
        processo.set_tempo_espera(4)
        processo.set_tempo_resposta(5)
        self.assertEqual(processo.pid, 1)
        self.assertEqual(processo.chegada, 2)
        self.assertEqual(processo.duracao, 3)
        self.assertEqual(processo.tempo_espera, 4)
        self.assertEqual(processo.tempo_resposta, 5)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
