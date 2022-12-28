

arquivo = open('ativ2_nomes/weblog_entries.txt', 'r')
for linha in arquivo:
    palavras = linha.split('\t')
    #print(palavras[1])
    print ('{0}\t{1}'.format(palavras[1], 'à testar'))
