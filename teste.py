import json

def escrever(usuarios):
    with open('usuarios.json', 'w') as arquivo:
        json.dump(usuarios, arquivo)
#faz a leitura do JSON com os dados dos usuarios
def ler():
    with open('usuarios.json', 'r') as arquivo:
        usuarios = json.load(arquivo)
    return usuarios

dados = ler()
dados["dados_usuario"]["0105"] = {
    "num_cont": "015",
        "endereco": "ndereco",
        "nome": "nome",
        "cpf": "cpf",
        "saldo": "000",
        "extrato": {
            "depositos": [],
            "saques": []
}
}
print(dados)