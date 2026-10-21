"""Independent initial-output endpoint reception; no emitter imports."""
import re
import verify

e, c = verify.e, verify.c


def receive(envelope, depth_factor=4):
    if not isinstance(envelope, dict) or set(envelope) != {'source', 'edges', 'request'}:
        raise c.Invalid('initial bridge fields; no optional proof occurrences')
    source = envelope['source']
    if not isinstance(source, dict) or set(source) != {'tree', 'letters', 'q', 'delete_zero'}:
        raise c.Invalid('source fields')
    if type(depth_factor) is not int or depth_factor < 1:
        raise c.Invalid('fixed positive admission constant')
    if type(source['delete_zero']) is not bool or not isinstance(source['letters'], list):
        raise c.Invalid('source dictionary/convention')
    names = source['letters'] + [source['q']]
    if any(not isinstance(x, str) or not re.fullmatch(r'[A-Za-z0-9_]+', x) for x in names):
        raise c.Invalid('ASCII names')
    if len(set(source['letters'])) != len(source['letters']):
        raise c.Invalid('distinct dictionary names required')
    y = e.imp(source['q'], source['q'])
    z = e.neg(y)

    def tree(t):
        if not isinstance(t, list) or not t:
            raise c.Invalid('source tree syntax')
        if t[0] in ('add', 'mul') and len(t) == 3:
            l, u, d = tree(t[1]); r, v, f = tree(t[2])
            return (e.xor if t[0] == 'add' else e.prod)(l, r), 1+u+v, 1+max(d, f)
        if t[0] in ('zero', 'one') and len(t) == 1:
            return (z if t[0] == 'zero' else y), 1, 0
        if t[0] == 'var' and len(t) == 2 and type(t[1]) is int and 0 <= t[1] < len(source['letters']):
            return source['letters'][t[1]], 1, 0
        raise c.Invalid('source tree operator/arity/position')

    f, U, d = tree(source['tree'])
    if d > depth_factor * (U+1).bit_length():
        raise c.Invalid('source depth admission')
    # Checks all suffixes, every connector, both bit-table families and terminal.
    verify.contract(source, envelope['edges'], envelope['request'])
    suffix = envelope['request']['suffixes'][0]
    if suffix != c.serialize(e.prod(f, y)):
        raise c.Invalid('initial suffix differs from copied root product')
    return dict(goal=c.serialize(e.eq(f, e.prod(f, y))),
                formula=c.serialize(f), suffix=suffix, U=U, depth=d)
