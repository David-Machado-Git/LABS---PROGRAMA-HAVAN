

print('--' * 35)
print(f'\033[7;40m{"   GERENCIADOR DE OPERAÇÕES  ":*^70}\033[0;0m')
print('--' * 35)

while True:
    print(f'     |-- {"OPÇÃO  ":-<2}{"   MENU   ":-^38}            |')
    print(f'     |\033[7;40m{"--   1  ":.<3} |{" - CADASTRAR CLIENTES - ":^38}            \033[0;0m|')
    print(f'     |{"--   2  ":.<3} |{" - LISTAR OPERAÇÕES - ":^38}            |')
    print(f'     |\033[7;40m{"--   3  ":.<3} |{" - VALOR TOTAL DAS OPERAÇÕES - ":^38}            \033[0;0m|')
    print(f'     |{"--   4  ":.<3} |{" - VALOR TOTAL DAS TAXAS COBRADAS - ":^38}            |')
    print('--' * 35)
    print(f'\033[7;40m{"   ESCOLHA UMA DAS OPÇÕES ACIMA:  ":*^70}\033[0;0m')
    print('--' * 35)
    opcao_menu = str(input('Digite a opção desejada:?'))

    if opcao_menu.isnumeric():
        if opcao_menu == '1':
            print('--' * 35)
            print(f'\033[7;40m{"   CADASTRAR CLIENTES  ":*^70}\033[0;0m')
            print('--' * 35)
            nome = str(input('Digite o nome do cliente:?'))
            print('--' * 30)
            print('-------------------   MOEDAS CADASTRADAS   -------------------')
            print('       | Digite --> (1) para MOEDA REAL - BRASIL   |')
            print('       | Digite --> (2) para MOEDA DÓLAR - EUA     |')
            print('       | Digite --> (3) para MOEDA EURO - EUROPA   |')
            print('       | Digite --> (4) para MOEDA DÓLAR - CANADÁ  |')
            print('        -------------------------------------------')
            moeda_origem = str(input('Moeda de origem: [somente número acima]:?'))
            print('--' * 30)

            if moeda_origem == '1':
                print('MOEDA DE ORIGEM: - REAL - BRASIL')

            elif moeda_origem == '2':
                print('MOEDA DE ORIGEM: - DÓLAR - EUA')

            elif moeda_origem == '3':
                print('MOEDA DE ORIGEM: - EURO - EUROPA')

            elif moeda_origem == '4':
                print('MOEDA DE ORIGEM: - DÓLAR - CANADÁ')

            print('--' * 30)
            print('-------------------   MOEDAS CADASTRADAS   -------------------')
            print('       | Digite --> (1) para MOEDA REAL - BRASIL   |')
            print('       | Digite --> (2) para MOEDA DÓLAR - EUA     |')
            print('       | Digite --> (3) para MOEDA EURO - EUROPA   |')
            print('       | Digite --> (4) para MOEDA DÓLAR - CANADÁ  |')
            print('        -------------------------------------------')
            moeda_destino = str(input('Moeda de destino:?'))
            print('--' * 30)
            if moeda_destino == '1':
                print('MOEDA DE DESTINO: - REAL - BRASIL')

            elif moeda_destino == '2':
                print('MOEDA DE DESTINO: - DÓLAR - EUA')

            elif moeda_destino == '3':
                print('MOEDA DE DESTINO: - EURO - EUROPA')

            elif moeda_destino == '4':
                print('MOEDA DE DESTINO: - DÓLAR - CANADÁ')

            print('--' * 30)
            data_operacao = str(input('Data da operação:?'))
            print('--' * 30)
            valor_original = str(input('Valor original:?'))
            print('--' * 30)
            valor_convertido = str(input('Valor convertido:?'))
            print('--' * 30)
            taxa_cobrada = str(input('Taxa cobrada:?'))

            break

        elif opcao_menu == '2':
            print('--' * 35)
            print(f'\033[7;40m{"   RELATÓRIOS --> OPERAÇÕES REALIZADAS  ":*^70}\033[0;0m')
            print('--' * 35)
            print('(2a) - FALTA CONSTRUIR - ')

        elif opcao_menu == '3':
            print('Faz outra coisa...3')

        elif opcao_menu == '4':
            print('Faz outra coisa...4')

        else:
            while True:
                print('--' * 30)
                print(f'\033[1;41m- SOMENTE NÚMEROS DE 1 A 4 QUE CORRESPONDEM AS OPÇÕES DO MENU:\033[0;0m')
                print('--' * 30)
                opcao_menu = str(input('Digite a opção desejada:?'))
                print('--' * 30)


    else:
        while True:
            print('--' * 30)
            print(f'\033[1;41m- SOMENTE NÚMEROS DE 1 A 4 QUE CORRESPONDEM AS OPÇÕES DO MENU:\033[0;0m')
            print('--' * 30)
            opcao_menu = str(input('Digite a opção desejada:?'))
            print('--' * 30)

            if opcao_menu == '1':
                print('--' * 35)
                print(f'\033[7;40m{"   CADASTRO  ":*^70}\033[0;0m')
                print('--' * 35)
                nome = str(input('Digite o nome do cliente:?'))
                print('--' * 30)
                moeda_origem = str(input('Moeda de origem:?'))
                print('--' * 30)
                moeda_destino = str(input('Moeda de destino:?'))
                print('--' * 30)
                data_operacao = str(input('Data da operação:?'))
                print('--' * 30)
                valor_original = str(input('Valor original:?'))
                print('--' * 30)
                valor_convertido = str(input('Valor convertido:?'))
                print('--' * 30)
                taxa_cobrada = str(input('Taxa cobrada:?'))

                break

# - FIM DO PROGRAMA
    break


# --> FIM CADASTRO

