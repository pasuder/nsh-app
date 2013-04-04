
#include <cmath>
#include <functional>

namespace activation_function {

    std::function<double (double) > linear(double a, double b = 0.0) {

        return [ = ](double x) -> double {
            return a * x + b;
        };
    }

    std::function<double (double) > linear_cut() {

        return [] (double x) -> double {
            return (x < -1.0 ? -1.0 : (x > 1.0 ? 1.0 : x));
        };
    }

    std::function<double (double) > threshold_unipolar(double a = 0.0) {

        return [ = ] (double x) -> double {
            return (x < a ? 0.0 : 1.0);
        };
    }

    std::function<double (double) > threshold_bipolar(double a = 0.0) {

        return [ = ] (double x) -> double {
            return (x < a ? -1.0 : 1.0);
        };
    }

    std::function<double (double) > sigmoid_unipolar(double beta = 0.0) {

        return [ = ] (double x) -> double {
            return (1.0 / (1.0 + exp(-beta * x)));
        };
    }

    std::function<double (double) > sigmoid_bipolar(double beta = 0.0) {

        return [ = ] (double x) -> double {
            double val = exp(-beta * x);
            return (1.0 - val) / (1.0 + val);
        };
    }

    std::function<double (double) > gauss(double a, double b, double c) {

        double div = 2.0 * pow(c, 2.0);

        return [ = ] (double x) -> double {
            return a * exp(1) - (pow(x - b, 2.0) / div);
        };
    }

}