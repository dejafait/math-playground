"""One preserved actual-zero composition; full streams and source-based bounds.

Interned immutable trees are only an in-memory representation. Every received
record occurrence and every expanded field is retained and serialized.
"""
import gzip
import hashlib
import json
import sys
from pathlib import Path
import chain

b, p, ep = chain.b, chain.p, chain.ep
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'scripts/left-closure'))
import replay_star as r
import finish_exports as spelling
import receive_actual_one_220 as reception
independent = reception.independent
suite = b.module('actual232_suite', ROOT/'scripts/backward-zero/run_suite.py')
auditchain = b.module('actual232_auditchain', ROOT/'scripts/backward-zero/audit_chain.py')
rowledger = b.module('actual232_rowledger', ROOT/'scripts/backward-zero/ledger.py')
sys.path.insert(0, str(ROOT/'scripts/coefficient-chain'))
tablecheck = b.module('actual232_tablecheck', ROOT/'scripts/coefficient-chain/check.py')
OUT = ROOT/'scripts/backward-zero/output/actual-zero-232-r1'
MODES = ('native', 'not-or')


def compact(x):
    return {k: v for k, v in x.items() if k not in ('rows', 'references')}


def fast_package(path, goal):
    """Exact aggregate.load contract with shared immutable subtrees.

    This independently reconstructs every native schema/MP and measures every
    occurrence. Paired full archive replay is separate; no saved success flag
    or hash replaces an inference check here.
    """
    syntax = r.f.FastSyntax(); terms = []; ids = []; rows = []
    sums = dict.fromkeys(MODES, 0); depths = dict.fromkeys(MODES, 0)
    payload = 1; digest = hashlib.sha256(); size = 0
    def tree(j):
        while len(terms) < len(syntax.nodes):
            tag, *args = syntax.nodes[len(terms)]
            terms.append(args[0] if tag == 'v' else tuple([tag]+[terms[a] for a in args]))
        return terms[j]
    try:
        target = syntax.parse(goal)
        with gzip.open(path, 'rb') as stream:
            raw = stream.readline(); digest.update(raw); size += len(raw)
            assert r.strict_read(raw) == dict(format='native', goal=goal)
            for index, raw in enumerate(stream):
                digest.update(raw); size += len(raw); row = r.strict_read(raw)
                rule = row['rule']; subs = row.get('subs', {})
                if rule == 'mp':
                    assert set(row) == {'f', 'rule', 'refs'}
                    refs = row['refs']
                    assert len(refs) == 2 and all(type(k) is int and 0 <= k < index for k in refs)
                    a, conditional = [ids[k] for k in refs]
                    tag, *args = syntax.nodes[conditional]
                    assert tag == 'i' and args[0] == a
                    expected = args[1]
                else:
                    assert set(row) == {'f', 'rule', 'subs'}
                    expected = syntax.ax(rule, subs); refs = []
                actual = syntax.parse(row['f']); assert actual == expected
                subids = {key: syntax.parse(value) for key, value in subs.items()}
                for node in [actual]+list(subids.values()):
                    stat = syntax.stats[node]; payload = max(payload, stat[4])
                    for m, offset in zip(MODES, (0, 2)):
                        sums[m] += stat[offset]; depths[m] = max(depths[m], stat[offset+1])
                rows.append((tree(actual), rule, refs, {k: tree(v) for k, v in subids.items()}))
                ids.append(actual)
        assert ids and ids[-1] == target
        return dict(rows=rows, node_sums=sums, depths=depths, name_bytes=payload,
                    measurement=dict(lines=len(rows), bytes=size, sha256=digest.hexdigest()))
    finally:
        syntax.close()


class ExactImportChain(chain.ChainStore):
    def copy(self, rows, env):
        if env:
            return super().copy(rows, env)
        # Simultaneous substitution by the empty map is the identity. Avoid
        # allocating expanded copies of immutable trees; still reconstruct
        # EVERY primitive occurrence. Store.retain compares every full field.
        moved = []
        for f, rule, refs, subs in rows:
            j = (self.p.mp(*(moved[a] for a in refs)) if rule == 'mp' else
                 self.p.ax(rule, subs['A'], subs['B'], subs.get('C')))
            assert self.p.rows[j][0] == f
            moved.append(j)
        return moved[-1]


def prefix(paths, count):
    size = 0; digest = hashlib.sha256()
    with gzip.open(paths[0], 'rb') as first, gzip.open(paths[1], 'rb') as second:
        first.readline(); second.readline()
        for i, raw in enumerate(first):
            assert raw == second.readline(), ('earlier prefix mismatch', i)
            size += len(raw); digest.update(raw)
        assert i+1 == count and second.readline()
    return dict(records=count, bytes=size, sha256=digest.hexdigest(), all_records_equal=True)


def chain_bound(data, packages, constants, terms, names):
    bound = chain.thresholds(data, packages, constants, terms, names)
    other, locations = auditchain.bounds(data, packages, constants, names)
    assert locations == bound['metadata_bytes']
    for m in MODES:
        assert other[m] == {k: bound['formats'][m][k] for k in other[m]}
    return bound


def main():
    assert not OUT.exists(), 'preserve prior attempt and archives'
    OUT.mkdir()
    cert = dict(step=232, complete=False, phase='saved-inputs', failures=[],
                resolved_harness_incidents=[dict(path='scripts/backward-zero/output/actual-zero-232/certificate.json',
                    reason='Initial driver used only library payload lengths; repaired to include original optional/source names before chain construction. No mathematical hypothesis changed.')],
                optional=[], local=[], coordinates=[], proofs={}, library={}, libraries={})
    dest = OUT/'certificate.json'
    def save(): dest.write_text(json.dumps(cert, indent=2)+'\n')
    save()
    try:
        oldpath = ROOT/'scripts/left-closure/output/reception-216.json'
        oldraw = oldpath.read_bytes(); old = r.strict_read(oldraw)
        tpath = ROOT/'scripts/coefficient-chain/output/empty.json'
        traw = tpath.read_bytes(); table = r.strict_read(traw)
        tablecheck.check(table)
        data = table['chain']; goals = chain.validate(data)
        inp_path = ROOT/'scripts/actual-tree/output/empty-zero-repaired.input.json'
        inp_raw = inp_path.read_bytes(); inp = r.strict_read(inp_raw)
        I, N, X, E, P = independent.I, independent.neg, independent.X, independent.E, independent.P
        y = I('q', 'q'); z = N(y); suffixes = [P(z, y), y]
        assert inp == dict(source=dict(tree=['zero'], letters=[], q='q', delete_zero=True),
            edges=[], request=dict(N=2, n=0, t=1, q='q', suffixes=suffixes,
                                  letters=[], E0=[[0,0],[0,0]], Eb=[]))
        assert table['source'] == inp['source'] and table['adjacency'] == inp['request']
        assert data == dict(N=2, n=0, q='q', suffixes=suffixes, letters=[],
            beta=[[0],[1]], G=[], levels=[dict(k=1,R=[[1,0]],T=[[]]),
                dict(k=0,R=[],T=[]),dict(k=0,R=[],T=[])])
        assert chain.base_request(data) == {k:old['receiving'][k] for k in chain.base_request(data)}
        assert goals == [E(suffixes[0], X(z,z)), E(y, X(y,z))]
        local_goals = [E(suffixes[v], X(z if v == 0 else y, X(z,z))) for v in range(2)]
        paths = [ROOT/x['proofs']['native']['measurement']['path'] for x in old['exports']]
        images = [ROOT/x['proofs']['not-or']['measurement']['path'] for x in old['exports']]
        cert['provenance'] = dict(input=str(inp_path.relative_to(ROOT)), input_sha256=hashlib.sha256(inp_raw).hexdigest(),
            table=str(tpath.relative_to(ROOT)), table_sha256=hashlib.sha256(traw).hexdigest(),
            prior=str(oldpath.relative_to(ROOT)), prior_sha256=hashlib.sha256(oldraw).hexdigest(),
            coordinate_paths=[str(x.relative_to(ROOT)) for x in paths], original_received=old['original_received'],
            receiving=data, exact_coordinate_endpoints=goals, exact_source_row_endpoint=E(suffixes[0], z))
        (OUT/'request.json').write_text(json.dumps(data, indent=2)+'\n'); save()
        prior = r.strict_read((ROOT/'scripts/actual-tree/output/audit-214.json').read_bytes())
        initial = r.strict_read((ROOT/'scripts/left-closure/output/certificate-202.json').read_bytes())
        cert['phase'] = 'fixed-library-replay'; save()
        libraries = reception.replay_libraries(prior, initial); cert['libraries'] = libraries
        constants = independent.constants({k:v for k,v in libraries['closure'].items() if k != 'close_cancel'})
        lib = {}
        for name, goal in ep.fixed().items():
            saved = libraries['closure'][name]['measurements']['native']
            lib[name] = fast_package(ROOT/saved['path'], ep.c.serialize(goal))
            assert all(lib[name]['measurement'][k] == saved[k] for k in ('lines','bytes','sha256'))
        cert['constants'] = constants; save()
        originals = []
        for i in range(2):
            term = 'unused'
            for _ in range(35 if i else 0): term = N(term)
            path = ROOT/old['original_received'][i]['path']
            got = r.scan(r.f.FastSyntax, path, I(term, term))
            assert compact(got) == prior['inputs'][i]
            cert['optional'].append(compact(got)); originals.append((path,len(got['rows'])))
        cert['phase'] = 'local-replay'; save()
        local_imports = []
        for v, goal in enumerate(local_goals):
            path = ROOT/old['source_packages'][v]['measurements']['native']['path']
            image = ROOT/old['source_packages'][v]['measurements']['not-or']['path']
            got = r.scan(r.f.FastSyntax, path, goal, image, imports=originals)
            assert compact(got) == old['source_packages'][v]
            cert['local'].append(compact(got)); local_imports.append((path,len(got['rows'])))
            print('PASS complete local pair and nested optional occurrences',v,flush=True); save()
        # Reuse the independently audited source/closure arithmetic. Its fixed
        # U=1,n=0 formulas apply to this very zero source; every field is checked.
        reception.independent_ledgers(cert, inp, initial, cert['local'], libraries,
            old['uniform_ledger'], old['source_bound'], old['composed_source_majorant'])
        cert['source_bound'] = old['source_bound']
        cert['closure_source_bound'] = old['composed_source_majorant']
        cert['phase'] = 'coordinate-replay'; save()
        roots = {}
        for v, goal in enumerate(goals):
            roots[old['exports'][v]['root']] = goal
            print('Replay complete coordinate pair',v,flush=True)
            got = r.scan(r.f.FastSyntax, paths[v], goal, images[v], roots=roots, imports=local_imports)
            assert len(got['rows'])-1 == old['exports'][v]['root']
            for m in MODES: assert got['measurements'][m] == old['exports'][v]['proofs'][m]['measurement']
            cert['coordinates'].append(compact(got)); save()
        cert['earlier_prefix'] = {m:prefix([paths[0],paths[1]] if m=='native' else images,
                                                len(range(old['exports'][0]['root']+1))) for m in MODES}
        print('PASS both complete coordinate pairs and full earlier prefix',flush=True)
        terms = {m:suite.measured_terms(data,m) for m in MODES}
        names = cert['source_accounting_check']['source_payload_bytes']
        received = [dict(rows=range(x['measurements']['native']['lines']),
            node_sums=x['node_sums'],depths=x['depths'],name_bytes=x['name_bytes']) for x in cert['coordinates']]
        direct = chain_bound(data,received,constants,terms,names)
        cb = cert['closure_source_bound']
        majorants = [dict(rows=range(cb['lines']),
            node_sums={m:cb['formats'][m]['bytes'] for m in MODES},
            depths={m:cb['formats'][m]['depth'] for m in MODES},name_bytes=names) for _ in paths]
        composed = chain_bound(data,majorants,constants,terms,names)
        for x in cert['coordinates']:
            assert x['name_bytes'] <= names
            for m in MODES:
                assert x['measurements'][m]['lines'] <= cb['lines']
                assert x['node_sums'][m] <= x['measurements'][m]['bytes'] <= cb['formats'][m]['bytes']
                assert x['depths'][m] <= cb['formats'][m]['depth']
        for m in MODES:
            for k in ('lines','depth','record_nodes','bytes','proof_and_locations_bytes'):
                assert direct['formats'][m][k] <= composed['formats'][m][k]
        cert.update(direct_chain_ledger=direct,original_source_chain_ledger=composed,phase='compile-fresh-store'); save()
        original_load = b.aggregate.load
        b.aggregate.load = fast_package
        try: obj = ExactImportChain(data, paths, lib).run()
        finally: b.aggregate.load = original_load
        for pkg,x in zip(obj.packages,cert['coordinates']):
            assert pkg['node_sums'] == x['node_sums'] and pkg['depths'] == x['depths'] and pkg['name_bytes'] == x['name_bytes']
            assert all(pkg['measurement'][k] == x['measurements']['native'][k] for k in ('lines','bytes','sha256'))
        assert len(obj.rows) == 1 and obj.rows[0]['level'] == 0 and obj.rows[0]['row'] == 0
        assert obj.root == obj.resolve(0,0,obj.handles[(0,0)])
        final = E(suffixes[0],z); assert p.text(obj.p.rows[obj.root][0]) == final
        cert.update(imports=obj.imports,rows=obj.rows,root=obj.root,max_argument_height=obj.max_argument_height)
        locations = dict(coordinate_imports=obj.imports,levels=[x['k'] for x in data['levels']],
            rows=[{k:x[k] for k in ('level','row','start','end','required_roots')} for x in obj.rows])
        locpath=OUT/'locations.json'; locpath.write_text(json.dumps(locations,separators=(',',':'))+'\n')
        assert locpath.stat().st_size <= direct['metadata_bytes'] <= composed['metadata_bytes']
        cert['locations'] = dict(path=str(locpath.relative_to(ROOT)),bytes=locpath.stat().st_size,required=composed['metadata_bytes'])
        root_goals = dict(zip(obj.rows[0]['required_roots'],ep.strings(chain.row_request(data,0,0))['goals']))
        for item,goal in zip(obj.imports,goals): root_goals[item['root']] = goal
        # The earlier coordinate is also retained inside the second occurrence.
        root_goals[obj.imports[1]['start']+old['exports'][0]['root']] = goals[0]
        cert['requested_roots'] = root_goals; cert['phase'] = 'write-complete-streams'; save()
        streams=[]; writers=[]
        for m in MODES:
            path=OUT/('chain.'+m+'.jsonl.gz'); streams.append(path)
            print('Write full joined',m,len(obj.p.rows),'records',flush=True)
            writers.append(spelling.write(obj,path,m=='not-or'))
        cert['phase']='joined-full-replay'; save()
        got=r.scan(r.f.FastSyntax,streams[0],final,streams[1],roots=root_goals,
                   imports=[(path,len(pkg['rows'])) for path,pkg in zip(paths,obj.packages)])
        assert len(got['rows'])-1 == obj.root
        for m,path,writer in zip(MODES,streams,writers):
            measured=got['measurements'][m]
            assert all(writer[k] == measured[k] for k in ('lines','bytes','sha256'))
            assert got['depths'][m] <= direct['formats'][m]['depth']
            checks=rowledger.check(measured,direct['formats'][m])
            sourcechecks=rowledger.check(measured,composed['formats'][m])
            assert all(checks.values()) and all(sourcechecks.values())
            cert['proofs'][m]=dict(measurement=measured,direct_checks=checks,original_source_checks=sourcechecks,
                full_field_depth=got['depths'][m],literal_image_every_record=True,complete_relocated_imports=True)
            print('PASS',m,'lines',measured['lines'],'<=',composed['lines'],
                  'bytes',measured['bytes'],'<=',composed['formats'][m]['bytes'],
                  'full depth',got['depths'][m],'<=',composed['formats'][m]['depth'],flush=True)
        syntax=r.f.FastSyntax()
        try:
            stats=[syntax.stats[syntax.parse(t)] for call in obj.calls for t in call['arguments'].values()]
            cert['arguments']={}
            for m,off in zip(MODES,(0,2)):
                actual=dict(nodes=max(s[off] for s in stats),depth=max(s[off+1] for s in stats))
                assert actual['nodes'] <= direct['formats'][m]['argument_nodes']
                assert actual['depth'] <= direct['formats'][m]['argument_depth']
                cert['arguments'][m]=actual
        finally: syntax.close()
        assert obj.max_argument_height <= direct['H']
        assert all(t['max_height'] <= direct['H'] for row in obj.rows for t in row['traces'])
        ancestors=r.a.ancestors(got['references'],obj.root)
        assert obj.coordinate_roots[0] in ancestors
        cert['source_coordinate_used_in_final_ancestry']=obj.coordinate_roots[0]
        interface=dict(source=inp,optional=old['original_received'],receiving=data,
            coordinates=[dict(native=str(path.relative_to(ROOT)),image=str(image.relative_to(ROOT)))
                         for path,image in zip(paths,images)],locations=locations)
        interface_bytes=len(json.dumps(interface,separators=(',',':')).encode('ascii'))
        library_bytes={name:{m:sum(x['measurements'][m]['bytes'] for x in lib0.values()) for m in MODES}
                       for name,lib0 in libraries.items()}
        # Pay the chain library again even though it is a closure subset.
        library_bytes['chain']={m:sum(x['measurements'][m]['bytes'] for k,x in libraries['closure'].items()
                                    if k!='close_cancel') for m in MODES}
        raw_input=len(inp_raw)+sum(x['measurements']['native']['bytes'] for x in cert['optional'])
        framing=len(json.dumps(old['original_received']).encode('ascii'))
        cert['original_input_accounting']=dict(source_optional_native_bytes=raw_input,
            optional_path_framing_bytes=framing,source_only_table_Q=table['ledger']['source_bytes'],
            table_certificate_bytes=len(traw),table_required_bytes=table['ledger']['original_source_byte_bound'],
            fixed_library_bytes=library_bytes,complete_interface=interface,interface_bytes=interface_bytes,
            qualification='Optional native packages have no separate supplied image files; every literal image of every nested optional occurrence is checked in complete local, coordinate and joined pairs. No independent NOT/OR input is received.')
        # An explicit very loose polynomial in original paid input, fixed a=4.
        # Interface is charged exactly here; its entries are original strings,
        # bounded-dimension tables, paths and locations, not proof abbreviations.
        Q=raw_input+framing+sum(x['native'] for x in library_bytes.values())
        polynomial=2**100*(Q+2)**1000
        accounted=sum(composed['formats'][m]['proof_and_locations_bytes'] for m in MODES)
        accounted+=table['ledger']['original_source_byte_bound']+interface_bytes
        accounted+=sum(sum(x.values()) for x in library_bytes.values())
        assert accounted <= polynomial
        cert['original_input_accounting'].update(Q=Q,complete_majorized_bytes=accounted,
            polynomial_constant_power_of_two=100,polynomial_exponent=1000,
            polynomial_bound_bits=polynomial.bit_length(),all_charges_within_bound=True)
        assert oldpath.read_bytes() == oldraw and tpath.read_bytes() == traw and inp_path.read_bytes() == inp_raw
        cert.update(complete=True,phase='complete',all_original_files_preserved=True,
            verdict='Exact source-row endpoint and complete native/image chain pass with original-source occurrence accounting.',
            limitations='One empty-zero fixture only; no initial-output identification, nonzero transition, ordinary-input completeness, whole L055, certificate existence or SAT conclusion; separate critical audit pending.')
        save(); print('PASS; failures',cert['failures'],'certificate',dest.relative_to(ROOT),flush=True)
    except BaseException as exc:
        cert['failures'].append(dict(type=type(exc).__name__,message=str(exc))); save(); raise


def source_interface_ledger():
    """Source-only interface majorant; preserve the full replay certificate.

    The main certificate's monomial is a finite diagnostic envelope. This
    supplement pays interface bytes by an a-priori input-based expression,
    rather than using their output measurement to define a uniform bound.
    """
    dest=OUT/'source-interface-ledger.json'
    assert not dest.exists(), 'preserve existing accounting evidence'
    raw=(OUT/'certificate.json').read_bytes(); cert=r.strict_read(raw)
    assert cert['complete'] and cert['failures']==[]
    old=r.strict_read((ROOT/'scripts/left-closure/output/reception-216.json').read_bytes())
    table=r.strict_read((ROOT/'scripts/coefficient-chain/output/empty.json').read_bytes())
    tablecheck.check(table)
    accounting=cert['original_input_accounting']; interface=accounting['complete_interface']
    source_raw=(ROOT/cert['provenance']['input']).read_bytes()
    assert hashlib.sha256(source_raw).hexdigest()==cert['provenance']['input_sha256']
    paths=[dict(native=x['proofs']['native']['measurement']['path'],
                image=x['proofs']['not-or']['measurement']['path']) for x in old['exports']]
    assert interface['coordinates']==paths
    path_bytes=len(json.dumps(paths,separators=(',',':')).encode('ascii'))
    # Each of the five outer fields is an original source object, original
    # optional-path list, subobject of the paid table certificate, fixed path
    # list, or L064(2) locations object. 1024 pays all keys/punctuation.
    table_bound=2**30*(table['ledger']['source_bytes']+2)**(4*table['depth_factor']+12)
    assert table_bound==accounting['table_required_bytes']
    metadata=cert['original_source_chain_ledger']['metadata_bytes']
    framing=len(json.dumps(old['original_received']).encode('ascii'))
    required=len(source_raw)+framing+table_bound+path_bytes+metadata+1024
    actual=len(json.dumps(interface,separators=(',',':')).encode('ascii'))
    assert actual==accounting['interface_bytes']<=required
    assert len(json.dumps(interface['receiving'],separators=(',',':')).encode('ascii'))<=table_bound
    assert len(json.dumps(interface['locations'],separators=(',',':')).encode('ascii'))<=metadata
    nested=[]
    for coord,imp in enumerate(cert['imports']):
        for loc,local in enumerate(old['imports']):
            optional_offset=0
            for opt,package in enumerate(old['original_received']):
                start=imp['start']+local['start']+optional_offset
                nested.append(dict(coordinate=coord,local=loc,optional=opt,start=start,
                    lines=package['lines'],end=start+package['lines']))
                optional_offset+=package['lines']
    assert len(nested)==8 and sum(x['lines'] for x in nested)==40
    library_bytes=sum(sum(x.values()) for x in accounting['fixed_library_bytes'].values())
    total_bound=sum(cert['original_source_chain_ledger']['formats'][m]['proof_and_locations_bytes'] for m in MODES)
    total_bound+=table_bound+required+library_bytes
    actual_total=sum(cert['proofs'][m]['measurement']['bytes']+cert['locations']['bytes'] for m in MODES)
    actual_total+=accounting['table_certificate_bytes']+actual+library_bytes
    assert actual_total<=total_bound
    result=dict(complete=True,failures=[],replay_certificate_sha256=hashlib.sha256(raw).hexdigest(),
        interface_actual_bytes=actual,interface_required_bytes=required,
        interface_input_charges=dict(original_source_bytes=len(source_raw),optional_framing_bytes=framing,
            coefficient_certificate_bound=table_bound,original_coordinate_path_bytes=path_bytes,
            source_bounded_locations_bytes=metadata,outer_framing_bytes=1024),
        nested_optional_occurrences=nested,total_nested_optional_records=40,
        retention_basis='Every optional/local/coordinate/chain field and relocated reference was compared in the complete replay; these offsets are its composed location map, not a new proof premise.',
        full_output_actual_bytes=actual_total,full_output_source_required_bytes=total_bound,
        polynomial_basis='L066(1) into L065(4), then each full coordinate byte/line/depth bound into L064(1)/(2), plus L067 source certificate bound and the displayed input-based interface bound. Fixed admission a=4; no measured generated proof/interface size chooses a bound.',
        diagnostic_qualification='The main certificate monomial envelope is finite-case arithmetic only. Polynomial dependence follows from the cited monotone compositions, with all hypotheses retained.')
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS source-only interface',actual,'<=',required,'bytes; full output',actual_total,'<=',total_bound,
          'bytes; nested optional records',40,'certificate',dest.relative_to(ROOT),flush=True)


if __name__=='__main__':
    if sys.argv[1:]==['--source-interface-ledger-only']: source_interface_ledger()
    else: main()
