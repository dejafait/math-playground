"""Step 480: audit original L153 certificates, without regenerating them.

No producer or replay imports. Integer minors and original null certificates
suffice; no RREF, higher-row compatibility, or nonlinear feasibility test.
"""
from hashlib import sha256
from itertools import combinations
from math import prod
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
OUT = HERE / 'l153-critical-audit'
MASTER = HERE / 'l153-critical-audit.json'
P = 97
H = [1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96]
S = [1,8,12,18,22,27,33]
J = [x for x in H if x not in S]
inputs = {}
context = {}
checks = 0


def encode(x):
    return json.dumps(x, separators=(',', ':')).encode()


def save(path, x):
    raw = encode(x) + b'\n'
    path.write_bytes(raw)
    return sha256(raw).hexdigest()


def read(path):
    raw = path.read_bytes()
    inputs[str(path.relative_to(HERE))] = sha256(raw).hexdigest()
    return json.loads(raw)


def require(label, actual, expected):
    global checks
    checks += 1
    if actual != expected:
        failure = dict(check=label, context=context.copy(), actual=actual,
                       required=expected)
        save(MASTER, dict(complete=False, checks=checks, failures=[failure],
                         input_sha256=inputs))
        print(f'FAIL: {label}; exact evidence: {MASTER}', flush=True)
        raise SystemExit(1)


def intdet(matrix):
    # Bareiss condensation over Z, with row swaps and checked exact divisions.
    # Each stage is the bordered-minor identity; the preceding pivot divides
    # every numerator. Final entry (with swap sign) is the integer determinant.
    a = [row[:] for row in matrix]
    previous, sign = 1, 1
    for k in range(len(a)-1):
        r = next((r for r in range(k, len(a)) if a[r][k] != 0), None)
        if r is None:
            return 0
        if r != k:
            a[k], a[r] = a[r], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, len(a)):
            old = a[i][k]
            for j in range(k+1, len(a)):
                numerator = pivot*a[i][j] - old*a[k][j]
                quotient, remainder = divmod(numerator, previous)
                if remainder:
                    require('integer condensation exact division',
                            dict(k=k,i=i,j=j,remainder=remainder), None)
                a[i][j] = quotient
            a[i][k] = 0
        previous = pivot
    return sign*a[-1][-1]


def run():
    global context
    OUT.mkdir(exist_ok=True)
    saved = read(HERE / 'all-disjoint-pair-census.json')
    replay = read(HERE / 'all-disjoint-pair-census-replay.json')
    # Literal theorem labels, independently compared to all roots of X^16-1.
    require('H roots', H, [x for x in range(1,P) if pow(x,16,P)==1])
    require('prime modulus', [d for d in range(2,10) if P%d==0], [])
    universe = sorted((tuple(x for x in a if x in S), tuple(x for x in a if x in J))
                      for a in combinations(H,4) if len(set(a)&set(S))==2)
    require('support count', len(universe), 756)
    columns = list(combinations(S,2))
    for key, val in dict(modulus=P,H=H,S=S,J=J,universe=[[list(i),list(k)] for i,k in universe],
                         column_pairs=[list(c) for c in columns]).items():
        require(key, saved[key], val)
    supports = [set(i+k) for i,k in universe]
    expected = {(a,b) for a,b in combinations(range(756),2) if not supports[a]&supports[b]}
    require('complete pair count', len(expected), 79380)
    require('original block count', len(saved['blocks']), 756)
    require('replay block count', len(replay['blocks']), 756)
    require('replay master binding', replay['source_sha256'], inputs['all-disjoint-pair-census.json'])
    matrices, ratio_matrices, block_evidence = [], [], []
    for n,(i,k) in enumerate(universe):
        context = dict(block=n)
        roots = [y for y in J if y not in k]
        values = {x: prod(x-y for y in roots)%P for x in H}
        require('exact polynomial zeros', [x for x in H if values[x]==0], roots)
        obs = [x for x in S if x not in i]
        z = obs[0]
        c = [[(values[z]*(t==x)-values[x]*(t==z))%P for t in S] for x in obs[1:]]
        matrix = [[(u[a]*v[b]-u[b]*v[a])%P for a,b in combinations(range(7),2)]
                  for u,v in combinations(c,2)]
        require('all original block fields', saved['blocks'][n],
                dict(I=list(i),K=list(k),pivot=z,covectors=c,matrix=matrix))
        scales = [values[z]**2*values[x]*values[y]%P for x,y in combinations(obs[1:],2)]
        require('all row scales nonzero', all(scales), True)
        ratios = [[entry*pow(scale,-1,P)%P for entry in row] for row,scale in zip(matrix,scales)]
        rb = replay['blocks'][n]
        require('replay original index', rb['index'], n)
        require('replay pivot', rb['pivot'], z)
        require('replay scales', rb['scales'], scales)
        require('replay g values', rb['values'], {str(x):v for x,v in values.items()})
        coeff = rb['polynomial']
        require('replay monic degree seven', [len(coeff),coeff[-1]], [8,1])
        require('replay polynomial all evaluations',
                {x:sum(v*pow(x,d,P) for d,v in enumerate(coeff))%P for x in H},values)
        require('replay all ratio entries', rb['ratio_matrix'], ratios)
        matrices.append(matrix)
        ratio_matrices.append(ratios)
        block_evidence.append(dict(index=n,g_values={str(x):v for x,v in values.items()},
                                   pivot=z,covectors=c,original_matrix=matrix,scales=scales))
    require('original batch count', len(saved['batches']), 105)
    require('replay batch count', len(replay['batches']), 105)
    seen, groups, reports, binding_records = set(), set(), [], {}
    vectors = residual_entries = 0
    for bn, batch in enumerate(saved['batches']):
        context = dict(batch=bn)
        data = read(HERE / batch['path'])
        require('original batch binding', inputs[batch['path']], batch['sha256'])
        rb = replay['batches'][bn]
        rd = read(HERE / rb['path'])
        require('replay batch binding', inputs[rb['path']], rb['sha256'])
        require('batch sizes', [len(data['records']),batch['count'],len(rd['records']),rb['count']], [756]*4)
        require('batch grouping', data['overlap_pairs'], batch['overlap_pairs'])
        group = tuple(tuple(i) for i in data['overlap_pairs'])
        require('unique group', group in groups, False)
        groups.add(group)
        evidence = []
        for record, rr in zip(data['records'],rd['records']):
            a,b = record['pair']
            context = dict(batch=bn,pair=[a,b])
            require('required unordered pair', (a,b) in expected, True)
            require('unique pair', (a,b) in seen, False)
            seen.add((a,b))
            require('record grouping', (universe[a][0],universe[b][0]),group)
            require('claimed rank',record['rank'],12)
            rows,cols,basis = record['minor_rows'],record['pivot_columns'],record['kernel_basis']
            require('all original rows exactly once',sorted(rows),list(range(12)))
            require('twelve unique sorted pivot columns',len(cols)==12 and cols==sorted(set(cols)) and all(type(c) is int and 0<=c<21 for c in cols),True)
            require('nine full canonical null vectors',len(basis)==9 and all(len(v)==21 and all(type(x) is int and 0<=x<P for x in v) for v in basis),True)
            free = [c for c in range(21) if c not in cols]
            identity = [[int(i==j) for j in range(9)] for i in range(9)]
            require('identity on free coordinates',[[v[c] for c in free] for v in basis],identity)
            matrix = matrices[a]+matrices[b]
            minor = [[matrix[r][c] for c in cols] for r in rows]
            determinant = intdet(minor)
            residue = determinant%P
            require('nonzero original integer minor mod 97',residue!=0,True)
            require('saved original minor',record['minor_residue'],residue)
            # Every coordinate of every original and ratio residual, no sampling.
            residuals = [[sum(row[c]*v[c] for c in range(21))%P for row in matrix] for v in basis]
            rres = [[sum(row[c]*v[c] for c in range(21))%P for row in ratio_matrices[a]+ratio_matrices[b]] for v in basis]
            require('saved full original residuals',record['kernel_residuals'],residuals)
            require('all original residual entries',residuals,[[0]*12 for _ in range(9)])
            require('all ratio residual entries',rres,[[0]*12 for _ in range(9)])
            require('entire saved replay record',rr,dict(pair=[a,b],rank=12,pivot_columns=cols,
                independent_minor_residue=residue,rebuilt_basis_sha256=sha256(encode(basis)).hexdigest(),
                original_residual_entries=108,ratio_residual_entries=108,all_residuals_zero=True))
            evidence.append(dict(pair=[a,b],integer_minor_determinant=determinant,minor_residue=residue,
                                 free_columns=free,identity_on_free_coordinates=True,
                                 original_residuals=residuals,ratio_residuals=rres))
            vectors += 9
            residual_entries += 108
            if (a,b) in [(0,411),(0,412)]:
                binding_records[(a,b)] = record
        require('original batch ranks', batch['rank_histogram'], {'12':756})
        path = OUT / f'batch-{bn:03d}.json'
        digest = save(path,dict(original_path=batch['path'],records=evidence))
        reports.append(dict(path=str(path.relative_to(HERE)),sha256=digest,count=len(evidence)))
        save(MASTER,dict(complete=False,completed_batches=bn+1,checks=checks,failures=[],batches=reports,input_sha256=inputs))
        if (bn+1)%15==0:
            print(f'Audit: {bn+1}/105 batches; {len(seen)}/79380 pairs; failures 0',flush=True)
    context = dict(stage='coverage and historical bindings')
    require('exact complete pair set',sorted(seen),sorted(expected))
    require('basis vector total',vectors,714420)
    require('original residual total',residual_entries,8573040)
    expected_summary=dict(actual_pairs=79380,required_pairs=79380,universe_size=756,batches=105,
                          rank_histogram={'12':79380},complete_kernel_vectors=714420,
                          original_residual_entries=8573040,exclusion_rank_required=21,failures=[])
    require('whole original summary',saved['summary'],expected_summary)
    for key,value in expected_summary.items():
        require('replay summary '+key,replay['summary'][key],value)
    require('replay ordered count',replay['summary']['ordered_pairs'],158760)
    require('replay ratio residual count',replay['summary']['ratio_residual_entries'],8573040)
    old110=read(HERE/'fixed-three-row-extensions.json')
    old109=read(HERE/'zero-anchor-support-filter.json')
    old125=read(HERE/'new-pair-filter.json')
    require('exact prefix names',[b['name'] for b in saved['prefix_bindings']],['L110','L125'])
    for binding,name,pair in zip(saved['prefix_bindings'],['L110','L125'],[(0,411),(0,412)]):
        context=dict(prefix=name)
        literal=([[v['I'],v['K']] for v in old110['seed'][:2]] if name=='L110' else old125['first_two'])
        oldblocks=old109['blocks'][:2] if name=='L110' else [old125['blocks'][n] for n in old125['first_indices']]
        require('literal prefix',binding['keys'],literal)
        require('prefix indices',binding['pair'],list(pair))
        require('prefix exact ordered universe keys',[[list(i),list(k)] for i,k in (universe[n] for n in pair)],literal)
        require('original prefix whole record',binding['record'],binding_records[pair])
        stack=matrices[pair[0]]+matrices[pair[1]]
        require('prefix stack hash',binding['stack_sha256'],sha256(encode(stack)).hexdigest())
        require('historical original blocks',[matrices[n] for n in pair],[b['matrix'] for b in oldblocks])
        rec=binding_records[pair]
        require('replay prefix record',replay['prefix_bindings'][name],dict(pair=list(pair),rank=12,
             pivot_columns=rec['pivot_columns'],basis_sha256=sha256(encode(rec['kernel_basis'])).hexdigest()))
    # Recheck all read originals unchanged; hashes supplement full content checks.
    for path,digest in inputs.items():
        require('input unchanged '+path,sha256((HERE/path).read_bytes()).hexdigest(),digest)
    out=dict(complete=True,summary=dict(actual_pairs=len(seen),required_pairs=79380,blocks=756,
             batches=len(reports),rank=12,nullity=9,complete_kernel_vectors=vectors,
             original_residual_entries=residual_entries,ratio_residual_entries=residual_entries,
             original_block_entries=756*6*21,integer_minors=len(seen),checks=checks,failures=[]),
             input_sha256=inputs,blocks=block_evidence,batches=reports,
             audit_source_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
    save(MASTER,out)
    print(json.dumps(out['summary'],sort_keys=True),flush=True)
    print(f'Complete evidence: {MASTER}; exclusion threshold remains 21, actual rank 12.',flush=True)


if __name__=='__main__':
    run()
