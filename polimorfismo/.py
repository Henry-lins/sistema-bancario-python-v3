class Passaro:
    def voar(self):
        print("Pássaro voa")
class Pardal(Passaro):
    def voar(self):
        return super().voar()
class Galiha(Passaro):
    def voar(self):
        print("Galinha não voa") 
def plano_voo(V):
    V.voar()

plano_voo(Passaro())
plano_voo(Pardal())
plano_voo(Galiha())    
