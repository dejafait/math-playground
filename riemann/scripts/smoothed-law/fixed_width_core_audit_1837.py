"""Independent application evidence audit of C034a; no evaluator imported.

Integer cell arithmetic is an audit oracle, never an evaluator primitive.
The entire trace is consumed in intended-expression order. Constructor
counts are independently derived from fixed schedules, not read as trusted.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import gzip
import hashlib
import json

BASE = Path(__file__).resolve().parent
OUT = BASE / 'fixed_width_core_audit_1837.json'
SRC = BASE / 'fixed_width_interval_core_1835.json'
TRACE = BASE / 'fixed_width_interval_core_trace_1835.jsonl.gz'
OLD = BASE / 'fixed_width_interval_core_check_1835.json'
H = 2**256


def pair(a):
    return tuple(map(F, a))


def polynomial(p, x):
    return sum(a*x**i for i, a in enumerate(p))


def main():
    if OUT.exists():
        raise SystemExit('Preserve evidence: refuses overwrite audit1837')
    z = json.loads(SRC.read_text())
    old = json.loads(OLD.read_text())
    report = {'status': 'RUNNING', 'failures': [], 'checks': {},
              'scope': 'C034a fixed W=2/W=1 only; independent finite audit; no all-width or global-cap claim'}
    counts = Counter()
    phase = 'coefficients'
    round_id = 0
    events = Counter()
    charged = defaultdict(Counter)
    divs = []
    retained_sizes = {'numerator': 0, 'denominator': 0}
    stream = gzip.open(TRACE, 'rt')

    def check(ok, name):
        if not ok:
            raise AssertionError(name)
        counts[name] += 1

    def event(kind):
        line = stream.readline()
        check(bool(line), 'trace_not_prematurely_exhausted')
        a = json.loads(line)
        check(a['kind'] == kind, 'intended_trace_event_order')
        events[kind] += 1
        return a

    def grid(x):
        check(H % x.denominator == 0, 'retained_grid')
        retained_sizes['numerator'] = max(retained_sizes['numerator'], abs(x.numerator).bit_length())
        retained_sizes['denominator'] = max(retained_sizes['denominator'], x.denominator.bit_length())

    def cell(x):
        nonlocal round_id
        a = event('round')
        round_id += 1
        check(-64 <= x <= 64, 'conversion_range')
        index = min((x+64).numerator*H//(x+64).denominator, 2**263-1)
        lo, hi = F(index, H)-64, F(index+1, H)-64
        check(a['id'] == round_id and a['phase'] == phase and F(a['raw']) == x,
              'conversion_input_and_order')
        check(a['branches'] == format(index, '0263b'), 'all_conversion_branch_decisions')
        check(pair((a['lo'], a['hi'])) == (lo, hi) and lo <= x <= hi,
              'conversion_endpoints_and_closed_containment')
        check(x < hi or x == hi == 64, 'conversion_equality_convention')
        check(a['calls'] == 1054, 'conversion_charge')
        charged[phase].update({'+': 263, '/': 263, 'comparison': 528})
        grid(lo); grid(hi)
        return lo, hi

    def retain(lo, hi):
        return cell(lo)[0], cell(hi)[1]

    def op(k, a, b):
        first = round_id+1
        if k == '+':
            lo, hi = a[0]+b[0], a[1]+b[1]
            cost = {k: 2}
        elif k == '-':
            lo, hi = a[0]-b[1], a[1]-b[0]
            cost = {k: 2}
        else:
            if k == '/':
                check(b[0] > 0 or b[1] < 0, 'interval_divisor_exclusion')
                divs.append({'phase': phase, 'interval': list(map(str, b)),
                             'positive': b[0] > 0, 'negative': b[1] < 0})
            values = [(x*y if k == '*' else x/y) for x in a for y in b]
            lo, hi = min(values), max(values)
            cost = {k: 4, 'comparison': 6 if k == '*' else 12}
        result = retain(lo, hi)
        saved = event('interval')
        check(saved['op'] == k and saved['phase'] == phase and
              pair(saved['a']) == a and pair(saved['b']) == b and pair(saved['out']) == result,
              'complete_interval_operand_output_association')
        check(saved['round_ids'] == [first, round_id] and
              saved['calls'] == 2108+sum(cost.values()), 'interval_charge_and_conversion_association')
        charged[phase].update(cost)
        return result

    def horner(p, x):
        value = p[-1]
        for coefficient in reversed(p[:-1]):
            value = op('+', op('*', value, x), coefficient)
        return value

    try:
        check(hashlib.sha256(TRACE.read_bytes()).hexdigest() == z['evidence']['trace_sha256'], 'trace_hash')
        check(hashlib.sha256(SRC.read_bytes()).hexdigest() == old['certificate_sha256'], 'prior_check_input_hash')
        check(hashlib.sha256((BASE/'fixed_width_interval_core_1835.py').read_bytes()).hexdigest()
              == z['evidence']['script_sha256'], 'evaluator_source_hash')
        # Reconstruct P12 and roots; no old constructor or Boolean trusted.
        previous, current = [F(1)], [F(0), F(1)]
        for n in range(1, 12):
            nxt = [((2*n+1)*(current[k-1] if 1 <= k <= len(current) else 0)
                    - n*(previous[k] if k < len(previous) else 0))/(n+1)
                   for k in range(n+2)]
            previous, current = current, nxt
        ref = z['reference']
        check(current == list(map(F, ref['coefficients'])), 'all_P12_coefficients')
        scan = [polynomial(current, F(j, 128)) for j in range(129)]
        seeds = [j for j in range(128) if scan[j]*scan[j+1] < 0]
        check(seeds == [16, 47, 75, 98, 115, 125] and all(scan), 'all_scan_values_seed_signs')
        positive = []
        for j in seeds:
            lo, hi = F(j, 128), F(j+1, 128)
            sign = polynomial(current, lo) > 0
            for _ in range(160):
                mid = (lo+hi)/2
                value = polynomial(current, mid)
                check(value != 0, 'all_refinement_nonzero_midpoints')
                if (value > 0) == sign:
                    lo = mid
                else:
                    hi = mid
            positive.append((lo, hi))
        brackets = [(-hi, -lo) for lo, hi in reversed(positive)]+positive
        roots = [(lo+hi)/2 for lo, hi in brackets]
        check(brackets == list(map(pair, ref['brackets'])) and roots == list(map(F, ref['midpoints'])),
              'all_root_brackets_and_midpoints')
        check(all(-1 < lo < hi < 1 and (hi-lo)/2 <= F(1, 2**168) and
                  polynomial(current, lo)*polynomial(current, hi) < 0 for lo, hi in brackets),
              'complete_root_isolation_hypotheses')
        check(all(brackets[i+1][0]-brackets[i][1] > F(1, 32) for i in range(11)), 'root_separations')
        weights = []
        for i, root in enumerate(roots):
            p, denominator = [F(1)], F(1)
            for k, other in enumerate(roots):
                if k == i:
                    continue
                new = [F(0)]*(len(p)+1)
                for j, a in enumerate(p):
                    new[j] -= other*a
                    new[j+1] += a
                p = new
                check(root != other, 'every_cardinal_divisor_factor_nonzero')
                denominator *= root-other
            weights.append(sum(2*p[j]/(j+1) for j in range(0, len(p), 2))/denominator)
        check(weights == list(map(F, ref['weights'])), 'all_cardinal_integral_weights')
        # Imported finite inequality constants, with their domains checked in prose.
        ds = F(4**22, factorial(23))/(1-F(16, 24*25))
        de = F(8*2**15, factorial(17)); dt = ds/4; dr = (de+dt)/2+2*ds
        check(0 < F(16, 24*25) < 1 and dr < F(1, 2**28), 'truncation_rational_inequality')
        check(F(48, factorial(41))+F(8, 2**169) < F(1, 2**150), 'Gaussian_import_inequality')
        coefficients = {'T40': [F(1, factorial(k)) for k in range(41)],
                        'E16': [F(1, 2**k*factorial(k)) for k in range(1, 17)],
                        'U10': [F(1, factorial(2*j+1)) for j in range(1, 11)]}
        check({k:list(map(str,v)) for k,v in coefficients.items()} == z['coefficients'], 'all_Taylor_coefficients')
        ti, ei, ui = ([cell(x) for x in coefficients[k]] for k in ['T40','E16','U10'])
        qlo, qhi = F(0), F(1)
        branches = ''
        for _ in range(64):
            mid = (qlo+qhi)/2
            if 2*mid*mid > 1:
                qhi = mid; branches += '0'
            else:
                qlo = mid; branches += '1'
        q = (qlo+qhi)/2
        check(branches == z['q']['branches'] and (qlo,qhi) == pair(z['q']['bracket']) and
              q == F(z['q']['qhat']) and 2*qlo*qlo <= 1 <= 2*qhi*qhi and qhi-qlo == F(1,2**64),
              'complete_q_bisection_and_error_contract')
        grid(q); grid(F(1)); grid(F(0)); grid(F(2)); grid(F(-16))
        phase = 'input_gaussians'
        check(len(z['inputs']) == 48, 'input_list_complete')
        input_data = []
        for j,d in enumerate(z['inputs']):
            panel, i = divmod(j, 12)
            x = panel+(1+roots[i])/2
            w = min(F(1), max(F(0), weights[i]/2))
            check(0 < x < 4 and 0 < weights[i]/2 < 1, 'exact_input_ranges_clamp_branches')
            xi, wi = cell(x), cell(w)
            g = horner(ti, op('/',op('*',xi,xi),(F(-16),)*2))
            check(g[0] >= 0 and g[1] >= 0, 'Gaussian_clamp_count_branch')
            gc = tuple(min(F(1), max(F(0), t)) for t in g)
            saved = event('clamp')
            check(pair(saved['in']) == g and pair(saved['out']) == gc, 'Gaussian_clamp_trace')
            g = gc
            for _ in range(4):
                g = op('*',g,g)
            e = g[0]
            error = g[1]-g[0]+F(48,factorial(41))+F(8,2**169)
            check(0 <= e <= 1 and error <= F(1,2**60), 'Gaussian_input_original_contract')
            expected = {'panel':panel,'node':i,'xhat':str(x),'what':str(w),'ehat':str(e),
                        'gaussian_poly_interval':list(map(str,g)),'true_gaussian_error':str(error),
                        'x_interval':list(map(str,xi)),'weight_interval':list(map(str,wi))}
            check(d == expected, 'all_saved_input_data')
            input_data.append((xi,wi,e,error))
        check(max(t[3] for t in input_data) == F(z['max_gaussian_input_error']), 'maximum_Gaussian_error')
        sums = {}
        for width,qhat in [(1,F(1)),(2,q)]:
            phase = f'core_W{width}'
            total = (F(0),)*2
            rows = z['contributions'][str(width)]
            check(len(rows) == 48, 'complete_width_contributions')
            for j,(xi,wi,e,_) in enumerate(input_data):
                a = op('*',wi,(e,e)); x = op('*',xi,(qhat,qhat)); v = op('*',x,x)
                E = horner(ei,x); U = horner(ui,v); T = op('*',x,U)
                S = op('+',(F(1),)*2,op('*',x,T)); den = op('*',(F(2),)*2,S)
                A = op('/',op('-',E,T),den); term = op('*',a,A); total = op('+',total,term)
                expected = {'index':j, **{k:list(map(str,t)) for k,t in
                            [('z',x),('S10',S),('divisor',den),('A',A),('term',term),('prefix',total)]}}
                check(rows[j] == expected, 'complete_width_row')
            sums[str(width)] = op('*',(qhat,qhat),total)
            check(sums[str(width)] == pair(z['sums'][str(width)]), 'complete_width_sum')
        phase = 'final_error'
        diff = op('-',sums['2'],sums['1']); allowance = 8*dr+F(2048,2**60)
        check(diff == pair(z['approximate_difference_interval']), 'approximate_difference')
        check([F(z['error'][k]) for k in ['dE','dS','dT','dR','total_allowance']]
              == [de,ds,dt,dr,allowance], 'all_R_based_enlargement_terms')
        final = retain(diff[0]-allowance,diff[1]+allowance)
        radius = (final[1]-final[0])/2
        check(final == pair((z['final']['lo'],z['final']['hi'])) and
              radius == F(z['final']['radius']) and radius < F(1,2**24) and
              (final[0]+final[1])/2 == F(z['final']['center']), 'final_exact_enclosure_radius_center')
        check(not stream.readline(), 'entire_trace_consumed')
        check(divs == z['divisors'] and len(divs) == 144, 'every_interval_divisor_in_order')
        minimum = min(F(d['interval'][0]) for d in divs if d['phase'].startswith('core_'))
        check(minimum == F(old['minimum_core_divisor']) and minimum > 2, 'minimum_positive_core_divisor')
        # Counts of untraced work, derived from actual fixed loops and the
        # branch exclusions above. Each rational division adds a zero test.
        residual = {}
        residual['constants'] = Counter({'+':255,'/':256+60+168,'comparison':256+60+168,'-':1})
        r = Counter()
        cells = sum(n+2 for n in range(1,12))
        r.update({'*':2*cells,'-':cells,'/':cells,'comparison':cells})
        r.update({'/':129,'comparison':129})
        r.update({'*':129*12,'+':129*12})
        r.update({'*':128,'comparison':128})
        r.update({'*':6*12,'+':6*12,'comparison':6})
        r.update({'+':960*13,'*':960*12,'/':960,'comparison':960*3})
        r.update({'-':12,'+':12,'/':12,'comparison':12})
        factor_ops = 12*(sum(range(1,12))+11)
        r.update({'*':factor_ops,'-':factor_ops})
        r.update({'*':72,'+':72,'/':72+12,'comparison':72+12})
        residual['reference_construction'] = r
        residual['coefficients'] = Counter({'*':41+2*16,'/':67,'comparison':67,'-':1})
        residual['q_construction'] = Counter({'+':65,'/':65,'*':128,'comparison':65+64+2})
        residual['input_gaussians'] = Counter({'+':48*4,'-':48,'*':48,'/':2+48*2,
                                               'comparison':2+48*(2+2+2+4)})
        residual['core_W1'] = Counter(); residual['core_W2'] = Counter()
        residual['final_error'] = Counter({'-':3,'+':5,'*':43,'/':32,'comparison':33})
        allcounts = {}
        for phase,rest in residual.items():
            check(rest == Counter(old['untraced_constructor_and_error_counts'][phase]), 'independent_untraced_count')
            allcounts[phase] = charged[phase]+rest
            check(allcounts[phase] == Counter(z['ledger']['by_phase'][phase]), 'complete_phase_primitive_ledger')
        total = sum(sum(x.values()) for x in allcounts.values())
        check(total == z['ledger']['total'] == 20921533, 'complete_local_count')
        check(dict(events) == z['ledger']['trace_events'] and round_id == 19755 and
              z['ledger']['interval_retains'] == events['interval']+1, 'complete_event_and_retention_counts')
        check(retained_sizes == z['grid']['retained_endpoint_max_bits'], 'retained_bit_maxima')
        report.update({'status':'PASS_FIXED_INSTANCE_APPLICATION_AUDIT',
                       'final_enclosure':list(map(str,final)), 'radius':str(radius),
                       'required_radius':str(F(1,2**24)), 'minimum_core_divisor':str(minimum),
                       'maximum_Gaussian_input_error':str(max(t[3] for t in input_data)),
                       'grid_denominator_exponent':256,'events_checked':dict(events),
                       'untraced_counts_independently_derived':{k:dict(v) for k,v in residual.items()},
                       'all_phase_counts':{k:dict(v) for k,v in allcounts.items()}, 'local_operations':total,
                       'legacy_global_cap':1000000,'global_cap_claimed':False,
                       'analytic_proof_location':'lemmas/C034a-fixed-width-dyadic-interval-core.md, audit1837',
                       'not_certified':['all widths','runtime','temporary bit maxima','full scalar','actual-Xi positivity',
                                        'source-wide correctness','finite-zero inputs','matching Mathlib theorem']})
    except Exception as exc:
        report['status'] = 'STOP_FIRST_UNSUPPORTED_CHECK'
        report['failures'].append(str(exc))
    finally:
        stream.close()
        report['checks'] = dict(counts); report['total_checks'] = sum(counts.values())
        report['source_hashes'] = {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [SRC,TRACE,OLD]}
        OUT.write_text(json.dumps(report,indent=2)+'\n')
        print(report['status'], 'checks:',report['total_checks'],'failures:',report['failures'])
        if 'radius' in report:
            print('Radius:',float(F(report['radius'])),'required <',2**-24,
                  '; local operations:',report['local_operations'],'; no global cap claimed')
            print('All events:',report['events_checked'],'; endpoint denominator divides 2^256')
        print('Full certificate:',OUT.relative_to(BASE.parent.parent))


if __name__ == '__main__':
    main()
