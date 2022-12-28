
chave = []
valor = []
arquivo = open('ativ3_email/dovecot_out.log', 'r')
for linha in arquivo:
    nome, contador = linha.split('\t')
    #print(nome)
    chave.append(nome)

#print(len(chave))     
#print(chave)
#print(valor)

#percorrer o vetor com todos os nomes a quantidade de vezes que seja
#equivalente ao tamanho da lista para contar todos os nomes e o bom
#que como já conta na sequência do vetor, logo, temos o par chave 
#valor, de nome e contagem
for i in range(0,len(chave)):
    for nome in chave:
        contador = chave.count(nome)
        valor.append(contador)

#print(valor)

#como ele vai contar o mesmo nome mais de uma vez,
#vou fazer um dicionário e ordenar o dicionário,
#pq assim ele remove as duplicatas

#Criar um dicionário a partir de 2 listas
dicionario = dict(zip(chave,valor))
#print(dicionario)

for i in sorted(dicionario, key = dicionario.get, reverse=True):
    #print(i, dicionario[i])
    #print('{0}\t{1}'.format(i, dicionario[i]))
    if dicionario[i] >= 100:
        print("Nome: {0}\tQtd_Acessos: {1}".format(i, dicionario[i]))

arquivo.close()