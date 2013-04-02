package main.neuronal;

import main.Compute;

import java.util.Collection;
import java.util.Collections;

public final class Network implements Compute<double[], double[]> {

    private final Collection<Layer> layers;

    public Network(Collection<Layer> layers) {
        this.layers = Collections.unmodifiableCollection(layers);
    }

    @Override
    public double[] compute(double[] values) {
        for (Layer layer : layers) {
            values = layer.compute(values);
        }
        return values;
    }
}
