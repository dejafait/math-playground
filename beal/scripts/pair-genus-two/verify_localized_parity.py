"""Independent high-pivot rank and complete low-pivot certificate replay.

No producer mathematics is imported. Existing audited ideal arithmetic
is an input; this verifies all new finite linear algebra and its bindings.
"""
import json
from hashlib import sha256
from localized_parity_budget import ROOT, Budget

OUT = ROOT / 'localized-parity-verification.json'

def main():
    b = Budget()
    result = dict(completed=False, failures=[], checks=0)
    def check(ok, name):
        result['checks'] += 1
        if not ok:
            raise AssertionError(name)
    def combination(mask, rows):
        check(type(mask) is int and 0 <= mask < (1 << len(rows)), 'combination domain')
        value = 0
        for k, row in enumerate(rows):
            if mask & (1 << k):
                value = b.xor(value, row)
        return value
    try:
        names = ['quartic-class-certificate.json', 'quartic-parity-certificate.json',
                 'localized-parity-certificate.json']
        raw = [(ROOT / name).read_bytes() for name in names]
        hashes = [sha256(x).hexdigest() for x in raw]
        check(hashes[:2] == [
            'c5363d1b846188e37fc53590b61de34923bb981da25ddd895cd82e14dda9b73b',
            'fdb376f96717188690de8c849197d8b64834afdcdc56d789f427f2cf186c5501'],
            'accepted input hashes')
        base, parity, cert = [json.loads(x) for x in raw]
        check(all(d['completed'] and d['failures'] == [] for d in [base,parity,cert]),
              'all certificates completed')
        check(cert['input_hashes'] == hashes[:2], 'producer input binding')
        check(parity['input_sha256'] == hashes[0] and parity['primes'] == base['generators'],
              'entire ordered prime lattices')
        selected = [1,26,27,28,29,30,31]
        check(cert['selected_indices'] == selected, 'fixed coordinate indices')
        check(cert['selected_primes'] == [base['generators'][i] for i in selected],
              'full selected lattices and actions')
        # Full exceptional coverage is an audited input, here bind every record.
        exceptional = []
        for entry, p, number in zip(base['exceptional'], [2,3,5], [1,2,3]):
            check(entry['p'] == p and len(entry['ideals']) == number,
                  'complete exceptional lists')
            check([q['space_id'] for q in entry['ideals']] == entry['maximal_ideals'],
                  'all and only audited maximal ideals')
            for q in entry['ideals']:
                check(q['included'], 'exceptional ideal included')
                exceptional.append(dict(p=p, space_id=q['space_id'], lattice=q['lattice']))
        check(exceptional == base['generators'][26:], 'six exact exceptional prime lattices')
        regular = next(e for e in base['regular'] if e['p'] == 11)
        check(cert['regular11'] == regular, 'entire regular 11 input record')
        check(regular['factors'] == [[5,1]] * 4 and len(regular['ideals']) == 1,
              'one distinct prime over 11, not four')
        q = regular['ideals'][0]
        check(q['included'] and q['factor'] == [5,1]
              and dict(p=11,factor=q['factor'],lattice=q['lattice']) == base['generators'][1],
              'actual full 11 ideal')
        check([i for i,p in enumerate(base['generators']) if p['p'] in [2,3,5,11]] == selected,
              'exact selected support')
        accepted = [e for e in parity['elements'] if e['decision'] == 'accepted']
        check(len(accepted) == 182 and cert['accepted_ids'] == parity['accepted_ids']
              == [e['tuple_id'] for e in accepted], 'complete accepted order')
        rows = []
        for e, vector in zip(accepted, cert['accepted_valuations']):
            check(vector == e['valuations'] and len(vector) == 32, 'all original valuations')
            digits = []
            for v in vector:
                check(type(v) is int and v >= 0, 'exact nonnegative valuation')
                digits.append(str(v % 2))
            rows.append(int(''.join(reversed(digits)), 2))
        check(len(cert['accepted_valuations']) == 182, 'all valuation rows consumed')
        check(rows == parity['parity_rows'], 'independently converted parity matrix')
        rows += [2 ** i for i in selected]
        check(rows == cert['rows'] and len(rows) == 189, 'complete augmented matrix')
        b.observe('input_rows', len(rows))
        check(len(cert['elimination']) == len(rows), 'all operations present')
        reduced, pivots = [], {}
        for i, (row, operation) in enumerate(zip(rows, cert['elimination'])):
            current, witness, used = row, 2 ** i, []
            b.observe('mask_bits', witness.bit_length())
            for column in range(32):
                if column in pivots and (current // (2 ** column)) % 2:
                    k = pivots[column]
                    current = b.xor(current, reduced[k]['output'])
                    witness = b.xor(witness, reduced[k]['combination'], witness=True)
                    used.append(k)
            pivot = next((j for j in range(32) if (current // 2 ** j) % 2), None)
            check(operation == dict(input=row, used_rows=used, output=current,
                  combination=witness, pivot=pivot), 'every exact elimination operation')
            check(combination(witness, rows) == current, 'full input-combination identity')
            if pivot is not None:
                check(pivot not in pivots, 'distinct leading pivot')
                pivots[pivot] = i
            reduced.append(operation)
            if i == 181:
                check(len(pivots) == cert['ordinary_rank'] == 30, 'original rank 30')
        check(sorted(pivots) == cert['pivot_columns'] and len(pivots) == cert['rank'],
              'producer rank exact in both directions')
        independent = {}
        records = []
        for row in reversed(rows):
            current, used = row, []
            while current:
                pivot = current.bit_length() - 1
                if pivot not in independent:
                    independent[pivot] = current
                    break
                current = b.xor(current, independent[pivot])
                used.append(pivot)
            records.append(dict(input=row, used_columns=used, output=current))
        check(len(independent) == len(pivots) == 30, 'reverse highest-pivot rank')
        check(cert['required_rank'] == 32 and cert['localized_mod_two_upper_bound'] == 2,
              'threshold and upper bound')
        check([r['coordinate'] for r in cert['coordinate_reductions']] == list(range(32)),
              'complete coordinate reductions')
        witnesses = []
        for record in cert['coordinate_reductions']:
            check(combination(record['combination'], rows)
                  == (2 ** record['coordinate']) ^ record['residue'], 'coordinate identity')
            check(all(not (record['residue'] & (1 << j)) for j in pivots),
                  'coordinate residual has no pivot bits')
            if record['coordinate'] in selected:
                check(record['residue'] == 0 and record['combination'] < 2 ** 182,
                      'inverted coordinate already in ORIGINAL relation span')
                witnesses.append(dict(coordinate=record['coordinate'],
                    relation_indices=[i for i in range(182) if record['combination'] & 2 ** i]))
        result.update(completed=True, input_hashes=hashes, rank=30, required_rank=32,
            upper_bound=2, independent_elimination=records,
            independent_pivots=sorted(independent), selected_original_span_witnesses=witnesses)
    except Exception as exc:
        result['failures'].append(repr(exc))
        b.fail(exc)
        raise
    finally:
        b.save()
        result['budget'] = b.data
        OUT.write_text(json.dumps(result, separators=(',', ':')) + '\n')
        print(json.dumps(dict(completed=result['completed'], checks=result['checks'],
            rank=result.get('rank'), required_rank=32, upper_bound=result.get('upper_bound'),
            failures=result['failures'], bounds=b.data, verification=str(OUT))))

if __name__ == '__main__':
    main()
