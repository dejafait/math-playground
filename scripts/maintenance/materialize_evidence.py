#!/usr/bin/env python3
"""Restore byte-identical JSON evidence from versioned lossless archives.

No network requests, inference, arithmetic regeneration or changed-file overwrite.
"""
import gzip
import hashlib
import json
import os
from pathlib import Path
import tempfile


def digest(path):
    result = hashlib.sha256()
    with path.open('rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            result.update(chunk)
    return result.hexdigest()


def contained(root, relative):
    path = (root / relative).resolve()
    if root not in path.parents:
        raise ValueError('Evidence path escapes repository: ' + relative)
    return path


def materialize(root, manifest=None, verify_existing=True):
    root = Path(root).resolve()
    manifest = manifest or root / 'scripts/maintenance/compressed-evidence.json'
    if not manifest.exists():
        return 0
    document = json.loads(manifest.read_text())
    if document.get('schema_version') != 1:
        raise ValueError('Unsupported evidence manifest')
    restored = 0
    for item in document['artifacts']:
        target = contained(root, item['path'])
        archive = contained(root, item['archive'])
        if target.exists():
            if not verify_existing:
                continue
            if target.stat().st_size != item['bytes'] or digest(target) != item['sha256']:
                raise ValueError('Refusing to overwrite changed evidence: ' + item['path'])
            continue
        if digest(archive) != item['archive_sha256']:
            raise ValueError('Archive checksum mismatch: ' + item['archive'])
        target.parent.mkdir(parents=True, exist_ok=True)
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(dir=target.parent, prefix='.restore-', delete=False) as out:
                temporary = Path(out.name)
                actual, size = hashlib.sha256(), 0
                with gzip.open(archive, 'rb') as source:
                    for chunk in iter(lambda: source.read(1024 * 1024), b''):
                        size += len(chunk)
                        if size > item['bytes']:
                            raise ValueError('Expanded evidence exceeds declared length')
                        actual.update(chunk)
                        out.write(chunk)
            if size != item['bytes'] or actual.hexdigest() != item['sha256']:
                raise ValueError('Expanded evidence checksum mismatch: ' + item['path'])
            # Never replace a concurrently created or changed user file.
            os.link(temporary, target)
            restored += 1
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
    return restored


if __name__ == '__main__':
    count = materialize(Path(__file__).resolve().parents[2])
    print(f'Restored {count} certificate file(s); all expanded hashes match.')
