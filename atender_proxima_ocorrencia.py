from util import historico_acoes, adicionaLog, tempo, titulo, buscarOcorrencia
from estrutura import deque, fila_ocorrencia, historico_acoes, ocorrencias

def atender_proxima_ocorrencia():
    titulo("Atendimento de Ocorrência (Ordem de chegada)")

    # print("         NOME        |    ASSUNTO    |              DESCRIÇÃO             | PRIORIDADE |  STATUS  |")

#   verifica se a fila de ocorrências está vazia ou não
    if len(fila_ocorrencia) == 0:
        return ("Não há mais ocorrências")
    
#   pegamos a primeira ocorrencia
    primeira_ocorrencia = fila_ocorrencia[0]


#   enviamos para a def buscarOcorrencia
    result = buscarOcorrencia(primeira_ocorrencia)

#   mostrar os dados da primeira ocorrência    
    for dados in result:
        print(dados, end=" | ")

    print()
    tempo(3)
    confirm = input(f"Confirmar atendimento da ocorrência {primeira_ocorrencia}: ( y / n ) ").upper()
    if confirm == "Y":
        adicionaLog(f"Confirmação da ocorrência {primeira_ocorrencia} atendida pela ordem de chegada.")
        ocorrencia_apagada = fila_ocorrencia.popleft()
#        tem que apagar da hash table também 
        tempo(1)
        adicionaLog(f"Ocorrência {ocorrencia_apagada} deletada da fila de ocorrências")
        print(f"Atendimento confirmado para a Ocorrência {ocorrencia_apagada}")
        tempo(1)
    elif confirm == "N":
        print("Nenhuma ação realizada!")
        tempo(1)
    else:
        print("Apenas 'y'ou 'n'")
        tempo(1)


   








