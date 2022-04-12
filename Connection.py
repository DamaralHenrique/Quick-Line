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

def getDispDeAtracao(Nome, Data):
    query = "select ID_Horario, count(quicklinebd.reserva.ID_Ingresso) as reservas from quicklinebd.reserva \
                LEFT JOIN quicklinebd.atracao on quicklinebd.atracao.Nome_Atracao=quicklinebd.reserva.Nome_Atracao \
                INNER JOIN quicklinebd.ingresso on quicklinebd.ingresso.ID_Ingresso=quicklinebd.reserva.ID_Ingresso \
                where (quicklinebd.atracao.Nome_Atracao=\'"+str(Nome)+"\') and (Data=\'"+str(Data)+"\') \
                GROUP BY ID_Horario and quicklinebd.atracao.Nome_Atracao and Data;"
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
    print(horarios_list)
    return(horarios_list)

# def createIngresso(data, cpf, idtipo):  #Cria o ingresso com os dados devidos - Connection.py

def getAtracoes():
    query = "select Nome_Atracao from Atracao"
    cursor.execute(query)
    atracoes = cursor.fetchall()
    return(atracoes)

def getAtracao(nome):  #Mostra os dados da atração [nome] - Connection.py
    query = "select * from Atracao where Nome_Atracao=\'"+str(nome)+"\'"
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

# def createReserva(id_ingresso, id_horario, nome_atracao):  #Cria a reserva com os dados devidos - Connection.py

def getIngressosWithCPF(cpf):   #Pega ingressos com o cpf dado - Connection.py
    query = "select ID_Ingresso, Nome, Descricao, Valor, Data   from quicklinebd.Ingresso \
            INNER JOIN quicklinebd.Cliente on quicklinebd.Cliente.cpf=quicklinebd.Ingresso.cpf \
            INNER JOIN quicklinebd.tipoingresso on quicklinebd.tipoingresso.ID_TipoIngresso=quicklinebd.Ingresso.ID_Tipo \
            where ingresso.cpf=\'"+str(cpf)+"\'"
    cursor.execute(query)
    ingressos = cursor.fetchall()
    return(ingressos)

def getClienteByCPF(CPF):
    query = "select * from Cliente where CPF="+str(CPF)
    cursor.execute(query)
    cliente = cursor.fetchall()
    return(cliente[0])

def loginCliente(Nome, Senha):
    query = "select CPF from cliente where Nome=\'"+str(Nome)+"\' and Senha=\'"+str(Senha)+"\'"
    cursor.execute(query)
    cpf = cursor.fetchall()
    if cpf == NULL:
        return 0
    else:
        return cpf

def getReservasByCPFAndDia(CPF, dia):
    query = "select Abertura, Fechamento, Nome_Atracao  from reserva \
            INNER JOIN ingresso on reserva.ID_Ingresso=ingresso.ID_Ingresso \
            INNER JOIN cliente on cliente.CPF=ingresso.CPF \
            INNER JOIN horario on horario.ID_Horario=reserva.ID_Horario \
            where ingresso.CPF=\'"+str(CPF)+"\' and ingresso.Data=\'"+str(dia)+"\';"
    cursor.execute(query)
    reservas = cursor.fetchall()
    return reservas

def getIngressosByAtracao(Nome_Atracao):
    query = "select * from reserva where Nome_Atracao=\'"+str(Nome_Atracao)+"\'"
    cursor.execute(query)
    ingressosVendidos = cursor.fetchall()
    numIngressosVendidos = len(ingressosVendidos)
    return numIngressosVendidos

def getTipoIngressoMaisCompradoByCPF(CPF):
    query = "select * from ingresso where CPF=\'"+str(CPF)+"\' and ID_Tipo=\'"+str(1)+"\'"
    cursor.execute(query)
    numIngressosNormal = len(cursor.fetchall())
    query = "select * from ingresso where CPF=\'"+str(CPF)+"\' and ID_Tipo=\'"+str(2)+"\'"
    cursor.execute(query)
    numIngressosPremium = len(cursor.fetchall())
    if numIngressosNormal > numIngressosPremium:
        print("O cliente de CPF "+str(CPF)+" comprou mais ingressos do tipo normal.")
    elif numIngressosNormal < numIngressosPremium:
        print("O cliente de CPF "+str(CPF)+" comprou mais ingressos do tipo premium.")
    else:
        print("O cliente de CPF "+str(CPF)+" comprou a mesma quantia de ingressos dos dois tipos.")

def getIngressosVendidosByTipo(ID_Tipo):
    query = "select count(*) from ingresso where ID_Tipo=\'"+str(ID_Tipo)+"\'"
    cursor.execute(query)
    numIngressosVendidos = cursor.fetchall()[0][0]
    return numIngressosVendidos

def getHorariosLotadosByAtracao(Nome_Atracao, Data):
    query = "select * from reserva where Nome_Atracao=\'"+str(Nome_Atracao)+"\'"
    cursor.execute(query)
    reservasTotais = cursor.fetchall()
    # for reserva in reservasTotais (TODO)

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
    print(getDispDeAtracao("Roda Gigante", "11/04/2022"))
    print("EOT")
    return

if __name__ == "__main__":
    main()
