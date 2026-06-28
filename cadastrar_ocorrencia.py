from util import ocorrencias, lista_ocorrencia, historico_acoes, gerarHash, gerarID

def cadastrar_ocorrencia():
    print("CADASTRO DE OCORRÊNCIAS")

    nome = input("Nome: ")
    cod = gerarID(nome)
    tipo = input("Assunto: ")
    descricao = input("Descrição: ")
    prioridade = int(input("Prioridade (1-5): "))
    status = "Aberto"

    # levar o codigo pra função de gerar hash pra saber a posição da inserção na hash table
    posicao = gerarHash(cod) 
    
    dados = (nome, tipo, descricao, prioridade, status)

    if posicao not in ocorrencias:
        ocorrencias[posicao] = []

    #                             K  ,  V
    ocorrencias[posicao].append((cod, dados))
    lista_ocorrencia.append(cod)
    historico_acoes.append("Cadastro da Ocorrência {cod}")

    print(ocorrencias)

    print(f"Ocorrência cadastrada com sucesso! Código: {cod}")