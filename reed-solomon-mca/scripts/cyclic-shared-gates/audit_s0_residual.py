"""Bridge the displayed L094 witness to every saved polynomial and label.

Reuses the reviewed verifier's quotient arithmetic, independently of the
producer. The uniform seed argument remains the written proof in L094.
"""
import hashlib
import json
from pathlib import Path
import verify_s0_residual as v


class K:
    def __init__(self, x):
        self.v = x.v if isinstance(x, K) else v.field(x)

    def __add__(self, y):
        return K(v.add(self.v, K(y).v))

    __radd__ = __add__

    def __neg__(self):
        return K(v.neg(self.v))

    def __sub__(self, y):
        return self + -K(y)

    def __rsub__(self, y):
        return K(y) + -self

    def __mul__(self, y):
        return K(v.mul(self.v, K(y).v))

    __rmul__ = __mul__

    def __truediv__(self, y):
        return K(v.div(self.v, K(y).v))

    def __eq__(self, y):
        return self.v == K(y).v


def trim(p):
    p = [K(x) for x in p]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    return trim([(p[i] if i < len(p) else K(0)) +
                 (q[i] if i < len(q) else K(0))
                 for i in range(max(len(p), len(q)))])


def scale(p, x):
    return trim([K(x)*a for a in p])


def mul(p, q):
    r = [K(0)]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i+j] = r[i+j]+a*b
    return trim(r)


def at(p, x):
    r = K(0)
    for a in reversed(p):
        r = r*x+a
    return r


def main():
    # This completes the modulus certification before any field division here.
    v.main()
    base = Path(__file__).parent
    data = json.loads((base/'s0-residual-certificate.json').read_text())
    before = json.loads((base.parents[1]/'drafts/2026-10-16-cyclic-unused-s0-audit-before.json').read_text())
    unchanged = {name: hashlib.sha256((base.parents[1]/name).read_bytes()).hexdigest() == digest
                 for name, digest in before.items()}
    assert all(unchanged.values())
    c, d, e, g = K(2), K(3), K(4), K([0, 1])
    x = K([50,22,50,60,67,77,30,42,14,85,39,8,43])
    j = c*(1-g)/(1-c)
    k = (d*e+g*j-d*(g+j))/(e-d)
    ell = c-k
    t = j*(j-g)*(k-d)/((j-c)*(j-d)*(k-g))
    u = j*(1-t)
    alpha, beta, gamma = e*(k-1), k-e, k*(e-1)
    Y, Q = [u,t], [gamma*u,beta*u+gamma*t-alpha,beta*t]
    M = [k*c,-k]
    N = scale(add([g*ell],scale(M,-1)), d*e)
    O = add(scale(add([(d+e)*ell],scale(M,-1)),g),[-d*e*ell])
    A, B, C2 = [c+d-j,K(-1)], [-c*d,j], [c*d*j,c*d-j*(c+d)]
    Z = scale(add(mul(B,N),mul(C2,O)),-1)
    W = add(mul(A,N),mul(B,O))
    U = add(scale(add([j-k],scale(Y,1-j)),ell),scale(M,k-1))
    V = add(scale(mul(Y,add(M,[ell*(k-1)])),j),
            scale(mul(M,add([1-j],scale(Y,-1))),k))
    E = add(mul(Z,U),mul(W,V))
    P = add(scale(mul(add(Y,[K(0),K(-1)]),add(Z,scale(W,-c))),d*(d-g)*(d-j)),
            scale(mul(mul(mul(add(Z,scale(W,-j)),[-g,K(1)]),[K(0),K(1)]),
                      add([d],scale(Y,-1))),d-c))
    polynomials = dict(Q=Q,M=M,N=N,O=O,Z=Z,W=W,E=E,P=P)
    saved = {name:trim([K(v.evaluate_rat(a,g.v)) for a in p])
             for name,p in data['polynomials'].items()}
    assert all(trim(p) == saved[name] for name,p in polynomials.items())
    for name, remainder in [('E','rho'),('P','sigma')]:
        assert add(mul(saved[name+'_quotient'],Q),saved[remainder]) == trim(polynomials[name])
        assert len(saved[remainder]) <= 2
    a,b = -Q[1]/Q[2], -Q[0]/Q[2]
    pp = P+[K(0)]*(6-len(P))
    sigma = [pp[0]+b*pp[2]+a*b*pp[3]+(a*a*b+b*b)*pp[4]+(a*a*a*b+2*a*b*b)*pp[5],
             pp[1]+a*pp[2]+(a*a+b)*pp[3]+(a*a*a+2*a*b)*pp[4]+(a*a*a*a+3*a*a*b+b*b)*pp[5]]
    assert trim(sigma) == saved['sigma']
    y,m,n,z = at(Y,x),at(M,x)/ell,at(N,x)/at(O,x),at(Z,x)/at(W,x)
    h4 = (y*(z+x-g)-z*x)/(y-g)
    a4,b4,c4 = e+h4-j-m,j*m-e*h4,e*h4*(j+m)-j*m*(e+h4)
    h13 = (-b4*x-c4)/(a4*x+b4)
    labels = {1:c,2:d,3:e,4:h4,5:K(1),6:z,7:K(0),8:x,9:g,10:j,11:n,12:m,13:h13,14:k,15:y}
    assert set(data['witness']['labels']) == {str(i) for i in labels}
    assert all(value == data['witness']['labels'][str(i)] for i,value in labels.items())
    assert len({None} | {value.v for value in labels.values()}) == 16
    denominators = [1-c,e-d,j-c,j-d,k-g,ell,Q[2],beta*x+gamma,
                    at(O,x),at(W,x),y-g,a4*x+b4,x,d-y,d-g,d-j,z-c]
    assert all(value != 0 for value in denominators)
    assert at(Q,x) == 0 and at(E,x) == 0
    expected_p = K([43,91,81,29,68,91,14,55,15,24,47,42,63])
    expected_s0 = K([87,19,21,78,62,13,4,13,9,10,71,26,6])
    s0 = y*(d-x)/(x*(d-y))+(d-c)*(z-j)*(x-g)/((d-g)*(d-j)*(z-c))-1
    assert at(P,x) == expected_p and s0 == expected_s0 and s0 != 0
    clearing = x*(d-y)*(d-g)*(d-j)*(at(Z,x)-c*at(W,x))
    assert clearing != 0 and clearing*s0 == expected_p
    expected_gates = {'rho1','q2','ell','O_at_X','W_at_X','D15_pole',
                      'D0_pole','D4_pole','delta_den','psi_den'}
    expected_gates |= {f'finite_{i}' for i in labels}
    expected_gates |= {f'difference_{i}_{j}' for i in labels for j in labels if i<j}
    assert set(data['reconstruction_gates']) == expected_gates
    bound = dict(actual_P_degree=len(trim(P))-1,required_P_degree_max=5,
                 actual_remainder_degree=max(len(saved['rho']),len(saved['sigma']))-1,
                 required_remainder_degree_max=1)
    assert bound == data['bound']
    result = dict(scope='Complete displayed-witness bridge; no uniform finite-seed claim',
                  unchanged_original_artifacts=unchanged,polynomial_coefficients={name:[list(a.v) for a in p] for name,p in polynomials.items()},
                  reconstructed_labels={str(i):list(a.v) for i,a in labels.items()},
                  explicit_denominators=[list(a.v) for a in denominators],
                  expected_gate_names=sorted(expected_gates),gate_count=len(expected_gates),
                  bound=bound,P_at_X=list(expected_p.v),S0_minus_one=list(s0.v),
                  clearing=list(clearing.v),failures=[],H_assignments_tested=0,rank_tests=0)
    out = base/'s0-critical-audit.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(bound=bound,gate_count=len(expected_gates),unchanged_original_artifacts=unchanged,failures=[])))
    print('Complete displayed-witness bridge:',out)


if __name__ == '__main__':
    main()
