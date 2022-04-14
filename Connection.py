from asyncio.windows_events import NULL
import mysql.connector as mysql
from mysql.connector import errorcode

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "P@sswordRoot12",
    database = "quicklinebd"
)

cursor = db.cursor()

def cadastraCliente(cpf, nome, senha):
    query = "INSERT INTO quicklinebd.cliente (CPF, Nome, Senha) VALUES \
            (%s, %s, %s);"
    val = (str(cpf), str(nome), str(senha))
    cursor.execute(query, val)
    db.commit()
    print("Cliente cadastrado!")

def cadastraIngresso(data, cpf, idTipo, idIngresso):
    query = "INSERT INTO ingresso (ID_Ingresso, Data, CPF, ID_Tipo) VALUES \
            (%s, %s, %s, %s);"
    val = ( str(idIngresso), str(data), str(cpf), str(idTipo))
    cursor.execute(query, val)
    db.commit()
    print("Ingresso cadastradado!")

def cadastraReserva(ID_ingresso, ID_Horario, Nome_Atracao):
    query = "INSERT INTO reserva (ID_Ingresso, ID_Horario, Nome_Atracao) VALUES \
            (%s, %s, %s);"
    val = (str(ID_ingresso), str(ID_Horario), str(Nome_Atracao))
    cursor.execute(query, val)
    db.commit()
    print("Reserva cadastradada!")

def alteraSenha(cpf_cliente, nova_senha):
    query = "UPDATE cliente \
             SET Senha = %s \
             WHERE CPF = %s"
    val = (nova_senha, cpf_cliente)
    cursor.execute(query, val)
    db.commit()
    print("Senha alterada!")

def getDispDeAtracao(Nome, Data):
    query = "select ID_Horario, count(quicklinebd.reserva.ID_Ingresso) as reservas from quicklinebd.reserva \
                LEFT JOIN quicklinebd.atracao on quicklinebd.atracao.Nome_Atracao=quicklinebd.reserva.Nome_Atracao \
                INNER JOIN quicklinebd.ingresso on quicklinebd.ingresso.ID_Ingresso=quicklinebd.reserva.ID_Ingresso \
                where (quicklinebd.atracao.Nome_Atracao=\'"+str(Nome)+"\') and (Data=\'"+str(Data)+"\') \
                GROUP BY ID_Horario , quicklinebd.atracao.Nome_Atracao , Data;"
    cursor.execute(query)
    lotacoes = cursor.fetchall()

    horarios = getHorarios()

    horarios_list = list(horarios)

    i = 0
    for hor in horarios_list:
        horarios_list[i] = list(hor)
        horarios_list[i].append(0)
        i += 1

    i = 0
    for horario in horarios_list:
        horarios_list[i][3] = 0
        for lotacao in lotacoes: 
            if(lotacao[0] == horario[0]):
                horarios_list[i][3] = lotacao[1]
        i += 1
    return(horarios_list)

def getAtracoes():
    query = "select Nome_Atracao from Atracao"
    cursor.execute(query)
    atracoes = cursor.fetchall()
    return(atracoes)

def getAtracao(nome):  #Mostra os dados da atração [nome] - Connection.py
    query = "select * from atracao where Nome_Atracao=\'"+str(nome)+"\'"
    cursor.execute(query)
    atracao = cursor.fetchall()
    return(atracao[0])

def getIngresso(id):   #Pega ingressos com o id dado - Connection.py
    query = "select ID_Ingresso, Nome, Descricao, Valor, Data   from quicklinebd.Ingresso \
            INNER JOIN quicklinebd.Cliente on quicklinebd.Cliente.cpf=quicklinebd.Ingresso.cpf \
            INNER JOIN quicklinebd.tipoingresso on quicklinebd.tipoingresso.ID_TipoIngresso=quicklinebd.Ingresso.ID_Tipo \
            where ID_Ingresso=\'"+str(id)+"\'"
    cursor.execute(query)
    ingresso = cursor.fetchall()
    return(ingresso[0])

def getHorarios():   #Pega todos os horários - Connection.py
    query = "select * from quicklinebd.horario"
    cursor.execute(query)
    horario = cursor.fetchall()
    return(horario)

def getClientes():
    query = "select * from Cliente"
    cursor.execute(query)
    return cursor.fetchall()

# def createReserva(id_ingresso, id_horario, nome_atracao):  #Cria a reserva com os dados devidos - Connection.py

def getIngressosWithCPF(cpf):   #Pega ingressos com o cpf dado - Connection.py
    query = "select ID_Ingresso, Nome, Descricao, Valor, Data   from quicklinebd.Ingresso \
            INNER JOIN quicklinebd.Cliente on quicklinebd.Cliente.cpf=quicklinebd.Ingresso.cpf \
            INNER JOIN quicklinebd.tipoingresso on quicklinebd.tipoingresso.ID_TipoIngresso=quicklinebd.Ingresso.ID_Tipo \
            where ingresso.cpf=\'"+str(cpf)+"\'"
    cursor.execute(query)
    ingressos = cursor.fetchall()
    return(ingressos)

def getIngressosPremiumWithCPF(cpf):   #Pega ingressos com o cpf dado - Connection.py
    query = "select ID_Ingresso, Nome, Descricao, Valor, Data   from quicklinebd.Ingresso \
            INNER JOIN quicklinebd.Cliente on quicklinebd.Cliente.cpf=quicklinebd.Ingresso.cpf \
            INNER JOIN quicklinebd.tipoingresso on quicklinebd.tipoingresso.ID_TipoIngresso=quicklinebd.Ingresso.ID_Tipo \
            where ingresso.cpf=\'"+str(cpf)+"\' and ID_Tipo=2"
    cursor.execute(query)
    ingressos = cursor.fetchall()
    return(ingressos)

def getClienteByCPF(CPF):
    query = "select * from Cliente where CPF="+str(CPF)
    cursor.execute(query)
    cliente = cursor.fetchall()
    return(cliente[0])

def loginCliente(cpf, Senha):
    query = "select CPF from cliente where cpf=\'"+str(cpf)+"\' and Senha=\'"+str(Senha)+"\'"
    cursor.execute(query)
    cpf = cursor.fetchall()
    if len(cpf) == 0:
        return 0
    else:
        return cpf

def getReservasByCPFAndDia(CPF, dia):
    query = "select Data, Abertura, Fechamento, Nome_Atracao, quicklinebd.ingresso.ID_Ingresso  from reserva \
            INNER JOIN ingresso on reserva.ID_Ingresso=ingresso.ID_Ingresso \
            INNER JOIN cliente on cliente.CPF=ingresso.CPF \
            INNER JOIN horario on horario.ID_Horario=reserva.ID_Horario \
            where ingresso.CPF=\'"+str(CPF)+"\' and ingresso.Data=\'"+str(dia)+"\';"
    cursor.execute(query)
    reservas = cursor.fetchall()
    return reservas

def getReservasByCPF(CPF):
    query = "select Data, Abertura, Fechamento, Nome_Atracao, quicklinebd.ingresso.ID_Ingresso  from reserva \
            INNER JOIN ingresso on reserva.ID_Ingresso=ingresso.ID_Ingresso \
            INNER JOIN cliente on cliente.CPF=ingresso.CPF \
            INNER JOIN horario on horario.ID_Horario=reserva.ID_Horario \
            where ingresso.CPF=\'"+str(CPF)+"\'"
    cursor.execute(query)
    reservas = cursor.fetchall()
    return reservas

def getOrderedReservasByAtracao(Atracao):
    query = "select Data, Abertura, Fechamento, Nome_Atracao, quicklinebd.ingresso.ID_Ingresso from reserva \
            INNER JOIN ingresso on reserva.ID_Ingresso=ingresso.ID_Ingresso \
            INNER JOIN cliente on cliente.CPF=ingresso.CPF \
            INNER JOIN horario on horario.ID_Horario=reserva.ID_Horario \
            where Nome_Atracao = \'" + str(Atracao) + "\' \
            order by Data"

    cursor.execute(query)
    reservas = cursor.fetchall()
    return reservas

def getIngressosByAtracao(Nome_Atracao):
    query = "select Nome_Atracao, COUNT(*) As Total from reserva where Nome_Atracao=\'"+str(Nome_Atracao)+"\'"
    cursor.execute(query)
    numIngressosVendidos = cursor.fetchall()
    # numIngressosVendidos = len(ingressosVendidos)
    return numIngressosVendidos[0][1]

def getTipoIngressoMaisCompradoByCPF(CPF):
    query = "SELECT IF((select count(ID_Ingresso) from quicklinebd.ingresso where ID_Tipo=2 and cpf="+str(CPF)+")<(select count(ID_Ingresso) from quicklinebd.ingresso where ID_Tipo=1 and cpf="+str(CPF)+") \
                , 'normal', IF((select count(ID_Ingresso) from quicklinebd.ingresso where ID_Tipo=2 and cpf="+str(CPF)+")=(select count(ID_Ingresso) from quicklinebd.ingresso where ID_Tipo=1 and cpf="+str(CPF)+"), 'igual', 'premium' )) as ingresso;"
    cursor.execute(query)
    resp = cursor.fetchall()
    return resp[0][0]

def getIngressosVendidosByTipo(ID_Tipo):
    query = "select count(*) from ingresso where ID_Tipo=\'"+str(ID_Tipo)+"\'"
    cursor.execute(query)
    numIngressosVendidos = cursor.fetchall()[0][0]
    return numIngressosVendidos

def getHorariosLotadosNoDia(Data):
    query = "select quicklinebd.reserva.Nome_Atracao, Abertura, Fechamento, count(quicklinebd.reserva.ID_Ingresso) as ingressos, Lotacao from quicklinebd.reserva \
                INNER JOIN quicklinebd.horario on quicklinebd.horario.ID_Horario=quicklinebd.reserva.ID_Horario \
                INNER JOIN quicklinebd.ingresso on quicklinebd.reserva.ID_Ingresso=quicklinebd.ingresso.ID_Ingresso \
                INNER JOIN quicklinebd.atracao on quicklinebd.reserva.Nome_Atracao=quicklinebd.atracao.Nome_Atracao \
                where Data=\'"+str(Data)+"\' \
                group by Abertura , quicklinebd.reserva.Nome_Atracao , Data \
                having count(quicklinebd.reserva.ID_Ingresso)=Lotacao;"
    cursor.execute(query)
    return cursor.fetchall()

def getNumIngressosPorMes(Ano):
    query = "select month(STR_TO_DATE(Data, '%d/%m/%Y')) as mês, count(quicklinebd.reserva.ID_Ingresso) as qtd from quicklinebd.ingresso \
                INNER JOIN quicklinebd.reserva on quicklinebd.reserva.ID_Ingresso=quicklinebd.ingresso.ID_Ingresso \
                where year(STR_TO_DATE(Data, '%d/%m/%Y')) ="+str(Ano)+" \
                group by month(STR_TO_DATE(Data, '%d/%m/%Y'));"
    cursor.execute(query)
    return cursor.fetchall()

def main():
    print("BOT")
    # print(getClienteByCPF(1))
    # print(loginCliente("RR", "BD_S2"))
    # print(getReservasByCPFAndDia(2,'11/04/2022'))
    # print(getIngressosVendidosByTipo(2))
    # print(getAtracao("Montanha-Russa"))
    # print(getIngresso(3))
    # print(getHorarios())
    # print(getIngressosWithCPF(1))
    # print(getAtracoes())
    # print(getDispDeAtracao("Roda Gigante", "11/04/2022"))
    # print(getReservasByCPF(2))
    # print(getIngressosPremiumWithCPF(1))
    # alteraSenha("1234", "novaSenha123")
    # getTipoIngressoMaisCompradoByCPF(321)
    print(getAtracao("Roda Gigante"))
    print("EOT")
    return

if __name__ == "__main__":
    main()
