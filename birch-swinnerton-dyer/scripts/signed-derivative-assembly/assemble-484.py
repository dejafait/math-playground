"""One application of audited L116; never imports a kernel implementation."""
import hashlib
import json
import pathlib
import re
import sys
import time
from fractions import Fraction as F

START = float(sys.argv[1])
OUT = pathlib.Path('scripts/signed-derivative-assembly/step-484')
OUT.mkdir(exist_ok=False)
inventory = {}
selected = []
stage = 'setup'

def check(ok, message):
    if not ok:
        raise ValueError(message)
    if time.time() - START >= 180:
        raise ValueError('inclusive 180-second cap reached')

def load(path):
    path = str(path)
    data = pathlib.Path(path).read_bytes()
    entry = {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
    if path in inventory:
        check(inventory[path] == entry, 'input changed: ' + path)
    inventory[path] = entry
    return json.loads(data) if path.endswith('.json') else data.decode()

def save(name, obj):
    (OUT / name).write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n')

def pair(x):
    check(isinstance(x, list) and len(x) == 2 and
          all(type(v) is int for v in x) and x[1] > 0, 'invalid rational pair')
    return F(*x)

def export(x):
    return [x.numerator, x.denominator]

def bind(path, audit):
    inv = load(audit + '/initial-inventory.json')
    obj = load(path)
    check(path in inv and inventory[path] == inv[path], 'audit binding failed: ' + path)
    return obj

try:
    stage = 'coefficient binding'
    cp = 'scripts/finite-derivative-coefficients/certificate.json'
    coeff = bind(cp, 'scripts/finite-derivative-coefficients/step-410')
    check(inventory[cp]['sha256'] == '9ad5f8b621dab84edeb97b891f5d4ed9cfe6d11c43b1b7b7f8e2b7147780363f', 'coefficient canonical hash')
    check(coeff['model'] == [0,1,1,-2,0] and coeff['N'] == 389 and
          coeff['selected_attempt'] == 0 and coeff['normalization'] ==
          'a_1=1; full untwisted unnormalized newform coefficients', 'coefficient normalization')
    rows = coeff['export_indices_1_through_128']
    check([r['n'] for r in rows] == list(range(1,129)), 'coefficient indices')
    check(all(type(r['a_n']) is int and r['a_n'] ==
              coeff['coefficients_with_index_zero_sentinel'][r['n']] for r in rows), 'export slots')
    check(coeff['upstream_path'] == 'scripts/twist-five/certificate.json' and
          coeff['upstream_sha256'] == '7547b371d675441190256195270c9282213e888cdb666451ae21a062896e4415', 'upstream binding')
    check(rows[0]['a_n'] == 1, 'a_1 normalization')
    stage = 'whole parameter binding'
    pp = 'scripts/first-rational-kernel/step-404/parameter.json'
    parameter = bind(pp, 'scripts/first-rational-kernel/step-406')
    D = 2**256
    cl, cu = [F(v,D) for v in parameter['c_grid']]
    midpoint, delta = pair(parameter['midpoint']), pair(parameter['delta'])
    check(F(3,10) <= cl <= cu <= F(1,2) and midpoint == (cl+cu)/2 and
          delta == (cu-cl)/2 and delta <= F(1,2**50), 'parameter values/range')
    check(parameter['c_grid'] == [36887902191165742374446831090090100164633110307723623187031015736440321082816,
                                36887902191165742374446831090090100380471044238365418461395933078627191865791], 'canonical parameter')
    blocks = [(1,1,103,404,406),(2,2,104,412,415),(3,6,105,417,422),
              (7,10,106,424,446),(11,14,107,431,433),(15,18,108,435,437),
              (19,22,109,440,442),(23,26,110,449,451),(27,30,111,453,455),
              (31,34,112,457,459),(35,38,113,461,463),(39,42,114,468,470)]
    for lo,hi,lid,prod,aud in blocks:
        stage = 'kernel binding n=' + str(lo)
        lemma = next(pathlib.Path('lemmas').glob('L%d-*.md' % lid))
        text = load(lemma)
        check('separate' in text and 'audit' in text, 'missing audit statement')
        base = ('scripts/first-rational-kernel' if lo == 1 else
                'scripts/second-rational-kernel' if lo == 2 else 'scripts/four-rational-kernels')
        audit = base + '/step-' + str(aud)
        for n in range(lo,hi+1):
            root = base + '/step-' + str(prod) + ('' if n<=2 else '/n-'+str(n))
            kernel = bind(root+'/kernel.json', audit)
            par = bind(root+'/parameter.json', audit)
            check(par == parameter, 'whole parameter mismatch n='+str(n))
            check(kernel['n'] == n and kernel['grid_denominator'] == D and
                  kernel['complete_panels'] == 1016, 'kernel identity')
            l,u = kernel['final_grid']
            check(type(l) is int and type(u) is int and l <= u, 'invalid endpoints')
            if n<=2:
                check(str(l) in text and str(u) in text, 'canonical endpoint mismatch')
            else:
                table = re.search(r'^\| '+str(n)+r' \| (\d+) \| (\d+) \|', text, re.M)
                check(table is not None and [int(table[1]),int(table[2])] == [l,u], 'canonical table mismatch')
            j,e = F(l+u,2*D), F(u-l,2*D)
            check(pair(kernel['midpoint']) == j and pair(kernel['radius']) == e and
                  0 <= e < F(1,2**183), 'kernel midpoint/radius')
            a = rows[n-1]['a_n']
            check(abs(a)<=n, 'selected coefficient majorant')
            selected.append({'n':n,'a_n':a,'kernel_path':root+'/kernel.json',
                             'parameter_path':root+'/parameter.json','audit':audit,
                             'canonical_lemma':str(lemma),'kernel':kernel,
                             'l':export(F(l,D)),'u':export(F(u,D)),
                             'j':export(j),'e':export(e)})
    stage = 'exact signed arithmetic'
    check(len(selected)==42, 'missing selected kernel')
    center = sum((4*F(r['a_n'],r['n'])*pair(r['j']) for r in selected), F(0))
    reverse = sum((4*F(r['a_n'],r['n'])*pair(r['j']) for r in reversed(selected)), F(0))
    width = sum((4*F(abs(r['a_n']),r['n'])*pair(r['e']) for r in selected), F(0))
    # Independent common-denominator integer center, then direct signed intervals.
    import math
    Q = math.lcm(*[r['n'] for r in selected])*2*D
    integer_center = F(sum(4*r['a_n']*(r['kernel']['final_grid'][0]+r['kernel']['final_grid'][1])*(Q//(r['n']*2*D)) for r in selected),Q)
    lower=F(0); upper=F(0)
    for r in reversed(selected):
        x,y = 4*F(r['a_n'],r['n'])*pair(r['l']), 4*F(r['a_n'],r['n'])*pair(r['u'])
        lower += min(x,y); upper += max(x,y)
    check(center==reverse==integer_center and lower==center-width and upper==center+width, 'independent arithmetic disagreement')
    analytic = F(1,2**43)
    transfer = 200*delta
    beta = F(130,387*2**14)
    radius = analytic+transfer+beta+width
    left,right = center-radius,center+radius
    save('selected-inputs.json', {'parameter':parameter,'coefficient_certificate':coeff,
                                 'selected':selected,'inventory':inventory})
    save('certificate.json', {'status':'ASSEMBLED_REQUIRES_SEPARATE_AUDIT',
         'center':export(center),'eta':[0,1], 'allowances':{'original_analytic_remainders':export(analytic),
         'full_sum_parameter_transfer':export(transfer),'discarded_block':export(beta),'retained_kernel_widths':export(width)},
         'radius':export(radius),'left':export(left),'right':export(right),
         'zero_excluded':left>0 or right<0,'positive':left>0,
         'radius_below_2^-14':radius<F(1,2**14),'radius_below_2^-40':radius<F(1,2**40),
         'comparisons':{'reverse_sum':center==reverse,'integer_common_denominator':center==integer_center,'direct_interval':lower==center-width and upper==center+width},
         'qualifications':'Imports audited containment and analytic inputs unchanged; no integration replay or new BSD case. Historical timing and document transitions remain qualified.'})
    stage = 'post-write input preservation'
    for p,entry in list(inventory.items()):
        load(p)
    save('preservation.json',{'all_match':True,'count':len(inventory),'files':inventory})
    print('ASSEMBLED; zero_excluded=%s; 1.5<center<1.6=%s; radius<2^-14=%s; radius<2^-40=%s; inputs=%d' %
          (left>0 or right<0,F(3,2)<center<F(8,5),radius<F(1,2**14),radius<F(1,2**40),len(inventory)))
except Exception as exc:
    save('failure.json',{'stage':stage,'first_failure':str(exc),'elapsed_since_setup':time.time()-START,'inventory':inventory,'selected':selected})
    print('STOP:',stage,str(exc))
    sys.exit(1)

size=sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file())
check(size < 134217728,'output byte cap')
print('Certificate:',OUT/'certificate.json','elapsed inclusive so far:',time.time()-START,'new output bytes:',size,'required caps: 180 seconds, 134217728 bytes')
