#!/usr/bin/env python3
"""One frozen-X reference proposal. Diagnostic only: no certified sign.

The full saved X and input pins are checked before any mathematical solve.
Singular Carleman matrix entries are represented by the existing full S
entries minus the smooth remainder, never by omitting the singularity.
Uncertified smooth quadrature, inverse residuals and pairings are named
failures in the complete report. All arrays are preserved for inspection.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = B / 'frozen-reference-proposal-652'
TARGET = "Test C999's lower reference on C999y's exact three-dimensional obstruction space using complete inverse actions and the .000999 Euclidean-Gram threshold."

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

checks, pins, arrays = [], {}, {}
report = dict(target=TARGET, result='INCONCLUSIVE', certified=False,
              checks=checks, input_sha256=pins, failures=[],
              parameters=dict(delta='.01', m=286, J=14, beta='.219999',
                              raw_trial_modes=256, smooth_quadrature_nodes=512),
              threshold='.000999 times exact X*X',
              qualifications=['REPRODUCTION proposal; no numerical sign is a theorem',
                              'Retains analytic/IEEE754/Decimal/source-to-Xi/core/c_star contracts',
                              'Neither S3 nor RH decided'])

def ck(ok, label):
    checks.append(dict(check=label, passed=bool(ok)))
    if not ok:
        raise ValueError(label)

def pin(name, expected=None):
    pins[name] = sha(B / name)
    if expected is not None:
        ck(pins[name] == expected, 'pin ' + name)

try:
    audit = json.loads((B / 'neutral-reference-rank-audit-642.json').read_text())
    ck(not audit['failures'] and all(q['passed'] for q in audit['checks']),
       'saved audit642 checks, not a new analytic audit')
    pin('neutral-reference-rank-audit-642.json')
    for name, expected in audit['input_sha256'].items():
        pin(name, expected)
    rank = json.loads((B / 'neutral-reference-rank-obstruction-640.json').read_text())
    w = rank['witness']
    ck(w == audit['witness'], 'entire saved witness equals audited witness')
    ck(w['support_indices_zero_based'] == list(range(16)) + list(range(1022,1038))
       and w['denominator'] == 2**24 and w['ambient_dimension'] == 2044
       and w['omitted_coordinates'] == 'exactly zero', 'exact frozen support and scale')
    xi = np.asarray(w['integer_columns_by_row'], dtype=np.int64)
    ck(xi.shape == (32,3), 'all96 coordinates present')
    X = np.zeros((2044,3)); X[w['support_indices_zero_based']] = xi / 2**24
    # Read all entries, including both independent endpoint arrays.
    report['witness'] = w
    spec = importlib.util.spec_from_file_location('entries532', B/'residual-certificate-532.py')
    old = importlib.util.module_from_spec(spec); spec.loader.exec_module(old)
    with np.load(B/'original-galerkin-586.npz', allow_pickle=False) as z:
        M,T,Ts,U,Z = [z[k].copy() for k in
            ['local_matrix','t_entries','ts_entries','u_entries','neutral_coordinate_center']]
    orig = json.loads((B/'original-galerkin-586.json').read_text())
    pin('original-galerkin-586.npz', orig['archive']['sha256'])
    pin('original-galerkin-586.json')
    ck(np.array_equal(M,M.T) and np.array_equal(T,Ts.T), 'square orientations')
    ell = old.constants()['ell']; a = ell/2; N=256; m=286; J=14
    nn = np.arange(N); k=nn*np.pi/ell
    nu=np.full(N,np.sqrt(2/ell)); nu[0]=1/np.sqrt(ell)
    f=Z@X[:1022]; h=Z@X[1022:]
    forcing = T@f+Ts@h
    # Exact parity/reflection on a raw cosine: sqrt(2)*(-1)^n*e_n(t).
    # The sign is common within each parity block, but retained explicitly.
    xx,ww=leggauss(512); ts=(xx+1)*a/2; ws=ww*a/2
    basis=np.sqrt(2)*nu[:,None]*((-1.)**nn[:,None])*np.cos(k[:,None]*ts)
    edges=np.arange(m+1)*a/m; mids=(edges[:-1]+edges[1:])/2
    integrals=np.empty((N,m)); integrals[0]=a/m
    integrals[1:]=(np.sin(k[1:,None]*edges[1:])-np.sin(k[1:,None]*edges[:-1]))/k[1:,None]
    integrals*=np.sqrt(2)*nu[:,None]*((-1.)**nn[:,None])
    def smooth_kernel(s):
        return np.exp(-s/2)/(-np.expm1(-2*s))-1/(2*s)
    hh=smooth_kernel(ts[:,None]+ts[None,:])
    hm=smooth_kernel(mids[:,None]+mids[None,:])
    correction=np.zeros((N,N))
    # S_app-S=(h_m-h)-sum_{j>=14}E_j. The finite E suffix here is
    # only a proposal; its omitted infinite suffix is explicitly unpaid.
    for parity,eps in [(0,1),(1,-1)]:
        ix=np.flatnonzero(nn%2==parity); b=basis[ix]*ws
        block=integrals[ix]@hm@integrals[ix].T-b@hh@b.T
        for j in range(J,80):
            c=2*j+.5; bj=np.exp(-2*a*c)
            ph=b@np.exp(-c*ts); ps=b@np.exp(-c*(2*a-ts))
            block-=(eps*bj*np.outer(ph,ph)+np.outer(ps,ps)
                    +eps*np.outer(ph,ps)+eps*np.outer(ps,ph))/(1-eps*bj)
        correction[np.ix_(ix,ix)]=block
    correction=(correction+correction.T)/2
    Bfinite=M[:N,:N]+correction-.01*np.eye(N)
    z=Z[:N,:N-2]
    Br=z.T@Bfinite@z
    rhs=z.T@forcing[:N]
    Y=np.linalg.solve(Br,rhs)  # a proposal, not a certified inverse
    q=z@Y
    endpoints=f.T@M@f+h.T@M@h-h.T@U@f-f.T@U.T@h
    debt=rhs.T@Y
    comparison=(endpoints-debt+(endpoints-debt).T)/2-.000999*(X.T@X)
    finite_res=rhs-Br@Y
    # Full original output through1023 is inspected, but the B0 correction
    # outside the256 square and every further row remain unpaid.
    original_residual_first1024=forcing-M[:,:N]@q
    gram=X.T@X
    arrays.update(X=X, f_raw=f, h_raw=h, free_middle_dyadics=Y,
                  neutral_coordinate_center=z, middle_raw_center=q,
                  reference_square_center=Bfinite, correction_center=correction,
                  restricted_reference_center=Br, rhs_center=rhs,
                  endpoint_center=endpoints, inverse_pairing_center=debt,
                  comparison_center=comparison, euclidean_gram_center=gram,
                  original_residual_first1024=original_residual_first1024)
    vals,vecs=np.linalg.eigh(comparison)
    arrays['comparison_eigenvectors_diagnostic']=vecs
    report['diagnostic_only']=dict(comparison_matrix=comparison.tolist(),
        comparison_eigenvalues=vals.tolist(), euclidean_gram=gram.tolist(),
        restricted_reference_minimum=float(np.linalg.eigvalsh(Br)[0]),
        finite_linear_residual_fro=float(np.linalg.norm(finite_res)),
        middle_column_norms=np.linalg.norm(q,axis=0).tolist(),
        original_first1024_residual_column_norms=np.linalg.norm(original_residual_first1024,axis=0).tolist(),
        correction_norm_fro=float(np.linalg.norm(correction)))
    # Save the exact jump locations as computable expressions and all columns'
    # boundary values; these determine the forcing-data obligation.
    boundary_basis=np.vstack((nu[:18],nu[:18]*((-1.)**np.arange(18))))
    boundary_f=boundary_basis@f[:18]; boundary_h=boundary_basis@h[:18]
    events=[]
    for (n,p),dl,wt in zip(old.POWERS,old.constants()['deltas'],old.constants()['weights']):
        for which,delay,bc in [('T f',dl,boundary_f),('T* h',-dl,boundary_h)]:
            loc=-delay if delay<0 else ell-delay
            jump=wt*(bc[0] if delay<0 else -bc[1])
            events.append(dict(operator=which,prime_power=n,prime=p,
                x_over_ell_expression=(f'log({n})/ell-7' if which=='T f' and dl<0 else
                    f'log({n})/ell-6' if which=='T f' else
                    f'7-log({n})/ell' if -dl<0 else f'8-log({n})/ell'),
                location_center=float(loc/ell), jump_center=jump.tolist()))
    report['forcing_jump_diagnostic']=events
    arrays['endpoint_boundary_values_f']=boundary_f
    arrays['endpoint_boundary_values_h']=boundary_h
    report['failures'] += [
        'Smooth remainder quadrature and exponential suffix lack certified errors; reference square is a proposal only',
        'No Gaussian-rational step forcing with paid jump strips, suffix and projected-output error was constructed',
        'No full projected B0 residual, including singular output beyond mode255, was certified',
        'All nine inverse-pairing and endpoint/remote/coordinate arithmetic errors remain unpaid',
        'Neither a nonnegative lower matrix nor a negative upper direction is certified']
    ck(all(sha(B/name)==digest for name,digest in pins.items()), 'all original inputs unchanged')
except Exception as exc:
    report['failures'].append(type(exc).__name__+': '+str(exc))
archive=OUT.with_suffix('.npz'); np.savez_compressed(archive,**arrays)
report['archive']=dict(path=str(archive.relative_to(ROOT)),sha256=sha(archive))
report['script_sha256']=sha(Path(__file__))
out=OUT.with_suffix('.json');out.write_text(json.dumps(report,indent=2)+'\n')
print('Result:',report['result'],'(diagnostic only)')
if 'diagnostic_only' in report:
    print('Proposed difference eigenvalues:',report['diagnostic_only']['comparison_eigenvalues'])
    print('Actual certified lower bound: unavailable. Required: nonnegative against .000999 X*X.')
    print('Finite solve residual:',report['diagnostic_only']['finite_linear_residual_fro'],
          '; complete inverse residual: unpaid')
print('Failures:',*report['failures'],sep='\n- ')
print('Complete report:',out.relative_to(ROOT));print('Complete arrays:',archive.relative_to(ROOT))
