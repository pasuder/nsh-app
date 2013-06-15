__author__ = 'paoolo'


def compute_error_on_neuron(neuron, error):
    return map(lambda weight: weight * error, neuron.weights)


def compute_error_on_layer(layer, errors):
    # compute error on each neuron in layer and get sequence of sequence
    errors = map(lambda val: compute_error_on_neuron(val[0], val[1]), zip(layer.neurons, errors))
    if len(errors) > 0:
        # transpose matrix
        seq = [[] for _ in xrange(len(errors[0]))]
        for error in errors:
            for val in zip(seq, error):
                val[0].append(val[1])
        # return reduced vector of errors per neuron
        return map(lambda e: reduce(lambda acc, val: acc + val, e), seq)


def compute_error_on_network(network, values, targets):
    values = network.compute(values)
    errors = map(lambda val: (val[0] - val[1]), zip(targets, values))

    all_errors = [errors]
    for layer in network.layers[::-1]:
        errors = compute_error_on_layer(layer, errors)
        all_errors.append(errors)

    return all_errors