"""Independent full set/predicate replay; no producer or math-helper imports."""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent


def digest(p):
    h = sha256()
    with p.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()


def run():
    result = dict(scope='Independent reconstruction and exact imported predicates only',
                  checks=[], thirds=[], residual_checks=[], failures=[], uncovered=[])

    def require(name, valid):
        result['checks'].append(dict(name=name,passes=bool(valid)))
        if not valid:
            raise AssertionError(name)

    cache = {}

    def read(name):
        if name not in cache:
            cache[name] = json.loads((BASE/name).read_bytes())
        return cache[name]

    def pointer(value, path):
        for part in path.split('/')[1:] if path else []:
            value = value[int(part)] if isinstance(value,list) else value[part]
        return value

    try:
        cert = read('new-pair-complete-assembly.json')
        require('complete successful producer', cert['failures'] == cert['uncovered'] == [] and
                all(c['passes'] for c in cert['checks']))
        require('producer bytes', cert['producer_sha256'] == digest(BASE/'new_pair_complete_assembly.py'))
        for name,value in cert['source_hashes'].items():
            require('input bytes '+name, (ROOT/name).resolve().is_relative_to(ROOT) and digest(ROOT/name) == value)
        audits = {}
        for n in range(125,151):
            a = read(f'l{n}-critical-audit.json')
            require('canonical audit failures '+str(n), a['failures'] == [])
            if n == 125:
                require('L125 original complete audit', a['full_saved_replay_identical'] and
                        a['original_artifacts_byte_unchanged'] and a['summary']['actual_cases'] == 100764)
            else:
                cs = a['checks']
                require('complete audit checks '+str(n), bool(cs) and
                    (all(v is True for v in cs.values()) if isinstance(cs,dict) else
                     all(c.get('passed',c.get('passes')) is True for c in cs)))
                fields = [k for k in ['runs','isolated_runs','execution','isolated_run'] if k in a]
                require('audit executions present '+str(n), bool(fields))
                for field in fields:
                    runs = a[field] if isinstance(a[field],list) else [a[field]]
                    require('all audit exits '+str(n)+field, bool(runs) and all(r['returncode']==0 for r in runs))
            manifest = a.get('inputs',a.get('input_sha256',a.get('audited_input_hashes')))
            audits[f'L{n}'] = {}
            for p,v in manifest.items():
                path = (BASE/p).resolve()
                value = v['sha256'] if isinstance(v,dict) else v
                require('audit manifest in frozen union '+str(n)+p,
                        path.is_relative_to(ROOT) and cert['source_hashes'][str(path.relative_to(ROOT))] == value)
                audits[f'L{n}'][str(path)] = value

        # Build four-sets first, then encode each as a bit mask; no pair-product enumeration.
        h = sorted({pow(8,i,97) for i in range(16)})
        s = {1,8,12,18,22,27,33}
        universe = sorted([[sorted(set(a)&s), sorted(set(a)-s)] for a in combinations(h,4)
                           if len(set(a)&s)==2])
        masks = [sum(1 << h.index(x) for x in i+k) for i,k in universe]
        fixed = [universe.index([[1,8],[47,50]]),universe.index([[12,18],[64,75]])]
        thirds = [i for i,m in enumerate(masks) if all((m&masks[f]).bit_count()<=1 for f in fixed)]
        master = read('new-pair-filter.json')
        require('entire independent original universe', len(universe)==756 and universe==master['universe'] and
                fixed == master['first_indices'] == [0,412] and cert['H']==h and set(cert['S'])==s)
        require('entire independent third universe', len(thirds)==382 and thirds==master['third_indices'] and
                [t['third_index'] for t in cert['thirds']]==thirds)

        # These are the exact index formulas in canonical conclusions, independent of overlays.
        expected = {}
        def add(label, indices):
            for index in indices:
                index = tuple(index)
                require('independent residual partition has no duplicate '+str(index), index not in expected)
                expected[index] = label
        singles = {126:(58,355),127:(58,647),129:(59,355),130:(59,647),133:(94,355),
                   135:(94,539),137:(175,238),139:(175,274),142:(199,565),143:(565,199),
                   144:(238,647),145:(239,647),147:(274,539)}
        for n,index in singles.items():
            add(f'L{n}',[index])
        a = [60,61,66,68,69,70,71]
        b = [60,61,66,67,68,69,70]
        add('L132',[(x,355) for x in a]+[(355,x) for x in [58,59]+a]+
                   [(x,647) for x in b]+[(647,x) for x in [58,59]+b])
        for label,t,fixed_index,old,orientation in [
            ('L134',[95,96,97,102,104,105,106,107],355,94,0),
            ('L136',[95,96,97,102,103,104,105,106],539,94,0),
            ('L138',[239,240,241,246,248,249,250,251],175,238,1),
            ('L140',[275,276,277,282,284,285,286,287],175,274,1),
            ('L148',[275,276,277,282,283,284,285,286],539,274,0)]:
            indices = ([(x,fixed_index) for x in t]+[(fixed_index,x) for x in [old]+t]
                       if orientation==0 else [(fixed_index,x) for x in t]+[(x,fixed_index) for x in [old]+t])
            add(label,indices)
        t = [240,241,246,247,248,249,250]
        add('L146',[(x,647) for x in t]+[(647,x) for x in [238,239]+t])
        add('L149',[(499,668),(668,499),(678,749),(749,678)])
        add('L150',[(467,750),(750,467),(608,695),(695,608)])
        require('exact independent residual set', len(expected)==154 and
                set(expected)==set(map(tuple,master['residual_occurrences'])))
        source_names = dict(zip([126,127,129,130,132,133,134,135,136,137,138,139,140,142,143,144,145,146,147,148,149,150],
            ['new-pair-first-residual-gates','new-pair-second-residual-gates',
             'third59-first-residual-gates','third59-second-residual-gates',
             'residual-locus-reuse','first-unmatched-locus-gates','l133-literal-reuse',
             'second-unmatched-locus-gates','l135-literal-reuse','first-l136-mismatch-locus-gates',
             'l137-literal-reuse','first-l138-mismatch-locus-gates','l139-literal-reuse',
             'first-l140-mismatch-locus-gates','l141-l142-literal-reuse',
             'first-l143-mismatch-locus-gates','l144-single-record-reuse',
             'l144-remaining-literal-reuse','first-l146-mismatch-locus-gates',
             'l147-literal-reuse','l148-rank20-gates','l148-rank20-gates']))
        counts = Counter()
        residuals = []
        for n,out_third in zip(thirds,cert['thirds']):
            shard_name = f'new-pair-filter/third-{n:03d}.json'
            shard = read(shard_name)
            indices = [j for j,m in enumerate(masks) if
                       all((m&masks[f]).bit_count()<=1 for f in fixed+[n])]
            require('independent complete fourth domain '+str(n),
                    [r['fourth_index'] for r in shard['cases']]==indices and
                    [r['fourth_index'] for r in out_third['cases']]==indices and out_third['third']==universe[n])
            evidence = []
            for pos,(j,original,r) in enumerate(zip(indices,shard['cases'],out_third['cases'])):
                idx = (n,j)
                require('all saved labels and pointers '+str(idx), r['fourth']==universe[j] and
                        r['original_shard']==shard_name and r['original_pointer']==f'/cases/{pos}' and
                        r['intersections']==[(masks[j]&masks[f]).bit_count() for f in fixed+[n]])
                if original['status'] != 'residual':
                    require('imported L125 predicate '+str(idx), original['status'] in ['rank','factor','omission'] and
                            r['disposition']=='L125_'+original['status'])
                    # Complete basis predicates are checked without rerunning rank searches.
                    basis = original['kernel_basis']
                    pairs = list(combinations(sorted(s),2))
                    factor = any(all(v[c]==0 for v in basis for c,pair in enumerate(pairs) if x not in pair)
                                 for f in fixed+[n,j] for x in universe[f][0]) if basis else False
                    omission = any(all(v[c]==0 for v in basis for c,pair in enumerate(pairs) if x in pair)
                                   for x in s) if basis else False
                    require('independent priority predicate '+str(idx),
                        (original['rank']==21 and not basis if original['status']=='rank' else
                         original['rank']<21 and bool(basis) and
                         (factor if original['status']=='factor' else not factor and omission)))
                else:
                    residuals.append(idx)
                    label = expected[idx]
                    require('canonical index-formula disposition '+str(idx), r['disposition']==label and
                            len(r['exclusions'])==1 and r['exclusions'][0]['lemma']==label)
                    binding = r['exclusions'][0]
                    source_name = source_names[int(label[1:])]+'.json'
                    require('exact audited source '+str(idx), binding['source']==source_name and
                            audits[label][str((BASE/source_name).resolve())]==digest(BASE/source_name))
                    source = pointer(read(source_name),binding['pointer'])
                    expected_rows = [dict(I=universe[f][0],K=universe[f][1]) for f in fixed+[n,j]]
                    require('all four imported labels '+str(idx), source['rows']==expected_rows==binding['rows'])
                    if 'complete_original_record' in source:
                        provenance = source if 'shard' in source else source['complete_prior_overlay']
                        require('whole original import '+str(idx), source['complete_original_record']==original and
                                provenance['shard']==shard_name and provenance['case_pointer']==f'/cases/{pos}')
                    else:
                        require('whole ordered kernel import '+str(idx), source['kernel_basis']==original['kernel_basis'])
                    if 'original_matrix' in source:
                        require('original stack binding '+str(idx), source['original_matrix']==
                                [v for f in fixed+[n,j] for v in master['blocks'][f]['matrix']])
                    require('whole original serialized binding '+str(idx), binding['original_record_sha256']==
                            sha256(json.dumps(original,sort_keys=True).encode()).hexdigest())
                    result['residual_checks'].append(dict(indices=idx,lemma=label,source=source_name,
                        source_pointer=binding['pointer'],original_shard=shard_name,original_pointer=f'/cases/{pos}',passes=True))
                counts[r['disposition']] += 1
                evidence.append(dict(fourth_index=j,disposition=r['disposition'],passes=True))
            result['thirds'].append(dict(third_index=n,eligible_fourths=indices,complete_checks=evidence))
        require('complete ordered residuals preserved', list(map(list,residuals))==master['residual_occurrences'])
        require('complete exchange evidence without quotient',
                [r['ordered_indices'] for r in cert['exchanges']]==
                [[[n,u],[u,n]] for n,u in residuals if n<u] and
                all([x['lemma'] for side in r['exclusions'] for x in side]==
                    [expected[tuple(i)] for i in r['ordered_indices']] for r in cert['exchanges']))
        require('complete residual binding manifest', [r['indices'] for r in cert['residual_bindings']]==master['residual_occurrences'] and
                all(r['exclusions']==next(c for t in cert['thirds'] if t['third_index']==r['indices'][0]
                    for c in t['cases'] if c['fourth_index']==r['indices'][1])['exclusions'] for r in cert['residual_bindings']))
        # Bind the actual surviving planes to the separate capacity conclusions.
        for source_name,capacity_name,points in [
            ('first-l140-mismatch-locus-gates.json','l141-survivor-full-rows.json',
             [read('first-l140-mismatch-locus-gates.json')['points_and_all_row_gates'][1]]),
            ('l148-rank20-gates.json','l149-survivor-full-rows.json',
             [r['plane_and_all_row_gates'] for r in read('l148-rank20-gates.json')['records']
              if r['disposition']=='intrinsic_survivor'])]:
            cap = read(capacity_name)
            require('complete capacity imported '+capacity_name, cap['failures']==cap['unresolved']==[])
            for p in points:
                matches = [q for q in cap['planes'] if q['u']==p['u'] and q['v']==p['v']]
                require('exact surviving plane '+source_name+str(p['u']),len(matches)==1 and p['passes_intrinsic_gates'])
        for n,label in [(58,'L128'),(59,'L131')]:
            overlap = next(x for x in cert['overlaps'] if x['lemma']==label)
            require('complete seed overlap '+label,overlap['occurrences']==[[n,r['fourth_index']] for r in read(f'new-pair-filter/third-{n:03d}.json')['cases']])
        require('complete final counts', sum(counts.values())==100764 and dict(counts)==cert['summary']['dispositions'])
        require('all inputs unchanged at finish',all(digest(ROOT/n)==v for n,v in cert['source_hashes'].items()))
        result['summary'] = dict(actual_thirds=len(thirds),required_thirds=382,
            actual_occurrences=sum(counts.values()),required_occurrences=100764,
            residuals_checked=len(residuals),required_residuals=154,uncovered=0,
            dispositions=dict(counts),exchanged_residuals_preserved=all((b,a) in expected for a,b in expected))
    except Exception as e:
        result['failures'].append(dict(type=type(e).__name__,message=str(e)))
    result['verifier_sha256'] = digest(Path(__file__))
    result['producer_certificate_sha256'] = digest(BASE/'new-pair-complete-assembly.json')
    path = BASE/'new-pair-complete-assembly-replay.json'
    path.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print(json.dumps(result.get('summary',{}),sort_keys=True))
    print('Failures:',len(result['failures']),'Uncovered:',len(result['uncovered']),'Certificate:',path)
    if result['failures']:
        print(result['failures'][0])
        raise SystemExit(1)


if __name__ == '__main__':
    run()
