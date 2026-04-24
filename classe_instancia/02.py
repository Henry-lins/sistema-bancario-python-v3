class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    @classmethod
    def data_nascimento(cls, ano, nome):
        idade = 2026 - ano
        return cls(nome, idade)
    @staticmethod
    def maior_idade(idade):
        return idade >= 18

p = Pessoa.data_nascimento(2007, "Henry")
print(p.nome, p.idade)

print(Pessoa.maior_idade(25))
print(Pessoa.maior_idade(17))
