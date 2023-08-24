import json
cad_padrao = {
    "num_cont": None,
    "endereco": ["", "", "", "", ""],
    "nome": "",
    "cpf": "",
    "saldo": None,
    "extrato": {
        "depositos": [],
        "saques": []
    }
}
#faz a escrita do paremetro 'usuarios' dentro do JSON
def escrever(usuarios):
    with open('usuarios.json', 'w') as arquivo:
        json.dump(usuarios, arquivo)
#faz a leitura do JSON com os dados dos usuarios
def ler():
    with open('usuarios.json', 'r') as arquivo:
        usuarios = json.load(arquivo)
    return usuarios
#determina o proximo número da conta, o maior da lista + 1
def new_num_cont():
    aux = 0
    usuarios = ler()
    chaves = list(usuarios["dados_usuario"].keys())
    for l in range(1,len(chaves)):
        for i in range(0,(len(chaves)-1)):
            if chaves[i] > chaves[i+1]:
                aux = chaves[i]
            else:
                aux = chaves[i+1]
    new_num = int(aux)+1
    return new_num
def cadastro_user():
    global cad_padrao
    endereco = ["Pais","Estado", "Cidade", "Numero", "CEP", "Logradouro"]
    num_cont = new_num_cont()
    nome = input("Digite o seu nome completo:")
    cpf = input("Digite o seu CPF:")
    for i in range(0,len(endereco)-1):
        endereco[i] = input(f"Digeite o {endereco[i]}:")
    opc = input(f"""
          SEUS DADOS SÃO:
          NOME: {nome}
          AGÊNCIA: 0001
          CONTA: {num_cont}
          ENDEREÇO: {endereco[0]}, {endereco[1]}, {endereco[2]} , Nº{endereco[3]} e CEP:{endereco[4]}
          
          DESEJA SALVAR? (s-SIM n-NÃO)\n""")
    if opc == "s":
        usuarios = ler()
        usuarios["dados_usuario"][num_cont] =  {"num_conta": f"{num_cont:04}", "endereco": endereco, "nome":nome, "cpf":cpf, "saldo":None, "extrato": {"depositos": [], "saques": []}}
        escrever(usuarios)
    elif opc == "n":
        print("voltando para menu inicial..")
        principal()

    else:
        print("Por favor digite uma opção válida!")
        cadastro_user()

def deposito():
    conta = input("Insira a sua conta")
    cpf = input("Digite o seu CPF")
    usuarios = ler()
    print(usuarios["dados_usuario"][str(conta)] in usuarios)
    # if usuarios["dados_usuario"][str(conta)] in usuarios["dados_usuario"]:
    #     valor_deposito = int(input("Insira o valor a depositar"))
    #     if usuarios["dados_usuario"][conta]["saldo"] < valor_deposito:
    #         print("Você não possuí saldo suficiente!")
    #         principal()
    #     else:
    #         usuarios["dados_usuario"][conta]["extrato"]["depositos"].append(val_deposito)
    #         escrever(usuarios)
    #         usuarios = ler()
    #         usuarios["dados_usuario"][conta]["saldo"] = usuarios["dados_usuario"][conta]["extrato"]["depositos"].sum() - usuarios["dados_usuario"][conta]["extrato"]["saques"].sum()
    #         escrever(usuarios)
    # else:
    #     print("usuário não encontrado...")
    #     principal()
    saldo_conta = []
    val_deposito = float(input("Insira o valor que deseja depositar na conta"))

def principal():
    while True:
        try:
            menu = str(input("""
            BEM VINDO AO SISTEMA BANCÁRIO SIMPLIFICADO
            ==========================================
            
            [d] DEPOSITO
            [s] SAQUE
            [e] EXTRATO
            [a] ABRIR CONTA
            [j] ENTRAR NO MODO ADMINSTRADOR
            [q] SAIR                 
                            """))
        except ValueError:
            print("Por favor digite uma opção válida!")
        else:
            if menu == "d":
                deposito()
            elif menu == "s":
                print("menu saque")
            elif menu == "e":
                print("menu extrato")
            elif menu == "a":
                cadastro_user()
            elif menu == "q":
                print("Até mais!")
                break
            else:
                print("Por favor digite uma opção válida!")
principal()