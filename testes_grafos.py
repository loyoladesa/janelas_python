import numpy as np
import pandas as pd
import networkx as nx
from statsmodels.tsa.stattools import grangercausalitytests
import datetime


def ObterListaSeriesTemporais(dataset_metricas):
    S = []
    colunas = list(dataset_metricas.columns)
    for col in colunas:
        S.append(dataset_metricas[[col]])
    return S


path_dataset_metricas_rnp = 'C:/Users/loyol/Documents/dataset_rnp_5.csv'
path_gexf = 'C:/Users/loyol/Documents/grafo_causalidade_rnp_2.gexf'



G = nx.read_gexf(path_gexf)


nodes = G.nodes()
print(nodes) # [4, 5]
print('--- ')
print(nx.edges(G,nbunch=nodes))


n_vertices = G.number_of_nodes()

n_arestas = G.number_of_edges()
print('vertices: ', n_vertices, '\narestas: ', n_arestas)

