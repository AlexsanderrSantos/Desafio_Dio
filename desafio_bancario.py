from time import sleep
nome = str(input("Para começarmos por favor digite seu nome: ")).strip()
menu = (f"""
-=-=-=-=-=-= BANCO V.1-=-=-=-=-=-=
   Olá {nome}, o que gostaria de fazer ?
   [D] Depositar
   [S] Sacar
   [E] Extrato
   [Q] Sair

===> """)

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print(menu,end="")
    opcao = str(input("Digite sua opção: ")).strip().lower()
    if opcao == "d":
            deposito = float(input("Digite o valor de deposito R$: "))
            if deposito < 0:
                print("Erro na operação ! Tente um valor válido.")
                sleep(1.0)
            else:
                saldo += deposito
                print(f"Confirmado o valor de deposito R${deposito:.2f}".replace(".", ","))
                extrato += (f"Depósito de R${deposito:.2f}\n".replace(".", ","))
                print("retornando ao menu principal...")
                sleep(1.2)
                
    elif opcao == "s":
        saque = float(input("Digite o valor a sacar: "))
        exceder_limite = saque > limite
        exceder_saldo = saque > saldo
        exceder_saques = numero_saques >= LIMITE_SAQUES
        
        if exceder_saldo:
            print("Você não tem saldo suficiente para esta operação.")
            sleep(1)
        elif exceder_limite:
            print("Você não pode sacar esse valor, pois é maior que o limite permitido.")
            sleep(1)
        elif exceder_saques:
            print("Operação falhou, limite de saques excedido.")
            sleep(1)
        elif saque > 0:
            saldo -= saque
            print(f"Saque efetuado de R${saque:.2f}".replace(".", ","))
            print("Retornando ao menu principal")
            numero_saques += 1
            sleep(1.2)
            extrato += (f"Saque de R${saque:.2f}\n".replace(".", ","))
        else:
            print("Operação falhou, o valor informado é inválido.")
            sleep(1)
            
    elif opcao == "e":
        print("-=-"* 10, f"EXTRATO", "-=-" * 10)
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo total de R${saldo:.2f}".replace(".", ","))
        print('-=-' * 23)
        sleep(3)
        
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida! Digite um valor correto e tente novamente. ")
        sleep(1.5)
print("Obrigado por usar nosso serviços, volte sempre !")
    