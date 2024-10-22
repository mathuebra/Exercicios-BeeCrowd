#include <iostream>
#include <vector>
#include <list>
#include <unordered_map>

class Grafo {
    public:
        Grafo(int vertices);
        void adicionarAresta(int v1, int v2);
        void printGrafo();

    private:
        int vertices;
        std::vector<std::list<int>> adjList;
};

Grafo::Grafo(int vertices) {
    this->vertices = vertices;
    adjList.resize(vertices);
}

void Grafo::adicionarAresta(int v1, int v2) {
    adjList[v1].push_back(v2);
    adjList[v2].push_back(v1);
}

void Grafo::printGrafo() {
    for (int i = 0; i < vertices; i++) {
        std::cout << i << " -> ";
        for (int j : adjList[i]) {
            std::cout << j << " ";
        }
        std::cout << std::endl;
    }
}

int main(int argc, char const *argv[])
{
    Grafo g(5);

    g.adicionarAresta(0, 1);
    g.adicionarAresta(0, 4);
    g.adicionarAresta(1, 2);
    g.adicionarAresta(1, 3);
    g.adicionarAresta(1, 4);
    g.adicionarAresta(2, 3);
    g.adicionarAresta(3, 4);

    g.printGrafo();

    return 0;
}
