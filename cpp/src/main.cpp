
#include <functional>
#include <array>

#include <cstdlib>
#include <iostream>

#include "neuronal_network.hpp"
#include "activation_function.hpp"

using namespace std;

int main(int argc, char** argv) {
    for (neuronal_network::Neuron<2> neuron :{neuronal_network::neuron_and(), neuronal_network::neuron_or()}) {
        std::array<std::array<double, 2>, 4> values = {
            {
                {
                    {0.0, 0.0}
                },
                {
                    {1.0, 0.0}
                },
                {
                    {0.0, 1.0}
                },
                {
                    {1.0, 1.0}
                }
            }};
        for (std::array<double, 2> value : values) {
            std::cout << neuron.compute(value) << endl;
        }
    }
    return 0;
}

