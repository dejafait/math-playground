"""Bounded symbolic joint-residual attempt; Python 2.7 / SymPy 0.7.4.1.

No field-label assignments or ranks are enumerated. Intermediate exact
polynomials are saved before subsequent, potentially expensive operations.
An unfinished computation supplies no mathematical exclusion.
"""
from __future__ import print_function
import json
import os
import sys
import signal
from sympy import GF
from sympy.polys.fields import field
from sympy.polys.rings import ring

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, 'joint-generic-elimination.json')
K, c, d, e, g = field('c,d,e,g', GF(97))
R, X = ring('X', K.to_domain())
result = dict(scope='Symbolic F_97(c,d,e,g)[X], no H assignments or rank tests',
              attempt_status='INCOMPLETE',
              variables=['c','d','e','g'], completed_stages=[],
              polynomials={}, failures=[], unresolved=['uniform joint exclusion',
              'rho=0 branch', 'all-zero residual branch', 'actual H restrictions'],
              H_assignments_tested=0, rank_tests=0)


def polydata(p):
    return [[list(m), int(a) % 97] for m, a in sorted(p.terms())]


def ratdata(a):
    return dict(numerator=polydata(a.numer), denominator=polydata(a.denom))


def save(stage, values):
    for name, value in values.items():
        if hasattr(value, 'numer'):
            result['polynomials'][name] = ratdata(value)
        else:
            result['polynomials'][name] = [[i[0][0], ratdata(i[1])]
                                           for i in sorted(value.terms())]
    result['completed_stages'].append(stage)
    with open(PATH, 'w') as out:
        json.dump(result, out, sort_keys=True, indent=2)
        out.write('\n')
    print('Saved stage %s: %s' % (stage, PATH))
    print('Bounds: %s; failures: %s; status: %s' %
          (result.get('bounds', {}), result['failures'], result['attempt_status']))
    sys.stdout.flush()


def main():
    j = c*(1-g)/(1-c)
    k = (d*e+g*j-d*(g+j))/(e-d)
    ell = c-k
    t = j*(j-g)*(k-d)/((j-c)*(j-d)*(k-g))
    u = j*(1-t)
    alpha, beta, gamma = e*(k-1), k-e, k*(e-1)
    Q = R(beta*t)*X**2+R(beta*u+gamma*t-alpha)*X+R(gamma*u)
    result['bounds'] = dict(actual_Q_degree=Q.degree(),required_Q_degree=2)
    save('quadratic', dict(j=j,k=k,ell=ell,t=t,u=u,Q=Q))
    Y = R(t)*X+R(u)
    M = R(k)*(R(c)-X)
    N = R(d*e)*(R(g*ell)-M)
    O = R(g)*(R((d+e)*ell)-M)-R(d*e*ell)
    A = R(c+d-j)-X
    B = R(j)*X-R(c*d)
    C2 = R(c*d)*(X+R(j))-R(j*(c+d))*X
    Z, W = -B*N-C2*O, A*N+B*O
    U = R(ell)*(R(j-k)+R(1-j)*Y)+R(k-1)*M
    V = R(j)*Y*(M+R(ell*(k-1)))+R(k)*M*(R(1-j)-Y)
    E = Z*U+W*V
    P = R(d*(d-g)*(d-j))*(Y-X)*(Z-R(c)*W)+R(d-c)*(Z-R(j)*W)*(X-R(g))*X*(R(d)-Y)
    save('cleared gates', dict(E=E,P=P,O=O,W=W))
    eq, er = E.div(Q)
    pq, pr = P.div(Q)
    assert eq*Q+er == E and pq*Q+pr == P
    rho0, rho1 = er.get((0,),K.zero), er.get((1,),K.zero)
    sigma0, sigma1 = pr.get((0,),K.zero), pr.get((1,),K.zero)
    result['bounds'] = dict(actual_E_degree=E.degree(),required_E_degree_max=4,
                          actual_P_degree=P.degree(),required_P_degree_max=5,
                          actual_residual_degree=max(er.degree(),pr.degree()),
                          required_residual_degree_max=1)
    save('exact division',dict(E_quotient=eq,P_quotient=pq,
                              rho0=rho0,rho1=rho1,sigma0=sigma0,sigma1=sigma1))
    delta = Q[(2,)]*rho0**2-Q[(1,)]*rho0*rho1+Q[(0,)]*rho1**2
    psi = rho1*sigma0-rho0*sigma1
    save('joint seed polynomials',dict(Delta=delta,Psi=psi))
    print('No uniform exclusion established. Full certificate: '+PATH)


if __name__ == '__main__':
    def stop(signum, frame):
        raise KeyboardInterrupt('120-second symbolic expansion limit')
    signal.signal(signal.SIGALRM, stop)
    signal.alarm(120)
    try:
        main()
    except KeyboardInterrupt:
        result['failures'].append('Expansion interrupted before joint factor test; no exclusion certificate')
        save('interrupted', {})
    finally:
        signal.alarm(0)
