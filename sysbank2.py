import json

def escrever(usuarios):
    with open('usuarios.json', 'w') as arquivo:
        json.dump(usuarios, arquivo)

# Dados dos usuários que você deseja escrever no arquivo
dados_usuarios = {
    "001": {"Nome": "David", "CPF": "00577892"},
    "002": {"Nome": "Allison", "CPF": "00522842"}
}

# Chamando a função para escrever os dados no arquivo
escrever(dados_usuarios)