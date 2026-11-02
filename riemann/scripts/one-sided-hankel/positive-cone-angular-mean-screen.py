"""Finite signed-mean diagnostic, NOT a rigorous/asymptotic certificate.

Uses only the Python standard library. Decimal precision replay detects
instability but supplies no interval enclosure. Saves all signed residues.
"""
import argparse
import cmath
from decimal import Decimal as D, getcontext
import json
import math
from pathlib import Path


class Z:
    def __init__(self, re=0, im=0):
        self.re, self.im = D(re), D(im)

    @staticmethod
    def cast(z):
        return z if isinstance(z, Z) else Z(z)

    def __add__(self, other):
        z = self.cast(other)
        return Z(self.re+z.re, self.im+z.im)

    __radd__ = __add__

    def __neg__(self):
        return Z(-self.re, -self.im)

    def __sub__(self, other):
        return self+-self.cast(other)

    def __rsub__(self, other):
        return self.cast(other)+-self

    def __mul__(self, other):
        z = self.cast(other)
        return Z(self.re*z.re-self.im*z.im, self.re*z.im+self.im*z.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        z = self.cast(other)
        den = z.re*z.re+z.im*z.im
        return Z((self.re*z.re+self.im*z.im)/den,
                 (self.im*z.re-self.re*z.im)/den)

    def __rtruediv__(self, other):
        return self.cast(other)/self

    def abs(self):
        return (self.re*self.re+self.im*self.im).sqrt()

    def data(self):
        return [str(self.re), str(self.im)]


def atan(v):
    power, total, k = v, v, 1
    while True:
        power *= -v*v
        fresh = total+power/D(2*k+1)
        if fresh == total:
            return fresh
        total, k = fresh, k+1


def nodes(q):
    pi = 16*atan(D(1)/5)-4*atan(D(1)/239)
    result = []
    for k in range(2*q):
        s = D(k)+D(1)/2
        for _ in range(20):
            f = s-k-D(1)/2-atan(1/(10*s))/pi
            ds = f/(1+10/(pi*(1+100*s*s)))
            fresh = s-ds
            if abs(ds) < D(10)**(-getcontext().prec+5):
                s = fresh
                break
            s = fresh
        result.append(s)
    return result


def W(a, u, n):
    x, U = -D(5)/4, D(121)/64
    out = x/a
    for j in range(1, n):
        t = D(j)/n
        out *= (x-t*u)/(a-t*u)*(U*u-t*a)/(U*u-t*x)
    return out


def run(q, precision):
    getcontext().prec = precision
    n = 12*q+3
    x, U, h = -D(5)/4, D(121)/64, D(27)/(10*n)
    v = Z(-D(99)/101, D(20)/101)
    ss = nodes(q)
    ys = [h*s for s in ss]
    rows, mean = [], D(1)
    for k, y in enumerate(ys):
        a = Z(x, y)
        ell = D(1)/2
        for l, yl in enumerate(ys):
            if l != k:
                ell *= yl*yl/(yl*yl-y*y)
        gauge = (W(a, v, n).abs()*W(Z(x, -y), v, n).abs()).sqrt()
        b = abs(ell)*(1+100*ss[k]*ss[k]).sqrt()/gauge
        residues, angular_mean = [], x/a
        for j in range(1, n):
            tj = D(j)/n
            pj = tj*x/U
            res = (x-a)/a
            for l in range(1, n):
                tl = D(l)/n
                res *= (x-tl*pj)/(a-tl*pj)
                if l != j:
                    res *= (tj*x-tl*a)/(x*(tj-tl))
            residues.append(res.data())
            angular_mean += res
        contribution = 2*b*angular_mean.re
        mean += contribution
        rows.append(dict(k=k, s=str(ss[k]), y=str(y), ell=str(ell),
                         gauge=str(gauge), b=str(b),
                         W_at_zero=(x/a).data(), residues=residues,
                         W_angular_mean=angular_mean.data(),
                         paired_mean_contribution=str(contribution)))
    continued = 1+sum(2*D(r['b'])*D(r['W_at_zero'][0]) for r in rows)
    absolute_sum = 1+sum(abs(D(r['paired_mean_contribution'])) for r in rows)
    return dict(q=q, n=n, precision=precision, mean=str(mean),
                apparent_rate=str(-abs(mean).ln()/n),
                normalized_loss=str((-abs(mean).ln()-D(n)/100)/D(n).ln()),
                continued_value_at_zero=str(continued),
                absolute_sum_of_paired_means=str(absolute_sum), nodes=rows)


def trapezoid(row, count):
    n, x, U = row['n'], -1.25, 121/64
    values = []
    for j in range(count):
        u = cmath.exp(2j*math.pi*j/count)
        residual = 1+0j
        for r in row['nodes']:
            y, b = float(r['y']), float(r['b'])
            for sign in (-1, 1):
                a = complex(x, sign*y)
                w = x/a
                for l in range(1, n):
                    t = l/n
                    w *= (x-t*u)/(a-t*u)*(U*u-t*a)/(U*u-t*x)
                residual += b*w
        values.append(residual)
    mean = complex(math.fsum(v.real for v in values)/count,
                   math.fsum(v.imag for v in values)/count)
    norm = math.sqrt(math.fsum(abs(v)**2 for v in values)/count)
    return dict(count=count, mean=[mean.real, mean.imag], sampled_L2=norm,
                difference_from_residue=abs(mean-float(row['mean'])),
                qualification='Double precision trapezoid, no alias/roundoff enclosure')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--q', type=int, nargs='+', default=[1, 2, 4, 8, 16])
    parser.add_argument('--precision', type=int, nargs='+', default=[80, 140])
    parser.add_argument('--output', type=Path, default=Path(__file__).with_suffix('.json'))
    args = parser.parse_args()
    report = dict(status='NUMERICAL DIAGNOSTIC ONLY; NOT A RIGOROUS CERTIFICATE',
                  required_asymptotic_rate='Strictly below 0.01 for a mean lower bound',
                  failures=['No rounding enclosure or uniform asymptotic estimate'], cases=[])
    for q in args.q:
        runs = [run(q, p) for p in args.precision]
        final = runs[-1]
        difference = abs(D(runs[0]['mean'])-D(final['mean']))
        case = dict(q=q, n=final['n'], precision_runs=runs,
                    precision_difference=str(difference))
        if q <= 4:
            case['trapezoid'] = [trapezoid(final, m) for m in (512, 1024)]
        report['cases'].append(case)
        args.output.write_text(json.dumps(report, indent=2)+'\n')
        print('n=%d mean=%+.12g apparent_rate=%.9g precision_difference=%s' %
              (final['n'], float(final['mean']), float(final['apparent_rate']),
               difference), flush=True)
    print('Required asymptotic rate <0.01; failures:', report['failures'])
    print('Full diagnostic:', args.output)


if __name__ == '__main__':
    main()
