#!/usr/bin/env python3
"""Check every saved cell and rational margin, not the analytic calculation."""
import hashlib
import json
from fractions import Fraction as R
from pathlib import Path


def main():
    p = Path(__file__).with_name('contact-certificate-896.json')
    d = json.loads(p.read_text())
    scale = 1 << d['bits']
    checked = []
    assert d['status'] == 'COMPACT_CERTIFIED_ENDPOINT_JOIN_OPEN'
    assert d['endpoint_join_proved'] is False and d['first_contact_proved'] is False
    assert len(d['segments']) == 2
    for s, span, mode in zip(d['segments'],
                             [('139/32', '35/8'), ('1/32', '139/32')],
                             ['decreasing', 'positive']):
        assert s['interval'] == list(span) and s['mode'] == mode and s['complete']
        assert not s['failures'] and not s['unprocessed']
        cursor = R(span[0])
        for row in s['cells']:
            a, b = R(row['left']), R(row['right'])
            assert a == cursor and a < b
            cursor = b
            R(row['tilt'])
            for key in ['Q_tilt', 'F', 'Z', 'Zprime']:
                lo, hi = map(int, row[key])
                assert lo <= hi
            assert int(row['Q_tilt'][0]) > 0
            if mode == 'positive':
                assert R(int(row['Z'][0]), scale) > R(1, 4000000)
            else:
                assert R(int(row['Zprime'][1]), scale) < R(-213, 1000000) < R(-1, 5000)
        assert cursor == R(span[1])
        checked.append({'interval':list(span), 'cells':len(s['cells']),
                        'all_cells_checked':True, 'failures':[]})
    assert [r['x'] for r in d['endpoints']] == ['139/32', '35/8']
    for row, lo, hi in zip(d['endpoints'],
                           [R(5694, 10**9), R(-2495, 10**9)],
                           [R(5695, 10**9), R(-2494, 10**9)]):
        assert lo < R(int(row['Z'][0]), scale) <= R(int(row['Z'][1]), scale) < hi
        for key in ['F', 'Z', 'Zprime']:
            a, b = map(int, row[key])
            assert a <= b
    assert int(d['summary']['minimum_prefix_Z_lower']) == min(
        int(c['Z'][0]) for c in d['segments'][1]['cells'])
    assert int(d['summary']['maximum_contact_Zprime_upper']) == max(
        int(c['Zprime'][1]) for c in d['segments'][0]['cells'])
    out = p.with_name('contact-certificate-ledger-check-896.json')
    result = {
        'status':'PASS',
        'scope':'Full saved-cell coverage and rational inequalities; not an independent analytic or arithmetic replay.',
        'certificate_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
        'checked':checked,
        'proved_bounds':{'prefix_Z':'>1/4000000', 'contact_Zprime':'<-213/1000000',
                         'required_contact_Zprime':'<-1/5000'},
        'unresolved':d['summary']['unresolved']}
    out.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS:', sum(s['cells'] for s in checked),
          'closed cells checked; no gap, overlap, unresolved cell or failed inequality.')
    print('Actual prefix Z > 1/4000000; required > 0.')
    print('Actual contact Zprime < -213/1000000; required < -1/5000.')
    print('Endpoint enclosures: (5694,5695)/1e9 and (-2495,-2494)/1e9.')
    print('Unresolved: endpoint join on (0,1/32), first contact, and critical audit.')
    print('Full check:', out)


if __name__ == '__main__':
    main()
