"""Exact arithmetic propagation of C057a's imported trace enclosures.

The trace identity, torus bound and group overlap are proved in C057a;
this certificate checks their rational endpoint arithmetic only.
L047's interval induction and IEEE model remain input qualifications.
"""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).parent
OUTPUT = ROOT / 'physical-strain-comparison-certificate.json'


def rational(q):
    return dict(num=str(q.numerator), den=str(q.denominator))


def imported(q):
    return F(int(q['num']), int(q['den']))


def interval(pair):
    return dict(lower=rational(pair[0]), upper=rational(pair[1]),
                endpoints='open')


def finite_decimal(q):
    # All printed endpoints below have denominators dividing 10^12.
    scaled = q * 10**12
    if scaled.denominator != 1:
        raise ValueError('nonterminating printed endpoint')
    sign = '-' if scaled < 0 else ''
    whole, rem = divmod(abs(scaled.numerator), 10**12)
    return (f'{sign}{whole}.{rem:012d}').rstrip('0').rstrip('.')


def main():
    source = ROOT / 'companion-enclosure-certificate.json'
    audit_source = ROOT / 'companion-enclosure-audit.json'
    data = json.loads(source.read_text())
    audit = json.loads(audit_source.read_text())
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    failures = []

    def check(condition, label):
        if not condition:
            failures.append(label)

    check(data['status'] == 'PASS' and not data['failures'], 'source_status')
    check(audit['passed'] and not audit['failures'], 'aggregate_audit_status')
    check(audit['certificate_sha256'] == source_hash, 'audited_source_hash')
    rows = []
    # Exact decimal input bounds are C057a's imports of L047(1),(3).
    for probe, slot, b_pair, quartic_pair in (
        (3, 1, ('111.03741', '111.03743'), ('-19379.50', '-16688.19')),
        (6, 3, ('-32.21998', '-32.21996'), ('-164110.08', '-163241.27')),
    ):
        record = data['final'][slot]
        check((record['probe'], record['trace']) == (probe, 'B'), f'B_{probe}_identity')
        exact = imported(record['lower']), imported(record['upper'])
        b = tuple(map(F, b_pair))
        check(b[0] < exact[0] < exact[1] < b[1], f'B_{probe}_containment')
        check(imported(record['total_error']) < F(1, 100000), f'B_{probe}_error')
        quartic = tuple(map(F, quartic_pair))
        physical = tuple(8 * x for x in b)
        # Canonical analytic hypothesis: 0 < d_* <= 1/4.
        group = (F(0), 192 * b[1]) if probe == 3 else (192 * b[0], F(0))
        cubic = group[0] - quartic[1], group[1] - quartic[0]
        check(physical[0] < physical[1] and group[0] < group[1], f'interval_order_{probe}')
        check((physical[0] > 0) if probe == 3 else (physical[1] < 0), f'strain_sign_{probe}')
        check(cubic[0] > 0, f'cubic_sign_{probe}')
        rows.append(dict(probe=probe, B_import=interval(b),
                         exact_source_B=interval(exact),
                         source_B_error=record['total_error'],
                         physical_strain=interval(physical),
                         quartic=interval(quartic), group=interval(group),
                         top_top_cubic=interval(cubic)))
    result = dict(passed=not failures, failures=failures,
                  input_ids=['L046', 'L047', 'L049', 'L055', 'L057'],
                  implementation_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  source_sha256=source_hash,
                  audit_sha256=hashlib.sha256(audit_source.read_bytes()).hexdigest(),
                  analytic_inputs=dict(physical_strain='8 B_i',
                                       group_coefficient='768 d_* B_i',
                                       d_range='0 < d_* <= 1/4',
                                       cubic_coefficient='group - quartic'),
                  required_source_trace_error_below=rational(F(1, 100000)),
                  qualification='Exact rational propagation; inherits L047 IEEE model and C057a analytic identities; not a full-response certificate.',
                  rows=rows)
    OUTPUT.write_text(json.dumps(result, indent=2) + '\n')
    for row in rows:
        probe = row['probe']
        for name in ('physical_strain', 'group', 'top_top_cubic'):
            values = row[name]
            lo, hi = imported(values['lower']), imported(values['upper'])
            print(f'{probe} {name}: ({finite_decimal(lo)}, {finite_decimal(hi)})')
        error = imported(row['source_B_error'])
        scaled_error = error * 10**12
        upper_error = F(-((-scaled_error.numerator) // scaled_error.denominator), 10**12)
        print(f'{probe} actual imported B error: <{finite_decimal(upper_error)}; required: <0.00001')
    print('PASS' if result['passed'] else 'FAIL', 'failures:', failures, 'path:', OUTPUT)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
