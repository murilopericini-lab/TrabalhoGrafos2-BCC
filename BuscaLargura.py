from collections import deque

def criar_grafo():
    return {}

def inserir_vertice(grafo, v):
    if v not in grafo:
        grafo[v] = []

def inserir_aresta(grafo, origem, destino, nao_direcionado=True):
    inserir_vertice(grafo, origem)
    inserir_vertice(grafo, destino)
    
    if destino not in grafo[origem]:
        grafo[origem].append(destino)
        
    if nao_direcionado and origem not in grafo[destino]:
        grafo[destino].append(origem)

def exibir_grafo(grafo):
    if not grafo:
        print("\nO grafo está vazio.")
        return
    
    print("\n--- Estrutura do Grafo (Lista de Adjacência) ---")
    for v in sorted(grafo.keys()):
        print(f"Vértice {v} -> Vizinhos: {grafo[v]}")
    print("-")

def busca_em_largura(grafo, inicio):
    if inicio not in grafo:
        return []

    visitados = []
    fila = deque([inicio])
    
    while fila:
        vertice_atual = fila.popleft()
        
        if vertice_atual not in visitados:
            visitados.append(vertice_atual)
            
            for vizinho in grafo.get(vertice_atual, []):
                if vizinho not in visitados and vizinho not in fila:
                    fila.append(vizinho)
                    
    return visitados

def main():
    grafo = criar_grafo()
    
    while True:
        print("\n MENU (BUSCA EM LARGURA)")
        print("1. Exibir o Grafo")
        print("2. Inserir Vértice")
        print("3. Inserir Aresta")
        print("4. Executar Busca em Largura Padrão")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            exibir_grafo(grafo)
        elif opcao == '2':
            v = input("Digite o nome do vértice: ").strip()
            inserir_vertice(grafo, v)
            print(f"Vértice '{v}' inserido.")
        elif opcao == '3':
            origem = input("Vértice de origem: ").strip()
            destino = input("Vértice de destino: ").strip()
            nd_input = input("O grafo é não-direcionado? (s/n): ").strip().lower()
            nd = True if nd_input == 's' else False
            inserir_aresta(grafo, origem, destino, nao_direcionado=nd)
            print("Aresta inserida com sucesso.")
        elif opcao == '4':
            inicio = input("Digite o vértice inicial: ").strip()
            resultado = busca_em_largura(grafo, inicio)
            print(f"-> Ordem de visitação BFS: {resultado}")
        elif opcao == '0':
            print("Encerrando programa.")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()