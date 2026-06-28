ocorrencias = {} # dicionário que armazena o cadastro das ocorrências
lista_ocorrencia = [] # lista que armazena a ordem das ocorrências cadastradas
historico_acoes = [] # lista de logs

def gerarID(nome):
    soma = 0

    for letra in nome:
        soma = soma + ord(letra)

    codigo = soma % 10000
    prefixo = nome[:3].upper()

    return prefixo + "-" + str(codigo)

def gerarHash(cod):
    hash_val = 5381

    for char in cod:
        hash_val = ((hash_val << 5) + hash_val) + ord(char)

    return hash_val % 55

def buscarHash(cod):
    posicao = gerarHash(cod)
    gaveta = ocorrencias[posicao]

    for chave, info in gaveta:
        if chave == cod:
            return info
    return None






 
