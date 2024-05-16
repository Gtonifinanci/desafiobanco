import textwrap

def menu(): #pronto
    menu = """\n
    ================== MENU ===================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExibir Extrato
    [nc]\tNova Conta
    [nu]\tNovo Usuario
    [lc]\tListar Cliente
    [0]\tSair
    ==>"""

    return input(textwrap.dedent(menu))
    

def depositar(saldo, valor, extrato, /): #pronto

    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("!!!DEPOSITO REALIZADO COM SUCESSO!!!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato
    

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): #pronto
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
         print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def exibir_extrato(saldo,/, *, extrato): #pronto

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios): #pronto


    cpf = input("Informe somente numeros do CPF:")
    usuario = filtrar_usuario(cpf, usuarios) 
    if usuario:
        print("!!!!!! USUARIO JA CADASTRADO NESSE CPF !!!!!!")
        return


    nome = input("Informe nome Completo: ")
    data_nascimento = input("Insira data de nascimento (dd-mm-aaaa): ")
    endereco = input("Insira seu endereço (logradouro - numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("USUARIO CADASTRATO COM SUCESSO!")

def filtrar_usuario(cpf, usuarios): #pronto
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    

def criar_conta(agencia, numero_conta, usuarios): #pronto
    cpf = input("Informe somente numeros do CPF:")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario: 
        print("Conta criada com sucesso!!!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuario não encontrado!")


def listar_contas(contas): #pronto
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main(): #pronto

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = [] 
    contas = []

    while True:
        opcao = menu()

        if opcao == "d": #certo
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s": #certo
            valor = input("Insira valor do saque: ")

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "nu": #certo
            criar_usuario(usuarios)

        elif opcao == "nc": #certo
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc": #certo
            listar_contas(contas)
            
        elif opcao == "e": #certo
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "0": #certo
             break

        else: #certo
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main() #certo
