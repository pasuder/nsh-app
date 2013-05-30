__author__ = 'paoolo'

from function import activation, learningrate, neighborhood, measures

ACTIVATION_FUNC = {'linear': activation.linear,
                   'linear_cut': activation.linear_cut,
                   'threshold_unipolar': activation.threshold_unipolar,
                   'threshold_bipolar': activation.threshold_unipolar,
                   'sigmoid_unipolar': activation.sigmoid_unipolar,
                   'sigmoid_bipolar': activation.sigmoid_bipolar,
                   'gauss': activation.gauss}

LEARNING_RATE_FUNC = {'linear': learningrate.linear,
                      'power': learningrate.power,
                      'exponential': learningrate.exponential}

NEIGHBORHOOD_FUNC = {'linear': neighborhood.linear,
                     'exponential': neighborhood.exponential}

MEASUREMENT_FUNC = {'euclidean': measures.euclidean,
                    'scalar': measures.scalar,
                    'manhattan': measures.manhattan,
                    'manhattan_infinity': measures.manhattan_infinity}

ERROR_TEXT = {
    'activation_function_not_found': 'Activation function not found.\n'
                                     'Available activation function:\n'
                                     '\tlinear,a=1.0,b=0.0\n'
                                     '\tlinear_cut\n'
                                     '\tthreshold_unipolar,a=0.0\n'
                                     '\tthreshold_bipolar,a=0.0\n'
                                     '\tsigmoid_unipolar,beta=0.0\n'
                                     '\tsigmoid_bipolar,beta=1.0\n'
                                     '\tgauss,a=1.0,b=1.0,c=1.0',
    'learning_rate_function_not_found': 'Learning rate function not found.\n'
                                        'Available learning rate function:\n'
                                        '\tlinear,max_period=1.0,initial_rate=1.0\n'
                                        '\tpower,alpha=1.0,initial_rate=1.0\n'
                                        '\texponential,max_iteration=1.0,min_transition=1.0,initial_rate=1.0',
    'neighborhood_function_not_found': 'Neighborhood function not found.\n'
                                       'Available neighborhood function:\n'
                                       '\tlinear,max_period=1.0,initial_radius=1.0\n'
                                       '\texponential,max_iteration=1.0,min_transition=1.0,initial_radius=1.0',
    'measures_function_not_found': 'Measures function not found.\n'
                                   'Available measures function:\n'
                                   '\teuclidean\n'
                                   '\tscalar\n'
                                   '\tmanhattan\n'
                                   '\tmanhattan_infinity',
    'object_not_found': 'Object not found.'}

LEARNING_RATE = 'learning_rate'
MEASUREMENT = 'measurement'
NEIGHBORHOOD_RADIUS = 'neighborhood_radius'
GROSSBERG_PARAMETER = 'grossberg_parameter'
ITERATIONS = 'iterations'