class Pessoa:
    def __init__(self, nome, date_of_birth):
        self._nome = nome
        self._date_of_birth = date_of_birth
    @property
    def nome(self):
        return self._nome
    @property
    def idade(self):
        _ano_atual = 2026
        return _ano_atual - self._date_of_birth
p = Pessoa("Henry", 2007)
print(f"Nome: {p.nome} \tIdade: {p.idade}")
