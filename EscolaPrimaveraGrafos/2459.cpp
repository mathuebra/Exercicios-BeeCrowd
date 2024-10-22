#include <iostream>
#include <vector>
#include <list>
#include <tuple>

class Grafo{
    public:
        Grafo(int vertices);
        void adicionaAresta(int v1, int v2, int peso, bool rodovia);
        void printGrafo();
    
    private:
        int vertices;
        std::vector<std::list<std::tuple<int, int, bool>>> adjList;
};

Grafo::Grafo(int vertices){
    this->vertices = vertices;
    adjList.resize(vertices);
}

void Grafo::adicionaAresta(int v1, int v2, int peso, bool rodovia){
    adjList[v1].push_back(std::make_tuple(v2, peso, rodovia));
    adjList[v2].push_back(std::make_tuple(v1, peso, rodovia));
}

void Grafo::printGrafo(){
    for(int i = 0; i < vertices; i++){
        std::cout << i << " -> ";
        for(auto j : adjList[i]){
            std::cout << "(" << std::get<0>(j) << ", " << std::get<1>(j) << ", " << (std::get<2>(j) ? "true" : "false") << ") ";
        }
        std::cout << std::endl;
    }
}

int main(int argc, char const *argv[])
{
    Grafo g(5);

    g.adicionaAresta(0, 1, 10, true);
    g.adicionaAresta(0, 4, 20, false);
    g.adicionaAresta(1, 2, 30, true);
    g.adicionaAresta(1, 3, 40, false);
    g.adicionaAresta(1, 4, 50, true);
    g.adicionaAresta(2, 3, 60, false);
    g.adicionaAresta(3, 4, 70, true);

    g.printGrafo();

    return 0;
}
