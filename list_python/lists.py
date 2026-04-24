carros = ["cruze", "fusion", "jetta"]
for indice, carro in enumerate(carros):
    print(f"{indice}: {carros}")


numeros = [1, 10, 66, 55, 43]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)    


lista = [1, "python", [40,30,20]]
lista.copy()
print(lista)
             

list = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print(list)             