
arquivo = open('ativ1_salarios/salarios.csv', 'r')
for linha in arquivo:
    palavras = linha.split(',')
    nome1 = palavras[0]
    nome2 = palavras[1]
    nome = nome1 + " " + nome2
    if len(palavras) == 9:
        salario = palavras[7]
    elif len(palavras) == 8:
        salario = palavras[6]
    else:
        salario = palavras[5]

    print ('{0}\t{1}'.format(nome, salario))

arquivo.close()