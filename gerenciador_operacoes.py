from time import sleep

dados = {} ### --> DICIONÁRIO RECEBE TODOS OS DADOS COM SEUS RESPECTIVOS VALORES; ID, NOME ETC...
lista_de_dados = []
lista_principal = []
copia_dados = []### --> DICIONÁRIO RECEBE TODOS OS DADOS
codigo_cliente = 0 ### --> CONTADOR CONTAGEM TRANSAÇÕES
moeda_origem_sigla = 'R$:'
moeda_destino_sigla = 'U$$:'
valor_tot_operacoes = float(0)
valor_tot_operacoes_a = float(0)
tot_taxas = float(0)
tot_movimento_brasil_dolar_eua = float(0)
tot_movimento_brasil_euro = float(0)
tot_movimento_brasil_dolar_canada = float(0)
tot_movimento_dolar_eua_brasil = float(0)
tot_movimento_dolar_eua_euro = float(0)
tot_movimento_dolar_eua_dolar_canada = float(0)
tot_movimento_euro_brasil = float(0)
tot_movimento_euro_dolar_eua = float(0)
tot_movimento_euro_dolar_canada = float(0)
tot_movimento_dolar_canada_brasil = float(0)
tot_movimento_dolar_canada_dolar_eua = float(0)
tot_movimento_dolar_canada_euro = float(0)


print('--' * 35)
print(f'\033[7;40m{"   GERENCIADOR DE OPERAÇÕES  ":*^70}\033[0;0m')
print('--' * 35)

while True:
    print(f'     |-- {"OPÇÃO  ":-<2}{"   MENU   ":-^38}            |')
    print(f'     |\033[1;90m----------------------------------------------------------  \033[0;0m|')
    print(f'     |\033[7;40m{" -> 1 <-":.<3}|{" - CADASTROS - CLIENTES - OPERAÇÕES ":^38}             \033[0;0m|')
    print(f'     |\033[1;90m----------------------------------------------------------  \033[0;0m|')
    print(f'     |{" -> 2 <-":.<3}|{"  - LISTAR OPERAÇÕES - ":^38}             |')
    print(f'     |\033[1;90m----------------------------------------------------------  \033[0;0m|')
    print(f'     |\033[7;40m{" -> 3 <-":.<3}|{"  - VALOR TOTAL DAS OPERAÇÕES - ":^38}             \033[0;0m|')
    print(f'     |\033[1;90m----------------------------------------------------------  \033[0;0m|')
    print(f'     |{" -> 4 <-":.<3}|{" - VALOR TOTAL DAS TAXAS COBRADAS - ":^38}             |')
    print(f'     |\033[1;90m----------------------------------------------------------  \033[0;0m|')
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
                codigo_cliente_convertida = str(codigo_cliente)
                print(f' --> {codigo_cliente}º CLIENTE - ORDEM DE SERVIÇO DE Nº [ {codigo_cliente_convertida} ]')
                dados['Cód'] = [codigo_cliente]
                lista_de_dados.append(codigo_cliente_convertida)
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
                if moeda_origem == '1':
                    print('MOEDA DE ORIGEM: - REAL - BRASIL')
                    dados['Moeda origem'] = ['REAL - BRL']
                    moeda_origem_sigla = 'R$:'
                    lista_de_dados.append('REAL - BRL')

                elif moeda_origem == '2':
                    print('MOEDA DE ORIGEM: - DÓLAR - EUA')
                    dados['Moeda origem'] = ['DÓLAR - EUA']
                    moeda_origem_sigla = 'U$$:'
                    lista_de_dados.append('DÓLAR - EUA')

                elif moeda_origem == '3':
                    print('MOEDA DE ORIGEM: - EURO - EUROPA')
                    dados['Moeda origem'] = ['EURO']
                    moeda_origem_sigla = '€:'
                    lista_de_dados.append('EURO')

                elif moeda_origem == '4':
                    print('MOEDA DE ORIGEM: - DÓLAR - CANADÁ')
                    dados['Moeda origem'] = ['DÓLAR - CAD']
                    moeda_origem_sigla = 'U$$:'
                    lista_de_dados.append('DÓLAR - CAD')

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
                        if moeda_origem == '1':
                            print('MOEDA DE ORIGEM: - REAL - BRASIL')
                            dados['Moeda origem'] = ['REAL - BRL']
                            moeda_origem_sigla = 'R$:'
                            lista_de_dados.append('REAL - BRL')
                            break

                        elif moeda_origem == '2':
                            print('MOEDA DE ORIGEM: - DÓLAR - EUA')
                            dados['Moeda origem'] = ['DÓLAR - EUA']
                            moeda_origem_sigla = 'U$$:'
                            lista_de_dados.append('DÓLAR - EUA')
                            break

                        elif moeda_origem == '3':
                            print('MOEDA DE ORIGEM: - EURO - EUROPA')
                            dados['Moeda origem'] = ['EURO']
                            moeda_origem_sigla = '€:'
                            lista_de_dados.append('EURO')
                            break

                        elif moeda_origem == '4':
                            print('MOEDA DE ORIGEM: - DÓLAR - CANADÁ')
                            dados['Moeda origem'] = ['DÓLAR - CAD']
                            moeda_origem_sigla = 'U$$:'
                            lista_de_dados.append('DÓLAR - CAD')
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

                if moeda_destino == '1':
                    print('MOEDA DE DESTINO: - REAL - BRASIL')
                    dados['Moeda destino'] = ['REAL - BRASIL']
                    moeda_destino_sigla = 'R$:'
                    lista_de_dados.append('REAL - BRASIL')

                elif moeda_destino == '2':
                    print('MOEDA DE DESTINO: - DÓLAR - EUA')
                    dados['Moeda destino'] = ['DÓLAR - EUA']
                    moeda_destino_sigla = 'U$$:'
                    lista_de_dados.append('DÓLAR - EUA')

                elif moeda_destino == '3':
                    print('MOEDA DE DESTINO: - EURO - EUROPA')
                    dados['Moeda destino'] = ['EURO']
                    moeda_destino_sigla = '€:'
                    lista_de_dados.append('EURO')

                elif moeda_destino == '4':
                    print('MOEDA DE DESTINO: - DÓLAR - CANADÁ')
                    dados['Moeda destino'] = ['DÓLAR CAD']
                    moeda_destino_sigla = 'U$$:'
                    lista_de_dados.append('DÓLAR CAD')

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

                        if moeda_destino == '1':
                            print('MOEDA DE DESTINO: - REAL - BRASIL')
                            dados['Moeda destino'] = ['REAL - BRASIL']
                            moeda_destino_sigla = 'R$:'
                            lista_de_dados.append('REAL - BRASIL')
                            break

                        elif moeda_destino == '2':
                            print('MOEDA DE DESTINO: - DÓLAR - EUA')
                            dados['Moeda destino'] = ['DÓLAR - EUA']
                            moeda_destino_sigla = 'U$$:'
                            lista_de_dados.append('DÓLAR - EUA')
                            break

                        elif moeda_destino == '3':
                            print('MOEDA DE DESTINO: - EURO - EUROPA')
                            dados['Moeda destino'] = ['EURO']
                            moeda_destino_sigla = '€:'
                            lista_de_dados.append('EURO')
                            break

                        elif moeda_destino == '4':
                            print('MOEDA DE DESTINO: - DÓLAR - CANADÁ')
                            dados['Moeda destino'] = ['DÓLAR CAD']
                            moeda_destino_sigla = 'U$$:'
                            lista_de_dados.append('DÓLAR CAD')
                            break

                print('--' * 30)
                data_operacao = str(input('Data da operação:\033[1;90m[NO FORMATO: __/__/____ ]\033[0;0m:?'))
                dados['Data Operação'] = [data_operacao]
                lista_de_dados.append(data_operacao)
                print('--' * 30)
                valor_original = str(input(f'Valor original:? {moeda_origem_sigla}'))
                dados['Valor Original'] = [valor_original]
                lista_de_dados.append(valor_original)
                convertendo_valor = float(valor_original)
                valor_tot_operacoes += convertendo_valor
                if moeda_origem == '1' and moeda_destino == '2':
                    convertendo_valor_brasil = float(valor_original)
                    tot_movimento_brasil_dolar_eua += convertendo_valor_brasil

                elif moeda_origem == '1' and moeda_destino == '3':
                    convertendo_valor_brasil_euro = float(valor_original)
                    tot_movimento_brasil_euro += convertendo_valor_brasil_euro

                elif moeda_origem == '1' and moeda_destino == '4':
                    convertendo_valor_brasil_dolar_canada = float(valor_original)
                    tot_movimento_brasil_dolar_canada += convertendo_valor_brasil_dolar_canada

                if moeda_origem == '2' and moeda_destino == '1':
                    convertendo_valor_eua_brasil = float(valor_original)
                    tot_movimento_dolar_eua_brasil += convertendo_valor_eua_brasil

                elif moeda_origem == '2' and moeda_destino == '3':
                    convertendo_valor_eua_euro = float(valor_original)
                    tot_movimento_dolar_eua_euro += convertendo_valor_eua_euro

                elif moeda_origem == '2' and moeda_destino == '4':
                    convertendo_valor_eua_canada = float(valor_original)
                    tot_movimento_dolar_eua_dolar_canada += convertendo_valor_eua_canada

                if moeda_origem == '3' and moeda_destino == '1':
                    convertendo_valor_euro_brasil = float(valor_original)
                    tot_movimento_euro_brasil += convertendo_valor_euro_brasil

                elif moeda_origem == '3' and moeda_destino == '2':
                    convertendo_valor_euro_eua = float(valor_original)
                    tot_movimento_euro_dolar_eua += convertendo_valor_euro_eua

                elif moeda_origem == '3' and moeda_destino == '4':
                    convertendo_valor_euro_canada = float(valor_original)
                    tot_movimento_euro_dolar_canada += convertendo_valor_euro_canada

                if moeda_origem == '4' and moeda_destino == '1':
                    convertendo_valor_canada_brasil = float(valor_original)
                    tot_movimento_dolar_canada_brasil += convertendo_valor_canada_brasil

                elif moeda_origem == '4' and moeda_destino == '2':
                    convertendo_valor_canada_eua = float(valor_original)
                    tot_movimento_dolar_canada_dolar_eua += convertendo_valor_canada_eua

                elif moeda_origem == '4' and moeda_destino == '3':
                    convertendo_valor_canada_euro = float(valor_original)
                    tot_movimento_dolar_canada_euro += convertendo_valor_canada_euro

                print('--' * 30)
                valor_convertido = str(input(f'Valor convertido:? {moeda_destino_sigla}'))

                dados['Valor Convertido'] = [valor_convertido]
                lista_de_dados.append(valor_convertido)

                print('--' * 30)
                taxa_cobrada = str(input(f'Taxa cobrada:? R$:'))
                conversao_taxa = float(taxa_cobrada)
                tot_taxas += conversao_taxa

                dados['Taxa Cobrada'] = [taxa_cobrada]
                lista_de_dados.append(taxa_cobrada)

                print('--' * 30)
                copia_dados.append(dados.copy())
                lista_principal.append(lista_de_dados)



                print('--' * 30)
                print('\033[1;90m----------------------- FIM CADASTRO -----------------------\033[0;0m')
                print('--' * 30)

                while True:
                    continua_cadastro = str(input('\nCadastrar mais clientes:? [C - P/ CONTINUAR OU S - P/ SAIR]:?')).strip().upper()[0]
                    print('')

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
                print('\033[1;90m------------------------------------------------------------\033[0;0m')
                print('\033[1;41mATÉ O PRESENTE MOMENTO NÃO HÁ NENHUMA OPERAÇÃO REALIZADA !\033[0;0m')
                print('\033[1;90m------------------------------------------------------------\033[0;0m')
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
                print(f'\033[7;40m{"   RELATÓRIOS --> OPERAÇÕES REALIZADAS:  ":*^70}\033[0;0m')
                print('--' * 35)
                print()
                print(f'\033[1;42mATÉ O PRESENTE MOMENTO VOCÊ TEM UM TOTAL DE: {codigo_cliente} \033[0;0m',end='')
                if codigo_cliente == 1:
                    print('\033[1;42mOPERAÇÃO !\033[0;0m')
                else:
                    print('\033[1;42mOPERAÇÕES !\033[0;0m')
                print('--' * 35)
                print(' -- | ABAIXO SEGUE A LISTA COMPLETA DE TODOS OS REGISTROS ATÉ O MOMENTO! | -- ')
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


                print('--' * 35)
                print('--' * 35)
                while True:
                    voltar_menu_principal = str(input('Digite:[S]-SAIR:')).strip().upper()[0]
                    if voltar_menu_principal == 'S':
                        break

                    else:
                        print(f'\033[1;41mSOMENTE DIGITE A LETRA [S]-PARA SAIR! :\033[0;0m')
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


            if codigo_cliente == 0:
                print('--' * 35)
                print('        \033[1;40m    Aguarde ! AVERIGUANDO OPERAÇÕES\033[0;0m', end='')
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
                print('\033[1;90m------------------------------------------------------------\033[0;0m')
                print('\033[1;41mATÉ O PRESENTE MOMENTO NÃO HÁ NENHUMA OPERAÇÃO REALIZADA !\033[0;0m')
                print('\033[1;90m------------------------------------------------------------\033[0;0m')
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
                print('        \033[1;40m    Aguarde ! AVERIGUANDO OPERAÇÕES\033[0;0m', end='')
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
                print(f'\033[7;40m{"   RELATÓRIOS --> VALOR TOTAL DAS OPERAÇÕES:  ":*^70}\033[0;0m')
                print('--' * 35)
                print()
                print(f'\033[1;42mATÉ O PRESENTE MOMENTO VOCÊ TEM UM TOTAL DE: {codigo_cliente} \033[0;0m', end='')
                if codigo_cliente == 1:
                    print('\033[1;42mOPERAÇÃO !\033[0;0m')
                else:
                    print('\033[1;42mOPERAÇÕES !\033[0;0m')

                if tot_movimento_brasil_dolar_eua > 0:
                    print(f'DE: BRL - BRASIL / PARA: DÓLAR - EUA / MOVIMENTAÇÃO TOTAL DÊ R$: {tot_movimento_brasil_dolar_eua:.2f} REAIS.')

                if tot_movimento_brasil_euro > 0:
                    print(f'DE: BRL - BRASIL / PARA: EURO - EUROPA / MOVIMENTAÇÃO TOTAL DÊ R$: {valor_tot_operacoes:.2f} REAIS.')

                if tot_movimento_brasil_dolar_canada > 0:
                    print(f'DE: BRL - BRASIL / PARA: DÓLAR - CANADÁ / MOVIMENTAÇÃO TOTAL DÊ R$: {tot_movimento_brasil_dolar_canada:.2f} REAIS.')

                if tot_movimento_dolar_eua_brasil > 0:
                    print(f'DE: DÓLAR - EUA / PARA: BRL - BRASIL / MOVIMENTAÇÃO TOTAL DÊ U$$: {tot_movimento_dolar_eua_brasil:.2f} DÓLAR')

                if tot_movimento_dolar_eua_euro > 0:
                    print(f'DE: DÓLAR - EUA / PARA: EURO - EUROPA / MOVIMENTAÇÃO TOTAL DÊ U$$: {tot_movimento_dolar_eua_euro:.2f} DÓLAR')

                if tot_movimento_dolar_eua_dolar_canada > 0:
                    print(f'DE: DÓLAR - EUA / PARA: DÓLAR - CANADÁ / MOVIMENTAÇÃO TOTAL DÊ U$$: {tot_movimento_dolar_eua_dolar_canada:.2f} DÓLAR')

                if tot_movimento_euro_brasil > 0:
                    print(f'DE: EURO - EUROPA / PARA: BRL - BRASIL / MOVIMENTAÇÃO TOTAL DÊ €: {tot_movimento_euro_brasil:.2f} EURO.')

                if tot_movimento_euro_dolar_eua > 0:
                    print(f'DE: EURO - EUROPA / PARA: DÓLAR - EUA / MOVIMENTAÇÃO TOTAL DÊ €: {tot_movimento_euro_dolar_eua:.2f} EURO.')

                if tot_movimento_euro_dolar_canada > 0:
                    print(f'DE: EURO - EUROPA / PARA: DÓLAR - CANADÁ / MOVIMENTAÇÃO TOTAL DÊ €: {tot_movimento_euro_dolar_canada:.2f} EURO.')

                if tot_movimento_dolar_canada_brasil > 0:
                    print(f'DE: DÓLAR - CANADÁ / PARA: BRL - BRASIL / MOVIMENTAÇÃO TOTAL DÊ U$$: {tot_movimento_dolar_canada_brasil:.2f} DÓLAR')

                if tot_movimento_dolar_canada_dolar_eua > 0:
                    print(f'DE: DÓLAR - CANADÁ / PARA: DÓLAR - EUA / MOVIMENTAÇÃO TOTAL DÊ U$$: {tot_movimento_dolar_canada_dolar_eua:.2f} DÓLAR')

                if tot_movimento_dolar_canada_euro > 0:
                    print(f'DE: DÓLAR - CANADÁ / PARA: EURO - EUROPA / MOVIMENTAÇÃO TOTAL DÊ U$$: {tot_movimento_dolar_canada_euro:.2f} DÓLAR')

                print()
                print()
                print()
                print('--' * 35)
                print('--' * 35)
                while True:
                    voltar_menu_principal = str(input('Digite:[S]-SAIR:')).strip().upper()[0]
                    if voltar_menu_principal == 'S':
                        break

                    else:
                        print(f'\033[1;41mSOMENTE DIGITE A LETRA [S]-PARA SAIR! :\033[0;0m')

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

        elif opcao_menu == '4':

            if codigo_cliente == 0:
                print('--' * 35)
                print('        \033[1;40m    Aguarde ! AVERIGUANDO SISTEMA\033[0;0m', end='')
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
                print('\033[1;90m------------------------------------------------------------\033[0;0m')
                print('\033[1;41mATÉ O PRESENTE MOMENTO NÃO HÁ NENHUMA OPERAÇÃO REALIZADA !\033[0;0m')
                print('\033[1;90m------------------------------------------------------------\033[0;0m')
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
                print('        \033[1;40m    Aguarde ! AVERIGUANDO SISTEMA\033[0;0m', end='')
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
                print(f'\033[7;40m{"   RELATÓRIOS --> VALOR TOTAL DE TAXAS:  ":*^70}\033[0;0m')
                print('--' * 35)
                print()
                print(f'\033[1;42mATÉ O PRESENTE MOMENTO VOCÊ TEM: {codigo_cliente} \033[0;0m', end='')
                if codigo_cliente == 1:
                    print('\033[1;42mOPERAÇÃO REGISTRADA!\033[0;0m')
                else:
                    print('\033[1;42mOPERAÇÕES REGISTRADAS!\033[0;0m')

                print('\033[1;90m------------------------------------------------------------\033[0;0m')
                print(f'SOMANDO TODAS AS ENTRADAS EM TAXAS: TEMOS UM TOTAL DÊ R$: {tot_taxas:.2f} REAIS.')
                print(f'AS MESMAS SÃO REFERENTE AS DEVIDAS CONVERSÕES ABAIXO:')
                print('\033[1;90m------------------------------------------------------------\033[0;0m')

                if tot_movimento_brasil_dolar_eua > 0:
                    print(f'DE: BRL - BRASIL / PARA: DÓLAR - EUA / MOVIMENTAÇÃO TOTAL DÊ R$: {tot_movimento_brasil_dolar_eua:.2f} REAIS.')

                if tot_movimento_brasil_euro > 0:
                    print(f'DE: BRL - BRASIL / PARA: EURO - EUROPA / MOVIMENTAÇÃO TOTAL DÊ R$: {valor_tot_operacoes:.2f} REAIS.')

                if tot_movimento_brasil_dolar_canada > 0:
                    print(f'DE: BRL - BRASIL / PARA: DÓLAR - CANADÁ / MOVIMENTAÇÃO TOTAL DÊ R$: {tot_movimento_brasil_dolar_canada:.2f} REAIS.')

                if tot_movimento_dolar_eua_brasil > 0:
                    print(f'DE: DÓLAR - EUA / PARA: BRL - BRASIL / MOVIMENTAÇÃO TOTAL DÊ U$$: {tot_movimento_dolar_eua_brasil:.2f} DÓLAR')

                if tot_movimento_dolar_eua_euro > 0:
                    print(f'DE: DÓLAR - EUA / PARA: EURO - EUROPA / MOVIMENTAÇÃO TOTAL DÊ U$$: {tot_movimento_dolar_eua_euro:.2f} DÓLAR')

                if tot_movimento_dolar_eua_dolar_canada > 0:
                    print(f'DE: DÓLAR - EUA / PARA: DÓLAR - CANADÁ / MOVIMENTAÇÃO TOTAL DÊ U$$: {tot_movimento_dolar_eua_dolar_canada:.2f} DÓLAR')

                if tot_movimento_euro_brasil > 0:
                    print(f'DE: EURO - EUROPA / PARA: BRL - BRASIL / MOVIMENTAÇÃO TOTAL DÊ €: {tot_movimento_euro_brasil:.2f} EURO.')

                if tot_movimento_euro_dolar_eua > 0:
                    print(f'DE: EURO - EUROPA / PARA: DÓLAR - EUA / MOVIMENTAÇÃO TOTAL DÊ €: {tot_movimento_euro_dolar_eua:.2f} EURO.')

                if tot_movimento_euro_dolar_canada > 0:
                    print(f'DE: EURO - EUROPA / PARA: DÓLAR - CANADÁ / MOVIMENTAÇÃO TOTAL DÊ €: {tot_movimento_euro_dolar_canada:.2f} EURO.')

                if tot_movimento_dolar_canada_brasil > 0:
                    print(f'DE: DÓLAR - CANADÁ / PARA: BRL - BRASIL / MOVIMENTAÇÃO TOTAL DÊ U$$: {tot_movimento_dolar_canada_brasil:.2f} DÓLAR')

                if tot_movimento_dolar_canada_dolar_eua > 0:
                    print(f'DE: DÓLAR - CANADÁ / PARA: DÓLAR - EUA / MOVIMENTAÇÃO TOTAL DÊ U$$: {tot_movimento_dolar_canada_dolar_eua:.2f} DÓLAR')

                if tot_movimento_dolar_canada_euro > 0:
                    print(f'DE: DÓLAR - CANADÁ / PARA: EURO - EUROPA / MOVIMENTAÇÃO TOTAL DÊ U$$: {tot_movimento_dolar_canada_euro:.2f} DÓLAR')

                print()
                print()
                print()
                print('--' * 35)
                print('--' * 35)
                while True:
                    voltar_menu_principal = str(input('Digite:[S]-SAIR:')).strip().upper()[0]
                    if voltar_menu_principal == 'S':
                        break

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


