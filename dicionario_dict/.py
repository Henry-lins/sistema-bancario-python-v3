#pessoa = {'nome': 'Henry', 'idade': 18}
#pessoa['telefone'] = '981444989'
#print(pessoa)

contatos = {
     "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1111-2222"},
     "giovana@gmail.com": {"nome": "Giovana", "telefone": "2222-4444"},
     "chappie@gmail.com": {"nome": "Chapie", "telefone": "5555-8888"},
}
#telefone = contatos["chappie@gmail.com"]["telefone"]
#print(telefone)
for chave, valor in contatos.items():
    print(chave, valor)


carro = {"marca": "Fiat", "modelo": "palio", "placa": "ABD-9826"}
print(carro.get("motor"))