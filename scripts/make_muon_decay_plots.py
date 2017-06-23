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

    # And the lab frame.
    n_lab = (y - 1) * (4 * y**2 - 5 * y - 5) / 5
    a_lab = (-8 * y**2 + y + 1) / (4 * y**2 - 5 * y - 5)

    # Plot the rest frame.
    plt.subplot(1, 2, 1)
    plt.plot(y, n_rest, label=r'$n(y)$')
    plt.plot(y, a_rest, label=r'$a(y)$')

    plt.title('Rest Frame')
    plt.xlabel(r'y [$E/E_{max}$]')
    plt.grid(alpha=0.5)
    plt.legend()

    # And, the lab frame.
    plt.subplot(1, 2, 2)
    plt.plot(y, n_lab, label='N')
    plt.plot(y, a_lab, label='A')

    plt.title('Lab Frame')
    plt.xlabel(r'y [$E/E_{max}$]')
    plt.grid(alpha=0.5)
    plt.savefig('fig/muon-decay-distributions.pdf')

    # Make similar plots with the FoM included now.
    fom = n_lab * a_lab * np.abs(a_lab)
    fom_lo = fom.cumsum()
    fom_hi = fom[::-1].cumsum()[::-1]

    plt.clf()
    plt.subplot(1, 2, 1)
    plt.plot(y, n_lab, label=r'$a(y)$')
    plt.plot(y, a_lab, label=r'$n(y)$')

    plt.title('Muon Decay Attributes')
    plt.xlabel(r'y [$E/E_{max}$]')
    plt.grid(alpha=0.5)
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(y, fom_lo / fom_hi.max(), label=r'$\int_0^y n(y)a^2(y) dy$')
    plt.plot(y, fom_hi / fom_hi.max(), label=r'$\int_y^1 n(y)a^2(y) dy$')

    plt.title('Spin Correlation Figure of Merit')
    plt.xlabel(r'y [$E/E_{max}$]')
    plt.ylim([-1.1, 1.1])
    plt.grid(alpha=0.5)
    plt.legend()

    plt.savefig('fig/muon-precession-fom.pdf')

    return 0

if __name__ == '__main__':
    sys.exit(main())