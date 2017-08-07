#!/bin/python

import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def main():

    # Config
    datafile = 'gm2-data/fid-analysis/ideal/flat-freq/run_total.csv'
    nbins = 250

    # Style setup
    mpl.rcParams['figure.figsize'] = (9, 6)

    # Load ideal waveform data
    d = np.genfromtxt(datafile, delimiter=',')

    freq = {}
    ferr = {}

    freq['zc'] = d[:, 2]
    ferr['zc'] = d[:, 3]

    freq['cn'] = d[:, 6]
    ferr['cn'] = d[:, 7]

    freq['an'] = d[:, 10]
    ferr['an'] = d[:, 11]

    freq['lz'] = d[:, 14]
    ferr['lz'] = d[:, 15]

    freq['ph'] = d[:, 22]
    ferr['ph'] = d[:, 23]

    freq['sn'] = d[:, 26]
    ferr['sn'] = d[:, 27]

    plt.subplot(2, 1, 1)
    bins = np.linspace(-0.05, 0.05, nbins+1)
    for key in ['cn', 'lz', 'an']:
        label = r'%s: $(\mu, \sigma)$ = (%i, %i)'
        df_ppb = (freq[key] - d[:, 0]) / 61.79e3 * 1e9
        label = label % (key.upper(), df_ppb.mean(), df_ppb.std())
        plt.hist(df_ppb, histtype='step', bins=nbins, label=label)

    plt.title('Ideal FID Frequency Extraction - Freq Domain')
    plt.xlabel(r'$f_{calc} - f_{truth}$ [ppb]')

    plt.grid()
    plt.legend(fontsize='small')

    plt.subplot(2, 1, 2)
    for key in ['ph', 'zc']:
        label = r'%s: $(\mu, \sigma)$ = (%.1f, %.1f)'
        df_ppb = (freq[key] - d[:, 0]) / 61.79e3 * 1e9
        label = label % (key.upper(), df_ppb.mean(), df_ppb.std())
        plt.hist(df_ppb, histtype='step', bins=nbins, label=label)

    plt.title('Ideal FID Frequency Extraction - Time Domain')
    plt.xlabel(r'$f_{calc} - f_{truth}$ [ppb]')

    plt.grid()
    plt.legend(fontsize='small')

    plt.tight_layout()
    plt.savefig('test.pdf')

    return 0


if __name__ == '__main__':
    sys.exit(main())