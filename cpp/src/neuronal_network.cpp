
#include <functional>
#include <array>

#include "activation_function.hpp"

namespace neuronal_network {

    template<std::size_t INPUTS>
    class Neuron {
    private:
        std::function<double(double) > function;
        std::array<double, INPUTS> weights;
        double bias;

    public:

        Neuron(std::function<double(double) > function = activation_function::linear(1.0),
                std::array<double, INPUTS> weights = std::array<double, 1>({1.0}), double bias = 1.0) {
            this->function = function;
            this->weights = weights;
            this->bias = bias;
        }

        double compute(std::array<double, INPUTS> values) {
            double summed = -this->bias;
            for (int i = 0; i < this->weights.size() && i < values.size(); i++) {
                summed = summed + this->weights[i] * values[i];
            }
            return summed;
        }
    };

    Neuron<2> neuron_and() {
        std::array<double, 2> weights = {
            {1.0, 1.0}
        };
        return Neuron<2>(activation_function::threshold_unipolar(), weights, 1.5);
    }

    Neuron<2> neuron_or() {
        std::array<double, 2> weights = {
            {1.0, 1.0}
        };
        return Neuron<2>(activation_function::threshold_unipolar(), weights, 0.5);
    }

    Neuron<1> neuron_not() {
        std::array<double, 1> weights = {
            {-1.0}
        };
        return Neuron<1>(activation_function::threshold_unipolar(), weights, -0.5);
    }

    template<std::size_t NEURONS, std::size_t INPUTS>
    class Layer {
    private:
        std::array<Neuron<INPUTS>, NEURONS> neurons;

    public:

        Layer(std::array<Neuron<INPUTS>, NEURONS> neurons) {
            this->neurons = neurons;
        }

        std::array<double, NEURONS> compute(std::array<double, INPUTS> values) {
            std::array<double, NEURONS> results;
            for (int i = 0; i < this->neurons; i++) {
                results[i] = this->neurons[i].compute(values);
            }
            return results;
        }
    };

    template<std::size_t LAYERS, std::size_t NEURONS, std::size_t INPUTS>
    class Network {
    private:
        std::array<Layer<NEURONS, INPUTS>, LAYERS> layers;

    public:

        Network(std::array<Layer<NEURONS, INPUTS>, LAYERS> layers) {
            this->layers = layers;
        }
    };

}