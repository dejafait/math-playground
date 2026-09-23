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
    for key in ('no_progress', 'exploration_turns', 'stalled_turns'):
        state[key] = 0
