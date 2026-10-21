"""Recompute step-236 source-only majorants without using generated proof sizes.

Actual stream/manifest sizes are compared only after the bounds are fixed.
Complete primitive verification is performed by initial_output.py, not here.
"""
import json
from pathlib import Path
import initial_verify as iv

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DEST = HERE / 'output' / 'source-ledger-236.json'


def main():
    assert not DEST.exists(), 'preserve prior evidence'
    original = json.loads((HERE/'output'/'certificate-236.json').read_text())
    assert original['complete'] and original['failures'] == []
    cert = dict(complete=False, failures=[], cases=[],
                premise='Complete primitive/image checks in certificate-236.json; this is accounting only.')

    def save():
        DEST.write_text(json.dumps(cert, indent=2)+'\n')

    save()
    try:
        J = 761+872+1
        assert original['constants'] == dict(lines=dict(unitR=761, symm=872),
            formats={'native': dict(D=16, S=584), 'not-or': dict(D=22, S=788)})
        for case in original['cases']:
            assert case['complete']
            raw = (ROOT/case['input']).read_bytes()
            envelope = json.loads(raw)
            checked = iv.receive(envelope)
            source = envelope['source']
            # No generated formula, suffix size, proof size or certificate bound
            # enters these quantities, only the original source tree/dictionary.
            U, d, n = checked['U'], checked['depth'], len(source['letters'])
            B = max([1, len(source['q'])]+[len(x) for x in source['letters']])
            Q0 = 2+len((json.dumps(source, separators=(',', ':'))+'\n').encode('ascii'))
            R = 1000*(B+4)*(n+2)*(U+2)**3*4**(2*d+3)
            H = d+1; Pstar = 48*4**(H+1)
            F = 256+64*(J+1).bit_length()
            required = {}
            for mode, S in (('native', 584), ('not-or', 788)):
                required[mode] = (J+2)*((B+4)*S*Pstar+F)
            metadata = 10000*(R+J+2)**2+(B+4)*(584+788)*Pstar
            total = R+metadata+sum(required.values())
            assert len(raw) <= R
            for mode in required:
                assert required[mode] == case['required']['formats'][mode]['bytes']
                assert case['checks']['measurements'][mode]['bytes'] <= required[mode]
            assert case['metadata_actual_bytes'] <= metadata
            assert case['total_actual_bytes'] <= total
            cert['cases'].append(dict(name=case['name'], source_bytes=Q0,
                U=U, d=d, n=n, B=B, envelope_actual_bytes=len(raw), envelope_required_bytes=R,
                proof_required_bytes=required, metadata_required_bytes=metadata,
                total_actual_bytes=case['total_actual_bytes'], total_required_bytes=total,
                total_required_bits=8*total, accepted=True))
            save()
            print(case['name'], 'source-only PASS', case['total_actual_bytes'], '/', total,
                  'bytes; envelope', len(raw), '/', R, flush=True)
        cert['complete'] = True; save()
        print('PASS', len(cert['cases']), 'source ledgers; failures', cert['failures'],
              '; certificate', DEST.relative_to(ROOT), flush=True)
    except BaseException as error:
        cert['failures'].append(type(error).__name__+': '+str(error)); save()
        raise


if __name__ == '__main__':
    main()
