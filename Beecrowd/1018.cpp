#include <iostream>

int main(int argc, char const *argv[])
{
    int n, cem = 0, cinquenta = 0, vinte = 0, dez = 0, cinco = 0, dois = 0, um = 0;

    std::cin >> n;
    int n_perm = n;

    for (int i = 0; n != 0; i ++) {
        if (n >= 100) {
            cem = n/100;
            n = n%100;
        } else if (n >= 50) {
            cinquenta = n/50;
            n = n%50;
        } else if (n >= 20) {
            vinte = n/20;
            n = n%20;
        } else if (n >= 10) {
            dez = n/10;
            n = n%10;
        } else if (n >= 5) {
            cinco = n/5;
            n = n%5;
        } else if (n >= 2) {
            dois = n/2;
            n = n%2;
        } else if (n >= 1) {
            n = 0;
            um ++;
        }
    }

    std::cout << n_perm << std::endl;
    std::cout << cem << " nota(s) de R$ 100,00" << std::endl;
    std::cout << cinquenta << " nota(s) de R$ 50,00" << std::endl;
    std::cout << vinte << " nota(s) de R$ 20,00" << std::endl;
    std::cout << dez << " nota(s) de R$ 10,00" << std::endl;
    std::cout << cinco << " nota(s) de R$ 5,00" << std::endl;
    std::cout << dois << " nota(s) de R$ 2,00" << std::endl;
    std::cout << um << " nota(s) de R$ 1,00" << std::endl;
}
