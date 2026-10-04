"""Bounded JSON inspection; never replace an exact certificate with a preview."""
import argparse
import json
from pathlib import Path


def preview(value, depth=0):
    if isinstance(value, dict):
        keys = list(value)
        return {'type': 'object', 'key_count': len(keys), 'keys': keys[:30],
                'preview': {k: preview(value[k], depth+1) for k in keys[:8]} if depth < 2 else None,
                'omitted_keys': max(0, len(keys)-8) if depth < 2 else len(keys)}
    if isinstance(value, list):
        return {'type': 'array', 'length': len(value),
                'first_items': [preview(v, depth+1) for v in value[:3]] if depth < 2 else None,
                'omitted_items': max(0, len(value)-3) if depth < 2 else len(value)}
    if isinstance(value, str) and len(value) > 300:
        return {'type': 'string', 'length': len(value), 'prefix': value[:300], 'truncated': True}
    return value


def select(value, pointer):
    if pointer and not pointer.startswith('/'):
        raise ValueError('JSON pointer must begin with /')
    for part in pointer.split('/')[1:] if pointer else []:
        part = part.replace('~1', '/').replace('~0', '~')
        value = value[int(part)] if isinstance(value, list) else value[part]
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', type=Path)
    parser.add_argument('--pointer', default='', help='Exact JSON pointer to inspect')
    parser.add_argument('--full', action='store_true', help='Print the selected value exactly; may be large')
    args = parser.parse_args()
    try:
        value = select(json.loads(args.path.read_text()), args.pointer)
    except (OSError, ValueError, KeyError, IndexError, TypeError) as exc:
        parser.error(str(exc))
    print(json.dumps(value if args.full else {'preview_only': True, 'certificate': str(args.path),
                                             'pointer': args.pointer, 'value': preview(value)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
