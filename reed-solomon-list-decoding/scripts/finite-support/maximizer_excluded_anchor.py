"""Fixed L074 excluded-anchor test; exact complete source and subset actions.

No optimizer, changed coefficient, included-anchor subtraction, or new source
algebra. Full rational certificates, including all principal minors, go to disk.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'maximizer-excluded-anchor-results.json'
LAYERS = [5, 6, 7]


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def enc(x):
    if isinstance(x, F):
        return [x.numerator, x.denominator]
    if isinstance(x, dict):
        return {str(k): enc(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [enc(v) for v in x]
    return x


@lru_cache(None)
def beta(n, l, m, a, t):
    return sum((-1)**(u-t)*c(u, t)*c(n-2*a, u-a)
               *c(n-a-u, l-u)*c(n-a-u, m-u)
               for u in range(max(a, t), min(l, m, n-a)+1))


def det(M):
    return sum((-1)**j*M[0][j]*det([r[:j]+r[j+1:] for r in M[1:]])
               for j in range(len(M))) if M else F(1)


def dot(x, y):
    assert len(x) == len(y)
    return sum((a*b for a, b in zip(x, y)), F(0))


def main():
    names = ['maximizer-seven-seven-scalars-results.json',
             'maximizer-completion-results.json', 'maximizer-completion-verification.json',
             'delsarte-lp-results.json', 'alternative-product-zero-plane-results.json',
             'seven-distance-full-base-kernel-results.json',
             'simultaneous-shell-ordinary-scalars-results.json',
             'seven-shell-affine-fixed-dual-results.json',
             'complemented-five-six-shell-results.json']
    paths = [ROOT/name for name in names]
    scalar, included, verified, lp, point, col, old, square, smaller = [
        json.loads(path.read_text()) for path in paths]
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    for name, data in zip(names, [scalar, included, verified, lp, point, col, old, square, smaller]):
        check('clean_input_'+name, not data['failures'])
        for path, digest in data.get('input_hashes', data.get('source_hashes', {})).items():
            check('input_hash_'+name+'_'+path,
                  hashlib.sha256((NB/path).read_bytes()).hexdigest() == digest)

    # Reconstruct the original pairs, column parameters and completed vector.
    primal = [F(v['numerator'], v['denominator']) for v in lp['exact']['primal']]
    check('complete_original_pair_domain', len(primal) == 64 and lp['active_distances'] == list(range(5, 69)))
    for j in range(1, 65):
        coeff = [0]*69
        for s in range(69-j):
            for t in range(min(j, 68-s)+1):
                coeff[s+t] += c(68-j, s)*c(956-j, s)*(-1)**t*c(j, t)
        check('pair_system_'+str(j), 1+sum(F(coeff[h], c(68, h)*c(956, h))*a
              for h, a in zip(range(5, 69), primal)) == 0)
    p = [F(1)]+[F(0)]*4+[x/(2*c(68, h)*c(956, h)) for h, x in zip(range(5, 69), primal)]
    rho = (F(c(1024, 64), c(68, 64))+1)/(2*c(1024, 68))
    check('same_pairs_rho', enc(p[:15]) == scalar['pairs_through_14']
          and enc(p[:14]) == included['pairs'] and enc(rho) == scalar['rho'] == included['rho'] and rho > 0)
    objective = [[F(*x) for x in row] for row in square['objective_matrix']]
    plane = [[F(*x) for x in row] for row in point['plane_matrix']]
    w, v = objective[0][3]/(-objective[3][3]), plane[0][2]/(-plane[2][2])
    parameters = [F(0), v, w]
    check('unchanged_maximizer', enc(parameters) == scalar['parameters'] == included['parameters'])
    f = [F(0)]*49
    f[33], f[42] = v, w
    pivots = col['equation_pivots']
    check('original_nonpivots', [j for j in range(49) if j not in pivots] == [27, 33, 42])
    for i, j in enumerate(pivots):
        row = [F(*x) for x in col['equation_rref'][i]]
        f[j] = row[-1]-sum(row[k]*f[k] for k in [27, 33, 42])
    check('unchanged_full_column', enc(f) == scalar['original_RREF_column'] == included['free_column'])
    for i, (row, rhs) in enumerate(zip(col['equations'], col['rhs'])):
        check('column_equation_'+str(i), dot([F(*x) for x in row], f) == F(*rhs))
    reconstructed = {tuple(row['type']): F(*row['y']) for row in old['types']}
    for row in col['column']:
        if row['orbit'] != [0, 0, 0]:
            l, i, j = row['orbit']
            reconstructed[l, 7, i, j] = p[7]*f[row['variable']] if row['kind'] == 'free' else F(*row['value'])
    A, rhs = [[F(*x) for x in row] for row in included['matrix']], [F(*x) for x in included['rhs']]
    defining_modes = [0,1,2,3,4,5,8,9,10,11,12,13,14,16,17,18,19,20,22,
                      24,25,26,27,28,29,32,33,34,35,40,41,42,48,49,56]
    check('original_defining_rows', included['certificate']['defining_rows'] ==
          [['mode', i] for i in defining_modes]+[['sign', 28]])
    mat = [A[i]+[rhs[i]] for i in defining_modes]+[[F(j == 28) for j in range(36)]+[F(0)]]
    for j in range(36):
        k = next(k for k in range(j, 36) if mat[k][j])
        mat[j], mat[k] = mat[k], mat[j]
        divisor = mat[j][j]
        mat[j] = [x/divisor for x in mat[j]]
        for k in range(36):
            if k != j:
                multiplier = mat[k][j]
                mat[k] = [x-multiplier*y for x, y in zip(mat[k], mat[j])]
    z = [row[-1] for row in mat]
    check('unchanged_all_36_coordinates', enc(z) == scalar['same_original_basis_z']
          == included['certificate']['z'] == verified['fresh_original_basis_solution'])
    free = [(r, q) for r, q in it.product(range(8), repeat=2) if r+q >= 7]
    for r, q in it.product(range(8), repeat=2):
        h = r+q
        y = (p[7] if h == 0 else F(0) if h <= 4 else reconstructed[h, 7, q, r]) if h <= 6 else (
            p[7]*z[free.index((r, q))]/(c(7, r)*c(61, r)*c(7, q)*c(949, q)))
        reconstructed[7, 7, 7-r, 7-q] = y
    expected = {(l, m, i, j) for l, m in [(5,5),(5,6),(6,6),(5,7),(6,7),(7,7)]
                for i, j in it.product(range(l+1), repeat=2)}
    check('complete_270_types', set(reconstructed) == expected)

    # Independent actual-support presentations of every affine coefficient.
    entries, dictionary, moments, keys = [], {}, {}, {}
    for saved in scalar['all_records']:
        l, m, i, j = typ = tuple(saved['type'])
        y = F(*saved['y'])
        check('same_reconstructed_entry_'+str(typ), reconstructed[typ] == y)
        D = set(range(68))
        U, V = set(range(m)), set(range(68, 68+m))
        X = set(range(i)) | set(range(m, m+l-i))
        Y = set(range(68, 68+j)) | set(range(68+m, 68+m+l-j))
        supports = [D, (D-X)|Y, (D-U)|V]
        orders, presentations = [], []
        for k, order in enumerate(it.permutations(range(3))):
            AA, BB, CC = [supports[t] for t in order]
            atoms = [0]*8
            for x in range(1024):
                atoms[4*(x in AA)+2*(x in BB)+(x in CC)] += 1
            a, b, h, t, s = len(AA-BB), len(AA-CC), len(BB-CC), len(AA-(BB|CC)), len((BB&CC)-AA)
            record = saved['presentations'][k]
            check('actual_presentation_'+str((typ, k)), record['atoms'] == atoms
                  and record['source_indices'] == [a,b,t,s] and a+b-t-s == h
                  and all(len(S) == 68 for S in supports))
            value = p[h]-y
            check('Boolean_forbidden_affine_'+str((typ, k)), value >= 0
                  and (0 not in [a,b,h] or y == p[max(a,b,h)])
                  and (not any(1 <= d <= 4 for d in [a,b,h]) or y == 0))
            presentations.append({'order': order, 'atoms': atoms, 'source_indices': [a,b,t,s],
                                  'h': h, 'pair': p[h], 'y': y, 'affine': value})
            orders.append(tuple(atoms))
        key = min(orders)
        check('unordered_full_key_'+str(typ), key not in keys or keys[key] == y)
        keys[key] = y
        for ll, mm in [(l,m),(m,l)]:
            moments[ll,mm,i,j], dictionary[ll,mm,i,j] = y, p[l+m-i-j]-y
        entries.append({'type': typ, 'y': y, 'affine': p[l+m-i-j]-y, 'presentations': presentations})
    check('both_complete_rectangles', set(dictionary) == {(l,m,i,j) for l,m in it.product(LAYERS,repeat=2)
          for i,j in it.product(range(min(l,m)+1),repeat=2)} and len(entries) == 270)
    anchor_cases = []
    for l,m in [(0,0),(0,5),(5,0),(0,6),(6,0),(0,7),(7,0)]:
        y, h = p[max(l,m)], l+m
        value = p[h]-y
        check('zero_anchor_'+str((l,m)), value == 0)
        anchor_cases.append({'layers': [l,m], 'pair': p[h], 'y': y, 'affine': value})
    for l in LAYERS:
        check('Boolean_diagonal_'+str(l), dictionary[l,l,l,l] == 1-p[l])

    # Independently count every subset relation and its full weighted action.
    bases, norms, gamma, factors, transitions, ratios = {}, {}, {}, [], [], {}
    for n in [68,956]:
        for l in LAYERS:
            weights = [c(7,i)*c(n-7,l-i) for i in range(l+1)]
            vectors, ns = [], []
            for a in range(l+1):
                vec = [F(i**a) for i in range(l+1)]
                for oldvec, norm in zip(vectors,ns):
                    projection = sum(weight*x*y for weight,x,y in zip(weights,vec,oldvec))/norm
                    vec = [x-projection*y for x,y in zip(vec,oldvec)]
                vectors.append(vec)
                ns.append(sum(weight*x*x for weight,x in zip(weights,vec)))
                check('positive_norm_'+str((n,l,a)), ns[-1] > 0)
            bases[n,l], norms[n,l] = vectors,ns
            factors.append({'n':n,'layer':l,'weights':weights,'basis':vectors,'norms':ns})
        for l,m in it.product(LAYERS,repeat=2):
            for t in range(min(l,m)+1):
                Q = [[sum(c(i,x)*c(7-i,j-x)*c(l-i,t-x)*c(n-7-l+i,m-j-t+x) for x in range(8))
                      for j in range(m+1)] for i in range(l+1)]
                check('transition_count_'+str((n,l,m,t)), all(sum(row) == c(l,t)*c(n-l,m-t) for row in Q))
                acts = []
                for a in range(m+1):
                    action = [dot(row,bases[n,m][a]) for row in Q]
                    acts.append(action)
                    if a <= l:
                        scale = action[-1]/bases[n,l][a][-1]
                        check('full_subset_action_'+str((n,l,m,t,a)), action == [scale*x for x in bases[n,l][a]])
                        gamma[n,l,m,a,t] = scale
                        B = beta(n,l,m,a,t)
                        if B:
                            ratios.setdefault((n,l,m,a),[]).append(scale/B)
                        else:
                            check('zero_beta_action_'+str((n,l,m,t,a)), scale == 0)
                    else:
                        check('absent_mode_'+str((n,l,m,t,a)), not any(action))
                transitions.append({'n':n,'l':l,'m':m,'intersection':t,'matrix':Q,'actions':acts})
        for l,m in it.product(LAYERS,repeat=2):
            for a in range(min(l,m)+1):
                rr = ratios[n,l,m,a]
                check('signed_uniform_beta_ratio_'+str((n,l,m,a)), len(set(rr)) == 1 and rr[0] > 0)
        for a in range(6):
            sigma = lambda l,m: norms[n,l][a]*ratios[n,l,m,a][0]
            check('coherent_three_layer_sign_'+str((n,a)), sigma(5,6)*sigma(6,7) == sigma(5,7)*sigma(6,6))

    blocks, negative, all_minors, all_pivots = [], [], [], []
    dimensions = dict.fromkeys(LAYERS,0)
    for a,b in it.product(range(8),repeat=2):
        layers = [l for l in LAYERS if max(a,b) <= l]
        def source_entry(l,m,use_moments=False):
            lookup = moments if use_moments else dictionary
            return sum(beta(68,l,m,a,i)*beta(956,l,m,b,j)*lookup[l,m,i,j]
                       for i,j in it.product(range(min(l,m)+1),repeat=2))
        B = [[source_entry(l,m) for m in layers] for l in layers]
        acts = [[sum(gamma[68,l,m,a,i]*gamma[956,l,m,b,j]*dictionary[l,m,i,j]
                     for i,j in it.product(range(min(l,m)+1),repeat=2)) for m in layers] for l in layers]
        N = [norms[68,l][a]*norms[956,l][b] for l in layers]
        Dl = [c(68-2*a,l-a)*c(956-2*b,l-b) for l in layers]
        weighted = [[N[k]*x for x in row] for k,row in enumerate(acts)]
        check('source_and_weighted_symmetry_'+str((a,b)), B == list(map(list,zip(*B)))
              and weighted == list(map(list,zip(*weighted))) and min(Dl) > 0)
        for k,l in enumerate(layers):
            for h,m in enumerate(layers):
                scale = ratios[68,l,m,a][0]*ratios[956,l,m,b][0]
                check('entire_signed_action_'+str((a,b,l,m)), acts[k][h] == scale*B[k][h]
                      and (l != m or scale == F(1,Dl[k])))
                check('congruent_pair_scale_'+str((a,b,l,m)),
                      scale*ratios[68,m,l,a][0]*ratios[956,m,l,b][0] == F(1,Dl[k]*Dl[h]))
                oldY = F(*verified['mode_evidence'][8*a+b]['full_block'][k][h])
                correction = p[l]*p[m]*c(68,l)*c(956,l)*c(68,m)*c(956,m) if a == b == 0 else 0
                check('unchanged_included_overlap_'+str((a,b,l,m)), source_entry(l,m,True) == oldY+correction)
        if max(a,b) <= 6:
            small = smaller['complete_blocks'][7*a+b]
            count = len(small['layers'])
            check('L063_complete_principal_overlap_'+str((a,b)), enc([row[:count] for row in B[:count]]) == small['matrix'])
        minors = []
        for size in range(1,len(layers)+1):
            for ind in it.combinations(range(len(layers)),size):
                value = det([[B[i][j] for j in ind] for i in ind])
                actual = det([[weighted[i][j] for j in ind] for i in ind])
                multiplier = F(1)
                for i in ind:
                    multiplier *= N[i]/Dl[i]
                check('coherent_full_minor_'+str((a,b,ind)), actual == value*multiplier)
                minors.append({'indices':ind,'value':value,'weighted_value':actual,'positive_scale':multiplier})
                all_minors.append(value)
        psd = all(row['value'] >= 0 for row in minors)
        if not psd:
            negative.append([a,b])
        # Sequential pivots when all preceding principal determinants are positive.
        piv, preceding = [], F(1)
        for count in range(1,len(layers)+1):
            leading = det([row[:count] for row in B[:count]])
            if preceding <= 0:
                break
            piv.append(leading/preceding/Dl[count-1])
            preceding = leading
        all_pivots.extend(piv)
        mult = (c(68,a)-c(68,a-1))*(c(956,b)-c(956,b-1))
        check('positive_multiplicity_'+str((a,b)), mult > 0)
        for l in layers:
            dimensions[l] += mult
        blocks.append({'mode':[a,b],'layers':layers,'multiplicity':mult,'source_block':B,
                       'actions':acts,'norms':N,'D':Dl,'weighted_block':weighted,
                       'all_principal_minors':minors,'normalized_pivots':piv,'PSD':psd})
    check('full_source_dimensions', all(dimensions[l] == c(68,l)*c(956,l) for l in LAYERS))
    summary = {'verdict':'RECONSTRUCTION_FAILURE' if failures else 'NEGATIVE_MODE' if negative else 'PSD',
               'checks':len(checks),'failures':len(failures),'types':len(entries),'presentations':6*len(entries),
               'zero_anchor_cases':len(anchor_cases),'source_blocks':len(blocks),'required_source_blocks':64,
               'PSD_blocks':sum(row['PSD'] for row in blocks),'principal_minors':len(all_minors),
               'positive_minors':sum(x>0 for x in all_minors),'zero_minors':sum(x==0 for x in all_minors),
               'normalized_pivots':len(all_pivots),'minimum_normalized_pivot':min(all_pivots),
               'required_minimum_pivot':0,'negative_modes':negative,'dimensions':dimensions}
    out = {'summary':summary,'checks':checks,'failures':failures,
           'input_hashes':{str(path.relative_to(NB)):hashlib.sha256(path.read_bytes()).hexdigest() for path in paths},
           'rho':rho,'pairs_through_14':p[:15],'parameters':parameters,'original_column':f,'completion_z':z,
           'entries':entries,'zero_anchor_cases':anchor_cases,'factor_bases':factors,
           'complete_subset_transitions':transitions,'signed_beta_ratios':ratios,'blocks':blocks}
    OUT.write_text(json.dumps(enc(out),indent=2)+'\n')
    print(json.dumps(enc(summary),sort_keys=True))
    print('Full rational certificate and failures: '+str(OUT.relative_to(NB)))
    if failures:
        print('Failure names: '+str(failures))
        raise SystemExit(1)


if __name__ == '__main__':
    main()
