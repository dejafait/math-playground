"""Critical-audit checks supplementing the reviewed independent full replay.

No producer imports. Preserve original certificates and replay. Explicit
two-way product-lattice coordinates and printed-kernel checks are saved.
"""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
import json
import re
import traceback
import replay_marked_octic_support_primes as replay

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUTPUT = HERE / 'marked-octic-support-primes-audit-certificate.json'
REPLAY = HERE / 'marked-octic-support-primes-audit-replay.json'
old = replay.old
E = old.equal


def main():
    report = dict(completed=False, failures=[], checks=[], kernels=[],
                  products=[], discovery=[], hashes={})
    try:
        replay.OUTPUT = REPLAY
        replay.main()
        rr = json.loads(REPLAY.read_text())
        report['replay_checks'] = len(rr['checks'])
        assert rr['completed'] and not rr['failures']
        assert all(x['passed'] and x['actual'] == x['required'] for x in rr['checks'])
        old.CHECKS.clear()
        report['checks'] = old.CHECKS
        c = old.decode(json.loads(replay.SOURCE.read_text()))
        for path in [replay.SOURCE, HERE/c['source'], REPLAY,
                     HERE/'marked-octic-support-primes-presentation.json',
                     Path(replay.__file__), Path(old.__file__)]:
            report['hashes'][path.name] = sha256(path.read_bytes()).hexdigest()
        E('original polynomial', old.POLY, [243, 0, -3564, 0, 6930, 0, -2860, 0, 275])
        l116 = (ROOT/'lemmas/L116-marked-octic-maximal-order.md').read_text()
        block = l116.split('```text\n', 1)[1].split('```', 1)[0]
        printed_basis = [[Q(x) for x in row.split()] for row in block.strip().splitlines()]
        E('complete printed L116 basis', c['basis'], printed_basis)
        E('printed b0 is one', [row[0] for row in c['basis']], [1]+[0]*7)
        l117 = (ROOT/'lemmas/L117-marked-octic-support-prime-decompositions.md').read_text()
        block = l117.split('```text\n', 1)[1].split('```', 1)[0]
        printed = {}
        label = None
        for line in block.splitlines():
            if line.startswith('P'):
                fields = line.split()
                label = fields[0]
                printed[label] = dict(e=int(fields[1]), f=int(fields[2]), rows=[])
            if label and '(' in line:
                printed[label]['rows'].append([int(x) for x in re.search(r'\(([^()]*)\)', line)[1].split(',')])
        presentation = old.decode(json.loads((HERE/'marked-octic-support-primes-presentation.json').read_text()))
        records = [r for d in c['decompositions'] for r in d['primes']]
        E('printed exact ordered labels', list(printed), [r['label'] for r in records])
        E('presentation source', presentation['source'], replay.SOURCE.name)
        E('complete presentation all six fields', presentation['primes'],
          [{key:r[key] for key in ['label', 'residue_degree', 'ramification_index',
                                  'residue_polynomial', 'quotient_map', 'ideal_basis']} for r in records])
        for d in c['decompositions']:
            p = d['prime']
            ranks = {2:2, 3:3, 5:4, 11:1}
            E(f'{p} reduced dimension', len(d['reduced_basis']), ranks[p])
            E(f'{p} exhaustive count', d['enumerated_elements'], p**ranks[p])
            report['discovery'].append(dict(prime=p, reduced_dimension=ranks[p],
                enumerated_elements=d['enumerated_elements'],
                idempotents=d['idempotents'], primitive=d['primitive_idempotents']))
            for r in d['primes']:
                name = r['label']
                f = r['residue_degree']
                E(name+' printed e f Q', printed[name],
                  dict(e=r['ramification_index'], f=f, rows=r['quotient_map']))
                required_g = [2,2,1] if name == 'P3_2' else [3,0,1] if name == 'P5_2' else [0,1]
                E(name+' printed residue polynomial', r['residue_polynomial'], required_g)
                pivots = [0,1] if name == 'P3_2' else [0,7] if name == 'P5_2' else [0]
                qm = r['quotient_map']
                E(name+' printed pivot identities', [[row[j] for j in pivots] for row in qm],
                  [[int(i == j) for j in range(f)] for i in range(f)])
                b = replay.identity()
                for j in range(8):
                    if j in pivots:
                        b[j][j] = p
                    else:
                        for a, k in enumerate(pivots):
                            b[k][j] = (-qm[a][j]) % p
                E(name+' all printed ideal columns', r['ideal_basis'], b)
                # Full inverse-image generators: normalized kernel lifts and pI.
                lifts = replay.transpose(r['quotient_kernel']['vectors'])
                gens = [row + replay.identity(p)[i] for i, row in enumerate(lifts)]
                coordinates = old.product(r['ideal_inverse'], gens)
                E(name+' entire inverse-image in ideal', old.integral(coordinates), True)
                E(name+' inverse-image reconstruction', old.product(b, coordinates), gens)
                E(name+' ideal in kernel', [[x % p for x in row] for row in old.product(qm,b)], [[0]*8 for _ in range(f)])
                # The discovery generator is genuinely in its reduced component.
                gen = r['generator']
                E(name+' generator in component', replay.modmul(r['idempotent'],gen,c['table'],p), gen)
                E(name+' generator in reduced algebra',
                  old.rank_by_columns(replay.transpose(d['reduced_basis']+[gen]),p)[0], ranks[p])
                report['kernels'].append(dict(label=name, pivots=pivots,
                    quotient_map=qm, ideal_basis=b, inverse_image_generators=gens,
                    inverse_image_in_ideal=coordinates))
            all_products = [(r['label']+f' power {j+1}', pr)
                            for r in d['powers'] for j,pr in enumerate(r['records'])]
            all_products += [(f'{p} assembled {j+1}', pr) for j,pr in enumerate(d['complete_product'])]
            for name, pr in all_products:
                gens = pr['generators']
                E(name+' full integer generators',
                  len(gens)==64 and all(len(row)==8 for row in gens) and old.integral(gens), True)
                E(name+' full integer terminal matrix',
                  len(pr['reduced_rows'])==64 and all(len(row)==8 for row in pr['reduced_rows']) and old.integral(pr['reduced_rows']), True)
                # Track the same invertible operations on the identity, making
                # explicit expressions of each terminal basis in all generators.
                transform = [[int(i==j) for j in range(64)] for i in range(64)]
                for op in pr['operations']:
                    if op[0]=='swap':
                        _,i,j=op
                        transform[i],transform[j]=transform[j],transform[i]
                    elif op[0]=='negate':
                        _,i=op
                        transform[i]=[-x for x in transform[i]]
                    elif op[0]=='add':
                        _,i,j,q=op
                        assert isinstance(q,int) and i!=j
                        transform[i]=[x+q*y for x,y in zip(transform[i],transform[j])]
                    else:
                        raise AssertionError(op)
                back = transform[:8]
                E(name+' terminal basis in generators', old.product(back, gens), replay.transpose(pr['basis']))
                forward = old.product(replay.inv(pr['basis']),replay.transpose(gens))
                E(name+' all generators in terminal basis', old.integral(forward), True)
                E(name+' generator reconstruction', old.product(pr['basis'],forward), replay.transpose(gens))
                # These reversible operations on I_64 specify the full exact
                # coefficient matrix; take its first eight rows. Keep this
                # straight-line representation rather than enormous decimal
                # coefficients. The expanded product back*gens was checked above.
                report['products'].append(dict(name=name,
                    basis_in_generators_program=dict(start='I_64',
                        operations=pr['operations'], select_rows=list(range(8))),
                    generators_in_basis=forward, operation_count=len(pr['operations'])))
        E('all eight kernels checked',len(report['kernels']),8)
        E('all 68 full lattice reductions checked',len(report['products']),68)
        report['completed']=True
    except Exception:
        report['failures'].append(traceback.format_exc())
        raise
    finally:
        OUTPUT.write_text(json.dumps(old.encode(report),indent=2)+'\n')
        print('audit_completed',report['completed'],'checks',len(report['checks']),
              'kernels',len(report['kernels']),'required',8,
              'products',len(report['products']),'required',68,
              'failures',len(report['failures']),'certificate',OUTPUT,flush=True)


if __name__ == '__main__':
    main()
