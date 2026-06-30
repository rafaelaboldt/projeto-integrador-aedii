import time
from estrutura import ocorrencias, fila_ocorrencia, historico_acoes

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

def buscarOcorrencia(cod):
    posicao = gerarHash(cod)
    gaveta = ocorrencias[posicao]

    for chave, info in gaveta:
        if chave == cod:
            return info
    return None

def adicionaLog(texto):
    historico_acoes.append(texto)

def titulo(texto):
    print(f"\n >>> {texto} <<< \n")

def tempo(num):
    return time.sleep(num) 

def ordenarFilaOcorrencia(fila):
    n = len(fila)
    
    for i in range(n):
        flag = False
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
                flag = True
                
        if not flag:
            break
            
    return fila