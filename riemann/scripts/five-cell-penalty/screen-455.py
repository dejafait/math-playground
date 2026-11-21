"""Float witness search inside the fixed 4096-mode, 128-response test.

This is a diagnostic, not a sign certificate. Every matrix entry is from
the complete bounded part, including all nine active prime powers and
all ten unnormalized physical cell moments. No Schur-tail payment is
asserted. Outputs preserve eigenvectors for a separate rigorous check.
"""
import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
ELL = math.log(3) / 2
A = 2.5 * ELL
L = 2 * A
PRIMES = [(2, 2), (3, 3), (4, 2), (5, 5), (7, 7), (8, 2), (9, 3), (11, 11), (13, 13)]


def digamma(z):
    z = np.asarray(z, dtype=complex)
    w = z + 32
    ans = np.log(w) - 0.5 / w
    for n, b in enumerate([1/6, -1/30, 1/42, -1/30, 5/66, -691/2730, 7/6, -3617/510], 1):
        ans -= b / (2*n*w**(2*n))
    for j in range(32):
        ans -= 1/(z+j)
    return ans


def build(parity, count):
    q = np.arange(count)
    k = (q + (0 if parity == 1 else .5))*math.pi/A
    half_norm = np.full(count, math.sqrt(2/A))
    if parity == 1:
        half_norm[0] = 1/math.sqrt(A)
    full_norm = half_norm/math.sqrt(2)
    d = digamma(.25+.5j*k).real-math.log(math.pi)
    matrix = np.diag(d)
    pp, qq = k[:, None], k[None, :]
    for n, p in PRIMES:
        delay = math.log(n)
        half = A-delay/2
        first = np.sinc((pp-qq)*half/math.pi)*np.cos((pp+qq)*delay/2)
        second = np.sinc((pp+qq)*half/math.pi)*np.cos((pp-qq)*delay/2)
        overlap = half*(first+parity*second)*full_norm[:, None]*full_norm[None, :]
        matrix -= 2*math.log(p)/math.sqrt(n)*overlap
    c = 2*np.arange(128)+.5
    responses = (half_norm[:, None]*(-1.)**q[:, None]*c[None, :]
                 *np.sqrt(1-parity*np.exp(-2*A*c))[None, :]
                 /(k[:, None]**2+c[None, :]**2))
    matrix += responses@responses.T
    pole = responses[:, 0]*math.exp(A/2)*math.sqrt(1-parity*math.exp(-A))
    matrix += parity*np.outer(pole, pole)
    moments = []
    for cell in range(5):
        center = (cell-2)*ELL
        left, right = center-ELL/2, center+ELL/2
        for sigma in [1, -1]:
            b = sigma/2
            def primitive(x):
                if parity == 1:
                    trig = b*np.cos(k*x)+k*np.sin(k*x)
                else:
                    trig = b*np.sin(k*x)-k*np.cos(k*x)
                return np.exp(b*(x-center))*trig/(b*b+k*k)
            moments.append(full_norm*(primitive(right)-primitive(left)))
    moments = np.asarray(moments)
    matrix += 256*moments.T@moments
    return matrix, moments, d


def main():
    result = {"status": "FLOAT_SCREEN_ONLY", "parameters": {"K":5, "penalty":256,
        "responses":128, "retained_modes_per_parity":4096, "covariance_prefix_end":16384},
        "a": A, "ell": ELL, "active_prime_powers": [n for n,p in PRIMES], "screens": []}
    for count in [64, 128, 256]:
        for parity in [1, -1]:
            matrix, moments, d = build(parity, count)
            eig, vec = np.linalg.eigh(matrix)
            v = vec[:, 0]
            entry = {"parity":parity, "dimension":count, "minimum_eigenvalue_float":float(eig[0]),
                     "rayleigh_float":float(v@matrix@v), "vector":v.tolist(),
                     "moments_float":(moments@v).tolist(),
                     "symmetry_error":float(np.max(np.abs(matrix-matrix.T)))}
            result["screens"].append(entry)
            print(f"parity={parity:+d} screen={count} lower-comparison Rayleigh={entry['rayleigh_float']:.12g}; required >0; FLOAT ONLY")
        if any(s['rayleigh_float'] < -1e-9 for s in result['screens']):
            break
    rho = sum(2*math.log(p)/math.sqrt(n)*math.cos(math.pi/(math.ceil(L/math.log(n))+1)) for n,p in PRIMES)
    result['complement_screen'] = {'C_nr_float':rho, 'parities':[]}
    for parity in [1,-1]:
        k=(4096+(0 if parity==1 else .5))*math.pi/A
        odd=0 if parity==1 else 2*(math.sinh(A)-A)
        t=float(digamma(.25+.5j*k).real-math.log(math.pi)-rho-odd)
        result['complement_screen']['parities'].append({'parity':parity,'t4096_float':t})
        print(f"parity={parity:+d} complement-floor screen={t:.12g}; required >0; FLOAT ONLY")
    path=ROOT/'screen-455.json'
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(f"Full diagnostic and witness coefficients: {path}")


if __name__ == '__main__':
    main()
