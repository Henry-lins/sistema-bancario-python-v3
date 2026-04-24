from abc import ABC, abstractmethod
from datetime import datetime


# ==================== INTERFACE / CLASSE ABSTRATA ====================

class Transacao(ABC):

    @property
    @abstractmethod
    def valor(self) -> float:
        pass

    @abstractmethod
    def registrar(self, conta: "Conta") -> None:
        pass


# ==================== TRANSAÇÕES ====================

class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self) -> float:
        return self._valor

    def registrar(self, conta: "Conta") -> None:
        sucesso = conta.depositar(self._valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self) -> float:
        return self._valor

    def registrar(self, conta: "Conta") -> None:
        sucesso = conta.sacar(self._valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)


# ==================== HISTÓRICO ====================

class Historico:
    def __init__(self):
        self._transacoes: list[dict] = []

    @property
    def transacoes(self) -> list:
        return self._transacoes

    def adicionar_transacao(self, transacao: Transacao) -> None:
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            }
        )


# ==================== CONTA ====================

class Conta:
    def __init__(self, numero: int, cliente: "Cliente"):
        self._saldo: float = 0.0
        self._numero: int = numero
        self._agencia: str = "0001"
        self._cliente: "Cliente" = cliente
        self._historico: Historico = Historico()

    @classmethod
    def nova_conta(cls, cliente: "Cliente", numero: int) -> "Conta":
        return cls(numero, cliente)

    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def agencia(self) -> str:
        return self._agencia

    @property
    def cliente(self) -> "Cliente":
        return self._cliente

    @property
    def historico(self) -> Historico:
        return self._historico

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            print("\n❌ Operação falhou! O valor do saque deve ser positivo.")
            return False
        if valor > self._saldo:
            print("\n❌ Operação falhou! Saldo insuficiente.")
            return False
        self._saldo -= valor
        print(f"\n✅ Saque de R$ {valor:.2f} realizado com sucesso!")
        return True

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            print("\n❌ Operação falhou! O valor do depósito deve ser positivo.")
            return False
        self._saldo += valor
        print(f"\n✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
        return True

    def __str__(self):
        return (
            f"\tAgência:\t{self.agencia}\n"
            f"\tC/C:\t\t{self.numero}\n"
            f"\tTitular:\t{self.cliente.nome}\n"
            f"\tSaldo:\t\tR$ {self.saldo:.2f}"
        )


class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente: "Cliente", limite: float = 500.0, limite_saques: int = 3):
        super().__init__(numero, cliente)
        self._limite: float = limite
        self._limite_saques: int = limite_saques

    @property
    def limite(self) -> float:
        return self._limite

    @property
    def limite_saques(self) -> int:
        return self._limite_saques

    def sacar(self, valor: float) -> bool:
        numero_saques = sum(
            1 for t in self.historico.transacoes if t["tipo"] == "Saque"
        )

        if valor > self._limite:
            print(f"\n❌ Operação falhou! O valor do saque excede o limite de R$ {self._limite:.2f}.")
            return False
        if numero_saques >= self._limite_saques:
            print(f"\n❌ Operação falhou! Número máximo de {self._limite_saques} saques diários atingido.")
            return False

        return super().sacar(valor)

    def __str__(self):
        return (
            f"\tAgência:\t{self.agencia}\n"
            f"\tC/C:\t\t{self.numero}\n"
            f"\tTitular:\t{self.cliente.nome}\n"
            f"\tSaldo:\t\tR$ {self.saldo:.2f}\n"
            f"\tLimite p/ saque:\tR$ {self.limite:.2f}\n"
             f"\tSaques restantes:\t{self.limite_saques - sum(1 for t in self.historico.transacoes if t['tipo'] == 'Saque')}"
        )


# ==================== CLIENTES ====================

class Cliente:
    def __init__(self, endereco: str):
        self._endereco: str = endereco
        self._contas: list[Conta] = []

    @property
    def endereco(self) -> str:
        return self._endereco

    @property
    def contas(self) -> list:
        return self._contas

    def realizar_transacao(self, conta: Conta, transacao: Transacao) -> None:
        transacao.registrar(conta)

    def adicionar_conta(self, conta: Conta) -> None:
        self._contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento: datetime, endereco: str):
        super().__init__(endereco)
        self._cpf: str = cpf
        self._nome: str = nome
        self._data_nascimento: datetime = data_nascimento

    @property
    def cpf(self) -> str:
        return self._cpf

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def data_nascimento(self) -> datetime:
        return self._data_nascimento


# ==================== HELPERS DO MENU ====================

def filtrar_cliente(cpf: str, clientes: list) -> Cliente | None:
    for cliente in clientes:
        if isinstance(cliente, PessoaFisica) and cliente.cpf == cpf:
            return cliente
    return None

def selecionar_conta(cliente: Cliente) -> Conta | None:
    
    if not cliente.contas:
        print("\n❌ Cliente não possui contas cadastradas.")
        return None
 
    if len(cliente.contas) == 1:
        return cliente.contas[0]
 
    print("\nContas disponíveis:")
    for i, conta in enumerate(cliente.contas, 1):
        print(f"  [{i}] Agência: {conta.agencia} | C/C: {conta.numero} | Saldo: R$ {conta.saldo:.2f}")
 
    try:
        idx = int(input("Escolha o número da conta: ")) - 1
        if 0 <= idx < len(cliente.contas):
            return cliente.contas[idx]
        print("\n❌ Opção inválida.")
        return None
    except ValueError:
        print("\n❌ Entrada inválida.")
        return None
# ==================== FUNÇÕES DO MENU ====================
def depositar(clientes: list) -> None:
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n❌ Cliente não encontrado!")
        return
    
    conta = selecionar_conta(cliente)
    if not conta:
        return
 
    try:
        valor = float(input("Informe o valor do depósito: R$ "))
    except ValueError:
        print("\n❌ Valor inválido.")
        return
 
    transacao = Deposito(valor)
    cliente.realizar_transacao(conta, transacao) 

def sacar(clientes: list) -> None:
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n❌ Cliente não encontrado!")
        return
    conta = selecionar_conta(cliente)
    if not conta:
        return
 
    try:
        valor = float(input("Informe o valor do saque: R$ "))
    except ValueError:
        print("\n❌ Valor inválido.")
        return
 
    transacao = Saque(valor)
    cliente.realizar_transacao(conta, transacao) 

def exibir_extrato(clientes: list) -> None:
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n❌ Cliente não encontrado!")
        return

    conta = selecionar_conta(cliente)
    if not conta:
        return

    print("\n" + "=" * 44)
    print("              EXTRATO")
    print("=" * 44)

    transacoes = conta.historico.transacoes
    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for t in transacoes:
            simbolo = "+" if t["tipo"] == "Deposito" else "-"
            print(f"  {t['data']}  {simbolo} R$ {t['valor']:>10.2f}  ({t['tipo']})")

    print("=" * 40)
    print(f"  Saldo atual: R$ {conta.saldo:.2f}")
    print("=" * 44)

def criar_conta(numero_conta: int, clientes: list, contas: list) -> None:
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n❌ Cliente não encontrado! Cadastre o cliente primeiro.")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.adicionar_conta(conta)
    print(f"\n✅ Conta corrente criada com sucesso!\n{conta}")

def listar_contas(contas: list) -> None:
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return
    print("\n" + "=" * 44)
    for conta in contas:
        print(conta)
        print("-" * 44)

def criar_cliente(clientes: list) -> None:
    cpf = input("Informe o CPF (somente números): ")
    if filtrar_cliente(cpf, clientes):
        print("\n❌ Já existe cliente com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nasc = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/UF): ")

    try:
       data_nasc_dt = datetime.strptime(data_nasc, "%d/%m/%Y")
    except ValueError :
        print("\n❌ Data inválida. Use o formato dd/mm/aaaa.")
        return
    
    cliente = PessoaFisica(cpf=cpf, nome=nome, data_nascimento=data_nasc_dt, endereco=endereco)
    clientes.append(cliente)
    print(f"\n✅ Cliente '{nome}' cadastrado com sucesso!")

# ==================== OPERAÇÕES DO MENU ====================

def menu() -> str:
    print("""
      BANCO PYTHON
[1]  Depositar              
[2]  Sacar                  
[3]  Extrato                
[4]  Nova conta             
[5]  Listar contas          
[6]  Novo cliente           
[0]  Sair                   
""")
    return input("=> ").strip()

# ==================== MAIN ====================

def main():
    clientes: list[Cliente] = []
    contas: list[Conta] = []

    opcoes = {
        "1": lambda: depositar(clientes),
        "2": lambda: sacar(clientes),
        "3": lambda: exibir_extrato(clientes),
        "4": lambda: criar_conta(len(contas) + 1, clientes, contas),
        "5": lambda: listar_contas(contas),
        "6": lambda: criar_cliente(clientes),
    }
    while True:
        opcao = menu()

        if opcao == "0":
            print("\nAté logo! 👋")
            break
        elif opcao in opcoes:
            opcoes[opcao]()
        else:
            print("\n⚠️  Opção inválida.")


if __name__ == "__main__":
    main()