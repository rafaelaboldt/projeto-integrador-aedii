from util import gerarHash, gerarID, titulo, adicionaLog, tempo
from estrutura import ocorrencias, fila_ocorrencia, historico_acoes

def cadastrar_ocorrencia():
    titulo("Cadastro de Ocorrências")

    nome = input("Nome: ")
    cod = gerarID(nome)
    tipo = input("Assunto: ")
    descricao = input("Descrição: ")
    prioridade = int(input("Prioridade (1-5): "))
    status = "Aberto"

    # levar o codigo pra função de gerar hash pra saber a posição da inserção na hash table
    posicao = gerarHash(cod) 
    
    dados = (nome, tipo, descricao, prioridade, status)

    #verificando se os campos estão vazios ou não
    if dados == "":
        return ("Os campos estão em branco!")
        
    if posicao not in ocorrencias:
        ocorrencias[posicao] = []

    #                             K  ,  V
    ocorrencias[posicao].append((cod, dados)) # dicionário com lista de tuplas
    fila_ocorrencia.append(cod)
    adicionaLog("Cadastro da Ocorrência {cod}")

    print(f"Ocorrência cadastrada com sucesso!")
    print(f"Código da Ocorrência: {cod}")