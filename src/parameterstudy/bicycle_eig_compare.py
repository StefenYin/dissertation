#!/usr/bin/env python

# data paths
import sys
sys.path.append('..')
from load_paths import path

import numpy as np
import bicycleparameters as bp

speeds = np.linspace(0., 10., num=100)

# compare a bike with rider and bike without rider
stratos = bp.Bicycle('Stratos', pathToData=path('pathToParameters'),
        forceRawCalc=True)
stratosRider = bp.Bicycle('Stratos', pathToData=path('pathToParameters'),
        forceRawCalc=True)
stratosRider.add_rider('Jason')
compareRider = bp.plot_eigenvalues([stratos, stratosRider], speeds)
ax = compareRider.axes[0]
ax.set_ylim(-10, 10)
ax.legend_.get_texts()[1].set_text('Stratos + Jason')
compareRider.savefig('../../figures/parameterstudy/compare-rider-eig.png',
        dpi=200)

# compare the benchmark parameters to some of the bicycles I measured

benchmark = bp.Bicycle('Benchmark', pathToData=path('pathToParameters'))

browser = bp.Bicycle('Browser', pathToData=path('pathToParameters'),
        forceRawCalc=True)
browser.add_rider('Jason')

stratos = bp.Bicycle('Stratos', pathToData=path('pathToParameters'),
        forceRawCalc=True)
stratos.add_rider('Jason')

benchmarkReal = bp.plot_eigenvalues([benchmark, browser, stratos], speeds)
ax = benchmarkReal.axes[0]
ax.set_ylim(-10, 10)
benchmarkReal.savefig('../../figures/parameterstudy/benchmark-real.png',
        dpi=200)

# compare the silver bicycle parameters to some of the bicycles I measured
bicycleNames = ['Silver',
                'Crescendo',
                'Fisher',
                'Pista',
                'Yellow']

bicycles = [bp.Bicycle(name, pathToData=path('pathToParameters')) for name in
        bicycleNames]

silverCompare = bp.plot_eigenvalues(bicycles, speeds)
ax = silverCompare.axes[0]
ax.set_ylim(-10, 10)
silverCompare.savefig('../../figures/parameterstudy/silver-compare.png',
        dpi=200)

# compare the yellow bicycle configurations
silver = bicycles[0]
yellow = bicycles[-1]
yellowRev = bp.Bicycle('Yellowrev', pathToData=path('pathToParameters'),
        forceRawCalc=True)
yellowCompare = bp.plot_eigenvalues([yellow, yellowRev, silver], speeds)
ax = yellowCompare.axes[0]
ax.set_ylim(-10, 10)
yellowCompare.savefig('../../figures/parameterstudy/yellow-compare.png',
        dpi=200)

# compare the browser configurations
browser = bp.Bicycle('Browser', pathToData=path('pathToParameters'),
        forceRawCalc=True)
browserIns = bp.Bicycle('Browserins', pathToData=path('pathToParameters'),
        forceRawCalc=True)
browserCompare = bp.plot_eigenvalues([browser, browserIns], speeds)
ax = browserCompare.axes[0]
ax.set_ylim(-10, 10)
browserCompare.savefig('../../figures/parameterstudy/browser-compare.png',
        dpi=200)
# now add a rider
browser.add_rider('Jason')
browserIns.add_rider('Jason')
browserRiderCompare = bp.plot_eigenvalues([browser, browserIns], speeds)
ax = browserRiderCompare.axes[0]
ax.set_ylim(-10, 10)
browserRiderCompare.savefig('../../figures/parameterstudy/browser-rider-compare.png',
        dpi=200)
