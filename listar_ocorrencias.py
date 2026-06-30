from util import titulo, buscarOcorrencia
from estrutura import fila_ocorrencia, ocorrencias

def listar_ocorrencias():

    titulo("Listar Ocorrências")

    if not ocorrencias:
        print("Nenhuma ocorrência cadastrada.")
        return

    for i in fila_ocorrencia:
        ocorrencia = buscarOcorrencia(i)
        if ocorrencia:
            print(f"Código: {i} - Nome: {ocorrencia[0]} - Tipo: {ocorrencia[1]} - Prioridade: {ocorrencia[3]} - Status: {ocorrencia[4]}")
