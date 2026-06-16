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
        pass
        # cadastrar_ocorrencia()
    elif opcao == "2":
        pass
        # listar_ocorrencias()
    elif opcao == "3":
        pass
        # atender_proxima_ocorrencia()
    elif opcao == "4":
        pass
        # atender_maior_prioridade()
    elif opcao == "5":
        pass
        # buscar_ocorrencia_por_id()
    elif opcao == "6":
        pass
        # buscar_ocorrencias_por_nome_ou_tipo()
    elif opcao == "7":
        pass
        # ordenar_ocorrencias()
    elif opcao == "8":
        pass
        # ver_historico_acoes()
    elif opcao == "9":
        pass
        # desfazer_ultima_acao()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")