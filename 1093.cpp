#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

float calculateProbability(int dice) {
    return (float) dice/6;
}

int main() {
    //int ev1 = 1, ev2 = 1, at = 3, d = 1;
    int ev1, ev2, at, d;
    float probability = 1;
    cin >> ev1 >> ev2 >> at >> d;

    while (ev2>0) {
        probability *= calculateProbability(at);
        ev2 -= d;
    }

    cout << fixed << setprecision(1) << probability * 100;
}