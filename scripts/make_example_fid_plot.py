#!/bin/python

import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def main():

    # Style setup
    mpl.rcParams['figure.figsize'] = (9, 6)

    lenfid = 4096
    t0 = -0.5
    t1 = 1.0
    wp = 20.0
    A = 300.0

    # Load ideal waveform data
    x = np.linspace(t0, t0 + 0.001 * lenfid, lenfid)
    y = A * np.exp(-x / t1) * np.cos(-wp * x)
    y *= x > 0.0
    y += np.random.normal(size=x.shape)
    
    plt.plot(x, y, alpha=0.7, linestyle='-', markersize=1.0, marker='o', label='FID Waveform')

    plt.title('Example FID')
    plt.ylabel(r'amplitude [a.u.]')
    plt.xlabel(r'time [ms]')
    plt.tight_layout()
    plt.savefig('test.pdf')

    return 0


if __name__ == '__main__':
    sys.exit(main())