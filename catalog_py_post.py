# python 3.6 com postgresql

# conecta banco: conn = psycopg2.connect("dbname='teste' user='postgres' password='123'")
# pega cursor: cur = conn.cursor()
# executa comando: cur.execute("")
# salva os dados: conn.commit()
import psycopg2
import os
import time
import sys

def opcaoUsuario():
    os.system("cls");
    print(".........AGENDA.........")
    opcao = input("Escolha a opcao desejada:\n\n1 - Cadastrar\n2 - Consultar\n3 - Alterar\n4 - Excluir\n5 - Mostrar Todos\n6 - Sair\n")
    try:
        opcao = int(opcao)
        if opcao < 1 or opcao > 6:
            os.system("cls");
            print("OPCAO INVALIDA: Verifique o valor digitado")
            time.sleep(2)
            opcaoUsuario()
    except:
        os.system("cls");
        print("OPCAO INVALIDA: Verifique o valor digitado")
        time.sleep(2)
        opcaoUsuario()

    if opcao == 1:
        conn = conectaBanco()
        funcCadastrar(conn)

    elif opcao == 2:
        conn = conectaBanco()
        funcConsultar(conn)

    elif opcao == 3:
        conn = conectaBanco()
        funcAlterar(conn)

    elif opcao == 4:
        conn = conectaBanco()
        funcExcluir(conn)

    elif opcao == 5:
        conn = conectaBanco()
        funcMostrarTodos(conn)

    elif opcao == 6:
        sys.exit()


def conectaBanco():
    USER = 'postgres'
    PASSWD = '123'
    DB = 'teste'

    try:
        conn = psycopg2.connect(dbname=DB, user=USER, password=PASSWD)

    except:
        print("O banco não foi encontrado..."),
        a = input()
        os.system("cls")
        opcaoUsuario()

    return conn

def funcCadastrar(conn):
    print("\n\nDigite o nome:\n")
    nome = str(input("Nome: "))
    nome = (nome.capitalize())
    cursor = conn.cursor()

    comando = "INSERT INTO usuario(nome) VALUES ('"+nome+"')"

    try:
        cursor.execute(comando)
        conn.commit()

    except:
        print("Erro")

    print("Dados gravados com sucesso.")
    conn.close()
    a = input()
    os.system("cls")
    opcaoUsuario()

def funcConsultar(conn):
    nome = str(input("Digite o nome a pesquisar: "))
    nome = (nome.capitalize())
    cursor = conn.cursor()
    comando = "SELECT * FROM usuario WHERE nome='"+nome+"'"
    resultados = 0

    try:
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for dados in resultado:
            ide = dados[0]
            nome = dados[1]
            resultados = int(resultados)
            resultados = resultados + 1
            print("\n----------------------------\n")
            print(" ID: %s\n Nome: %s" % (ide, nome))
            conn.commit()
            print("\n\nForam encontrados %d resultados" % resultados)

    except:
        print("Erro")

    conn.close()
    a = input()
    os.system("cls")
    opcaoUsuario()


def funcAlterar(conn):
    print("\n\nDigite os dados:\n")
    ide = input("ID do contato a alterar:  ")
    novo_nome = input("Novo nome: ")
    novo_nome = (novo_nome.capitalize())
    cursor = conn.cursor()
    comando = "UPDATE usuario SET nome='"+novo_nome+"' WHERE id='"+ide+"'"

    try:
        cursor.execute(comando)
        conn.commit()

    except:
        print("Erro")


    print("Alteração feita com sucesso.")
    conn.close()
    a = input()
    os.system("cls")
    opcaoUsuario()


def funcExcluir(conn):
    print("\n\nDigite os dados:\n")
    ide_excluir = input("Digite o id do contato a excluir: ")
    cursor = conn.cursor()
    comando = "DELETE FROM usuario WHERE id='"+ide_excluir+"'"

    try:
        cursor.execute(comando)
        conn.commit()

    except:
        print("Erro")

    print("Exclusão feita com sucesso.")
    conn.close()
    a = input()
    os.system("cls")
    opcaoUsuario()

def funcMostrarTodos(conn):
    resultados = 0
    cursor = conn.cursor()
    comando = ("SELECT * FROM usuario;")

    try:
        cursor.execute(comando)
        resultado = cursor.fetchall()

        for dados in resultado:
            ide = dados[0]
            nome = dados[1]

            resultados = int(resultados)
            resultados = resultados + 1
            print("----------------------------------")
            print("ID: %s\n Nome: %s" % (ide, nome))
            conn.commit()

    except:
        print("Erro")

    print("\n\nForam encontrados %s resultados" %resultados)
    conn.close()
    a = input()
    os.system("cls")
    opcaoUsuario()


if __name__ == '__main__':
    opcaoUsuario()