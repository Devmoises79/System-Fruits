import unittest
from frutas.py import autenticar_usuario  # exemplo de função que você cria para autenticar

class TestSystemFruits(unittest.TestCase):
    def test_autenticacao_valida(self):
        self.assertTrue(autenticar_usuario("Admin01", "Adm123"))
        self.assertTrue(autenticar_usuario("User01", "User123"))
        
    def test_autenticacao_invalida(self):
        self.assertFalse(autenticar_usuario("Admin01", "senhaErrada"))
        self.assertFalse(autenticar_usuario("OutroUsuario", "Adm123"))

if __name__ == '__main__':
    unittest.main()
