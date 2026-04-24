from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass
    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
    def desligar(self):
        print("Desligando TV")
    @property
    def marca(self):
        return "LG"     
class ControleAR(ControleRemoto):
    def ligar(self):
        print("Ar Ligado")
    def desligar(self):
        print("Ar desligado")
    @property
    def marca(self):
        return "Phillips"        

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleAR()
controle.ligar()
controle.desligar()
print(controle.marca)