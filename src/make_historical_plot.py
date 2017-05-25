#!/bin/python

import sys
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


def main():

    mpl.rcParams['figure.figsize'] = (9, 4)
    mpl.rcParams['figure.dpi'] = 220

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

        plt.scatter(x, y, color=c, alpha=0.8, label=label)
        plt.errorbar(x, y, yerr=yerr, ecolor=c, alpha=0.4, fmt='none')

    plt.title(r'Historical Values of Muon $a_\mu$')
    plt.xlabel(r'year')
    plt.ylabel(r'$a_\mu \times 10^{11}$')
    plt.legend()

    # plt.ylim([])
    plt.savefig('../fig/intro-historical-values.png')

    return 0


if __name__ == '__main__':
    sys.exit(main())