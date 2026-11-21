"""Exact auxiliary rate checks for L710; not an audit of its contour proof.

Read only the named arithmetic functions in step 166's script, without
executing its top-level calculations or overwriting its certificate.
L709 supplies their complete Taylor, Simpson and rational-log error bounds.
"""
import ast
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

helper = Path(__file__).with_name('spatial-complex-phase-166.py')
source = helper.read_text()
names = {'ceildiv', 'fixed', 'log_unit', 'logq', 'q_squared', 'derivative', 'simpson'}
definitions = [node for node in ast.parse(source).body
               if isinstance(node, ast.FunctionDef) and node.name in names]
assert {node.name for node in definitions} == names
ns = dict(F=F, SCALE=1 << 100, TERMS=40, PANELS=32,
          d=F(5,4), R=F(11,8), U=F(121,64), A=F(27,10), Y=F(9,20))
exec(compile(ast.Module(body=definitions, type_ignores=[]), str(helper), 'exec'), ns)
ns['LOG2'] = ns['log_unit'](2,1)
simpson, logq, scale = ns['simpson'], ns['logq'], ns['SCALE']
d, R, U, A, Y = [ns[key] for key in ('d','R','U','A','Y')]

def enc(value):
    value = F(value)
    return dict(numerator=value.numerator, denominator=value.denominator,
                decimal_preview=float(value))

checks = {}
def check(name, actual, relation, required):
    actual, required = F(actual), F(required)
    passed = {'<': actual < required, '>': actual > required,
              '=': actual == required}[relation]
    checks[name] = dict(actual=enc(actual), relation=relation,
                        required=enc(required), passed=passed)

omega = tuple(A*(F(logq(F(9,5))[k],scale)-F(4,5)
                 +F(121,100)*F(logq(F(201,121))[k],scale)) for k in (0,1))
endpoint, _ = simpson(-Y,F(0))
point, _ = simpson(F(-19,50),F(1,20))
centered = (point[0]+F(1,20)*omega[0]/A,
            point[1]+F(1,20)*omega[1]/A)
check('endpoint_rate_upper',endpoint[1],'<',F(2053,100000))
check('outer_centered_residue_rate_lower',centered[0],'>',F(207,10000))
check('outer_centered_coefficient_margin',centered[0]-endpoint[1],'>',F(1,5000))
z2 = U/((d+F(1,20))**2+F(19,50)**2)
check('outer_point_outside_unit_disk',z2,'>',1)
check('outer_point_inside_larger_disk',z2,'<',F(65,64)**2)

# For X<0 every factor's log modulus decreases with c. Thus c=1/25
# bounds the full rectangle X in [-2/5,-9/25], c in [1/25,2/25].
cells=[]
count=40
cell_radius=F(1,25)/(2*count)
for j in range(count):
    x=F(-2,5)+F(2*j+1,2*count)*F(1,25)
    rate, der=simpson(x,F(1,25))
    upper=rate[1]+max(abs(der[0]),abs(der[1]))*cell_radius \
          +cell_radius**2/(d+F(1,25))**2
    cells.append(dict(index=j, midpoint=enc(x),
                      midpoint_rate=[enc(v) for v in rate],
                      midpoint_derivative=[enc(v) for v in der],
                      whole_cell_upper=enc(upper)))
box_upper=max(F(row['whole_cell_upper']['numerator'],
                row['whole_cell_upper']['denominator']) for row in cells)
check('whole_rectangle_product_rate',box_upper,'<',F(1,100))
check('negative_high_frequency_rate',F(1,100)-F(1,25)*F(9,4)/A,
      '<',F(-1,50))
check('positive_contour_remainder_rate',F(-41,1000)+F(543,500)/18,
      '=',F(29,1500))
check('remainder_vs_endpoint_lower',F(51,2500)-F(29,1500),'>',F(1,1000))
check('upper_contour_pole_distance',F(3,20)-F(2,25),'=',F(7,100))
check('lower_contour_pole_distance',F(1,25)+F(1,10),'=',F(7,50))
check('box_spatial_denominator_lower',
      (d+F(1,25))**2+F(9,25)**2,'>',1)
check('finite_tail_vs_endpoint',
      F(24,1000)+(F(59657,61952)-1)/6-F(51,2500),'<',F(-1,400))

result=dict(
    purpose='L710 auxiliary exact rates; full signed-residue proof is separate',
    arithmetic='Exact Fractions and integer-directed rational logarithms',
    helper=dict(path=str(helper.relative_to(Path(__file__).parent)),
                sha256=hashlib.sha256(source.encode()).hexdigest(),
                functions=sorted(names)),
    rate_enclosures=dict(omega=[enc(v) for v in omega],
                         endpoint=[enc(v) for v in endpoint],
                         outer_product=[enc(v) for v in point],
                         outer_centered_residue=[enc(v) for v in centered]),
    rectangle_cells=cells, checks=checks,
    failures=[key for key,value in checks.items() if not value['passed']],
    qualifications=['No lower bound for the bump transform',
                    'No upper bound for the complete unit spatial maximum',
                    'Not a proof of positive B_sp/n or of sublinear B_sp',
                    'Contour, Poisson, uniformity and endpoint proofs remain analytic'])
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(result,indent=2)+'\n')
for name,row in checks.items():
    print(f"{name}: actual {row['actual']['decimal_preview']:.12g} "
          f"{row['relation']} required {row['required']['decimal_preview']:.12g}; "
          f"pass={row['passed']}")
print(f"Checks: {len(checks)}; failures: {result['failures']}; certificate: {path}")
if result['failures']:
    raise SystemExit(1)
