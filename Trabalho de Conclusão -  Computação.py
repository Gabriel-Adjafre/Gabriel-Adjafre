# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 23:56:44 2021

@author: Gabriel Adjafre
"""

# Alunos: Gabriel Adjafre, Gabriel Freire e João Pedro Azevedo


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics as st
from sklearn.linear_model import LinearRegression
import math as mt


df0 = pd.read_csv('players_stats.csv') #A base é bem limpa, então facilita o uso
df0['PPG']=df0['PTS']/df0['Games Played']
df= df0.sort_values(['PPG'], ascending=False) #Dados ordenados por PPG, padrão da NBA
df.rename(columns={'Collage': 'College'}, inplace=True) #Corrigindo erro gramatical da base
df.index = df['Name']
df_sal=pd.read_csv('C:/Users/gabri/Documents/Salários NBA 2014-15.csv')

# Em primeiro lugar, o arquivo sofreu duas correções. A primeira foi que, para deixarmos no padrão NBA, 
# criamos uma nova coluna chamada PPG (pontos por jogo) e ordenamos o data frame segundo ela, para deixar os jogadores
# ordenados segundo os critérios oficiais da NBA. Além disso, indexamos o nome dos jogadores e corrigimos o nome de uma 
# coluna, que era denominada ‘Collage’ e se tornou ‘College’, escrita correta de algo equivalente a 'universidade' em inglês.


def StatJogador(nome): #A função mostra as estatísticas completas do jogador inserido.
    sj=df.transpose()
    print(sj[nome]) 
#Ao longo do relatório iremos utilizar nas análises, preferencialmente, os jogadores que tiveram mais pontos por jogo,
# ou seja, Russell Westbrook e James Harden, que, mesmo se destacando nessa questão, não foram eleitos MVP (Most Valuable 
# Player ou, em português, ‘Jogador Mais Valioso’) da temporada, pois o jogador Stephen Curry venceu o prêmio.
# Console: StatJogador(‘Russell Westbrook’)



# As funções Top5(stat) e Top5Pos(posiçao), possuem como entrada a estatística desejada e a posição desejada, 
# respectivamente. A primeira retorna os 5 melhores jogadores em relação ao que foi inserido e a segunda retorna 
# os 5 melhores pontuadores por posição.
def Top5(stat): #Stat: qualquer coluna numérica de df
    t5=df.sort_values([stat], ascending=False)
    print(t5[stat].head(5))
# Console: Top5('PPG')
    
    
def Top5Pos(posiçao): #Posições: 'PG', 'SG, 'SF', 'PF', 'C'.
    top5pos=[]
    n=0
    for pos in df['Pos']:
        if pos == posiçao:
            top5pos.append(df['Name'][n])
            top5pos.append(df['PPG'][n])
            n=n+1
        else:
            n=n+1
            pass
    print(top5pos[0:10])
# Console: Top5Pos('SG')
    
    
def ComparaJogador(nome1, nome2): #Exibe as estatísticas dos jogadores inseridos. a fim de fazer uma comparação.
     cj=df.transpose()
     cj= pd.DataFrame(cj,columns=[nome1, nome2])
     print(cj)
# Comparando cara-a-cara os maiores pontuadores, podemos perceber que Harden jogou mais jogos que Westbrook e, portanto,
# não podemos comparar de forma igual os números totais de pontos, assistências e etc dos dois. Porém, podemos comparar
# o percentual, ou seja, PPG, FG% (porcentagem de arremessos de quadra convertidos, ou seja, FGM/FGA), 3P% (arremessos de 3
# pontos convertidos, 3PM/3PA), FT% (lances-livre convertidos, FTM/FTA), AST/TOV (assistências por desperdício de bola) e
# STL/TOV (roubos de bola por desperdício de posse).
# Comparando as estatísticas citadas, percebemos que os números são muito parecidos (alguns até iguais, como STL/TOV), mas
# Harden leva vantagem considerável de 7.6% em 3P% e Westbrook se sobressai em AST/TOV, com 0.2 a mais (uma assistência a
# mais que Harden a cada 5 posses)
# Console: ComparaJogador(‘Russell Westbrook’, ‘James Harden’)

def JogUni(): #A função mostra as 5 universidades que mais enviam jogadores à NBA, expressando quais são as mais tradicionais
#no que diz respeito à formação de jogadores de basquete de elite.
    df_novo=df.dropna()
    moda=df['College'].value_counts()
    print(moda.head(5))
# Elas são, no caso, Duke, com 18 jogadores, University of North Carolina, UCLA, University of Kentucky (com 15 cada) 
# e University of Kansas, com 13.
# Console: JogUni()

    
def QualJog(uni):
    qj=df.transpose()
    lista=[]
    n=0
    for universidade in df['College']:
        if universidade==uni:
            lista.append(df['Name'][n])
            n=n+1
        else:
            n=n+1
            pass
    pontos=qj[lista[0]][34]+qj[lista[1]][34]+qj[lista[1]][34]+qj[lista[2]][34]+qj[lista[3]][34]+qj[lista[4]][34]
    print(lista, pontos)
        
# Mostrar quais jogadores eram daquela universidade
# Se der, fazer um 5x5 das universidades com mais jogadores e ver quanto seria o jogo (soma dos PPG)


def StatCrescente(stat): # Ela mostra uma curva crescente da estatística inserida em relação a todos os jogadores
#Iremos trabalhar com o stat='PPG', para vermos a discrepância entre os melhores e os piores jogadores
    sc=df.sort_values([stat], ascending = True)
    plt.plot(sc[stat])
    # A partir do gráfico, podemos observar que nos primeiros dois terços a inclinação da curva é pequena, ou seja,
    #  a discrepância não é tão grande (fica ali entre 0 e entre 10 e 12 PPG). Porém, no último terço do gráfico, vemos uma
    #  inclinação altíssima, mostrando o quão melhor os 'melhores' são dos 'médios'. Os seus números de PPG crescem mais que
    #  o dobro do maior 'médio', indo da faixa citada (por volta do intervalo entre 10 e 12 PPG) para acima dos 25 PPG.
    # Podemos observar que o mesmo fenômeno se dá para as entradas stat='AST' e stat='REB', ou seja, nas 3 estatísticas
    #  mais relevantes do basquete, há uma disparidade muito grande entre os que são muito bons.
    # Console: StatCrescente(‘PPG’), StatCrescente(‘AST’) e StatCrescente(‘REB’)

def GrafStat(stat1, stat2): # Essa função recebe duas entradas para mostrar um gráfico relacionando duas estatísticas
# Iremos usar o exemplo de PPG por idade para analisarmos qual a idade média para se atingir o auge, quando começa-se a
#perder rendimento pela idade e, após testarmos, achamos outras curiosidades interessantes, como o fato de aos 37 anos,
# a média de pontos por jogo aumentar substancialmente, o que não faria sentido por ser uma idade mais avançada e na qual os
# jogadores, na maioria esmagadora dos casos, já passou do seu auge.
    df1= df.sort_values(['Age'])
    df2= df.sort_values(['Age'], ascending = False)
    jogs_37=[]
    n=0
    plt.bar(df1[stat1], df1[stat2])
    plt.title(stat1 + ' por ' + stat2)
    if stat1=='Age':
        print('O jogador mais velho tem ', df2['Age'][0])
        print('O jogador mais novo tem ', df1['Age'][0])
        # Quais jogadores têm 37 anos? Motivo: entender pq a média de PPG volta a crescer.
        for idade in df1['Age']:
            if idade == 37:
                jogs_37.append(df1['Name'][n])
                n=n+1
            else:
                n=n+1
                pass
        print(jogs_37)
    # Um ponto que chama atenção é o fato de a barra dos 37 ser muito mais elevada do que todas após os 32 anos. Por quê?
    # Ao vermos a lista com tais jogadores, podemos observar 3 dos 4 jogadores com 37 anos são all-stars e 3 deles 
    # são campeões da NBA.
    # Um (Kobe) está nas discussões de melhor de todos os tempos e outro (Dirk) é unanimemente top3 estrangeiros
    # da história da NBA.
    # Esses fatores (a baixa quantidade de jogadores e suas respectivas qualidades) justificam um PPG médio > 20 numa
    # idade tão avançada.
    # Além disso, pela análise do gráfico, podemos inferir que o auge (idade com maior PPG) corresponde aos 26 anos de idade.
    # O ponto em que podemos observar uma queda permanente (ou seja, que não é um ano atípico) se dá aos 32 anos,
    # pois a partir dessa idade o PPG nunca volta a ser tão alto quanto o dos 31 anos.
    # Console: GrafStat('Age', 'PPG')
            

def JogMed():
    colunas = ['Games Played','MIN','PTS','FGM','FGA','FG%','3PM','3PA','3P%','FTM','FTA','FT%','OREB','DREB','REB','AST','STL','BLK','TOV','PF','EFF','AST/TOV','STL/TOV','Age', 'Height', 'Weight', 'BMI', 'PPG']
    df_med = df[colunas].mean()
    print('O jogador médio teria as médias: ')
    print(df_med)
    print('Vamos comparar com a mediana para saber se mais da metade dos jogadores está abaixo da média,o que demonstraria um desbalanceamento e uma disparidade muito grande entre os jogadores.')
    df_mediano = df[colunas].median()
    df.loc['Media']=df_med
    df.loc['Mediano']=df_mediano
    jm=df.transpose()
    df_compara= pd.DataFrame(jm,columns=['Media', 'Mediano'])
    print(df_compara)
    x=['Games Played','MIN','PTS','FGM','FGA','FG%','3PM','3PA','3P%','FTM','FTA','FT%','OREB','DREB','REB','AST','STL','BLK','TOV','PF','EFF','AST/TOV','STL/TOV','Age', 'Height', 'Weight', 'BMI', 'PPG']
    y1=df_med.tolist()
    y2=df_mediano.tolist()
    plt.plot(x, y1, marker ='o', label = 'Média')
    plt.plot(x, y2, marker ='o', label = 'Mediana')
    plt.legend()
    plt.xticks(range(len(x)), x, rotation=(90))
# Primeiramente são exibidas as stats do jogador que teria estatísticas iguais a da média da NBA inteira. Depois, é
# gerada uma tabela para comparar a média com a mediana lado a lado e, por fim, um gráfico mostrando qual é maior.
# Analisando o gráfico, é possível perceber que a média se mostra maior ou igual à mediana em todos os pontos,
# o que revela que a há mais jogadores abaixo da média do que acima. Esse fato se articula com a função StatCrescente,
# pois esta revela que há aproximadamente 2/3 dos jogadores possuem menos da metade dos PPG dos líderes em pontuação da NBA.
# Console: Jogmed()
        
def JogEfi():
    df['Eficiência']=df['PTS']/df['MIN']
    df_efi=df.sort_values(['Eficiência'], ascending=False)
    top10_efi=(df_efi['Name']).head(10)
    df_eff=df.sort_values(['EFF'], ascending=False)
    top10_eff=(df_eff['Name']).head(10)
    print('Eficiência (pontuação) ',' Eficiência (NBA Rating)')
    print(top10_efi[0], '      ', top10_eff[0])
    print(top10_efi[1], '           ', top10_eff[1]) 
    print(top10_efi[2], '           ', top10_eff[2]) 
    print(top10_efi[3], '          ', top10_eff[3]) 
    print(top10_efi[4], '       ', top10_eff[4])
# Criamos um método de medir a eficiência na pontuação para comparar com a métrica oficial da NBA (EFF), dada 
# por [(PTS + REB + AST + STL + BLK − Missed FG − Missed FT - TO) / GP]. A nossa métrica, chamada de Efi, se baseou 
# na pontuação, medindo quantos pontos por minuto os jogadores conseguem fazer. Logo, pegamos o top5 desse novo 
# método (Efi) e o top5 da métrica oficial (EFF) para compararmos se os jogadores com mais pontos por minuto também são 
# eficientes na métrica oficial. O resultado foi que o líder em PPG, Russell Westbrook, também liderou o ranking de Efi, mas 
# não apareceu no top5 de EFF, mostrando que ele é eficiente fazendo pontos, mas deixa a desejar no que diz respeito às 
# outras partes importantes do jogo, como por exemplo na retenção da posse, já que muitos desperdícios atrapalham o time e 
# geram contra-ataques. Os dois únicos jogadores que aparecem nos 2 top5 são James Harden e Stephen Curry, o MVP da 
# temporada, mostrando que ambos são eficientes pontuando e jogando em geral. (Console: JogEfi())
 
    
def Regressão(stat1, stat2):
    df_aux=df.sort_values([stat1], ascending=False)
    x = np.array(df[stat1]).reshape((-1, 1))
    y = np.array(df[stat2]).reshape((-1, 1))
    regressao = LinearRegression().fit(x,y)
    coef = round(regressao.score(x,y), 3)
    print(coef)
    pred_y = regressao.predict(x)
    plt.scatter(x, y, s=20, alpha=.3)
    plt.plot(x, pred_y, color = 'black')                  
    plt.title('Regressão Linear entre ' + stat1 + ' e ' + stat2)         
    plt.xlabel(stat2)                                   
    plt.ylabel(stat1)                                
    plt.text(200,5, 'Regressão:' + str(coef))
    plt.annotate(df_aux['Name'][0], (1500, 1750))
# Fizemos uma função que cria um gráfico com a regressão linear com as estatísticas inseridas na função. 
# Achamos que o exemplo de PTS por FGA ficou com uma boa visualização, pois trouxe um resultado bem homogêneo e próximo 
# à linha do Harden (maior pontuador).
# Console: Regressão('PTS', 'FGA')

    
def AmericanosVsEstrangeiros():
    n=0
    listaAmericanos = []
    listaEstrangeiros = []
    for lugar in df['Birth_Place']:
        if lugar == 'us':
            listaAmericanos.append(df['Name'][n])
            n=n+1
        else:
            pass
            n=n+1
    n=0
    for lugar in df['Birth_Place']:
        if lugar != 'us' and str(lugar) != 'nan':
            listaEstrangeiros.append(df['Name'][n])
            n=n+1
        else:
             pass
             n=n+1
    AvE=df.transpose()
    eua=int(AvE[listaAmericanos[0]][34]) + int(AvE[listaAmericanos[1]][34]) + int(AvE[listaAmericanos[2]][34]) + int(AvE[listaAmericanos[3]][34]) + int(AvE[listaAmericanos[4]][34])
    world=int(AvE[listaEstrangeiros[0]][34]) + int(AvE[listaEstrangeiros[1]][34]) + int(AvE[listaEstrangeiros[2]][34]) + int(AvE[listaEstrangeiros[3]][34]) + int(AvE[listaEstrangeiros[4]][34])
    resultado= ('Team USA', eua, 'x', world, 'Team World')
    print('Team USA starting lineup:', listaAmericanos[0:5])
    print('Team World starting lineup:', listaEstrangeiros[0:5])
    print(resultado)
# Pegamos os 5 maiores pontuadores estadunidenses e comparamos com os 5 maiores pontuadores nascidos fora 
# dos Estados Unidos para comparar, já que, hoje, na temporada 2021-22, o atual MVP é sérvio (Nikola Jokic),
# o melhor defensor (ganhador do prêmio DPOY) é francês (Rudy Gobert) e a grande estrela jovem é eslovena (Luka Doncic).
# Foram formados dois times: o ‘Team USA’, com os 5 jogadores americanos de maior PPG, e o ‘Team ‘World’, análogo ao 
# Team USA mas com apenas jogadores não nascidos em território norte-americano. Infelizmente, os jogadores estrangeiros 
# de destaque hoje ainda não estavam na liga ou não eram destaques ainda, então os estrangeiros que representaram o
# ‘Team World’ na temporada em questão, 2014-15, perderam de 125 x 92 para o ’Team USA’, uma derrota muito elástica para 
# os padrões da NBA, o equivalente a uma grande goleada no futebol.
# Console: AmericanosVsEstrangeiros()

def NovoMVP():
    nm=df.transpose()
    # nm['Fulano']
    # Critérios: O MVP será dado por (5*PPG + 3*APG + 3*RPG + SPG + BPG -2*TPG)*(FG%+3P%+FT%)/2
    # APG = AST/GP, RP=REB/GP, SPG=STL/GP, BPG=BLK/GP e TPG=TOV/GP.
    # Concorrentes: Stephen Curry, Russell Westbrook, James Harden, LeBron James e Anthony Davis
    # Eles foram os 5 mais votados para o prêmio. Kevin Durant foi o terceiro maior pontuador por jogo, mas jogou apenas
    # 27 jogos devido a uma lesão, então não jogou o suficiente para poder participar da votação.
    listaWestbrook=[nm['Russell Westbrook'][34], nm['Russell Westbrook'][16]/nm['Russell Westbrook'][1], nm['Russell Westbrook'][15]/nm['Russell Westbrook'][1],nm['Russell Westbrook'][17]/nm['Russell Westbrook'][1],nm['Russell Westbrook'][18]/nm['Russell Westbrook'][1],nm['Russell Westbrook'][19]/nm['Russell Westbrook'][1],nm['Russell Westbrook'][6],nm['Russell Westbrook'][9],nm['Russell Westbrook'][12]]
    listaCurry=[nm['Stephen Curry'][34], nm['Stephen Curry'][16]/nm['Stephen Curry'][1], nm['Stephen Curry'][15]/nm['Stephen Curry'][1],nm['Stephen Curry'][17]/nm['Stephen Curry'][1],nm['Stephen Curry'][18]/nm['Stephen Curry'][1],nm['Stephen Curry'][19]/nm['Stephen Curry'][1],nm['Stephen Curry'][6],nm['Stephen Curry'][9],nm['Stephen Curry'][12]]
    listaLebron=[nm['LeBron James'][34], nm['LeBron James'][16]/nm['LeBron James'][1], nm['LeBron James'][15]/nm['LeBron James'][1],nm['LeBron James'][17]/nm['LeBron James'][1],nm['LeBron James'][18]/nm['LeBron James'][1],nm['LeBron James'][19]/nm['LeBron James'][1], nm['LeBron James'][6], nm['LeBron James'][9], nm['LeBron James'][12]]
    listaAD=[nm['Anthony Davis'][34], nm['Anthony Davis'][16]/nm['Anthony Davis'][1], nm['Anthony Davis'][15]/nm['Anthony Davis'][1],nm['Anthony Davis'][17]/nm['Anthony Davis'][1],nm['Anthony Davis'][18]/nm['Anthony Davis'][1],nm['Anthony Davis'][19]/nm['Anthony Davis'][1], nm['Anthony Davis'][6], nm['Anthony Davis'][9], nm['Anthony Davis'][12]]
    listaHarden=[nm['James Harden'][34], nm['James Harden'][16]/nm['James Harden'][1], nm['James Harden'][15]/nm['James Harden'][1],nm['James Harden'][17]/nm['James Harden'][1],nm['James Harden'][18]/nm['James Harden'][1],nm['James Harden'][19]/nm['James Harden'][1],nm['James Harden'][6],nm['James Harden'][9],nm['James Harden'][12]]
    Westbrook=(5*listaWestbrook[0]+3*listaWestbrook[1]+3*listaWestbrook[2]+listaWestbrook[3]+listaWestbrook[4]-2*listaWestbrook[5])/(listaWestbrook[6]+listaWestbrook[7]+listaWestbrook[8])/2
    Curry= (5*listaCurry[0]+3*listaCurry[1]+3*listaCurry[2]+listaCurry[3]+listaCurry[4]-2*listaCurry[5])/(listaCurry[6]+listaCurry[7]+listaCurry[8])/2
    Lebron=(5*listaLebron[0]+3*listaLebron[1]+3*listaLebron[2]+listaLebron[3]+listaLebron[4]-2*listaLebron[5])/(listaLebron[6]+listaLebron[7]+listaLebron[8])/2
    AD= (5*listaAD[0]+3*listaAD[1]+3*listaAD[2]+listaAD[3]+listaAD[4]-2*listaAD[5])/(listaAD[6]+listaAD[7]+listaAD[8])/2
    Harden=(5*listaHarden[0]+3*listaHarden[1]+3*listaHarden[2]+listaHarden[3]+listaHarden[4]-2*listaHarden[5])/(listaHarden[6]+listaHarden[7]+listaHarden[8])/2
    Lista=sorted([Westbrook, Curry, Lebron, AD, Harden])
    print('Westbrook: ', Westbrook)
    print('Curry: ', Curry)
    print('Lebron: ', Lebron)
    print('Anthony Davis: ', AD)
    print('Harden: ', Harden)
    print(Lista)
    print('1- Russell Westbrook')
    print('2- Anthony Davis')
    print('3- LeBron James')
    print('4- James Harden')
    print('5- Stephen Curry')    
    
#Projeto avulso:
# codigo = 11418 
# url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json'.format(codigo)
# df = pd.read_json(url)
# df2 = df.loc[32:40]
# n=32
# lista=[0]
# while n<= 40:
#   if df2['valor'][n]<=df2['valor'][n+1]:
#     print('A dívida também cresceu no período')
#     lista.append(1)
#   else:
#     pass
# if lista==[0]:
#  print('A dívida caiu todos os anos.')


    



