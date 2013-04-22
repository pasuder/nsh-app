# Nsh

Neural network app with shell and batch processing mode.

[![Master Build Status](https://travis-ci.org/paoolo/neurony-main.png?branch=master)](https://travis-ci.org/paoolo/neurony-main)
[![Devel Build Status](https://travis-ci.org/paoolo/neurony-main.png?branch=devel)](https://travis-ci.org/paoolo/neurony-main)

### What I need to have?

*   python

### How to run?

1.  Download this as zip or by cloning repo
2.  Extract archive (if you have downloaded) and change directory
3.  Type ``$(PROJECT_ROOT)/python/main.py`` or double-click on file ``main.py`` in ``$(PROJECT_ROOT)/main/``
4.  Prompt shell will be shown

If you want to use batch processing mode, type ``$(PROJECT_ROOT)/python/main.py -f path/to/file``.

### How to use?

Available modes:

*   shell mode
*   batch processing mode

Available activation function (``FUNC``):

*   ``linear``
*   ``linear_cut``
*   ``threshold_unipolar``
*   ``threshold_bipolar``
*   ``sigmoid_unipolar``
*   ``sigmoid_bipolar``
*   ``gauss``

Weights (``WEIGHTS``) and inputs (``INPUTS``) must a one dimensional float sequence: ``1.0 1.0 1.0``.
Bias (``BIAS``) must be a single float value: ``1.0``.

##### Shell mode

Available commands:

*   ``new neuron NAME FUNC WEIGHTS... BIAS``
*   ``new layer NAME NEURONS...``
*   ``new network NAME LAYERS...``
*   ``show NAME``
*   ``compute NAME INPUTS``
*   ``load FILE``

##### Batch processing mode

Available options:

*   ``neuron NAME FUNC WEIGHTS... BIAS``
*   ``layer NAME NEURONS...``
*   ``network NAME LAYERS...``
*   ``compute NAME INPUTS``
