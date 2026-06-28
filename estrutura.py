from collections import deque

ocorrencias = {} # dicionário que armazena o cadastro das ocorrências
fila_ocorrencia = deque() # fila que armazena a ordem das ocorrências cadastradas
historico_acoes = [] # lista de logs