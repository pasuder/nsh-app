from main.function import activation as func

__author__ = 'paoolo'

from network import network as net


def neuron_and():
    return net.Neuron(func.threshold_unipolar(), weights=[1.0, 1.0], bias=1.5)


def neuron_or():
    return net.Neuron(func.threshold_unipolar(), weights=[1.0, 1.0], bias=0.5)


def neuron_not():
    return net.Neuron(func.threshold_unipolar(), weights=[-1.0], bias=-0.5)
