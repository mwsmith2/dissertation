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
    wp = 40.0
    A = 300.0

    # Load ideal waveform data
    x = np.linspace(t0, t0 + 0.001 * lenfid, lenfid)
    y = A * (1.0 + 0.1 * np.sin(1.8 * wp * x + 0.2)) * np.exp(-x / t1) * np.cos(wp * x)
    y *= x > 0.0
    y += np.random.normal(size=x.shape)

    # Draw FID    
    plt.plot(x, y, alpha=0.6, linestyle='-', markersize=1.0, marker='o', label='FID Waveform')
    plt.title('Zero Crossing Hysteresis')
    plt.ylabel(r'amplitude [a.u.]')
    plt.xlabel(r'time [ms]')
    plt.grid(color='k', alpha=0.1)

    # Draw hysteresis lines
    plt.axhline(A * 0.2, color='k', lw=3, alpha=0.5, ls='--', label='Hysteresis Threshold')
    plt.axhline(-A * 0.2, color='k', lw=3, alpha=0.5, ls='--')

    # Draw zero crossing fits
    phi = 0.5 * np.pi
    i = np.where(wp * x < -0.1 * np.pi + phi)[0][-1]
    f = np.where(wp * x > +0.1 * np.pi + phi)[0][0]

    p1 = np.polyfit(x[i:f] - phi, y[i:f], 3)
    x1 = x[i:f] - phi
    y1 = p1[0] * x1**3 + p1[1] * x1**2 + p1[2] * x1 + p1[3]
    plt.plot(x[i:f],  y[i:f], lw=3, label='First Zero Crossing Fit')
    #plt.plot(x1,  y1, label='First Zero Crossing Fit')

    phi = 20.5 * np.pi
    i = np.where(wp * x < -0.1 * np.pi + phi)[0][-1]
    f = np.where(wp * x > +0.1 * np.pi + phi)[0][0]

    p2 = np.polyfit(x[i:f] - phi, y[i:f], 3)
    x2 = x[i:f] - phi
    y2 = p2[0] * x2**3 + p2[1] * x2**2 + p2[2] * x2 + p1[3]
    #plt.plot(x2,  y2, label='Final Zero Crossing Fit')
    plt.plot(x[i:f],  y[i:f], lw=3, label='Final Zero Crossing Fit')

    plt.legend()
    plt.xlim([x[0], x[-1]])
    plt.tight_layout()
    plt.savefig('fig/fid-freq-zc-hysteresis.pdf')

    return 0


if __name__ == '__main__':
    sys.exit(main())