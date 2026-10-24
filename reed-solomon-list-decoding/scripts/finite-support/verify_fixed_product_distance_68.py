"""Independent actual-set/beta verification of all 69 endpoint modes.

No constructor import, new box, factor solve, alternative enclosure or
midpoint sign. A straddling interval remains inconclusive.
"""
import gzip
import hashlib
import json
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations
from math import factorial
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
SOURCE = B/'fixed-product-distance-68.json'
OUT = B/'fixed-product-distance-68-verification.json'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


@lru_cache(None)
def choose(n, k):
    return factorial(n)//factorial(k)//factorial(n-k) if 0<=k<=n else 0


def enc(q):
    return [q.numerator,q.denominator]


def beta(n, k, i, j, t):
    return sum((-1)**(u-t)*choose(u,t)*choose(n-2*k,u-k)*
               choose(n-k-u,i-u)*choose(n-k-u,j-u)
               for u in range(max(k,t),min(i,j,n-k)+1))


def main():
    saved = json.loads(SOURCE.read_text())
    counts = Counter()
    report = dict(stage='in_progress', failures=[], source_sha256=sha(SOURCE),
                  code_sha256=sha(Path(__file__)))

    def save():
        report.update(checks=sum(counts.values()), checks_by_kind=dict(counts))
        OUT.write_text(json.dumps(report,indent=2)+'\n')

    def ck(kind, ok, detail=None):
        counts[kind] += 1
        if not ok:
            report['failures'].append(dict(kind=kind,detail=detail))
            report['stage'] = 'failed'
            save()
            raise AssertionError((kind,detail))

    ck('constructor_binding', saved['code_sha256']==sha(B/'fixed_product_distance_68.py'))
    for p,h in saved['input_sha256'].items():
        ck('every_input_binding', sha(ROOT/p)==h, p)
    for name, code in [('l112-l113-critical-audit.json','critical_audit_l112_l113.py'),
                       ('l114-critical-audit.json','critical_audit_l114.py')]:
        audit = json.loads((B/name).read_text())
        ck('retained_audit_status_code', audit['stage']=='verified' and not audit['failures']
           and audit['code_sha256']==sha(B/code),name)
        for p,h in audit['input_sha256'].items():
            ck('every_retained_audit_binding',sha(ROOT/p)==h,p)
    with gzip.open(B/'positive-factor-enclosure.json.gz','rt') as f:
        z = json.load(f)
    rv = json.loads((B/'positive-factor-enclosure-verification.json').read_text())
    margins = [min(l+10**25,10**25-u) for l,u in z['krawczyk_image']]
    ck('retained_root_input', z['stage']=='exact_complete' and z['inclusion'] and
       rv['stage']=='verified' and not rv['failures'] and rv['input_sha256']==sha(B/'positive-factor-enclosure.json.gz')
       and len(margins)==64 and min(margins)>0 and margins==z['inclusion_margins']==rv['inclusion_margins'])
    lp = json.loads((B/'delsarte-lp-results.json').read_text())
    av = [F(v['numerator'],v['denominator']) for v in lp['exact']['primal']]
    N, H, S = 65537**28//2**128+1, choose(1024,68), choose(956,68)
    U = F(choose(1024,64),choose(68,64))
    g = [choose(68,i)*choose(956,i) for i in range(69)]
    c = [F(1)]+[F(0)]*4+[(N-1)*av[i-5]/((U-1)*g[i]) for i in range(5,69)]
    ck('canonical_data', len(av)==64 and min(av)>0 and sum(av)==U-1 and
       list(map(enc,c))==saved['c']==z['c'] and saved['N']==z['N']==N and
       saved['H']==z['H']==H and F(*saved['rho'])==F(N,H)>0 and
       (N-1)*2**128<=65537**28<N*2**128 and sum(g[i]*c[i] for i in range(69))==N)
    ck('all_frozen_data', saved['frozen']=={p:z[p] for p in saved['frozen']} and
       set(saved['frozen'])=={'N','H','Q','radius','point','scale_powers','box'} and
       z['Q']==10**70 and z['radius']==10**25 and len(z['point'])==len(z['scale_powers'])==64 and
       z['box']==[[q-10**25,q+10**25] for q in z['point']])
    ck('endpoint_array_length',len(saved['endpoints'])==64)
    box = {}
    for i in range(5,69):
        j = i-5
        p = z['scale_powers'][j]
        scale = F(10**p) if p>=0 else F(1,10**(-p))
        box[i] = tuple(scale*F(z['point'][j]+s*10**25,10**70) for s in (-1,1))
        ck('every_original_endpoint', saved['endpoints'][j]==dict(i=i,interval=list(map(enc,box[i])))
           and 0<box[i][0]<box[i][1],i)
    A, P = set(range(68)), set(range(68,136))
    dictionary, entries = [], []
    for r in range(69):
        Q = set(range(68,136-r))|set(range(136,136+r))
        words = [A,P,Q]
        atoms = [sum(sum(1<<j for j,W in enumerate(words) if p in W)==mask for p in range(1024))
                 for mask in range(8)]
        ck('all_actual_atoms', atoms==[888-r,68,r,0,r,0,68-r,0] and min(atoms)>=0 and
           sum(atoms)==1024 and all(len(W)==68 for W in words),r)
        presentations, values = [], []
        for order in permutations(range(3)):
            X,Y,Z = [words[j] for j in order]
            i,j,h = len(X-Y),len(X-Z),len(Y-Z)
            t,s = len((X-Y)&(X-Z)),len((Y-X)&(Z-X))
            D = choose(i,t)*choose(68-i,j-t)*choose(i,s)*choose(956-i,j-s)
            ck('all_six_presentations', h==i+j-t-s and t-s==r and D>0 and
               max(0,i+j-68)<=t<=min(i,j) and max(0,i+j-956)<=s<=min(i,j),[r,order])
            if min(i,j,h)==0:
                value = (c[max(i,j,h)],)*2
                ck('all_Boolean_repetitions', D==(g[j] if i==0 else 1),[r,order])
            elif min(i,j,h)<5:
                value = (F(0),F(0))
                ck('all_forbidden_cases',min(c[i],c[j],c[h])==0,[r,order])
            else:
                value = tuple(box[i][e]*box[j][e]*box[h][e] for e in (0,1))
            values.append(value)
            presentations.append(dict(order=list(order),orbit=[i,j,t,s],h=h,D=D,full_count=g[i]*D))
        v = choose(68,r)*choose(888,r)
        ck('complete_counts_and_dictionary', presentations[0]['orbit']==[68,68,68,68-r] and
           presentations[0]['h']==r and presentations[0]['D']==v and
           all(p['full_count']==S*v for p in presentations) and len(set(values))==1,r)
        entry = dict(r=r,orbit=[68,68,68,68-r],h=r,D=v,interval=list(map(enc,values[0])))
        ck('every_entry_interval', saved['entries'][r]==entry,r)
        dictionary.append(dict(r=r,atoms=atoms,presentations=presentations,interval=entry['interval']))
        entries.append(values[0])
    ck('all_dictionary_lengths',len(saved['entries'])==len(dictionary)==69)

    # k=0 is the only surviving full-weight head representation.
    head = beta(68,0,68,68,68)
    ck('degenerate_head_and_source_range',head==choose(68,68)==1 and
       [k for k in range(35) if k<=68<=68-k]==[0] and
       [k for k in range(479) if k<=68<=956-k]==list(range(69)))
    denominators = [choose(956-2*k,68-k) for k in range(69)]
    E = [[F(head*beta(956,k,68,68,68-r),denominators[k]) for r in range(69)] for k in range(69)]
    mult = [choose(956,k)-choose(956,k-1) for k in range(69)]
    v = [choose(68,r)*choose(888,r) for r in range(69)]
    ck('all_multiplicities_and_dimension', saved['size']==g[68]==S and
       saved['multiplicities']==mult and min(mult)>0 and sum(mult)==S and
       saved['valencies']==v and E[0]==v and sum(v)==S and min(denominators)>0)
    ck('spectral_table_dimensions',len(saved['eigenmatrix'])==69 and
       all(len(row)==69 for row in saved['eigenmatrix']))
    for k in range(69):
        for r in range(69):
            ck('every_independent_beta',E[k][r].denominator==1 and E[k][r]==saved['eigenmatrix'][k][r],[k,r])
        ck('identity_relation',E[k][0]==1,k)
    for r in range(69):
        for s in range(69):
            ck('complete_trace_orthogonality',sum(mult[k]*int(E[k][r])*int(E[k][s]) for k in range(69))==
               (S*v[r] if r==s else 0),[r,s])
    # Both cross directions and both diagonal entries in the source's
    # constant anchor block, before the congruence.
    cross = beta(68,0,0,68,0)*beta(956,0,0,68,0)
    cross_reverse = beta(68,0,68,0,0)*beta(956,0,68,0,0)
    ck('complete_source_anchor',cross==cross_reverse==S and
       beta(68,0,0,0,0)*beta(956,0,0,0,0)==1 and denominators[0]==S)
    modes, widths = [], []
    for k in range(69):
        terms = [(w*l,w*u) if w>=0 else (w*u,w*l) for w,(l,u) in zip(E[k],entries)]
        lo,hi = sum(q[0] for q in terms),sum(q[1] for q in terms)
        correction = S*c[68]**2 if k==0 else F(0)
        sl,su = lo-correction,hi-correction
        sign = 'negative' if su<0 else 'positive' if sl>0 else 'zero' if sl==su==0 else 'unresolved'
        mode = dict(k=k,multiplicity=mult[k],shell=list(map(enc,(lo,hi))),correction=enc(correction),
                    schur=list(map(enc,(sl,su))),schur_over_c68=[enc(sl/c[68]),enc(su/c[68])],verdict=sign)
        ck('every_original_mode',saved['modes'][k]==mode and lo<=hi,k)
        ck('source_scalar_normalization',denominators[k]*lo==sum(head*beta(956,k,68,68,68-r)*
           entries[r][0 if E[k][r]>=0 else 1] for r in range(69)),k)
        if sign=='unresolved':
            ck('actual_straddle',sl<0<su,k)
        modes.append(mode)
        widths.append(dict(k=k,width_over_c68=enc((hi-lo)/c[68])))
    row = [sum(v[r]*entries[r][e] for r in range(69)) for e in (0,1)]
    ck('constant_anchor_congruence',modes[0]['shell']==list(map(enc,row)) and
       all(S*row[e]-(S*c[68])**2==S*F(*modes[0]['schur'][e]) for e in (0,1)))
    ck('all_mode_lengths',len(saved['modes'])==69)
    for r in range(69):
        ck('complete_coefficient_trace',sum(mult[k]*E[k][r] for k in range(69))==(S if r==0 else 0),r)
    signs = Counter(m['verdict'] for m in modes)
    negative = [m['k'] for m in modes if m['verdict']=='negative']
    verdict = 'FIXED_PRODUCT_EXCLUDED' if negative else 'INCONCLUSIVE' if signs['unresolved'] else 'SHELL_PASSES'
    summary = dict(counts=dict(signs),negative_modes=negative,verdict=verdict,
                   required='all 69 Schur coordinates nonnegative')
    # The observed attempt stops at its straddles; no alternative interval
    # or unverified negative-direction inference is accepted.
    ck('entire_inconclusive_summary',saved['stage']=='complete' and not saved['failures'] and
       saved['summary']==summary and verdict=='INCONCLUSIVE' and not negative and saved['direction'] is None)
    minimum = min((m for m in modes if m['verdict']=='positive'),key=lambda m:F(*m['schur_over_c68'][0]))
    bound = F(*minimum['schur_over_c68'][0])
    floor = bound*10**6//1
    ck('positive_mode_lower_bracket',F(floor,10**6)<=bound<F(floor+1,10**6))
    report.update(stage='verified',dictionary=dictionary,source_denominators=denominators,
                  eigenmatrix=[[int(q) for q in row] for row in E],multiplicities=mult,modes=modes,
                  widths=widths,summary=summary,
                  positive_modes=[m['k'] for m in modes if m['verdict']=='positive'],
                  unresolved_modes=[m['k'] for m in modes if m['verdict']=='unresolved'],
                  minimum_positive_lower=dict(k=minimum['k'],value=enc(bound),
                      bracket=[enc(F(floor,10**6)),enc(F(floor+1,10**6))]))
    save()
    print('Independent checks:',sum(counts.values()),'; failures:',len(report['failures']))
    print('Actual/required relations 69/69, presentations 414/414, modes 69/69')
    print('Whole-box signs:',dict(signs),'; required all >=0; verdict:',verdict)
    print('Positive mode indices:',report['positive_modes'])
    print('Unresolved mode indices:',report['unresolved_modes'])
    print('Minimum positive lower/c68 in ['+str(floor)+'/1000000, '+str(floor+1)+'/1000000); required >=0')
    print('Certificate:',OUT)


if __name__=='__main__':
    main()
