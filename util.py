ocorrencias = []
lista_ocorrencia = []
historico_acoes = []

def gerarID(nome):
    soma = 0

    for letra in nome:
        soma = soma + ord(letra)

    codigo = soma % 10000
    prefixo = nome[:3].upper()

    return prefixo + "-" + str(codigo)

def gerarHash(cod):
    hash_cod = cod
    
    hash_cod ^ = hash_cod >> 16
    hash_cod *= 0x85ebca6b
    hash_cod &= 0xFFFFFFFF
    
    hash_cod ^ = hash_cod >> 13
    hash_cod *= 0xc2b2ae35
    return hash_cod % 55