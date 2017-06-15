#!/bin/python

import sys
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


def main():

    mpl.rcParams['figure.figsize'] = (9, 4)
    mpl.rcParams['figure.dpi'] = 220

    mpl.rcParams['lines.linewidth'] = 1.0
    mpl.rcParams['lines.markersize'] = 2.0
    
    mpl.rcParams['grid.color'] = '#b0b0b0'
    mpl.rcParams['axes.facecolor'] = 'white'
    mpl.rcParams['axes.edgecolor'] = '#b0b0b0'

    with open('historical_values.json') as f:
        data = json.loads(f.read())

    colors = sns.hls_palette(10, l=0.3, s=0.8)

    a_avg = 0
    a_err = 0

    expt_color = {}
    c_idx = 0
    e_idx = 1 # Skip the first experiment

    for d in data['expt'][e_idx:]:
        x = d['year']
        y = d['value'] * 10**11
        yerr = d['error'] * 10**11

        if d['expt'] in expt_color.keys():
            c = expt_color[d['expt']]
            label = None

        else:
            c = colors[c_idx]
            expt_color[d['expt']] = c
            c_idx += 1
            label = 'Expt - ' + d['expt']

        plt.scatter(x, y, color=c, alpha=1.0, label=label)
        plt.errorbar(x, y, yerr=yerr, ecolor=c, alpha=0.7, fmt='none')

    plt.title(r'Historical Values of Muon $a_\mu$')
    plt.xlabel(r'year')
    plt.ylabel(r'$a_\mu \times 10^{11}$')
    plt.legend(facecolor='white', frameon=True, framealpha=0.7)
    plt.grid(c='#a0a0a0', alpha=0.4)

    # plt.ylim([])
    plt.savefig('../fig/intro-historical-values.png')

    return 0


if __name__ == '__main__':
    sys.exit(main())