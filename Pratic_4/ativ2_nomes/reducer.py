#!/usr/bin/env python3
import sys
chave = []
# Process each key-value pair from the mapper
for linha in sys.stdin:
    palavra, teste = linha.split('\t')
    #print(len(palavra))
    #print(type(contador))
    #só ajuste de tamanho da sring, contando com o '.html' já da 5 caracteres 
    if 5 < len(palavra) <= 10:
        chave.append(palavra)
#esse valor é só para organizar a saída e ficar arrumadinho :)
valor = "<=5"
#print(chave)
#print(valor)

for i in chave:
    print('{0}\t{1}'.format(i, valor))