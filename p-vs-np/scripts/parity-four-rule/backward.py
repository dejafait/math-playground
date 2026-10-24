"""Finite goal-directed primitive synthesis; no change to the rule interface.

This is an incomplete bounded search, not an implementation of completeness.
Boolean masks only reject impossible subgoals. Only primitive records certify
success, and checker.py imports none of this code.
"""
from functools import lru_cache
import itertools
import time

from prepare import N, O, names, nodes, evaluate


LIMITS = dict(template_seconds=20, library_seconds=80, template_states=60000,
              library_states=200000, template_records=20000,
              max_depth=10, formula_nodes='max(24, target nodes + 12)',
              pivots='target subtrees and their single negations, plus constants')


class Limit(Exception):
    pass


def synthesize(target, seconds, states):
    start = time.monotonic()
    cap = max(24, nodes(target) + 12)
    state_limit = min(states, LIMITS['template_states'])
    seconds = min(seconds, LIMITS['template_seconds'])
    slots = sorted(names(target))
    assignments = [dict(zip(slots, bits))
                   for bits in itertools.product((False, True), repeat=len(slots))]
    full = (1 << len(assignments)) - 1
    pool = {'true', 'false'}

    def collect(t):
        pool.add(t)
        if isinstance(t, tuple):
            for c in t[1:]:
                collect(c)

    collect(target)
    pool |= {N(t) for t in tuple(pool)}
    pool = sorted(pool, key=lambda t: (nodes(t), repr(t)))
    rows, proven = [], {}
    failed, active = set(), set()
    stats = dict(states=0, rejected_size=0, rejected_boolean=0,
                 cache_hits=0, active_cycles=0, cut_options=0,
                 completed_depth=0, attempted_depth=0)

    @lru_cache(maxsize=120000)
    def mask(f):
        if isinstance(f, str):
            return sum(int(evaluate(f, v)) << i for i, v in enumerate(assignments))
        if f[0] == 'not':
            return full ^ mask(f[1])
        return mask(f[1]) | mask(f[2])

    def budget():
        if time.monotonic() - start >= seconds:
            raise Limit('seconds')
        if stats['states'] >= state_limit:
            raise Limit('states')

    def emit(f, tag, refs=()):
        if len(rows) >= LIMITS['template_records'] - 2:
            raise Limit('records')
        i = len(rows)
        rows.append(dict(f=f, rule=tag, refs=list(refs)))
        proven[f] = i
        return i

    def is_or(t):
        return isinstance(t, tuple) and t[0] == 'or'

    def solve(f, depth):
        budget()
        if f in proven:
            stats['cache_hits'] += 1
            return proven[f]
        if nodes(f) > cap:
            stats['rejected_size'] += 1
            return None
        if mask(f) != full:
            stats['rejected_boolean'] += 1
            return None
        key = (f, depth)
        if depth < 0 or key in failed:
            return None
        # Failed states are memoized by depth. There is no active-path pruning:
        # decreasing depth terminates recursion, and pruning by formula alone
        # would make a failure depend on an unrecorded ancestor context.
        stats['states'] += 1
        if f == 'true':
            return emit(f, 'true')
        if f == N('false'):
            return emit(f, 'not-false')
        if is_or(f) and f[1] == N(f[2]):
            return emit(f, 'axiom')
        if depth == 0:
            failed.add(key)
            return None
        if is_or(f):
            a, b = f[1:]
            # Inverse expansion, then inverse directed association.
            i = solve(b, depth - 1)
            if i is not None:
                return emit(f, 'expansion', [i])
            if is_or(a):
                i = solve(O(a[1], O(a[2], b)), depth - 1)
                if i is not None:
                    return emit(f, 'association', [i])
            # Cuts are constrained to the target-derived finite pivot pool.
            # Try pairs with primitive axiom leaves first.
            options = []
            for pivot in pool:
                p, q = O(pivot, a), O(N(pivot), b)
                if nodes(p) <= cap and nodes(q) <= cap and mask(p) == full and mask(q) == full:
                    score = sum(x in proven or (is_or(x) and x[1] == N(x[2])) for x in (p, q))
                    options.append((-score, nodes(p) + nodes(q), repr(pivot), p, q))
            options.sort(key=lambda r: r[:3])
            for _, _, _, p, q in options:
                stats['cut_options'] += 1
                i = solve(p, depth - 1)
                if i is None:
                    continue
                j = solve(q, depth - 1)
                if j is not None:
                    return emit(f, 'cut', [i, j])
        i = solve(O(f, f), depth - 1)
        if i is not None:
            return emit(f, 'contraction', [i])
        failed.add(key)
        return None

    # Retain ground axioms even if unused; ensures a legal partial endpoint.
    emit('true', 'true')
    emit(N('false'), 'not-false')
    result, reason = None, None
    try:
        for depth in range(LIMITS['max_depth'] + 1):
            stats['attempted_depth'] = depth
            result = solve(target, depth)
            if result is not None:
                break
            stats['completed_depth'] = depth
        if result is None:
            reason = 'depth'
    except Limit as err:
        reason = str(err)
    if result is not None:
        # Finish literally at the requested endpoint without aliases.
        i = len(rows)
        rows.append(dict(f=O(target, target), rule='expansion', refs=[result]))
        rows.append(dict(f=target, rule='contraction', refs=[i]))
    return rows, dict(status='PREPARED' if result is not None else 'UNPREPARED',
                      reason=reason, target=target, records=len(rows), stats=stats,
                      seconds=time.monotonic() - start,
                      bounds=dict(seconds=seconds, states=state_limit, nodes=cap,
                                  records=LIMITS['template_records'], depth=LIMITS['max_depth']),
                      pivots=pool, failed_states=len(failed),
                      qualification='Failure is only for this incomplete bounded tactic; no nonderivability claim.')
