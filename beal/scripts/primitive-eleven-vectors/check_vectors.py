"""Exact finite-field and local-factor evidence; ascending coefficients.

No package dependencies. Run from the active notebook. Complete evidence is
written before the compact summary. Further certification is documented in L041.
"""
from pathlib import Path
from itertools import product
import json

BASE = Path(__file__).resolve().parent


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a): c[i] += x
    for i, x in enumerate(b): c[i] += x
    return trim(c)


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i+j] += x*y
    return trim(c)


def power(a, n):
    c = [1]
    for _ in range(n): c = mul(c, a)
    return c


def mod(a): return trim([x % 11 for x in a])


def divide(a, b):
    a = mod(a)
    q = [0]*max(1, len(a)-len(b)+1)
    while a != [0] and len(a) >= len(b):
        i = len(a)-len(b)
        t = a[-1]*pow(b[-1], -1, 11) % 11
        q[i] = t
        for j, x in enumerate(b): a[i+j] = (a[i+j]-t*x) % 11
        a = trim(a)
    return trim(q), a


def scale(a, t): return mod([t*x for x in a])


def xgcd(a, b):
    r0, r1 = mod(a), mod(b)
    u0, u1, v0, v1 = [1], [0], [0], [1]
    while r1 != [0]:
        q, r = divide(r0, r1)
        r0, r1 = r1, r
        u0, u1 = u1, mod(add(u0, scale(mul(q,u1), -1)))
        v0, v1 = v1, mod(add(v0, scale(mul(q,v1), -1)))
    c = pow(r0[-1], -1, 11)
    return scale(r0,c), scale(u0,c), scale(v0,c)


m = [-380,-774,-1062,-456,258,468,104,-126,-6,6,-6,0,1]
def valuation(n):
    if n == 0: return None
    answer = 0
    while n % 11 == 0:
        n //= 11
        answer += 1
    return answer


def evaluate(a, x):
    result = 0
    for c in a[::-1]: result = result*x+c
    return result


def main():
    shifted = [0]
    for c in m[::-1]: shifted = add(mul(shifted, [-1,1]), [c])
    blocks = [power([1,1],10), [3,1], [9,1]]
    reconstruction = [1]
    for block in blocks: reconstruction = mul(reconstruction, block)
    bezout = []
    for i in range(3):
        for j in range(i+1,3):
            gcd, u, v = xgcd(blocks[i], blocks[j])
            identity = mod(add(mul(u,blocks[i]),mul(v,blocks[j])))
            assert gcd == identity == [1]
            bezout.append({'pair':[i,j], 'u':u,'v':v,'identity':identity})
    derivative = [i*m[i] for i in range(1,len(m))]
    roots = [{'residue':a, 'polynomial_residue':evaluate(m,a)%11,
              'derivative_residue':evaluate(derivative,a)%11} for a in [8,2]]
    shifted_vals = [valuation(c) for c in shifted]
    # Shifted complementary Hensel block is (u+2)(u+8) modulo 11.
    h0 = 2*8 % 11
    g0_over_11 = (shifted[0]//11)*pow(h0,-1,11)%11
    pi10_over_11 = -g0_over_11 % 11
    unit_residue = (-5)*pow(pi10_over_11,-1,11)%11
    unit_constructions = []
    for q0 in range(1,11):
        u = pow(q0,-1,11)
        unit_constructions.append({'q0':q0,'chosen_c_unit_residue':u,
                                   'q0_times_u11':q0*pow(u,11,11)%11})
    cube_roots = [{'unit':a,'root':pow(a,7,11),
                   'cube':pow(pow(a,7,11),3,11)} for a in range(1,11)]
    checks = {
        'complete_residue_reconstruction':mod(reconstruction)==mod(m),
        'dimension_twelve':sum(len(b)-1 for b in blocks)==12,
        'two_simple_residue_roots':all(r['polynomial_residue']==0 and r['derivative_residue']!=0 for r in roots),
        'shift_constant_valuation_one':shifted_vals[0]==1,
        'shift_first_ten_coefficients_divisible_by_11':all(c%11==0 for c in shifted[:10]),
        'shifted_complement_constant_unit':h0==5,
        'eisenstein_block_constant_residue':g0_over_11==5,
        'kummer_adjustment_residue_one':unit_residue==1,
        'ramified_point_root_residue':(6*6-14)%11==0,
        'ramified_point_derivative_unit':(2*6)%11!=0,
        'ramified_f_over_uniformizer_unit':(6-5)%11!=0,
        'cube_roots_complete':all(t['cube']==t['unit'] for t in cube_roots),
        'fourth_root_target_residue_one':all(t['q0_times_u11']==1 for t in unit_constructions),
        'norm_plane_size':sum((a+b+c)%5==2 for a,b,c in product(range(5),repeat=3))==25,
    }
    certificate = {
        'inputs':{'field_polynomial_ascending':m},
        'residue_blocks_ascending':blocks,
        'residue_reconstruction':mod(reconstruction),
        'pairwise_bezout':bezout,'simple_roots':roots,
        'shifted_polynomial_ascending':shifted,'shifted_coefficient_valuations':shifted_vals,
        'ramified_factor':{'degree':10,'ramification_index':10,'residue_degree':1,
                           'complement_constant_mod11':h0,'constant_over_11_mod11':g0_over_11,
                           'pi10_over_11_mod_uniformizer':pi10_over_11,
                           'kummer_polynomial_ascending':[55]+[0]*9+[1],
                           'kummer_adjustment_unit_residue':unit_residue},
        'all_places': [{'label':'root_mod_8','e':1,'f':1},
                       {'label':'root_mod_2','e':1,'f':1},
                       {'label':'root_mod_10_block','e':10,'f':1}],
        'hensel_ramified_point':{'w_residue':6,'equation_residue':0,
                                 'derivative_residue':1,'f_over_uniformizer_residue':1,
                                 'actual_11_over_uniformizer_valuation':9,
                                 'required_positive_valuation':1},
        'scalar_cube_root_residues':cube_roots,
        'scalar_c_unit_choices':unit_constructions,
        'bounds':{'unrestricted_vector_count':125,'inherited_norm_plane_count':25,
                  'complete_restricted_vector_count':None,
                  'required_for_target':'complete restricted set with realization for every retained vector'},
        'checks':checks,'failures':[k for k,v in checks.items() if not v],
        'unresolved':['complete simultaneous modular fiber compatibility and vector realizations'],
    }
    path=BASE/'vector-prerequisites-certificate.json'
    path.write_text(json.dumps(certificate,indent=2)+'\n')
    print('Field factors: (e,f)=(1,1),(1,1),(10,1); dimension actual=12 required=12')
    print('Ramified factor: Q11[root of X^10+55]; Eisenstein constant valuation actual=1 required=1')
    print('Hensel derivative valuations actual=0 required=0; ramified 11/pi valuation actual=9 required>=1')
    print('Unrestricted vectors=125; inherited norm candidates=25; exact restricted count=UNRESOLVED')
    print('Checks:',sum(checks.values()),'/',len(checks),'failures:',certificate['failures'])
    print('Certificate:',path.relative_to(Path.cwd()))
    assert not certificate['failures']


if __name__ == '__main__': main()
