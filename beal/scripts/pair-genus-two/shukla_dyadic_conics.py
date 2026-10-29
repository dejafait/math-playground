"""Fixed good-element conics: dyadic rational-root row only.

Positive results carry strict Hensel certificates. Finite failure is unknown.
The existing odd/real producer is deliberately not rerun or overwritten.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
import traceback
import two_adic_filter as f

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'shukla-dyadic-conics-certificate.json'
D = dict(completed=False, failures=[], bindings={}, checks=0, classes=[],
         full_goodness_decided=False, pairing_computed=False,
         bounds=dict(classes_required=2, classes_actual=0,
                     candidates_cap_per_class=2560, candidates_actual=0,
                     digit_precision_required=9, digit_precision_actual=9,
                     rational_bits_cap=8192))


def ck(test, name):
    D['checks'] += 1
    assert test, name


def read(name):
    raw = (ROOT/name).read_bytes()
    D['bindings'][name] = sha256(raw).hexdigest()
    return json.loads(raw)


def val(a):
    terms = [4*f.v2(x)+i for i, x in enumerate(a) if x]
    return min(terms) if terms else None


def ppow(n):
    return f.power(f.PI if n >= 0 else f.PIINV, abs(n))


def square_certificate(h, square_roots):
    n = val(h)
    if n is None:
        return dict(square=True, zero=True, root_approx=[Q(0)]*4)
    if n % 2:
        return dict(square=False, valuation=n)
    normalized = f.mul(h, ppow(-n))
    residue = f.reduce_pi(normalized)
    digit_root = square_roots.get(str(residue))
    if digit_root is None:
        return dict(square=False, valuation=n, unit_residue=residue)
    root = f.mul(ppow(n//2), f.from_digits(digit_root))
    error = f.add(f.mul(root, root), f.scale(h, -1))
    ev = val(error)
    derivative = f.scale(root, 2)
    dv = val(derivative)
    ck(ev is None or ev >= n+9, 'complete square residue error')
    ck(dv == 4+n//2, 'derivative valuation')
    ck(ev is None or ev > 2*dv, 'strict Hensel inequality')
    return dict(square=True, zero=False, valuation=n,
                normalized=normalized, unit_residue=residue,
                digit_root=digit_root, root_approx=root,
                residual=error, residual_valuation=ev,
                derivative=derivative, derivative_valuation=dv,
                hensel_threshold=2*dv, guaranteed_error_lower=n+9)


def main():
    old = read('shukla-good-conics-certificate.json')
    replay = read('shukla-good-conics-verification.json')
    two = read('two-adic-filter-certificate.json')
    audit = read('two-adic-filter-audit.json')
    model = read('odd-model-support-certificate.json')
    for label, c in [('old', old), ('old replay', replay), ('dyadic', two), ('dyadic audit', audit)]:
        ck(c['completed'] and not c['failures'], label+' complete')
    ck(replay['bindings']['shukla-good-conics-certificate.json'] == D['bindings']['shukla-good-conics-certificate.json'], 'old replay binds input')
    ck(audit['bindings']['two-adic-filter-certificate.json'] == D['bindings']['two-adic-filter-certificate.json'], 'dyadic audit binds input')
    ck(two['bindings']['odd-model-support-certificate.json'] == D['bindings']['odd-model-support-certificate.json'], 'same model')
    f.E = list(map(Q, two['field']['pi_polynomial']))
    f.PIINV = [-f.E[i+1]/f.E[0] for i in range(4)]
    ck(f.E == list(map(Q, [5850,-8442,1272,-64,1])), 'actual Eisenstein field')
    ck(f.mul(f.PI, f.PIINV) == f.ONE, 'uniformizer inverse')
    transport = two['field']['alpha_to_pi']
    D['field'] = two['field']
    D['square_rows'] = two['square_table']['square_rows']
    D['square_roots'] = two['square_table']['square_roots']
    # Authenticate every table row again, rather than use an unverified lookup.
    roots = D['square_roots']
    ck(len(D['square_rows']) == 256 and len(roots) == 8, 'complete unit-square domain')
    for j, (s, z) in enumerate(D['square_rows']):
        ck(s == 2*j+1 and f.reduce_pi(f.mul(f.from_digits(s), f.from_digits(s))) == z, 'all unit squares')
    for z, s in roots.items():
        ck(f.reduce_pi(f.mul(f.from_digits(s), f.from_digits(s))) == int(z), 'each saved root')
    eta = f.matvec(transport, list(map(Q, model['field']['eta_in_alpha'])))
    ck(eta == list(map(Q, two['field']['eta_pi'])), 'actual eta transport')
    gap = f.add([Q(9075),0,0,0],f.scale(eta,-1))
    gapnorm = f.norm(gap)
    ck(gapnorm == 73990352390625 == 3**5*5**6*11**7, 'complete branch-gap norm support')
    D['outside_support'] = dict(gap_pi=gap,gap_norm=gapnorm,
        gap_norm_factorization={'3':5,'5':6,'11':7},
        allowed_rational_primes=[2,3,5,11],
        b_even_valuation_input='L147/L149 supported full representatives',
        integrality_input='L138 monic H(eta)=0')
    ck([(c['label'],c['mask']) for c in old['classes']] == [('eta_class',132102),('nu',3109)], 'exact two classes')
    for oldrec in old['classes']:
        q=Q(1); b=f.ONE[:]
        for j,w in enumerate(two['witnesses']):
            if oldrec['mask'] >> j & 1:
                q *= Q(w['source']['inverse_norm'])
                bp = f.matvec(two['field']['O_to_pi'], list(map(Q,w['source']['coefficients'])))
                b = f.mul(b,bp)
        ck(q == Q(oldrec['rational']) and b == f.matvec(transport,list(map(Q,oldrec['quartic_power']))), 'reconstructed full representative')
        ck(q.numerator == 1, 'rational component numerator support')
        cofactor=q.denominator; factors={}
        for p in (2,3,5,11):
            exponent=0
            while cofactor%p==0:
                cofactor//=p;exponent+=1
            factors[str(p)]=exponent
        ck(cofactor==1, 'complete rational-component support')
        a = f.matvec(transport,list(map(Q,oldrec['row']['quaternion_a_power'])))
        c = f.matvec(transport,list(map(Q,oldrec['row']['quaternion_c_power'])))
        ck(f.mul(a,b) == [q,0,0,0], 'a*b=q')
        ck(f.mul(c,b) == f.add([Q(9075),0,0,0],f.scale(eta,-1)), 'c*b=r-eta')
        va,vc = val(a),val(c)
        ka,kc = va//2,vc//2
        aa,cc = f.mul(a,ppow(-2*ka)),f.mul(c,ppow(-2*kc))
        ck(val(aa) in (0,1) and val(cc) in (0,1), 'square normalization')
        rec=dict(label=oldrec['label'],mask=oldrec['mask'],rational=q,
                 b_pi=b,q_denominator_factorization=factors,
                 a_pi=a,c_pi=c,a_valuation=va,c_valuation=vc,
                 a_scale_exponent=ka,c_scale_exponent=kc,
                 normalized_a=aa,normalized_c=cc,attempts=[],
                 soluble=None,good=None)
        D['classes'].append(rec)
        # Fixed bounded search. A successful Hensel certificate alone is used.
        # No negative conclusion is permitted from exhausting this domain.
        for k in (0,1,-1,2,-2):
            for digit in range(512):
                vv = f.mul(ppow(k),f.from_digits(digit))
                h = f.add(f.mul(aa,f.mul(vv,vv)),cc)
                result=square_certificate(h,roots)
                rec['attempts'].append(dict(scale=k,digit=digit,**result))
                D['bounds']['candidates_actual'] += 1
                if result['square']:
                    uu=result['root_approx']
                    original_u=f.mul(ppow(kc),uu)
                    original_v=f.mul(ppow(kc-ka),vv)
                    original_error=f.add(f.add(f.mul(original_u,original_u),f.scale(f.mul(a,f.mul(original_v,original_v)),-1)),f.scale(c,-1))
                    normalized_error=f.add(f.add(f.mul(uu,uu),f.scale(f.mul(aa,f.mul(vv,vv)),-1)),f.scale(cc,-1))
                    ck(original_error == f.mul(ppow(2*kc),normalized_error), 'full conic coordinate transport')
                    rec.update(soluble=True,solution=dict(V=vv,U_approx=uu,
                         original_u_approx=original_u,original_v=original_v,
                         original_w=1,original_residual=original_error,
                         normalized_residual=normalized_error,certificate=result))
                    break
            if rec['soluble']:break
        D['bounds']['classes_actual'] += 1
    D['bounds']['rational_bits_actual']=f.D['bounds']['max_rational_bits']
    D['source_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    D['helper_sha256']=sha256((ROOT/'two_adic_filter.py').read_bytes()).hexdigest()
    D['completed']=True


if __name__=='__main__':
    try:main()
    except Exception as e:D['failures'].append(dict(message=str(e),traceback=traceback.format_exc()))
    OUT.write_text(json.dumps(D,indent=2,default=str)+'\n')
    print(json.dumps(dict(completed=D['completed'],failures=[e['message'] for e in D['failures']],
        classes=[dict(label=c['label'],soluble=c['soluble'],candidates=len(c['attempts']),good=c['good']) for c in D['classes']],
        bounds=D['bounds'],path=str(OUT))))
    raise SystemExit(0 if D['completed'] else 1)
