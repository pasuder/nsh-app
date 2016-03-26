__author__ = 'paoolo'

from nsh_app.function import activation, learningrate, neighborhood, measures

ACTIVATION_FUNC = {'linear': activation.linear,
                   'linear_cut': activation.linear_cut,
                   'threshold_unipolar': activation.threshold_unipolar,
                   'threshold_bipolar': activation.threshold_unipolar,
                   'sigmoid_unipolar': activation.sigmoid_unipolar,
                   'sigmoid_bipolar': activation.sigmoid_bipolar,
                   'gauss': activation.gauss}

LEARNING_RATE_FUNC = {'const': learningrate.const,
                      'linear': learningrate.linear,
                      'power': learningrate.power,
                      'exponential': learningrate.exponential,
                      'kohonen': learningrate.kohonen}

NEIGHBORHOOD_FUNC = {'linear': neighborhood.linear,
                     'exponential': neighborhood.exponential}

MEASUREMENT_FUNC = {'euclidean': measures.euclidean,
                    'scalar': measures.scalar,
                    'manhattan': measures.manhattan,
                    'manhattan_infinity': measures.manhattan_infinity}
