import time


class GrafoLista:
    # Classe com todos os atributos do grafo na representação lista de adjacencias
    def __init__(self, arquivo):
        inicio = time.perf_counter()
        (self.num_vertices, self.num_arestas, self.grafo, self.tempo_cria_representacao) = self.converte_lista(arquivo)
        (self.maior_grau, self.menor_grau, self.media_grau, self.distribuicao) = self.definir_graus()
        self.tempo_largura = self.busca_largura_lista(0)
        self.tempo_profundidade = self.busca_profundidade_lista(0)
        (self.componentes_conexas, self.num_conexa) = self.conexidade()
        fim = time.perf_counter()
        self.tempo_total = fim - inicio

    def converte_lista(self, arquivo):
        # Converte o grafo do arquivo .dat em uma lista de adjacencias e lê o numero de vertices e arestas no grafo"
        inicio1 = time.perf_counter()
        linha = arquivo.readline()
        conteudo = linha.split(' ')  # divide a linha, interpretando ' ' como o fim de uma informação, uma quebra
        num_vertices = int(conteudo[0])
        num_arestas = int(conteudo[1])
        grafo = [[] for _ in range(num_vertices)]
        for linha in arquivo:       # adiciona as posição V1 e V2 da lista a conexão
            conteudo = linha.split(' ')
            v1 = int(conteudo[0])
            v2 = int(conteudo[1])
            a = int(conteudo[2])
            grafo[v1].append((v2, a))
            grafo[v2].append((v1, a))
        fim1 = time.perf_counter()
        return (num_vertices, num_arestas, grafo, fim1 - inicio1)

    def definir_graus(self):
        # retorna o vertice com maior grau, o com menor grau, o grau medio do grafo e a ...
        # distribuicao relativa de cada grau
        maior = [0, 0]
        menor = [0, self.num_vertices]
        soma = 0
        frequencia = [0 for _ in range(self.num_vertices)]
        distribuicao = []
        arquivo4 = open("distribuicao_relativa.txt", 'w')
        for i in range(self.num_vertices):
            frequencia[len(self.grafo[i])] = frequencia[len(self.grafo[i])] + 1
            # frequencia - cada posição é um grau e nela guarda se o seu nº de repetições
            if maior[1] < len(self.grafo[i]):
                maior[0] = i
                maior[1] = len(self.grafo[i])
            elif menor[1] > len(self.grafo[i]):
                menor[0] = i
                menor[1] = len(self.grafo[i])
            soma = soma + len(self.grafo[i])     # soma de todos os graus encontrados
        for i in range(self.num_vertices):
            if frequencia[i] != 0:
                # guarda o grau existente e sua distribuição relativa em uma lista
                distribuicao.append((i, frequencia[i] / self.num_vertices))
                st = str(i) + ':' + str(100 * frequencia[i] / self.num_vertices) + '\n'
                # escreve o vertice e sua % da distribuicao em um arquivo de saida .txt
                arquivo4.write(st)
        arquivo4.close()
        media = float(soma) / float(self.num_vertices)   # media de graus
        return (maior, menor, media, distribuicao)

    def busca_largura_lista(self, s):
        # Escreve em um arquivo .txt o nivel de cada vertice na arvore, ...
        # considerando o caminho percorrido na busca em largura.
        inicio2 = time.perf_counter()
        arquivo2 = open('nivel_largura.txt', 'w')
        desc = [0 for _ in range(self.num_vertices)]
        Q = [s]
        R = [s]
        desc[s] = 1
        ordem = [-1 for _ in range(self.num_vertices)]   # considerando todos os vertices com altura = -1, altura nula
        ordem[s] = 0     # vertice s tem altura 0
        while len(Q) != 0:
            u = Q.pop(0)
            for (v, a) in self.grafo[u]:
                if desc[v] == 0:
                    Q.append(v)
                    R.append(v)
                    desc[v] = 1
                    ordem[v] = ordem[u] + 1  # altura de v  = altura do seu vertice anterior u + 1
        for i in range(len(ordem)):
            if ordem[i] != -1:   # vertice com altura -1 não foram encontrados
                saidas = str(i) + ':' + str(ordem[i]) + '\n'
                # escreve a string = "vertice : altura do vertice" em um arquivo de saida .txt
                arquivo2.write(saidas)
        arquivo2.close()
        fim2 = time.perf_counter()
        return (fim2 - inicio2)

    def busca_profundidade_lista(self, s):
        # Escreve em um arquivo .txt o nivel de cada vertice na arvore, ...
        # considerando o caminho percorrido na busca em profundidade
        inicio3 = time.perf_counter()
        arquivo3 = open('nivel_profundidade.txt', 'w')
        desc = [0 for _ in range(self.num_vertices)]
        S = [s]
        R = [s]
        desc[s] = 1
        ordem = [-1 for _ in range(self.num_vertices)]   # considerando todos os vertices com altura = -1, altura nula
        ordem[s] = 0     # vertice s tem altura 0
        while len(S) != 0:
            u = S[-1]
            desempilhar = True
            for (v, a) in self.grafo[u]:
                if desc[v] == 0:
                    desempilhar = False
                    S.append(v)
                    R.append(v)
                    desc[v] = 1
                    ordem[v] = ordem[u] + 1
                    break
            if desempilhar:
                S.pop()
        for i in range(len(ordem)):
            if ordem[i] != -1:   # vertice com altura -1 não foram encontrados
                saidas = str(i) + ':' + str(ordem[i]) + '\n'
                # escreve a string = "vertice : altura do vertice" em um arquivo de saida .txt
                arquivo3.write(saidas)
        arquivo3.close()
        fim3 = time.perf_counter()
        return (fim3 - inicio3)

    def busca_largura(self, comp, s):
        # busca simples em largura de um grafo G - lista
        desc = [0 for _ in range(self.num_vertices)]
        Q = [s]
        R = [s]
        desc[s] = 1
        comp[s] = 0
        while len(Q) != 0:
            u = Q.pop(0)
            for (v, a) in self.grafo[u]:
                if desc[v] == 0:
                    Q.append(v)
                    R.append(v)
                    desc[v] = 1
                    comp[v] = 1  # componente foi encontrada e setada
        return R

    def conexidade(self):
        # retorna o numero de componentes conexas no grafo, e o numero de vertices nessas componentes
        componente = [0 for _ in range(self.num_vertices)]  # 0 para componente ainda não encontrada
        t = []   # salva tamanho de componentes conexas encontradas
        quant = 0    # quantidade de componentes conexas
        cont = 0   # contador do numero de vertices ja encontrados
        for i in range(self.num_vertices):
            if componente[i] != 1:   # testa se ele ja não foi descoberto em alguma busca
                busca = self.busca_largura(componente, i)    # busca em largura no grafo, componente é passado e
                # modificado dentro da função de busca, vertices encontrados em uma busca não são mais testados
                t.append(len(busca))
                quant = quant + 1
                cont = cont + len(busca)
            if cont == self.num_vertices:
                return (quant, t)
