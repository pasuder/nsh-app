
#ifndef ACTIVATION_FUNCTION_HPP
#define	ACTIVATION_FUNCTION_HPP

#include <functional>

namespace activation_function {

    std::function<double (double) > linear(double a, double b = 0.0);

    std::function<double (double) > linear_cut();

    std::function<double (double) > threshold_unipolar(double a = 0.0);

    std::function<double (double) > threshold_bipolar(double a = 0.0);

    std::function<double (double) > sigmoid_unipolar(double beta = 0.0);

    std::function<double (double) > sigmoid_bipolar(double beta = 0.0);

    std::function<double (double) > gauss(double a, double b, double c);

}

#endif	/* ACTIVATION_FUNCTION_HPP */

