#somente quando quiser valores que parem de se repetir
numeros = set([1, 1, 2, 3, 3, 4])
print(numeros)
time = set("corinthians")
print(time)
carros = set(("palio", "gol", "palio"))
print(carros)
#para acessar um valor no set use ele como list
numbers = {1, 2, 3, 2}
numbers = list(numbers)
print(numbers[0])
#para percorrer no set usa o for, for + enumerate
#conjuntos matemáticos também
con_a = {1, 2, 3}
con_b = {2, 3, 4}
print(con_a.union(con_b))
print(con_a.intersection(con_b))
print(con_a.issubset(con_b))