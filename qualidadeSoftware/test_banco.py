import unittest
from agencia_bancaria import Cliente, Conta, Banco

class TestBanco(unittest.TestCase):
    
    def setUp(self):
        """Configura o ambiente para os testes"""
        self.banco = Banco("Banco Teste")
        self.cliente1 = self.banco.criar_cliente("João Silva", "111.111.111-11")
        self.cliente2 = self.banco.criar_cliente("Maria Souza", "222.222.222-22")
        self.conta1 = self.banco.criar_conta("12345", self.cliente1)
        self.conta2 = self.banco.criar_conta("67890", self.cliente2)
    
    def test_deposito(self):
        """Teste para verificar se o depósito aumenta o saldo corretamente"""
        self.conta1.depositar(500)
        self.assertEqual(self.conta1.saldo, 500)
    
    def test_saque(self):
        """Teste para verificar se o saque diminui o saldo e impede saques além do saldo"""
        self.conta1.depositar(300)
        self.conta1.sacar(100)
        self.assertEqual(self.conta1.saldo, 200)

        # Tentativa de sacar mais do que o saldo disponível
        self.conta1.sacar(500)
        self.assertEqual(self.conta1.saldo, 200)  # Saldo não deve mudar
    
    def test_transferencia(self):
        """Teste para verificar se a transferência entre contas funciona corretamente"""
        self.conta1.depositar(1000)
        self.conta1.transferir(300, self.conta2)
        
        self.assertEqual(self.conta1.saldo, 700)
        self.assertEqual(self.conta2.saldo, 300)
    
    def test_saldo_inicial(self):
        """Teste para verificar se o saldo inicial da conta é zero"""
        self.assertEqual(self.conta1.saldo, 0)
        self.assertEqual(self.conta2.saldo, 0)

if __name__ == "__main__":
    unittest.main()
