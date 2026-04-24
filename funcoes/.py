#def exibir_mensagem():
    #print("Hello Word")

#def exibir_mensagem_2(nome):
    #print(f"Welcome {nome}")

#exibir_mensagem()
#exibir_mensagem_2(nome="Henry")

def calcular_total(numeros):
    return sum(numeros)
 
def mostrar_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor
print(calcular_total([10, 20, 40]))
print(mostrar_antecessor_sucessor(100)) 
