import os
import time
import fun_matriz
import fun_lista

ch = False
entrada = ''
while not ch:
    entrada = input('\n-Informe o nome do arquivo: ')
    ch = os.path.isfile(entrada)
    if not ch:
        print("\nInfelizmente não foi possivel encontrar esse arquivo, tente novamente com um nome valido")
        espera = input('\t...aperte enter para continuar...')
arquivo = open(entrada, 'r')


print('\tEscolha o tipo de representação do grafo:')
chave = input('\t\t(1 para lista de adjacencias  /  2 para matriz de adjacencias) -> ')
chave = int(chave)

print('\n\n-Grafo:')
if chave == 1:
    saida = fun_lista.GrafoLista(arquivo)
    if saida.num_vertices < 15:
        for item in saida.grafo:
            print('\t', item)
    else:
        print('\tDesculpe, é inviavel imprimir este grafo')
else:
    saida = fun_matriz.GrafoMatriz(arquivo)
    if saida.num_vertices < 15:
        for item in saida.grafo:
            print('\t', item)
    else:
        print('\tDesculpe, é inviavel imprimir este grafo')

print('-Numero de vertices:', saida.num_vertices)
print('-Numero de arestas:', saida.num_arestas)
print('-Maior grau:', saida.maior_grau[1], '| | no vertice:', saida.maior_grau[0])
print('-Menor grau:', saida.menor_grau[1], '| | no vertice:', saida.menor_grau[0])
print('-Grau Medio :', saida.media_grau)
print('-Distribuição relativa:')
for (grau, freq) in saida.distribuicao:
    print('\t->Grau', grau, ': ', freq)
print('-Componentes conexas:', saida.componentes_conexas)
for item in saida.num_conexa:
    print('\t->', item, 'vertices')
print('-Tempo de execução de todas as funcionalidades :',  saida.tempo_total)
print('-Tempo de execução na criação da representação :',  saida.tempo_cria_representacao)
print('-Tempo de execução de busca largura :',  saida.tempo_largura)
print('-Tempo de execução de busca profundidade :',  saida.tempo_profundidade)
fim = input()