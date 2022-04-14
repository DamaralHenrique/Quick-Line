from Connection import * 
import os

def mostraHorarios():
    hor = getHorarios()   # Pega todos os horários - Connection.py
    print("Horários possíveis:")
    print(hor)

def mostraLotacao(lotacao):
    if(len(lotacao) == 0):
        print("Não existem atrações lotadas nesse dia! :(")
    else:
        print("   ATRACAO                    ABERTURA  FECHAMENTO  LOTACAO")
        for lot in lotacao:
            print("-> "+'{0:<25}'.format(str(lot[0]))+"  "+str(lot[1])+"  "+str(lot[2])+"    "+str(lot[3]))
    return

def mostraReservas(reservas):
    if(len(reservas) == 0):
        print("Não há reservas disponíveis :(")
    else:
        print("   DATA        ATRACAO                    ABERTURA  FECHAMENTO  INGRESSO")
        for reserva in reservas:
            print("-> "+'{0:<8}'.format(str(reserva[0]))+"  "+'{0:<25}'.format(str(reserva[3]))+"  "+str(reserva[1])+"  "+str(reserva[2])+"    "+str(reserva[4]))
    return

def mostraIngressos(ingressos):
    if(len(ingressos) == 0):
        print("Não ha ingressos disponíveis :(")
    else:
        print("   TIPO     VALOR   DATA        CÓDIGO")
        i = 1
        for ingresso in ingressos:
            print('{0:>2}'.format(str(i))+". "+'{0:<8}'.format(str(ingresso[2]))+" R$"+str(ingresso[3])+"  "+str(ingresso[4])+"  "+str(ingresso[0]))
            i += 1
    return

def mostraDisponibilidade(horarios, atracao):
    if(len(horarios) == 0):
        print("Não há horários disponíveis para essa atração :(")
    else:
        print("Horarios diponiveis para "+str(atracao[0])+":")
        print("     ABERTURA     FECHAMENTO   LOTAÇÃO ATUAL")
        i = 1
        for horario in horarios:
            print('{0:>2}'.format(str(i))+". "+'{0:<12}'.format(str(horario[1][0:5]))+" "+'{0:<12}'.format(str(horario[2][0:5]))+"  "+str(horario[3])+"/"+str(atracao[2]))
            i += 1
    return

def mostraNumIngressosPorMes(lista):
    print("Mês     Número de Ingressos")
    for item in lista:
        print('{0:<8}'.format(str(item[0])) + "                  " + '{0:<8}'.format(str(item[1])))

def mostraClientes(Clientes):
    print("CPF         Nome")
    for cliente in Clientes:
        print('{0:<10}'.format(str(cliente[0])) + "  " + '{0:<8}'.format(str(cliente[1])))

def mostraAtracoes(Atracoes):
    if(len(Atracoes) == 0):
        print("Não há atrações para serem mostradas :(")
    else:
        print("Atrações disponíveis:")
        print("    NOME")
        i = 1
        for atracao in Atracoes:
            print('{0:>2}'.format(str(i))+". "+str(atracao[0]))
            i += 1
        print(" q. Voltar")
    return

def reserva(horario, atracao, cpf):
    ingresso = ''
    ingressos = getIngressosPremiumWithCPF(cpf)
    print("Seus ingressos:")
    mostraIngressos(ingressos)
    cadastrou = False
    while (ingresso != "q" and cadastrou==False):
        ingresso = input("Dê o número do ingresso a ser utilizado ('q' para cancelar): ")
        if ingresso == "q":
            print("Cancelando reserva...")
        elif int(ingresso)-1 < len(ingressos):
            cadastraReserva(ingressos[int(ingresso)-1][0], horario, atracao)
            print("Reserva feita com sucesso!")
            cadastrou = True
        else:
            print("Ingresso digitado não existe.")

def consulta1():
    print("\nBusca de quais atrações um cliente reservou em um determinado dia.")
    cpf = input("Digite o cpf do cliente: ")
    data = input("Digite a data em que deseja buscar (DD/MM/AAAA): ")
    reservas = getReservasByCPFAndDia(cpf, data)
    print("\nReservas feitas pelo cliente de cpf " + str(cpf) + " no dia " + str(data) + ":")
    mostraReservas(reservas)

def consulta2():
    print("\nNúmero de ingressos que reservaram por meio do painel para uma determinada atração.")
    atracoes = getAtracoes()
    mostraAtracoes(atracoes)
    nome = input("Digite o nome da atração: ")
    if nome == 'q':
        print("Retornando...")
    elif int(nome)-1 < len(atracoes):
        atracao = str(atracoes[int(nome)-1][0])
        numero = getIngressosByAtracao(atracao)
        print(str(numero) + " ingressos foram usados para resevar o(a) " + str(atracao) + ".")
        reservas = getOrderedReservasByAtracao(atracao)
        mostraReservas(reservas)

def consulta3():
    print("\nDeterminação de qual tipo de ingresso um determinado cliente mais comprou.")
    cpf = input("Digite o cpf do cliente: ")
    print("")
    tipo = getTipoIngressoMaisCompradoByCPF(cpf)
    if tipo == "igual":
        print("O cliente de CPF "+str(cpf)+" comprou a mesma quantia de ingressos dos dois tipos.")
    else:
        print("O cliente de CPF "+str(cpf)+" comprou mais ingressos do tipo "+tipo+".")

def consulta4():
    print("\nMostra o número total de ingressos comprados em cada mês de um determinado ano. ")
    ano = input("Digite o ano desejado: ")
    print("")
    lista = getNumIngressosPorMes(ano)
    mostraNumIngressosPorMes(lista)

def consulta5():
    print("\nDeterminação de quais horários e atrações ficaram lotadas num certo dia.")
    data = input("Digite a data em que deseja buscar (DD/MM/AAAA): ")
    lista = getHorariosLotadosNoDia(data)
    print("\nNo dia " + str(data) + ", as seguintes atrações e horários ficaram lotados:")
    mostraLotacao(lista)

def consulta6():
    print("\nMostra todos os clientes cadastrados.")
    clientes = getClientes()
    mostraClientes(clientes)

def inicioCliente(cpf):
    cliente = getClienteByCPF(cpf)
    print("===========================")
    print("Bem-vindo(a) " + str(cliente[1]))
    op = 0
    while op != "5":
        print("===========================")
        print("Escolha o que deseja fazer:\n 1. Consultar atrações disponíveis para reserva \n 2. Consultar seus ingressos \n 3. Consultar suas reservas \n 4. Alterar senha \n 5. Encerrar sessão")
        op = input("Opção: ")
        if op == "1":
            atracoes = getAtracoes()
            mostraAtracoes(atracoes)
            atr = input("Selecione uma atração: ")
            if atr == 'q':
                print("Cancelando...")
            elif int(atr)-1 < len(atracoes):
                atracao = getAtracao(atracoes[int(atr)-1][0])
                print("Você escolheu a atração "+atracao[0])
                print("Sobre ela: "+atracao[1])
                data = input("Deseja saber sobre qual data? (DD/MM/AAAA) ")
                horarios = getDispDeAtracao(atracao[0], str(data))
                mostraDisponibilidade(horarios,atracao)
                hor = input("Opção: ")
                if hor == 'q':
                    print("Cancelando...")
                elif (str(horarios[int(hor)-1][3]) == str(atracao[2])):
                    print("Você escolheu um horário lotado")
                elif int(hor)-1 < len(horarios):
                    print("Você escolheu o horario "+str(horarios[int(atr)-1][0]))
                    ID_Horario = horarios[int(atr)-1][0]
                    nome_atracao = atracoes[int(atr)-1][0]
                    reserva(ID_Horario, nome_atracao, cpf)
        elif op == "2":
            ingressos = getIngressosWithCPF(cpf)
            print("Seus ingressos:")
            mostraIngressos(ingressos)
            dumb = input("Aperte qualquer tecla para continuar.")
        elif op == "3":
            reservas = getReservasByCPF(cpf)
            print("Suas reservas:")
            mostraReservas(reservas)
            dumb = input("Aperte qualquer tecla para continuar.")
        elif op == "4": 
            senha = input("Digite sua senha: ")
            resp = loginCliente(cpf, senha)
            if(resp == 0):
                print("Senha incorreta! Operação abortada.")
            else:     
                nova_senha = input("Digite nova senha: ")
                alteraSenha(cpf, nova_senha)
                dumb = input("Aperte qualquer tecla para continuar.")
        elif op == "5":
            print("Encerrando sessão...")
        os.system('cls' if os.name == 'nt' else 'clear')
    return                    

def inicioFuncionario():
    op = 0
    while op != "4":
        print("===========================")
        print("Escolha o que deseja fazer:\n 1. Fazer consultas \n 2. Cadastrar um cliente \n 3. Cadastrar o ingresso de um cliente \n 4. Sair")
        op = input("Opção: ")
        if op == "1":
            print("Escolha uma consulta:\n 1. Busca de quais atrações um cliente reservou em um determinado dia \n 2. Número de ingressos que reservaram por meio do painel uma determinada atração")
            print(" 3. Determinação de qual tipo de ingresso um determinado cliente mais comprou \n 4. Mostra o número total de ingressos comprados em cada mês em um determinado ano")
            print(" 5. Determinação de quais horários uma certa atração ficou lotada num certo dia \n 6. Mostra todos os clientes cadastrados")
            consulta = input("Digite o número da consulta: ")
            if consulta == "1":
                consulta1()
                dumb = input("Aperte qualquer tecla para continuar.")
            elif consulta == "2":
                consulta2()
                dumb = input("Aperte qualquer tecla para continuar.")
            elif consulta == "3":
                consulta3()
                dumb = input("Aperte qualquer tecla para continuar.")
            elif consulta == "4":
                consulta4()
                dumb = input("Aperte qualquer tecla para continuar.")
            elif consulta == "5":
                consulta5()
                dumb = input("Aperte qualquer tecla para continuar.")
            elif consulta == "6":
                consulta6()
                dumb = input("Aperte qualquer tecla para continuar.")
            else:
                print("Consulta inexistente.")
        elif op == "2":
            cpf = input("Digite o CPF do cliente: ")
            nome = input("Digite o nome do cliente: ")
            senha = "123" # Senha padrao
            cadastraCliente(cpf, nome, senha)
            dumb = input("Digite qualquer coisa para continuar: ")

        elif op == "3":
            data = input("Insira a data em que o ingresso será utilizado: ")
            cpf = input("Digite o CPF do cliente: ")
            idtipo = input("Insira o tipo de ingresso comprado (1-Normal e 2-Premium): ")
            idIngresso = input("Insira o codigo do ingresso: ")
            cadastraIngresso(data, cpf, idtipo, idIngresso)
            dumb = input("Digite qualquer coisa para continuar: ")
        os.system('cls' if os.name == 'nt' else 'clear')

def imprimeBoasVindas():
    print("========================")
    print("      Quick line        ")
    print("========================")

def imprimeTelaInicial():
    print("Escolha como quer logar:\n 1. Cliente \n 2. Funcionário \n 3. Sair")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    imprimeBoasVindas()
    resp = 0
    while (resp != "3"):
        imprimeTelaInicial()
        resp = input("Opção: ")

        if resp == "1":
            cpf = input("Digite seu CPF: ")
            senha = input("Digite sua senha: ")
            resp = loginCliente(cpf, senha)
            if(resp == 0):
                print("Usuário ou senha inválidos!")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                inicioCliente(cpf)

        elif resp == "2":
            id = input("Digite seu código de funcionário: ")
            senha = input("Digite a senha: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            inicioFuncionario() 

        elif resp == "3":
            print("Bye ;)")

if __name__ == "__main__":
    main()
