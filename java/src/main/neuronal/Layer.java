package main.neuronal;

import main.Compute;

import java.util.Collection;
import java.util.Collections;

public final class Layer implements Compute<double[], double[]> {

    private final Collection<Neuron> neurons;

    public Layer(Collection<Neuron> neurons) {
        this.neurons = Collections.unmodifiableCollection(neurons);
    }

    @Override
    public double[] compute(double[] values) {
        int index = 0;
        double[] results = new double[neurons.size()];
        for (Neuron neuron : neurons) {
            results[index++] = neuron.compute(values);
        }

        return results;
    }
}
