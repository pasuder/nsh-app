__author__ = 'paoolo'

from main.function.activation import threshold_unipolar
from main.network.network import Neuron


def neuron_and():
    return Neuron(threshold_unipolar(), weights=[1.0, 1.0], bias=1.5)


def neuron_or():
    return Neuron(threshold_unipolar(), weights=[1.0, 1.0], bias=0.5)


def neuron_not():
    return Neuron(threshold_unipolar(), weights=[-1.0], bias=-0.5)
