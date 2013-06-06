__author__ = 'paoolo'

HELP_TEXT = {
    'activation_func': 'Activation function not found.\n'
                       'Available activation function:\n'
                       '\tlinear,a=1.0,b=0.0\n'
                       '\tlinear_cut\n'
                       '\tthreshold_unipolar,a=0.0\n'
                       '\tthreshold_bipolar,a=0.0\n'
                       '\tsigmoid_unipolar,beta=0.0\n'
                       '\tsigmoid_bipolar,beta=1.0\n'
                       '\tgauss,a=1.0,b=1.0,c=1.0',
    'learning_rate_func': 'Learning rate function not found.\n'
                          'Available learning rate function:\n'
                          '\tlinear,max_period=1.0,initial_rate=1.0\n'
                          '\tpower,alpha=1.0,initial_rate=1.0\n'
                          '\texponential,max_iteration=1.0,min_transition=1.0,initial_rate=1.0',
    'neighborhood_func': 'Neighborhood function not found.\n'
                         'Available neighborhood function:\n'
                         '\tlinear,max_period=1.0,initial_radius=1.0\n'
                         '\texponential,max_iteration=1.0,min_transition=1.0,initial_radius=1.0',
    'measures_func': 'Measures function not found.\n'
                     'Available measures function:\n'
                     '\teuclidean\n'
                     '\tscalar\n'
                     '\tmanhattan\n'
                     '\tmanhattan_infinity'}