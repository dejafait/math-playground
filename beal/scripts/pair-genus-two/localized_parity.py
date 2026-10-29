"""Approved 182+7 row test, with exact input and combination certificates."""
import json
from hashlib import sha256
from localized_parity_budget import ROOT, Budget

OUT = ROOT / 'localized-parity-certificate.json'
CLASS_HASH = 'c5363d1b846188e37fc53590b61de34923bb981da25ddd895cd82e14dda9b73b'
PARITY_HASH = 'fdb376f96717188690de8c849197d8b64834afdcdc56d789f427f2cf186c5501'
SELECTED = [1, 26, 27, 28, 29, 30, 31]
EXPECTED_COLUMNS = [
    [[1,0,0,5], [0,1,0,8], [0,0,1,9], [0,0,0,11]],
    [[1,0,0,1], [0,1,0,1], [0,0,1,1], [0,0,0,2]],
    [[1,0,0,1], [0,1,0,1], [0,0,1,2], [0,0,0,3]],
    [[1,1,0,0], [0,0,1,0], [0,0,0,1], [0,3,0,0]],
    [[1,0,0,1], [0,1,0,0], [0,0,1,2], [0,0,0,5]],
    [[1,0,0,1], [0,1,0,1], [0,0,1,4], [0,0,0,5]],
    [[1,0,0,4], [0,1,0,0], [0,0,1,3], [0,0,0,5]]]

def main():
    b = Budget()
    result = dict(completed=False, failures=[], elimination=[])
    try:
        payloads = [(ROOT / name).read_bytes() for name in
                    ['quartic-class-certificate.json', 'quartic-parity-certificate.json']]
        hashes = [sha256(raw).hexdigest() for raw in payloads]
        assert hashes == [CLASS_HASH, PARITY_HASH]
        base, data = [json.loads(raw) for raw in payloads]
        assert data['completed'] and not data['failures']
        assert base['completed'] and not base['failures']
        assert data['input_sha256'] == CLASS_HASH
        assert data['primes'] == base['generators'] and len(data['primes']) == 32
        primes = data['primes']
        assert [i for i, p in enumerate(primes) if 330 % p['p'] == 0] == SELECTED
        assert [primes[i]['p'] for i in SELECTED] == [11,2,3,3,5,5,5]
        assert [primes[i]['lattice']['columns'] for i in SELECTED] == EXPECTED_COLUMNS
        # Bind the complete exceptional-prime lists, not just their norms.
        assert [dict(p=e['p'], space_id=q['space_id'], lattice=q['lattice'])
                for e in base['exceptional'] for q in e['ideals']] == primes[26:]
        regular11 = next(e for e in base['regular'] if e['p'] == 11)
        result['regular11'] = regular11
        accepted = [e for e in data['elements'] if e['decision'] == 'accepted']
        assert [e['tuple_id'] for e in accepted] == data['accepted_ids']
        rows = []
        for e in accepted:
            v = e['valuations']
            assert len(v) == 32 and all(type(x) is int and x >= 0 for x in v)
            rows.append(sum((x % 2) << i for i, x in enumerate(v)))
        assert rows == data['parity_rows'] and len(rows) == 182
        rows += [1 << i for i in SELECTED]
        b.observe('input_rows', len(rows))
        assert len(rows) == 189 and all(type(x) is int and 0 <= x < 2**32 for x in rows)
        result.update(input_hashes=hashes, selected_indices=SELECTED,
                      selected_primes=[primes[i] for i in SELECTED],
                      accepted_ids=data['accepted_ids'], rows=rows,
                      accepted_valuations=[e['valuations'] for e in accepted])
        pivots = {}
        for i, row in enumerate(rows):
            current, witness, used = row, 1 << i, []
            b.observe('mask_bits', witness.bit_length())
            for col in sorted(pivots):
                if current & (1 << col):
                    pivot_row, pivot_witness, source_id = pivots[col]
                    current = b.xor(current, pivot_row)
                    witness = b.xor(witness, pivot_witness, witness=True)
                    used.append(source_id)
            pivot = (current & -current).bit_length() - 1 if current else None
            result['elimination'].append(dict(input=row, used_rows=used,
                output=current, combination=witness, pivot=pivot))
            if pivot is not None:
                pivots[pivot] = (current, witness, i)
            if i == 181:
                result['ordinary_rank'] = len(pivots)
        result.update(rank=len(pivots), required_rank=32,
                      localized_mod_two_upper_bound=32-len(pivots),
                      pivot_columns=sorted(pivots))
        # For each coordinate, certify membership or its precise nonzero residue.
        result['coordinate_reductions'] = []
        for j in range(32):
            current, witness = 1 << j, 0
            for col in sorted(pivots):
                if current & (1 << col):
                    row, combination, _ = pivots[col]
                    current = b.xor(current, row)
                    witness = b.xor(witness, combination, witness=True)
            result['coordinate_reductions'].append(dict(coordinate=j,
                residue=current, combination=witness))
        result['completed'] = True
    except Exception as exc:
        result['failures'].append(repr(exc))
        b.fail(exc)
        raise
    finally:
        b.save()
        result['budget'] = b.data
        OUT.write_text(json.dumps(result, separators=(',', ':')) + '\n')
        print(json.dumps(dict(completed=result['completed'], rank=result.get('rank'),
            required_rank=32, upper_bound=result.get('localized_mod_two_upper_bound'),
            failures=result['failures'], bounds=b.data, certificate=str(OUT))))

if __name__ == '__main__':
    main()
