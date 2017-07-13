#!/bin/python

import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def main():

    # Config
    datafile = 'gm2-data/fid-analysis/e821/m9.fid'

    # Style setup
    mpl.rcParams['figure.figsize'] = (9, 6)

    # Load ideal waveform data
    d = np.genfromtxt(datafile)

    tm = d[:, 0]
    wf = d[:, 1] - d[:, 1].mean()
    N = wf.shape[0]

    fft = np.fft.fft(wf)

    fft[0] = 0.0
    fft[1:N/2+1] *= -1j;
    fft[N/2+1:] *= 1j;
    ht = np.fft.ifft(fft)

    env = (np.abs(wf)**2 + np.abs(ht)**2)**0.5

    n = 500
    plt.plot(tm[:n], wf[:n], alpha=0.7, linestyle='-', markersize=1.0, marker='o', label='FID Waveform')
    plt.plot(tm[:n], ht[:n], alpha=0.7, linestyle='-', markersize=1.0, marker='o', label='Hilbert Transform')
    plt.plot(tm[:n], env[:n], alpha=0.7, linestyle='-', markersize=1.0, marker='o', label='Envelope Function')

    plt.title('FID Hilbert Transform and Envelope')
    plt.ylabel(r'amplitude [a.u.]')
    plt.xlabel(r'time [ms]')
    plt.legend()
    plt.tight_layout()
    plt.savefig('test.pdf')

    # Now plot the phase and fit it
    plt.clf()

    i = 20
    n = 200
    ph = np.unwrap(np.arctan2(np.real(ht), wf))
    plt.plot(tm[:n], ph[:n], alpha=0.7, linestyle='-', markersize=1.0, marker='o', label='FID Phase')

    par = np.polyfit(tm[i:n], ph[i:n], 3)
    fit = par[0] * tm[:n]**3 + par[1] * tm[:n]**2
    fit += par[2] * tm[:n] + par[3]
    plt.plot(tm[:n], fit, alpha=0.7, linestyle='-', markersize=1.0, marker='o', label='Polynomial Fit')

    plt.title('FID Phase and Polynomial Fit')
    plt.ylabel(r'$\phi$')
    plt.xlabel(r'time [ms]')
    plt.legend()
    plt.tight_layout()
    plt.savefig('test2.pdf')


    return 0


if __name__ == '__main__':
    sys.exit(main())