"""Read and replay every final step-194 cell, branch, jet and error bound."""
import json
from fractions import Fraction as F
from pathlib import Path
import certify_bulk_conditional_sign as c


def main():
    directory = Path(__file__).parent
    data = json.loads((directory/'bulk-haar-conditional-sign-194.json').read_text())
    for k in c.calls:
        c.calls[k] = 0
    centers = [F(s['g']) for s in data['centers']]
    gs = [c.I(g) for g in centers]
    checks = {'generator_checks': all(data['checks'].values())}
    a, z = [F(data['g_full_range'][k]) for k in ('lower', 'upper')]
    checks['exact_three_centers'] = centers == [a, (a+z)/2, z]
    cells = data['cells']
    checks['full_partition'] = (F(cells[0]['left']) == 0 and F(cells[-1]['right']) == 1
        and all(x['right'] == y['left'] for x,y in zip(cells,cells[1:]))
        and all(F(x['right'])-F(x['left']) == F(x['mass']) > 0 for x in cells)
        and sum((F(x['mass']) for x in cells),F(0)) == 1)
    for r in cells:
        replay, _ = c.cell(F(r['left']), F(r['right']), gs)
        assert json.loads(json.dumps(replay)) == r, ('full cell replay mismatch', r['left'], r['right'])
    checks['all_selector_branches_jets_and_integrals_replayed'] = True
    for k,s in enumerate(data['centers']):
        lo = sum(F(r['values'][k]['integral']['lower']) for r in cells)
        hi = sum(F(r['values'][k]['integral']['upper']) for r in cells)
        assert s['value'] == {'lower':str(lo),'upper':str(hi)}
    checks['exact_complete_aggregates'] = True
    low, high = data['centers'][0]['value'], data['centers'][2]['value']
    checks['opposite_endpoint_signs'] = F(low['upper']) < 0 < F(high['lower'])
    checks['convenient_rational_sign_margins'] = F(low['upper']) < -F(1,3000) and F(high['lower']) > F(1,1200000)
    checks['initial_work_cap'] = data['callback_total'] <= data['initial_callback_cap']
    failed = json.loads((directory/'bulk-haar-conditional-sign-194-verifier-failed.json').read_text())['total_callbacks']
    total = data['callback_total']+failed+c.count()
    checks['complete_work_cap'] = total <= data['total_callback_cap']
    checks['leaves_and_precision_caps'] = len(cells) <= 4096 and data['precision_places'] <= 160
    checks['correct_stop'] = data['reason'] == 'CERTIFIED_OPPOSITE_POINT_SIGNS' and not data['failures']
    checks['unresolved_mass'] = F(data['unresolved_mass']) == sum((F(r['mass']) for r in cells if r['values'][0]['kind']=='unresolved'),F(0))
    assert all(checks.values())
    out = {'checks':checks, 'terminal_cells':len(cells),
           'strict_cells':sum(r['values'][0]['kind']=='strict' for r in cells),
           'unresolved_cells':sum(r['values'][0]['kind']=='unresolved' for r in cells),
           'initial_callbacks':data['callback_total'], 'verification_callbacks':c.calls,
           'failed_verifier_and_recovery_callbacks':failed, 'verification_callback_total':c.count(), 'complete_callback_total':total,
           'required_total_callback_cap':data['total_callback_cap'],
           'complete_center_evidence':data['centers'],
           'no_response_transport_needed':'Opposite endpoint signs already refute the tested uniform-sign condition.',
           'failures':[]}
    path = directory/'bulk-haar-conditional-sign-verification-194.json'
    path.write_text(json.dumps(out,indent=2)+'\n')
    print('All checks passed:',len(checks),'; all cell branches, jets and integral errors replayed.')
    print('Initial / verification / total / cap:', data['callback_total'],c.count(),total,data['total_callback_cap'])
    print('Strict / unresolved cells:',out['strict_cells'],out['unresolved_cells'])
    print('Certified margins: A(a)<-1/3000; A(b)>1/1200000')
    print('Failures:',out['failures'])
    print('Verification certificate:',path)


if __name__ == '__main__':
    main()
