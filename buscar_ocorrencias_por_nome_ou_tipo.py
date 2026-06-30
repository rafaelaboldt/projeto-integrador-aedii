from util import adicionaLog, tempo, titulo
from estrutura import ocorrencias


def buscar_ocorrencias_por_nome_ou_tipo():
    """Buscar ocorrências por nome ou tipo."""
    titulo("Busca de ocorrências")

    termo = input("Digite um nome ou tipo para buscar: ").strip()
    if not termo:
        print("Informe um termo para buscar.")
        return

    termo_busca = termo.lower()

    hash_table_busca = {}

    for gaveta in ocorrencias.values():
        for cod, dados in gaveta:
            nome, tipo, descricao, prioridade, status = dados

            chaves = set(nome.lower().split() + tipo.lower().split() + [nome.lower(), tipo.lower()])
            
            for chave in chaves:
                if chave not in hash_table_busca:
                    hash_table_busca[chave] = []
                hash_table_busca[chave].append((cod, dados))

    resultados = hash_table_busca.get(termo_busca, [])

    if not resultados:
        print("Nenhuma ocorrência encontrada.")
        return

    for cod, dados in resultados:
        nome, tipo, descricao, prioridade, status = dados
        print(f"Código: {cod}")
        print(f"Nome: {nome}")
        print(f"Tipo: {tipo}")
        print(f"Descrição: {descricao}")
        print(f"Prioridade: {prioridade}")
        print(f"Status: {status}")
        print("-" * 40)

    adicionaLog(f"Busca por '{termo}' realizada.")
    tempo(1)