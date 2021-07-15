import os
import fun_matriz
import fun_lista

ch = False
while(ch == False):
    entrada1 = input('\n-Informe o nome do arquivo: ')
    entrada = entrada1 + '.txt'
    ch = os.path.exists(entrada)
    if ch == False:
        entrada = entrada1 + '.dat'
        ch = os.path.exists(entrada)
    if ch == False:
        print("\nInfelizmente não foi possivel encontrar esse arquivo, tente novamente com um nome valido")
        espera = input('\t...aperte enter para continuar...')
arquivo = open(entrada, 'r')

print('\tEscolha o tipo de representação do grafo:')
chave = input('\t\t(1 para lista de adjacencias  /  2 para matriz de adjacencias) -> ')
chave = int(chave)

print('\n\n-Grafo:')
if chave == 1:
    saida = fun_lista.Grafo_Lista(arquivo)
    for item in saida.grafo:
        print(item)
else:
    saida = fun_matriz.Grafo_Matriz(arquivo)
    for i in range(saida.num_vertices):
        for j in range(saida.num_vertices):
            print(" %d" % (saida.grafo[i][j]), end="")
        print('\n')
arquivo.close()

print('-Numero de vertices:', saida.num_vertices)
print('-Numero de arestas:', saida.num_arestas)
print('-Maior grau:', saida.maior_grau[1], '| | no vertice:', saida.maior_grau[0])
print('-Menor grau:', saida.menor_grau[1], '| | no vertice:', saida.menor_grau[0])
print('-Media grau:', saida.media_grau)
print('-Frequencia relativa:')
for (grau, freq) in saida.frequencia:
    print('->Grau', grau, ': ', freq)
print('-Componentes conexas:', saida.componentes_conexas)
for item in saida.num_conexa:
    print('->', item, 'vertices')

fim = input()