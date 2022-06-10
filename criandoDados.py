import pandas as pd
import random

nomes = pd.read_csv("nomes.txt", header=None)
matricula = list('%04d' % i for i in range(1,361))
ano = (6,7,8,9)*(int(len(matricula)/4))
turma = ("A","B","C")*(int(len(matricula)/3))

biologia = list(random.randrange(5, 10) for i in range(len(matricula)))
quimica = list(random.randrange(5, 10) for i in range(len(matricula)))
matematica = list(random.randrange(5, 10) for i in range(len(matricula)))
fisica = list(random.randrange(5, 10) for i in range(len(matricula)))
portugues = list(random.randrange(5, 10) for i in range(len(matricula)))
historia = list(random.randrange(5, 10) for i in range(len(matricula)))
geografia = list(random.randrange(5, 10) for i in range(len(matricula)))
ingles = list(random.randrange(5, 10) for i in range(len(matricula)))
religiao = list(random.randrange(5, 10) for i in range(len(matricula)))

dados = {"nome":nomes[0], "matricula": matricula, "ano": ano, "turma":turma, "biologia":biologia, "quimica": quimica, "matematica":matematica, "fisica":fisica, "portugues":portugues, "historia":historia, "geografia":geografia, "ingles":ingles, "religiao":religiao}

dadosAlunos = pd.DataFrame(dados)

print(dadosAlunos.head())

dadosAlunos.to_csv('dadosAlunos.csv', index=False)