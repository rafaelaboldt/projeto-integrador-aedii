def cadastrar_ocorrencia():
    print("CADASTRO DE OCORRÊNCIAS")

    nome = input("Nome: ")
    cod = gerarID(nome)
    tipo = input("Assunto: ")
    descricao = input("Descrição: ")
    prioridade = int(input("Prioridade (1-5): "))
    status = input("Status: ")

    ocorrencias.append({cod, nome, tipo, descricao, prioridade, status})
    historico_acoes.append("Cadastro da Ocorrência {cod}")