from time import sleep

dados = {}
lista_de_dados = []
lista_principal = []
copia_dados = []
copia_dados_a = {}
codigo_cliente = 0
busca_por_cod = {}
busca_por_nome = {}
busca_por_telefone = {}
busca_por_data = {}
moeda_origem = 'R$:'
moeda_destino = 'U$$:'


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
            while True:
                print('--' * 35)
                print(f'\033[7;40m{"   CADASTRAR CLIENTES  ":*^70}\033[0;0m')
                print('--' * 35)
                codigo_cliente += 1
                cod_cadastro_cliente = str(codigo_cliente).upper()
                lista_de_dados.append(cod_cadastro_cliente)
                print(f' --> {codigo_cliente}º Cadastro e Nº do Cliente [ {codigo_cliente} ]')
                dados['Cód'] = [codigo_cliente]
                # print('--' * 35)
                # print(f'TESTE DADOS EM FORMA DE DICIONÁRIOS: {dados.values()}')
                print('--' * 35)
                nome = str(input('Digite o nome do cliente:?')).strip().upper()
                dados['Nome'] = [nome]
                lista_de_dados.append(nome)
                # print(f'TESTE DADOS: {dados}')
                print('--' * 30)
                print('-------------------   MOEDAS CADASTRADAS   -------------------')
                print('       | Digite --> (1) para MOEDA REAL - BRASIL   |')
                print('       | Digite --> (2) para MOEDA DÓLAR - EUA     |')
                print('       | Digite --> (3) para MOEDA EURO - EUROPA   |')
                print('       | Digite --> (4) para MOEDA DÓLAR - CANADÁ  |')
                print('        -------------------------------------------')
                moeda_origem = str(input('Moeda de origem?: [somente números acima]:?'))

                dados['Moeda origem'] = [moeda_origem]

                print('--' * 30)
                ##### --> DESATIVADO TEMPORARIAMENTE - REATIVAR FUTURAMENTE
                if moeda_origem == '1':
                    print('MOEDA DE ORIGEM: - REAL - BRASIL')
                    dados['Moeda origem'] = ['REAL - BRL']
                    moeda_origem = 'R$:'
                    lista_de_dados.append('REAL - BRL')
                    # print(f'TESTE MOEDA DE ORIGEM: {dados}')

                elif moeda_origem == '2':
                    print('MOEDA DE ORIGEM: - DÓLAR - EUA')
                    dados['Moeda origem'] = ['DÓLAR - EUA']
                    moeda_origem = 'U$$:'
                    lista_de_dados.append('DÓLAR - EUA')
                    # print(f'TESTE MOEDA DE ORIGEM: {dados}')

                elif moeda_origem == '3':
                    print('MOEDA DE ORIGEM: - EURO - EUROPA')
                    dados['Moeda origem'] = ['EURO']
                    moeda_origem = '€:'
                    lista_de_dados.append('EURO')
                    # print(f'TESTE MOEDA DE ORIGEM: {dados}')

                elif moeda_origem == '4':
                    print('MOEDA DE ORIGEM: - DÓLAR - CANADÁ')
                    dados['Moeda origem'] = ['DÓLAR - CAD']
                    moeda_origem = 'U$$:'
                    lista_de_dados.append('DÓLAR - CAD')
                    # print(f'TESTE MOEDA DE ORIGEM: {dados}')

                else:
                    while True:
                        print(f'\033[1;41mVALOR INVÁLIDO - SOMENTE NÚMEROS DE 1 A 4 QUE CORRESPONDEM AS MOEDAS CADASTRADAS:\033[0;0m')
                        print('--' * 30)
                        print('-------------------   MOEDAS CADASTRADAS   -------------------')
                        print('       | Digite --> (1) para MOEDA REAL - BRASIL   |')
                        print('       | Digite --> (2) para MOEDA DÓLAR - EUA     |')
                        print('       | Digite --> (3) para MOEDA EURO - EUROPA   |')
                        print('       | Digite --> (4) para MOEDA DÓLAR - CANADÁ  |')
                        print('        -------------------------------------------')
                        moeda_origem = str(input('Moeda de origem?: [somente números acima]:?'))
                        print('--' * 30)
                        ##### --> DESATIVADO TEMPORARIAMENTE - REATIVAR FUTURAMENTE
                        if moeda_origem == '1':
                            print('MOEDA DE ORIGEM: - REAL - BRASIL')
                            dados['Moeda origem'] = ['REAL - BRL']
                            moeda_origem = 'R$:'
                            lista_de_dados.append('REAL - BRL')
                            # print(f'TESTE MOEDA DE ORIGEM: {dados}')
                            break

                        elif moeda_origem == '2':
                            print('MOEDA DE ORIGEM: - DÓLAR - EUA')
                            dados['Moeda origem'] = ['DÓLAR - EUA']
                            moeda_origem = 'U$$:'
                            lista_de_dados.append('DÓLAR - EUA')
                            # print(f'TESTE MOEDA DE ORIGEM: {dados}')
                            break

                        elif moeda_origem == '3':
                            print('MOEDA DE ORIGEM: - EURO - EUROPA')
                            dados['Moeda origem'] = ['EURO']
                            moeda_origem = '€:'
                            lista_de_dados.append('EURO')
                            # print(f'TESTE MOEDA DE ORIGEM: {dados}')
                            break

                        elif moeda_origem == '4':
                            print('MOEDA DE ORIGEM: - DÓLAR - CANADÁ')
                            dados['Moeda origem'] = ['DÓLAR - CAD']
                            moeda_origem = 'U$$:'
                            lista_de_dados.append('DÓLAR - CAD')
                            # print(f'TESTE MOEDA DE ORIGEM: {dados}')
                            break

                print('--' * 30)
                print('-------------------   MOEDAS CADASTRADAS   -------------------')
                print('       | Digite --> (1) para MOEDA REAL - BRASIL   |')
                print('       | Digite --> (2) para MOEDA DÓLAR - EUA     |')
                print('       | Digite --> (3) para MOEDA EURO - EUROPA   |')
                print('       | Digite --> (4) para MOEDA DÓLAR - CANADÁ  |')
                print('        -------------------------------------------')
                moeda_destino = str(input('Moeda de destino?: [somente números acima]:?'))
                print('--' * 30)

                ##### --> DESATIVADO TEMPORARIAMENTE - REATIVAR FUTURAMENTE
                if moeda_destino == '1':
                    print('MOEDA DE DESTINO: - REAL - BRASIL')
                    dados['Moeda destino'] = ['REAL - BRASIL']
                    moeda_destino = 'R$:'
                    lista_de_dados.append('REAL - BRASIL')
                    # print(f'TESTE MOEDA DE ORIGEM: {dados}')

                elif moeda_destino == '2':
                    print('MOEDA DE DESTINO: - DÓLAR - EUA')
                    dados['Moeda destino'] = ['DÓLAR - EUA']
                    moeda_destino = 'U$$:'
                    lista_de_dados.append('DÓLAR - EUA')
                    # print(f'TESTE MOEDA DE ORIGEM: {dados}')

                elif moeda_destino == '3':
                    print('MOEDA DE DESTINO: - EURO - EUROPA')
                    dados['Moeda destino'] = ['EURO']
                    moeda_destino = '€:'
                    lista_de_dados.append('EURO')
                    # print(f'TESTE MOEDA DE ORIGEM: {dados}')

                elif moeda_destino == '4':
                    print('MOEDA DE DESTINO: - DÓLAR - CANADÁ')
                    dados['Moeda destino'] = ['DÓLAR CAD']
                    moeda_destino = 'U$$:'
                    lista_de_dados.append('DÓLAR CAD')
                    # print(f'TESTE MOEDA DE ORIGEM: {dados}')

                else:
                    while True:
                        print(f'\033[1;41mVALOR INVÁLIDO - SOMENTE NÚMEROS DE 1 A 4 QUE CORRESPONDEM AS MOEDAS CADASTRADAS:\033[0;0m')
                        print('--' * 30)
                        print('-------------------   MOEDAS CADASTRADAS   -------------------')
                        print('       | Digite --> (1) para MOEDA REAL - BRASIL   |')
                        print('       | Digite --> (2) para MOEDA DÓLAR - EUA     |')
                        print('       | Digite --> (3) para MOEDA EURO - EUROPA   |')
                        print('       | Digite --> (4) para MOEDA DÓLAR - CANADÁ  |')
                        print('        -------------------------------------------')
                        moeda_destino = str(input('Moeda de destino?: [somente números acima]:?'))
                        print('--' * 30)

                        ##### --> DESATIVADO TEMPORARIAMENTE - REATIVAR FUTURAMENTE
                        if moeda_destino == '1':
                            print('MOEDA DE DESTINO: - REAL - BRASIL')
                            dados['Moeda destino'] = ['REAL - BRASIL']
                            moeda_destino = 'R$:'
                            lista_de_dados.append('REAL - BRASIL')
                            # print(f'TESTE MOEDA DE ORIGEM: {dados}')
                            break

                        elif moeda_destino == '2':
                            print('MOEDA DE DESTINO: - DÓLAR - EUA')
                            dados['Moeda destino'] = ['DÓLAR - EUA']
                            moeda_destino = 'U$$:'
                            lista_de_dados.append('DÓLAR - EUA')
                            # print(f'TESTE MOEDA DE ORIGEM: {dados}')
                            break

                        elif moeda_destino == '3':
                            print('MOEDA DE DESTINO: - EURO - EUROPA')
                            dados['Moeda destino'] = ['EURO']
                            moeda_destino = '€:'
                            lista_de_dados.append('EURO')
                            # print(f'TESTE MOEDA DE ORIGEM: {dados}')
                            break

                        elif moeda_destino == '4':
                            print('MOEDA DE DESTINO: - DÓLAR - CANADÁ')
                            dados['Moeda destino'] = ['DÓLAR CAD']
                            moeda_destino = 'U$$:'
                            lista_de_dados.append('DÓLAR CAD')
                            # print(f'TESTE MOEDA DE ORIGEM: {dados}')
                            break

                print('--' * 30)
                data_operacao = str(input('Data da operação:?'))

                dados['Data Operação'] = [data_operacao]
                lista_de_dados.append(data_operacao)
                # print(f'TESTE DATA: {dados}')
                print('--' * 30)
                valor_original = str(input(f'Valor original:? {moeda_origem}'))
                dados['Valor Original'] = [valor_original]
                lista_de_dados.append(valor_original)
                # print(f'TESTE VALOR ORIGINAL: {dados}')
                print('--' * 30)
                valor_convertido = str(input(f'Valor convertido:? {moeda_destino}'))

                dados['Valor Convertido'] = [valor_convertido]
                lista_de_dados.append(valor_convertido)
                # print(f'TESTE VALOR CONVERTIDO: {dados}')
                print('--' * 30)
                taxa_cobrada = str(input(f'Taxa cobrada:? R$:'))
                dados['Taxa Cobrada'] = [taxa_cobrada]
                lista_de_dados.append(taxa_cobrada)
                # print(f'TESTE LISTA NORMAL DE DADOS: {dados}')
                print('--' * 30)
                copia_dados.append(dados.copy())
                lista_principal.append(lista_de_dados)
                dados_p_copia_nome = lista_principal[-1][1]
                busca_por_nome[dados_p_copia_nome] = lista_principal

                dados_p_copia_data = lista_principal[-1][4]
                busca_por_data[dados_p_copia_data] = lista_principal
                ###---> TRABALHANDO AQUI...
                # dados_p_copia_nome = dados[-1][1]
                # print(f'TESTE LISTA CÓPA DE DADOS: {copia_dados}')
                print('--' * 30)
                # dados.clear()
                # print(f'TESTE LISTA NORMAL DE DADOS: {dados}')

                print('--' * 30)

                # --> NÃO APAGAR OS CÓDIGOS ABAIXO <--
                # --> ESSA SOLUÇÃO SERIA PARA LISTAR TODOS OS CLIENTES E INFORMAÇÕES <--
                # print(' --------------------  |SEQUÊNCIA E ORDEM DE COLUNAS|  -------------- VALORES -------------')
                # print('1ºCÓD:|2ºNOME:        |3ºMOED ORIG. |4º MOED DEST.  |5º DATA:   |6ºORIGI:|7ºCONV:|8ºTAXA. ')
                # print('---' * 30)
                # for c, v in enumerate(copia_dados):
                #     for d in v.values():
                #         print(f"  {str(d).replace('[','').replace(']','').replace('','')}",end=' ')
                #     print()








                while True:
                    print('')
                    continua_cadastro = str(input('\nCadastrar mais clientes:? [C - P/ CONTINUAR OU S - P/ SAIR]:?')).strip().upper()[0]

                    if continua_cadastro == 'C':
                        break

                    elif continua_cadastro == 'S':
                        break

                    else:
                        print(f'\033[1;41m- SOMENTE UMA DAS OPÇÕES ACIMA: [C - CONTINUAR/ S - SAIR]:\033[0;0m')

                if continua_cadastro == 'S':
                    print('--' * 35)
                    print('             \033[1;30m\033[1;43m     CARREGANDO MENU PRINCIPAL\033[0;0m', end='')
                    sleep(0.3)
                    print('\033[1;30m\033[1;43m.\033[0;0m', end='')
                    sleep(0.3)
                    print('\033[1;30m\033[1;43m.\033[0;0m', end='')
                    sleep(0.3)
                    print('\033[1;30m\033[1;43m.\033[0;0m', end='')
                    sleep(0.3)
                    print('\033[1;30m\033[1;43m50%\033[0;0m', end='')
                    sleep(0.8)
                    print('\033[1;30m\033[1;43m.\033[0;0m', end='')
                    sleep(0.8)
                    print('\033[1;30m\033[1;43m.\033[0;0m', end='')
                    sleep(0.8)
                    print('\033[1;30m\033[1;43m100%\033[0;0m', end='')
                    print('\033[1;30m\033[1;43m   \033[0;0m', end='')
                    print('\n')

                    break


        elif opcao_menu == '2':
            print('--' * 35)
            print(f'\033[7;40m{"   RELATÓRIOS --> OPERAÇÕES REALIZADAS  ":*^70}\033[0;0m')
            print('--' * 35)
            if codigo_cliente == 0:
                print('--' * 35)
                print('        \033[1;40m    Aguarde ! AVERIGUANDO DADOS\033[0;0m', end='')
                sleep(0.3)
                print('\033[1;40m.\033[0;0m', end='')
                sleep(0.3)
                print('\033[1;40m.\033[0;0m', end='')
                sleep(0.3)
                print('\033[1;40m.\033[0;0m', end='')
                sleep(0.3)
                print('\033[1;40m50%\033[0;0m', end='')
                sleep(0.8)
                print('\033[1;40m.\033[0;0m', end='')
                sleep(0.8)
                print('\033[1;40m.\033[0;0m', end='')
                sleep(0.8)
                print('\033[1;40m100%\033[0;0m', end='')
                print('\033[1;40m   \033[0;0m', end='')
                print('\n')

                print('--' * 35)
                print()
                print()
                print('\033[1;41mATÉ O PRESENTE MOMENTO NÃO HÁ NENHUMA OPERAÇÃO REALIZADA !\033[0;0m')
                print()
                print()
                print('--' * 35)
                print('--' * 35)
                print('             \033[1;30m\033[1;43m     VOLTANDO AO MENU PRINCIPAL\033[0;0m', end='')
                sleep(0.3)
                print('\033[1;30m\033[1;43m.\033[0;0m', end='')
                sleep(0.3)
                print('\033[1;30m\033[1;43m.\033[0;0m', end='')
                sleep(0.3)
                print('\033[1;30m\033[1;43m.\033[0;0m', end='')
                sleep(0.3)
                print('\033[1;30m\033[1;43m50%\033[0;0m', end='')
                sleep(0.8)
                print('\033[1;30m\033[1;43m.\033[0;0m', end='')
                sleep(0.8)
                print('\033[1;30m\033[1;43m.\033[0;0m', end='')
                sleep(0.8)
                print('\033[1;30m\033[1;43m100%\033[0;0m', end='')
                print('\033[1;30m\033[1;43m   \033[0;0m', end='')
                print('\n')

            elif codigo_cliente > 0:
                print('--' * 35)
                print('        \033[1;40m    Aguarde ! AVERIGUANDO DADOS\033[0;0m', end='')
                sleep(0.3)
                print('\033[1;40m.\033[0;0m', end='')
                sleep(0.3)
                print('\033[1;40m.\033[0;0m', end='')
                sleep(0.3)
                print('\033[1;40m.\033[0;0m', end='')
                sleep(0.3)
                print('\033[1;40m50%\033[0;0m', end='')
                sleep(0.8)
                print('\033[1;40m.\033[0;0m', end='')
                sleep(0.8)
                print('\033[1;40m.\033[0;0m', end='')
                sleep(0.8)
                print('\033[1;40m100%\033[0;0m', end='')
                print('\033[1;40m   \033[0;0m', end='')
                print('\n')

                print('--' * 35)
                print()
                print()
                print(f'\033[1;42mATÉ O PRESENTE MOMENTO VOCÊ TEM UM TOTAL DE: {codigo_cliente} \033[0;0m',end='')
                if codigo_cliente == 1:
                    print('\033[1;42mOPERAÇÃO !\033[0;0m')
                else:
                    print('\033[1;42mOPERAÇÕES !\033[0;0m')
                print('--' * 35)
                print(' -- | ABAIXO SEGUE A LISTA COMPLETA DE TODOS OS CLIENTES CADASTRADOS ATÉ O MOMENTO! | -- ')
                print('--' * 35)
                print(' --------------------  |SEQUÊNCIA E ORDEM DE COLUNAS|  -------------- VALORES -------------')
                print('1ºCÓD:|2ºNOME:        |3ºMOED ORIG. |4º MOED DEST.  |5º DATA:   |6ºORIGI:|7ºCONV:|8ºTAXA. ')
                print('---' * 30)
                for c, v in enumerate(copia_dados):
                    for d in v.values():
                        print(f"  {str(d).replace('[', '').replace(']', '').replace('', '')}", end=' ')
                    print()
                print()
                print()
                while True:
                    pesquisa = str(input('Digite cliente ou dados a pesquisar:?')).upper()

                    if pesquisa in busca_por_nome.keys():
                        print('--' * 35)
                        print(f'\033[1;42mBusca Realizada com sucesso !\033[0;0m')
                        print(f'A busca com esse nome pertence ao cadastro')
                        print(f'{busca_por_nome[f"{pesquisa}"]}')
                        print('--' * 35)

                    elif pesquisa in busca_por_data.keys():
                        print('--' * 35)
                        print(f'\033[1;42mBusca Realizada com sucesso !\033[0;0m')
                        print(f'A busca com esse nome pertence ao cadastro')
                        print(f'{busca_por_data[f"{pesquisa}"]}')
                        print('--' * 35)

                    else:
                        print(f'Infelizmente não conseguimos encontrar nenhum id com esse número !')

                # busca_dados_var = f'{copia_dados}'.index(busca_dados_dicionario)
                # print(f'{dados}')

                print('--' * 35)
                print('--' * 35)
                while True:
                    voltar_menu_principal = str(input('Para voltar ao menu principal digite [S]-SAIR:')).strip().upper()[0]
                    if voltar_menu_principal == 'S':
                        break
                    else:
                        print(f'\033[1;41mSOMENTE DIGITE A LETRA V PARA VOLTAR! :\033[0;0m')
                print('--' * 35)
                print('             \033[1;30m\033[1;43m     CARREGANDO MENU PRINCIPAL\033[0;0m', end='')
                sleep(0.3)
                print('\033[1;30m\033[1;43m.\033[0;0m', end='')
                sleep(0.3)
                print('\033[1;30m\033[1;43m.\033[0;0m', end='')
                sleep(0.3)
                print('\033[1;30m\033[1;43m.\033[0;0m', end='')
                sleep(0.3)
                print('\033[1;30m\033[1;43m50%\033[0;0m', end='')
                sleep(0.8)
                print('\033[1;30m\033[1;43m.\033[0;0m', end='')
                sleep(0.8)
                print('\033[1;30m\033[1;43m.\033[0;0m', end='')
                sleep(0.8)
                print('\033[1;30m\033[1;43m100%\033[0;0m', end='')
                print('\033[1;30m\033[1;43m   \033[0;0m', end='')
                print('\n')





        elif opcao_menu == '3':
            print('(2b) - FALTA CONSTRUIR - ')

        elif opcao_menu == '4':
            print('(2c) - FALTA CONSTRUIR - ')

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



# --> FIM CADASTRO

