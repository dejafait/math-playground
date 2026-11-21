"""Nonrigorous diagnostics for the step-181 exact resolvent target.

All sampled values are retained in the JSON output. They are not a
certificate of convergence, a tail bound, or absence of zeros.
"""
import json
from pathlib import Path

from decimal import Decimal as D, getcontext

getcontext().prec = 400
A, U, alpha = D(27)/10, D(121)/64, D(11)/8
omega = A * ((D(9)/5).ln()-D(4)/5+D(121)/100*(D(201)/121).ln())

class C:
    def __init__(self, r=0, i=0):
        if isinstance(r, C):
            self.r, self.i = r.r, r.i
        else:
            self.r, self.i = D(r), D(i)
    def __add__(self, other):
        other = C(other)
        return C(self.r+other.r, self.i+other.i)
    __radd__ = __add__
    def __neg__(self):
        return C(-self.r, -self.i)
    def __sub__(self, other):
        return self + (-C(other))
    def __mul__(self, other):
        other = C(other)
        return C(self.r*other.r-self.i*other.i,
                 self.r*other.i+self.i*other.r)
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = C(other)
        den = other.r*other.r+other.i*other.i
        return C((self.r*other.r+self.i*other.i)/den,
                 (self.i*other.r-self.r*other.i)/den)
    def __abs__(self):
        return (self.r*self.r+self.i*self.i).sqrt()

def exp(z):
    z = C(z)
    term, total = C(1), C(1)
    for k in range(1, 2000):
        term = term*C(0, z.i)/k
        total = total+term
        if abs(term) < D(10)**(-getcontext().prec-5):
            return total*z.r.exp()
    raise RuntimeError('Taylor cutoff exhausted')

def polyval(coeff, z):
    value = C(0)
    for a in reversed(coeff):
        value = value*z+a
    return value

u = C(D(3)/10, D(4)/10)

def encode(z):
    return {"real": format(z.r, '.50g'), "imag": format(z.i, '.50g')}

rows = []
for n in (15, 63, 255):
    getcontext().prec = n+100
    coeff = []
    choose = D(1)
    for j in range(n):
        value = choose*(-1)**j
        for k in range(1, n):
            value *= 1-D(j)*k/(U*n*n)
        coeff.append(value)
        choose = choose*(n-1-j)/(j+1)
    num_coeff = [C(coeff[j])/(alpha+u*D(j)/n) for j in range(n)]
    deriv_coeff = [j*coeff[j] for j in range(n)]
    for offset in (-D(1)/3000, D(0), D(1)/3000):
        v = omega + offset
        z = exp(-u*v/A)
        den = polyval(coeff, z)
        num = polyval(num_coeff, z)
        t = polyval(deriv_coeff, z)/(n*den)
        radial = []
        for s in (D(0), D(1)/10, D(1)/2, D(1), D(2), D(4)):
            zs = z*(-s).exp()
            hs = polyval(coeff, zs)
            ts = polyval(deriv_coeff, zs)/(n*hs)
            radial.append({"s": str(s), "T_n": encode(ts),
                           "phase_real": format(-(C(alpha)/u).r*s
                                                 + abs(hs/den).ln()/n, '.50g')})
        rows.append({"n": n, "offset": str(offset), "v": format(v, '.50g'),
                     "z": encode(z), "Q_n": encode(num/den), "T_n": encode(t),
                     "local_guess": encode(C(1)/(alpha+u*t)), "radial": radial})

out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps({"status": "NONRIGOROUS_DIAGNOSTIC",
                          "required": "Uniform nonzero limit and full-tail proof",
                          "omega": format(omega, '.50g'), "rows": rows,
                          "failures": ["No interval certification or uniform tail bound"]},
                         indent=2)+'\n')
for row in rows:
    if row['offset'] == '0':
        print(f"n={row['n']}: Q={row['Q_n']}; local guess={row['local_guess']}")
print("Required: uniform nonzero limit and full-tail proof; diagnostic only.")
print(f"Evidence: {out}")
