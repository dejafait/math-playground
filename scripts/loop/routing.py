"""Bounded next-turn recommendations and read-only session telemetry."""
import json
import os
from pathlib import Path
import sqlite3

from research import field

MODELS = {'routine': 'gpt-6-luna', 'standard': 'gpt-6.1-sol', 'deep_research': 'gpt-6-astra'}
DEFAULTS = {'metadata': ('routine', 'low'), 'source_extraction': ('routine', 'medium'),
            'literature_comparison': ('standard', 'medium'), 'calculation': ('standard', 'high'),
            'implementation': ('standard', 'high'), 'proof_attempt': ('deep_research', 'xhigh'),
            'proof_audit': ('standard', 'high')}
EFFORTS = ('low', 'medium', 'high', 'xhigh', 'max')
REASONING_CLASSES = {'creative', 'development', 'routine_audit', 'conceptual_audit', 'candidate_audit'}
CLASS_ROUTES = {'creative': ('deep_research', 'max'), 'development': ('deep_research', 'xhigh'),
                'routine_audit': ('standard', 'high'), 'conceptual_audit': ('deep_research', 'xhigh'),
                'candidate_audit': ('deep_research', 'max')}


def reasoning_class(task, recommendation):
    """Explicit mathematical purpose, bound to the saved target; no keyword guessing."""
    value = recommendation.get('reasoning_class')
    allowed = ({'creative', 'development'} if task == 'proof_attempt' else
               {'routine_audit', 'conceptual_audit', 'candidate_audit'} if task == 'proof_audit' else set())
    if value in allowed:
        # Maximum effort requires a specific obstruction or load-bearing claim,
        # but not an earlier failure. Incomplete metadata never rejects research.
        if value in {'creative', 'candidate_audit'} and not recommendation.get('escalation'):
            return 'development' if task == 'proof_attempt' else 'conceptual_audit'
        return value
    return 'development' if task == 'proof_attempt' else 'routine_audit' if task == 'proof_audit' else None


def planning_instruction(local):
    """Keep discovery from being indefinitely displaced; never override a source gate."""
    history = [r for r in local.get('routing_history', []) if r.get('validation') == 'accepted']
    since = []
    for row in reversed(history):
        if row.get('reasoning_class') == 'creative' and row.get('outcome') == 'success':
            break
        since.append(row)
    if len(since) < 4:
        return ''
    return ('\nDiscovery planning: at least four accepted turns have passed without a protected creative attempt. '
            'When choosing the next target, prioritize a bounded new mechanism for a central mathematical gap '
            'and nominate proof_attempt/creative with NEXT_ESCALATION naming the obstruction and why it matters. '
            'Prepare missing source coverage first; do not skip an essential audit, invent a target just to fill '
            'a quota, repeat an exhausted mechanism, or label routine specialization creative. If no justified '
            'creative target is available, state the blocker in the existing route decision.\n')


def profile_home():
    return Path(os.environ.get('CODEX_HOME', Path.home() / '.codex'))


def available(home=None):
    """Cached availability is advisory; never guess an unsupported effort."""
    try:
        data = json.loads(((home or profile_home()) / 'models_cache.json').read_text())
        return {m['slug']: {e['effort'] for e in m.get('supported_reasoning_levels', [])}
                for m in data['models'] if m.get('visibility') != 'hide'}
    except (OSError, ValueError, KeyError, TypeError):
        return {}


def select(progress, local, ready, catalog=None):
    target = field(progress, 'Next action')
    recommendation = local.get('next_route', {})
    valid = recommendation.get('target') == target
    task = recommendation.get('task_type') if valid else None
    if task not in DEFAULTS:
        task = 'calculation' if ready else 'literature_comparison'
    role, effort = DEFAULTS[task]
    reason = 'Default for ' + task + '; no validated next-turn recommendation.'
    if valid:
        role = recommendation.get('role', role)
        effort = recommendation.get('effort', effort)
        reason = recommendation.get('reason', reason)
    if role not in MODELS:
        role = DEFAULTS[task][0]
    if effort not in EFFORTS:
        effort = DEFAULTS[task][1]
    if not ready and task not in ('metadata', 'source_extraction', 'literature_comparison'):
        role, effort = 'standard', 'medium'
        reason += ' Source gate requires comparison first.'
    purpose = reasoning_class(task, recommendation if valid else {})
    gated = not ready and task not in ('metadata', 'source_extraction', 'literature_comparison')
    if purpose and not gated:
        role, effort = CLASS_ROUTES[purpose]
        reason += ' Mathematical purpose: ' + purpose + '; protected task-based allocation.'
    elif effort == 'max':
        effort = 'high'
        reason += ' Maximum effort is reserved for justified creative work and candidate audits.'
    catalog = available() if catalog is None else catalog
    model = MODELS[role]
    if catalog and model not in catalog:
        model = next((MODELS[r] for r in ('standard', 'routine', 'deep_research') if MODELS[r] in catalog), None)
        if model is None:
            raise RuntimeError('No configured routing model is listed in the active profile model cache.')
        reason += ' Requested role unavailable; explicit fallback selected.'
    if catalog and effort not in catalog[model]:
        options = [e for e in EFFORTS if e in catalog[model] and EFFORTS.index(e) <= EFFORTS.index(effort)]
        if not options:
            raise RuntimeError('No supported effort within the routing budget for ' + model)
        effort = options[-1]
        reason += ' Effort adjusted to advertised support.'
    return dict(target=target, task_type=task, reasoning_class=purpose if not gated else None,
                model=model, effort=effort, reason=reason,
                availability='cached' if catalog else 'unverified')


def recommendation(progress):
    """Only accepted reports can nominate settings; missing fields use defaults."""
    task, role, effort, reason = (field(progress, k) for k in
        ('NEXT_TASK_TYPE', 'NEXT_MODEL_ROLE', 'NEXT_EFFORT', 'NEXT_ROUTING_REASON'))
    if task not in DEFAULTS or role not in MODELS or effort not in EFFORTS or not reason:
        return None
    return dict(target=field(progress, 'Next action'), task_type=task, role=role,
                effort=effort, reason=reason, escalation=field(progress, 'NEXT_ESCALATION'),
                reasoning_class=field(progress, 'NEXT_REASONING_CLASS'))


INSTRUCTION = '''\nRecord ACTUAL_TASK_TYPE using one task-type value below for the work just completed; this is a self-report.
Recommend settings for the exact Next action using single-line checkpoint fields:
NEXT_TASK_TYPE: metadata|source_extraction|literature_comparison|calculation|implementation|proof_attempt|proof_audit
NEXT_MODEL_ROLE: routine|standard|deep_research
NEXT_EFFORT: low|medium|high|xhigh|max
NEXT_REASONING_CLASS: creative|development|routine_audit|conceptual_audit|candidate_audit (proof tasks only)
NEXT_ROUTING_REASON: concrete task difficulty and expected benefit
NEXT_ESCALATION: required for creative/candidate_audit; precise obstruction or critical claim and its main-goal importance
Use routine for mechanical extraction/repairs, standard for theorem comparison and ordinary calculations,
proof_attempt/creative for genuinely new mechanisms at central gaps (Astra/max immediately),
proof_attempt/development for difficult development of an established route (Astra/xhigh),
proof_audit/routine_audit for replay, arithmetic and ordinary hypothesis checks (Sol/high),
proof_audit/conceptual_audit for delicate logical/analytic arguments (Astra/xhigh), and
proof_audit/candidate_audit for independent scrutiny of a possible complete solution (Astra/max).
These purpose routes override older role/effort recommendations; no rolling Astra/max share cap applies.
Distinguish reproduction/specialization from creative work. Never reduce conceptual audit rigor to save tokens.
For creative work name one bounded test and the decisive evidence; preserve partial reasoning and require
a materially new input, informative obstruction or refined mechanism before repeating an unsuccessful attempt.
Use existing STEP_EVIDENCE/route decision for conclusions; no extra report or lemma quota. Choose discovery
regularly when justified, instead of chains of routine audits/approvals. Source gates and exploration stops
still apply. Ultra/delegation is not enabled. Do not edit runtime state.
'''


def telemetry(thread_id, home=None):
    result = {'actual_model': None, 'actual_effort': None, 'allowance': 'unavailable'}
    if not thread_id:
        return result
    home = home or profile_home()
    try:
        with sqlite3.connect((home / 'state_5.sqlite').as_uri() + '?mode=ro', uri=True) as db:
            row = db.execute('SELECT model, reasoning_effort FROM threads WHERE id=?', (thread_id,)).fetchone()
        if row:
            result.update(actual_model=row[0], actual_effort=row[1])
    except sqlite3.Error:
        pass
    return result
