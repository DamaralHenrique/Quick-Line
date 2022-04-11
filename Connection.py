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

# def getAtracoesDisp():  #Pega atrações que não estão lotadas - Connection.py

# def createIngresso(data, cpf, idtipo):  #Cria o ingresso com os dados devidos - Connection.py

#  def getAtracao(nome):  #Mostra os dados da atração [nome] - Connection.py

# def getIngresso(id)   #Pega ingressos com o id dado - Connection.py

#  def getHorarios()   #Pega todos os horários - Connection.py

# def createReserva(id_ingresso, id_horario, nome_atracao)  #Cria a reserva com os dados devidos - Connection.py

# def getIngressosWithCPF(cpf)   #Pega ingressos com o cpf dado - Connection.py

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
    print(getIngressosVendidosByTipo(2))
    print("EOT")
    return

if __name__ == "__main__":
    main()
