
arquivo = open('ativ3_email/dovecot.log', 'r')
for linha in arquivo:
    palavras = linha.split(' ')
    # se no vetor de palavras estiver contido a palavra login, eu imprimo
    # só a palavra "user=<xxxxxx>," e em seguida faço o tratamento com 
    # a função strip para remover só o nome do usuário daí de dentro,
    # começando como se cada usuário fosse diferente, com um acesso
    # aí no reducer eu faço a contagem
    if "Login:" in palavras:
        #print(palavras[7].strip()[6:-2])
        print ('{0}\t{1}'.format(palavras[7].strip()[6:-2], 1))

arquivo.close()