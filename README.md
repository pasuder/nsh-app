# Nsh

Neural network app with shell and batch processing mode.

## What I need to have?

*   python

## How to run?

1.  Download this as zip or by cloning repo
2.  Extract *.zip (if you have downloaded) and change directory
3.  Type
    <code>$ ./main.py</code>
4.  Prompt shell will be shown

## How to use?

You can use this software in:

*   shell mode
*   batch processing mode

Available activation function (FUNC):
*   linear
*   linear_cut
*   threshold_unipolar
*   threshold_bipolar
*   sigmoid_unipolar
*   sigmoid_bipolar
*   gauss

Weights (WEIGHTS) and inputs (INPUTS) must look like: <code>1.0 1.0 1.0<code>.

### Shell mode

Available commands:

*   new neuron NAME FUNC WEIGHTS... BIAS
*   new layer NAME NEURONS...
*   new network NAME LAYERS...
*   show NAME
*   compute NAME INPUTS

### Batch processing mode

Available options:

*   neuron NAME FUNC WEIGHTS... BIAS
*   layer NAME NEURONS...
*   network NAME LAYERS...
*   compute NAME INPUTS