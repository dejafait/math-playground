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


def main():
    require((ROOT / 'PROMPT.md').is_file(), 'Missing sole research prompt: PROMPT.md')
    for vendor in ('codex', 'claude', 'gemini', 'grok'):
        require((ROOT / f'loop-{vendor}.sh').is_file(), f'Missing root launcher: loop-{vendor}.sh')
    require(not re.search(r'^## (?:Initial|Recurrent) prompt', (ROOT / 'README.md').read_text(), re.M), 'README must link to PROMPT.md instead of maintaining runnable prompts.')
    dag = (ROOT / 'DAG.md').read_text()
    blocks = re.findall(r'```mermaid\n(.*?)```', dag, re.S)
    require(len(blocks) == 1, 'DAG.md must contain exactly one Mermaid graph.')
    if len(blocks) != 1:
        return finish()
    nodes, targets, edges = {}, {}, set()
    for line in blocks[0].splitlines():
        line = line.strip()
        if line == 'flowchart TD' or not line:
            continue
        node = re.fullmatch(rf'({ID})\["([^"\n]+)"\]', line)
        target = re.fullmatch(rf'click ({ID}) "(lemmas/[^"\n]+\.md)"', line)
        edge = re.fullmatch(rf'({ID}(?: & {ID})*) --> ({ID})', line)
        if node:
            ident, title = node.groups()
            require(ident not in nodes, f'Duplicate node: {ident}')
            nodes[ident] = title
        elif target:
            ident, path = target.groups()
            require(ident not in targets, f'Duplicate file target: {ident}')
            targets[ident] = path
        elif edge:
            parents, child = edge.groups()
            for parent in parents.split(' & '):
                require((parent, child) not in edges, f'Duplicate edge: {parent} -> {child}')
                edges.add((parent, child))
        else:
            errors.append(f'Unsupported graph syntax: {line}')
    require(set(nodes) == set(targets), 'Every graph node needs exactly one file target.')
    files = {str(p.relative_to(ROOT)) for p in (ROOT / 'lemmas').glob('*.md')}
    require(set(targets.values()) == files, 'Graph targets must cover exactly the lemma files.')
    require(len(set(targets.values())) == len(targets), 'Multiple nodes target the same file.')
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
    for ident, target in targets.items():
        require(Path(target).name.startswith(ident + '-'), f'File ID mismatch: {target}')
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:
            continue
        text = path.read_text()
        rel = path.relative_to(ROOT)
        if path.name != 'DAG.md':
            require('```mermaid' not in text, f'Graph outside DAG.md: {rel}')
            require(not re.search(rf'\b{ID}\s*(?:-->|->)', text), f'Edge record outside DAG.md: {rel}')
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
