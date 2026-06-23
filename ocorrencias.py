ocorrencias = []
historico_acoes = []

# def gerarID():

def cadastrar_ocorrencia():
    print("CADASTRO DE OCORRÊNCIAS")

    cod = input("Código: ")
    nome = input("Nome: ")
    tipo = input("Assunto: ")
    descricao = input("Descrição: ")
    prioridade = int(input("Prioridade (1-5): "))
    ordem = int(input("Ordem Chegada: "))
    status = input("Status: ")

    ocorrencias.append({cod, nome, tipo, descricao, prioridade, status})
    historico_acoes.append("Cadastro da Ocorrência {cod}")

def listar_ocorrencias():
    """Listar todas as ocorrências cadastradas."""
    print("Função listar_ocorrencias ainda não implementada.")


def atender_proxima_ocorrencia():
    print("Atendimento de Ocorrência por Ordem de chegada")

    print()

    for i in len(ocorrencias):

        

def atender_maior_prioridade():
    """Atender a ocorrência de maior prioridade."""
    print("Função atender_maior_prioridade ainda não implementada.")


def buscar_ocorrencia_por_id():
    """Buscar uma ocorrência por seu ID."""
    print("Função buscar_ocorrencia_por_id ainda não implementada.")


def buscar_ocorrencias_por_nome_ou_tipo():
    """Buscar ocorrências por nome ou tipo."""
    print("Função buscar_ocorrencias_por_nome_ou_tipo ainda não implementada.")


def ordenar_ocorrencias():
    """Ordenar a lista de ocorrências."""
    print("Função ordenar_ocorrencias ainda não implementada.")


def ver_historico_acoes():
    """Exibir o histórico de ações realizadas."""
    print("Função ver_historico_acoes ainda não implementada.")


def desfazer_ultima_acao():
    """Desfazer a última ação realizada."""
    print("Função desfazer_ultima_acao ainda não implementada.")
