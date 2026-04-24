#def carac_carro(modelo, ano, placa, /, marca, motor):
    #print(modelo, ano, placa, marca, motor)
#carac_carro("Agile", 2012, "GLI", marca="Chevrolet", motor="1.4")


#def carac_carro(*, modelo, ano, marca):
    #print(modelo, ano, marca)
#carac_carro(modelo="T-cross", ano="2021", marca="Volskwagem")


#def carac_moto(modelo, ano, /, *, marca, motor):
    #print(modelo, ano, marca, motor)
#carac_moto("Fazer", "2020", marca="Yamaha", motor="125CC")    

def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def exibir_resultado(a, b, funcao, operador):
    resultado = funcao(a, b)
    print(f"Resultado: {a} {operador} {b} = {resultado}")

exibir_resultado(5, 5, somar, "+")
exibir_resultado(5, 5, subtrair, "-")    

    