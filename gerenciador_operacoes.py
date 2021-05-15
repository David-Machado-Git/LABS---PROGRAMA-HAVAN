dados = {}
copia_dados = []
codigo_cliente = 0


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
                print(f'Código do Cadastro: {codigo_cliente}')
                dados['Cód'] = [codigo_cliente]
                # print('--' * 35)
                # print(f'TESTE DADOS EM FORMA DE DICIONÁRIOS: {dados.values()}')
                print('--' * 35)
                nome = str(input('Digite o nome do cliente:?'))
                dados['Nome'] = [nome]
                print(f'TESTE DADOS: {dados}')
                print('--' * 30)
                print('-------------------   MOEDAS CADASTRADAS   -------------------')
                print('       | Digite --> (1) para MOEDA REAL - BRASIL   |')
                print('       | Digite --> (2) para MOEDA DÓLAR - EUA     |')
                print('       | Digite --> (3) para MOEDA EURO - EUROPA   |')
                print('       | Digite --> (4) para MOEDA DÓLAR - CANADÁ  |')
                print('        -------------------------------------------')
                moeda_origem = str(input('Moeda de origem: [somente número acima]:?'))

                dados['Moeda origem'] = [moeda_origem]

                print('--' * 30)
                ##### --> DESATIVADO TEMPORARIAMENTE - REATIVAR FUTURAMENTE
                if moeda_origem == '1':
                    print('MOEDA DE ORIGEM: - REAL - BRASIL')
                    dados['Moeda origem'] = ['REAL - BRL']
                    print(f'TESTE MOEDA DE ORIGEM: {dados}')

                elif moeda_origem == '2':
                    print('MOEDA DE ORIGEM: - DÓLAR - EUA')
                    dados['Moeda origem'] = ['DÓLAR - EUA']
                    print(f'TESTE MOEDA DE ORIGEM: {dados}')

                elif moeda_origem == '3':
                    print('MOEDA DE ORIGEM: - EURO - EUROPA')
                    dados['Moeda origem'] = ['EURO']
                    print(f'TESTE MOEDA DE ORIGEM: {dados}')

                elif moeda_origem == '4':
                    print('MOEDA DE ORIGEM: - DÓLAR - CANADÁ')
                    dados['Moeda origem'] = ['DÓLAR - CAD']
                    print(f'TESTE MOEDA DE ORIGEM: {dados}')

                print('--' * 30)
                print('-------------------   MOEDAS CADASTRADAS   -------------------')
                print('       | Digite --> (1) para MOEDA REAL - BRASIL   |')
                print('       | Digite --> (2) para MOEDA DÓLAR - EUA     |')
                print('       | Digite --> (3) para MOEDA EURO - EUROPA   |')
                print('       | Digite --> (4) para MOEDA DÓLAR - CANADÁ  |')
                print('        -------------------------------------------')
                moeda_destino = str(input('Moeda de destino:?'))
                dados['Moeda destino'] = [moeda_destino]
                print('--' * 30)

                ##### --> DESATIVADO TEMPORARIAMENTE - REATIVAR FUTURAMENTE
                if moeda_destino == '1':
                    print('MOEDA DE DESTINO: - REAL - BRASIL')
                    dados['Moeda destino'] = ['REAL - BRASIL']
                    print(f'TESTE MOEDA DE ORIGEM: {dados}')

                elif moeda_destino == '2':
                    print('MOEDA DE DESTINO: - DÓLAR - EUA')
                    dados['Moeda destino'] = ['DÓLAR - EUA']
                    print(f'TESTE MOEDA DE ORIGEM: {dados}')

                elif moeda_destino == '3':
                    print('MOEDA DE DESTINO: - EURO - EUROPA')
                    dados['Moeda destino'] = ['EURO']
                    print(f'TESTE MOEDA DE ORIGEM: {dados}')

                elif moeda_destino == '4':
                    print('MOEDA DE DESTINO: - DÓLAR - CANADÁ')
                    dados['Moeda destino'] = ['DÓLAR CAD']
                    print(f'TESTE MOEDA DE ORIGEM: {dados}')

                print('--' * 30)
                data_operacao = str(input('Data da operação:?'))

                dados['Data Operação'] = [data_operacao]
                print(f'TESTE DATA: {dados}')
                print('--' * 30)
                valor_original = str(input('Valor original:?{Sigla Moeda}:'))
                dados['Valor Original'] = [valor_original]
                print(f'TESTE VALOR ORIGINAL: {dados}')
                print('--' * 30)
                valor_convertido = str(input('Valor convertido:?{Sigla Moeda}:'))

                dados['Valor Convertido'] = [valor_convertido]
                print(f'TESTE VALOR CONVERTIDO: {dados}')
                print('--' * 30)
                taxa_cobrada = str(input('Taxa cobrada:?{Sigla Moeda}:'))
                dados['Taxa Cobrada'] = [taxa_cobrada]
                print(f'TESTE LISTA NORMAL DE DADOS: {dados}')
                print('--' * 30)
                copia_dados.append(dados.copy())
                print(f'TESTE LISTA CÓPA DE DADOS: {copia_dados}')
                print('--' * 30)
                dados.clear()
                print(f'TESTE LISTA NORMAL DE DADOS: {dados}')

                print('--' * 30)
                # --> ESSA SOLUÇÃO SERIA PARA LISTAR TODOS OS CLIENTES E INFORMAÇÕES <--
                print(' --------------------  |SEQUÊNCIA E ORDEM DE COLUNAS|  -------------- VALORES -------------')
                print('1ºCÓD:|2ºNOME:        |3ºMOED ORIG. |4º MOED DEST.  |5º DATA:   |6ºORIGI:|7ºCONV:|8ºTAXA. ')
                print('---' * 30)
                for c, v in enumerate(copia_dados):
                    for d in v.values():
                        print(f"  {str(d).replace('[','').replace(']','').replace('','')}",end=' ')
                    print()








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
                    break


        elif opcao_menu == '2':
            print('--' * 35)
            print(f'\033[7;40m{"   RELATÓRIOS --> OPERAÇÕES REALIZADAS  ":*^70}\033[0;0m')
            print('--' * 35)
            print('(2a) - FALTA CONSTRUIR - ')

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

