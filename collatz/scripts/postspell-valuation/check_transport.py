"""One guarded witness for the approved shifted-valuation transport test."""

import json
from pathlib import Path
import runpy

HERE = Path(__file__).resolve().parent
helpers = runpy.run_path(str(HERE.parent / 'growing-postspell/check_chains.py'))
coding, word, crt, replay, parameters = (
    helpers[k] for k in ('coding', 'word', 'crt', 'replay', 'parameters'))


def v2(x):
    assert x > 0
    return (x & -x).bit_length() - 1


def main():
    chain = [[2, 3], [2, 3], [3, 3]]
    w = ''.join(word(*p) for p in chain)
    _, _, residue = coding(w + 'O')
    modulus = 1 << (len(w) + 1)
    root = crt(residue, modulus)
    states, ends, tails = replay(root, chain)
    assert all(x % 2 == 1 and x % 27 == 20 for x in [root] + ends)
    rows, offset = [], 0
    for i, (j, h) in enumerate(chain):
        n, y, z, m = states[offset], states[offset+4*j], tails[i], ends[i]
        u = (y+1) // (1 << h)
        A, C, D = parameters(j, h)
        assert 11*y+23 == 27**j*(11*n+23) // 16**j
        assert 16**j*(11*y+23) == 27**j*(11*n+23)
        assert y+1 == (1 << h)*u and u % 2 == 1
        assert z == 3**h*u-1 == 4*m and v2(z) == 2
        assert 4*(11*m+23) == 11*3**h*u+81
        assert (1 << D)*m == A*n+C
        assert v2(11*n+23) == 4*j+2 and v2(11*y+23) == 2
        rows.append(dict(J=j, H=h, n=n, y=y, u=u, z=z, m=m,
                         input_V=v2(11*n+23), after_B_V=v2(11*y+23),
                         output_V=v2(11*m+23), exact_tail_v2=v2(z)))
        offset += D
    assert rows[1]['input_V'] == 10 and rows[1]['output_V'] == 14
    result = dict(result='PASS', chain=chain, root=root,
                  parity_residue_with_endpoint_O=residue,
                  root_period=27*modulus, states=states, words=rows,
                  endpoints=ends, failed_checks=[],
                  required_bound='V(m)<=V(n) on an extendible middle word',
                  actual_bound='V(m)=14>10=V(n); after-B V=2',
                  limitations='One finite witness; arbitrary replenishment is proved in L024.')
    path = HERE / 'result.json'
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in
                      ('result', 'root', 'endpoints', 'required_bound',
                       'actual_bound', 'failed_checks')}, indent=2))
    print(f'certificate: {path}')


if __name__ == '__main__':
    main()
