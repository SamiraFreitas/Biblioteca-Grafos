import timeit

class GrafoMatriz:
    # Classe com todos os atributos e metodos do grafo na representação matriz de adjacencias
    def __init__(self, arquivo):
        (self.num_vertices, self.num_arestas, self.grafo, self.tempo_cria_representacao) = self.converte_matriz(arquivo)
        (self.maior_grau, self.menor_grau, self.media_grau, self.frequencia) = self.definir_graus()
        self.tempo_largura = self.busca_largura_matriz(1)
        self.tempo_profundidade = self.busca_profundidade_matriz(1)
        (self.componentes_conexas, self.num_conexa) = self.conexidade()

    def converte_matriz(self, arquivo):
        # Converte o grafo do arquivo .dat em uma matriz de adjacencias
        inicio2 = timeit.default_timer()
        linha = arquivo.readline()
        conteudo = linha.split(' ')
        num_vertices = int(conteudo[0])
        num_arestas = int(conteudo[1])
        grafo = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
        for linha in arquivo:
            conteudo = linha.split(' ')
            v1 = int(conteudo[0])
            v2 = int(conteudo[1])
            a = int(conteudo[2])
            grafo[v1][v2] = a
            grafo[v2][v1] = a
        fim2 = timeit.default_timer()
        return (num_vertices, num_arestas, grafo, fim2 - inicio2)

    def definir_graus(self):
        # retorna o vertice com maior grau, o com menor grau, o grau medio do grafo e a ...
        # frequencia relativa de cada grau
        maior = [0, 0]
        menor = [0, 10000]
        soma = 0
        distribuicao = [0 for _ in range(self.num_vertices)]
        frequencia = []
        arquivo4 = open("frequencia_relativa.txt", 'w')
        for i in range(self.num_vertices):
            aux = 0
            for j in range(self.num_vertices):
                if self.grafo[i][j] != 0:
                    aux = aux + 1
            distribuicao[aux] = distribuicao[aux] + 1
            if maior[1] < aux:
                maior[0] = i
                maior[1] = aux
            elif menor[1] > aux:
                menor[0] = i
                menor[1] = aux
            soma = soma + aux
        for i in range(self.num_vertices):
            if distribuicao[i] != 0:
                frequencia.append((i, distribuicao[i] / self.num_vertices))
                st = str(i) + ':' + str(100 * distribuicao[i] / self.num_vertices) + '\n'
                arquivo4.write(st)
        arquivo4.close()
        media = float(soma)/float(self.num_vertices)
        return (maior, menor, media, frequencia)

    def busca_largura_matriz(self, s):
        # Escreve em um arquivo .txt saida o nivel de cada vertice na arvore, ...
        # considerando o caminho percorrido na busca em largura.
        inicio2 = timeit.default_timer()
        arquivo2 = open('nivel_largura.txt', 'w')
        desc = [0 for _ in range(len(self.grafo))]
        Q = [s]
        R = [s]
        desc[s] = 1
        ordem = [-1 for _ in range(len(self.grafo))]
        ordem[s] = 0
        while len(Q) != 0:
            u = Q.pop(0)
            for v in range(len(self.grafo[u])):
                if self.grafo[u][v] != 0 and desc[v] == 0:
                    Q.append(v)
                    R.append(v)
                    desc[v] = 1
                    if ordem[v] == -1:
                        ordem[v] = ordem[u] + 1
        for i in range(len(ordem)):
            if ordem[i] != -1:
                saidas = str(i) + ':' + str(ordem[i]) + '\n'
                arquivo2.write(saidas)
        arquivo2.close()
        fim2 = timeit.default_timer()
        return (fim2 - inicio2)

    def busca_profundidade_matriz(self, s):
        # Escreve em um arquivo .txt saida o nivel de cada vertice na arvore, ...
        # considerando o caminho percorrido na busca em profundidade
        inicio2 = timeit.default_timer()
        arquivo3 = open('nivel_profundidade.txt', 'w')
        desc = [0 for _ in range(len(self.grafo))]
        S = [s]
        R = [s]
        desc[s] = 1
        ordem = [-1 for _ in range(len(self.grafo))]
        ordem[s] = 0
        while len(S) != 0:
            u = S[-1]
            desempilhar = True
            for v in range(len(self.grafo[u])):
                if self.grafo[u][v] != 0 and desc[v] == 0:
                    desempilhar = False
                    S.append(v)
                    R.append(v)
                    desc[v] = 1
                    if ordem[v] == -1:
                        ordem[v] = ordem[u] + 1
                    break
            if desempilhar:
                S.pop()
        for i in range(len(ordem)):
            if ordem[i] != -1:
                saidas = str(i) + ':' + str(ordem[i]) + '\n'
                arquivo3.write(saidas)
        arquivo3.close()
        fim2 = timeit.default_timer()
        return (fim2 - inicio2)

    def busca_largura(self, comp, s):
        # busca comum em largura de um grafo G - matriz
        desc = [0 for _ in range(self.num_vertices)]
        Q = [s]
        R = [s]
        desc[s] = 1
        comp[s] = 0
        while len(Q) != 0:
            u = Q.pop(0)
            for v in range(self.num_vertices):
                if self.grafo[u][v] != 0 and desc[v] == 0:
                    Q.append(v)
                    R.append(v)
                    desc[v] = 1
                    comp[v] = 0
        return R

    def conexidade(self):
        # retorna o numero de componentes conexas no grafo, e o numero de vertices nessas componentes
        componente = [1 for _ in range(self.num_vertices)]
        t = []
        k = 0
        for i in range(len(self.grafo)):
            bit = 0
            if componente[i] != 0:
                busca = self.busca_largura(componente, i)
                t.append(len(busca))
                k = k + 1
            for j in range(self.num_vertices):
                if componente[j] == 0:
                    bit = bit + 1
                if bit == self.num_vertices:
                    return (k, t)
