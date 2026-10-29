"""Reconcile step 514 source binding, complete saved counts and evidence bytes."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE/'output-514-repaired'
FAILED = HERE/'output-514'


def main():
    path = OUT/'receipt-check.json'
    if path.exists():
        raise RuntimeError('preserve prior reconciliation')
    units = 0

    def same(a, b):
        nonlocal units
        units += 1
        if type(a) is not type(b):
            return False
        if type(a) is dict:
            return a.keys() == b.keys() and all(same(a[k], b[k]) for k in a)
        if type(a) is list:
            return len(a) == len(b) and all(same(x, y) for x, y in zip(a, b))
        return a == b

    def load(p):
        return json.loads(p.read_bytes())  # administrative receipts only

    report = load(OUT/'wire-audit.json')
    old = load(HERE/'output-502/preflight.json')
    fresh = load(OUT/'regenerated/preflight.json')
    manifest = load(HERE/'output-502/manifest.json')
    failed = load(FAILED/'wire-audit.json')
    assert report['status'] == 'PASS' and report['failures'] == []
    assert failed['status'] == 'FAIL' and failed['combined_selected_item_units'] == 102
    for field in report['compared_receipt_fields']:
        assert same(old[field], fresh[field]), field
    assert hashlib.sha256((OUT/'preflight_job7_transport.py').read_bytes()).hexdigest() == manifest['script_sha256']
    assert (OUT/'preflight_job7_transport.py').read_bytes() == (HERE/'preflight_job7_transport.py').read_bytes()
    assert (OUT/'audit_job7_wire_encoding.py').read_bytes() == (HERE/'audit_job7_wire_encoding.py').read_bytes()
    assert report['auxiliary_item_units'] == sum(report['auxiliary_ledger'].values())
    assert report['combined_selected_item_units'] == report['fresh_primary_visits']+report['auxiliary_item_units']
    assert report['fresh_primary_visits'] == fresh['item_visits'] == old['item_visits']
    assert len(report['counts']) == 2
    for row, section, key in zip(report['counts'], ('B_bind', 'B_trans'), ('binding_bytes','transport_bytes')):
        assert row['section'] == section
        assert row['independent_bytes'] == row['original_bytes'] == fresh[key]
        assert row['complete_ASCII_characters_checked'] == row['independent_bytes']
    assert same(report['endpoints']['zero'], fresh['zero_rank_size_baseline'])
    assert same(report['endpoints']['full'], fresh['full_rank_size_endpoint'])
    assert report['scratch_bytes'] == fresh['scratch_rows_bytes'] == 53884
    primary = report['combined_selected_item_units']
    assert primary+units < 100_000_000
    (OUT/Path(__file__).name).write_bytes(Path(__file__).read_bytes())
    # Both authored programs AND their immutable output copies are charged.
    programs = [HERE/'audit_job7_wire_encoding.py', Path(__file__)]
    used = sum(f.stat().st_size for root in (FAILED, OUT) for f in root.rglob('*') if f.is_file())
    used += sum(f.stat().st_size for f in programs)
    result = dict(status='PASS', complete_compared_fields=report['compared_receipt_fields'],
        original_source_manifest_hash_matches=True, source_hash_is_not_mathematical_byte_equality=True,
        primary_selected_units_including_failed_load=primary,
        reconciliation_value_nodes=units, combined_selected_units=primary+units,
        required_selected_units=100_000_000,
        encoder_ASCII_character_scans_separate=sum(r['complete_ASCII_characters_checked'] for r in report['counts']),
        max_encoder_fragment_characters=max(r['max_encoder_fragment_characters'] for r in report['counts']),
        saved_bytes_including_programs_snapshots_failure_and_this_receipt=0,
        required_receipt_reserve=1_000_000, proposed_baseline_plus_all_audit_evidence=0,
        required_evidence_bytes=200_000_000, full_transport_audit=False, total_work_bound=False,
        failures=[], limitations='Reuses graph constructors and library scalar escaping. Source interfaces/internal costs, strict schema reception, graph semantics, ranks/equalities and live-memory peaks remain unaccepted.')
    while True:
        raw = json.dumps(result, ensure_ascii=True, separators=(',', ':')).encode()
        total = used+len(raw)
        if total == result['saved_bytes_including_programs_snapshots_failure_and_this_receipt']:
            break
        result['saved_bytes_including_programs_snapshots_failure_and_this_receipt'] = total
        result['proposed_baseline_plus_all_audit_evidence'] = report['endpoints']['zero']['wire_bytes']+total
    assert total < 1_000_000 and result['proposed_baseline_plus_all_audit_evidence'] < 200_000_000
    with path.open('xb') as stream:
        stream.write(raw)
    print(json.dumps(dict(status='PASS', selected_units=primary+units, required_units=100_000_000,
        saved_bytes=total, required_reserve=1_000_000, failures=[], path=str(path))))


if __name__ == '__main__':
    main()
