#!/usr/bin/env python3
import sys
# Read each line from stdin
for linha in sys.stdin:
    palavras = linha.split('\t')
    #print(palavras[1])
    #coloquei essa string "à testar" apenas para passar no formato de tabulação
    print ('{0}\t{1}'.format(palavras[1], 'à testar'))
