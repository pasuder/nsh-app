from main.function import activation, learningrate, neighborhood, measures

__author__ = 'paoolo'

activation_func = {'linear': activation.linear(),
                   'linear_cut': activation.linear_cut(),
                   'threshold_unipolar': activation.threshold_unipolar(),
                   'threshold_bipolar': activation.threshold_unipolar(),
                   'sigmoid_unipolar': activation.sigmoid_unipolar(),
                   'sigmoid_bipolar': activation.sigmoid_bipolar(),
                   'gauss': activation.gauss()}

learning_rate_func = {'linear': learningrate.linear(),
                      'power': learningrate.power(),
                      'exponential': learningrate.exponential()}

neighborhood_func = {'linear': neighborhood.linear(),
                     'exponential': neighborhood.exponential()}

measures_func = {'euclidean': measures.euclidean,
                 'scalar': measures.scalar,
                 'manhattan': measures.manhattan,
                 'manhattan_infinity': measures.manhattan_infinity}

info_text = {'neuron_not_added': 'Neuron "%s" not added',
             'neuron_added': 'Neuron "%s" added',
             'layer_not_added': 'Layer "%s" not added',
             'layer_added': 'Layer "%s" added',
             'network_not_added': 'Network "%s" not added',
             'network_added': 'Network "%s" added'}

error_text = {
    'activation_function_not_found': 'Activation function "%s" not found: %s.\n'
                                     'Available activation function:\n'
                                     '\tlinear\n'
                                     '\tlinear_cut\n'
                                     '\tthreshold_unipolar\n'
                                     '\tthreshold_bipolar\n'
                                     '\tsigmoid_unipolar\n'
                                     '\tsigmoid_bipolar\n'
                                     '\tgauss',
    'learning_rate_function_not_found': 'Learning rate function "%s" not found: %s.\n'
                                        'Available learning rate function:\n'
                                        '\tlinear\n'
                                        '\tpower\n'
                                        '\texponential',
    'neighborhood_function_not_found': 'Neighborhood function "%s" not found: %s.\n'
                                       'Available neighborhood function:\n'
                                       '\tlinear\n'
                                       '\texponential',
    'measures_function_not_found': 'Measures function "%s" not found: %s.\n'
                                   'Available measures function:\n'
                                   '\teuclidean\n'
                                   '\tscalar\n'
                                   '\tmanhattan\n'
                                   '\tmanhattan_infinity',
    'neuron_not_found': 'Neuron "%s" not found: %s',
    'layer_not_found': 'Layer "%s" not found: %s',
    'name_not_found': 'Name "%s" not found: %s',
    'file_not_found': 'File "%s" not found: %s'}

help_text = {
    '': 'Usage: new_neuron|new_layer|new_network|new_kohonen|'
        'show_all|show|compute|init|zero|load|locate|train_c|train_n',
    'new_neuron': 'Usage: new_neuron NAME FUNC WEIGHTS BIAS [location LOCATION]',
    'new_layer': 'Usage: new_layer NAME NEURONS',
    'new_network': 'Usage: new_network NAME LAYERS',
    'new_kohonen': 'Usage: new_kohonen NAME INPUT_FUNC KOHONEN_FUNC INPUTS WIDTH [HEIGHTS]',
    'new_cp': 'Usage: new_cp NAME INPUT_FUNC KOHONEN_FUNC GROSSBERG_FUNC INPUTS OUTPUTS WIDTH [HEIGHTS]',
    'show': 'Usage: show NAME',
    'compute': 'Usage: compute NAME INPUTS',
    'init': 'Usage: init NAME MIN MAX',
    'zero': 'Usage: zero NAME',
    'load': 'Usage: load NAME',
    'locate': 'Usage: locate NAME LOCATION',
    'train_c': 'Usage: train_c NAME LEARNING_RATE ITERATION TRAITS',
    'train_n': 'Usage: train_n NAME LEARNING_RATE MEASUREMENT NEIGHBORHOOD_RADIUS ITERATIONS TRAITS'}

LEARNING_RATE = 'learning_rate'
MEASUREMENT = 'measurement'
NEIGHBORHOOD_RADIUS = 'neighborhood_radius'
GROSSBERG_PARAMETER = 'mi'