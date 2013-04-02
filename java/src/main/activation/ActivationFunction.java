package main.activation;

import main.Compute;

public interface ActivationFunction extends Compute<Double, Double> {

    public static class Linear implements ActivationFunction {

        private final double a, b;

        public Linear(double a, double b) {
            this.a = a;
            this.b = b;
        }

        public Linear(double a) {
            this(a, 0.0);
        }

        @Override
        public Double compute(Double x) {
            return a * x + b;
        }
    }

    public static class LinearCut implements ActivationFunction {

        @Override
        public Double compute(Double x) {
            return (x < -1.0 ? 1.0 : (x > 1.0 ? 1.0 : x));
        }
    }

    public static class ThresholdUnipolar implements ActivationFunction {

        private final double a;

        public ThresholdUnipolar(double a) {
            this.a = a;
        }

        public ThresholdUnipolar() {
            this(0.0);
        }

        @Override
        public Double compute(Double x) {
            return (x < a ? 0.0 : 1.0);
        }
    }

    public static class ThresholdBipolar implements ActivationFunction {

        private final double a;

        public ThresholdBipolar(double a) {
            this.a = a;
        }

        public ThresholdBipolar() {
            this(0.0);
        }

        @Override
        public Double compute(Double x) {
            return (x < a ? -1.0 : 1.0);
        }
    }

    public static class SigmoidUnipolar implements ActivationFunction {

        private final double beta;

        public SigmoidUnipolar(double beta) {
            this.beta = beta;
        }

        public SigmoidUnipolar() {
            this(0.0);
        }

        public Double compute(Double x) {
            return 1.0 / (1.0 + Math.pow(Math.E, -beta * x));
        }
    }

    public static class SigmoidBipolar implements ActivationFunction {

        private final double beta;

        public SigmoidBipolar(double beta) {
            this.beta = beta;
        }

        public SigmoidBipolar() {
            this(0.0);
        }

        @Override
        public Double compute(Double x) {
            double val = Math.pow(Math.E, -beta * x);
            return (1.0 - val) / (1.0 + val);
        }
    }

    public static class Gauss implements ActivationFunction {

        private final double a, b, div;

        public Gauss(double a, double b, double c) {
            this.a = a;
            this.b = b;

            div = 2.0 * Math.pow(c, 2.0);
        }

        @Override
        public Double compute(Double x) {
            return a * Math.E - (Math.pow(x - b, 2.0) / div);
        }
    }
}
