# Nsh

[![Codacy Badge](https://api.codacy.com/project/badge/grade/f11cf980b1ca4184bb3b7951314ab12b)](https://www.codacy.com/app/pasuder/nsh-app)
[![Code Health](https://landscape.io/github/pasuder/nsh-app/master/landscape.svg?style=flat)](https://landscape.io/github/pasuder/nsh-app/master)

[![Code Climate](https://codeclimate.com/github/pasuder/nsh-app/badges/gpa.svg)](https://codeclimate.com/github/pasuder/nsh-app)
[![Test Coverage](https://codeclimate.com/github/pasuder/nsh-app/badges/coverage.svg)](https://codeclimate.com/github/pasuder/nsh-app/coverage)
[![Issue Count](https://codeclimate.com/github/pasuder/nsh-app/badges/issue_count.svg)](https://codeclimate.com/github/pasuder/nsh-app)

Neural network app with shell and batch processing mode.


## Requirements

* `python` with `pip` and `virtualenv`

## How to deploy

* Clone this project.
* Create python virtual environment using `bin/install.sh`
* Import project to your favorite IDE.

## How to use (PyPi)

Simply. Add to `requirements.txt`

    -e git+git://github.com/pasuder/nsh-app#egg=nsh-app

You can install it by python-installer

    pip install -e git+git://github.com/pasuder/nsh-app#egg=nsh-app

## How to run

After successful clone and install steps, in directory of this repository type `bin/main.sh`

    (local) ➜  nsh-app git:(master)  bin/main.sh     
    Neuronal (shell)
    nsh> help
    Command "help" not found.
    Available commands:
            compute
            compute_error
            compute_error_normalize
            compute_normalize
            init
            init_bias
            load
            locate
            multi_train_bp
            multi_train_bp_m
            multi_train_c
            multi_train_c_cp
            multi_train_n
            multi_train_n_cp
            new_cp
            new_kohonen
            new_layer
            new_network
            new_neuron
            show
            show_all
            train_bp
            train_bp_m
            train_c
            train_c_cp
            train_n
            train_n_cp
            zero
            zero_bias


Close by `[ctrl]+[c]`.

    nsh> ^C Ouch...
    Bye!

Commands used in shell and in batch mode described below in **Features**.

Application can be also run in batch mode:

    (local) ➜  nsh-app git:(master)  bin/main.sh -f examples/bp.nn
    Neuronal (batch)
    Creating BP network
    ---
    Testing back-propagation
    ...
    
    (local) ➜  nsh-app git:(master)  bin/main.sh --file=examples/bp.nn
    Neuronal (batch)
    Creating BP network
    ---
    Testing back-propagation
    ...


## How to contribute

Clone this repo, setup your environment using `bin/install.sh`. Change what you want to change and make pull request.

# Features

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

Load configuration from file.

Parameters:

*   ``file`` - ``string`` - path to file which contains commands to execute

### Creating objects

#### ``new_neuron``

Create new neuron.

Parameters:

*   ``name`` - ``string`` - name of created neuron
*   ``activation_func`` - ``string,params,...`` - name of activation function, activation function can be setup by params
*   ``weights`` - ``double,double,...`` - sequence of values used to set up on weights on neuron
*   ``bias`` - ``double`` - value set on bias of neurons
*   ``location`` - ``int,int,..`` - values of location on 1D or 2D Kohonen map

#### ``new_layer``

Create new layer using existing neurons.

Parameters:

*   ``name`` - ``string`` -  name of created layer
*   ``neurons`` - ``string,string,...`` - sequence of names of neurons used to create layer

#### ``new_network``

Create new network using existing layers.

Parameters:

*   ``name`` - ``string`` - name of created network
*   ``layers`` - ``string,string,...`` - sequence of names of layers used to create network

#### ``new_kohonen``

Create new Kohonen network.

Parameters:

*   ``name`` - ``string`` - name of created Kohonen network
*   ``input_func`` - ``string,params,...`` - name of activation function used in input layer
*   ``kohonen_func`` - ``string,params,...`` - name of activation function used in Kohonen layer
*   ``inputs`` - ``int`` - count of inputs
*   ``width`` - ``int`` - width of 1/2D Kohonen map
*   ``height`` - ``int`` - height of 2D Kohonen map

#### ``new_cp``

Create new CounterPropagation network.

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

Initialize weights on object using random values from range (min_value, max_value).

Parameters:

*   ``name`` - ``string`` - name of objects on which weights will initialized
*   ``min_value`` - ``double`` - minimum value of range
*   ``max_value`` - ``double`` - maximum value of range

#### ``zero_weights``

Set weights to zero.

Parameters:

*   ``name`` - ``string`` - name of objects on which weights will set to zero

#### ``set_location``

Set location on neuron.

Parameters:

*   ``name`` - ``string`` - name of neuron which will be setup on location
*   ``location`` - ``int,int,...`` - sequence of values of location

### Display objects

#### ``show_all``

Show list of objects names.

Parameters: none

#### ``show``

Show details of object.

Parameters:

*   ``name`` - ``string`` - name of objects to show

### Compute values

#### ``compute``

Compute value on selected object.

Parameters:

*   ``name`` - ``string`` - name of object which will be used to compute
*   ``values`` - ``double,double,...`` - sequence of values used to compute

### Train network

#### ``train_c``

Train network using competitive mode (Kohonen network).

Parameters:

*   ``name`` - ``string`` - name of object which will be used to train
*   ``learning_rate`` - ``string,params,...`` - name and params for learning rate function
*   ``iterations`` - ``int`` - count of iterations
*   ``traits`` - ``double,double,...`` - sequence of value of traits vector

#### ``train_n``

Train network using neighborhood mode (Kohonen network).

Parameters:

*   ``name`` - ``string`` - name of object which will be used to train
*   ``learning_rate`` - ``string,params,...`` - name and params for learning rate function
*   ``measurement`` - ``string,params,...`` - name and params for measurement function
*   ``neighborhood_radius`` - ``string,params,...`` - name and params for neighborhood radius function
*   ``iterations`` - ``int`` - count of iterations
*   ``traits`` - ``double,double,...`` - sequence of value of traits vector

#### ``train_c_cp``

Train network using competitive mode (CounterPropagation network).

Parameters:

*   ``name`` - ``string`` - name of object which will be used to train
*   ``learning_rate`` - ``string,params,...`` - name and params for learning rate function
*   ``grossberg_parameter`` - ``double`` - value of parameter used in Grossberg layer
*   ``iterations`` - ``int`` - count of iterations
*   ``traits`` - ``double,double,...`` - sequence of value of traits vector

#### ``train_n_cp``

Train network using neighborhood mode (CounterPropagation network).

Parameters:

*   ``name`` - ``string`` - name of object which will be used to train
*   ``learning_rate`` - ``string,params,...`` - name and params for learning rate function
*   ``measurement`` - ``string,params,...`` - name and params for measurement function
*   ``neighborhood_radius`` - ``string,params,...`` - name and params for neighborhood radius function
*   ``grossberg_parameter`` - ``double`` - value of parameter used in Grossberg layer
*   ``iterations`` - ``int`` - count of iterations
*   ``traits`` - ``double,double,...`` - sequence of value of traits vector

#### ``multi_train_c``

Performing many training using neighborhood mode (Kohonen network).

Parameters:

*   ``name`` - ``string`` - name of object which will be used to train
*   ``traits`` - ``double,double,...`` - sequence of value of traits vector
*   ``configs`` - ``learning_rate;grossberg_parameter|learning_rate;grossberg_parameter|...``
    *   ``learning_rate`` - ``string,params,...`` - name and params for learning rate function
    *   ``iterations`` - ``int`` - count of iterations

#### ``multi_train_n``

Performing many training using neighborhood mode (Kohonen network).

Parameters:

*   ``name`` - ``string`` - name of object which will be used to train
*   ``traits`` - ``double,double,...`` - sequence of value of traits vector
*   ``configs`` - ``learning_rate;measurement;neighborhood_radius;grossberg_parameter|...``
    *   ``learning_rate`` - ``string,params,...`` - name and params for learning rate function
    *   ``measurement`` - ``string,params,...`` - name and params for measurement function
    *   ``neighborhood_radius`` - ``string,params,...`` - name and params for neighborhood radius function
    *   ``iterations`` - ``int`` - count of iterations

#### ``multi_train_c_cp``

Performing many training using neighborhood mode (CounterPropagation network).

Parameters:

*   ``name`` - ``string`` - name of object which will be used to train
*   ``traits`` - ``double,double,...`` - sequence of value of traits vector
*   ``configs`` - ``learning_rate;grossberg_parameter|learning_rate;grossberg_parameter|...``
    *   ``learning_rate`` - ``string,params,...`` - name and params for learning rate function
    *   ``grossberg_parameter`` - ``double`` - value of parameter used in Grossberg layer
    *   ``iterations`` - ``int`` - count of iterations


#### ``multi_train_n_cp``

Performing many training using neighborhood mode (CounterPropagation network).

Parameters:

*   ``name`` - ``string`` - name of object which will be used to train
*   ``traits`` - ``double,double,...`` - sequence of value of traits vector
*   ``configs`` - ``learning_rate;measurement;neighborhood_radius;grossberg_parameter|...``
    *   ``learning_rate`` - ``string,params,...`` - name and params for learning rate function
    *   ``measurement`` - ``string,params,...`` - name and params for measurement function
    *   ``neighborhood_radius`` - ``string,params,...`` - name and params for neighborhood radius function
    *   ``grossberg_parameter`` - ``double`` - value of parameter used in Grossberg layer
    *   ``iterations`` - ``int`` - count of iterations
