from time import sleep

quantia_convertida = []
moeda_origem = '0'
converter_para = 0
moedas_em_numeros = 0
sigla = 'R$:'


while True:

    print('--' * 35)
    print(f'{"   CASA DE CÂMBIO MUITO DINHEIRO - CONVERSOR DE MOEDAS  ":-^70}')
    print('--' * 35)
    print()
    print(f'     \033[7;40m{"CÓDIGOS E MOEDAS CADASTRADAS:":^60}\033[0;0m')
    print('--' * 35)
    print(f'     |--  {"CÓD  ":-<4}{"   MOEDA   ":-^38}            |')
    print(f'     |\033[7;40m{"--   1  ":.<3}|{" - BRL	Real Brasileiro - ":^38}            \033[0;0m|')
    print(f'     |{"--   2  ":.<3}|{" - Dólar dos Estados Unidos - ":^38}            |')
    print(f'     |\033[7;40m{"--   3  ":.<3}|{" - EUR Euro - ":^38}            \033[0;0m|')
    print(f'     |{"--   4  ":.<3}|{" - CAD	Dólar Canadense - ":^38}            |')
    print('--' * 35)
    moeda_origem = str(input('Digite o cód da moeda de origem:?'))

    if moeda_origem.isnumeric():
        if moeda_origem == '1':
            print('--' * 35)
            print('DÊ: MOEDA REAL - BRASIL / PARA: ')
            print('--' * 35)

        elif moeda_origem == '2':
            print('--' * 35)
            print('DÊ: - MOEDA DÓLAR - EUA / PARA: ')
            print('--' * 35)


        elif moeda_origem == '3':
            print('--' * 35)
            print('DÊ: - MOEDA EURO - EUROPA / PARA: ')
            print('--' * 35)


        elif moeda_origem == '4':
            print('--' * 35)
            print('DÊ: - MOEDA DÓLAR - CANADÁ / PARA: ')
            print('--' * 35)

        else:
            while True:
                print(
                    f'\033[1;41mVALOR INVÁLIDO - SOMENTE NÚMEROS DE 1 A 4 QUE CORRESPONDEM AS MOEDAS CADASTRADAS:\033[0;0m')
                moeda_origem = str(input('Digite corretamente o cód da moeda de origem:?'))
                if moeda_origem == '1':
                    print('--' * 35)
                    print('DÊ: MOEDA REAL - BRASIL / PARA: ')
                    print('--' * 35)
                    break

                elif moeda_origem == '2':
                    print('--' * 35)
                    print('DÊ: - MOEDA DÓLAR - EUA / PARA: ')
                    print('--' * 35)
                    break


                elif moeda_origem == '3':
                    print('--' * 35)
                    print('DÊ: - MOEDA EURO - EUROPA / PARA: ')
                    print('--' * 35)
                    break


                elif moeda_origem == '4':
                    print('--' * 35)
                    print('DÊ: - MOEDA DÓLAR - CANADÁ / PARA: ')
                    print('--' * 35)
                    break


    else:
        while True:
            print(
                f'\033[1;41mVALOR INVÁLIDO - SOMENTE NÚMEROS DE 1 A 4 QUE CORRESPONDEM AS MOEDAS CADASTRADAS:\033[0;0m')
            moeda_origem = str(input('Digite corretamente o cód da moeda de origem:?'))
            if moeda_origem == '1':
                print('--' * 35)
                print('DÊ: MOEDA REAL - BRASIL / PARA: ')
                print('--' * 35)
                break

            elif moeda_origem == '2':
                print('--' * 35)
                print('DÊ: - MOEDA DÓLAR - EUA / PARA: ')
                print('--' * 35)
                break


            elif moeda_origem == '3':
                print('--' * 35)
                print('DÊ: - MOEDA EURO - EUROPA / PARA: ')
                print('--' * 35)
                break


            elif moeda_origem == '4':
                print('--' * 35)
                print('DÊ: - MOEDA DÓLAR - CANADÁ / PARA: ')
                print('--' * 35)
                break

    while True:  # SIGLAS
        if moeda_origem == '1':
            sigla = 'R$:'
        elif moeda_origem == '2':
            sigla = 'U$$:'
        elif moeda_origem == '3':
            sigla = '€:'
        elif moeda_origem == '4':
            sigla = 'U$$:'

        valor_para_converter = (input(f'Digite o Valor a ser convertido:? {sigla}'))
        print('--' * 35)

        if valor_para_converter.isnumeric():
            quantia_convertida.append(float(valor_para_converter))
            break

        else:
            quantia_convertida.append(float(valor_para_converter[0:]))
            print(quantia_convertida)
            break

    while True:
        converter_para = str(input('Converter para: [Digite o CÓD DA MOEDA/DESTINO]: ?'))

        if converter_para.isnumeric():
            if converter_para == '1':
                print('--' * 35)
                print('PARA: MOEDA REAL - BRASIL')
                print('--' * 35)
                while converter_para == '1' and moeda_origem == '1':
                    print(
                        f'\033[1;41mESCOLHA OUTRA OPÇÃO: MOEDA DE DESTINO NÃO PODE SER IGUAL MOEDA DE ORIGEM\033[0;0m')
                    converter_para = str(input('Converter para: [Digite o CÓD DA MOEDA/DESTINO]: ?'))
                    print('--' * 35)
                break


            elif converter_para == '2':
                print('--' * 35)
                print('PARA: MOEDA DÓLAR - EUA')
                print('--' * 35)
                while converter_para == '2' and moeda_origem == '2':
                    print(
                        f'\033[1;41mESCOLHA OUTRA OPÇÃO: MOEDA DE DESTINO NÃO PODE SER IGUAL MOEDA DE ORIGEM\033[0;0m')
                    converter_para = str(input('Converter para: [Digite o CÓD DA MOEDA/DESTINO]: ?'))
                    print('--' * 35)
                break

            elif converter_para == '3':
                print('--' * 35)
                print('PARA: MOEDA EURO - EUROPA')
                print('--' * 35)

                while converter_para == '3' and moeda_origem == '3':
                    print(
                        f'\033[1;41mESCOLHA OUTRA OPÇÃO: MOEDA DE DESTINO NÃO PODE SER IGUAL MOEDA DE ORIGEM\033[0;0m')
                    converter_para = str(input('Converter para: [Digite o CÓD DA MOEDA/DESTINO]: ?'))
                    print('--' * 35)
                break

            elif converter_para == '4':
                print('--' * 35)
                print('PARA: MOEDA DÓLAR - CANADÁ')
                print('--' * 35)
                while converter_para == '4' and moeda_origem == '4':
                    print(
                        f'\033[1;41mESCOLHA OUTRA OPÇÃO: MOEDA DE DESTINO NÃO PODE SER IGUAL MOEDA DE ORIGEM\033[0;0m')
                    converter_para = str(input('Converter para: [Digite o CÓD DA MOEDA/DESTINO]: ?'))
                    print('--' * 35)
                break

        else:
            print('--' * 35)
            print(
                f'\033[1;41mVALOR INVÁLIDO - SOMENTE NÚMEROS DE 1 A 4 QUE CORRESPONDEM AS MOEDAS CADASTRADAS:\033[0;0m')
            print('--' * 35)
    print()
    print('        \033[1;40m    Aguarde ! CONVERTENDO MOEDA\033[0;0m', end='')
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

    if moeda_origem == '1' and converter_para == '2':
        # print('1 - caiu no que eu queria - 1 - !!!')
        moeda_origem = float(quantia_convertida[0])
        converter_para = float(0.1574)
        calculo_conversao = float(moeda_origem * converter_para)
        print('--' * 35)
        print(f'Considerando que você escolheu CÓD 1 - BRL	Real Brasileiro como\n'
              f'moeda de origem: e CÓD 2 - Dólar dos Estados Unidos - como moeda de destino.\n'
              f'É importante que você saiba que a cada R$: 1,00 real Brasileiro \n'
              f'corresponde a exatamente U$$: 0.1574 Dólar cotados no dia 12/05/2021.')
        print(f'         \033[1;42m   Sendo assim com R$: {quantia_convertida[0]:.2f} Reais,       \033[0;0m')
        print(f'         \033[1;42m   você tem exatamente U$$: {calculo_conversao:.2f} Dólar.   \033[0;0m')
        print('--' * 35)

    elif moeda_origem == '1' and converter_para == '3':
        moeda_origem = float(quantia_convertida[0])
        converter_para = float(0.1576)
        calculo_conversao = float(moeda_origem * converter_para)
        print('--' * 35)
        print(f'Considerando que você escolheu CÓD 1 - BRL	Real Brasileiro como\n'
              f'moeda de origem: e CÓD 3 - EUR Euro - como moeda de destino.\n'
              f'É importante que você saiba que a cada R$: 1,00 real Brasileiro \n'
              f'corresponde a exatamente €: 0.1576 Euros cotados no dia 12/05/2021')
        print(f'         \033[1;42m   Sendo assim com R$: {quantia_convertida[0]:.2f} Reais,       \033[0;0m')
        print(f'         \033[1;42m   você tem exatamente €: {calculo_conversao:.2f} Euros.     \033[0;0m')
        print('--' * 35)

    elif moeda_origem == '1' and converter_para == '4':
        moeda_origem = float(quantia_convertida[0])
        converter_para = float(0.23)
        calculo_conversao = float(moeda_origem * converter_para)
        print('--' * 35)
        print(f'Considerando que você escolheu CÓD 1 - BRL	Real Brasileiro como\n'
              f'moeda de origem: e CÓD 4 - CAD	Dólar Canadense como moeda de destino.\n'
              f'É importante que você saiba que a cada R$: 1,00 real Brasileiro \n'
              f'corresponde a exatamente U$$: 0.23 Dólar Canadense cotados no dia 12/05/2021')
        print(f'         \033[1;42m   Sendo assim com R$: {quantia_convertida[0]:.2f} Reais,               \033[0;0m')
        print(f'         \033[1;42m   você tem exatamente U$$: {calculo_conversao:.2f} Dólar Canadense.\033[0;0m')
        print('--' * 35)

    if moeda_origem == '2' and converter_para == '1':
        moeda_origem = float(quantia_convertida[0])
        converter_para = float(5.27)
        calculo_conversao = float(moeda_origem * converter_para)
        print('--' * 35)
        print(f'Considerando que você escolheu CÓD 2 - Dólar dos Estados Unidos - como\n'
              f'moeda de origem: e CÓD 1 - BRL	Real Brasileiro como moeda de destino.\n'
              f'É importante que você saiba que a cada U$$: 1,00 Dólar Americano \n'
              f'corresponde a exatamente R$: 5,27 Reais cotados no dia 12/05/2021')
        print(f'         \033[1;42m   Sendo assim com U$$: {quantia_convertida[0]:.2f} Dólar,        \033[0;0m')
        print(f'         \033[1;42m   você tem exatamente R$: {calculo_conversao:.2f} Reais.    \033[0;0m')
        print('--' * 35)

    elif moeda_origem == '2' and converter_para == '3':
        moeda_origem = float(quantia_convertida[0])
        converter_para = float(0.83)
        calculo_conversao = float(moeda_origem * converter_para)
        print('--' * 35)
        print(f'Considerando que você escolheu CÓD 2 - Dólar dos Estados Unidos - como\n'
              f'moeda de origem: e CÓD 3 - EUR Euro como moeda de destino.\n'
              f'É importante que você saiba que a cada U$$: 1,00 Dólar Americano \n'
              f'corresponde a exatamente €: 0,83 Euros cotados no dia 12/05/2021.')
        print(f'         \033[1;42m   Sendo assim com U$$: {quantia_convertida[0]:.2f} Dólar,      \033[0;0m')
        print(f'         \033[1;42m   você tem exatamente R$: {calculo_conversao:.2f} Euros.   \033[0;0m')
        print('--' * 35)

    elif moeda_origem == '2' and converter_para == '4':
        moeda_origem = float(quantia_convertida[0])
        converter_para = float(1.21)
        calculo_conversao = float(moeda_origem * converter_para)
        print('--' * 35)
        print(f'Considerando que você escolheu CÓD 2 - Dólar dos Estados Unidos - como\n'
              f'moeda de origem: e CÓD 4 - CAD	Dólar Canadense como moeda de destino.\n'
              f'É importante que você saiba que a cada U$$: 1,00 Dólar Americano \n'
              f'corresponde a exatamente U$$: 1,21 Dólar Canadense cotados no dia 12/05/2021.')
        print(f'         \033[1;42m   Sendo assim com U$$: {quantia_convertida[0]:.2f} Dólar,                \033[0;0m')
        print(f'         \033[1;42m   você tem exatamente U$$: {calculo_conversao:.2f} Dólar Canadense.  \033[0;0m')
        print('--' * 35)

    if moeda_origem == '3' and converter_para == '1':
        moeda_origem = float(quantia_convertida[0])
        converter_para = float(6.40)
        calculo_conversao = float(moeda_origem * converter_para)
        print('--' * 35)
        print(f'Considerando que você escolheu CÓD 3 - EUR Euro - como\n'
              f'moeda de origem: e CÓD 1 - BRL	Real Brasileiro como moeda de destino.\n'
              f'É importante que você saiba que a cada €: 1,00 Euro \n'
              f'corresponde a exatamente R$: 6,40 Reais Brasileiro cotados no dia 12/05/2021.')
        print(f'         \033[1;42m   Sendo assim com €: {quantia_convertida[0]:.2f} Euros,                 \033[0;0m')
        print(f'         \033[1;42m   você tem exatamente R$: {calculo_conversao:.2f} Reais Brasileiro.\033[0;0m')
        print('--' * 35)

    elif moeda_origem == '3' and converter_para == '2':
        moeda_origem = float(quantia_convertida[0])
        converter_para = float(1.21)
        calculo_conversao = float(moeda_origem * converter_para)
        print('--' * 35)
        print(f'Considerando que você escolheu CÓD 3 - EUR Euro - como\n'
              f'moeda de origem: e CÓD 2 - Dólar dos Estados Unidos como moeda de destino.\n'
              f'É importante que você saiba que a cada €: 1,00 Euro \n'
              f'corresponde a exatamente U$$: 1,21 Dólar EUA cotados no dia 12/05/2021.')
        print(f'         \033[1;42m   Sendo assim com €: {quantia_convertida[0]:.2f} Euros,              \033[0;0m')
        print(f'         \033[1;42m   você tem exatamente U$$: {calculo_conversao:.2f} Dólar EUA.    \033[0;0m')
        print('--' * 35)

    elif moeda_origem == '3' and converter_para == '4':
        moeda_origem = float(quantia_convertida[0])
        converter_para = float(1.46)
        calculo_conversao = float(moeda_origem * converter_para)
        print('--' * 35)
        print(f'Considerando que você escolheu CÓD 3 - EUR Euro - como\n'
              f'moeda de origem: e CÓD 4 - CAD	- Dólar Canadense como moeda de destino.\n'
              f'É importante que você saiba que a cada €: 1,00 Euro \n'
              f'corresponde a exatamente U$$: 1,46 Dólar Canadense cotados no dia 12/05/2021.')
        print(f'         \033[1;42m   Sendo assim com €: {quantia_convertida[0]:.2f} Euros,                  \033[0;0m')
        print(f'         \033[1;42m   você tem exatamente U$$: {calculo_conversao:.2f} Dólar Canadense.  \033[0;0m')
        print('--' * 35)

    if moeda_origem == '4' and converter_para == '1':
        moeda_origem = float(quantia_convertida[0])
        converter_para = float(4.38)
        calculo_conversao = float(moeda_origem * converter_para)
        print('--' * 35)
        print(f'Considerando que você escolheu CÓD 4 - CAD - Dólar Canadense - como\n'
              f'moeda de origem: e CÓD 1 - BRL	Real Brasileiro como moeda de destino.\n'
              f'É importante que você saiba que a cada U$$: 1,00 Dólar Canadense \n'
              f'corresponde a exatamente R$: 4,38 Reais Brasileiro cotados no dia 12/05/2021.')
        print(
            f'         \033[1;42m   Sendo assim com U$$: {quantia_convertida[0]:.2f} Dólar Canadense,        \033[0;0m')
        print(f'         \033[1;42m   você tem exatamente R$: {calculo_conversao:.2f} Reais Brasileiro.   \033[0;0m')
        print('--' * 35)

    if moeda_origem == '4' and converter_para == '2':
        moeda_origem = float(quantia_convertida[0])
        converter_para = float(0.82)
        calculo_conversao = float(moeda_origem * converter_para)
        print('--' * 35)
        print(f'Considerando que você escolheu CÓD 4 - CAD - Dólar Canadense - como\n'
              f'moeda de origem: e CÓD 2 - Dólar dos Estados Unidos  como moeda de destino.\n'
              f'É importante que você saiba que a cada U$$: 1,00 Dólar Canadense \n'
              f'corresponde a exatamente U$$: 0,82 Dólar EUA cotados no dia 12/05/2021.')
        print(f'         \033[1;42m   Sendo assim com U$$: {quantia_convertida[0]:.2f} Dólar Canadense, \033[0;0m')
        print(f'         \033[1;42m   você tem exatamente U$$: {calculo_conversao:.2f} - Dólar EUA. \033[0;0m')
        print('--' * 35)

    if moeda_origem == '4' and converter_para == '3':
        moeda_origem = float(quantia_convertida[0])
        converter_para = float(0.68)
        calculo_conversao = float(moeda_origem * converter_para)
        print('--' * 35)
        print(f'Considerando que você escolheu CÓD 4 - CAD - Dólar Canadense - como\n'
              f'moeda de origem: e CÓD 3 - EUR - Euro  como moeda de destino.\n'
              f'É importante que você saiba que a cada U$$: 1,00 Dólar Canadense \n'
              f'corresponde a exatamente €: 0,68 Euros cotados no dia 12/05/2021.')
        print(f'         \033[1;42m   Sendo assim com U$$: {quantia_convertida[0]:.2f} Dólar Canadense, \033[0;0m')
        print(f'         \033[1;42m   você tem exatamente €: {calculo_conversao:.2f} - Euros.       \033[0;0m')
        print('--' * 35)

    # print('\n                  --- | FIM DO PROGRAMA | ---')



