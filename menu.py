from cadastrar_ocorrencia import cadastrar_ocorrencia
from listar_ocorrencias import listar_ocorrencias
from atender_proxima_ocorrencia import atender_proxima_ocorrencia
from atender_maior_prioridade import atender_maior_prioridade
from buscar_ocorrencia_por_id import buscar_ocorrencia_por_id
from buscar_ocorrencias_por_nome_ou_tipo import buscar_ocorrencias_por_nome_ou_tipo
from ordenar_ocorrencias import ordenar_ocorrencias
from ver_historico_acoes import ver_historico_acoes
from desfazer_ultima_acao import desfazer_ultima_acao


while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar ocorrência")
    print("2 - Listar todas as ocorrências")
    print("3 - Atender próxima ocorrência pela fila")
    print("4 - Atender ocorrência de maior prioridade")
    print("5 - Buscar ocorrência por ID")
    print("6 - Buscar ocorrências por nome ou tipo")
    print("7 - Ordenar ocorrências")
    print("8 - Ver histórico de ações")
    print("9 - Desfazer última ação")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_ocorrencia()
    elif opcao == "2":
        listar_ocorrencias()
    elif opcao == "3":
        atender_proxima_ocorrencia()
    elif opcao == "4":
        atender_maior_prioridade()
    elif opcao == "5":
        buscar_ocorrencia_por_id()
    elif opcao == "6":
        buscar_ocorrencias_por_nome_ou_tipo()
    elif opcao == "7":
        ordenar_ocorrencias()
    elif opcao == "8":
        ver_historico_acoes()
    elif opcao == "9":
        desfazer_ultima_acao()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")