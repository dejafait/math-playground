#!/usr/bin/env python3
"""Exact certificates for L033's two fixed-label overlap configurations."""
import itertools
import json
from pathlib import Path
from triple_support_rank import Q, root_product, mul, evaluate, determinant

OUT = Path(__file__).with_name('three-overlap-results.json')
FAILURES = []

def check(test, label):
    if not test:
        FAILURES.append(label)


def case(domain, triples, realized):
    flat = sum(triples, [])
    check(len(set(flat)) == 9 and set(flat) <= set(domain), 'nine distinct subgroup points')
    unused = [x for x in domain if x not in flat]
    core = unused[:60]
    private = [unused[60+2*i:62+2*i] for i in range(3)]
    t12, t23, t31 = triples
    supports = [core+t12+t31+private[0], core+t12+t23+private[1], core+t23+t31+private[2]]
    sets = list(map(set, supports))
    check(all(len(s)==68 for s in sets), '68 support sizes')
    check(sets[0]&sets[1]&sets[2] == set(core), 'common core')
    for i,j,t in [(0,1,t12),(1,2,t23),(2,0,t31)]:
        check(sets[i]&sets[j] == set(core+t), 'exact pair intersection')
    cubics = [root_product(t) for t in triples]
    matrix = [[f[i] for f in cubics] for i in range(4)]
    minors = [{'rows':list(rows), 'value':determinant([matrix[i] for i in rows])} for rows in itertools.combinations(range(4),3)]
    rank = 3 if any(m['value'] for m in minors) else 2
    check(rank == (2 if realized else 3), 'expected rank')
    small = dict(triples=triples, subgroup_membership_powers=[pow(x,1024,Q) for x in flat], cubics=cubics, matrix=matrix, minors=minors, rank=rank)
    result = dict(small=small, core=core, private=private, supports=supports)
    if realized:
        check(all(f[1:] == cubics[0][1:] for f in cubics), 'common nonconstant coefficients')
        d = [f[0] for f in cubics]
        z = [(d[1]-d[2])%Q, (d[2]-d[0])%Q, (d[0]-d[1])%Q]
        check(all(z), 'three nonzero kernel entries')
        check(all(sum(row[j]*z[j] for j in range(3))%Q == 0 for row in matrix), 'complete kernel identity')
        G = root_product(core)
        f = [[0], [(-z[0]*x)%Q for x in mul(G,cubics[0])], [(z[2]*x)%Q for x in mul(G,cubics[2])]]
        check(all(len(a)<=64 for a in f), 'strict degrees')
        vals = [[evaluate(a,x) for x in domain] for a in f]
        center = []
        for pos,x in enumerate(domain):
            prescriptions = [vals[i][pos] for i in range(3) if x in sets[i]]
            check(len(set(prescriptions))<=1, 'compatible center at '+str(x))
            center.append(prescriptions[0] if prescriptions else 0)
        agreements = [[x for pos,x in enumerate(domain) if vals[i][pos]==center[pos]] for i in range(3)]
        equalities = []
        for i,j,t in [(0,1,t12),(1,2,t23),(2,0,t31)]:
            eq = [x for pos,x in enumerate(domain) if vals[i][pos]==vals[j][pos]]
            check(set(eq)==set(core+t), 'full exact pair equality')
            equalities.append(eq)
        check(all(sets[i]<=set(agreements[i]) for i in range(3)), 'all selected agreements')
        small.update(kernel=z, agreement_counts=list(map(len,agreements)), pair_equality_counts=list(map(len,equalities)), message_degrees=[-1,len(f[1])-1,len(f[2])-1])
        result.update(core_polynomial=G, messages=f, message_evaluations=vals, center=center, full_agreements=agreements, pair_equalities=equalities)
    return result


def main():
    h=pow(3,64,Q)
    check(pow(h,1024,Q)==1 and pow(h,512,Q)==Q-1, 'generator order')
    domain=[pow(h,i,Q) for i in range(1024)]
    cases={'realized':case(domain,[[1,25417,40120],[8306,27221,30011],[14177,16349,35012]],True),
           'forbidden':case(domain,[[pow(h,3*r+j,Q) for j in range(3)] for r in range(3)],False)}
    certificate=dict(field=Q,generator=h,domain=domain,cases=cases,failures=FAILURES,required_agreements=68,established_list_lower_bound=3,threshold_numerator=Q**28,threshold_denominator=2**128)
    OUT.write_text(json.dumps(certificate,indent=2)+'\n')
    for name,c in cases.items():
        print(name+': rank='+str(c['small']['rank'])+'; actual agreements='+str(c['small'].get('agreement_counts'))+'; required=68')
    print('Established list lower bound=3; unsafe threshold requires >65537^28/2^128; not reached.')
    print('failures='+str(FAILURES)+'; full certificate: '+str(OUT))
    if FAILURES:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
