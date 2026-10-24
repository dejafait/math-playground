#!/usr/bin/env python3
"""Integer-only replay of the displayed positive identity; no producer import."""
from pathlib import Path
import hashlib
import json


def main():
    directory = Path(__file__).parent
    source = directory/'mask17-global-scalar-square-certificate.json'
    original = json.loads(source.read_text())
    f = [243, 0, -3564, 0, 6930, 0, -2860, 0, 275]
    p = [0, -6183, 0, 8865, 0, -3085, 0, 275]
    r = [-110592, 0, 120825, 0, -36410, 0, 3025]
    left, right = [], []
    for k in range(15):
        lhs = 11*sum(p[i]*p[k-i] for i in range(8) if 0 <= k-i < 8)
        lhs += 1728**2*({0: -9, 2: 1}.get(k, 0))
        rhs = sum(f[i]*r[k-i] for i in range(9) if 0 <= k-i < 7)
        left.append(lhs)
        right.append(rhs)
    expected_h = ['0', '-229/64', '0', '985/192', '0', '-3085/1728', '0', '275/1728']
    failures = [f'coefficient {k}' for k in range(15) if left[k] != right[k]]
    if original['h'] != expected_h:
        failures.append('producer h')
    if original['scalar'] != -11:
        failures.append('producer scalar')
    if original['F'] != [str(x) for x in f]:
        failures.append('producer field polynomial')
    evidence = dict(identity='11*P(t)^2 + 1728^2*(t^2-9) = F(t)*R(t)',
                    F=f, P=p, R=r, denominator=1728, scalar=-11,
                    left_coefficients=left, right_coefficients=right,
                    producer_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                    producer_h=original['h'], expected_h=expected_h,
                    comparisons=18, failures=failures)
    path = directory/'mask17-global-scalar-square-replay.json'
    path.write_text(json.dumps(evidence, indent=2)+'\n')
    print(json.dumps(dict(result='PASS' if not failures else 'FAIL',
                          actual_coefficient_differences=[a-b for a, b in zip(left, right)],
                          required='15 zero differences', comparisons=18, failures=failures,
                          certificate=str(path.relative_to(Path.cwd())))))
    assert not failures


if __name__ == '__main__':
    main()
