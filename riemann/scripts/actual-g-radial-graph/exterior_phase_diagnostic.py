"""Nonrigorous low-coefficient screen for the current relative range test."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'scripts/actual-fredholm/fixed-pair-certificate-431.json'
OUTPUT = Path(__file__).with_name('exterior-phase-diagnostic.json')


def main():
    if OUTPUT.exists():
        raise SystemExit('Preserve existing diagnostic evidence.')
    raw = SOURCE.read_bytes()
    data = json.loads(raw)['evaluation']
    a = [(float(lo) + float(hi))/2 for lo, hi in data['coefficients']]
    def saddle(x):
        return sum((n-1)*an*x**n for n, an in enumerate(a))
    lo, hi = 1.0, 256.0
    for _ in range(60):
        mid = (lo+hi)/2
        if saddle(mid) < 0:
            lo = mid
        else:
            hi = mid
    radius = (lo+hi)/2
    c = [an*radius**n for n, an in enumerate(a)]
    b = {k: sum((2*n+k-2)*c[n]*c[n+k]
                for n in range(12-k)) for k in (1, 2, 3)}
    margin = b[1]+b[2]-b[2]**2/(4*b[3])
    result = dict(status='NONRIGOROUS_DIAGNOSTIC', input_path=str(SOURCE.relative_to(ROOT)),
                  input_sha256=hashlib.sha256(raw).hexdigest(), radius=radius,
                  saddle_float_bracket=[lo, hi], scaled_first_twelve=c[:12],
                  truncated_B=b, quadratic_margin=margin, required_margin='> 0',
                  failures=[] if margin > 0 else ['three-mode quadratic test'],
                  limitation='Floating-point midpoints and truncated series; no proof, root enclosure or zero-set certificate.')
    OUTPUT.write_text(json.dumps(result, indent=2)+'\n')
    print(result['status'])
    print('R display:', radius, '; quadratic margin:', margin, '; required > 0')
    print('Failures:', result['failures'])
    print('Complete diagnostic:', OUTPUT.relative_to(ROOT))


if __name__ == '__main__':
    main()
