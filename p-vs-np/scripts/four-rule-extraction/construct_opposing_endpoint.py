"""Step 485: a single fixed source-guided opposing-units transcript.

No tautology solver, saturation, general proof compiler or extraction. Helpers
expand only Shoenfield's assessed structural operations into primitive records.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
from parameterized_input import CAPS, request, input_bounds, write_json, check_tree

HERE = Path(__file__).resolve().parent
BASE = HERE / 'output-461/final/opposing-units'
OUT = HERE / 'output-485'
LIMIT = 1000


def N(a):
    return ['not', a]


def O(a, b):
    return ['or', a, b]


def A(a, b):
    return N(O(N(a), N(b)))


def fold(xs):
    assert xs
    t = xs[-1]
    for x in reversed(xs[:-1]):
        t = O(x, t)
    return t


def enc(t):
    return (json.dumps(t, separators=(',', ':')) + '\n').encode()


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    OUT.mkdir(exist_ok=False)
    pins = {k: (BASE/k).read_bytes() for k in
            ('source.json', 'annotations.json', 'request.json', 'proof.jsonl')}
    write_json(OUT/'retained-inputs.json', {k: sha(v) for k,v in pins.items()})
    req = json.loads(pins['request.json'])
    assert json.loads(pins['source.json']) == dict(format='ordered-width-three-v1',
        clauses=[dict(literals=[dict(variable='x', negative=False)],tree=0),
                 dict(literals=[dict(variable='x', negative=True)],tree=0)],
        tree=['and',0,1])
    assert json.loads(pins['annotations.json']) == dict(format='L087-occurrences-v1',
        gadget=['u','v'], names=[['y0'],['y1'],['y2','y3'],['y4','y5']],
        alphabet=['y5','y4','y3','y2','y1','y0'])
    p, q = N('y0'), N('y1')
    f = A(p, N(q))
    g1, g2 = O(N('y2'),N('y3')), O(N(N('y4')),N(N('y5')))
    c = A(A(f,g1),g2)
    a, b = A(N(p),N(q)), A(p,q)
    u0 = O(a,b)
    u1 = O(A(N(N('y2')),N(N('y4'))),A(N('y2'),N('y4')))
    u2 = O(A(N(N('y3')),N(N('y5'))),A(N('y3'),N('y5')))
    u = A(u0,A(u1,u2))
    goal = N(A(c,u))
    assert goal == req['goal']
    header = dict(format='literal-four-rule-v1',alphabet=req['alphabet'],goal=goal)
    path = OUT/'proof.jsonl'
    path.write_bytes(enc(header))
    records, stages = [], []
    nodes = check_tree(goal,set(req['alphabet']))
    stage = 'initialization'

    def add(tag,t,*refs):
        nonlocal nodes
        r = dict(rule=tag,f=t,refs=list(refs))
        raw = enc(r)
        needed = check_tree(t,set(req['alphabet']))
        assert len(records)+1 <= LIMIT, 'attempt record cap'
        assert nodes+needed <= CAPS['tree_nodes'], 'aggregate formula node cap'
        assert path.stat().st_size+len(raw) <= CAPS['input_bytes'], 'proof byte cap'
        with path.open('ab') as out:
            out.write(raw)
        records.append(r)
        nodes += needed
        return len(records)-1

    def at(i,t):
        assert records[i]['f'] == t, 'derived operation endpoint mismatch'
        return i

    def ax(t):
        return add('axiom',O(N(t),t))

    def exp(i,t):
        return add('expansion',O(t,records[i]['f']),i)

    def com(i):
        _,x,y = records[i]['f']
        return add('cut',O(y,x),i,ax(x))

    def assoc(i):
        _,x,(_,y,z) = records[i]['f']
        return add('association',O(O(x,y),z),i)

    def contract(i):
        _,x,y = records[i]['f']
        assert x == y
        return add('contraction',x,i)

    def cut(i,j):
        _,x,y = records[i]['f']
        _,nx,z = records[j]['f']
        assert nx == N(x), 'cut pivot mismatch'
        return add('cut',O(y,z),i,j)

    def rearrange(i,xs,ys):
        # Expand source (A)/(A') on actual proved disjunctions. This is
        # structural reception, never a search for a proof or a truth test.
        at(i,fold(xs))
        assert all(x in ys for x in xs)
        m = len(xs)
        if xs == ys:
            return i
        if m == 1:
            k = ys.index(xs[0])
            if k+1 < len(ys):
                i = com(exp(i,fold(ys[k+1:])))
            for x in reversed(ys[:k]):
                i = exp(i,x)
        elif m == 2:
            x,y = xs
            if x == y:
                return rearrange(contract(i),[x],ys)
            k,l = ys.index(x),ys.index(y)
            if k > l:
                return rearrange(com(i),[y,x],ys)
            if len(ys) == 2:
                return at(i,fold(ys))
            if k >= 1:
                i = exp(rearrange(i,xs,ys[1:]),ys[0])
            elif l >= 2:
                i = rearrange(i,xs,[ys[0]]+ys[2:])
                i = com(assoc(exp(com(i),ys[1])))
            else:
                # Insert the right-associated tail after the two premises.
                i = com(assoc(exp(i,fold(ys[2:]))))
                i = com(assoc(i))
        else:
            target = fold(ys)
            x,y = xs[:2]
            i = rearrange(assoc(i),[O(x,y)]+xs[2:],[O(x,y)]+ys)
            i = assoc(com(i))                  # (target or x) or y
            i = rearrange(i,[O(target,x),y],[O(target,x)]+ys)
            i = assoc(com(i))                  # (target or target) or x
            i = rearrange(i,[O(target,target),x],[O(target,target)]+ys)
            # Now (target or target) or target. Expand and rotate at the
            # whole-formula level to a square, then contract twice. No
            # contextual contraction or inverse association is assumed.
            i = assoc(com(assoc(exp(i,target))))
            i = contract(contract(i))
        return at(i,fold(ys))

    def dn_left(i):
        _,x,y = records[i]['f']
        j = com(ax(N(x)))
        return at(com(cut(i,j)),O(N(N(x)),y))

    def join_neg(i,j,x,y,z):
        at(i,O(N(x),z)); at(j,O(N(y),z))
        h = N(O(x,y))
        k = com(assoc(ax(O(x,y))))             # y or (h or x)
        k = com(assoc(k))                      # x or (y or h)
        k = cut(k,i)                          # (y or h) or z
        k = rearrange(com(k),[z,y,h],[y,z,h])
        k = cut(k,j)                          # (z or h) or z
        k = com(k)                            # z or (z or h)
        return at(rearrange(k,[z,z,h],[h,z]),O(h,z))

    def dn(i):
        # L097 §10's standalone bridge, applied to an actually proved tree.
        x = records[i]['f']; nn = N(N(x))
        j = ax(N(x)); k = exp(i,nn); h = ax(nn)
        v = cut(k,h); w = cut(j,h)
        return at(contract(cut(v,w)),nn)

    def save(label,i):
        stages.append(dict(label=label,record=i,endpoint=records[i]['f']))
        write_json(OUT/'stages.json',stages)
        return i

    spec = importlib.util.spec_from_file_location('literal_checker_485',
                                                 HERE.parent/'parity-four-rule/checker.py')
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    try:
        # Explicit complementary closures for this fixed equality core.
        # Desired common context is S = not-p or not-not-q. These closures
        # use the two opposite source literals and their actual consistency
        # group, not a Boolean identification of occurrence names.
        stage = 'equality first branch'
        s = O(N(p),N(N(q)))
        i = dn_left(com(ax(p)))                # NN p or N p
        i = rearrange(i,[N(N(p)),N(p)],[N(p),N(N(q)),N(N(p)),N(N(q))])
        i = dn_left(com(assoc(i)))
        save('first-consistency-disjunct',at(i,O(N(a),s)))
        stage = 'equality second branch'
        j = rearrange(ax(N(q)),[N(N(q)),N(q)],[N(p),N(N(q)),N(p),N(q)])
        j = dn_left(com(assoc(j)))
        save('second-consistency-disjunct',at(j,O(N(b),s)))
        stage = 'two-premise negated-disjunction case'
        k = com(join_neg(i,j,a,b,s))
        k = dn_left(k)
        save('source-and-first-consistency-core',at(k,O(N(f),N(u0))))
        stage = 'opaque gadget attachment'
        for sibling in (g1,g2):
            _,x,z = records[k]['f']
            k = rearrange(k,[x,z],[z,x,N(sibling)])
            k = dn_left(com(k))
        save('both-gadgets-attached',at(k,O(N(c),N(u0))))
        stage = 'remaining consistency attachment'
        k = com(k)
        k = rearrange(k,[N(u0),N(c)],[N(c),N(u0),N(A(u1,u2))])
        k = com(dn_left(com(k)))
        save('whole-formula-before-standalone-bridge',at(k,O(N(c),N(u))))
        stage = 'standalone double negation and strict reception'
        k = dn(k)
        save('exact-goal',at(k,goal))
        raw = path.read_bytes()
        checked = checker.check_bytes(raw,goal,CAPS['input_bytes'])
        fresh = dict(req,source_sha256=sha(raw))
        fresh_path = OUT/'request.json'
        write_json(fresh_path,fresh,'input_bytes')
        received,received_raw,received_records,strict = request(path,fresh_path)
        assert received == fresh and received_raw == raw and received_records == records
        assert strict == checked
        assert all(fresh[k] == req[k] for k in ('goal','alphabet','dictionary','format'))
        metrics = input_bounds(fresh,raw,records,fresh_path)
        assert metrics['actual']['source_lines'] <= LIMIT
        unchanged = {k:(BASE/k).read_bytes()==v for k,v in pins.items()}
        assert all(unchanged.values())
        result = dict(accepted=True,literal_receipt=checked,input_bounds=metrics,
            attempt_records=dict(actual=len(records),required=LIMIT),
            retained_inputs_unchanged=unchanged,changed_request_fields=['source_sha256'],
            exact_goal_alphabet_dictionary=True,extraction_performed=False,
            full_composition_performed=False,failures=[])
        write_json(OUT/'verification.json',result)
        print(json.dumps(dict(accepted=True,records=len(records),attempt_cap=LIMIT,
            actual=metrics['actual'],required=metrics['required'],failures=[],
            certificate=str(path.relative_to(HERE.parent.parent)),
            receipt=str((OUT/'verification.json').relative_to(HERE.parent.parent)))))
    except Exception as error:
        prefix_receipt = None
        if records:
            last = records[-1]['f']
            prefix = enc(dict(header,goal=last))+b''.join(enc(r) for r in records)
            (OUT/'checked-prefix.jsonl').write_bytes(prefix)
            try:
                prefix_receipt = checker.check_bytes(prefix,last,CAPS['input_bytes'])
            except Exception as pe:
                prefix_receipt = dict(accepted=False,error=repr(pe))
        write_json(OUT/'failure.json',dict(accepted=False,error=repr(error),stage=stage,
            records=len(records),attempt_cap=LIMIT,aggregate_nodes=nodes,
            checked_prefix=prefix_receipt,exact_target=goal,
            last_endpoint=records[-1]['f'] if records else None,
            retained_inputs_unchanged={k:(BASE/k).read_bytes()==v for k,v in pins.items()},
            extraction_performed=False,full_composition_performed=False))
        print(json.dumps(dict(accepted=False,stage=stage,error=repr(error),
            records=len(records),attempt_cap=LIMIT,prefix_accepted=prefix_receipt,
            evidence=str((OUT/'failure.json').relative_to(HERE.parent.parent)))))
        return


if __name__ == '__main__':
    main()
