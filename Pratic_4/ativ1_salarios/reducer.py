
#!/usr/bin/env python3
import sys
chave = []
valor = []
# Process each key-value pair from the mapper
for linha in sys.stdin:
    nome, salario = linha.split('\t')
    #print(nome)
    chave.append(nome)
    salario = int(salario.strip()[1:-3])
    #print(type(salario))
    valor.append(salario)
    #print ('{0}\t{1}'.format(nome, salario))
    
#print(chave)
#print(valor)

#Criar um dicionário a partir de 2 listas
dicionario = dict(zip(chave,valor))
#print(dicionario)

#ordenar o dicionário pelo valor maior até o menor
cont = 0
for i in sorted(dicionario, key = dicionario.get, reverse=True):
    #print(i, dicionario[i])
    #print('{0}\t{1}'.format(i, dicionario[i]))
    print("Nome: {0}\tSalário: ${1:.2f} ".format(i, dicionario[i]))
    cont = cont + 1
    if cont == 10:
        break