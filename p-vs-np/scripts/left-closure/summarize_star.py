"""Record the partial step-205 boundary; writer sidecars are not verification.

The original driver checked the three local proofs but saved only their paths
and log results. Recheck those complete small inputs to retain full machine
evidence. Do not replay, rebuild or certify either large coordinate archive.
"""
import json
import run_star as s


def main():
    source = s.OUT / 'certificate-205-star.json'
    cert = json.loads(source.read_text())
    case = cert['cases'][0]
    assert not cert['complete'] and not case['exports']
    assert cert['failures'] == ['KeyboardInterrupt: ']
    data = json.loads((s.ROOT / case['request']).read_text())
    tables = s.ep.request(data)
    result = dict(step=205, source=str(source.relative_to(s.ROOT)),
                  outcome='EXPLORATION', complete=False,
                  boundary='Stopped during full coordinate-0 archive replay',
                  failures=cert['failures'], verified_exports=[],
                  local_proofs=[], uniform_ledger=case['uniform_ledger'],
                  finite_tables={key: tables[key] for key in ('K', 'beta', 'G')},
                  unverified_writers={},
                  pending=['all star export replay', 'per-record depth/node checks',
                           'writer/replay hash equality', 'relocated input retention',
                           'earlier/final exported roots', 'aggregate/argument checks',
                           'coordinates 1/2 construction and exports', 'all-size audit'])
    for v, path in enumerate(case['inputs']):
        checked = s.h.c.check(s.ROOT / path, s.ep.e.c.serialize(tables['local'][v]))
        result['local_proofs'].append(dict(coordinate=v, path=path, check=checked))
        print('local', v, 'complete primitive/endpoint PASS;',
              checked['lines'], 'records;', path, flush=True)
    for mode in ('native', 'not-or'):
        archive = s.OUT / ('star-205-coordinate-0.' + mode + '.jsonl.gz')
        sidecar = archive.with_name(archive.name + '.writer.json')
        writer = json.loads(sidecar.read_text())
        bound = result['uniform_ledger']['formats'][mode]
        result['unverified_writers'][mode] = dict(
            archive=str(archive.relative_to(s.ROOT)),
            sidecar=str(sidecar.relative_to(s.ROOT)), writer=writer,
            required_lines=bound['lines'], required_bytes=bound['bytes'],
            replay_verified=False)
        print('UNVERIFIED', mode, 'writer lines actual/required',
              writer['lines'], '/', bound['lines'], 'bytes actual/required',
              writer['bytes'], '/', bound['bytes'], flush=True)
    destination = s.OUT / 'certificate-205-summary.json'
    assert not destination.exists(), 'preserve existing summary'
    destination.write_text(json.dumps(result, indent=2) + '\n')
    print('EXPLORATION; verified_exports=[]; failures=', result['failures'],
          ';', destination.relative_to(s.ROOT), flush=True)


if __name__ == '__main__':
    main()
