#!/usr/bin/env python3
import sys
# Read each line from stdin
for linha in sys.stdin:
    palavras = linha.split(' ')
    # se no vetor de palavras estiver contido a palavra login, eu imprimo
    # só a palavra "user=<xxxxxx>," e em seguida faço o tratamento com 
    # a função strip para remover só o nome do usuário daí de dentro,
    # começando como se cada usuário fosse diferente, com um acesso
    # aí no reducer eu faço a contagem
    if "Login:" in palavras:
        #print(palavras[7].strip()[6:-2])
        print ('{0}\t{1}'.format(palavras[7].strip()[6:-2], 1))