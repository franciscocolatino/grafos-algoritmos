class Fila:
    def __init__(self) -> None:
        self._itens: list[str] = []

    def enqueue(self, item: str) -> None:
        """Adiciona um item ao final da fila"""
        self._itens.append(item)

    def dequeue(self) -> str:
        """Remove e retorna o item do início da fila"""
        if not self.is_empty():
            return self._itens.pop(0)
        raise IndexError("A fila está vazia")

    def peek(self) -> str:
        """Retorna o item do início sem remover"""
        if not self.is_empty():
            return self._itens[0]
        raise IndexError("A fila está vazia")

    def is_empty(self) -> bool:
        """Verifica se a fila está vazia"""
        return len(self._itens) == 0

    def __len__(self) -> int:
        """Retorna o tamanho da fila"""
        return len(self._itens)

grafo: dict[str, list[str]] = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['H'],
    'D': [],
    'E': [],
    'F': ['G'],
    'G': [],
    'H': []
}

def busca_em_largura(grafo: dict[str, list[str]], vertice_inicial: str, vertice_final: str) -> bool:
  fila = Fila()
  visitados = set[str]()
  fila.enqueue(vertice_inicial)

  while not fila.is_empty():
    vertice_atual = fila.dequeue()

    if vertice_atual == vertice_final:
      return True

    if vertice_atual not in visitados:
      visitados.add(vertice_atual)
      print(f"VISITADOS QUANDO O VERTICE ATUAL É {vertice_atual}: {visitados}")

      for vizinho in grafo[vertice_atual]:
        if vizinho not in visitados:
          fila.enqueue(vizinho)
      print('Estrutura da fila')
      print(fila._itens)
    
  return False


resultado = busca_em_largura(grafo, 'A', 'G')
print("Caminho encontrado:", resultado)
