
#!/usr/bin/env python3
import sys
# Read each line from stdin
for linha in sys.stdin:
    palavras = linha.split(',')
    #como a separação é por vírgulas, tô somando as
    #duas primeiras strings para fazer o nome completo
    nome1 = palavras[0]
    nome2 = palavras[1]
    nome = nome1 + " " + nome2
    #essa parte é o teste para garantir de pegar o penúltimo
    #salário, pq tem uns que tem dois e outros só tem 1
    if len(palavras) == 9:
        salario = palavras[7]
    elif len(palavras) == 8:
        salario = palavras[6]
    else:
        salario = palavras[5]

    print ('{0}\t{1}'.format(nome, salario))
