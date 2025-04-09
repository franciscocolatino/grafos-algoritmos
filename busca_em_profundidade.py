class Pilha:
    def __init__(self) -> None:
        self._itens: list[str] = []
    
    def push(self, item: str) -> None:
        """Adiciona um item no topo da pilha"""
        self._itens.append(item)
    
    def pop(self) -> str:
        """Remove e retorna o item do topo da pilha"""
        if not self.is_empty():
            return self._itens.pop()
        raise IndexError("A pilha está vazia")
    
    def is_empty(self) -> bool:
        """Verifica se a pilha está vazia"""
        return len(self._itens) == 0
    
    def __len__(self) -> int:
        """Retorna o tamanho da pilha"""
        return len(self._itens)


grafo: dict[str, list[str]] = {
    '0': ['1', '3', '8'],
    '1': ['0', '7'],
    '2': ['3', '5', '7'],
    '3': ['0', '2', '4'],
    '4': ['3', '8'],
    '5': ['2', '6'],
    '6': ['5'],
    '7': ['1', '2'],
    '8': ['0', '4']
}

def busca_em_profundidade(grafo: dict[str, list[str]], vertice_inicial: str, vertice_final: str) -> bool:
  pilha = Pilha()
  visitados = set[str]()
  pilha.push(vertice_inicial)

  while not pilha.is_empty():
      vertice_atual = pilha.pop()

      if vertice_atual == vertice_final:
          return True

      if vertice_atual not in visitados:
          visitados.add(vertice_atual)
          print(f"VISITADOS QUANDO O VERTICE ATUAL É {vertice_atual}: {visitados}")

          for vizinho in grafo[vertice_atual]:
              if vizinho not in visitados:
                  pilha.push(vizinho)
          print('Estrutura da pilha')
          print(pilha._itens)
        
  return False

resultado = busca_em_profundidade(grafo, '0', '6')
print("Caminho encontrado:", resultado)