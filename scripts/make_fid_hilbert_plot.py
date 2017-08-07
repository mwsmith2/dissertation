#!/bin/python

import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def main():

    # Config
    datafile = 'gm2-data/fid-analysis/e821/m9.fid'

    # Style setup
    mpl.style.use('presentation')
    mpl.rcParams['figure.figsize'] = (16, 9)

    lw = 3.0
    ms = 4.0

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

    n = 200
    plt.plot(tm[:n], wf[:n], alpha=0.7, lw=lw, linestyle='-', markersize=ms, marker='o', label='FID Waveform')
    plt.plot(tm[:n], ht[:n], alpha=0.7, lw=lw, linestyle='-', markersize=ms, marker='o', label='Hilbert Transform')
    plt.plot(tm[:n], env[:n], alpha=0.7, lw=lw, linestyle='-', markersize=ms, marker='o', label='Envelope Function')

    plt.title('FID Hilbert Transform and Envelope')
    plt.ylabel(r'amplitude [a.u.]')
    plt.xlabel(r'time [ms]')
    plt.legend(fontsize='xx-large')
    plt.tight_layout()
    plt.grid()
    plt.savefig('test.pdf')
    plt.savefig('test.png')

    # Now plot the phase and fit it
    plt.clf()
    plt.subplots(2, 1, figsize=(16, 9))
    plt.subplot(2, 1, 1)

    i = 20
    n = 200
    ph = np.unwrap(np.arctan2(np.real(ht), wf))
    plt.plot(tm[:n], ph[:n], alpha=0.7, linestyle='-', markersize=1.0, marker='o', label='FID Phase')

    par = np.polyfit(tm[i:n], ph[i:n], 3)
    fit = par[0] * tm[:n]**3 + par[1] * tm[:n]**2
    fit += par[2] * tm[:n] + par[3]
    plt.plot(tm[10:n], fit[10:], alpha=0.7, linestyle='-', markersize=1.0, marker='o', label='Polynomial Fit')

    plt.title('FID Phase, Polynomial Fit and Residuals')
    plt.ylabel(r'$\phi$')
    xlim = plt.xlim()
    plt.legend(fontsize='xx-large', loc=4)
    plt.grid()

    plt.subplot(2, 1, 2)
    c = mpl.rcParams['axes.color_cycle'][2]
    plt.plot(tm[10:n], fit[10:] - ph[10:n], alpha=0.7, c=c, ls='-', ms=1.0, marker='o', label='Fit Residuals')

    plt.ylabel(r'$\delta \phi$')
    plt.xlabel(r'time [ms]')
    plt.xlim(xlim)
    plt.legend(fontsize='xx-large', loc=4)

    plt.tight_layout()
    plt.grid()
    plt.savefig('test2.pdf')
    plt.savefig('test2.png')

    # Now plot the normalized signal and fit it
    plt.clf()
    plt.subplots(1, 1, figsize=(16, 9))

    i = 20
    n = 100
    y = wf / np.sqrt(np.real(ht)**2 + wf**2)

    def sinusoid(t, w, a, b, phi):
        return a * np.sin(w * t - phi) + b

    pguess = [par[2], 1.0, 0.0, 0.0]
    p, c = curve_fit(sinusoid, tm[20:500], y[20:500], p0=pguess)
    x3 = np.linspace(tm[10], tm[n], 1001)
    y3 = sinusoid(x3, p[0], p[1], p[2], p[3])
    
    plt.plot(tm[:n], y[:n], alpha=1.0, lw=0.5*lw, linestyle='-', markersize=ms, marker='o', label='Normalized FID')
    plt.plot(x3, y3, alpha=1.0, lw=lw, linestyle=':', label='Sinsoid Fit')

    plt.title('Normalized FID and Sinusoidal Fit')
    plt.ylabel(r'normalized amplitude')
    plt.xlabel(r'time [ms]')
    plt.ylim([-1.5, 1.2])
    plt.legend(fontsize='xx-large')
    plt.tight_layout()
    plt.grid()
    plt.savefig('test3.pdf')
    plt.savefig('test3.png')


    return 0


if __name__ == '__main__':
    sys.exit(main())