"""Inspect this attempt's complete saved evidence; partial output stays partial.

This is not a receiver for an incomplete native stream. Internal checkpoint
replay and byte counts are reported separately from the missing archive pair.
"""
import gzip
import hashlib
import json
import pickle
import sys
import time
import zlib
import coordinate_261 as t

c,h=t.c,t.h
OUT=t.OUT

def expanded(path):
    dec=zlib.decompressobj(31); size=0
    with path.open('rb') as stream:
        while True:
            block=stream.read(2**16)
            if not block: break
            while block:
                got=dec.decompress(block,2**20); size+=len(got)
                block=dec.unconsumed_tail
            while True:
                got=dec.decompress(b'',2**20); size+=len(got)
                if not got: break
    assert not dec.unused_data, 'unexpected concatenated/trailing gzip input'
    return dict(bytes=size,complete_gzip=dec.eof)

def main():
    started=time.monotonic(); assert __debug__
    cert=json.loads((OUT/'certificate.json').read_text())
    monitor=json.loads((OUT/'monitor.json').read_text())
    preflight=json.loads((OUT/'heartbeat-selftest.json').read_text())
    assert preflight['complete'] and preflight['stopped'] and preflight['stop_reason']=='rss'
    assert preflight['exit_code']!=0 and not preflight['failures']
    assert monitor['complete'] and not monitor['failures'] and monitor['samples']>0
    assert monitor['peak_process_tree_rss_bytes']==monitor['parent_peak_rss_bytes']+monitor['worker_peak_rss_bytes']
    assert cert['runtime']['assertions'] is True and cert['small']['complete']
    assert len(cert['small']['counted_fixed_fields'])==15
    assert [a['rows'] for a in cert['small']['normalizer_differentials']]==[117267,117267]
    assert all(a['all_fields_both_formats'] for a in cert['small']['normalizer_differentials'])
    assert len(cert['small']['rejections'])==6 and cert['small']['simultaneous_substitution']
    with gzip.open(OUT/'constructed.pkl.gz','rb') as stream:
        obj=pickle.load(stream); assert stream.read()==b''
    snap=obj['store']; s=c.pool(snap['nodes']); rows=snap['rows']
    assert type(rows) is list and len(rows)==cert['rows_so_far']==1149478
    prefix=[]
    for row in rows: c.replay_row(s,prefix,row); prefix.append(row)
    assert s.text(rows[-1][0])==cert['expected']
    imports=json.loads(json.dumps(cert['imports']))
    # JSON certificates encode these two declared tuple fields as arrays.
    # Restore exactly those schema fields before type-sensitive comparison.
    for segment in imports:
        segment['paths']=tuple(segment['paths'])
        segment['substitutions']=tuple(tuple(pair) for pair in segment['substitutions'])
    assert c.exact(snap['segments'],imports)
    A,B=s.parse('prefix'),s.parse('padding')
    assert rows[0]==(s.ax_ids('ax1',dict(A=A,B=B)),'ax1',(),(('A',A),('B',B)))
    headers=[len(h.enc(dict(format=m,goal=s.text(rows[-1][0],image)))) for m,image in zip(h.MODES,(False,True))]
    counts=headers[:]; counter=t.ByteCount(s); maxima=[0,0]
    for row in rows:
        for mode in (0,1):
            amount=counter.row(row,bool(mode)); counts[mode]+=amount; maxima[mode]=max(maxima[mode],amount)
    assert dict(zip(h.MODES,counts))==cert['complete_prefix_byte_counts']
    assert dict(zip(h.MODES,maxima))==cert['max_serialized_row_bytes']
    envelope=json.loads((h.SOURCE/'source-envelope.json').read_text())
    assert hashlib.sha256((h.SOURCE/'source-envelope.json').read_bytes()).hexdigest()==cert['source_envelope_sha256']
    expected=t.lc.ep.e.c.serialize(t.lc.ep.request(envelope['request'])['closed'][0])
    assert expected==cert['expected']
    # Independent source-index mapping checks every retained local occurrence
    # without expanding its formula text or trusting destination IDs as source IDs.
    with gzip.open(t.ROOT/'scripts/output-zero/output/interned-255/packages.pkl.gz','rb') as stream:
        sources=pickle.load(stream); assert stream.read()==b''
    locations=[]
    for occurrence,(source,seg) in enumerate(zip(sources,snap['segments'])):
        mapping=[]
        for node in source['nodes']:
            tag,*args=node
            mapping.append(s.node(tag,*(args if tag=='v' else [mapping[j] for j in args])))
        assert seg['paths']==source['paths'] and seg['count']==len(source['rows'])
        for local,(f,r,refs,subs) in enumerate(source['rows']):
            moved=(mapping[f],r,tuple(seg['start']+k for k in refs),tuple((k,mapping[v]) for k,v in subs))
            assert c.exact(rows[seg['start']+local],moved)
            locations.append((occurrence,seg['paths'],local,seg['start']+local))
    assert len(sources)==len(snap['segments'])==6 and c.exact(locations,snap['locations'])
    assert len(locations)==155588
    # Correct the fixed-prefix name charge while preserving the executed ledger.
    original=cert['original_input_ledger']
    inputs=[seg['checked']|dict(rows=range(seg['count'])) for seg in snap['segments']]
    fixed=dict(rows=[rows[0]],node_sums={},depths={},name_bytes=7)
    fields=[rows[0][0]]+[v for k,v in rows[0][3]]
    term_stats={}
    for mode,off in zip(h.MODES,(0,2)):
        fm=original['formats'][mode]; assert fm['payload_bytes']==1
        fixed['node_sums'][mode]=sum(s.stats[j][off] for j in fields)
        fixed['depths'][mode]=max(s.stats[j][off+1] for j in fields)
        term_stats[mode]=(fm['input_term_nodes'],fm['input_term_depth'],1)
    constants=json.loads((t.ROOT/'scripts/left-closure/output/certificate-202.json').read_text())['constants']
    corrected=t.lc.thresholds(envelope['request'],inputs+[fixed],constants,term_stats,7)
    assert corrected['imported_records']==155589
    for mode in h.MODES:
        fm=corrected['formats'][mode]
        assert len(rows)<=fm['lines'] and counts[h.MODES.index(mode)]<=fm['bytes']
    gz={path.name:expanded(path) for path in OUT.glob('*.gz')}
    storage=sum(path.stat().st_size for path in OUT.iterdir() if path.is_file())
    out=dict(complete=True,target_complete=cert['target_complete'],failures=[],
        construction_internal_only=True,primitive_checkpoint_rows=len(rows),retained_local_rows=len(locations),
        generated_rows_including_prefix=len(rows)-len(locations),exact_independently_rebuilt_endpoint=True,
        counts_both_complete_proposed_formats=dict(zip(h.MODES,counts)),max_record_bytes=dict(zip(h.MODES,maxima)),
        expanded_new_gzip=gz,expanded_actual=sum(a['bytes'] for a in gz.values()),
        observed_artifact_bytes_before_inspector=storage,corrected_original_input_ledger=corrected,
        prefix_payload_correction='Initial ledger omitted the fixed prefix: charge its one known axiom and all fields as a fixed constant input, and use B=7. No generated size becomes an input parameter; no proof row changed.',
        production_monitor=monitor,preflight=preflight,
        inspection_runtime=dict(python=sys.version,assertions=__debug__),inspection_seconds=time.monotonic()-started,
        limitation='Checkpoint primitive checks and exact output counts do not supply complete native/image archives or their full replay.')
    assert out['expanded_actual']<t.CAP['expanded']
    assert storage<t.CAP['artifacts']
    assert not cert['target_complete'] or all(gz[f'coordinate-0.{mode}.jsonl.gz']['complete_gzip'] for mode in h.MODES)
    path=OUT/'inspection.json'; assert not path.exists(); path.write_text(json.dumps(out,indent=2)+'\n')
    s.close()
    print('RESULT internal construction checked; target complete',cert['target_complete'],'checkpoint rows',len(rows),'local occurrences',len(locations))
    print('complete proposed native/image bytes',counts,'/',t.CAP['expanded'],'combined',sum(counts))
    print('expanded gzip bytes actually available',out['expanded_actual'],'/',t.CAP['expanded'])
    print('monitor time',monitor['elapsed_seconds'],'stop',monitor.get('stop_reason'),'RSS',monitor['peak_process_tree_rss_bytes'],'/',t.CAP['rss'])
    print('failures',out['failures'],'evidence',path.relative_to(t.ROOT))

if __name__=='__main__': main()
