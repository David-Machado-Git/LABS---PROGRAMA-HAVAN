from time import sleep
from math import floor

quantia_convertida = []
moeda_origem = '0'
converter_para = 0
moedas_em_numeros = 0
sigla = 'R$:'

print('--' * 35)
print(f'{"   CASA DE CÂMBIO MUITO DINHEIRO - CONVERSOR DE MOEDAS  ":-^70}')
print('--' * 35)
print()
print(f'     \033[7;40m{"CÓDIGOS E MOEDAS CADASTRADAS:":^60}\033[0;0m')
print('--' * 35)
print(f'     |--  {"CÓD  ":-<4}{"   MOEDA   ":-^38}{"  COTAÇÃO   ":-^11}|')
print(f'     |\033[7;40m{"--   1  ":.<3}|{" - BRL	Real Brasileiro - ":^38}|           \033[0;0m|')
print(f'     |{"--   2  ":.<3}|{" - Dólar dos Estados Unidos - ":^38}|{"U$$ 5,24   ":-^11}|')
print(f'     |\033[7;40m{"--   3  ":.<3}|{" - EUR Euro - ":^38}|{"  € 6,34   ":-^11}\033[0;0m|')
print(f'     |{"--   4  ":.<3}|{" - PYG Guarani Paraguaio - ":^38}|{"  ₲ 0,79   ":-^11}|')
print(f'     |\033[7;40m{"--   5  ":.<3}|{" - CAD	Dólar Canadense - ":^38}|{"U$$ 4,33   ":-^11}\033[0;0m|')
print('--' * 35)
moeda_origem = str(input('Digite o cód da moeda de origem:?'))


if moeda_origem.isnumeric():
    # print('Caiu em números')
    if moeda_origem == '1':
        print('--' * 35)
        print('Moeda de origem CÓD 1 - BRL	Real Brasileiro - ')
        print('--' * 35)

    elif moeda_origem == '2':
        print('--' * 35)
        print('Moeda de origem CÓD 2 - Dólar dos Estados Unidos - ')
        print('--' * 35)


    elif moeda_origem == '3':
        print('--' * 35)
        print('Moeda de origem CÓD 3 - EUR Euro - ')
        print('--' * 35)


    elif moeda_origem == '4':
        print('--' * 35)
        print('Moeda de origem CÓD 4 - PYG Guarani Paraguaio - ')
        print('--' * 35)


    elif moeda_origem == '5':
        print('--' * 35)
        print('Moeda de origem CÓD 5 - CAD	Dólar Canadense - ')
        print('--' * 35)

    else:
        print(f'\033[1;41mVALOR INVÁLIDO - SOMENTE NÚMEROS DE 1 A 5 QUE CORRESPONDEM AS MOEDAS CADASTRADAS:\033[0;0m')

else:
    while True:
        # print('Caiu em String')
        print(f'\033[1;41mVALOR INVÁLIDO - SOMENTE NÚMEROS DE 1 A 5 QUE CORRESPONDEM AS MOEDAS CADASTRADAS:\033[0;0m')
        moeda_origem = str(input('Digite corretamente o cód da moeda de origem:?'))
        if moeda_origem == '1':
            print('--' * 35)
            print('Moeda de origem CÓD 1 - BRL	Real Brasileiro - ')
            print('--' * 35)
            break

        elif moeda_origem == '2':
            print('--' * 35)
            print('Moeda de origem CÓD 2 - Dólar dos Estados Unidos - ')
            print('--' * 35)
            break


        elif moeda_origem == '3':
            print('--' * 35)
            print('Moeda de origem CÓD 3 - EUR Euro - ')
            print('--' * 35)
            break


        elif moeda_origem == '4':
            print('--' * 35)
            print('Moeda de origem CÓD 4 - PYG Guarani Paraguaio - ')
            print('--' * 35)
            break


        elif moeda_origem == '5':
            print('--' * 35)
            print('Moeda de origem CÓD 5 - CAD	Dólar Canadense - ')
            print('--' * 35)
            break

while True:
    if moeda_origem == '1':
        sigla = 'R$:'
    elif moeda_origem == '2':
        sigla = 'U$$:'
    elif moeda_origem == '3':
        sigla = '€:'
    elif moeda_origem == '4':
        sigla = '₲:'
    elif moeda_origem == '5':
        sigla = 'U$$:'

    valor_para_converter = str(input(f'Digite o Valor a ser convertido:? {sigla}'))
    print('--' * 35)

    if valor_para_converter.isnumeric():
        # print('Valor para converter caiu em números')
        quantia_convertida.append(float(valor_para_converter))
        print(f'{quantia_convertida[0]:.2f}') # --> chamando quantia a ser convertida <--
        # print('--' * 31)
        # print(f'{quantia_convertida[0]:.2f}')
        break


    else:
        print(f'\033[1;41mVALOR INVÁLIDO - SOMENTE NÚMEROS !\033[0;0m')

while True:
    converter_para = str(input('Converter para: [Digite o CÓD DA MOEDA/DESTINO]: ?'))

    if converter_para.isnumeric():
        # print('Converter para caiu em números')
        if converter_para == '1':
            print('--' * 35)
            print('Moeda de conversão CÓD 1 - BRL	Real Brasileiro - ')
            print('--' * 35)
            break

        elif converter_para == '2':
            print('--' * 35)
            print('Moeda de conversão CÓD 2 - Dólar dos Estados Unidos - ')
            print('--' * 35)
            break

        elif converter_para == '3':
            print('--' * 35)
            print('Moeda de conversão CÓD 3 - EUR Euro - ')
            print('--' * 35)
            break

        elif converter_para == '4':
            print('--' * 35)
            print('Moeda de conversão CÓD 4 - PYG Guarani Paraguaio - ')
            print('--' * 35)
            break

        elif converter_para == '5':
            print('--' * 35)
            print('Moeda de conversão CÓD 5 - CAD	Dólar Canadense - ')
            print('--' * 35)
            break

    else:
        print('--' * 35)
        print('Converter para caiu em String')
        print(f'\033[1;41mVALOR INVÁLIDO - SOMENTE NÚMEROS DE 1 A 5 QUE CORRESPONDEM AS MOEDAS CADASTRADAS:\033[0;0m')
        print('--' * 35)
print()
print('        \033[1;40m    Aguarde ! CONVERTENDO MOEDA\033[0;0m',end='')
sleep(0.3)
print('\033[1;40m.\033[0;0m',end='')
sleep(0.3)
print('\033[1;40m.\033[0;0m',end='')
sleep(0.3)
print('\033[1;40m.\033[0;0m',end='')
sleep(0.3)
print('\033[1;40m50%\033[0;0m',end='')
sleep(0.8)
print('\033[1;40m.\033[0;0m',end='')
sleep(0.8)
print('\033[1;40m.\033[0;0m',end='')
sleep(0.8)
print('\033[1;40m100%\033[0;0m',end='')
print('\033[1;40m   \033[0;0m',end='')
print('\n')

if moeda_origem == '1' and converter_para == '2':
    print('1 - caiu no que eu queria - 1 - !!!')
    moeda_origem = float(quantia_convertida[0])
    converter_para = float(0.1574)
    calculo_conversao = float(moeda_origem*converter_para)
    print('--' * 35)
    print(f'Considerando que você escolheu CÓD 1 - BRL	Real Brasileiro como\n'
          f'moeda de origem: e CÓD 2 - Dólar dos Estados Unidos - como moeda de destino.\n'
          f'É importante que você saiba que a cada R$: 1,00 real Brasileiro \n'
          f'corresponde a exatamente U$$: 0.1574 Dólar.\n'
          f'\033[1;42mSendo assim com R$: {quantia_convertida[0]:.2f} Reais, você tem exatamente €: {calculo_conversao:.2f} Euros.\033[0;0m')
    print('--' * 35)

elif moeda_origem == '1' and converter_para == '3':
    # print('2 - caiu no que eu queria - 2 - !!!')
    moeda_origem = float(quantia_convertida[0])
    converter_para = float(0.1576)
    calculo_conversao = float(moeda_origem*converter_para)
    print('--' * 35)
    print(f'Considerando que você escolheu CÓD 1 - BRL	Real Brasileiro como\n'
          f'moeda de origem: e CÓD 3 - EUR Euro - como moeda de destino.\n'
          f'É importante que você saiba que a cada R$: 1,00 real Brasileiro \n'
          f'corresponde a exatamente €: 0.1576 Euros.\n'
          f'\033[1;42mSendo assim com R$: {quantia_convertida[0]:.2f} Reais, você tem exatamente €: {calculo_conversao:.2f} Euros.\033[0;0m')
    print('--' * 35)


if converter_para == '1':
    converter_para = float(quantia_convertida[0])

elif converter_para == '2':
    converter_para = float(5.24)

elif converter_para == '3':
    converter_para = float(6.34)

elif converter_para == '4':
    converter_para = float(0.79)

elif converter_para == '5':
    converter_para = float(4.33)

print('\n                  --- | FIM DO PROGRAMA | ---')




# print(f'{calculo_conversao:.2f}')
# print(f'{moeda_origem:.2f}')
# print(f'{converter_para}')








