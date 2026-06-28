from util import ocorrencias, lista_ocorrencia, historico_acoes, gerarHash, gerarID, buscarHash

def atender_proxima_ocorrencia():
    print("Atendimento de Ocorrência por Ordem de chegada")

    # print(" ID |        NOME        |    ASSUNTO    |              DESCRIÇÃO             |  STATUS  |")

#   pegamos a primeira ocorrencia
    primeira_ocorrencia = lista_ocorrencia[0]

#   enviamos para a def buscarHash
    result = buscarHash(primeira_ocorrencia)
    
#   
    print(result)

   








