"""Bounded next-turn recommendations and read-only session telemetry."""
import json
import os
from pathlib import Path
import sqlite3

from research import field

MODELS = {'routine': 'gpt-6-luna', 'standard': 'gpt-6.1-sol', 'deep_research': 'gpt-6-astra'}
DEFAULTS = {'metadata': ('routine', 'low'), 'source_extraction': ('routine', 'medium'),
            'literature_comparison': ('standard', 'medium'), 'calculation': ('standard', 'high'),
            'implementation': ('standard', 'high'), 'proof_attempt': ('deep_research', 'high'),
            'proof_audit': ('deep_research', 'high')}
EFFORTS = ('low', 'medium', 'high', 'xhigh', 'max')


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
    history = local.get('routing_history', [])[-9:]
    if effort == 'max' and (not valid or not recommendation.get('escalation')
                            or local.get('last_outcome') != 'success'
                            or local.get('research_outcome') not in ('EXPLORATION', 'NEGATIVE')
                            or local.get('last_route', {}).get('target') != target
                            or local.get('last_route', {}).get('model') != MODELS['deep_research']
                            or local.get('last_route', {}).get('effort') not in ('high', 'xhigh')
                            or sum(r.get('effort') == 'max' for r in history) >= 2):
        effort = 'high'
        reason += ' Max requires a specific obstruction after a successful high-depth attempt; limited to two in ten.'
    if role == 'deep_research' and sum(r.get('model') == MODELS[role] for r in history) >= 4:
        role, effort = 'standard', min(effort, 'high', key=EFFORTS.index)
        reason += ' Deep-model share limited to four in ten attempted turns.'
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
    return dict(target=target, task_type=task, model=model, effort=effort, reason=reason,
                availability='cached' if catalog else 'unverified')


def recommendation(progress):
    """Only accepted reports can nominate settings; missing fields use defaults."""
    task, role, effort, reason = (field(progress, k) for k in
        ('NEXT_TASK_TYPE', 'NEXT_MODEL_ROLE', 'NEXT_EFFORT', 'NEXT_ROUTING_REASON'))
    if task not in DEFAULTS or role not in MODELS or effort not in EFFORTS or not reason:
        return None
    return dict(target=field(progress, 'Next action'), task_type=task, role=role,
                effort=effort, reason=reason, escalation=field(progress, 'NEXT_ESCALATION'))


INSTRUCTION = '''\nRecommend settings for the exact Next action using single-line checkpoint fields:
NEXT_TASK_TYPE: metadata|source_extraction|literature_comparison|calculation|implementation|proof_attempt|proof_audit
NEXT_MODEL_ROLE: routine|standard|deep_research
NEXT_EFFORT: low|medium|high|xhigh|max
NEXT_ROUTING_REASON: concrete task difficulty and expected benefit
NEXT_ESCALATION: optional specific unresolved obstruction after a serious high-effort attempt
Use routine for mechanical extraction/repairs, standard for theorem comparison and ordinary calculations,
deep_research for new mechanisms, difficult proofs and critical audits. Downgrade after the hard step.
Max requires a precise obstruction and one bounded test; failure alone is insufficient. No lemma quota.
The supervisor validates recommendations and enforces expensive-turn limits; do not edit runtime state.
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
