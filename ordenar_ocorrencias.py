from util import historico_acoes, buscarOcorrencia , adicionaLog, tempo, titulo, ordenarFilaOcorrencia
from estrutura import deque, fila_ocorrencia, historico_acoes, ocorrencias, ocorrencias_ordenadas, fila_ocorrencia_ordenada

def ordenar_ocorrencias():
    titulo("Ordernar Ocorrência por ID")

    for i in fila_ocorrencia:
        fila_ocorrencia_ordenada.append(i)

    fila_ordenada = ordenarFilaOcorrencia(fila_ocorrencia_ordenada)

    print(fila_ordenada) # ['BRU-504', 'ELI-282', 'LUI-510', 'MAR-613', 'SAB-704', 'TIT-416']

    for i in fila_ordenada:
        ocorrencia = buscarOcorrencia(i)
        print(f"Ocorrencia buscada: {ocorrencia}")
        if ocorrencia:
            ocorrencias_ordenadas.append(ocorrencia)
            print(f"Ocorrencia ordenada: {ocorrencias_ordenadas}")

    print("Fila de Ocorrencias Ordenadas:")
    print(ocorrencias_ordenadas)

    