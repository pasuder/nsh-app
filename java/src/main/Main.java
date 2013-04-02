package main;

import main.neuronal.Neuron;

public class Main {

    public static void main(String[] args) {
        for (Neuron neuron : new Neuron[]{Neuron.getNeuronAnd(), Neuron.getNeuronOr()}) {
            for (double[] values : new double[][]{new double[]{0.0, 0.0}, new double[]{0.0, 1.0}, new double[]{1.0, 0.0}, new double[]{1.0, 1.0}}) {
                System.out.println(neuron.compute(values));
            }
        }
        Neuron neuron = Neuron.getNeuronNot();
        for (double value : new double[]{0.0, 1.0}) {
            System.out.println(neuron.compute(new double[]{value}));
        }
    }
}
