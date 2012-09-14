#!/usr/bin/env python

import sys
sys.path.append('..')
from load_paths import path

import cPickle
from canonicalbicycleid import canonical_bicycle_id as cbi
import pandas

with open(path('pathToIDMat')) as f:
    idMat = cPickle.load(f)

with open(path('pathToCovarMat')) as f:
    covMat = cPickle.load(f)
fNames = ['one', 'two', 'three']

roll = [['Mpd', 'C1pd', 'K0pd'], [], []]
steer = [[], ['Mdd', 'C1dp', 'C1dd'], ['K0dd', 'K2dd', 'HdF']]

for n, r, s in zip(fNames, roll, steer):
    tableData = cbi.table_data(r, s, idMat, covMat)
    df = pandas.DataFrame(tableData)
    del df[0], df[1]
    for col in df.columns:
        if '%' in  df[col][0]:
            del df[col]
    df = df.astype(float)
    print r, s
    print(df.mean())
    print(df.std())
    print(df.std() / abs(df.mean()) * 100)
    cbi.create_rst_table(tableData, r, s,
            fileName='../../tables/systemidentification/canonical-id-table-' +
            n + '.rst')

# this computes the trail given the identified C1dp parameter
rigid = cbi.bp.Bicycle('Rigid', path('pathToParameters'))
p = cbi.bp.io.remove_uncertainties(rigid.parameters['Benchmark'])
SF = p['IFyy'] / p['rF']
SR = p['IRyy'] / p['rR']
ST = SR + SF
for k, v in idMat.items():
    C1dp = v[1][1, 0]
    c = -p['w'] * (C1dp + SF * cbi.np.cos(p['lam'])) / ST / cbi.np.cos(p['lam'])
    print k, c
