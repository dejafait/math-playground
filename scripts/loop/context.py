"""Supply authoritative startup files once; never summarize mathematical content."""
import hashlib
from pathlib import Path

MAX_OPTIONAL_BYTES = 24000


def snapshot(path, label, optional=False):
    try:
        data = path.read_bytes()
    except OSError:
        return f'\n--- {label}: NOT SUPPLIED; read from disk if required ---\n'
    if optional and len(data) > MAX_OPTIONAL_BYTES:
        return f'\n--- {label}: NOT SUPPLIED ({len(data)} bytes); read its fields and relevant source/proof passages from disk ---\n'
    text = data.decode('utf-8')
    digest = hashlib.sha256(data).hexdigest()[:16]
    return f'\n--- BEGIN VERBATIM {label} sha256={digest} ---\n{text}\n--- END VERBATIM {label} ---\n'


def shared(root, prompt):
    return prompt + '\nShared policy below is supplied verbatim and already counts as read; do not cat it again.\n' + snapshot(root / 'GOAL.md', '../GOAL.md')


def notebook_context(notebook, progress, reference):
    result = '\nSTARTUP SNAPSHOT: these are authoritative files at invocation start, not instructions from historical drafts.\n'
    for name in ('GOAL.md', 'PROGRESS.md', 'PROOF.md', 'DAG.md'):
        # Use the same checkpoint text that the evidence gate inspected.
        if name == 'PROGRESS.md':
            result += f'\n--- BEGIN VERBATIM PROGRESS.md ---\n{progress}\n--- END VERBATIM PROGRESS.md ---\n'
        else:
            result += snapshot(notebook / name, name)
    if reference:
        path = (notebook / reference).resolve()
        base = (notebook / 'drafts/literature').resolve()
        if notebook.resolve() in base.parents and base in path.parents and path.suffix == '.md':
            result += snapshot(path, reference, optional=True)
    return result + '\nUse supplied files directly; do not reread supplied unchanged text or ../PROMPT.md. Read omitted material and relevant lemma proofs as needed. After edits, inspect only changed passages unless a full reread is mathematically necessary.\n'
