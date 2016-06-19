###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF968 -- Programacao 1
#
# Autor: José Wilson Madruga Rezende FIlho
#            
#
# Email:    jwmrf@cin.ufpe.br
#           
#
# Data:        2016-06-19
#
# Descricao:  Este e' um modelo de arquivo para ser utilizado para a implementacao
#                do projeto pratico da disciplina de Programacao 1. 
#                 A descricao do projeto encontra-se no site da disciplina e trata-se
#                de uma adaptacao do projeto disponivel em 
#                http://nifty.stanford.edu/2016/manley-urness-movie-review-sentiment/
#                O objetivo deste projeto e' implementar um sistema de analise de
#                sentimentos de comentarios de filmes postados no site Rotten Tomatoes.
#
# Licenca: The MIT License (MIT)
#            Copyright(c) 2016 Wilson Filho
#
###############################################################################
import sys
import re
#Função para REMOVER Caracteres Desnecessários em Fim de Linhas e Tornar o texto Minúsculo.
def clean_up(x):
    punctuation = ''''!"',;:.-?)([]<>*#\n\t\r'''
    result = x.lower().strip(punctuation).replace("-"," ")
    return result.replace("/"," ")
#Função semelhante ao split comun, mas feita para fazer sublistas em listas, aplicando também a função clean_up()
def split(x):
    contador = 0
    for a in x:
        a = clean_up(a)
        x[contador] = a.split()
        contador+=1
    return x
#Função que retorna uma lista com as StopWords.
def stopwords():
    stopwordis = open("stopwords.txt","r").read()
    stopwordis =stopwordis.split("\n")
    return stopwordis
#Função que lê o arquivo de treino e nele retorna um dicionário com a média de cada palavra.        
def dicionario_palavras(x):
    x = split(x)
    dicionario = {}
    contador = 0
    while(contador!=len(x)):
        for a in x[contador]:
            if a not in stopwords() and a not in dicionario:
                dicionario[a]=[int(x[contador][0]),1]
            elif a not in stopwords():
                dicionario[a]+=dicionario[a][0]+int(x[contador][0]),dicionario[a][1]+1
        contador += 1
    for a in dicionario:
        dicionario[a]=dicionario[a][0]//dicionario[a][1]   
    return dicionario
#Função responsável por fazer o cálculo entre a média das palavras de treino e comparálas com as notas dos reviews no arquivo de teste
#E realizando a soma do quadrado dos erros.
def quadrado_erros(x,y):
    dicionario=dicionario_palavras(x)
    contador = 0
    total=0.0
    y = split(y)
    while(contador!=len(y)):
        somador=[0,0]
        for a in y[contador]:
            if a not in stopwords() and a in dicionario:
                somador=somador[0]+dicionario[a],somador[1]+1
            elif a not in stopwords() and a not in dicionario:
                somador=somador[0]+2,somador[1]+1
        if int(y[contador][0])!=somador[0]/somador[1]:
            total+=(int(y[contador][0])-(somador[0]/somador[1]))**2
        contador+=1
    return total/contador
# FUNÇÃO PRINCIPAL RESPONSÁVEL PELA LINHA DE ARGUMENTO, ONDE ENTRAM OS ARQUIVOS "trainSet.txt" e "testSet.txt".
def main():
    if len(sys.argv) < 3:
        print ('Numero invalido de argumentos')
        print ('O programa deve ser executado como python projeto.py <arq-treino> <arq-teste>')
        sys.exit(0)
    words = open(sys.argv[1],"r").readlines()
    reviews = open(sys.argv[2],"r").readlines()
    return "A soma dos quadrados dos erros é: "+format("%.1f"%quadrado_erros(words,reviews))

if __name__ == '__main__':
    print(main())

#Observação: Fiz meu projeto num sistema linux que utiliza o Debian, o resultado saí em cerca de 18 segundos, já num windows é questão de minutos,
#Mas nada que atrapalhe ou influencie no resultado final.










	
