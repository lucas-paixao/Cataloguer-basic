# Python w/ the user interface TKinter
# ***the bugs need fixing***

from tkinter import *
import psycopg2


BG = '#C9C9C9'
BTN = '#B0B0B0'
class Catalogador(object):
    def __init__(self, i):
        # Frame que contem texto inicial
        self.frame1 = Frame(i, pady=40, bg=BG)
        self.frame1.pack()
        # Frame que contem os botoes
        self.frame2 = Frame(i, pady=10, bg=BG)
        self.frame2.pack()

        self.texto = Label(self.frame1, text="AGENDA", bg=BG)
        self.texto.pack()
        self.texto2 = Label(self.frame1, text="Escolha a opção desejada: ", bg=BG)
        self.texto2.pack()


        botoes = ('Cadastrar', 'Consultar', 'Alterar', 'Excluir', 'Mostrar Todos', 'Sair')
        comando = (self.funcCadastrar, self.funcConsultar, self.funcAlterar, self.funcExcluir, self.funMostrarTodos, self.sair)

        for b in range(len(botoes)):
            if b % 3 == 0:
                subframe = Frame(self.frame2, pady=20, bg=BG)
                subframe.pack()
            a = Button(subframe, text=botoes[b], width=25, command=comando[b], bg=BTN)
            a.pack(side=LEFT)

    def conectaBanco(self):
        USER = 'yourUser'
        PASSWD = 'yourPass'
        DB = 'yourDB'

        try:
            self.conn = psycopg2.connect(dbname=DB, user=USER, password=PASSWD)

        except:
            print("O banco não foi encontrado..."),

        return self.conn


    def funcCadastrar(self):
        self.jan = Tk()
        self.jan.geometry("200x120")
        self.jan.title("Cadastrar")
        self.jan['bg']=BG
        t = Label(self.jan, text="Digite o nome a cadastrar: ", bg=BG)
        t.pack()
        self.e = Entry(self.jan)
        self.e.pack()
        b = Button(self.jan, text="Cadastrar", bg=BTN, command=self.cadastro)
        b.pack()


    def cadastro(self):
        self.conn = self.conectaBanco()
        self.nome = self.e.get()
        self.nome = (self.nome.capitalize())
        cursor = self.conn.cursor()
        comando = "INSERT INTO usuario(nome) VALUES ('" + self.nome + "')"

        try:
            cursor.execute(comando)
            self.conn.commit()
            t = Label(self.jan, text="Cadastrado com sucesso!", bg=BG)
            t.pack()

        except:
            print("Erro")

        self.conn.close()


    def funcConsultar(self):
        self.jan = Tk()
        self.jan.geometry("200x400")
        self.jan.title("Consultar")
        self.jan['bg'] = BG
        t = Label(self.jan, text="Digite o nome a consultar:", bg=BG)
        t.pack()
        self.e = Entry(self.jan)
        self.e.pack()
        b = Button(self.jan, text="Consultar", bg=BTN, command=self.consultado)
        b.pack()


    def consultado(self):
        self.conn = self.conectaBanco()
        self.nome = self.e.get()
        self.nome = (self.nome.capitalize())
        cursor = self.conn.cursor()
        comando = "SELECT * FROM usuario WHERE nome='" + self.nome + "'"
        resultados = 0

        try:
            cursor.execute(comando)
            resultado = cursor.fetchall()
            for dados in resultado:
                ide = dados[0]
                self.nome = dados[1]
                resultados = int(resultados)
                resultados = resultados + 1
                t = Label(self.jan, text="\nForam encontrados %d resultados\n" % resultados, bg=BG)
                t1 = Label(self.jan, text="ID: %s  Nome: %s" %(ide, self.nome), bg=BG)
                self.conn.commit()
                t.pack()
                t1.pack()

        except:
            print("Erro")

        self.conn.close()

    def funcAlterar(self):
        self.jan = Tk()
        self.jan.geometry("200x200")
        self.jan.title("Alterar")
        self.jan['bg'] = BG
        t = Label(self.jan, text="Digite o ID do contato a alterar:", bg=BG)
        t.pack()
        self.e = Entry(self.jan)
        self.e.pack()
        t1 = Label(self.jan, text="Novo nome do contato:", bg=BG)
        t1.pack()
        self.e2 = Entry(self.jan)
        self.e2.pack()
        b = Button(self.jan, text="Alterar", bg=BTN, command=self.alterado)
        b.pack()

    def alterado(self):
        self.conn = self.conectaBanco()
        ide = self.e.get()
        novo_nome = self.e2.get()
        novo_nome = (novo_nome.capitalize())
        cursor = self.conn.cursor()
        comando = "UPDATE usuario SET nome='" + novo_nome + "' WHERE id='" + ide + "'"

        try:
            cursor.execute(comando)
            self.conn.commit()
            t = Label(self.jan, text="Alteração feita com sucesso!", bg=BG)
            t.pack()

        except:
            print("Erro")

        self.conn.close()

    def funcExcluir(self):
        self.jan = Tk()
        self.jan.geometry("200x100")
        self.jan.title("Excluir")
        self.jan['bg'] = BG
        t = Label(self.jan, text="Digite o ID do contato a excluir:", bg=BG)
        t.pack()
        self.e = Entry(self.jan)
        self.e.pack()
        b = Button(self.jan, text="Excluir", bg=BTN, command=self.excluido)
        b.pack()

    def excluido(self):
        self.conn = self.conectaBanco()
        ide_excluir = self.e.get()
        cursor = self.conn.cursor()
        comando = "DELETE FROM usuario WHERE id='" + ide_excluir + "'"

        try:
            cursor.execute(comando)
            self.conn.commit()
            t = Label(self.jan, text="Exclusão feita com sucesso.", bg=BG)
            t.pack()

        except:
            print("Erro")

        self.conn.close()

    def funMostrarTodos(self):
        self.jan = Tk()
        self.jan.geometry("200x600")
        self.jan.title("Nomes")
        self.jan['bg'] = BG
        self.conn = self.conectaBanco()
        resultados = 0
        cursor = self.conn.cursor()
        comando = ("SELECT * FROM usuario;")

        try:
            cursor.execute(comando)
            resultado = cursor.fetchall()

            for dados in resultado:
                ide = dados[0]
                nome = dados[1]

                resultados = int(resultados)
                resultados = resultados + 1
                t = Label(self.jan, text="ID: %s Nome: %s\n" %(ide, nome), bg=BG)
                t.pack()
                self.conn.commit()

        except:
            print("Erro")

        t1 = Label(self.jan, text="\nForam encontrados %s resultados\n" % resultados, bg=BG)
        t1.pack()
        self.conn.close()

    def sair(self):
        i.destroy()

# Cria a tela
i = Tk()
# Cria uma instancia do catalogador
Catalogador(i)
# Tamanho da tela
i.geometry("800x600")
# Titulo
i.title("Catalogador")
#icone
i.wm_iconbitmap("note.ico")
#background
i['bg'] = BG
#inicia tela
i = mainloop()
