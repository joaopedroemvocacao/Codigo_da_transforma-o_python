import json

clientes = {
    "001": {"nome": "Ana Silva", "telefone": "9999-1111"},
    "002": {"nome": "Carlos Souza", "telefone": "9999-2222"}
}

with open("clientes.json", "w", encoding="utf-8") as arquivo:
    json.dump(clientes, arquivo)

print("Clientes salvos!")

with open("clientes.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

print("\nClientes cadastrados:")
for codigo, info in dados.items():
    print(f"{codigo} - {info['nome']}")