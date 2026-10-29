"""L140 audit supplement: printed evidence and complete real quotient.

Consumes the full independently replayed certificate. No new witness search,
upstream arithmetic, or finite-place computation. Run the existing verifier
first. The mathematical component/generation argument is in canonical L140.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
import traceback

HERE = Path(__file__).resolve().parent
OUT = HERE / 'real-kummer-audit.json'
R = dict(completed=False, failures=[], bindings={}, checks=[])


def need(name, condition):
    R['checks'].append(dict(name=name, passed=bool(condition)))
    if not condition:
        raise AssertionError(name)


def load(name):
    raw = (HERE / name).read_bytes()
    R['bindings'][name] = sha256(raw).hexdigest()
    return json.loads(raw)


def phi(mask):
    return [mask & 1, ((mask >> 1) ^ (mask >> 2)) & 1]


def main():
    d = load('real-kummer-certificate.json')
    v = load('real-kummer-verification.json')
    old = load('real-kummer-preaudit-verification.json')
    need('producer and complete replay accepted',
         d['completed'] and v['completed'] and not d['failures'] and not v['failures'])
    need('replay consumes exact entire producer',
         v['bindings']['real-kummer-certificate.json'] == R['bindings']['real-kummer-certificate.json'])
    need('all replay evidence unchanged', v == old and v['checks'] == 1118)
    need('all bound inputs remain bound', all(v['bindings'][k] == h for k,h in d['bindings'].items()))
    need('printed producer hash', R['bindings']['real-kummer-certificate.json'] ==
         '1abd068db5a72c8ffd06d2670d5e4dbfd1c20efff75698f0dd944e430c6064d9')
    need('all producer checks pass', all(c['passed'] is True for c in d['checks']))
    need('printed final root intervals', d['alpha_intervals'] ==
         [['-48','-47'],['-34','-33'],['-7/2','-13/4'],['20','21']])
    need('printed eta intervals', d['eta_intervals'] ==
         [['453750/49','907500/97'],['75625/7','907500/83'],
          ['1815000/107','1210000/71'],['30250','907500/29']])
    need('printed six sample abscissae', [r['sample'] for r in d['gaps']] ==
         ['9074','898425/98','13688125/1358','123873750/8881','1678875/71','907529/29'])
    need('printed refined endpoint values', [r['value'] for r in d['refinements']] ==
         ['57897/16','-1088271/256'])
    need('complete real generator masks', d['local_rows'] == [30,24,0,0])
    selected = {w['id']:w for w in d['witnesses']}
    source = {e['tuple_id']:e for e in d['input_accepted_records']}
    expected = [
        (0, [-2,-2,-2,-2], -36000, [1,0,0,0,1],
         {26:5,27:1,28:1,30:3}, ['-76/15','-1139/375','-614/9375','-1/9375'],
         [['3891/3125','42404/9375'],['240293/9375','53978/1875'],
          ['1219087/300000','241163/50000'],['-185102/1875','-11608/125']]),
        (152, [-1,-1,-2,0], 13500, [0,1,0,0,1],
         {26:2,27:2,28:1,29:1,30:1,31:1}, ['-2','-39/25','-1/25','0'],
         [['-482/25','-426/25'],['23/5','154/25'],
          ['523/200','601/200'],['-262/5','-246/5']])]
    R['decisive_evidence'] = []
    for t,coeffs,n,bits,sparse,power,boxes in expected:
        w = selected['tuple-'+str(t)]
        vals = [sparse.get(i,0) for i in range(32)]
        need('complete printed witness '+str(t),
             w['coefficients'] == coeffs == source[t]['coefficients'] and
             w['signed_norm'] == n and w['sign_bits'] == bits and
             w['valuations'] == vals == source[t]['valuations'] and
             w['power_coefficients'] == power and w['alpha_value_intervals'] == boxes)
        need('supported inverse norm '+str(t), F(w['inverse_norm']) == 1/F(n) and
             all(x == 0 for i,x in enumerate(vals) if i not in d['S_indices']))
        R['decisive_evidence'].append(dict(witness=w, source_record=source[t], phi=phi(w['mask'])))
    E = [m for m in range(32) if m.bit_count()%2 == 0]
    W = sorted({0,30,24,30^24})
    table = [dict(mask=m, phi=phi(m), in_W=m in W) for m in E]
    need('entire quotient kernel equals W', [m for m in E if phi(m)==[0,0]] == W)
    need('entire quotient is onto', {tuple(phi(m)) for m in E} == {(0,0),(1,0),(0,1),(1,1)})
    need('two witnesses have independent quotient images',
         [e['phi'] for e in R['decisive_evidence']] == [[1,0],[0,1]])
    need('complete replay spans match printed quotient', v['local_span'] == W and
         v['full_real_norm_kernel'] == E and v['quotient_basis_ids'] == ['tuple-0','tuple-152'])
    R['quotient_table'] = table
    R['bound_cases'] = [dict(c=c, ambient=11+c, filtered=9+c,
                            rank_upper=8+c, required_upper=1, shortfall=7+c) for c in range(3)]
    need('all bound arithmetic', all(r['filtered'] == r['ambient']-2 and
         r['rank_upper'] == r['filtered']-1 and r['shortfall'] == r['rank_upper']-1
         for r in R['bound_cases']))
    need('complete fixed-domain counts', d['result']['accepted']==182 and
         d['result']['retained_box']==34 and d['result']['rejected_box']==148 and
         len(d['witnesses'])==39 and d['result']['matrix_columns']==43)
    R['bounds'] = dict(witnesses=[39,187], coordinates=[5,5], combined_columns=[43,192],
                       quotient_cases=[16,16], class_cases=[3,3],
                       bisections=d['bisections'], bisections_per_root_cap=64,
                       producer_bits=[d['bounds']['max_rational_bits'],4096],
                       replay_bits=[v['bounds']['max_rational_bits'],4096])
    need('reported actual bounds', d['bisections']==[0,0,2,0] and
         d['bounds']['max_rational_bits']==v['bounds']['max_rational_bits']==135)
    R['result'] = dict(verdict='ACCEPT', new_mathematical_bound=False,
                       local_image_dimension=2, restriction_rank=2,
                       filtered_dimension='9+c', rank_bound='8+c',
                       unconditional_rank_upper_bound=10, required_rank_upper_bound=1)
    R['completed'] = True


try:
    main()
except Exception as exc:
    R['failures'].append(dict(error=str(exc), traceback=traceback.format_exc()))
finally:
    OUT.write_text(json.dumps(R, indent=2)+'\n')
    print(json.dumps(dict(completed=R['completed'], checks=len(R['checks']),
                          result=R.get('result'), bounds=R.get('bounds'),
                          failures=R['failures'], certificate=str(OUT))))
if not R['completed']:
    raise SystemExit(1)
