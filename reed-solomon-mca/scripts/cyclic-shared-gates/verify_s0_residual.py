"""Independent direct-gate replay of the one algebraic S_0 witness."""
import hashlib
import json
from pathlib import Path

P = 97
F = [24,15,13,48,60,8,80,67,51,21,15,1,48,1]
N = 13
ZERO = (0,)*N
ONE = (1,)+(0,)*(N-1)


def field(value):
    if isinstance(value,int):
        value = [value]
    coeff = [a % P for a in value]+[0]*max(0,N-len(value))
    for i in range(len(coeff)-1,N-1,-1):
        leading = coeff[i]
        for j in range(N):
            coeff[i-N+j] = (coeff[i-N+j]-leading*F[j]) % P
    return tuple(coeff[:N])


def add(a,b):
    return tuple((x+y) % P for x,y in zip(a,b))


def neg(a):
    return tuple(-x % P for x in a)


def sub(a,b):
    return add(a,neg(b))


def mul(a,b):
    coeff = [0]*(2*N-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            coeff[i+j] += x*y
    return field(coeff)


def power(a,n):
    out = ONE
    while n:
        if n & 1:
            out = mul(out,a)
        a = mul(a,a)
        n //= 2
    return out


def div(a,b):
    assert b != ZERO
    inverse = power(b,P**N-2)
    assert mul(b,inverse) == ONE
    return mul(a,inverse)


def det(rows):
    a,b,c = rows
    return add(sub(mul(a[0],sub(mul(b[1],c[2]),mul(b[2],c[1]))),
                   mul(a[1],sub(mul(b[0],c[2]),mul(b[2],c[0])))),
               mul(a[2],sub(mul(b[0],c[1]),mul(b[1],c[0]))))


def pairs_determinant(labels,pairs):
    rows=[]
    for i,j in pairs:
        x,y=labels[i],labels[j]
        if x is None:
            rows.append([y,ONE,ZERO])
        elif y is None:
            rows.append([x,ONE,ZERO])
        else:
            rows.append([mul(x,y),add(x,y),ONE])
    return det(rows)


def evaluate_rat(data,g):
    def poly(coeff):
        out=ZERO
        for c in reversed(coeff):
            out=add(mul(out,g),field(c))
        return out
    return div(poly(data['numerator']),poly(data['denominator']))


def gcd_degree(a,b):
    def trim(v):
        while len(v)>1 and v[-1] % P == 0:
            v.pop()
        return [x % P for x in v]
    a,b=trim(a[:]),trim(b[:])
    while b != [0]:
        while a != [0] and len(a)>=len(b):
            shift=len(a)-len(b)
            coef=a[-1]*pow(b[-1],-1,P) % P
            for i,x in enumerate(b):
                a[shift+i]=(a[shift+i]-coef*x) % P
            a=trim(a)
        a,b=b,a
    return len(a)-1


def main():
    path=Path(__file__).with_name('s0-residual-certificate.json')
    data=json.loads(path.read_text())
    witness=data['witness']
    assert witness['modulus']==F
    g=field([0,1])
    # 13 is prime: the Frobenius criterion needs only its proper divisor 1.
    frobenius=g
    for _ in range(N):
        frobenius=power(frobenius,P)
    assert frobenius==g
    assert gcd_degree(F,list(sub(power(g,P),g)))==0
    labels={int(i):field(v) for i,v in witness['labels'].items()}
    labels[0]=None
    assert len(labels)==16 and len(set(labels.values()))==16
    assert labels[1]==field(2) and labels[2]==field(3) and labels[3]==field(4)
    assert labels[5]==ONE and labels[7]==ZERO and labels[9]==g
    for i,v in data['reconstructed_labels'].items():
        assert evaluate_rat(v,g)==labels[int(i)]
    gate_values={name:evaluate_rat(v,g) for name,v in data['reconstruction_gates'].items()}
    assert all(value!=ZERO for value in gate_values.values())
    assert all(value==field(witness['gates'][name]) for name,value in gate_values.items())
    d_gates={}
    for t in [1,10,15,8,3,2,0,4,6]:
        pairs=[((t-1)%16,t),((t+4)%16,(t+9)%16),((t+6)%16,(t+8)%16)]
        value=pairs_determinant(labels,pairs)
        assert value==ZERO
        d_gates[str(t)]=list(value)
    c,d,e,g,j,k=map(labels.__getitem__,[1,2,3,9,10,14])
    x,y,z=map(labels.__getitem__,[8,15,6])
    C=div(mul(sub(j,g),sub(k,d)),mul(mul(sub(j,c),sub(j,d)),sub(k,g)))
    s8=sub(add(div(y,j),mul(C,sub(j,x))),ONE)
    s0=sub(add(div(mul(y,sub(d,x)),mul(x,sub(d,y))),
               div(mul(mul(sub(d,c),sub(z,j)),sub(x,g)),
                   mul(mul(sub(d,g),sub(d,j)),sub(z,c)))),ONE)
    assert s8==ZERO and s0!=ZERO
    evaluations={}
    for name in ['Q','E','P']:
        value=ZERO
        for a in reversed(data['polynomials'][name]):
            value=add(mul(value,x),evaluate_rat(a,g))
        assert value==field(witness[name+'_at_X'])
        evaluations[name]=list(value)
    assert field(evaluations['Q'])==ZERO and field(evaluations['E'])==ZERO
    assert field(evaluations['P'])!=ZERO
    w_value=ZERO
    for a in reversed(data['polynomials']['W']):
        w_value=add(mul(w_value,x),evaluate_rat(a,g))
    clearing=ONE
    for value in [x,sub(d,y),sub(d,g),sub(d,j),mul(sub(z,c),w_value)]:
        assert value!=ZERO
        clearing=mul(clearing,value)
    assert mul(clearing,s0)==field(evaluations['P'])
    result=dict(scope='Complete replay of one algebraic witness; not an H-labeling',
                certificate_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                irreducible_degree=N, irreducibility_frobenius_checks=2,
                labels_checked=16, distinct_pair_checks=120,
                nonzero_gates_checked=len(gate_values), D_gates=d_gates,
                S8=list(s8), S0_minus_one=list(s0), evaluations=evaluations,
                failures=[], H_assignments_tested=0, rank_tests=0)
    out=Path(__file__).with_name('s0-residual-audit.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['irreducible_degree','labels_checked',
                     'distinct_pair_checks','nonzero_gates_checked','failures',
                     'H_assignments_tested','rank_tests']}))
    print('Complete witness replay:',out)


if __name__=='__main__':
    main()
