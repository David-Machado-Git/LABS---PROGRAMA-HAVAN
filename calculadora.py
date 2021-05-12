from time import sleep

moedas = []
quantia_convertida = []
moeda_origem = '0'
converter_para = 0
moedas_em_numeros = 0


print('--'*31)
print(f'{"  CASA DE CÂMBIO MUITO DINHEIRO - CONVERSOR DE MOEDAS  ":-^60}')
print('--'*31)
print()
print(f'\033[7;40m{"CÓDIGOS E MOEDAS CADASTRADAS:":^60}\033[0;0m')
print('--'*31)
print(f'|--  {"CÓD  ":-<4}{"   MOEDA   ":-^39}{"  COTAÇÃO   ":-^11}|')
print(f'|\033[7;40m{"--   1  ":.<3}|{" - BRL	Real Brasileiro - ":^38}|           \033[0;0m|')
print(f'|{"--   2  ":.<3}|{" - Dólar dos Estados Unidos - ":^39}|{"U$$ 5,22   ":-^11}|')
print(f'|\033[7;40m{"--   3  ":.<3}|{" - EUR Euro - ":^39}|{"U$$ 5,22   ":-^11}\033[0;0m|')
print(f'|{"--   4  ":.<3}|{" - PYG Guarani Paraguaio - ":^39}|{"U$$ 5,22   ":-^11}|')
print(f'|\033[7;40m{"--   5  ":.<3}|{" - CAD	Dólar Canadense - ":^39}|{"U$$ 5,22   ":-^11}\033[0;0m|')
print('--'*31)
moeda_origem = str(input('Digite o cód da moeda de origem:?'))

if moeda_origem.isnumeric():
    # print('Caiu em números')
    if moeda_origem == '1':
        print('--' * 31)
        print('Moeda de origem CÓD 1 - BRL	Real Brasileiro - ')
        print('--' * 31)

    elif moeda_origem == '2':
        print('--' * 31)
        print('Moeda de origem CÓD 2 - Dólar dos Estados Unidos - ')
        print('--' * 31)


    elif moeda_origem == '3':
        print('--' * 31)
        print('Moeda de origem CÓD 3 - EUR Euro - ')
        print('--' * 31)


    elif moeda_origem == '4':
        print('--' * 31)
        print('Moeda de origem CÓD 4 - PYG Guarani Paraguaio - ')
        print('--' * 31)


    elif moeda_origem == '5':
        print('--' * 31)
        print('Moeda de origem CÓD 5 - CAD	Dólar Canadense - ')
        print('--' * 31)

    else:
        print(f'\033[1;41mVALOR INVÁLIDO - SOMENTE NÚMEROS DE 1 A 5 QUE CORRESPONDEM AS MOEDAS CADASTRADAS:\033[0;0m')

else:
    while True:
        # print('Caiu em String')
        print(f'\033[1;41mVALOR INVÁLIDO - SOMENTE NÚMEROS DE 1 A 5 QUE CORRESPONDEM AS MOEDAS CADASTRADAS:\033[0;0m')
        moeda_origem = str(input('Digite corretamente o cód da moeda de origem:?'))
        if moeda_origem == '1':
            print('--' * 31)
            print('Moeda de origem CÓD 1 - BRL	Real Brasileiro - ')
            print('--' * 31)
            break

        elif moeda_origem == '2':
            print('--' * 31)
            print('Moeda de origem CÓD 2 - Dólar dos Estados Unidos - ')
            print('--' * 31)
            break


        elif moeda_origem == '3':
            print('--' * 31)
            print('Moeda de origem CÓD 3 - EUR Euro - ')
            print('--' * 31)
            break


        elif moeda_origem == '4':
            print('--' * 31)
            print('Moeda de origem CÓD 4 - PYG Guarani Paraguaio - ')
            print('--' * 31)
            break


        elif moeda_origem == '5':
            print('--' * 31)
            print('Moeda de origem CÓD 5 - CAD	Dólar Canadense - ')
            print('--' * 31)
            break

while True:
    valor_para_converter = str(input('Digite o Valor a ser convertido:?'))
    print('--' * 31)

    if valor_para_converter.isnumeric():
        # print('Valor para converter caiu em números')
        quantia_convertida.append(float(valor_para_converter))
        # print('--' * 31)
        # print(f'{quantia_convertida[0]:.2f}')
        break


    else:
        print(f'\033[1;41mVALOR INVÁLIDO - SOMENTE NÚMEROS !\033[0;0m')


while True:
    converter_para = str(input('Converter para: [Digite o CÓD DA MOEDA] ?'))
    print('--' * 31)

    if converter_para.isnumeric():
        # print('Converter para caiu em números')
        if converter_para == '1':
            print('--' * 31)
            print('Moeda de conversão CÓD 1 - BRL	Real Brasileiro - ')
            print('--' * 31)
            break

        elif converter_para == '2':
            print('--' * 31)
            print('Moeda de conversão CÓD 2 - Dólar dos Estados Unidos - ')
            print('--' * 31)
            break

        elif converter_para == '3':
            print('--' * 31)
            print('Moeda de conversão CÓD 3 - EUR Euro - ')
            print('--' * 31)
            break

        elif converter_para == '4':
            print('--' * 31)
            print('Moeda de conversão CÓD 4 - PYG Guarani Paraguaio - ')
            print('--' * 31)
            break

        elif converter_para == '5':
            print('--' * 31)
            print('Moeda de conversão CÓD 5 - CAD	Dólar Canadense - ')
            print('--' * 31)
            break

    else:
        print('--' * 31)
        print('Converter para caiu em String')
        print(f'\033[1;41mVALOR INVÁLIDO - SOMENTE NÚMEROS DE 1 A 5 QUE CORRESPONDEM AS MOEDAS CADASTRADAS:\033[0;0m')
        print('--' * 31)
print()
print('\033[1;40m    Aguarde ! Processando\033[0;0m',end='')
sleep(0.3)
print('\033[1;40m.\033[0;0m',end='')
sleep(0.3)
print('\033[1;40m.\033[0;0m',end='')
sleep(0.3)
print('\033[1;40m.\033[0;0m',end='')
sleep(0.3)
print('\033[1;40mCONVERTENDO !.\033[0;0m',end='')
sleep(0.8)
print('\033[1;40m.\033[0;0m',end='')
sleep(0.8)
print('\033[1;40m.\033[0;0m',end='')
sleep(0.8)
print('\033[1;40m100%\033[0;0m',end='')
print('\033[1;40m   \033[0;0m',end='')
print()
print('\n      RESULTADO DO PROGRAMA')
print('\n   --- | FIM DO PROGRAMA | ---')







