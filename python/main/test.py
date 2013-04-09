from main import neuronal_network, activation_function

__author__ = 'paoolo'


def neuron_and():
    return neuronal_network.Neuron(activation_function.threshold_unipolar(), [2.8147, 1.9058], 3.7460)


def neuron_xor():
    hidden_neuron1 = neuronal_network.Neuron(activation_function.sigmoid_bipolar(), [0.7827, 0.7725], 0.3666)
    hidden_neuron2 = neuronal_network.Neuron(activation_function.sigmoid_bipolar(), [1.4412, 1.3907], -1.5368)
    hidden_layer = neuronal_network.Layer([hidden_neuron1, hidden_neuron2])
    output_neuron = neuronal_network.Neuron(activation_function.linear(), [-1.2556, 1.3087], 0.8297)
    output_layer = neuronal_network.Layer([output_neuron])
    return neuronal_network.Network([hidden_layer, output_layer])


def quick_test():
    neurons = [neuronal_network.neuron_and(), neuronal_network.neuron_or(), neuron_and(), neuron_xor()]
    for neuron in neurons:
        print neuron
        for val in [(0., 0.), (1., 0.), (0., 1.), (1., 1.)]:
            print '\t' + str(neuron.compute(val))
    neuron = neuronal_network.neuron_not()
    print neuron
    for val in [0, 1]:
        print '\t' + str(neuron.compute([val]))
