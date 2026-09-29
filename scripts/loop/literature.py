"""Evidence gate, not a mathematical novelty verifier. No network requests."""
import hashlib
from datetime import date
import re

from research import field

READY = {'IMPORT', 'SPECIALIZE', 'EXPLORE'}
DECISIONS = READY | {'REVIEW_REQUIRED', 'SOURCE_BLOCKED'}
CLASSES = {'KNOWN_IMPORTED', 'REPRODUCTION', 'POTENTIALLY_NEW', 'NOVELTY_UNCHECKED'}
REQUIRED = ('TARGET', 'SEARCH_EVIDENCE', 'SOURCE_EVIDENCE', 'COMPARISON', 'GAP', 'REASON')


def read_review(notebook, reference, target):
    """Accept only local, complete assessments bound to an exact target."""
    if not reference:
        raise ValueError('Missing literature assessment path.')
    base = (notebook / 'drafts/literature').resolve()
    path = (notebook / reference).resolve()
    if notebook.resolve() not in base.parents or path.suffix != '.md' or base not in path.parents:
        raise ValueError('Literature assessments must be inside drafts/literature/.')
    try:
        text = path.read_text()
    except (OSError, UnicodeError) as exc:
        raise ValueError('Cannot read literature assessment: ' + reference) from exc
    if any(not field(text, key) for key in REQUIRED):
        raise ValueError('Incomplete or duplicate literature evidence fields: ' + reference)
    if not target or field(text, 'TARGET') != target:
        raise ValueError('Literature assessment does not match the exact target.')
    decision = field(text, 'DECISION')
    if decision not in DECISIONS:
        raise ValueError('Invalid literature decision.')
    checked = field(text, 'CHECKED') or ''
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', checked):
        raise ValueError('Missing literature check date.')
    try:
        date.fromisoformat(checked)
    except ValueError as exc:
        raise ValueError('Invalid literature check date.') from exc
    if decision in READY and not re.search(r'https?://\S+', text):
        raise ValueError('Ready assessments need a direct source URL.')
    return decision


def artifacts(notebook):
    """Review-only turns must not produce mathematical lemmas or programs."""
    digest = hashlib.sha256()
    for folder in ('lemmas', 'scripts'):
        for path in sorted((notebook / folder).rglob('*')):
            if path.is_file() and '__pycache__' not in path.parts:
                digest.update(str(path.relative_to(notebook)).encode())
                digest.update(path.read_bytes())
    return digest.digest()


def prepare(notebook, progress):
    target = field(progress, 'Next action')
    reference = field(progress, 'NEXT_REVIEW')
    try:
        decision = read_review(notebook, reference, target)
        reason = decision
    except ValueError as exc:
        decision, reason = 'REVIEW_REQUIRED', str(exc)
    return dict(target=target, reference=reference, decision=decision,
                reason=reason, artifacts=artifacts(notebook),
                review=(notebook / reference).read_bytes() if decision in READY else None)


def instruction(context):
    if context['decision'] in READY:
        return ('Literature gate: the saved next target has a prior assessment ('
                + context['decision'] + '). Read it before work. Work only on that '
                'target or perform a literature-only review; a new target needs a prior review turn.\n')
    return ('Literature gate: LITERATURE-ONLY TURN. ' + context['reason']
            + '. Search/read sources and complete the assessment for the saved Next action. '
            'Do not derive new results or modify lemmas/ or scripts/. Preserve the '
            'research target while reviewing it; record STEP_KIND: LITERATURE.\n')


def validate_turn(notebook, context, after):
    """Reject unsupported research before its outcome can reset any budget."""
    kind = field(after, 'STEP_KIND')
    classification = field(after, 'STEP_CLASSIFICATION')
    if kind not in {'LITERATURE', 'RESEARCH'} or classification not in CLASSES:
        return 'Missing or invalid STEP_KIND / STEP_CLASSIFICATION.'
    try:
        decision = read_review(notebook, field(after, 'STEP_REVIEW'), context['target'])
        next_decision = read_review(notebook, field(after, 'NEXT_REVIEW'), field(after, 'Next action'))
    except ValueError as exc:
        return str(exc)
    if field(after, 'Next action') != context['target'] and next_decision in READY:
        return 'A new next target needs its own literature review turn.'
    if kind == 'RESEARCH':
        if context['decision'] not in READY:
            return 'Research attempted without an assessment approved before this turn.'
        if field(after, 'STEP_REVIEW') != context['reference'] or decision != context['decision']:
            return 'Research changed its approved assessment; perform a literature turn first.'
        if (notebook / context['reference']).read_bytes() != context['review']:
            return 'Research rewrote its prior assessment; perform a literature turn first.'
        if classification == 'NOVELTY_UNCHECKED':
            return 'Novelty-unchecked work is limited to literature review.'
        expected = {'IMPORT': {'KNOWN_IMPORTED'}, 'SPECIALIZE': {'REPRODUCTION', 'POTENTIALLY_NEW'},
                    'EXPLORE': {'REPRODUCTION', 'POTENTIALLY_NEW'}}
        if classification not in expected[decision]:
            return 'Step classification conflicts with the literature decision.'
    elif artifacts(notebook) != context['artifacts']:
        return 'Literature-only turn modified mathematical lemmas or scripts.'
    return None
