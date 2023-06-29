class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, vertice):
        self.vertices[vertice] = {}

    def adicionar_aresta(self, origem, destino, distancia):
        if origem not in self.vertices:
            self.adicionar_vertice(origem)
        if destino not in self.vertices:
            self.adicionar_vertice(destino)

        self.vertices[origem][destino] = distancia
        self.vertices[destino][origem] = distancia

    def encontrar_vertice_menor_distancia(self, distancias, visitados):
        min_distancia = float('inf')
        vertice_menor_distancia = None
        for vertice in self.vertices:
            if distancias[vertice] < min_distancia and not visitados[vertice]:
                min_distancia = distancias[vertice]
                vertice_menor_distancia = vertice
        return vertice_menor_distancia

    def dijkstra(self, vertice_origem):
        distancias = {vertice: float('inf') for vertice in self.vertices}
        distancias[vertice_origem] = 0
        visitados = {vertice: False for vertice in self.vertices}

        for _ in range(len(self.vertices)):
            vertice_atual = self.encontrar_vertice_menor_distancia(distancias, visitados)
            visitados[vertice_atual] = True
            for vertice_adjacente, distancia in self.vertices[vertice_atual].items():
                nova_distancia = distancias[vertice_atual] + distancia
                if nova_distancia < distancias[vertice_adjacente]:
                    distancias[vertice_adjacente] = nova_distancia 

        return distancias


# Criando o grafo e adicionando vértices e arestas
grafo = Grafo()

grafo.adicionar_vertice(0)  # Criciuma
grafo.adicionar_vertice(1)  # Içara
grafo.adicionar_vertice(2)  # Forquilhinha
grafo.adicionar_vertice(3)  # Sideropolis
grafo.adicionar_vertice(4)  # Cocal do Sul
grafo.adicionar_vertice(5)  # Nova Veneza
grafo.adicionar_vertice(6)  # Urussanga
grafo.adicionar_vertice(7)  # Balneario Rincão
grafo.adicionar_vertice(8)  # Morro da Fumaça


matriz_adjacencia = [
    [0, 4, 8, 0, 0, 0, 0, 0, 0],  # Criciuma (ponto 0)
    [4, 0, 11, 0, 0, 0, 0, 0, 0],  # Içara 
    [8, 11, 0, 7, 1, 0, 0, 0, 0],  # Forquilhinha
    [0, 8, 0, 0, 2, 0, 4, 0, 0],   # Sideropolis 
    [0, 0, 7, 2, 0, 6, 0, 0, 0],  # Cocal do Sul 
    [0, 0, 1, 0, 6, 0, 0, 2, 0],  # Nova Veneza
    [0, 0, 0, 7, 0, 0, 0, 14, 9],  # Urussanga 
    [0, 0, 0, 4, 0, 2, 14, 0, 10],  # Balneario Rincão 
    [0, 0, 0, 0, 0, 0, 9, 10, 0],  # Morro da Fumaça 
]

for i in range(len(matriz_adjacencia)):
    for j in range(len(matriz_adjacencia[i])):
        if matriz_adjacencia[i][j] != 0:
            grafo.adicionar_aresta(i, j, matriz_adjacencia[i][j])

distancias = grafo.dijkstra(0)  # 'Criciuma' corresponde ao ponto 0

for vertice, distancia in distancias.items():
    print(f'Distância mínima de Criciuma até {vertice}: {distancia}')
