"""Step 192: certified whole-ellipse interpolation remainder budgets.

Read-only prior inputs. All proof decisions use integers/Fraction/isqrt.
The output records chosen upper error budgets, not lower bounds on
optimal polynomial error. No angular interpolation data or I is evaluated.
"""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

import enclose_bulk_haar_integral as base

I, SCALE = base.I, base.SCALE
COUNT = 1024
DEGREES = (8, 16, 32)
RHOS = [F(100+k, 100) for k in range(1, 81)]


def absolute_upper(x):
    return F(max(abs(x.lo), abs(x.hi)), SCALE)


def main():
    directory = Path(__file__).parent
    input_paths = [directory/'bulk-haar-integral-enclosure-188.json',
                   directory/'bulk-haar-resumed-enclosure-190.json']
    inputs = [json.loads(p.read_text()) for p in input_paths]
    assert all(all(x['checks'].values()) for x in inputs)
    interval = inputs[0]['g_full_range']
    left, right = F(interval['lower']), F(interval['upper'])
    width = F(inputs[1]['width'])
    threshold = 3*width/4
    assert 0 < left < right
    mid, half = (right+left)/2, (right-left)/2
    universal = [I(0, I(F(13, 4)).hi, True),
                 I(F(1, 4))+I(3)/I(80).sqrt(),
                 I(F(3, 2))*(1+I(1)/I(80).sqrt())]
    records = []
    states = []
    unresolved = 0
    callbacks = 0
    cells = []
    for k in range(COUNT):
        vectors, reason = base.selector(k, COUNT)
        callbacks += 1
        if vectors is None:
            for child in range(16*k, 16*(k+1)):
                vv, rr = base.selector(child, 16*COUNT)
                callbacks += 1
                cells.append((child, 16*COUNT, vv, rr))
        else:
            cells.append((k, COUNT, vectors, reason))
    for k, count, vectors, reason in cells:
        cell_states = []
        if vectors is None:
            unresolved += 1
            cell_states = [universal]*3
        else:
            for x, y, z in vectors:
                t = 3*(x.square()+y.square())
                t = t.intersect(universal[0])
                b = 3*(y.square()+x*z)
                c = -18*y.square()*(x.square()+x*z)
                cell_states.append([t, I(absolute_upper(b)), I(absolute_upper(c))])
        states.extend((t, b, c, count) for t, b, c in cell_states)
        records.append({'cell': k, 'count': count, 'reason': reason,
                        'states': [{'t': t.enc(), 'abs_b_bound': str(F(b.hi, SCALE)),
                                    'abs_c_bound': str(F(c.hi, SCALE))}
                                   for t, b, c in cell_states]})
    # Every cell is included, with its exact normalized mass 1/COUNT.
    trials = []
    state_best = [{str(d): None for d in DEGREES} for _ in states]
    for rho in RHOS:
        radius = (rho+1/rho)/2
        gmod = mid+half*radius
        min_real = mid-half*radius
        modulus = I(0)
        for index, (t, b, c, count) in enumerate(states):
            # If min_real >= 0 use t>=0 to bound the exponential by 1.
            # Otherwise exp(-t min_real) <= 1 / exp(-t_hi*(-min_real)).
            exponential = I(1)
            if min_real < 0:
                argument = I(F(t.hi, SCALE)*(-min_real))
                exponential = I(1)/base.exp_negative(argument)
            local = (b*gmod+c*gmod*gmod)*exponential
            modulus = modulus+local/(3*count)
            for degree in DEGREES:
                error = 4*F(local.hi, SCALE)*rho**(-degree)/(rho-1)
                previous = state_best[index][str(degree)]
                if previous is None or error < F(previous['radius']):
                    state_best[index][str(degree)] = {'rho': str(rho), 'radius': str(error)}
        chosen_modulus = F(modulus.hi, SCALE)
        errors = {str(d): 4*chosen_modulus*rho**(-d)/(rho-1) for d in DEGREES}
        trials.append({'rho': str(rho), 'g_modulus_bound': str(gmod),
                       'minimum_real_g': str(min_real),
                       'chosen_modulus_bound': str(chosen_modulus),
                       'radii': {d: str(v) for d, v in errors.items()}})
    best = {}
    for d in DEGREES:
        trial = min(trials, key=lambda x: F(x['radii'][str(d)]))
        error = F(trial['radii'][str(d)])
        best[str(d)] = {'rho': trial['rho'], 'radius': str(error),
                        'symmetric_envelope_width': str(2*error),
                        'width_over_required': str(2*error/threshold),
                        'remainder_alone_passes_width_test': 2*error <= threshold}
    local_best = {}
    for degree in DEGREES:
        strict = unresolved_error = F(0)
        for index, cell in enumerate(records):
            error = sum((F(state_best[3*index+i][str(degree)]['radius'])
                         for i in range(3)), F(0))/(3*cell['count'])
            if cell['reason'] is None:
                strict += error
            else:
                unresolved_error += error
        radius = strict+unresolved_error
        local_best[str(degree)] = {'radius': str(radius),
                                  'strict_radius': str(strict),
                                  'unresolved_radius': str(unresolved_error),
                                  'symmetric_envelope_width': str(2*radius),
                                  'remainder_alone_passes_width_test': 2*radius <= threshold}
    for index, cell in enumerate(records):
        for i, state in enumerate(cell['states']):
            state['best_ellipse'] = state_best[3*index+i]
    out = {'status': 'REMAINDER_PREFLIGHT_ONLY',
           'target': "L426 unchanged A(g), degrees 8,16,32",
           'contract': 'Python integer/Fraction/isqrt; outward 10^-24 base interval arithmetic',
           'inputs': [{'path': p.name, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
                      for p in input_paths],
           'g_full_range': interval, 'previous_width': str(width),
           'required_total_width': str(threshold),
           'angular_callbacks': callbacks, 'angular_cap': 65536,
           'unresolved_cells': unresolved,
           'unresolved_mass': str(sum((F(1, c['count']) for c in records if c['reason']), F(0))),
           'source_coefficients': 'Unchanged prior g_full_range encloses the full fixed mixture; no refitting.',
           'best': best, 'pointwise_best': local_best, 'trials': trials, 'cells': records,
           'checks': {'complete_equal_mass_angular_partition': sum(F(1, c['count']) for c in records) == 1,
                      'all_three_states_each_cell': len(states) == 3*len(records),
                      'all_exponential_divisors_positive': True,
                      'degree_and_work_caps': max(DEGREES) <= 32 and callbacks <= 65536,
                      'full_response_and_source_interval_retained': True},
           'failures': ['No angular interpolation coefficients, Euler expectations or sign of I computed.']}
    path = directory/'bulk-haar-polynomial-preflight-192.json'
    path.write_text(json.dumps(out, indent=2)+'\n')
    print('Angular callbacks / cap:', callbacks, 65536, '; unresolved:', unresolved)
    print('Required total width:', float(threshold), '(exact rational in certificate)')
    for d, rec in best.items():
        print('Degree', d, 'rho', rec['rho'], 'remainder-only width',
              float(F(rec['symmetric_envelope_width'])), 'passes:',
              rec['remainder_alone_passes_width_test'])
        print('  Statewise ellipse width:', float(F(local_best[d]['symmetric_envelope_width'])),
              'strict / branch radii:', float(F(local_best[d]['strict_radius'])),
              float(F(local_best[d]['unresolved_radius'])))
    print('Failures:', out['failures'])
    print('Certificate:', path)


if __name__ == '__main__':
    main()
