from util import tempo, titulo
from estrutura import historico_acoes


def ver_historico_acoes():
    
    titulo("Histórico de ações")

    if not historico_acoes:
        print("Nenhuma ação registrada ainda.")
        return

    print("Últimas ações realizadas (Topo da Pilha):\n")
    for indice, acao in enumerate(reversed(historico_acoes), start=1):
        print(f"{indice} - {acao}")

    tempo(1)