
chave = []
arquivo = open('ativ2_nomes/weblog_entries_out.txt', 'r')
for linha in arquivo:
    palavra, teste = linha.split('\t')
    #print(len(palavra))
    #print(type(contador))
    #só ajuste de tamanho da sring, contando com o '.html' já da 5 caracteres 
    if 5 < len(palavra) <= 10:
        chave.append(palavra)

valor = "<=5"
#print(chave)
#print(valor)

#Criar um dicionário com a mesma chave
#dicionario = dict.fromkeys(chave, valor)
#print(dicionario)

# como ele não quer saber as quantidade das palavras, para diminuir as palavras repetidas
#  e no dicionário as chaves não se repetem, então...
#for i in dicionario:
    #print('{0}\t{1}'.format(i, dicionario[i]))
# mas o professor quer todas as ocorrências kkkkkkk, então dicionário não dá
for i in chave:
    print('{0}\t{1}'.format(i, valor))