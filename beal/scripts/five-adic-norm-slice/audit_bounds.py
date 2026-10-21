"""Independent arithmetic audit for L060; uniform arguments remain in the lemma.

No construction code is imported. Source coefficients are transcribed from
L034's canonical source data; all saved Bezout witnesses are multiplied out.
"""
from fractions import Fraction
from math import comb, gcd
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent


def clean(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def plus(*ps):
    return clean([sum(p[i] if i < len(p) else 0 for p in ps)
                  for i in range(max(map(len, ps)))])


def times(p, q):
    return clean([sum(p[i] * q[k-i] for i in range(len(p))
                      if 0 <= k-i < len(q))
                  for k in range(len(p)+len(q)-1)])


def scale(p, n):
    return clean([n*c for c in p])


def cube(p):
    return times(times(p, p), p)


def mod(p):
    return clean([c % 5 for c in p])


def value(p, x):
    return sum(c*x**i for i, c in enumerate(p))


def poly_gcd(p, q):
    p, q = mod(p), mod(q)
    while q != [0]:
        while p != [0] and len(p) >= len(q):
            shift = len(p)-len(q)
            p = mod(plus(p, [0]*shift + scale(q, -p[-1]*pow(q[-1], -1, 5))))
        p, q = q, p
    return mod(scale(p, pow(p[-1], -1, 5)))


a = [-39176677684144739,108160113602504237,74593328129816300,
     420015065507429,-14545268641576841,-1895608370650736,
     576036867160006,82165362766027,2536749758583,19162005343,
     21559874,743]
b = times([-707351591,271927184,65058492,1304157,4518,1],
          [-37315543,-37789861,-3406817,3626752,192189,1])
h = [9789217,4971236,1333262,-52820,1]
d = [comb(11, i)*(-16)**(11-i) for i in range(12)]
J = plus(scale(a, 2), scale(b, -1))
g = [-20,-10,-1,1]
source = json.loads((BASE.parent/'five-isogeny-modular-norm/norm-certificate.json').read_text())
old = json.loads((BASE/'bounds-certificate.json').read_text())
checks = {}
for name, p in [('a', a), ('b', b), ('h', h), ('d', d), ('jcoef', J)]:
    checks['source_'+name] = p == source['polynomials_ascending'][name]
identity = plus(times(a,a), scale(times(a,b), -1),
                scale(times(times(b,b),g), -1), times(d,cube(h)))
checks['elimination_identity'] = identity == [0]
f0, f1 = [-55,30,-4], [-4,1]
conjugate_product = plus(times(f0,f0), scale(times(f0,f1),-1),
                         scale(times(times(f1,f1),g),-1))
checks['f_conjugate_product'] = conjugate_product == [-comb(5,i)*(-5)**(5-i) for i in range(6)]

cases = {}
for r in [1,2,4]:
    F = mod(plus(cube(h), scale(J,r), scale(d,-r*r)))
    derived = {'derivative': mod([i*F[i] for i in range(1,len(F))]),
               'b': mod(b), 'd': mod(d)}
    checks[f'F_{r}_matches'] = F == old['cases'][str(r)]['F_mod5']
    evidence = {}
    for label, p in derived.items():
        witness = old['cases'][str(r)]['bezout'][label]
        lhs = mod(plus(times(witness['u'],F),times(witness['v'],p)))
        actual_gcd = poly_gcd(F,p)
        checks[f'{r}_{label}_polynomial'] = p == witness['p']
        checks[f'{r}_{label}_identity'] = lhs == witness['gcd'] == actual_gcd
        if label != 'd':
            checks[f'{r}_{label}_unit'] = lhs == [1]
        evidence[label] = {'p':p,'u':witness['u'],'v':witness['v'],
                           'product_sum':lhs,'independent_gcd':actual_gcd}
    cases[str(r)] = {'F_mod5':F,'verified_witnesses':evidence}
P, Q = [2,1,2,2,4,4,1], [4,1,2,2,1,1,1]
checks['residue_one_blocks'] = mod(times(P,Q)) == cases['1']['F_mod5']
checks['residue_one_coprime'] = poly_gcd(P,Q) == [1]
checks['residue_four_d_not_inverted'] = poly_gcd(cases['4']['F_mod5'],d) == [4,1]

nonintegral = {'five_power_eleven_mod_eleven':pow(5,11,11),
              'J16_mod5':value(J,16)%5,'h16_mod5':value(h,16)%5}
checks['nonintegral_matches'] = nonintegral == old['nonintegral']
checks['eleventh_root_unique'] = gcd(11,5**11-1) == gcd(11,4) == 1
checks['nonintegral_units'] = value(J,16)%5 == value(h,16)%5 == 1
x, y = 16, -61
dy = Fraction(3*x*x-2*x-10,2*y+1)
f = (x-4)*y-4*x*x+30*x-55
df = y+(x-4)*dy-8*x+30
assert dy.denominator == df.denominator == 1
lower = {'point':[x,y],'curve_y_derivative':2*y+1,
         'curve_x_rhs_derivative':3*x*x-2*x-10,'dy_dx':int(dy),
         'f':f,'df_dx':int(df),'log_derivative_mod5':int(df)*pow(f,-1,5)%5}
checks['lower_on_curve'] = y*y+y == value(g,x)
checks['lower_matches'] = lower == old['lower_bound_data']
checks['lower_units_and_nonzero_variation'] = (2*y+1)%5 != 0 and f%5 != 0 and lower['log_derivative_mod5'] == 1
binomial = [comb(5,i)*5**i for i in range(6)]
checks['principal_fifth_mod25'] = [n%25 for n in binomial] == [1,0,0,0,0,0]
checks['principal_fifth_mod125'] = [n%125 for n in binomial] == [1,25,0,0,0,0]
units = [i for i in range(125) if gcd(i,125)==1]
fifths = sorted(set(i**5%125 for i in units))
kernel = [i for i in units if i**5%125 == 1]
quotient = {'modulus':125,'unit_count':len(units),'fifth_power_residues':fifths,
            'fifth_power_kernel':kernel,'unit_class_upper_bound':len(units)//len(fifths)}
checks['quotient_matches'] = quotient == old['rational_unit_quotient']
checks['quotient_size'] = len(units) == 100 and len(fifths) == 20 and len(kernel) == 5
bounds = {'unrestricted_constructed_unit_classes':5**11,'norm_class_upper_bound':5,
          'norm_slice_lower_bound':5**11//5,'integral_scalar_residues':[2,4],
          'scalar_lifts_per_residue_mod125':125//5,'root_upper_bound_per_residue':12,
          'whole_fiber_upper_bound':2*(125//5)*12}
checks['bounds_match'] = bounds == old['bounds']
checks['strict_separation'] = 0 < bounds['whole_fiber_upper_bound'] < bounds['norm_slice_lower_bound']

out = {'source_coefficients':{'a':a,'b':b,'h':h,'d':d,'J':J},
       'elimination_identity':identity,'f_conjugate_product':conjugate_product,
       'cases':cases,'residue_one_blocks':[P,Q], 'nonintegral':nonintegral,
       'lower_bound_data':lower,'fifth_binomial_coefficients':binomial,
       'rational_unit_quotient':quotient,'bounds':bounds,
       'checks':checks,'failures':[k for k,v in checks.items() if not v]}
target = BASE/'bounds-audit-certificate.json'
target.write_text(json.dumps(out,indent=2)+'\n')
print(f'Independent checks: {len(checks)}; failures: {out["failures"]}')
print(f'Actual upper bound: {bounds["whole_fiber_upper_bound"]}; required below: {bounds["norm_slice_lower_bound"]}')
print('All scalar cases require the uniform proof in L060; no finite sampling claim.')
print('Certificate:', target.relative_to(BASE.parent.parent))
assert not out['failures']
