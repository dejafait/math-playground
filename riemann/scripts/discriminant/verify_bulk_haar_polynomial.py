"""Read complete step-192 evidence and replay signed expectation arithmetic."""
import json
from fractions import Fraction as F
from pathlib import Path
import enclose_bulk_haar_integral as base


def main():
    p = Path(__file__).parent
    x = json.loads((p/'bulk-haar-polynomial-expectation-192.json').read_text())
    n = json.loads((p/'bulk-haar-polynomial-nodes-192.json').read_text())
    b = json.loads((p/'bulk-haar-polynomial-preflight-192.json').read_text())
    def bounds(r):
        return F(r['lower']), F(r['upper'])
    checks = {}
    checks['saved_checks'] = all(x['checks'].values()) and all(n['checks'].values()) and all(b['checks'].values())
    checks['moment_order_list'] = x['orders'] == sorted({k for r in x['expectations']
                                                       for k, v in enumerate(r['polynomial']) if any(bounds(v))})
    checks['local_ratios'] = all(F(r['next_ratio']) == F((r['j']+r['e'])**2,
                                (r['e']+1)**2*r['p']**5) < 1 for r in x['local_factors'])
    checks['global_tails'] = all(F(r['prime_log_tail']) == F(r['j']**2, 4*200**4)/
                               (1-F(r['j']**2, 201**5)) < 1 for r in x['moments'])
    checks['node_coefficients_contain_zero'] = all(bounds(r)[0] <= 0 <= bounds(r)[1]
                                                  for r in n['chebyshev_coefficients'])
    checks['all_node_values_contain_zero'] = all(bounds(r)[0] <= 0 <= bounds(r)[1] for r in n['nodes'])
    checks['angular_mass_one'] = sum(F(1, r['count']) for r in b['cells']) == 1
    coverage = [k for r in b['cells'] for k in range(r['cell']*((1<<14)//r['count']),
                                                   (r['cell']+1)*((1<<14)//r['count']))]
    checks['angular_disjoint_partition'] = len(coverage) == len(set(coverage)) == 1<<14
    raw_full = sum(bounds(r['raw_expectation'])[0] <= -1 and bounds(r['raw_expectation'])[1] >= 1
                   for r in x['expectations'][1:])
    result = bounds(x['integral'])
    checks['zero_and_failed_width'] = result[0] < 0 < result[1] and result[1]-result[0] > F(x['required_width'])
    checks['coarse_result'] = F(-2625, 1000) < result[0] and result[1] < F(2616, 1000)
    callbacks = 8+1024+1024+b['angular_callbacks']+n['selector_replay_callbacks']+n['angular_boxes']
    checks['node_total_below_cap'] = callbacks <= 65536
    base.SCALE = 10**160
    def decode(rec):
        lo, hi = bounds(rec)
        return base.I(base.I(lo).lo, base.I(hi).hi, True)
    moments = {0: base.I(1), **{r['j']: decode(r['moment']) for r in x['moments']}}
    total = base.I(0)
    for record in x['expectations']:
        raw = sum((decode(v)*moments[k] for k, v in enumerate(record['polynomial'])
                   if any(bounds(v))), base.I(0))
        assert raw.enc() == record['raw_expectation']
        bounded = raw.intersect(base.I(-base.SCALE, base.SCALE, True))
        assert bounded.enc() == record['bounded_expectation']
        term = decode(record['coefficient'])*bounded
        assert term.enc() == record['term']
        total = total+term
    assert total.enc() == x['polynomial_expectation']
    radius = base.I(F(x['uniform_radius'])).hi
    final = base.I(total.lo-radius, total.hi+radius, True)
    checks['complete_signed_expectation_replay'] = final.enc() == x['integral']
    assert all(checks.values())
    summary = {'checks': checks, 'raw_nonconstant_expectations_cover_full_unit_interval': raw_full,
               'local_factors': len(x['local_factors']), 'orders': len(x['orders']),
               'all_nodes_and_coefficients_inspected': True, 'angular_boxes_total': callbacks,
               'integral': x['integral'], 'width': x['width'], 'required': x['required_width'],
               'failures': x['failures']}
    out = p/'bulk-haar-polynomial-verification-192.json'
    out.write_text(json.dumps(summary, indent=2)+'\n')
    print('All checks passed:', len(checks), '; full signed expectation replay included.')
    print('Raw nonconstant expectations covering [-1,1]:', raw_full, 'of 32')
    print('Local factors / orders / total angular boxes:', len(x['local_factors']), len(x['orders']), callbacks)
    print('Actual / required width:', float(F(x['width'])), float(F(x['required_width'])))
    print('Failures:', x['failures'])
    print('Verification certificate:', out)


if __name__ == '__main__':
    main()
