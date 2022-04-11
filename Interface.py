from Connection import * 

def imprimeAtracoesDisponiveis():
    # disp = getAtracoesDisp() #Pega atrações que não estão lotadas - Connection.py
    # print(disp)
    return

def cadastraIngresso(data, cpf, idtipo):
    # createIngresso(data, cpf, idtipo) #Cria o ingresso com os dados devidos - Connection.py
    print("Ingresso cadastradado!")

def apresentaAtracao(nome):
    # dados = getAtracao(nome)  #Mostra os dados da atração [nome] - Connection.py
    return

def ingressoValido(id):
    # lista = getIngresso(id)   #Pega ingressos com o id dado - Connection.py
    # return len(lista)
    return

def mostraHorarios():
    # hor = getHorarios()   #Pega todos os horários - Connection.py
    print("Horários possíveis:")
    # print(hor)

def criaReserva(id_ingresso, id_horario, nome_atracao):
    # createReserva(id_ingresso, id_horario, nome_atracao)  #Cria a reserva com os dados devidos - Connection.py
    return

def mostraIngressos(cpf):
    # ingressos = getIngressosWithCPF(cpf)   #Pega ingressos com o cpf dado - Connection.py
    # print(ingressos)
    return

def TelaCliente(cpfCliente):
    # convidado = getClienteByCPF(cpfCliente)
    # return convidado
    return

def reserva(nome):
    ingresso = input("Dê o número do ingresso a ser utilizado: ")
    if ingressoValido(ingresso):
        mostraHorarios()
        horario = input("Qual horário deseja visitar a atração (forneça o id): ")
        criaReserva(ingresso, horario, nome)
        print("Reserva feita com sucesso!")
    else:
        print("Ingresso digitado não existe.")

def consulta1():
    print("Busca de quais atrações um cliente reservou em um determinado dia.")
    cpf = print("Digite o cpf do cliente: ")
    data = print("Digite a data em que deseja buscar (DD/MM/AAAA): ")
    reservas = getReservasByCPFAndDia(cpf, data)
    print("Reservas feitas pelo cliente de cpf " + str(cpf) + " no dia " + str(data) + ":")
    print(reservas)

def consulta2():
    print("Número de ingressos que reservaram por meio do aplicativo uma determinada atração.")
    nome = print("Digite o nome da atração: ")
    numero = getIngressosByAtracao(nome)
    print(str(numero) + " foram usados para resevar o(a) " + str(nome) + ".")

def consulta3():
    print("Determinação de qual tipo de ingresso um determinado cliente mais comprou.")
    cpf = print("Digite o cpf do cliente: ")
    getTipoIngressoMaisCompradoByCPF(cpf)

def consulta4():
    print("Número de pessoas que compraram um determinado tipo de ingresso e o usaram numa certa atração.")
    nome = print("Digite o nome da atração: ")
    tipo = print("Digite o tipo de ingresso (1 ou 2): ")
    quant = getIngressosVendidosByTipo(nome, tipo)
    print("Foram usados " + str(quant) + " ingressos do tipo " + str(tipo) + " para reservar lugar na atração " + str(nome))

def consulta5():
    print("Determinação de quais horários uma certa atração ficou lotada num certo dia.")
    nome = print("Digite o nome da atração: ")
    data = print("Digite a data em que deseja buscar (DD/MM/AAAA): ")
    lista = getHorariosLotadosByAtracao(nome, data)
    print("A atração " + str(nome) + " ficou lotada no dia " + str(data) + " nos seguintes horários:")
    print(lista)

def inicioCliente(nome, cpf):
    print("Bem-vindo(a) " + str(nome))
    op = 0
    while op != 3:
        print("Escolha o que deseja fazer:\n 1. Consultar atrações disponíveis para reserva \n 2. Consultar seus ingressos válidos \n 3. Encerrar sessão")
        op = input("Opção: ")
        if op == "1":
            imprimeAtracoesDisponiveis()
            boo = input("Deseja selecionar alguma atração[y/n]? ")
            if boo == 'y':
                atrac = input("Atração escolhida: ")
                apresentaAtracao(atrac)
                boo = input("Deseja fazer a reseva[y/n]?" )
                if boo == 'y':
                    reserva(atrac)
        elif op == "2":
            mostraIngressos(cpf)
        elif op == "3":
            print("Encerrando sessão...")
    return                    

def inicioFuncionario():
    op = 0
    while op != 3:
        print("Escolha o que deseja fazer:\n 1. Fazer consultas \n 2. Cadastrar o ingresso de um cliente \n 3. Sair")
        op = input("Opção: ")
        if op == "1":
            consulta = input("Digite o número da consulta: ")
            if consulta == "1":
                consulta1()
            elif consulta == "2":
                consulta2()
            elif consulta == "3":
                consulta3()
            elif consulta == "4":
                consulta4()
            elif consulta == "5":
                consulta5()
            else:
                print("Consulta inexistente.")
        elif op == "2":
            data = input("Insira a data em que o ingresso será utilizado: ")
            cpf = input("Digite o CPF do cliente: ")
            idtipo = input("Insira o tipo de ingresso comprado: ")
            cadastraIngresso(data, cpf, idtipo)

def imprimeBoasVindas():
    print("========================")
    print("      Quick line        ")
    print("========================")

def imprimeTelaInicial():
    print("Escolha como quer logar:\n 1. Cliente \n 2. Funcionário \n 3. Sair")

def main():
    imprimeBoasVindas()
    resp = 0
    while (resp != 3):
        imprimeTelaInicial()
        resp = input("Opção: ")

        if resp == "1":
            cpf = input("Digite seu CPF: ")
            senha = input("Digite sua senha: ")
            nome = TelaCliente(cpf)
            inicioCliente(nome, cpf)


        elif resp == "2":
            id = input("Digite seu código de funcionário: ")
            senha = input("Digite a senha: ")
            inicioFuncionario() 

if __name__ == "__main__":
    main()
