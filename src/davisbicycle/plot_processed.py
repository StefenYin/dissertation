#!/usr/bin/env python

# data paths
import sys
sys.path.append('..')
from load_paths import path

import bicycledataprocessor as bdp
import numpy as np
import matplotlib.pyplot as plt

dataset = bdp.DataSet(fileName=path('pathToDatabase'))
dataset.open()

trial = bdp.Run('00699', dataset, path('pathToParameterData'), filterFreq=40.)

dataset.close()

golden_mean = (np.sqrt(5) - 1.0) / 2.0
fig_width = 6.0
fig_height = fig_width * golden_mean
params = {'backend': 'ps',
          'axes.labelsize': 8,
          'axes.titlesize': 10,
          'text.fontsize': 8,
          'legend.fontsize': 6,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'figure.titlesize': 10,
          'figure.figsize': [fig_width,fig_height],
          'figure.dpi' : 200,
          'figure.subplot.left' : 0.2,
          'figure.subplot.bottom' : 0.15}
plt.rcParams.update(params)

sigs = ['PullForce', 'RollAngle', 'SteerAngle', 'SteerTorque']

mx = {sig : abs(trial.taskSignals[sig]).max() for sig in sigs}

plotStrings = [('%1.0f' % (mx['PullForce'] / v)) + '*' + k for k, v in mx.items()]

fig = trial.plot(*plotStrings)

fig.savefig('../../figures/davisbicycle/processed-data.png')
fig.savefig('../../figures/davisbicycle/processed-data.pdf')
