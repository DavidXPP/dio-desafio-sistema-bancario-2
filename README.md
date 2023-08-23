# dio-desafio-sistema-bancario-2
Desafio do sistema bancario da DIO, agora com cadastro de usuários. Esse desafio faz parte do bootcamp Ciencia de Dados com Python, do módulo de Python Básico.

função de saque keyword only
- sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques
- sugestao de retorno: saldo e extrato

função de depósito deve receber os argumentos apenas por posição
- sugestão de argumentos: saldo, valor, extrato
- sugestão de retorno saldo e extrato

função extrato deve receber os argumentos por posição e keyword
- argumentos posicionioas: saldo
-argumentos nomeados: extrato

função de criar usuário e criar conta corrente
(criar usuário)
- nome, data de nascimento, cpf e endereço
- o endereço é string com formato: logradouro, nro - bairro - cidade/sigla estado.
- cpf somente os numeros, não pode haver dois usuarios com o mesmo cpf

função de criar conta corrente
-agencia, numero da conta e usuário
- o numero da conta é sequencial iniciando em 1
- o número da agencia é fixo 0001
- um usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.


- Também será exercitado nesse projeto manupulação de variáveis do tipo json, para que os dados estejam disponíveis para além do tempo de execução.