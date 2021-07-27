import os
import fun_matriz
import fun_lista

ch = False
entrada = ''
print('\n-Informe o arquivo: ')
primeira_tentativa = True
while not ch:
    ch = True
    if not primeira_tentativa: # verifica se é a primeira vez que tenta entrar com o nome do arquivo
        print("\n-Infelizmente não foi possivel encontrar esse arquivo, tente novamente com um nome valido")
    print('\t( Formato indicado: nome_do_arquivo.txt ou nome_do_arquivo.dat )')
    entrada = input('\t arquivo: ')
    ch = os.path.isfile(entrada) # verfica se o arquivo existe
    primeira_tentativa = False
arquivo = open(entrada, 'r') # abrir arquivo para leitura

print('\n\tEscolha o tipo de representação do grafo:')
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
arquivo.close() #fechar arquivo

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