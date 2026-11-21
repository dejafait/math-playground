#!/usr/bin/env python3
"""Independent reconstruction of the assessed Theorem 3.3 checks.

Not a byte-identical copy of the author's checker. Always save a certificate,
including unavailable dependencies and unexecuted gates. No numerical fallback.
"""
import argparse
from fractions import Fraction
import importlib.metadata
import json
from pathlib import Path
import platform
import sys


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--bits', type=int, default=192)
    ap.add_argument('--output', type=Path,
                    default=Path(__file__).with_name('independent-audit-136.json'))
    args = ap.parse_args()
    if args.bits < 192:
        raise ValueError('The assessed replay requires at least 192 bits')
    X, W, C, H, K = 6000000185827, 120000000000000, 690988, 3100000, 128
    ends = [C]
    while ends[-1] < H:
        nxt = min(H, 101 * ends[-1] // 100)
        if nxt <= ends[-1]:
            raise ArithmeticError('Non-increasing endpoint recurrence')
        ends.append(nxt)
    global_names = ['positive_heat_band', 'finite_natural_index_upper_wall',
                    'finite_natural_index_lower_wall', 'prefix_above_centre',
                    'centre_log_between_3_and_7_2', 'cover_starts_at_C',
                    'cover_ends_at_H', 'cover_strictly_increasing']
    leaf_names = ['position_not_left_of_X',
                  'all_coefficient_heat_exponents_nonpositive',
                  'convex_derivative_at_prefix_negative',
                  'convex_derivative_at_upper_negative',
                  'tail_integrals_positive',
                  'complete_centred_moment_below_81_4']
    gates = {name: None for name in global_names}
    for j in range(1, len(ends)):
        gates.update({f'leaf_{j:03d}_{name}': None for name in leaf_names})
    out = dict(status='INCOMPLETE', implementation='independent reconstruction',
               source_commit='18dbc01ea36bf9a24d8f79822b5ce06b545e4ace',
               source_byte_hash_verified=False, bits=args.bits,
               runtime={'python': platform.python_version(), 'executable': sys.executable},
               domain={'a':'98/625', 'T':'1/5', 'X':X, 'W':W},
               required_cap='81/4', actual_uniform_bound=None,
               closed_index_endpoints=ends, closed_leaf_count=len(ends)-1,
               required_leaf_count=151, required_gate_count=914,
               gates=gates, failures=[], leaves=[], maximum_upper_endpoint=None)

    def gate(name, condition):
        gates[name] = bool(condition)
        if not condition:
            out['failures'].append(name + ': false or indeterminate')

    gate('positive_heat_band', 0 < Fraction(98, 625) < Fraction(1, 5) < Fraction(1, 2))
    gate('prefix_above_centre', K > 32)
    gate('cover_starts_at_C', ends[0] == C)
    gate('cover_ends_at_H', ends[-1] == H)
    gate('cover_strictly_increasing', all(l < u for l, u in zip(ends, ends[1:])))
    out['exact_integer_checks'] = {
        '151_adjacent_closed_leaves': len(ends)-1 == 151,
        '914_named_gates': len(gates) == 914,
        'covers_every_integer_C_through_H': ends[0] == C and ends[-1] == H
            and all(l < u for l, u in zip(ends, ends[1:]))}
    try:
        from flint import arb, ctx
        import flint
        ctx.prec = args.bits
        out['runtime']['python_flint'] = importlib.metadata.version('python-flint')
        out['runtime']['flint'] = str(getattr(flint, '__FLINT_VERSION__', 'unreported'))
        enc = lambda v: v.str(90, more=True)
        a, T = arb(98)/625, arb(1)/5
        pi, half = arb.pi(), arb(1)/2
        kappa, low = arb(32).log(), arb(K).log()
        cap = arb(81)/4
        gate('finite_natural_index_upper_wall', arb(H+1)**2-arb(W)/(4*pi)-T/16 > 0)
        gate('finite_natural_index_lower_wall', arb(X)/(4*pi)+a/16-arb(C)**2 > 0)
        gate('centre_log_between_3_and_7_2', kappa > 3 and kappa < arb(7)/2)
        upper_endpoints = []
        for j, (L, U) in enumerate(zip(ends, ends[1:]), 1):
            xl = arb(X) if j == 1 else 4*pi*(arb(L)**2-T/16)
            c = ((1+xl*xl).sqrt()/(4*pi)).log()/4-1/(2*(1+xl*xl))
            sigma, high = half+a*c, arb(U).log()
            B = sigma-1
            g = lambda u: 1+(u-kappa)*(a*u/2-sigma)
            prefix = arb(0)
            for n in range(1, K+1):
                u = arb(n).log()
                d = arb(0) if n == 32 else ((arb(32)/n).log() if n < 32 else (arb(n)/32).log())
                prefix += d*(a*u*u/4-sigma*u).exp()
            E = lambda u: (a*u*u/4-B*u).exp()
            primitive = lambda u: (pi/a).sqrt()*(-B*B/a).exp()*((a*u/2-B)/a.sqrt()).erfi()
            I = primitive(high)-primitive(low)
            J = 2/a*(E(high)-E(low)+B*I)
            tail = J-kappa*I
            bound = prefix+tail
            values = [xl >= X, high < 4*c, g(low) < 0, g(high) < 0,
                      I > 0 and tail > 0, bound < cap]
            for name, value in zip(leaf_names, values):
                gate(f'leaf_{j:03d}_{name}', value)
            upper_endpoints.append(bound.upper())
            out['leaves'].append(dict(left=L, right=U, x_left=enc(xl), c_left=enc(c),
                sigma=enc(sigma), g_low=enc(g(low)), g_high=enc(g(high)),
                prefix=enc(prefix), I=enc(I), J=enc(J), tail=enc(tail),
                bound=enc(bound), upper_endpoint=enc(bound.upper()), required='81/4'))
        # upper() returns an exact dyadic rounded outward; no midpoint ordering.
        largest = max(upper_endpoints)
        out['maximum_upper_endpoint'] = enc(largest)
        out['actual_uniform_bound'] = enc(largest)
        out['maximum_upper_endpoint_below_cap'] = bool(largest < cap)
        if not largest < cap:
            out['failures'].append('Maximum upper endpoint is not certified below 81/4')
    except Exception as exc:
        out['failures'].append(type(exc).__name__ + ': ' + str(exc))
    out['gate_counts'] = {'passed':sum(v is True for v in gates.values()),
                          'failed':sum(v is False for v in gates.values()),
                          'unexecuted':sum(v is None for v in gates.values()),
                          'required':914}
    if (not out['failures'] and all(out['exact_integer_checks'].values())
            and all(v is True for v in gates.values())
            and out.get('maximum_upper_endpoint_below_cap') is True):
        out['status'] = 'PASS'
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2)+'\n')
    print(out['status'], 'leaves', len(ends)-1, '/151;', out['gate_counts'])
    print('Actual bound:', out['actual_uniform_bound'], '; required: <81/4')
    print('Failures:', out['failures'])
    print('Certificate:', args.output)
    return 0 if out['status'] == 'PASS' else 1


if __name__ == '__main__':
    sys.exit(main())
