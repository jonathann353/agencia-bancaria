class Cliente:
    """Classe que representa um cliente do banco."""
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Conta:
    """Classe que representa uma conta bancária."""
    def __init__(self, numero, cliente, saldo=0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def transferir(self, valor, conta_destino):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            conta_destino.depositar(valor)
            print(f"Transferência de R${valor} para a conta {conta_destino.numero} realizada com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

class Banco:
    """Classe que gerencia clientes e contas bancárias."""
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def criar_cliente(self, nome, cpf):
        cliente = Cliente(nome, cpf)
        self.clientes.append(cliente)
        print(f"Cliente {nome} criado com sucesso.")
        return cliente

    def criar_conta(self, numero, cliente):
        if cliente in self.clientes:
            conta = Conta(numero, cliente)
            self.contas.append(conta)
            print(f"Conta {numero} criada com sucesso para o cliente {cliente.nome}.")
            return conta
        else:
            print("Cliente não encontrado.")
            return None

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        print("Conta não encontrada.")
        return None

# Simulação de uma agência bancária

banco = Banco("Banco Python")

# Criar clientes
cliente1 = banco.criar_cliente("João Silva", "111.111.111-11")
cliente2 = banco.criar_cliente("Maria Souza", "222.222.222-22")

# Criar contas para os clientes
conta1 = banco.criar_conta("12345", cliente1)
conta2 = banco.criar_conta("67890", cliente2)

# Operações bancárias
conta1.depositar(1000)
conta1.exibir_saldo()

conta1.sacar(200)
conta1.exibir_saldo()

conta1.transferir(300, conta2)
conta1.exibir_saldo()
conta2.exibir_saldo()

conta2.sacar(100)
conta2.exibir_saldo()
