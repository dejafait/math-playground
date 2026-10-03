"""Bound self-reported research exploration independently of checkpoint writes."""
import re


def field(text, name):
    values = re.findall(r'^' + name + r':[ \t]*([^\n]+)$', text, re.M)
    return values[0].strip() if len(values) == 1 else None


def assess(state, before, after, changed):
    """Update persisted counters; return a human-readable stop reason or None."""
    step = field(after, 'STEP_ID')
    outcome = field(after, 'STEP_OUTCOME')
    valid = (changed and step and step != field(before, 'STEP_ID')
             and step != state.get('research_step_id')
             and field(after, 'STEP_EVIDENCE')
             and outcome in {'ADVANCE', 'NEGATIVE', 'EXPLORATION', 'STALLED'})
    if not valid:
        state['no_progress'] = state.get('no_progress', 0) + 1
        if state['no_progress'] >= 3:
            return 'Three missing, invalid, or unchanged research step reports.'
        return None
    state['research_step_id'] = step
    state['research_outcome'] = outcome
    state['no_progress'] = 0
    kind = field(after, 'STEP_KIND')
    state['turn_mix'] = (state.get('turn_mix', []) + [kind])[-10:]
    if kind == 'LITERATURE':
        state['literature_stalled'] = state.get('literature_stalled', 0) + 1 if outcome == 'STALLED' else 0
        if state['literature_stalled'] >= 2:
            return 'Two consecutive stalled literature turns; park the source blocker and select an independent target.'
        return None
    if outcome in {'ADVANCE', 'NEGATIVE'}:
        state['exploration_turns'] = 0
        state['stalled_turns'] = 0
    elif outcome == 'EXPLORATION':
        state['stalled_turns'] = 0
        state['exploration_turns'] = state.get('exploration_turns', 0) + 1
        if state['exploration_turns'] >= 3:
            return 'Three exploration turns without an advance or informative negative result; review the recorded decision.'
    else:
        state['stalled_turns'] = state.get('stalled_turns', 0) + 1
        if state['stalled_turns'] >= 2:
            return 'Two consecutive stalled research turns, regardless of history edits.'
    return None


def resume(state):
    """Explicitly renew research budget without altering quota/retry fields."""
    state.pop('research_halt', None)
    for key in ('no_progress', 'exploration_turns', 'stalled_turns', 'literature_stalled', 'unknowns'):
        state[key] = 0


def recover(state):
    """Turn a persistent stop into a queued review, preserving its evidence."""
    reason = state.pop('research_halt', None)
    if reason:
        state['recovery_attempts'] = state.get('recovery_attempts', 0) + 1
        state['require_new_target'] = bool(state.get('require_new_target')
            or state['recovery_attempts'] >= 2
            or reason.startswith(('Three exploration turns', 'Two consecutive stalled')))
        state['research_recovery'] = reason
        state['last_research_stop'] = dict(
            reason=reason, step=state.get('research_step_id'),
            counters={key: state.get(key, 0) for key in
                      ('no_progress', 'exploration_turns', 'stalled_turns', 'unknowns')})
        state.setdefault('first_research_stop', state['last_research_stop'])
        state['recovery_count'] = state.get('recovery_count', 0) + 1
    return reason


def balance_instruction(state, ready):
    """Guide attempted work, never require successful proofs or bypass source gates."""
    mix = state.get('turn_mix', [])
    mature = mix.count('RESEARCH') >= 4
    limit = 0.2 if mature else 1 / 3
    share = mix.count('LITERATURE') / len(mix) if mix else 0
    return (f'Turn balance: recent {mix.count("RESEARCH")} mathematical / '
            f'{mix.count("LITERATURE")} literature turns; aim for at most '
            f'{round(limit * 100)}% literature. Mathematical attempts need not succeed or create a lemma. '
            + ('A ready target must receive a mathematical attempt now; further review needs a specific LITERATURE_REASON. '
               if ready and (not mix or mix[-1] == 'LITERATURE' or share >= limit) else '')
            + 'Reuse adequate coverage. If sources remain blocked, park dependent work and choose an independently testable target.\n')
