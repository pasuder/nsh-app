
#ifndef NEURONAL_NETWORK_HPP
#define	NEURONAL_NETWORK_HPP

#include <functional>
#include <array>

namespace neuronal_network {

    template<std::size_t INPUTS>
    class Neuron {
    public:
        Neuron(std::function<double(double) > function, std::array<double, INPUTS> weights, double bias);

        double compute(std::array<double, INPUTS> values);
    };

    Neuron<2> neuron_and();

    Neuron<2> neuron_or();

    Neuron<1> neuron_not();

    template<std::size_t NEURONS, std::size_t INPUTS>
    class Layer {
    public:
        Layer(std::array<Neuron<INPUTS>, NEURONS> neurons);

        std::array<double, NEURONS> compute(std::array<double, INPUTS> values_sequence);
    };

    template<std::size_t LAYERS, std::size_t NEURONS, std::size_t INPUTS>
    class Network {
    public:
        Network(std::array<Layer<NEURONS, INPUTS>, LAYERS> layers);
    };
}

#endif	/* NEURONAL_NETWORK_HPP */

