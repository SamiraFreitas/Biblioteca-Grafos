

class Grafo_Lista:
    def __init__(self, arquivo):
        (self.num_vertices, self.num_arestas) = self.tamanhos(arquivo)
        self.grafo = self.converte_lista(arquivo)
        (self.maior_grau, self.menor_grau, self.media_grau, self.frequencia) = self.definir_graus()
        self.busca_largura_lista(0)
        self.busca_profundidade_lista(0)
        (self.componentes_conexas, self.num_conexa) = self.conexidade()

    def converte_lista(self, arquivo):
        "Converte o grafo do arquivo .dat em uma lista de adjacencias"
        lista = []
        for i in range(self.num_vertices):
            lista.append([])

        for linha in arquivo:
            conteudo = linha.split(' ')
            v1 = int(conteudo[0])
            v2 = int(conteudo[1])
            a = int(conteudo[2])
            lista[v1].append((v2, a))
            lista[v2].append((v1, a))
        return lista

    def tamanhos(self, arquivo):
        "retorna o numero de vertices e arestas no grafo"
        for linha in arquivo:
            conteudo = linha.split(' ')
            return (int(conteudo[0]), int(conteudo[1]))

    def definir_graus(self):
        "calcula o vertice com maior grau, o com menor grau, o grau medio do grafo"
        maior = [0, 0]
        menor = [0, 10000]
        soma = 0
        distribuicao = [0 for k in range(self.num_vertices)]
        frequencia = []

        for i in range(self.num_vertices):
            aux = 0
            distribuicao[len(self.grafo[i])] = distribuicao[len(self.grafo[i])] + 1
            if maior[1] < len(self.grafo[i]):
                maior[0] = i
                maior[1] = len(self.grafo[i])
            elif menor[1] > len(self.grafo[i]):
                menor[0] = i
                menor[1] = len(self.grafo[i])
            soma = soma + len(self.grafo[i])
        for i in range(self.num_vertices):
            if distribuicao[i] != 0:
                frequencia.append((i, distribuicao[i] / self.num_vertices))
        media = float(soma) / float(5)
        return (maior, menor, media, frequencia)

    def busca_largura_lista(self, s):
        "Escreve em um arquivo .txt saida o nivel de cada vertice na arvore, ..."
        "... considerando o caminho percorrido na busca em largura."
        arquivo2 = open('nivel_largura.txt', 'w')
        desc = [0 for i in range(self.num_vertices)]
        Q = [s]
        R = [s]
        desc[s] = 1
        ordem = [-1 for i in range(self.num_vertices)]
        ordem[s] = 0

        while len(Q) != 0:
            u = Q.pop(0)
            for (v, a) in self.grafo[u]:
                if desc[v] == 0:
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

    def busca_profundidade_lista(self, s):
        "Escreve em um arquivo .txt saida o nivel de cada vertice na arvore, ..."
        "considerando o caminho percorrido na busca em profundidade"
        arquivo3 = open('nivel_profundidade.txt', 'w')
        desc = [0 for i in range(self.num_vertices)]
        S = [s]
        R = [s]
        desc[s] = 1
        ordem = [-1 for i in range(self.num_vertices)]
        ordem[s] = 0
        while len(S) != 0:
            u = S[-1]
            desempilhar = True
            for (v, a) in self.grafo[u]:
                if desc[v] == 0:
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

    def busca_largura(self, comp, s):
        "busca em largura de um grafo G"
        desc = [0 for i in range(self.num_vertices)]
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
                    comp[v] = 0
        return R

    def conexidade(self):
        "retorna o numero de componentes conexas no grafo, e o numero de vertices nessas componentes"
        componente = [1 for i in range(self.num_vertices)]
        t = []
        k = 0
        for i in range(self.num_vertices):
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






