"""Non-certified quadrature probe; no RH or Laguerre-sign certificate."""
import math


def logadd(xs):
    m = max(xs)
    return m + math.log(sum(math.exp(x-m) for x in xs))


def run(h):
    # Whole-line even moments; tail u>4 and theta indices >8 omitted.
    us = [i*h for i in range(1, round(4/h))]
    lk = []
    for u in us:
        terms = []
        for j in range(1, 9):
            v = math.pi*j*j*math.exp(2*u)
            terms.append(math.log(4*v*(2*v-3))+u/2-v)
        lk.append(logadd(terms))
    moments = {}
    for p in range(0, 516, 2):
        vals = [l+p*math.log(u) for l,u in zip(lk,us)]
        if p == 0:
            k0 = sum(4*math.pi*j*j*(2*math.pi*j*j-3)*math.exp(-math.pi*j*j) for j in range(1,9))
            vals.append(math.log(k0/2))
        moments[p] = math.log(2*h)+logadd(vals)
    def lc(n,j):
        return math.lgamma(n+1)-math.lgamma(j+1)-math.lgamma(n-j+1)
    for n in (1,4,16,64,128,256):
        den = logadd([lc(2*n,j)+moments[j]+moments[2*n-j] for j in range(0,2*n+1,2)])
        pos = logadd([lc(2*n,j)+moments[j+2]+moments[2*n-j] for j in range(0,2*n+1,2)])
        neg = logadd([lc(2*n,j)+moments[j+1]+moments[2*n-j+1] for j in range(1,2*n,2)])
        variance = (math.exp(pos-den)-math.exp(neg-den))/2
        print(f'h={h:g} n={n:3} variance={variance:.10g} sufficient_abs_a={1/math.sqrt(2*variance):.8g}')

if __name__ == '__main__':
    run(0.002)
    run(0.001)
