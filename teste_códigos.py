

dados0 =[['1','David Machado','47.98446.5314'],['2','ENOQUE','48.9987.3794']]
dados1 = {'Cód': ['1'], 'Nome': ['David Machado'], 'Telefone': ['47.98446.5314']}
dados2 = {'Cód': ['2'], 'Nome': ['Adriano Pereira'], 'Telefone': ['47.9892.7133']}
dados_p_copiar = dados0[-1][1]
dados_completo = {}
dados_completo[dados_p_copiar] = [dados0]

# print(f'{dados_completo["Enoque"]}')
while True:
    pesquisa = str(input('Digite sua busca:?')).upper()
    if pesquisa in dados_completo.keys():
        print('Sim está na Lista !')
        print(f'{dados_completo[f"{pesquisa}"]}'.replace('[','').replace(']','').replace("'",""))

    else:
        print(f'Não está na Lista !')

# print(f'{dados_completo["Enoque"]}')

# while True:
#     cod = str(input('Cód Cliente:?'))
#     dados['Cód'] = [cod]
#     nome = str(input('Qual é o seu nome:?'))
#     dados['Nome'] = [nome]
#     fone = str(input('Telefone:?'))
#     dados['Telefone'] = [fone]
# print(f'{dados.values()}')


# for c, i in enumerate(dados.values()):
#     print(f' --- {str(i):^2}',end=' ')
# print()





# dados_dicionario = {'nome':'David','telefone':'3328.9191'}
#
#
# dados_lista = [['David Machado'],['Adriano Pereira']]
# print(f'{dados_dicionario_2}')
# fim = str(input('FIM:'))
# while True:
#     pesquisa = str(input('Digite sua busca:?'))

    # if pesquisa in dados_dicionario.values():
    #     print('Sim está na lista!')
    #
    # else:
    #     print('Não está na lista!')



    # print(f'{"David" in dados_dicionario.values()}')
    # print(f'{dados_lista}')
