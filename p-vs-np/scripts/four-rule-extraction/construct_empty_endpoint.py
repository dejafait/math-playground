"""Step 470: one fixed empty-clause transcript, no search or extraction.

Run from the notebook root. An existing output directory is never overwritten.
The independent checker imports no construction code from this module.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
from parameterized_input import CAPS, request, input_bounds, write_json

HERE = Path(__file__).resolve().parent
BASE = HERE / 'output-461/final/empty-clause'
OUT = HERE / 'output-470'
ATTEMPT_CAP = 1000


def N(a):
    return ['not', a]


def O(a, b):
    return ['or', a, b]


def A(a, b):
    return N(O(N(a), N(b)))


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(x):
    return (json.dumps(x, separators=(',', ':')) + '\n').encode()


def main():
    OUT.mkdir(exist_ok=False)
    pinned = {k: (BASE / k).read_bytes() for k in
              ('source.json', 'annotations.json', 'request.json', 'proof.jsonl')}
    write_json(OUT / 'retained-inputs.json', {k: sha(v) for k, v in pinned.items()})
    source = json.loads(pinned['source.json'])
    ann = json.loads(pinned['annotations.json'])
    req = json.loads(pinned['request.json'])
    assert source == dict(format='ordered-width-three-v1',
                          clauses=[dict(literals=[], tree='false')], tree=0)
    assert ann == dict(format='L087-occurrences-v1', gadget=['u', 'v'],
                       names=[[], ['y0', 'y1'], ['y2', 'y3']],
                       alphabet=['y3', 'y2', 'y1', 'y0'])
    # Explicit reconstruction of this one input; siblings remain opaque trees.
    g1 = O(N('y0'), N('y1'))
    g2 = O(N(N('y2')), N(N('y3')))
    u0 = O(A(N(N('y0')), N(N('y2'))), A(N('y0'), N('y2')))
    u1 = O(A(N(N('y1')), N(N('y3'))), A(N('y1'), N('y3')))
    c = A(A('false', g1), g2)
    u = A(u0, u1)
    goal = N(A(c, u))
    assert goal == req['goal']
    header = dict(format='literal-four-rule-v1', alphabet=req['alphabet'], goal=goal)
    records, operations = [], []
    proof_path = OUT / 'proof.jsonl'
    proof_path.write_bytes(encode(header))

    def add(tag, f, *refs):
        assert len(records) < ATTEMPT_CAP, 'attempt record cap'
        record = dict(rule=tag, f=f, refs=list(refs))
        raw = encode(record)
        assert proof_path.stat().st_size + len(raw) <= CAPS['input_bytes']
        with proof_path.open('ab') as stream:
            stream.write(raw)
        records.append(record)
        return len(records) - 1

    def ax(a):
        return add('axiom', O(N(a), a))

    def commute(i):
        _, a, b = records[i]['f']
        j = ax(a)
        return add('cut', O(b, a), i, j)

    def append_right(i, b):
        a = records[i]['f']
        j = add('expansion', O(b, a), i)
        return commute(j)

    def double_negate(i):
        a = records[i]['f']
        nn = N(N(a))
        j = ax(N(a))                         # NN A or N A
        k = add('expansion', O(nn, a), i)     # NN A or A
        h = ax(nn)                           # NNN A or NN A
        p = add('cut', O(a, nn), k, h)
        q = add('cut', O(N(a), nn), j, h)
        r = add('cut', O(nn, nn), p, q)
        return add('contraction', nn, r)

    spec = importlib.util.spec_from_file_location('independent_literal_checker',
                                                 HERE.parent / 'parity-four-rule/checker.py')
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    try:
        i = add('not-false', N('false'))
        for label, sibling in [('first-gadget', g1), ('second-gadget', g2),
                               ('consistency', u)]:
            start = len(records)
            i = double_negate(append_right(i, N(sibling)))
            operations.append(dict(label=label, start=start, end=i,
                                   exact_endpoint=records[i]['f']))
            write_json(OUT / 'operations.json', operations)
        assert records[i]['f'] == goal
        raw = proof_path.read_bytes()
        checked = checker.check_bytes(raw, goal, CAPS['input_bytes'])
        # The old caller request binds INVALID diagnostic bytes. Preserve it;
        # this fresh request changes only that explicitly caller-owned digest.
        fresh = dict(req, source_sha256=sha(raw))
        request_path = OUT / 'request.json'
        write_json(request_path, fresh, 'input_bytes')
        received, received_raw, received_records, strict = request(proof_path, request_path)
        assert received == fresh and received_raw == raw and received_records == records
        assert strict == checked
        assert fresh['goal'] == req['goal'] and fresh['alphabet'] == req['alphabet']
        assert fresh['dictionary'] == req['dictionary']
        metrics = input_bounds(fresh, raw, records, request_path)
        assert metrics['actual']['source_lines'] <= ATTEMPT_CAP
        unchanged = {k: (BASE / k).read_bytes() == v for k, v in pinned.items()}
        assert all(unchanged.values())
        result = dict(accepted=True, literal_receipt=checked, input_bounds=metrics,
                      attempt_records=dict(actual=len(records), required=ATTEMPT_CAP),
                      retained_inputs_unchanged=unchanged,
                      changed_request_fields=['source_sha256'],
                      exact_goal_alphabet_dictionary=True,
                      extraction_performed=False, full_composition_performed=False,
                      failures=[])
        write_json(OUT / 'verification.json', result)
        print(json.dumps(dict(accepted=True, records=len(records), attempt_cap=ATTEMPT_CAP,
                              actual=metrics['actual'], required=metrics['required'],
                              failures=[], certificate=str(proof_path.relative_to(HERE.parent.parent)),
                              receipt=str((OUT/'verification.json').relative_to(HERE.parent.parent)))))
    except Exception as error:
        prefix_receipt = None
        if records:
            last = records[-1]['f']
            prefix = encode(dict(header, goal=last)) + b''.join(encode(r) for r in records)
            (OUT / 'partial-prefix.jsonl').write_bytes(prefix)
            try:
                prefix_receipt = checker.check_bytes(prefix, last, CAPS['input_bytes'])
            except Exception as prefix_error:
                prefix_receipt = dict(accepted=False, error=repr(prefix_error))
        write_json(OUT / 'failure.json', dict(error=repr(error), records=len(records),
                   required_records=ATTEMPT_CAP, checked_prefix=prefix_receipt,
                   exact_target=goal, last_endpoint=records[-1]['f'] if records else None))
        raise


if __name__ == '__main__':
    main()
