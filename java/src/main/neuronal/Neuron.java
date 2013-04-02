package main.neuronal;

import main.Compute;
import main.activation.ActivationFunction;

public abstract class Neuron implements Compute<double[], Double> {

    protected final ActivationFunction activationFunction;

    protected final double bias;

    protected final double[] weights;

    public Neuron(ActivationFunction activationFunction, double[] weights, double bias) {
        this.activationFunction = activationFunction;
        this.bias = bias;
        this.weights = weights;
    }

    private static class SimpleNeuron extends Neuron {

        public SimpleNeuron(ActivationFunction activationFunction, double[] weights, double bias) {
            super(activationFunction, weights, bias);
        }

        @Override
        public Double compute(double[] values) {
            if (values == null) {
                throw new NullPointerException();
            }
            if (values.length != weights.length) {
                throw new IllegalArgumentException("Lengths: " + values.length + " != " + weights.length);
            }

            double result = -bias;
            for (int index = 0; index < weights.length; index++) {
                result = result + values[index] * weights[index];
            }

            return activationFunction.compute(result);
        }
    }

    public static Neuron getNeuronAnd() {
        return new SimpleNeuron(new ActivationFunction.ThresholdUnipolar(), new double[]{1.0, 1.0}, 1.5);
    }

    public static Neuron getNeuronOr() {
        return new SimpleNeuron(new ActivationFunction.ThresholdUnipolar(), new double[]{1.0, 1.0}, 0.5);
    }

    public static Neuron getNeuronNot() {
        return new SimpleNeuron(new ActivationFunction.ThresholdUnipolar(), new double[]{-1.0}, -0.5);
    }

}
