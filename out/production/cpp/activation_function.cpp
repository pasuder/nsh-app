#include <cmath>

namespace activation_function {

    auto linear(double a, double b = 0.0) {
        return [] (double x){return a * x + b; };
    }

    auto linear_cut() {
        return [] (double x) { return (x < -1.0 ? -1.0 : (x > 1.0 ? 1.0 : x)); };
    }

    auto threshold_unipolar(double a=0.0) {
        return [] (double x) { return (x < a ? 0.0 : 1.0); };
    }

    auto threshold_bipolar(double a=0.0) {
        return [] (double x) { return (x < a ? -1.0, 1.0); };
    }

    auto sigmoid_unipolar(double beta=0.0) {
        return [] (double x) { return (1.0 / (1.0 + exp(-beta * x))); };
    }

    auto sigmoid_bipolar(double beta=0.0) {
        // paoolo TODO
    }

    auto gauss(double a, double b, double c) {
        // paoolo TODO
    }

}