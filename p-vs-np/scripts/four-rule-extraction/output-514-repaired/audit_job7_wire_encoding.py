"""Step 514: independent complete JSON sizing and L110 framing arithmetic.

Reuse the fixed constructor, not its serializer, for the independent count.
No coordinate search, new graph recipe, schema-acceptance or total-work claim.
"""
from collections import Counter
import json
from pathlib import Path
import struct
import sys
import time
import traceback

import parameterized_input as p
import preflight_job7_transport as original

HERE = Path(__file__).resolve().parent
FAILED = HERE/'output-514'
OUT = HERE/'output-514-repaired'
LIMIT, SECONDS, RESERVE = 100_000_000, 900, 1_000_000


def main():
    if OUT.exists():
        raise RuntimeError('fresh output required; preserve all archives')
    OUT.mkdir()
    started = time.monotonic()
    budget, counts = Counter(), []
    failed_report = json.loads((FAILED/'wire-audit.json').read_bytes())
    auxiliary = failed_report['combined_selected_item_units']
    budget['preserved_failed_metadata_load_units'] = auxiliary
    active = None
    report = dict(status='IN_PROGRESS', failures=[], coordinate_search=False,
                  accepted_equality=False, independent_graph_correspondence=False,
                  strict_transport_decoder_audited=False, total_work_bound=False)

    def guard(n=0):
        total = auxiliary+(active.visits if active is not None else 0)+n
        if total > LIMIT:
            raise original.Stop('ADMINISTRATIVE', dict(resource='combined selected units',
                actual=total, required=LIMIT, auxiliary=dict(budget)))
        if time.monotonic()-started+failed_report['elapsed_seconds'] > SECONDS:
            raise original.Stop('ADMINISTRATIVE', dict(resource='audit seconds',
                actual=time.monotonic()-started, required=SECONDS))

    def tick(kind, n=1):
        nonlocal auxiliary
        guard(n)
        auxiliary += n
        budget[kind] += n

    def walk(value, metadata=False):
        tick('independent_JSON_nodes')
        kind = type(value)
        if kind is dict:
            for key, child in value.items():
                if type(key) is not str:
                    raise AssertionError('JSON key type')
                walk(key, metadata)
                walk(child, metadata)
        elif kind is list:
            for child in value:
                walk(child, metadata)
        elif kind not in (str, int, bool, type(None)) and not (metadata and kind is float):
            raise AssertionError('strict finite JSON value domain')

    class AuditRun(original.Run):
        def __init__(self):
            nonlocal active
            super().__init__()
            active = self

        def tick(self, n=1):
            guard(n)
            super().tick(n)

        def count(self, value, name, previous=0):
            measured = super().count(value, name, previous)
            if name not in ('B_bind', 'B_trans'):
                return measured
            before = dict(budget)
            walk(value)
            independent, fragments, largest = 0, 0, 0
            # iterencode walks the whole object using the library encoder's
            # own punctuation/key/string logic. It never calls Run.chunks.
            encoder = json.JSONEncoder(ensure_ascii=True, separators=(',', ':'),
                                       allow_nan=False, check_circular=True)
            for piece in encoder.iterencode(value):
                tick('independent_encoder_fragments')
                if type(piece) is not str or not piece.isascii():
                    raise AssertionError('complete ASCII output fragment')
                length = len(piece)  # ASCII length equals its UTF-8 byte length.
                independent += length
                fragments += 1
                largest = max(largest, length)
                if previous+independent+RESERVE > p.CAPS['certificate_bytes']:
                    raise original.Stop('ADMINISTRATIVE', dict(resource='wire and reserve',
                        section=name, actual=previous+independent+RESERVE,
                        required=p.CAPS['certificate_bytes'], fragment=fragments))
            if independent != measured:
                raise AssertionError(('independent full count mismatch', name, independent, measured))
            counts.append(dict(section=name, original_bytes=measured,
                independent_bytes=independent, fragments=fragments,
                complete_ASCII_characters_checked=independent,
                max_encoder_fragment_characters=largest,
                independent_nodes=budget['independent_JSON_nodes']-before.get('independent_JSON_nodes', 0),
                payload_saved=False))
            return measured

    def same(a, b):
        tick('complete_receipt_comparison_nodes')
        if type(a) is not type(b):
            return False
        if type(a) is dict:
            return a.keys() == b.keys() and all(same(a[k], b[k]) for k in a)
        if type(a) is list:
            return len(a) == len(b) and all(same(x, y) for x, y in zip(a, b))
        return a == b

    def endpoint(dims, framing, full):
        # Build actual fixed headers; size only the hypothetical coordinate arrays.
        header = struct.pack('<8sQQQ', b'J7F2C001', 4, framing['B_bind'], framing['B_trans'])
        if len(header) != 32 or struct.unpack('<8sQQQ', header) != (
                b'J7F2C001', 4, framing['B_bind'], framing['B_trans']):
            raise AssertionError('fixed little-endian header')
        wire = len(header)+framing['B_bind']+framing['B_trans']
        rows, bits, ops = [], 0, 0
        for d in dims:
            tick('independent_endpoint_rows')
            n, q, r = d['N'], d['q'], d['N'] if full else 0
            packed = struct.pack('<QQQQ', len(rows), n, q, r)
            if len(packed) != 32 or struct.unpack('<QQQQ', packed) != (len(rows), n, q, r):
                raise AssertionError('comparison header round trip')
            sizes = [divmod(k, 8) for k in (r*n, r, q*r*r)]
            a, b, c = [whole+bool(remainder) for whole, remainder in sizes]
            wire += len(packed)+a+b+c
            bits += r*n+r+q*r*r
            ops += 16*(q+1)*(r+1)**2*(n+d['m0']+d['mL']+1)
            rows.append(dict(name=d['name'], r=r, B_bytes=a, c_bytes=b, T_bytes=c,
                initial_comparisons=n, transition_comparisons=q*r*n, final_comparisons=r))
        return dict(rows=rows, wire_bytes=wire, logical_coordinate_bits=bits,
                    algebraic_bit_operation_bound=ops)

    try:
        if p.CAPS != original.EXPECTED_CAPS or sys.gettrace() is not None:
            raise AssertionError('unchanged caps and initial tracer')
        snapshots = [Path(__file__), Path(original.__file__), Path(p.__file__),
                     HERE.parent/'parity-four-rule/checker.py']
        for path in snapshots:
            name = 'literal-checker.py' if path.name == 'checker.py' else path.name
            (OUT/name).write_bytes(path.read_bytes())
        receipts = {}
        for name in ('manifest.json', 'preflight.json', 'accounting-check.json',
                     'inventory-fields.json', 'helper-first-read.failure.json'):
            body = (HERE/'output-502'/name).read_bytes()
            receipts[name] = json.loads(body, object_pairs_hook=p.no_duplicates,
                                       parse_constant=p.reject_number)
            walk(receipts[name], metadata=True)
        manifest, old = receipts['manifest.json'], receipts['preflight.json']
        if not same(manifest['binding_paths'], original.BIND_PATHS):
            raise AssertionError('all eight binding paths and their order')
        original.OUT = OUT/'regenerated'
        original.Run = AuditRun
        code = original.main()
        if code != 0:
            raise AssertionError(('regeneration did not complete', code))
        fresh = json.loads((original.OUT/'preflight.json').read_bytes(),
                           object_pairs_hook=p.no_duplicates)
        checked_fields = ('caps', 'raw_binding_manifest', 'binding_bytes', 'transport_bytes',
            'dimensions', 'known_dimensions', 'graphs', 'sections', 'framing',
            'zero_rank_size_baseline', 'full_rank_size_endpoint', 'scratch_rows_bytes',
            'buffer_peak_bytes', 'completed_checks')
        for field in checked_fields:
            if not same(old[field], fresh[field]):
                raise AssertionError(('complete regenerated receipt field', field))
        if [c['section'] for c in counts] != ['B_bind', 'B_trans']:
            raise AssertionError('both independent payload counts completed')
        dims, frames = fresh['dimensions'], fresh['framing']
        if len(dims) != 4 or [d['name'] for d in dims] != ['Dfree','Dzero','Daxiom','Dcomm']:
            raise AssertionError('exact four ordered comparisons')
        endpoints = dict(zero=endpoint(dims, frames, False), full=endpoint(dims, frames, True))
        if not same(endpoints['zero'], fresh['zero_rank_size_baseline']) or not same(
                endpoints['full'], fresh['full_rank_size_endpoint']):
            raise AssertionError('all endpoint fields, no zip truncation')
        scratch = sum(divmod(max(d['N'] for d in dims), 8)[0]+
                      bool(divmod(max(d['N'] for d in dims), 8)[1]) for _ in range(4))
        if scratch != fresh['scratch_rows_bytes']:
            raise AssertionError('four separately rounded scratch rows')
        report.update(status='PASS', counts=counts, compared_receipt_fields=list(checked_fields),
            endpoints=endpoints, scratch_bytes=scratch,
            raw_binding_bytes=sum(row['bytes'] for row in fresh['raw_binding_manifest']),
            original_primary_visits=old['item_visits'], fresh_primary_visits=active.visits,
            runtime=sys.version, transport_bytes_independently_counted=True,
            constructor_correspondence='REUSED, NOT INDEPENDENTLY AUDITED',
            full_rank_fits=False, actual_ranks='UNKNOWN', equalities='UNKNOWN')
    except Exception as exc:
        report.update(status='FAIL', failures=[dict(kind=type(exc).__name__, message=str(exc),
            trace=traceback.format_exc())], partial_counts=counts)
    finally:
        sys.settrace(None)
    report.update(auxiliary_item_units=auxiliary, auxiliary_ledger=dict(budget),
        combined_selected_item_units=auxiliary+(active.visits if active else 0),
        required_item_units=LIMIT, elapsed_seconds=time.monotonic()-started+failed_report['elapsed_seconds'],
        required_seconds=SECONDS, reserve_bytes=RESERVE, required_evidence_bytes=200_000_000,
        limitations='Primary observer omissions remain; JSON/internal/C/read/hash/bit/index work and full live peaks are not bounded. No complete administrative or transport-schema pass. No payload or coordinate arrays saved.')
    path = OUT/'wire-audit.json'
    used = sum(f.stat().st_size for root in (FAILED, OUT) for f in root.rglob('*') if f.is_file())
    report['preserved_failure'] = str((FAILED/'wire-audit.json').relative_to(HERE))
    report['saved_before_receipt'] = used
    raw = json.dumps(report, ensure_ascii=True, separators=(',', ':')).encode()
    if used+len(raw) > RESERVE:
        raise RuntimeError('receipt reserve exhausted; existing evidence preserved')
    path.write_bytes(raw)
    print(json.dumps(dict(status=report['status'], counts=counts,
        selected_item_units=report['combined_selected_item_units'], required_item_units=LIMIT,
        saved_bytes=used+len(raw), required_reserve_bytes=RESERVE,
        elapsed_seconds=report['elapsed_seconds'], failures=report['failures'], path=str(path))))
    return 0 if report['status'] == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
