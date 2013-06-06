# Nsh

Neural network app with shell and batch processing mode.

[![Master Build Status](https://travis-ci.org/paoolo/neurony-main.png?branch=master)](https://travis-ci.org/paoolo/neurony-main)
[![Devel Build Status](https://travis-ci.org/paoolo/neurony-main.png?branch=devel)](https://travis-ci.org/paoolo/neurony-main)

## What I need to have?

*   python

## How to run?

1.  Download this as zip or by cloning repo
2.  Extract archive (if you have downloaded) and change directory to ``./python/``
3.  Type ``$ ./main.py``
4.  Prompt shell will be shown

If you want to use batch processing mode, type ``$ ./main.py -f path/to/file``.

## Activation function

*   ``linear[,a[,b]]`` - Linear activation function, default:
    *   a - 1.0
    *   b - 0.0
*   ``linear_cut`` - Partially linear activation function
*   ``threshold_unipolar[,a]`` - Threshold unipolar activation function
    *   a - 0.0
*   ``threshold_bipolar[,a]`` - Threshold bipolar activation function
    *   a - 0.0
*   ``sigmoid_unipolar[,beta]`` - Sigmoid unipolar activation function
    *   beta - 0.0
*   ``sigmoid_bipolar[,beta]`` - Sigmoid bipolar activation function
    *   beta - 1.0
*   ``gauss[,a[,b[,c]]]`` - Gauss activation function
    *   a - 1.0
    *   b - 1.0
    *   c - 1.0

## Learning rate function

*   ``linear[,max_period[,initial_rate]]`` - Linear learning rate function, default:
    *   max_period - 1.0
    *   initial_rate - 1.0
*   ``power[,alpha[,initial_rate]]`` - Power learning rate function, default:
    *   alpha - 1.0
    *   initial_rate - 1.0
*   ``exponential[,max_iteration[,min_transition[,initial_rate]]]`` - Exponential learning rate function, default:
    *   max_iteration - 1.0
    *   min_transition - 1.0
    *   initial_rate - 1.0

## Neighborhood function

*   ``linear[,max_period[,initial_radius]]`` - Linear radius neighborhood function, default:
    *   max_period - 1.0
    *   initial_radius - 1.0
*   ``exponential[,max_iteration[,min_transition[,initial_radius]]]`` - Exponential radius neighborhood function, default:
    *   max_iteration - 1.0
    *   min_transition - 1.0
    *   initial_radius - 1.0

## Measure function

*   ``euclidean`` - Euclidean measure
*   ``scalar`` - Scalar measure
*   ``manhattan`` - Manhattan measure, under L_1 standard
*   ``manhattan_infinity`` - Manhattan measure, under L_infinity standard

## Values types

*   ``string`` - any string, without whitespaces, like 'example_string'
*   ``int`` - decimal number, like '10'
*   ``double`` - floating point number, like '123.4'
*   ``type,type,...`` - sequence of values of type, without whitespaces, like '10,13,1' or 'test_string,next_string'

## Commands

*   Batch mode
    *   ``load``
*   Creating objects
    *   ``new_neuron``
    *   ``new_layer``
    *   ``new_network``
    *   ``new_kohonen``
    *   ``new_cp``
*   Setting objects
    *   ``init_weights``
    *   ``zero_weights``
    *   ``set_location``
*   Display objects
    *   ``show_all``
    *   ``show``
*   Compute values
    *   ``compute``
*   Train network
    *   ``train_c``
    *   ``train_n``
    *   ``train_c_cp``
    *   ``train_n_cp``
    *   ``multi_train_c``
    *   ``multi_train_n``

### Batch mode

#### ``load``

Parameters:

*   ``file`` - ``string`` - path to file which contains commands to execute

### Creating objects

#### ``new_neuron``

Parameters:

*   ``name`` - ``string`` - name of created neuron
*   ``activation_func`` - ``string,params,...`` - name of activation function, activation function can be setup by params
*   ``weights`` - ``double,double,...`` - sequence of values used to set up on weights on neuron
*   ``bias`` - ``double`` - value set on bias of neurons
*   ``location`` - ``int,int,..`` - values of location on 1D or 2D Kohonen map

#### ``new_layer``

Parameters:

*   ``name`` - ``string`` -  name of created layer
*   ``neurons`` - ``string,string,...`` - sequence of names of neurons used to create layer

#### ``new_network``

Parameters:

*   ``name`` - ``string`` - name of created network
*   ``layers`` - ``string,string,...`` - sequence of names of layers used to create network

#### ``new_kohonen``

Parameters:

*   ``name`` - ``string`` - name of created Kohonen network
*   ``input_func`` - ``string,params,...`` - name of activation function used in input layer
*   ``kohonen_func`` - ``string,params,...`` - name of activation function used in Kohonen layer
*   ``inputs`` - ``int`` - count of inputs
*   ``width`` - ``int`` - width of 1/2D Kohonen map
*   ``height`` - ``int`` - height of 2D Kohonen map

#### ``new_cp``

Parameters:

*   ``name`` - ``string`` - name of created CounterPropagation network
*   ``input_func`` - ``string,params,...`` - name of activation function used in input layer
*   ``kohonen_func`` - ``string,params,...`` - name of activation function used in Kohonen layer
*   ``grossberg_func`` - ``string,params,...`` - name of activation function used in Grossberg layer
*   ``inputs`` - ``int`` - count of inputs
*   ``outputs`` - ``int`` - count of outputs
*   ``width`` - ``int`` - width of 1/2D Kohonen map
*   ``height`` - ``int`` - height of 2D Kohonen map

### Setting objects

#### ``init_weights``

Parameters:

*   ``name`` - ``string`` - name of objects on which weights will initialized
*   ``min_value`` - ``double`` - minimum value of range
*   ``max_value`` - ``double`` - maximum value of range

#### ``zero_weights``

Parameters:

*   ``name`` - ``string`` - name of objects on which weights will set to zero

#### ``set_location``

Parameters:

*   ``name`` - ``string`` - name of neuron which will be setup on location
*   ``location`` - ``int,int,...`` - sequence of values of location

### Display objects

#### ``show_all``

Parameters: none

#### ``show``

Parameters:

*   ``name`` - ``string`` - name of objects to show

### Compute values

#### ``compute``

Parameters:

*   ``name`` - ``string`` - name of objects which will be used to compute
*   ``values`` - ``double,double,...`` - sequence of values used to compute

### Train network

#### ``train_c``

#### ``train_n``

#### ``train_c_cp``

#### ``train_n_cp``

#### ``multi_train_c``

#### ``multi_train_n``