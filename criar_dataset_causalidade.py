#libraries for data manipulation
import numpy as np
import pandas as pd
import networkx as nx
from statsmodels.tsa.stattools import grangercausalitytests
import datetime


# Escreve log em arquivo
def EscreveLog(arquivoLog,mensagem):
    try:
        with open(arquivoLog, "a") as file:
            file.write(str(mensagem) + "\n")
            file.close()

    except:
        print("Erro na Escrita:" + mensagem + " " + str(datetime.datetime.now()))

def calcularCausalidade(a,b):
  array = pd.DataFrame()
  array[0] = b
  array[1] = a
  array.dropna()
  try:
      #perform Granger-Causality test
      causalidade_test = grangercausalitytests(array, maxlag=[3])
      tupla = causalidade_test[3]
      testes = tupla[0]
      p_values = testes['params_ftest']
      if (p_values[1] < 0.05):
        return True
      return False
  except Exception as e:
      print("Exception: ",e)
      return False

def ObterListaSeriesTemporais(dataset_metricas):
    S = []
    colunas = list(dataset_metricas.columns)
    for col in colunas:
        S.append(dataset_metricas[[col]])
    return S

def CriarGrafoCausalidadeStage1(lista_series_temporais,path_gexf,indice_alvo):
    G = nx.DiGraph()
    n = len(lista_series_temporais) - 1
    i = 0
    passos = 0
    while(i < n):
        j = (i+1)
        while(j < n):
            print("Passos: ", passos)
            if (passos == 1000):
                mensagem = "i =", i, "j = ", j
                print(mensagem)
                nx.write_gexf(G, path_gexf)
                print("Grafo Salvo")
                EscreveLog('C:/Users/loyol/Documents/log_causalidade.txt',mensagem)
                passos = 0

            array = pd.DataFrame()
            print("Criou array")
            array[0] = lista_series_temporais[i]
            print("colocou i no array")
            array[1] = lista_series_temporais[j]
            print("colocou j no array")
            array.dropna()

            existeCausalidade = calcularCausalidade(array[0], array[1])
            "Calculou causalidade i e j"
            if existeCausalidade:
                G.add_edge(i, j)

            existeCausalidade = calcularCausalidade(array[1], array[0])
            if existeCausalidade:
                G.add_edge(j, i)

            existeCausalidade = calcularCausalidade(array[0], alvo)
            if existeCausalidade:
                G.add_edge(i, indice_alvo)

            existeCausalidade = calcularCausalidade(array[1], alvo)
            if existeCausalidade:
                G.add_edge(j, indice_alvo)
            j = j + 1
            passos = passos + 1
        i = i + 1
    return G


print("Iniciando o Script:")


path_dataset_metricas_rnp = 'C:/Users/loyol/Documents/dataset_rnp_5.csv'
path_gexf = 'C:/Users/loyol/Documents/grafo_causalidade_rnp_3.gexf'

dataset_metricas = pd.read_csv(path_dataset_metricas_rnp,sep=",")

print(dataset_metricas.head())

dataset_metricas = dataset_metricas.drop(columns=['TimeStamp'])

lista_series_temporais = ObterListaSeriesTemporais(dataset_metricas)

indice_alvo = 5108

alvo = lista_series_temporais[indice_alvo]

print(alvo)


print("Inicia a Criação dos Grafos : --  " + str(datetime.datetime.now()))

G = CriarGrafoCausalidadeStage1(lista_series_temporais,path_gexf,indice_alvo)

print("Terminou a Criação do GRafo Stage 1 : --  " + str(datetime.datetime.now()))

nx.write_gexf(G, path_gexf)

print("Grafo Salvo")

print("Hello World!")