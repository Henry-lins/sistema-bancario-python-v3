class Estudante:
    faculdade = "Unip"
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.faculdade}"
def mostrar(*resultado):
    for result in resultado:
        print(result)
aluno_1 = Estudante("Henry", 5000420)
aluno_2 = Estudante("Yrneh", 1)
mostrar(aluno_1, aluno_2)
