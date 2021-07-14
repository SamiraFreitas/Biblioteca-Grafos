import fun_matriz
entrada = input('Informe o nome o arquivo:')
entrada= entrada+'.dat'
arquivo = open(entrada, 'r')

print('\t','Informe a escolha de representação:')
bit = input('\t\t(1 - LISTA DE ADJACENCIAS || 2- MATRIZ DE ADJACENCIAS ) -> ')
bit = int(bit)

if bit == 1:
    "saida= fun_lista.Grafo_Lista(arquivo)"
else:
    saida = fun_matriz.Grafo_Matriz(arquivo)

arquivo.close()



print('-Grafo:\n\n')
for i in range(saida.num_vertices):

    for j in range(saida.num_vertices):
        print(" %d" % (saida.grafo[i][j]), end="")
    print('\n')


print('\tNumero de vertices:', saida.num_vertices)
print('\tNumero de arestas:', saida.num_arestas)
print('\tMaior grau:', saida.maior_grau[1],' no vertice:', saida.maior_grau[0])
print('\tMaior grau:', saida.menor_grau[1],' no vertice:', saida.menor_grau[0])
print('\tMedia grau:', saida.media_grau)
print('Componentes conexas:', saida.componentes_conexas)
for item in saida.num_conexa:
    print('-',item, 'vertices')














