#!/usr/bin/env python3
"""Uncertified locator for one signed neutral middle covariance comparison.

No output of this program proves a form sign. Full finite matrices and
directions are saved to support a separate exact-neutral interval test.
"""
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('entries545', BASE/'residual-certificate-532.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
con = mod.constants()
n = np.arange(512)
k = n*con['pi']/con['ell']
d, _, _ = mod.head_diagonal(k, con)
with np.load(BASE/'complete-covariance-532.npz') as saved:
    a = saved['m0'].copy()
    t = saved['mc']+saved['mg']
with np.load(BASE/'shared-middle-diagnostic-matrices-543.npz') as saved:
    oldbasis = saved['basis'].copy()
    u = oldbasis@saved['fourteen']@oldbasis.T

records = []
matrices = {}
for size in [8, 16, 32, 64, 128, 512]:
    z = np.zeros((512, size-2))
    for m in range(2, size):
        z[m,m-2] = 1
        p = m % 2
        ratio = ((.25+k[p]**2)/(.25+k[m]**2))*(np.sqrt(2) if p==0 else 1)
        z[p,m-2] = -ratio
    aa = z.T@a@z
    dd = z.T@(d[:,None]*z)
    tt = z.T@t@z
    uu = z.T@u@z
    refl = np.diag(np.where(np.arange(2,size)%2==0, 1., -1.))
    for sign in [-1, 1]:
        # h=sign*reflection(f); middle b=(I+sign*reflection) T f.
        coupling = tt+sign*tt.T@refl
        remote = sign*refl@uu
        surrogate = aa-remote-coupling.T@np.linalg.solve(dd,coupling)/2
        vals, vecs = np.linalg.eigh((surrogate+surrogate.T)/2)
        f = z@vecs[:,0]
        h = sign*np.where(n%2==0,1.,-1.)*f
        g = z@np.linalg.solve(dd,z.T@t@f+z.T@t.T@h)
        endpoint = float(f@a@f+h@a@h-2*h@u@f)
        middle = float(g@(d*g)-2*g@(t@f+t.T@h))
        original_middle_response = float(g@a@g-g@(d*g))
        key = f'n{size}_s{sign:+d}'
        records.append(dict(key=key,modes=size,sector=sign,
            diagonal_min=float(np.linalg.eigvalsh(dd)[0]),
            surrogate_min=float(vals[0]),endpoint_energy_minus_remote=endpoint,
            diagonal_middle_contribution=middle,comparison_value=endpoint+middle,
            omitted_positive_middle_response=original_middle_response,
            original_finite_value=endpoint+middle+original_middle_response))
        matrices[key+'_profiles'] = np.array([f,g,h])
        matrices[key+'_surrogate'] = surrogate

archive = BASE/'signed-diagonal-locator-545.npz'
np.savez_compressed(archive,**matrices)
report = dict(certified=False,records=records,failures=[],
    required_comparison_value='nonnegative for every neutral triple',
    limitations=['new floating matrices and eigensolves are uncertified',
                 'neutral moment ratios use floating constants',
                 'middle response deliberately omitted only in sufficient comparison',
                 'no infinite covariance sign and no original negative witness'],
    matrices=dict(path=archive.name,sha256=hashlib.sha256(archive.read_bytes()).hexdigest()))
path = BASE/'signed-diagonal-locator-545.json'
path.write_text(json.dumps(report,indent=2)+'\n')
for r in records:
    print(f"{r['key']}: comparison={r['comparison_value']:.9g}; original={r['original_finite_value']:.9g}; required>=0 (uncertified)")
print(f'Failures={report["failures"]}; report={path.relative_to(BASE.parent.parent)}; matrices={archive.relative_to(BASE.parent.parent)}')
