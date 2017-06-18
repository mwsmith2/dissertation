#!/bin/python

import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def main():

    mpl.rcParams['figure.figsize'] = (9, 3)
    mpl.rcParams['figure.dpi'] = 220

    mpl.rcParams['lines.linewidth'] = 1.0
    mpl.rcParams['lines.markersize'] = 2.0
    
    mpl.rcParams['grid.color'] = '#b0b0b0'
    mpl.rcParams['axes.facecolor'] = 'white'
    mpl.rcParams['axes.edgecolor'] = '#b0b0b0'

    y = np.linspace(0, 1, 10001)

    # Distributions in the muon rest frame.
    n_rest = y * y * (3 - 2 * y)
    a_rest = (2 * y - 1) / (3 - 2 * y)

    plt.subplot(1, 2, 1)
    plt.plot(y, n_rest, label='N')
    plt.plot(y, a_rest, label='A')

    plt.title('Rest Frame')
    plt.xlabel(r'y [$E/E_{max}$]')
    plt.grid(alpha=0.5)
    plt.legend()

    # And the lab frame.
    n_lab = (y - 1) * (4 * y**2 - 5 * y - 5) / 5
    a_lab = (-8 * y**2 + y + 1) / (4 * y**2 - 5 * y - 5)

    plt.subplot(1, 2, 2)
    plt.plot(y, n_lab, label='N')
    plt.plot(y, a_lab, label='A')

    plt.title('Lab Frame')
    plt.xlabel(r'y [$E/E_{max}$]')
    plt.grid(alpha=0.5)
    plt.savefig('fig/muon-decay-distributions.pdf')

    return 0

if __name__ == '__main__':
    sys.exit(main())