"""Step 471: one supplied-proof reception, with full failure checkpoints.

Consumes existing immutable proof bytes. Never constructs a proof or changes
production caps. Run from the notebook root; existing outputs are refused.
"""
import hashlib
import json
import traceback
from pathlib import Path

import emit_occurrence
import receive_occurrence
from occurrence_input import context
from parameterized_input import CAPS, input_bounds, request, write_json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = HERE / 'output-461/final/empty-clause'
SUPPLIED = HERE / 'output-470'
OUT = HERE / 'output-471'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def relative(path):
    return str(path.relative_to(ROOT))


def main():
    OUT.mkdir(exist_ok=False)
    inputs = OUT / 'inputs'
    inputs.mkdir()
    originals = {k: BASE / (k + '.json') for k in ('source', 'annotations', 'pair')}
    originals.update(proof=SUPPLIED / 'proof.jsonl', request=SUPPLIED / 'request.json')
    # The old diagnostic proof/request are pinned too, without relabeling them.
    pinned_paths = list(originals.values()) + [BASE / 'proof.jsonl', BASE / 'request.json']
    pinned = {relative(p): digest(p.read_bytes()) for p in pinned_paths}
    write_json(OUT / 'preservation-before.json', pinned)
    selected = {}
    for key, path in originals.items():
        target = inputs / (key + ('.jsonl' if key == 'proof' else '.json'))
        target.write_bytes(path.read_bytes())
        selected[key] = target
    manifest = dict(format='L097-occurrence-caller-v1',
                    **{k: digest(p.read_bytes()) for k, p in selected.items()})
    write_json(inputs / 'manifest.json', manifest, 'input_bytes')
    selected['manifest'] = inputs / 'manifest.json'
    sources = [HERE / (x + '.py') for x in
               ('emit_occurrence', 'receive_occurrence', 'occurrence_input',
                'emit_parameterized', 'receive_parameterized', 'parameterized_input',
                'audit_parameterized', 'receive_positive_occurrence')]
    sources += [HERE.parent / 'parity-four-rule/checker.py',
                HERE.parent / 'affine-abp-boolean/check_suffix_graph.py',
                HERE.parent / 'affine-abp-commutator/check_marked_graph.py']
    # Hash actual inputs before any potentially lengthy construction.
    existing = [p for p in sources if p.is_file()]
    write_json(OUT / 'source-hashes.json',
               {relative(p): digest(p.read_bytes()) for p in existing})
    stage = 'caller-preflight'
    try:
        ctx = context(**{k + '_path': p for k, p in selected.items()})
        req, raw, records, checked = request(selected['proof'], selected['request'])
        write_json(OUT / 'preflight.json', dict(
            occurrence=ctx['input_metrics'], literal=checked,
            bounds=input_bounds(req, raw, records, selected['request']),
            approved_target='Implement a bounded receiver from a supplied four-rule proof of the exact complemented occurrence-CNF endpoint to the unchanged L097 fg/B witness.',
            originals={k: relative(p) for k, p in originals.items()}, caps=CAPS))
        stage = 'emission'
        built = emit_occurrence.emit(**selected, output=OUT / 'emitted')
        write_json(OUT / 'emission.json', built)
        stage = 'reception'
        received = receive_occurrence.receive(
            **selected, K=OUT / 'emitted/K.json', H=OUT / 'emitted/H.json')
        write_json(OUT / 'reception.json', received)
        write_json(OUT / 'verification.json', dict(
            completed=True, accepted=True, stage=stage, caps=CAPS,
            forward_verification='pending', failures=[]))
        print(dict(completed=True, accepted=True, stage=stage,
                   bounds=received['bounds'], path=relative(OUT / 'verification.json')))
    except Exception as error:
        # Serialize complete relevant frame state, not a preview. A generic
        # emitter preflight may fail before its usual final certificate exists.
        frames = []
        trace = error.__traceback__
        keep = ('out', 'blocks', 'i', 'r', 'seed', 'kind', 'args', 'parent',
                'f', 'g', 'a', 'bb', 'cc', 'nv', 'ne', 'p', 'q', 'n', 'stage')
        while trace is not None:
            frame = trace.tb_frame
            filename = Path(frame.f_code.co_filename).resolve()
            if filename.is_relative_to(HERE.parent):
                values = {}
                for key in keep:
                    if key in frame.f_locals:
                        value = frame.f_locals[key]
                        try:
                            json.dumps(value)
                        except (TypeError, ValueError):
                            continue
                        values[key] = value
                artifact = OUT / ('failure-frame-' + str(len(frames)) + '.json')
                write_json(artifact, values)
                frames.append(dict(function=frame.f_code.co_name,
                                   source=relative(filename), line=trace.tb_lineno,
                                   evidence=relative(artifact)))
            trace = trace.tb_next
        write_json(OUT / 'failure.json', dict(
            completed=False, accepted=False, stage=stage,
            failure=repr(error), detail=list(error.args), frames=frames,
            construction=emit_occurrence.extraction.CONSTRUCTION.copy(),
            traceback=traceback.format_exc(), caps=CAPS))
        write_json(OUT / 'verification.json', dict(
            completed=False, accepted=False, stage=stage, caps=CAPS,
            failures=[repr(error)], evidence=relative(OUT / 'failure.json')))
        print(dict(completed=False, accepted=False, stage=stage,
                   failure=repr(error), path=relative(OUT / 'failure.json')))
    finally:
        after = {relative(p): digest(p.read_bytes()) for p in pinned_paths}
        unchanged = after == pinned
        write_json(OUT / 'preservation-after.json', dict(unchanged=unchanged, hashes=after))
        assert unchanged, 'retained input changed'


if __name__ == '__main__':
    main()
