import time
from typing import List, Tuple, Dict

DIRECOES = [
    (0, 1), (0, -1), (1, 0), (-1, 0),
    (1, 1), (1, -1), (-1, 1), (-1, -1)
]

def busca_backtracking(
    matriz: List[List[str]],
    palavra: str,
    linha: int,
    coluna: int,
    indice: int
) -> bool:
    
    if indice == len(palavra):
        return True
    
    if (linha < 0 or linha >= len(matriz) or
        coluna < 0 or coluna >= len(matriz[0]) or
        matriz[linha][coluna] != palavra[indice] or
        matriz[linha][coluna] == '#'):
        return False
    
    char_original = matriz[linha][coluna]
    matriz[linha][coluna] = '#'
    
    encontrado = False
    for dr, dc in DIRECOES:
        if busca_backtracking(matriz, palavra, linha + dr, coluna + dc, indice + 1):
            encontrado = True
            break

    matriz[linha][coluna] = char_original
    
    return encontrado


def palavras_matriz(matriz: List[List[str]], palavras: List[str]) -> Dict[str, Tuple[bool, float]]:
    
    resultados = {}
    
    for palavra in palavras:
        if not palavra:
            resultados[palavra] = (False, 0.0)
            continue
            
        start_time = time.time()
        
        M = len(matriz)
        N = len(matriz[0]) if M > 0 else 0
        encontrado = False
        
        for i in range(M):
            for j in range(N):
                if matriz[i][j] == palavra[0]:
                    matriz_copia = [lin[:] for lin in matriz]
                    if busca_backtracking(matriz_copia, palavra, i, j, 0):
                        encontrado = True
                        break
            if encontrado:
                break
                
        end_time = time.time()
        tempo_execucao = (end_time - start_time) * 1000
        
        resultados[palavra] = (encontrado, tempo_execucao)
        
    return resultados

#Main
matriz_exemplo = [
    ['C', 'A', 'N', 'D', 'O'],
    ['E', 'G', 'U', 'N', 'A'],
    ['L', 'A', 'M', 'O', 'S'],
    ['P', 'O', 'I', 'R', 'T']
]

palavras_para_buscar = ["CANTO", "LAGO", "DIREITA", "SIM", "AMOR", "CASA",]

print("========== Programa Word Search ==========")
print(f"Matriz de exemplo: {matriz_exemplo}")
print(f"Palavras a buscar: {palavras_para_buscar}")
print("-------------------------------------------\n")

resultados_finais = palavras_matriz(matriz_exemplo, palavras_para_buscar) 

for palavra, (encontrado, tempo) in resultados_finais.items():
    print(f"Palavra: '{palavra}'")
    if encontrado == False:
        print(f"  Encontrada? Não")
    else:
        print(f"  Encontrada? Sim")
    print(f"  Tempo de Execução: {tempo:.6f} milissegundos")
    print("-------------------------------------------")