#!/usr/bin/env python

# data paths
import sys
sys.path.append('..')
from load_paths import path
# dependencies
import numpy as np
import bicycleparameters as bp
from dtk import bicycle

# create the Whipple model (with my parameters)
try:
    f = open('Whipple.py', 'r')
except IOError:
    from altk import alparse
    alparse.alparse('Whipple', 'Whipple', code='Python')
else:
    f.close()
    del f

# local dependencies
from Whipple import LinearWhipple

whip = LinearWhipple()

# load the benchmark parameters
crescendo = bp.Bicycle('Crescendo', path('pathToParameters'), forceRawCalc=True)
benchmarkPar = bp.io.remove_uncertainties(crescendo.parameters['Benchmark'])
# convert to my parameter set
moorePar = bicycle.benchmark_to_moore(benchmarkPar, oldMassCenter=False)
whip.set_parameters(moorePar)

# linearize about the nominal configuration
equilibrium = np.zeros(len(whip.stateNames))
pitchAngle = bicycle.pitch_from_roll_and_steer(0., 0., moorePar['rf'], moorePar['rr'],
        moorePar['d1'], moorePar['d2'], moorePar['d3'])
equilibrium[whip.stateNames.index('q5')] = pitchAngle
speedNaught = 1.5
u6Naught = -speedNaught / moorePar['rr']
equilibrium[whip.stateNames.index('u6')] = u6Naught
whip.linear(equilibrium)

figs = whip.plot_eigenvectors(states=('u4', 'u7'), pub=True)

for i, f in enumerate(figs):
    speed = '1p5'
    f.savefig('../../figures/parameterstudy/cres-evec-' + speed + '-' + str(i + 1) + '.png')
