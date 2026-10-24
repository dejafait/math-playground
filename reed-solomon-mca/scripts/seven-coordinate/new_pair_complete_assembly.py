"""Approved L125 pair assembly. Read-only imports of audited mathematics.

No rank search, locus solver, four-row converse, or historical deletion.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json
import re

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
S = [1, 8, 12, 18, 22, 27, 33]
H = [x for x in range(1, 97) if pow(x, 16, 97) == 1]
J = sorted(set(H)-set(S))
FIRST = [[[1, 8], [47, 50]], [[12, 18], [64, 75]]]
SINGLES = [
    (126, (58,355), 'new-pair-first-residual-gates'),
    (127, (58,647), 'new-pair-second-residual-gates'),
    (129, (59,355), 'third59-first-residual-gates'),
    (130, (59,647), 'third59-second-residual-gates'),
    (133, (94,355), 'first-unmatched-locus-gates'),
    (135, (94,539), 'second-unmatched-locus-gates'),
    (137, (175,238), 'first-l136-mismatch-locus-gates'),
    (139, (175,274), 'first-l138-mismatch-locus-gates'),
    (142, (199,565), 'first-l140-mismatch-locus-gates'),
    (144, (238,647), 'first-l143-mismatch-locus-gates'),
    (145, (239,647), 'l144-single-record-reuse'),
    (147, (274,539), 'first-l146-mismatch-locus-gates')]
OVERLAYS = [(132,'residual-locus-reuse'), (134,'l133-literal-reuse'),
            (136,'l135-literal-reuse'), (138,'l137-literal-reuse'),
            (140,'l139-literal-reuse'), (143,'l141-l142-literal-reuse'),
            (146,'l144-remaining-literal-reuse'), (148,'l147-literal-reuse')]


def digest(path):
    h = sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()


def rowkey(row):
    return [row['I'], row['K']] if isinstance(row, dict) else row


def run():
    out = dict(step_id='2026-10-24-mca-461-new-pair-complete-assembly',
               scope='Only the approved conditional L125 fixed pair',
               H=H, S=S, first_two=FIRST, source_hashes={}, audit_bindings=[],
               checks=[], residual_bindings=[], thirds=[], overlaps=[],
               exchanges=[], uncovered=[], failures=[])
    hashes = out['source_hashes']
    cache = {}
    audited_sources = {}

    def check(name, value):
        out['checks'].append(dict(name=name, passes=bool(value)))
        if not value:
            raise ValueError(name)

    def bind(path, expected=None):
        path = path.resolve()
        check('local input '+str(path), path.is_relative_to(ROOT))
        name = str(path.relative_to(ROOT))
        value = hashes.get(name)
        if value is None:
            value = digest(path)
            hashes[name] = value
        if expected is not None:
            check('audited bytes '+name, value == expected)
        return value

    def load(name):
        if name not in cache:
            bind(BASE/name)
            cache[name] = json.loads((BASE/name).read_bytes())
        return cache[name]

    def audit(number):
        name = f'l{number}-critical-audit.json'
        a = load(name)
        check('empty audit failures '+name, a['failures'] == [])
        if number == 125:
            check('L125 complete audit', a['original_artifacts_byte_unchanged'] and
                  a['full_saved_replay_identical'] and
                  a['summary']['actual_cases'] == a['summary']['required_cases'] == 100764)
        else:
            c = a['checks']
            check('all audit checks '+name, bool(c) and
                  (all(v is True for v in c.values()) if isinstance(c, dict) else
                   all(r.get('passes', r.get('passed')) is True for r in c)))
            execution_fields = [k for k in ['runs','isolated_runs','execution','isolated_run'] if k in a]
            check('explicit executions '+name, bool(execution_fields))
            for k in execution_fields:
                runs = a[k] if isinstance(a[k], list) else [a[k]]
                check('successful executions '+name+'/'+k, bool(runs) and
                      all(r['returncode'] == 0 for r in runs))
        for flag in ['original_artifacts_byte_unchanged','full_saved_replay_identical']:
            if flag in a:
                check('unchanged '+name+'/'+flag, a[flag] is True)
        manifest = a.get('audited_input_hashes', a.get('input_sha256', a.get('inputs')))
        check('explicit manifest '+name, isinstance(manifest, dict) and bool(manifest))
        for path, value in manifest.items():
            bind(BASE/path, value['sha256'] if isinstance(value, dict) else value)
        audited_sources[f'L{number}'] = {str((BASE/p).resolve()):
            (v['sha256'] if isinstance(v, dict) else v) for p,v in manifest.items()}
        lemma = next((ROOT/'lemmas').glob(f'L{number:03d}-*.md'))
        bind(lemma)
        text = lemma.read_text()
        code_hash = a.get('audit_code_sha256', a.get('audit_program_sha256'))
        if code_hash:
            candidates = re.findall(r'scripts/seven-coordinate/(audit[\w]+\.py)', text)
            check('canonical audit code '+name, any(digest(BASE/p) == code_hash for p in candidates))
            for p in candidates:
                bind(BASE/p)
        out['audit_bindings'].append(dict(lemma=f'L{number}', path=name,
                                         sha256=bind(BASE/name), manifest_entries=len(manifest)))
        return a

    try:
        check('assertions enabled', __debug__)
        for n in range(125,151):
            audit(n)
        for n in [86,103,104,109]:
            bind(next((ROOT/'lemmas').glob(f'L{n:03d}-*.md')))
        master = load('new-pair-filter.json')
        universe = [[list(i),list(k)] for i,k in product(combinations(S,2), combinations(J,2))]
        check('original universe and pair', master['universe'] == universe and
              master['first_two'] == FIRST and master['first_indices'] == [0,412] and len(universe) == 756)
        check('original master success', not master['failures'])
        sets = [set(i+k) for i,k in universe]
        fixed = [set(i+k) for i,k in FIRST]
        thirds = [i for i,a in enumerate(sets) if all(len(a & b) <= 1 for b in fixed)]
        check('all original thirds', thirds == master['third_indices'] and len(thirds) == 382)
        originals = {}
        shard_meta = {r['third_index']: r for r in master['thirds']}
        for n in thirds:
            meta = shard_meta[n]
            shard = load(meta['certificate'])
            check('original third identity '+str(n), shard['third_index'] == n and not shard['failures'])
            for pos, case in enumerate(shard['cases']):
                index = (n,case['fourth_index'])
                check('original unique occurrence '+str(index), index not in originals)
                originals[index] = (case, meta['certificate'], f'/cases/{pos}')
        historical = [list(index) for index,(r,_,_) in originals.items() if r['status'] == 'residual']
        check('complete original residual order', historical == master['residual_occurrences'] and len(historical) == 154)

        imports = {}

        def attach(index, label, source, pointer, record):
            index = tuple(index)
            check('import in original residual domain '+str(index), list(index) in historical)
            check('source in exact canonical audit '+label+str(index),
                  audited_sources[label].get(str((BASE/source).resolve())) == bind(BASE/source))
            case, shard, cp = originals[index]
            expected_rows = [dict(I=universe[i][0],K=universe[i][1]) for i in [0,412,*index]]
            check('all four source labels '+label+str(index), record['rows'] == expected_rows)
            if 'complete_original_record' in record:
                provenance = record if 'shard' in record else record['complete_prior_overlay']
                check('whole original record '+label+str(index), record['complete_original_record'] == case and
                      provenance['shard'] == shard and provenance['case_pointer'] == cp and
                      provenance['complete_original_record'] == case)
            else:
                check('complete source kernel '+label+str(index), record['kernel_basis'] == case['kernel_basis'])
            if 'original_matrix' in record:
                check('original source matrix '+label+str(index), record['original_matrix'] ==
                      [row for i in [0,412,*index] for row in master['blocks'][i]['matrix']])
            binding = dict(lemma=label, source=source, pointer=pointer, original_shard=shard,
                           original_pointer=cp, rows=expected_rows,
                           original_record_sha256=sha256(json.dumps(case,sort_keys=True).encode()).hexdigest())
            imports.setdefault(index, []).append(binding)

        for lemma,index,stem in SINGLES:
            record = load(stem+'.json')
            attach(index,f'L{lemma}',stem+'.json','',record)
        # L142's indexed conclusion uses L141's classification AND its audited capacity.
        capacity = load('l141-survivor-full-rows.json')
        check('L142 complete capacity source', capacity['failures'] == [] and capacity['unresolved'] == [])
        check('L142 capacity audit binding', audited_sources['L142'].get(str((BASE/'l141-survivor-full-rows.json').resolve())) ==
              bind(BASE/'l141-survivor-full-rows.json'))
        for lemma,stem in OVERLAYS:
            cert = load(stem+'.json')
            check('unchanged full historical list '+stem, cert['historical_residual_occurrences'] == historical and not cert['failures'])
            covered = []
            for pos,r in enumerate(cert['overlay']):
                if r['disposition'] == 'covered':
                    attach(r['indices'],f'L{lemma}',stem+'.json',f'/overlay/{pos}',r)
                    covered.append(r['indices'])
            check('exact declared covered list '+stem, covered == cert['covered_indices'])
        r20 = load('l148-rank20-gates.json')
        capacities = load('l149-survivor-full-rows.json')
        check('L150 complete capacity success', capacities['failures'] == capacities['unresolved'] == [])
        for pos,r in enumerate(r20['records']):
            label = 'L149' if r['disposition'] == 'excluded_necessary_gates' else 'L150'
            if label == 'L150':
                plane = r['plane_and_all_row_gates']
                matches = [p for p in capacities['planes'] if r['indices'] in p['historical_indices']]
                check('unique surviving plane capacity '+str(r['indices']), len(matches) == 1 and
                      matches[0]['u'] == plane['u'] and matches[0]['v'] == plane['v'])
            else:
                check('L149 exact failing disposition', r['disposition'] == 'excluded_necessary_gates')
            attach(r['indices'],label,'l148-rank20-gates.json',f'/records/{pos}',r)
        check('all residuals covered exactly as a set', set(imports) == set(map(tuple,historical)))
        for index in map(tuple,historical):
            out['residual_bindings'].append(dict(indices=index, exclusions=imports.get(index,[])))
        for n,u in map(tuple,historical):
            check('historical exchanged residual retained '+str((n,u)), (u,n) in imports)
            if n < u:
                out['exchanges'].append(dict(ordered_indices=[[n,u],[u,n]],
                    exclusions=[imports[n,u],imports[u,n]]))
        # The seed assemblies remain overlapping independent evidence, not added cases.
        for n,label in [(58,'L128'),(59,'L131')]:
            out['overlaps'].append(dict(lemma=label, third_index=n,
                occurrences=[list(i) for i in originals if i[0] == n],
                source='third'+str(n)+'-assembly.json'))
            load('third'+str(n)+'-assembly.json')
        counts = Counter()
        for n in thirds:
            expected = [u for u,a in enumerate(sets) if all(len(a & b) <= 1 for b in fixed+[sets[n]])]
            actual = [u for v,u in originals if v == n]
            check('complete original eligible fourths '+str(n), actual == expected)
            records = []
            for u in actual:
                case,shard,cp = originals[n,u]
                if case['status'] != 'residual':
                    label = 'L125_'+case['status']
                    evidence = [dict(lemma='L125',source=shard,pointer=cp)]
                else:
                    evidence = imports.get((n,u),[])
                    label = evidence[0]['lemma'] if evidence else 'UNCOVERED'
                    if not evidence:
                        out['uncovered'].append([n,u])
                counts[label] += 1
                records.append(dict(fourth_index=u, fourth=universe[u],
                    original_shard=shard, original_pointer=cp,
                    intersections=[len(sets[u]&a) for a in fixed+[sets[n]]],
                    disposition=label, exclusions=evidence))
            out['thirds'].append(dict(third_index=n,third=universe[n],cases=records))
        check('complete occurrence count', sum(counts.values()) == 100764)
        check('nothing uncovered', out['uncovered'] == [])
        check('all frozen inputs unchanged', all(digest(ROOT/n) == h for n,h in hashes.items()))
        out['summary'] = dict(actual_thirds=len(thirds),required_thirds=382,
            actual_occurrences=sum(counts.values()),required_occurrences=100764,
            original_residuals=len(historical),covered_residuals=len(imports),
            dispositions=dict(counts),uncovered=len(out['uncovered']),audits=len(out['audit_bindings']),
            inputs=len(hashes))
    except Exception as e:
        out['failures'].append(dict(type=type(e).__name__,message=str(e)))
    out['producer_sha256'] = digest(Path(__file__))
    target = BASE/'new-pair-complete-assembly.json'
    target.write_text(json.dumps(out,separators=(',',':'))+'\n')
    print(json.dumps(out.get('summary',{}),sort_keys=True))
    print('Failures:',len(out['failures']),'Uncovered:',len(out['uncovered']),'Certificate:',target)
    if out['failures']:
        print(out['failures'][0])
        raise SystemExit(1)


if __name__ == '__main__':
    run()
