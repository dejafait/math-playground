#!/usr/bin/env python3
"""Diagnostic only: frozen 512-mode Schur residual with a finite covariance.

No sign claim: floating arithmetic, omitted complementary modes, and
phase gaps are not certified here. Full matrices and vectors are saved.
"""
import json
from pathlib import Path
import numpy as np

FOLDER = Path(__file__).parent
N, K, PENALTY, TAU = 512, 4096, 256, 1.43


def psi_pair(z):
    z = np.asarray(z, dtype=complex)
    w = z + 32
    p = np.log(w) - .5/w
    dp = 1/w + .5/w**2
    for j, b in enumerate([1/6, -1/30, 1/42, -1/30, 5/66,
                            -691/2730, 7/6, -3617/510], 1):
        p -= b/(2*j*w**(2*j))
        dp += b/w**(2*j+1)
    for j in range(32):
        p -= 1/(z+j)
        dp += 1/(z+j)**2
    return p, dp


def build():
    ell = np.log(3.)/2
    n = np.arange(K)
    k = n*np.pi/ell
    norm = np.full(K, np.sqrt(2/ell)); norm[0] = 1/np.sqrt(ell)
    parity = (-1.)**n
    p, dp = psi_pair(.25+.5j*k)
    h = p.real - np.log(np.pi)
    # sum_j c_j^2/[(c_j^2+k_n^2)(c_j^2+k_m^2)]
    b = k*p.imag/2
    den = k[:, None]**2 - k[None, :N]**2
    den[np.arange(N), np.arange(N)] = 1
    s = (b[:, None]-b[None, :N])/den
    diag = np.empty(N)
    diag[0] = dp[0].real/4
    diag[1:] = p[1:N].imag/(4*k[1:N])+dp[1:N].real/8
    s[np.arange(N), np.arange(N)] = diag
    for j in range(64):
        c = 2*j+.5
        v = c/(c*c+k*k)
        s -= np.exp(-ell*c)*np.outer(parity*v, v[:N])
    same = parity[:, None] == parity[None, :N]
    s *= 2*np.outer(norm, norm[:N])*same

    powers = [(29,29),(31,31),(32,2),(37,37),(41,41),(43,43),
              (47,47),(49,7),(53,53),(59,59),(61,61),(64,2),
              (67,67),(71,71),(73,73),(79,79)]
    nn, mm = k[:, None], k[None, :N]
    scale = np.outer(norm, norm[:N])
    def translation(delta):
        lo, hi = max(0., -delta), min(ell, ell-delta)
        length, mid = hi-lo, (hi+lo)/2
        return scale*length/2*(
            np.cos((nn-mm)*mid-mm*delta)*np.sinc((nn-mm)*length/(2*np.pi))
            +np.cos((nn+mm)*mid+mm*delta)*np.sinc((nn+mm)*length/(2*np.pi)))
    t, tt = np.zeros_like(s), np.zeros_like(s)
    for power, prime in powers:
        delta, weight = 7*ell-np.log(power), np.log(prime)/np.sqrt(power)
        t += weight*translation(delta)
        tt += weight*translation(-delta)
    for j in range(1, 8):
        c = 2*j+.5
        minus = norm*c*(1-parity*np.exp(-c*ell))/(c*c+k*k)
        plus = norm*c*(parity-np.exp(-c*ell))/(c*c+k*k)
        t += np.exp(-6*ell*c)*np.outer(minus, plus[:N])
        tt += np.exp(-6*ell*c)*np.outer(plus, minus[:N])
    moments = np.array([norm*c*(parity*np.exp(c*ell)-1)/(c*c+k*k)
                        for c in [.5, -.5]])
    w0 = s + PENALTY*moments.T@moments[:, :N]
    wc, wg = (t+tt)/2, (t-tt)/2
    m0 = w0[:N].copy(); m0[np.arange(N),np.arange(N)] += h[:N]
    mc, mg = wc[:N], wg[:N]
    f0, fc, fg = w0[N:], wc[N:], wg[N:]
    cov00, covcc, covgg = f0.T@f0, fc.T@fc, fg.T@fg
    v = f0.T@fc; cov0c = v+v.T
    v = f0.T@fg; cov0g = v-v.T
    v = fc.T@fg; covcg = v-v.T
    return dict(m0=m0, mc=mc, mg=mg, cov00=cov00, covcc=covcc,
                covgg=covgg, cov0c=cov0c, cov0g=cov0g, covcg=covcg,
                f0=f0, fc=fc, fg=fg, moments=moments, response=s)


def main():
    data = build()
    matrix_path = FOLDER/'residual-matrices-532.npz'
    np.savez_compressed(matrix_path, **data)
    samples, least, least_vector = [], float('inf'), None
    for theta in np.linspace(0, np.pi, 17):
        c, s = np.cos(theta), np.sin(theta)
        matrix = (data['m0']+c*data['mc']+1j*s*data['mg']
                  -(data['cov00']+c*c*data['covcc']+s*s*data['covgg']
                    +c*data['cov0c']+1j*s*data['cov0g']
                    +1j*c*s*data['covcg'])/TAU)
        values, vectors = np.linalg.eigh(matrix)
        val = float(values[0])
        samples.append({'theta':float(theta), 'minimum_eigenvalue':val})
        if val < least:
            least, least_vector = val, vectors[:,0]
        print(f'Diagnostic phase {theta:.6f}: residual minimum {val:.9f}',flush=True)
    vector_path = FOLDER/'residual-least-vector-532.npz'
    np.savez_compressed(vector_path, vector=least_vector)
    result = dict(certified=False, parameters=dict(N=N,K=K,penalty=PENALTY,tau=TAU),
                  samples=samples, least_sampled_value=least,
                  required_full_uniform_lower_bound=0,
                  finite_covariance_frobenius_norms={key:float(np.linalg.norm(data[key]))
                                                    for key in ['f0','fc','fg']},
                  files=[str(matrix_path), str(vector_path)],
                  failures=['infinite covariance beyond K omitted',
                            'floating arithmetic and special functions',
                            'phase gaps unbounded'],
                  full_inequality_certified=False)
    path=FOLDER/'residual-locator-532.json'
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(f'DIAGNOSTIC ONLY: actual sampled minimum {least}; required complete uniform bound 0. Evidence {path}',flush=True)


if __name__ == '__main__':
    main()
