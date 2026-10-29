"""Step 489 independent trace/reference reception for the explicit units caller.

No emitter, adapter or correction constructor is imported. The inherited full
receiver is unchanged; only original-caller preservation and truthful success
qualification are adapted, with an additional full nonzero-fJ discriminator.
"""
import hashlib
import sys
from pathlib import Path
import verify_trimmed_occurrence as base
import verify_empty_central_occurrence as selected
import parameterized_input as inputs
from receive_selected_commutator import install_evidence_budget

HERE = Path(__file__).resolve().parent
OUT = HERE / 'output-489'
ROOT = HERE.parents[1]


def preservation():
    scope = inputs.load(OUT / 'run-scope.json')
    inputs.require(inputs.exact_equal(scope['caps'], inputs.CAPS), 'unchanged scope caps')
    inputs.require(scope['caller_base'] == 'scripts/four-rule-extraction/output-461/final/opposing-units'
                   and scope['supplied'] == 'scripts/four-rule-extraction/output-485',
                   'explicit approved caller combination')
    hashes = inputs.load(OUT / 'preservation-before.json')
    hashes.update(inputs.load(OUT / 'source-hashes.json'))
    hashes.update(scope['source_hashes'])
    for name, digest in hashes.items():
        inputs.require(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest,
                       'unchanged source/input bytes: ' + name)
    manifest = inputs.load(OUT / 'inputs/manifest.json')
    for key in ('source', 'annotations', 'pair', 'proof', 'request'):
        filename = key + ('.jsonl' if key == 'proof' else '.json')
        copied = (OUT / 'inputs' / filename).read_bytes()
        original = HERE / ('output-485' if key in ('proof', 'request') else
                           'output-461/final/opposing-units') / filename
        inputs.require(copied == original.read_bytes() and
                       hashlib.sha256(copied).hexdigest() == manifest[key],
                       'exact unchanged original opposing-units caller bytes')
    inputs.require(inputs.load(OUT / 'preservation-after.json')['unchanged'] is True,
                   'driver preservation completed')
    return hashes


class Reception(selected.Reception):
    def __init__(self, *args):
        super().__init__(*args)
        global active_receiver
        active_receiver = self


def main():
    inputs.require(not any(name in sys.modules for name in
                   ('emit_parameterized', 'emit_occurrence', 'empty_central_translation',
                    'constant_translation')), 'separate receiver process imports no constructors')
    base.OUT = selected.OUT = OUT
    base.Reception = Reception
    base.preservation = preservation
    original = inputs.write_json
    aliases = [name for name, module in list(sys.modules.items())
               if module is not None and getattr(module, 'write_json', None) is original]
    writer = install_evidence_budget(OUT)
    inputs.require(all(getattr(sys.modules[name], 'write_json') is writer for name in aliases),
                   'all observed receiver writer aliases rebound')

    def save(path, result, key='certificate_bytes'):
        if Path(path) == OUT / 'integration-reception.json' and result['accepted']:
            receiver = active_receiver
            correction = receiver.hdata['correction']
            polys = receiver.evaluate(
                # Already typed in H; evaluate directly below instead of retranslating.
                # This branch uses the same bounded arithmetic on its actual graph.
                untyped(correction['graphs']['fJ'], receiver.transport),
                ('free', 'zero', 'axioms'))
            received = inputs.load(OUT / 'reception.json')['correction']['graphs']['fJ']
            inputs.require(all(inputs.exact_equal(base.serial(poly), received[mode])
                               for mode, poly in polys.items()), 'complete fJ receiver agreement')
            inputs.require(not polys['zero'] and bool(polys['axioms']),
                           'nonempty complete substituted fJ discriminator')
            inputs.require(receiver.statistics['occurrence_direct_calls'] == 3,
                           'all three opposing-units correction calls')
            writer(OUT / 'nonzero-fJ.json', dict(
                accepted=True, polynomials={mode: base.serial(poly) for mode, poly in polys.items()},
                word_counts={mode: len(poly) for mode, poly in polys.items()},
                arithmetic=receiver.ar.counts, caps=inputs.CAPS, failures=[]))
            result.update(nonzero_fJ_received=True, nonzero_evidence='nonzero-fJ.json',
                          trace_arithmetic=receiver.ar.counts,
                          receiver_writer_aliases=aliases,
                          qualifications=['finite reproduction; separate critical audit pending',
                                          'complete nonzero substituted fJ received',
                                          'trusted paths and remaining SHA bindings retained',
                                          'not total interpreter work or memory'])
        return writer(path, result, key)

    # Only the final receipt write gains the extra discriminator. All original
    # recipe, event, copy, production receipt and hash checks run inside base.main.
    base.write_json = save
    base.main()


def untyped(graph, transport):
    inverse = {tuple(value): key for key, value in transport.items()}
    return dict(vertices=graph['vertices'], source=graph['source'], sink=graph['sink'],
                edges=[[u, v, [inverse[tuple(a)] for a in lab]] for u, v, lab in graph['edges']])


if __name__ == '__main__':
    main()
