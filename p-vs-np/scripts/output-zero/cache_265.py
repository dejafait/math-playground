"""One compiler-free bounded-cache trial; never exports a production pair.

Executed only by watch_cache_265 through the child-denying rss_worker_255.
Trusted local pickle remains a qualification. Assertions are required.
"""
import gc
import gzip
import hashlib
import io
import json
import os
import pickle
import resource
import sys
import time
import zlib
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT/'scripts/output-zero/output/cache-265'
OLD = ROOT/'scripts/output-zero/output/coordinate-261'
DEADLINE = float(os.environ['CACHE265_DEADLINE'])
EXPANDED = 0
DIFFERENTIAL = 0
BENCHMARK = 0
CAP = dict(rss=2147483648, rss_stop=1610612736, seconds=600,
           artifacts=17179869184, expanded=137438953472,
           differential=268435456, benchmark=1073741824)


def check_time():
    if time.monotonic() >= DEADLINE-15:
        raise RuntimeError('absolute deadline reporting reserve')


def charge(n, kind=None):
    global EXPANDED, DIFFERENTIAL, BENCHMARK
    assert type(n) is int and n >= 0
    EXPANDED += n
    kinds = (kind,) if type(kind) is not tuple else kind
    if 'differential' in kinds: DIFFERENTIAL += n
    if 'benchmark' in kinds: BENCHMARK += n
    assert EXPANDED <= CAP['expanded'], 'expanded limit'
    assert DIFFERENTIAL <= CAP['differential'], 'differential limit'
    assert BENCHMARK <= CAP['benchmark'], 'benchmark limit'
    check_time()


def peak():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform=='darwin' else 1024)


def reject(label, call, evidence):
    try:
        call()
    except (AssertionError, ValueError, TypeError, RuntimeError, OSError, zlib.error, EOFError) as e:
        evidence.append(dict(case=label, error=type(e).__name__+': '+str(e)))
    else:
        raise AssertionError('accepted corruption: '+label)


class Spelling:
    """Fixed owner/mode, bounded LRU; active frames own child string values.

    The validated pool is frozen to tuples before construction. Along a DFS
    path, held completed left subtrees are disjoint occurrences in the root,
    so their total text length is at most the root length. An eviction never
    changes those local references. The cache has no all-node text memo.
    """
    def __init__(self, s, lengths, image, limit=33554432, entries=32768):
        assert type(image) is bool and type(s.nodes) is tuple and s.pool
        assert 0 <= limit <= 33554432 and 0 <= entries <= 32768
        self.s, self.nodes, self.lengths, self._image = s, s.nodes, lengths, image
        self.limit, self.entries = limit, entries
        self.cache = OrderedDict()
        self.bytes = self.hits = self.misses = self.evictions = self.skipped = 0
        self.max_bytes = self.max_entries = self.max_frames = 0

    @property
    def image(self):
        return self._image

    def clear(self):
        self.cache.clear(); self.bytes = 0

    def insert(self, j, value):
        assert type(value) is str and len(value)==self.lengths[j][self.image]
        if j in self.cache: self.bytes -= len(self.cache.pop(j))
        if len(value)>self.limit or not self.entries:
            self.skipped += 1; return
        while self.cache and (self.bytes+len(value)>self.limit or len(self.cache)>=self.entries):
            _, old = self.cache.popitem(last=False)
            self.bytes -= len(old); self.evictions += 1
        self.cache[j] = value; self.bytes += len(value)
        self.max_bytes = max(self.max_bytes,self.bytes)
        self.max_entries = max(self.max_entries,len(self.cache))
        assert self.bytes<=self.limit and len(self.cache)<=self.entries

    def text(self, term):
        assert self.s.nodes is self.nodes and self.s.pool, 'mutated/closed owner'
        j = c.owned(term,self.s)
        stack = [[j,0,None]]; value = None
        while stack:
            self.max_frames = max(self.max_frames,len(stack))
            frame = stack[-1]; k,stage,left = frame
            node = self.nodes[k]; tag = node[0]
            if stage == 0:
                if k in self.cache:
                    self.hits += 1; value = self.cache[k]; self.cache.move_to_end(k)
                    stack.pop(); continue
                self.misses += 1
                if tag == 'v': value = node[1]
                else:
                    frame[1] = 1; stack.append([node[1],0,None]); continue
            elif tag == 'n': value = '(~'+value+')'
            elif stage == 1:
                frame[1] = 2; frame[2] = value
                stack.append([node[2],0,None]); continue
            else:
                value = ('((~'+left+')|'+value+')') if self.image else ('('+left+'>'+value+')')
            self.insert(k,value); stack.pop()
        return value

    def statistics(self):
        return {k:getattr(self,k) for k in ('bytes','hits','misses','evictions','skipped',
                'max_bytes','max_entries','max_frames')}


def admit(s, lengths, fields, size):
    """Conservative extra workspace, checked before rendering any field.

    Fields retained simultaneously total <= size ASCII characters. DFS held
    left values total <= current root length; concatenation temporaries add
    <= 3 root lengths. Oracle spelling's parts list has <= size entries and
    its pending stack <= 4*depth; list overallocation is paid at 16 bytes per
    entry. JSON/ASCII/decoder/comparison copies and join buffers are overpaid
    by the remaining 64*size allowance. Per-frame 1024*depth covers list/int
    references and loop temporaries. Cache payload is <=32 MiB, and 512 bytes
    per entry pays its string header, key and OrderedDict bookkeeping. A
    further 64 MiB pays gzip/decoder buffers and interpreter slack. This is
    fail-closed admission plus sampled RSS, not a hard memory theorem.
    """
    depth = max(s.stats[j][3] for j in fields)
    assert depth<=4096, 'parser depth qualification'
    workspace = 64*size+1024*(depth+1)+33554432+512*32768+64*2**20
    parent = int(os.environ.get('CACHE265_PARENT_PEAK','0'))
    assert peak()+parent+workspace < CAP['rss_stop'], 'conservative live-workspace admission'
    check_time()
    return workspace


def strict_gunzip(blob):
    d = zlib.decompressobj(31); result = bytearray()
    # Tiny reads deliberately exercise input arriving after gzip EOF.
    for start in range(0,len(blob),8192):
        block = blob[start:start+8192]
        assert not d.eof, 'input after completed gzip member'
        while block:
            got = d.decompress(block,2**20); charge(len(got),'differential'); result.extend(got)
            assert not d.unused_data, 'extra member/trailing input'
            block = d.unconsumed_tail
    while True:
        got = d.decompress(b'',2**20); charge(len(got),'differential'); result.extend(got)
        if not got: break
    assert d.eof and not d.unused_data and not d.unconsumed_tail, 'truncated gzip'
    return bytes(result)


def header(s,goal,image,spell=None):
    return h.enc(dict(format=h.MODES[image],goal=(spell.text(c.term(s,goal)) if spell else s.text(goal,image))))


def raw_record(s,row,image,spell=None):
    if spell is None: return h.enc(h.Package(s,row[0],[],(),{}).record(row,image))
    f,rule,refs,subs = row
    obj = dict(f=spell.text(c.term(s,f)),rule=rule)
    if rule=='mp': obj['refs']=list(refs)
    else: obj['subs']={k:spell.text(c.term(s,v)) for k,v in subs}
    return h.enc(obj)


def restore(cert):
    """The generated-tail inspect_261 contract, with explicit external inputs."""
    old = json.loads((OLD/'certificate.json').read_text())
    inspected = json.loads((OLD/'inspection.json').read_text())
    assert inspected['complete'] and not inspected['failures']
    envelope_path = h.SOURCE/'source-envelope.json'
    assert hashlib.sha256(envelope_path.read_bytes()).hexdigest()==old['source_envelope_sha256']
    envelope = json.loads(envelope_path.read_text())
    expected = t.lc.ep.e.c.serialize(t.lc.ep.request(envelope['request'])['closed'][0])
    assert old['expected']==expected and envelope['request']['q']=='x'
    path = OLD/'constructed.pkl.gz'
    with gzip.open(path,'rb') as stream:
        data = stream.read(); charge(len(data)); obj = pickle.loads(data)
    assert type(obj) is dict and set(obj)=={'store','adapter'}
    snap = obj['store']
    assert type(snap) is dict and set(snap)=={'version','nodes','rows','locations','segments'}
    assert type(snap['version']) is int and snap['version']==1
    s = c.pool(snap['nodes']); rows = snap['rows']
    assert type(rows) is list and len(rows)==1149478==old['rows_so_far']
    prefix=[]
    for j,row in enumerate(rows):
        c.replay_row(s,prefix,row); prefix.append(row)
        if j%8192==0: check_time()
    assert s.text(rows[-1][0])==expected
    imports=json.loads(json.dumps(old['imports']))
    for seg in imports:
        seg['paths']=tuple(seg['paths']); seg['substitutions']=tuple(tuple(x) for x in seg['substitutions'])
    assert c.exact(snap['segments'],imports)
    A,B=s.parse('prefix'),s.parse('padding')
    assert rows[0]==(s.ax_ids('ax1',dict(A=A,B=B)),'ax1',(),(('A',A),('B',B)))
    with gzip.open(ROOT/'scripts/output-zero/output/interned-255/packages.pkl.gz','rb') as stream:
        data=stream.read(); charge(len(data)); sources=pickle.loads(data)
    assert len(sources)==len(imports)==6
    locations=[]; start=1
    for occurrence,(source,seg) in enumerate(zip(sources,imports)):
        assert seg['start']==start and seg['root']==start+seg['count']-1
        mapping=[]
        for node in source['nodes']:
            tag,*args=node
            mapping.append(s.node(tag,*(args if tag=='v' else [mapping[x] for x in args])))
        assert seg['paths']==source['paths'] and seg['count']==len(source['rows'])
        for local,(f,r,refs,subs) in enumerate(source['rows']):
            moved=(mapping[f],r,tuple(start+x for x in refs),tuple((k,mapping[v]) for k,v in subs))
            assert c.exact(rows[start+local],moved)
            assert all(start<=r<start+local for r in rows[start+local][2])
            locations.append((occurrence,seg['paths'],local,start+local))
        assert rows[seg['root']][0]==seg['goal'] and s.text(seg['goal'])==seg['source_goal']
        start+=seg['count']; check_time()
    assert start==155589 and c.exact(locations,snap['locations']) and len(locations)==155588
    counter=t.ByteCount(s); counter.sync(); totals=[0,0]; maxima=[(-1,-1),(-1,-1)]
    headers=[len(header(s,rows[-1][0],m)) for m in (False,True)]
    for i,row in enumerate(rows):
        for m in (False,True):
            n=counter.row(row,m); totals[m]+=n
            if n>maxima[m][1]: maxima[m]=(i,n)
        if i%8192==0: check_time()
    assert dict(zip(h.MODES,[x+y for x,y in zip(headers,totals)]))==old['complete_prefix_byte_counts']
    assert dict(zip(h.MODES,[x[1] for x in maxima]))==inspected['max_record_bytes']
    # Recompute the corrected fixed-prefix ledger, using original source inputs.
    original=old['original_input_ledger']; fixed=dict(rows=[rows[0]],node_sums={},depths={},name_bytes=7)
    term_stats={}; fields=[rows[0][0]]+[v for k,v in rows[0][3]]
    for mode,off in zip(h.MODES,(0,2)):
        fm=original['formats'][mode]
        fixed['node_sums'][mode]=sum(s.stats[j][off] for j in fields)
        fixed['depths'][mode]=max(s.stats[j][off+1] for j in fields)
        term_stats[mode]=(fm['input_term_nodes'],fm['input_term_depth'],1)
    constants=json.loads((ROOT/'scripts/left-closure/output/certificate-202.json').read_text())['constants']
    inputs=[seg['checked']|dict(rows=range(seg['count'])) for seg in imports]
    ledger=t.lc.thresholds(envelope['request'],inputs+[fixed],constants,term_stats,7)
    assert c.exact(ledger,inspected['corrected_original_input_ledger'])
    for m,mode in enumerate(h.MODES):
        assert len(rows)<=ledger['formats'][mode]['lines']
        assert headers[m]+totals[m]<=ledger['formats'][mode]['bytes']
    cert['restore']=dict(all_primitive_rows=len(rows),external_source_occurrences=len(locations),
        generated_tail_rows=len(rows)-start,exact_endpoint=True,corrected_ledger=ledger,
        totals=dict(zip(h.MODES,[x+y for x,y in zip(headers,totals)])),maxima=maxima,
        checkpoint_sha256=hashlib.sha256(path.read_bytes()).hexdigest())
    del obj,snap,data,sources,prefix,locations; gc.collect()
    return s,rows,counter,maxima


def small_tests(cert):
    evidence=[]; s=c.pool([('v','A'),('n',0),('i',1,1)])
    s.nodes=tuple(s.nodes); s.stats=tuple(s.stats)
    counter=t.ByteCount(s); counter.sync(); lengths=tuple(counter.lengths)
    other=c.pool([('v','A')]); other.nodes=tuple(other.nodes)
    for image in (False,True):
        spell=Spelling(s,lengths,image,limit=7,entries=1)
        for j in (2,0,2,1,2): assert spell.text(c.term(s,j))==s.text(j,image)
        assert spell.evictions and spell.skipped and spell.max_bytes<=7 and spell.max_entries<=1
        # Oversized parent with repeated children exercises eviction-safe locals.
        spell.insert(0,'A'); spell.insert(0,'A'); assert spell.bytes==1
        spell.clear(); assert spell.bytes==0 and not spell.cache
        for name,value in [('bool',True),('float',0.0),('negative',-1),('range',3)]:
            reject(name,lambda value=value:spell.text(c.Term(s,value)),evidence)
        reject('foreign-owner',lambda:spell.text(c.term(other,0)),evidence)
        reject('bare-index',lambda:spell.text(0),evidence)
    reject('mode-type',lambda:Spelling(s,lengths,1),evidence)
    # Construct admitted parser-depth-4096 syntax without Python recursion.
    deep=c.pool([('v','q')]+[('n',i) for i in range(4095)])
    deep.nodes=tuple(deep.nodes); deep.stats=tuple(deep.stats)
    dc=t.ByteCount(deep); dc.sync()
    for image in (False,True):
        spell=Spelling(deep,tuple(dc.lengths),image,limit=16,entries=2)
        admit(deep,dc.lengths,[4095],dc.lengths[4095][image])
        assert spell.text(c.term(deep,4095))==deep.text(4095,image)
        assert spell.max_frames==4096
        assert spell.text(c.term(deep,2))=='(~(~q))'
    dead=Spelling(other,((1,1),),False); other.close()
    reject('closed-owner',lambda:dead.text(c.Term(other,0)),evidence)
    s.close(); deep.close()
    # Strict member/checksum/trailing tests and sink errors, including close.
    good=gzip.compress(b'valid\n',compresslevel=1,mtime=0); charge(6)
    assert strict_gunzip(good)==b'valid\n'
    for name,bad in [('truncated',good[:-1]),('checksum',good[:-8]+bytes([good[-8]^1])+good[-7:]),
                     ('extra-member',good+good),('trailing',good+b'x')]:
        reject(name,lambda bad=bad:strict_gunzip(bad),evidence)
    class Broken(io.BytesIO):
        fail=False
        def write(self,b):
            if self.fail:
                self.fail=False
                raise OSError('injected sink write failure')
            return super().write(b)
    sink=Broken(); stream=gzip.GzipFile(fileobj=sink,mode='wb',compresslevel=1)
    sink.fail=True
    def write_flush():
        stream.write(b'payload'); stream.flush()
    reject('sink-write-flush',write_flush,evidence)
    try: stream.close()
    except OSError: pass
    class CloseBroken(io.BytesIO):
        fail=False
        def write(self,b):
            if self.fail:
                self.fail=False
                raise OSError('injected gzip close failure')
            return super().write(b)
    sink=CloseBroken(); stream=gzip.GzipFile(fileobj=sink,mode='wb',compresslevel=1)
    stream.write(b'x'); sink.fail=True; reject('gzip-close',stream.close,evidence); charge(1)
    cert['small']=dict(rejections=evidence,depth4096=True,eviction_recomputation=True,
                       mode_separation=True,double_negations=True)


def select(rows,counter,maxima):
    n=len(rows); windows=[('begin',list(range(4))),('middle',list(range(n//2,n//2+4))),
                         ('end',list(range(n-4,n)))]
    for m,(i,_) in enumerate(maxima): windows.append(('maximum-'+str(m),list(range(max(0,i-1),min(n,i+2)))))
    first={}; duplicate=None; seen={}
    for i,row in enumerate(rows[:8192]):
        first.setdefault(row[1],i)
        if duplicate is None and row in seen: duplicate=(seen[row],i)
        if duplicate is None: seen[row]=i
        if len(first)==4 and duplicate is not None: break
    assert set(first)=={'ax1','ax2','ax3','mp'} and duplicate is not None
    windows.append(('all-rules',list(first.values())))
    windows.append(('repeated-row',list(duplicate)))
    # Every window preserves original global indices, even repeated selections.
    prospective=0
    for _,indices in windows:
        prospective+=sum(counter.row(rows[i],m) for i in indices for m in (False,True))*6
    assert prospective<210*2**20, 'differential selection admission'
    return windows


def primitive_corruptions(s,rows,cert):
    evidence=[]
    ax=next(row for row in rows if row[1]=='ax1')
    mp=next((i,row) for i,row in enumerate(rows) if row[1]=='mp')
    class Prefix:
        def __len__(self): return mp[0]
        def __getitem__(self,j): return rows[j]
    def receive(native,image,prefix):
        # The actual native receiver enforces schemas, formula and references;
        # the type-sensitive complete image comparison enforces literal images.
        row=h.check_row(s,prefix,h.replay.strict_read(h.enc(native)))
        assert c.exact(h.replay.strict_read(h.enc(image)),h.Package(s,row[0],[],(),{}).record(row,True))
    native_ax=json.loads(raw_record(s,ax,False)); image_ax=json.loads(raw_record(s,ax,True))
    native_mp=json.loads(raw_record(s,mp[1],False)); image_mp=json.loads(raw_record(s,mp[1],True))
    receive(native_ax,image_ax,[]); receive(native_mp,image_mp,Prefix())
    for image in (False,True):
        obj=json.loads(raw_record(s,ax,image))
        for label,changed in [('extra',obj|dict(extra=0)),('missing',{k:v for k,v in obj.items() if k!='f'}),
                              ('formula',obj|dict(f='bad')),('image',obj|dict(f='(~bad)'))]:
            def test(changed=changed,image=image):
                receive(native_ax if image else changed,changed if image else image_ax,[])
            reject(str(image)+'-'+label,test,evidence)
        for name,value in [('boolean',True),('float',0.0),('forward',mp[0])]:
            changed=json.loads(raw_record(s,mp[1],image)); changed['refs'][0]=value
            def test(changed=changed,image=image):
                receive(native_mp if image else changed,changed if image else image_mp,Prefix())
            reject(str(image)+'-'+name,test,evidence)
        changed=json.loads(raw_record(s,ax,image)); changed['subs']['A']='bad'
        reject(str(image)+'-substitution',lambda:receive(native_ax if image else changed,
               changed if image else image_ax,[]),evidence)
    cert['record_rejections']=evidence


def experiment(cert):
    # Conservative reserve for all small-test and endpoint/schema serializations
    # (each has bounded tiny fields), separate from counted large record output.
    charge(2**20,'differential')
    cert['small_and_metadata_expanded_reserve_bytes']=2**20
    small_tests(cert); save(cert)
    s,rows,counter,maxima=restore(cert); save(cert)
    windows=select(rows,counter,maxima)
    cert['selection']=dict(valid_prefix=list(range(64)),windows=[dict(name=name,indices=idx) for name,idx in windows],
        rules=sorted({rows[i][1] for _,idx in windows for i in idx}),both_maximum_rows=True,
        q='x',disconnected_windows='record tests only; no proof or renumbering claim')
    save(cert)
    primitive_corruptions(s,rows,cert)
    # Complete valid prefix replay in both formats, using actual native receiver.
    rs=h.Syntax(); retained=[]; prefix_bytes=[0,0]
    for i,row in enumerate(rows[:64]):
        native=json.loads(raw_record(s,row,False)); image=json.loads(raw_record(s,row,True))
        charge(len(h.enc(native))+len(h.enc(image)),'differential')
        received=h.check_row(rs,retained,native); retained.append(received)
        assert c.exact(image,h.Package(rs,received[0],[],(),{}).record(received,True))
        prefix_bytes[0]+=len(h.enc(native)); prefix_bytes[1]+=len(h.enc(image))
    assert rs.text(retained[-1][0])==s.text(rows[63][0]); rs.close()
    cert['valid_prefix']=dict(records=64,complete_primitive_replay=True,bytes=prefix_bytes,endpoint=s.text(rows[63][0]))
    s.nodes=tuple(s.nodes); s.stats=tuple(s.stats); lengths=tuple(counter.lengths)
    comparisons=[]; timings={m:dict(baseline=0.,adapted=0.) for m in h.MODES}
    for image,mode in enumerate(h.MODES):
        for name,indices in windows:
            check_time(); goal=rows[indices[-1]][0]
            initial_header=header(s,goal,bool(image)); charge(len(initial_header),'differential')
            expected_size=len(initial_header)+sum(counter.row(rows[i],bool(image)) for i in indices)
            largest=max(counter.row(rows[i],bool(image)) for i in indices)
            assert DIFFERENTIAL+6*expected_size<=CAP['differential']
            assert BENCHMARK+2*expected_size<=CAP['benchmark']
            # Reserve all field/JSON/oracle/gzip/comparison allocations before both runs.
            workspace=max(admit(s,lengths,[rows[i][0]]+[v for k,v in rows[i][3]],largest) for i in indices)
            variants=[]
            for adapted in (False,True):
                sink=io.BytesIO(); started=time.perf_counter()
                spell=Spelling(s,lengths,bool(image)) if adapted else None
                size=0
                with gzip.GzipFile(fileobj=sink,mode='wb',compresslevel=1,mtime=0) as gz:
                    raw=header(s,goal,bool(image),spell); gz.write(raw); size+=len(raw)
                    for i in indices:
                        raw=raw_record(s,rows[i],bool(image),spell); gz.write(raw); size+=len(raw)
                elapsed=time.perf_counter()-started
                charge(size,('benchmark','differential')); assert size==expected_size
                blob=sink.getvalue(); charge(len(blob))
                path=OUT/(name+'.'+mode+('.adapted' if adapted else '.baseline')+'.jsonl.gz')
                path.write_bytes(blob)
                variants.append((blob,elapsed,spell.statistics() if spell else None))
                timings[mode]['adapted' if adapted else 'baseline']+=elapsed
            left=strict_gunzip(variants[0][0]); right=strict_gunzip(variants[1][0])
            assert left==right and len(left)==expected_size, 'complete reinflated bytes'
            # Full every-field checks and exact header; no preview/hash substitutes.
            records=right.splitlines(keepends=True)
            final_header=header(s,goal,bool(image)); charge(len(final_header),'differential')
            assert records[0]==final_header
            for i,raw in zip(indices,records[1:]):
                want=raw_record(s,rows[i],bool(image)); charge(len(want),'differential')
                assert raw==want and c.exact(h.replay.strict_read(raw),h.replay.strict_read(want))
            assert len(records)==len(indices)+1
            comparisons.append(dict(window=name,format=mode,indices=indices,bytes=expected_size,
                baseline_seconds=variants[0][1],adapted_seconds=variants[1][1],cache=variants[1][2],
                workspace_admission_bytes=workspace,all_reinflated_bytes_equal=True,
                sha256=hashlib.sha256(left).hexdigest()))
            cert.update(comparisons=comparisons,timings=timings); save(cert)
            del variants,left,right,records,spell,sink,blob; gc.collect()
            print('CHECK',mode,name,expected_size,'bytes',flush=True)
        timings[mode]['ratio']=timings[mode]['baseline']/timings[mode]['adapted']
    cert['timings']=timings
    s.close()
    assert all(x['ratio']>=2 for x in timings.values()), 'aggregate speedup below required two in at least one format'
    cert.update(target_complete=True,status='PASS')


def save(cert):
    cert.update(expanded_actual=EXPANDED,differential_expanded=DIFFERENTIAL,benchmark_expanded=BENCHMARK,
                worker_peak_rss_bytes=peak(),last_monotonic=time.monotonic())
    (OUT/'certificate.json').write_text(json.dumps(cert,indent=2)+'\n')


def main():
    global c,h,t
    assert __debug__
    mode=os.environ.get('CACHE265_TEST','main')
    if mode=='stall':
        sys.setswitchinterval(5); end=time.monotonic()+3
        while time.monotonic()<end: pass
        return
    if mode=='output':
        (OUT/'output-selftest.bin').write_bytes(b'x'*(2*2**20)); time.sleep(3); return
    if mode=='terminal':
        # Unit injection exercises the terminal receipt path, without a real oversized allocation.
        os.write(int(sys.argv[1]) if len(sys.argv)>1 else int(os.environ['CACHE265_HEARTBEAT_FD']),b'1610612736\n')
        return
    binary=ROOT/'scripts/left-closure/output/native_parser-207.so'
    assert binary.is_file(), 'existing parser unavailable; rebuilding is forbidden'
    check_time()
    import coordinate_261 as t
    c,h=t.c,t.h
    cert=dict(step=265,status='INCOMPLETE',target_complete=False,failures=[],caps=CAP,
        runtime=dict(python=sys.version,assertions=__debug__),deadline_monotonic=DEADLINE,
        parser_sha256=hashlib.sha256(binary.read_bytes()).hexdigest(),compiler_invoked=False,
        qualification='trusted local pickle; fixed ASCII keys; immutable owned pools; parser depth <=4096; sampled child-free RSS')
    save(cert)
    try: experiment(cert)
    except BaseException as error:
        cert.update(status='STOPPED',failures=[type(error).__name__+': '+str(error)])
        raise
    finally: save(cert)


if __name__=='__main__': main()
