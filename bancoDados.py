import psycopg2
import pandas as pd
# import numpy as np

class BancoDados():
    def __init__(self, nomeBanco):
        self.nomeBanco = nomeBanco
        self.conn = None
        self.cur = None
        self.nome_tabela = None
        self.dados = None
        print('\nBancoDados instanciado\n')

    def conectando(self):
        self.conn = psycopg2.connect(host="localhost",
            database= self.nomeBanco,
            user= "postgres",
            password= 'test')
        print("Conectado em: %s\n" %self.nomeBanco)

    def run_sql(self, sql): 
        self.cur = self.conn.cursor()
        newSql = self.cur.mogrify(sql);
        self.cur.execute(newSql)
        self.conn.commit()

    def desconectando(self):
        self.conn.close()
        self.conn = None
        print("Desconectado a %s" %self.nomeBanco)

    def criandoBD(self, nome_tabela):
        self.nome_tabela = nome_tabela

        comando = """CREATE TABLE %s (nome VARCHAR(20), 
            matricula INTEGER, 
            ano INTEGER, 
            turma VARCHAR(1), 
            biologia INTEGER, 
            quimica INTEGER, 
            matematica INTEGER, 
            fisica INTEGER, 
            portugues INTEGER, 
            historia INTEGER, 
            geografia INTEGER, 
            ingles INTEGER, 
            religiao INTEGER)""" %(self.nome_tabela)

        self.run_sql(comando)
        print('Criada a table de dados com o nome de: ' + self.nome_tabela)

    def del_old_table(self, table_name): # deletar a tabela que estiver no banco de dados para armazenar a nova
        sql = 'DROP TABLE IF EXISTS public.%s CASCADE' % (table_name)
        self.run_sql(sql)

    def inserirDados(self):
        self.dados = pd.read_csv("dadosAlunos.csv")
        dados = self.dados
        for i in range(0, len(dados)):
            comando = """INSERT INTO %s (nome, matricula, ano, turma, biologia, quimica, matematica, fisica, portugues, historia, geografia, ingles, religiao) VALUES('%s','%i','%i','%s','%i','%i','%i','%i','%i','%i','%i','%i','%i');""" %(self.nome_tabela, dados["nome"][i], dados["matricula"][i], dados["ano"][i], dados["turma"][i], dados["biologia"][i], dados["quimica"][i], dados["matematica"][i], dados["fisica"][i], dados["portugues"][i], dados["historia"][i], dados["geografia"][i], dados["ingles"][i], dados["religiao"][i])
            self.run_sql(comando)
    
    def call_db(self, sql):
        conexao = self.conn
        cur = conexao.cursor()
        cur.execute(sql)
        recset = cur.fetchall()
        data_row = []
        for rec in recset:
            data_row.append(rec)
        return data_row

    def aluno(self, matricula, *colNames):
        dataColNames = colNames[0]
        comando = """SELECT * FROM %s WHERE matricula = %d;""" %(self.nome_tabela, matricula)
        reg = self.call_db(comando)
        df_bd = pd.DataFrame(reg, columns = dataColNames)   
        df_bd_trans = df_bd.T           
        print("\n### Dados do aluno ###\n\n", df_bd_trans[0].to_string(), "\n")
