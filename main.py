from bancoDados import BancoDados

dataColNames = ("nome", "matricula", "ano", "turma", "biologia", "quimica", "matematica", "fisica", "portugues", "historia", "geografia", "ingles", "religiao")

a = BancoDados("banco_alunos.db")
a.conectando()
a.del_old_table("dados")
a.criandoBD("dados")
a.inserirDados()

run = True

while run:
    matri = input("Matrícula (ou 'sair' para parar com a busca):")
    
    if matri == "sair":
        print("Fechando conexão!")
        a.desconectando()
        run = False
    
    elif matri.isalpha():
        print("Não é uma matrícula válida.")

    elif (int(matri) == 0) or (int(matri) > len(a.dados)):
        print("Não é uma matrícula válida.")

    else:    
        a.aluno(int(matri), dataColNames)
    