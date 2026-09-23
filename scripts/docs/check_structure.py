#!/usr/bin/env python3
"""Validate notebook layout; DAG.md is read directly, never copied or generated.

This checks storage invariants, links, and acyclicity, not mathematical correctness
or completeness of dependencies. Run from any working directory.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
ID = r'(?:L\d{3}|C\d{3}[a-z]?)'
errors = []


def require(condition, message):
    if not condition:
        errors.append(message)


def parse_dag(text):
    """Parse ID-only adjacency rows; reject redundant titles, paths, and Mermaid."""
    problems = []
    blocks = re.findall(r'```text\n(.*?)```', text, re.S)
    expected_intro = ('# Lemma dependencies\n\n'
                      '`ID: inputs` lists direct mathematical dependencies; empty means none. '
                      'Find statements in `lemmas/ID-*.md`.\n\n')
    if len(blocks) != 1 or text != expected_intro + '```text\n' + blocks[0] + '```\n':
        return set(), set(), ['DAG.md must use the minimal header and one text block of ID-only rows.']
    nodes, edges = set(), set()
    for line in blocks[0].splitlines():
        match = re.fullmatch(rf'({ID}):((?: {ID})*)', line)
        if not match:
            problems.append(f'Invalid dependency row: {line}')
            continue
        child, parents = match.groups()
        if child in nodes:
            problems.append(f'Duplicate node: {child}')
        nodes.add(child)
        for parent in parents.split():
            if (parent, child) in edges:
                problems.append(f'Duplicate edge: {parent} -> {child}')
            edges.add((parent, child))
    return nodes, edges, problems


def main():
    require((ROOT / 'PROMPT.md').is_file(), 'Missing sole research prompt: PROMPT.md')
    require((ROOT / 'loop-codex.sh').is_file(), 'Missing root launcher: loop-codex.sh')
    require(not re.search(r'^## (?:Initial|Recurrent) prompt', (ROOT / 'README.md').read_text(), re.M), 'README must link to PROMPT.md instead of maintaining runnable prompts.')
    dag = (ROOT / 'DAG.md').read_text()
    nodes, edges, parse_errors = parse_dag(dag)
    errors.extend(parse_errors)
    files = {}
    for path in (ROOT / 'lemmas').glob('*.md'):
        match = re.fullmatch(rf'({ID})-.+\.md', path.name)
        require(match is not None, f'Invalid lemma filename: {path.name}')
        if match:
            ident = match[1]
            require(ident not in files, f'Multiple lemma files for ID: {ident}')
            files[ident] = path
    require(nodes == set(files), 'DAG IDs must cover exactly the lemma files.')
    adjacency = {ident: [] for ident in nodes}
    for parent, child in edges:
        require(parent in nodes and child in nodes, f'Unknown endpoint: {parent} -> {child}')
        if parent in nodes and child in nodes:
            adjacency[parent].append(child)
    visiting, visited = set(), set()

    def visit(ident):
        if ident in visiting:
            errors.append(f'Cycle involving {ident}')
            return
        if ident in visited:
            return
        visiting.add(ident)
        for child in adjacency[ident]:
            visit(child)
        visiting.remove(ident)
        visited.add(ident)

    for ident in nodes:
        visit(ident)
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:
            continue
        text = path.read_text()
        rel = path.relative_to(ROOT)
        if path.name != 'DAG.md':
            require('```mermaid' not in text, f'Graph outside DAG.md: {rel}')
            require(not re.search(rf'\b{ID}\s*(?:-->|->)', text), f'Edge record outside DAG.md: {rel}')
            require(not re.search(rf'^({ID}):(?: {ID})*$', text, re.M), f'Dependency row outside DAG.md: {rel}')
        if path.parent == ROOT / 'lemmas':
            require(not re.search(r'(?im)^(?:#+\s*|\*\*)?(?:depends on|dependencies|used by|dependents)\b', text), f'Dependency section in {rel}')
            require(not text.startswith('---\n'), f'Metadata header in {rel}; graph metadata belongs in DAG.md.')
        for url in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)', text):
            if re.match(r'\w+://', url) or url.startswith('#'):
                continue
            destination = (path.parent / url.split('#', 1)[0]).resolve()
            require(destination.exists(), f'Broken link in {rel}: {url}')
            if path.parent == ROOT / 'lemmas':
                require(destination.parent != ROOT / 'lemmas', f'Inter-lemma link in {rel}: {url}')
    for name, limit in [('PROGRESS.md', 40), ('PROOF.md', 100)]:
        require(len((ROOT / name).read_text().splitlines()) <= limit, f'{name} exceeds {limit} lines.')
    progress = (ROOT / 'PROGRESS.md').read_text()
    require(len(re.findall(r'^STATUS: ', progress, re.M)) == 1, 'Expected one current status.')
    require(len(re.findall(r'^Next action: ', progress, re.M)) == 1, 'Expected one current next action.')
    require(not re.search(r'^## Next lemma|^Next action:', (ROOT / 'PROOF.md').read_text(), re.M), 'Next action belongs only in PROGRESS.md.')
    if not errors:
        print(f'OK: {len(nodes)} nodes, {len(edges)} unique edges; acyclic graph, complete file coverage, valid local links, and compact overviews.')
    return finish()


def finish():
    for error in errors:
        print('ERROR:', error, file=sys.stderr)
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
