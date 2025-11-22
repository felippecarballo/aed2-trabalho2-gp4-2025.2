# AED2 - Trabalho 2 - Grupo 4

# Algoritmo de Backtracking: Palavras em uma Matriz

Este trabalho foca na resolução do **Problema 5** do Trabalho 2, que consiste em determinar se uma palavra pode ser formada por letras adjacentes em uma matriz. O método escolhido para a resolução é o **Backtracking**.

## Funcionamento do Backtracking

O algoritmo explora todas as possíveis sequências de células adjacentes que correspondem aos caracteres de uma palavra, garantindo que cada célula seja usada apenas uma vez por palavra.

### Estratégia de Busca

A busca é implementada como uma **Busca em Profundidade (DFS | sigla em inglês para Depth-First Search). É um algoritmo para percorrer ou buscar nós em uma estrutura de dados de árvore ou grafo.

A principal característica do DFS é que ele explora o máximo possível ao longo de cada ramo antes de retroceder (backtrack). Ou seja, ele vai "fundo" em um caminho antes de explorar caminhos adjacentes.** recursiva, iniciada a partir de cada célula da matriz que corresponde ao primeiro caractere da palavra.

1.  **Exploração:** A função `busca_backtracking` é chamada recursivamente para a próxima letra da palavra em todas as **8 direções adjacentes** (horizontal, vertical e diagonal).
2.  **Marcação:** Antes de fazer uma chamada recursiva, a célula atual é temporariamente marcada com `#` (caractere `char_original` é armazenado) para indicar que já foi visitada nesse caminho de busca.
3.  **Backtracking (Restauração):** Se o caminho não levar à palavra completa, o valor da célula é restaurado (`matriz[linha][coluna] = char_original`). Essa restauração permite que outros caminhos subsequentes utilizem a mesma célula em suas próprias buscas.
4.  **Parada:** A busca é bem-sucedida quando todos os caracteres da palavra são encontrados (`indice == len(palavra)`).

### Implementação (Python)

A implementação do algoritmo consiste em:
* **`DIRECOES`**: Uma lista de tuplas que define os 8 movimentos possíveis na matriz.
* **`busca_backtracking`**: A função recursiva que realiza a DFS e o Backtracking.
* **`palavras_matriz`**: A função principal que itera sobre a lista de palavras, mede o tempo de execução e inicia a busca a partir de cada célula inicial.

## Complexidade

A complexidade é analisada em relação às dimensões da matriz ($M \times N$) e ao comprimento da palavra ($L$).

### Função de Busca

T(M, N, L) = M \cdot N \cdot O(8^L)

* **Complexidade de Tempo (Pior Caso):** O(M \cdot N \cdot 8^L)
    * O fator M \cdot N vem de iniciar a DFS em cada célula da matriz.
    * O fator 8^L reflete o número de possíveis caminhos de comprimento L, pois, no pior caso, há até 8 ramificações em cada passo da recursão.
* **Complexidade de Espaço (Pior Caso):** O(L + M \cdot N)
    * O(L) para a profundidade da pilha de chamadas recursivas (que é limitada pelo comprimento da palavra).
    * O(M \cdot N) para a cópia da matriz usada para preservar o estado em cada nova busca.

*Onde M e N são as dimensões da matriz, e L é o comprimento da palavra a ser encontrada.*

## Execução e Resultados

A medição de tempo é feita em **milissegundos (ms)**.

### Como Executar

O script foi projetado para ser executado diretamente, sem a necessidade de argumentos de linha de comando. Os valores de entrada são definidos no próprio código.

Configure a Entrada: Abra o arquivo Python e altere os valores das variáveis moedas e troco conforme desejado.

**Matriz de Exemplo:**
1.  *Configure a Entrada:*

Os valores da matriz e das palavras a serem buscadas são definidos diretamente no bloco de teste do código Python.
 Abra o arquivo Python e certifique-se de que os valores das variáveis **`matriz_exemplo`** e **`palavras_para_buscar`** estejam configurados corretamente
```
# Variáveis definidas no código:
matriz_exemplo = [
    ['C', 'A', 'N', 'D', 'O'],
    ['E', 'G', 'U', 'N', 'A'],
    ['L', 'A', 'M', 'O', 'S'],
    ['P', 'O', 'I', 'R', 'T']
]

palavras_para_buscar = ["CANTO", "LAGO", "DIREITA", "SIM", "AMOR", "CASA"]
```
2.  *Execute o script*

Abra um terminal na pasta do projeto e execute o seguinte comando:
```
python Questao_5.py
```
### Saída de Exemplo
A execução do script produzirá a seguinte saída no console:
```
========== Programa Word Search ==========
Matriz de exemplo: [['C', 'A', 'N', 'D', 'O'], ['E', 'G', 'U', 'N', 'A'], ['L', 'A', 'M', 'O', 'S'], ['P', 'O', 'I', 'R', 'T']]
Palavras a buscar: ['CANTO', 'LAGO', 'DIREITA', 'SIM', 'AMOR', 'CASA']
-------------------------------------------

Palavra: 'CANTO'
  Encontrada? Não
  Tempo de Execução: 0.019073 milissegundos
-------------------------------------------
Palavra: 'LAGO'
  Encontrada? Não
  Tempo de Execução: 0.016451 milissegundos
-------------------------------------------
Palavra: 'DIREITA'
  Encontrada? Não
  Tempo de Execução: 0.005007 milissegundos
-------------------------------------------
Palavra: 'SIM'
  Encontrada? Não
  Tempo de Execução: 0.004530 milissegundos
-------------------------------------------
Palavra: 'AMOR'
  Encontrada? Sim
  Tempo de Execução: 0.009298 milissegundos
-------------------------------------------
Palavra: 'CASA'
  Encontrada? Não
  Tempo de Execução: 0.006437 milissegundos
-------------------------------------------
```

# Autores

* *João Luiz Schiavini Filho*
* *Felippe Carballo Leal*
