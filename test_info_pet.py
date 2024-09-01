import unittest
from unittest.mock import patch
from io import StringIO
from info_pet import coletar_informacoes_pet

class TestColetarInformacoesPet(unittest.TestCase):
    @patch("builtins.input", side_effect=["Rex", "3", "7"])
    def test_coleta_informacoes(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            coletar_informacoes_pet()

        expected_output = (
            "Por favor, insira as informações sobre seu pet.\n"
            "Nome do pet: Rex\n"
            "Idade do pet (em anos): 3\n"
            "Peso do pet (em kg): 7\n"
            "\nInformações do pet:\n"
            "Nome: Rex\n"
            "Idade: 3 anos\n"
            "Peso: 7.0 kg\n"
        )

if __name__ == "__main__":
    unittest.main()
