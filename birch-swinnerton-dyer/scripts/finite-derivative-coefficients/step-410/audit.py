
import hashlib, json, math, traceback
from pathlib import Path
ROOT = Path.cwd()
BASE = ROOT/'scripts/finite-derivative-coefficients'
OUT = BASE/'step-410'
LIMIT = 134217728
EXPECTED = '7547b371d675441190256195270c9282213e888cdb666451ae21a062896e4415'
EXTRACTED = '9ad5f8b621dab84edeb97b891f5d4ed9cfe6d11c43b1b7b7f8e2b7147780363f'
L031 = 'lemmas/L031-independent-twist-five-ratio-certificate.md'
INSERT_HASH = 'd8a11d35c1e71ce05beb162a34f4f19591beac33b94733aa042d25b09c468ecd'
state, initial, checks, failure = 'setup', {}, {}, None
def digest(raw):
    return hashlib.sha256(raw).hexdigest()
def disk():
    return sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file())
def save(name, obj):
    raw = (json.dumps(obj, indent=2)+'\n').encode()
    assert disk()+len(raw)+65536 <= LIMIT, 'artifact cap and finalization reserve'
    (OUT/name).write_bytes(raw)
def inventory(paths):
    return {str(p.relative_to(ROOT)): {'sha256':digest(p.read_bytes()),'bytes':p.stat().st_size}
            for p in sorted(set(paths))}
try:
    OUT.mkdir()
    (OUT/'audit.py').write_text(SOURCE)
    (OUT/'bootstrap.txt').write_text(
        'Start monotonic clock before signal imports, source writing, inventory and arithmetic. '
        'Arm 174-second work timer. Execute audit.py with START, SOURCE, time and signal supplied. '
        'Finalization keeps the aggregate 180-second deadline armed through termination. '
        'No original producer or report entrypoint runs.\n')
    paths = [p for folder in ('scripts/twist-five','scripts/first-rational-kernel','scripts/finite-derivative-coefficients')
             for p in (ROOT/folder).rglob('*') if p.is_file() and OUT not in p.parents]
    for pattern in ('lemmas/L030-*.md','lemmas/L031-*.md','lemmas/L101-*.md','lemmas/L102-*.md','lemmas/L103-*.md'):
        paths.extend(ROOT.glob(pattern))
    paths.extend(ROOT/p for p in ('PROOF.md','DAG.md',
        'drafts/literature/2026-10-23-finite-derivative-coefficient-audit.md',
        'drafts/literature/2026-10-22-finite-derivative-coefficient-certificate.md'))
    initial = inventory(paths)
    save('initial-inventory.json', initial)
    state = 'historical preservation and exact L031 transition'
    historic = json.loads((BASE/'preservation.json').read_text())
    assert len(historic) == 48
    old_path = ROOT/'scripts/first-rational-kernel/step-404/originals'/L031
    old, current = old_path.read_bytes(), (ROOT/L031).read_bytes()
    assert digest(old) == historic[L031] == '31e0d2b9e1ffe4961d92fed9fdf5f54d1bbb25c9faf0743c3ac533cec4fef0d1'
    marker = b'## Mathlib\n'
    assert old.count(marker) == current.count(marker) == 1
    prefix, suffix = old.split(marker)
    assert current.startswith(prefix) and current.endswith(marker+suffix)
    insertion = current[len(prefix):-(len(marker)+len(suffix))]
    assert len(insertion) == 2790 and digest(insertion) == INSERT_HASH
    assert current == prefix+insertion+marker+suffix
    save('historical-document-transition.json', {
        'path':L031,'retained_old_path':str(old_path.relative_to(ROOT)),
        'old_sha256':digest(old),'current_sha256':digest(current),
        'insert_before':'## Mathlib\n','exact_insertion':insertion.decode(),
        'insertion_sha256':INSERT_HASH,'exact_entire_document_equality':True})
    historic_rows = []
    for rel, sha in historic.items():
        observed = digest(old) if rel == L031 else digest((ROOT/rel).read_bytes())
        assert observed == sha, ('historical input',rel)
        historic_rows.append({'path':rel,'expected_sha256':sha,'matched_sha256':observed,
            'binding':'retained-copy plus exact full insertion transition' if rel==L031 else 'unchanged current bytes'})
    save('historical-preservation.json', historic_rows)
    checks['historical_inventory_entries'] = len(historic_rows)
    state = 'full count replay'
    original_path = ROOT/'scripts/twist-five/certificate.json'
    assert digest(original_path.read_bytes()) == EXPECTED
    assert digest((BASE/'certificate.json').read_bytes()) == EXTRACTED
    original = json.loads(original_path.read_text())
    fresh = json.loads((BASE/'certificate.json').read_text())
    assert original['selected_attempt'] == 0 and len(original['attempts']) == 1
    data = original['attempts'][0]
    assert data['T'] == 256
    assert data['source_inputs']['model'] == [0,1,1,-2,0]
    assert data['source_inputs']['N'] == data['source_inputs']['Delta'] == 389
    prime_list = [p for p in range(2,257) if all(p%d for d in range(2,math.isqrt(p)+1))]
    assert len(prime_list) == 54
    assert [r['p'] for r in data['point_counts']] == prime_list
    assert data['nodal_count']['p'] == 389
    counts, full_fibers = [], []
    for row in data['point_counts']+[data['nodal_count']]:
        p = row['p']
        ys_by_x = [[] for _ in range(p)]
        # Reverse nesting from the original replay, covering every pair.
        for y in range(p):
            lhs = (y*y+y)%p
            for x in range(p):
                if lhs == (x*x*x+x*x-2*x)%p:
                    ys_by_x[x].append(y)
        fibers = [len(ys) for ys in ys_by_x]
        pairs = [[x,y] for x,ys in enumerate(ys_by_x) for y in ys]
        if p==2:
            assert pairs == row['pairs'], 'all pairs at two'
        else:
            assert [k-1 for k in fibers] == row['discriminant_characters'], ('characters',p)
        affine = sum(fibers)
        assert (row['affine'],row['total'],row['a_p']) == (affine,affine+1,p-affine), ('count',p)
        counts.append({'p':p,'fiber_counts':fibers,'affine':affine,'total':affine+1,'a_p':p-affine,
                       'pairs_at_two':pairs if p==2 else None})
        full_fibers.append({'p':p,'y_solutions_by_x':ys_by_x,'infinity_points':1})
    assert counts == fresh['point_counts'], 'all fresh count fields'
    assert counts[-1]['a_p'] == 1
    save('full-fibers.json', full_fibers)
    checks.update(good_prime_rows=54,nodal_rows=1,exhausted_xy_pairs=sum(r['p']**2 for r in counts))
    state = 'all fixed factorizations and recurrence records'
    ap = {r['p']:r['a_p'] for r in counts[:-1]}
    factor_records, by_factors = [], [0,1]
    for n in range(2,257):
        rem, factors, value = n, [], 1
        for p in prime_list:
            exponent = 0
            while rem%p==0:
                rem //= p
                exponent += 1
            if exponent:
                terms = [1,ap[p]]
                for k in range(2,exponent+1):
                    terms.append(ap[p]*terms[-1]-p*terms[-2])
                factors.append([p,exponent,terms])
                value *= terms[-1]
        assert rem == 1, ('complete factorization',n)
        factor_records.append([n,factors])
        by_factors.append(value)
    assert factor_records == data['factorizations_and_prime_powers'] == fresh['factorizations_and_prime_powers']
    assert by_factors == data['coefficients'] == fresh['coefficients_with_index_zero_sentinel']
    state = 'distinct increasing-index least-prime recurrence'
    independent, recurrence = [0,1], [{'n':1,'value':1,'rule':'normalized'}]
    for n in range(2,257):
        # No factorization or prime-power array from the preceding replay is read.
        p = next(d for d in range(2,n+1) if n%d==0)
        m = n//p
        first = ap[p]*independent[m]
        second = p*independent[m//p] if m%p==0 else 0
        value = first-second
        assert value == by_factors[n] == data['coefficients'][n] == fresh['coefficients_with_index_zero_sentinel'][n], ('independent slot',n)
        independent.append(value)
        recurrence.append({'n':n,'least_prime':p,'m':m,'p_divides_m':m%p==0,
            'a_p':ap[p],'a_m':independent[m],'a_m_over_p':independent[m//p] if m%p==0 else None,
            'first':first,'subtracted':second,'value':value})
    export = [{'n':n,'a_n':independent[n]} for n in range(1,129)]
    expected = {'upstream_path':'scripts/twist-five/certificate.json','upstream_sha256':EXPECTED,
        'selected_attempt':0,'model':[0,1,1,-2,0],'N':389,'Delta':389,'T':256,
        'point_counts':counts,'factorizations_and_prime_powers':factor_records,
        'coefficients_with_index_zero_sentinel':independent,'export_indices_1_through_128':export,
        'normalization':'a_1=1; full untwisted unnormalized newform coefficients'}
    assert expected == fresh, 'entire extraction, all bindings and exact export rows'
    save('full-replayed-extraction.json', expected)
    save('independent-recurrence.json', recurrence)
    checks.update(factorization_records=255,coefficient_slots=256,independent_slots=256,exported_slots=128,
        zero_coefficient_indices=[n for n in range(1,257) if independent[n]==0],
        powers_of_two=[{'n':2**k,'a_n':independent[2**k]} for k in range(9)])
    state = 'fixed historical report verification'
    historical_report = json.loads((BASE/'report.json').read_text())
    expected_report = {'failures':[],'required_seconds':180,'required_new_bytes':LIMIT,
        'external_theorems_verified':False,'complete_replay':True,'good_prime_rows':54,'nodal_rows':1,
        'exhausted_xy_pairs':1147098,'factorization_records':255,'coefficient_slots':256,
        'exported_slots':128,'preserved_files':48,'certificate_sha256':EXTRACTED,
        'measured_seconds_before_final_write':0.07647291710600257,'new_artifact_bytes_upper_bound':167628}
    assert historical_report == expected_report
    historic_bytes = sum((BASE/p).stat().st_size for p in ('replay.py','certificate.json','preservation.json','report.json'))
    assert historic_bytes == 163638 and historic_bytes < historical_report['new_artifact_bytes_upper_bound'] <= LIMIT
    save('historical-report-review.json', {'fixed_report':historical_report,'four_original_file_bytes':historic_bytes,
        'post_write_seconds_independently_persisted':False,
        'qualification':'0.076641 seconds is historical printed output only; no retroactive timing certification.'})
    checks['original_four_file_bytes'] = historic_bytes
    state = 'complete'
except Exception as exc:
    failure = {'stage':state,'type':type(exc).__name__,'message':str(exc),'traceback':traceback.format_exc()}
finally:
    def hard_stop(*_):
        raise SystemExit('aggregate 180-second deadline reached')
    signal.signal(signal.SIGALRM, hard_stop)
    signal.setitimer(signal.ITIMER_REAL,max(0.001,180-(time.monotonic()-START)))
    after = inventory([ROOT/p for p in initial])
    preserved = after == initial
    if not preserved and failure is None:
        failure = {'stage':'final preservation','message':'current input bytes changed'}
    save('final-preservation.json', {'before':initial,'after':after,'all_equal':preserved,'count':len(initial)})
    elapsed = time.monotonic()-START
    inclusive_seconds = math.ceil(elapsed)+2
    inclusive_bytes = disk()+65536
    if (inclusive_seconds>180 or inclusive_bytes>LIMIT) and failure is None:
        failure = {'stage':'final resource bound','message':'aggregate cap exceeded'}
    report = {'status':'PASS' if failure is None and state=='complete' else 'STOP',
        'state':state,'checks':checks,'failure':failure,'preserved_current_files':len(initial),'all_current_inputs_preserved':preserved,
        'elapsed_before_final_report':elapsed,'inclusive_seconds_upper_bound':inclusive_seconds,
        'inclusive_bytes_upper_bound':inclusive_bytes,'required_seconds':180,'required_new_bytes':LIMIT,
        'scope':'known coefficient extraction only; no kernel, period, original producer or original report entrypoint'}
    save('report.json', report)
    actual_seconds, actual_bytes = time.monotonic()-START, disk()
    assert actual_seconds<=inclusive_seconds<=180
    assert actual_bytes<=inclusive_bytes<=LIMIT
    print(json.dumps({'status':report['status'],'coverage':checks,'preserved_files':len(initial),
        'failures':failure,'actual_seconds_after_final_report':actual_seconds,
        'inclusive_seconds_bound':inclusive_seconds,'required_seconds':180,
        'actual_new_bytes':actual_bytes,'inclusive_bytes_bound':inclusive_bytes,'required_new_bytes':LIMIT,
        'path':'scripts/finite-derivative-coefficients/step-410/report.json'}), flush=True)
    if report['status']!='PASS':
        raise SystemExit(1)
