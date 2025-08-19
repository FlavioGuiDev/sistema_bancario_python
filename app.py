# Um único usuário
# validar se o depósito é positivo
# Armazenar os saques e depósitos em lista e exibi-los no extrato
# no fim do extrato, exibir o saldo atual
# Formato dos valores de saque e depósito deve ser R$ xxx.xx
# O sistema deve permitir que o usuário realize apenas 3 saques diários com limite
# de $ 500 por saque. 
# Validar se existe saldo em conta no momento do saque e caso não tenha, informar o usuário
# todos os saques devem ser armazenados e exibidos no extrato

titulo = "MENU"
LIMITE = 500
operacoes = []
saque = 0
saldo = 0
deposito = 0

print (f"""" 
Bem-vindo ao sistema bancário!
       {titulo.center(20, "=")}
        1 - Depositar
        2 - Sacar
        3 - Extrato
        4 - Sair
""")

while True:
    input_usuario = input("\nDigite a opção desejada: ")
    if input_usuario == "1":
        deposito = float(input("\nDigite o valor do depósito: R$ "))
        if deposito > 0:
            saldo += deposito
            operacoes.append(f"+R$ {deposito:.2f}")
            print(f"\nDepósito de R$ {deposito:.2f} realizado com sucesso!")
        else:
            print("\nValor inválido. Digite o valor correto.")
    elif input_usuario == "2":
        if saque < 3:
            saque_valor = float(input("\nDigite o valor do saque: R$ "))
            if saque_valor > 0 and saque_valor <= LIMITE and saque_valor <= saldo:
                saldo -= saque_valor
                operacoes.append(f"-R$ {saque_valor:.2f}")
                saque += 1
                print(f"\nSaque de R$ {saque_valor:.2f} realizado com sucesso!")
            elif saque_valor > LIMITE:
                print(f"\nValor do saque excede o limite por saque de R$ {LIMITE:.2f}.")
            elif saque_valor > saldo:
                print("\nSaldo insuficiente.")
            else:
                print("\nValor inválido. Digite o valor correto.")
        else:
            print("\nLimite de saques diários atingido.")
    elif input_usuario == "3":
        if operacoes:
            print("\n========Extrato========")
            for operacao in operacoes:
                print(operacao)
            print(f"\nSaldo atual: R$ {saldo:.2f}")
        else:
            print("\nNenhuma operação realizada.")
    elif input_usuario == "4":
        print("\nSaindo do sistema. Até logo!")
        break
    else:
        print("\nOpção inválida. Por favor, escolha uma opção válida.")           
