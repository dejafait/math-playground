"""Step 502: exact explicit L110 transport sizing, without word or row search.

Fresh output only. Original archives and engines are read-only. A successful
result sizes a representation; it is not an equality or coordinate receipt.
"""
from collections import Counter, deque
from pathlib import Path
import ast
import hashlib
import inspect
import json
import resource
import sys
import time
import parameterized_input as p

HERE = Path(__file__).resolve().parent
OUT = HERE / 'output-502'
TARGET = "Preflight L110's fixed job-7 graph/reference transports and evidence framing under the unchanged caps, without coordinate search or path-word expansion."
REVIEW = 'drafts/literature/2026-10-25-job7-coefficient-transport-preflight.md'
EXPECTED_CAPS = dict(records=2_000_000, certificate_bytes=200_000_000,
    polynomial_words=1_000_000, word_length=256, multiplication_pairs=100_000_000,
    stored_words=20_000_000, input_bytes=2_000_000, tree_depth=64, json_depth=160,
    tree_nodes=100_000, source_lines=10_000, alphabet=256, dictionary_entries=32_896,
    label_entries=2_000_000, label_width=1024, name_bytes=4096)
BIND_PATHS = [
    'output-493/restricted-boolean.json',
    'output-493/restricted-interior-bound.json',
    'output-491/retained-interior-bound.json',
    'output-489/inputs/proof.jsonl', 'output-489/inputs/request.json',
    'output-495/reception.failure.json',
    'output-489/trace/event-02642.json', 'output-489/trace/event-02643.json']
LAYOUT = ['format', 'alphabet', 'dictionary', 'symbol_transport', 'source_binding',
          'whole_operand_maps', 'selected_occurrences', 'reference_copies',
          'product_copies', 'base_graphs', 'mode_transports', 'comparisons']


class Stop(Exception):
    def __init__(self, kind, details):
        self.kind, self.details = kind, details
        super().__init__(str(details))


class Run:
    def __init__(self):
        self.start = time.monotonic()
        self.stage = 'manifest'
        self.visits = 0
        self.by_stage = Counter()
        self.times = []
        self.last_time = self.start
        self.graphs = []
        self.sections = []
        self.raw_manifest = []
        self.serialized_buffer_peak = 0
        self.integer_bits = 1
        self.reach_operations = Counter()
        self.reach_bit_upper = 0
        self.binding = None
        self.transport = None
        self.dimensions = 'UNKNOWN'
        self.checks = []
        self.source_observer = Counter()

    def tick(self, n=1):
        if self.visits+n > 100_000_000:
            raise Stop('ADMINISTRATIVE', dict(resource='item_visits', actual=self.visits+n,
                required=100_000_000, stage=self.stage))
        self.visits += n
        self.by_stage[self.stage] += n
        self.integer_bits = max(self.integer_bits, self.visits.bit_length())

    def timer(self):
        elapsed = time.monotonic()-self.start
        if elapsed > 900:
            raise Stop('ADMINISTRATIVE', dict(resource='seconds', actual=elapsed,
                required=900, stage=self.stage))

    def at(self, stage):
        now = time.monotonic()
        self.times.append(dict(stage=self.stage, seconds=now-self.last_time))
        self.last_time, self.stage = now, stage
        self.timer()
        print(json.dumps(dict(stage=stage, item_visits=self.visits,
                              elapsed_seconds=now-self.start)), flush=True)

    def items(self, xs):
        for x in xs:
            self.tick()
            if self.visits % 4096 == 0:
                self.timer()
            yield x

    def eq(self, a, b):
        self.tick()
        if type(a) is not type(b):
            return False
        if type(a) is dict:
            return a.keys() == b.keys() and all(self.eq(a[k], b[k]) for k in a)
        if type(a) is list:
            return len(a) == len(b) and all(self.eq(x,y) for x,y in zip(a,b))
        return a == b

    def walk(self, value):
        self.tick()
        if type(value) is dict:
            for key, child in value.items():
                self.tick()  # consumed key
                self.walk(child)
        elif type(value) is list:
            for child in value:
                self.walk(child)

    def chunks(self, x):
        self.tick()
        if type(x) is dict:
            yield '{'
            for i,(key,child) in enumerate(x.items()):
                if i: yield ','
                yield from self.chunks(key)
                yield ':'
                yield from self.chunks(child)
            yield '}'
        elif type(x) is list:
            yield '['
            for i,child in enumerate(x):
                if i: yield ','
                yield from self.chunks(child)
            yield ']'
        elif type(x) is str:
            yield '"'
            for offset in range(0, len(x), 65536):
                # Independent escaped chunks inside one JSON string; splitting
                # before encoding cannot split an encoded escape sequence.
                self.timer()
                yield json.dumps(x[offset:offset+65536], ensure_ascii=True)[1:-1]
            yield '"'
        else:
            p.require(x is None or type(x) in (bool,int), 'strict transport JSON scalar')
            yield json.dumps(x, ensure_ascii=True, separators=(',',':'))

    def count(self, value, name, previous=0):
        size = 0
        for index, chunk in enumerate(self.chunks(value)):
            data = chunk.encode('utf-8')
            self.serialized_buffer_peak = max(self.serialized_buffer_peak, len(data))
            actual = previous+size+len(data)
            if actual > p.CAPS['certificate_bytes']:
                raise Stop('MANDATORY_CAP', dict(resource='certificate_bytes', section=name,
                    complete_previous_bytes=previous, completed_chunk_bytes=size,
                    chunk_index=index, chunk_bytes=len(data),
                    rejected_byte_in_chunk=p.CAPS['certificate_bytes']-previous-size+1,
                    first_rejected_prefix=p.CAPS['certificate_bytes']+1,
                    required=p.CAPS['certificate_bytes'], full_proposed_size='UNKNOWN'))
            size += len(data)
            if index % 4096 == 0: self.timer()
        self.sections.append(dict(name=name, bytes=size, previous_bytes=previous))
        return size


R = None


def graph(n=2, edges=None, s=0, t=1):
    return dict(vertices=n, source=s, sink=t, edges=[] if edges is None else edges)


def append_edge(g, u, v, lab):
    R.tick()
    nrec = g['vertices']+len(g['edges'])+1
    if nrec > p.CAPS['records']:
        raise Stop('MANDATORY_CAP', dict(resource='records', actual=nrec,
            required=p.CAPS['records'], stage=R.stage, full_size='UNKNOWN'))
    g['edges'].append([u,v,list(R.items(lab))])


def copy(g, child, s=None, t=None):
    offset = g['vertices']
    total = offset+child['vertices']+len(g['edges'])+len(child['edges'])
    if total > p.CAPS['records']:
        raise Stop('MANDATORY_CAP', dict(resource='records', actual=total,
            required=p.CAPS['records'], stage=R.stage, full_size='UNKNOWN'))
    begin = len(g['edges'])
    for _ in R.items(range(child['vertices'])): pass
    g['vertices'] += child['vertices']
    for u,v,lab in R.items(child['edges']): append_edge(g,u+offset,v+offset,lab)
    return dict(vertex_range=[offset,g['vertices']], edge_range=[begin,len(g['edges'])],
        entry=offset+(child['source'] if s is None else s),
        exit=offset+(child['sink'] if t is None else t))


def product(children):
    g = graph(); last = 0; maps = []
    for child in R.items(children):
        m = copy(g,child); maps.append(m)
        append_edge(g,last,m['entry'],['1']); last=m['exit']
    append_edge(g,last,1,['1'])
    return g,maps


def translation(t, alphabet):
    R.tick()
    if type(t) is str:
        return ['scalar',int(t=='false')] if t in ('true','false') else ['original',alphabet.index(t)]
    a = translation(t[1],alphabet)
    if t[0]=='not':
        return ['scalar',1^a[1]] if a[0]=='scalar' else ['one-plus',a]
    b = translation(t[2],alphabet)
    if a==['scalar',0] or b==['scalar',0]: return ['scalar',0]
    if a==['scalar',1]: return b
    if b==['scalar',1]: return a
    return ['product',a,b]


def translated_graph(t):
    R.tick()
    tag=t[0]
    if tag=='scalar': return graph(edges=[] if t[1]==0 else [[0,1,['1']]])
    if tag=='original': return graph(edges=[[0,1,['x'+str(t[1]+1)]]])
    if tag=='product': return product([translated_graph(t[1]),translated_graph(t[2])])[0]
    g=graph(edges=[[0,1,['1']]])
    m=copy(g,translated_graph(t[1]))
    append_edge(g,0,m['entry'],['1']); append_edge(g,m['exit'],1,['1'])
    return g


def validate(g, symbols, original=False):
    p.fields(g,'vertices source sink edges')
    n=g['vertices']; edges=g['edges']
    p.require(type(n) is int and n>0 and type(edges) is list,'graph types')
    p.bound(n+len(edges),'records','graph explicit records')
    p.require(all(type(g[k]) is int and 0<=g[k]<n for k in ('source','sink')),'roots')
    adj=[[] for _ in R.items(range(n))]; incoming=[0 for _ in R.items(range(n))]
    labels=0; m0=0
    for edge in R.items(edges):
        p.require(type(edge) is list and len(edge)==3,'edge schema')
        u,v,lab=edge
        p.require(type(u) is int and type(v) is int and 0<=u<n and 0<=v<n,'edge endpoints')
        p.require(type(lab) is list,'label type'); p.bound(len(lab),'label_width','label width')
        for token in R.items(lab):
            p.require(type(token) is str and token in symbols,'declared token')
            p.name(token)
            p.require(not original or symbols[token][0] in ('one','original'),'original operand')
            labels+=1
        p.bound(labels,'label_entries','graph label entries')
        m0 += lab==['1']
        adj[u].append(v); incoming[v]+=1
    todo=deque(i for i in R.items(range(n)) if incoming[i]==0); order=[]
    while todo:
        R.tick(); u=todo.popleft(); order.append(u)
        for v in R.items(adj[u]):
            incoming[v]-=1
            if incoming[v]==0: todo.append(v)
    p.require(len(order)==n,'acyclic graph')
    # Check the produced permutation and every edge independently.
    position=[None for _ in R.items(range(n))]
    for i,v in R.items(enumerate(order)):
        p.require(position[v] is None,'topological injectivity'); position[v]=i
    for u,v,_ in R.items(edges): p.require(position[u]<position[v],'topological edge')
    return order,dict(vertices=n,edges=len(edges),records=n+len(edges),label_entries=labels,
        normalized_edges=len(edges),constant_edges=m0,letter_edges=len(edges)-m0,
        root_index_bits=sum(max(1,g[k].bit_length()) for k in ('source','sink')),
        max_index_bits=max(1,(n-1).bit_length()))


def reachability(g, symbols):
    order,_=validate(g,symbols,True)
    adj=[[] for _ in R.items(range(g['vertices']))]
    for u,v,_ in R.items(g['edges']): adj[u].append(v)
    reach=[0 for _ in R.items(range(g['vertices']))]
    for u in R.items(reversed(order)):
        reach[u]=1<<u
        R.reach_operations['shift']+=1; R.reach_bit_upper+=g['vertices']
        for v in R.items(adj[u]):
            reach[u] |= reach[v]
            R.reach_operations['or']+=1; R.reach_bit_upper+=g['vertices']
    return reach


def cut(g,s,t,reach):
    n=g['vertices']
    def has(u,v):
        R.reach_operations['shift_and_test']+=1; R.reach_bit_upper+=2*n+1
        return bool(reach[u] & (1<<v))
    no_path=not has(s,t)
    live=sorted({s,t}) if no_path else [v for v in R.items(range(n)) if has(s,v) and has(v,t)]
    ranks={v:i for i,v in R.items(enumerate(live))}
    mapping=[ranks.get(v) for v in R.items(range(n))]
    indices=[]
    for i,(u,v,_) in R.items(enumerate(g['edges'])):
        if not no_path and has(s,u) and has(v,t): indices.append(i)
    retained=set(R.items(indices))
    meta=dict(entry=s,exit=t,old_to_new=mapping,new_to_old=live,retained_edges=indices,
        deleted_vertices=[v for v in R.items(range(n)) if v not in ranks],
        deleted_edges=[i for i in R.items(range(len(g['edges']))) if i not in retained],
        no_path=no_path,transported_entry=mapping[s],transported_exit=mapping[t])
    out=graph(len(live),[],mapping[s],mapping[t])
    for i in R.items(indices):
        u,v,lab=g['edges'][i]; append_edge(out,mapping[u],mapping[v],lab)
    return meta,out


def central(a,b,symbols):
    labels=[]
    for x in R.items(a):
        for y in R.items(b):
            xx,yy=symbols[x],symbols[y]
            if xx[0]==yy[0]=='original' and xx[1]!=yy[1]:
                lo,hi=sorted((xx[1]+1,yy[1]+1)); labels.append('t:%d:%d'%(lo,hi))
    return labels


def observe_source(frame,event,arg):
    # Observer only: no replacement of the literal checker's rule engine.
    filename=frame.f_code.co_filename; name=frame.f_code.co_name
    if filename.endswith('/parity-four-rule/checker.py'):
        if event=='call' and name in ('tree','nodes','variables','<genexpr>','<listcomp>'):
            R.tick(); R.source_observer[name]+=1
        elif event=='line' and name=='_check_stream' and frame.f_lineno==76:
            R.tick(); R.source_observer['source_record']+=1
    elif filename==p.__file__:
        if event=='line' and (name,frame.f_lineno) in SOURCE_LOOP_LINES:
            R.tick(); R.source_observer[name+' loop']+=1
        if event=='call' and name in ('<genexpr>','<listcomp>'):
            R.tick(); R.source_observer[name]+=1
    return observe_source


SOURCE_LOOP_LINES=set()
for definition in ast.walk(ast.parse(inspect.getsource(p))):
    if isinstance(definition,ast.FunctionDef) and definition.name in ('request','check_tree','input_bounds','size_depth'):
        for node in ast.walk(definition):
            if isinstance(node,(ast.For,ast.While)):
                SOURCE_LOOP_LINES.add((definition.name,node.body[0].lineno))


def save_small(name, value):
    path=OUT/name
    p.require(not path.exists(),'refuse evidence overwrite')
    # Receipt bytes are not mathematical input items; separately sized/written.
    raw=json.dumps(value,ensure_ascii=True,separators=(',',':')).encode()
    used=sum(x.stat().st_size for x in OUT.iterdir() if x.is_file())
    p.require(len(raw)<=1_000_000 and used+len(raw)<=p.CAPS['certificate_bytes'],
              'receipt reserve and unchanged aggregate allowance')
    with path.open('xb') as stream: stream.write(raw)
    return len(raw)


def main():
    global R
    p.require(not OUT.exists(),'fresh run required; preserve prior artifacts')
    OUT.mkdir(); R=Run()
    p.require(p.CAPS==EXPECTED_CAPS,'all original caps pinned')
    save_small('manifest.json',dict(target=TARGET,assessment=REVIEW,status='IN_PROGRESS',
        caps=p.CAPS,item_visit_limit=100_000_000,seconds_limit=900,reserve_bytes=1_000_000,
        binding_paths=BIND_PATHS,manifest_clarification='six enumerated files plus two events = eight',
        transport_key_order=LAYOUT,encoding='compact UTF-8 JSON, ensure_ascii=True, no newline',
        layouts='explicit base graphs; explicit local-mode graphs; four explicit disjoint comparison graphs',
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()))
    result=dict(target=TARGET,assessment=REVIEW,accepted_equality=False,coordinate_search=False,
        word_expansion=False,status='IN_PROGRESS',unknown=['coordinate ranks','coordinate evidence',
        'all four equalities','later jobs','whole Boolean/K/H/nonzero-fJ','total interpreter bound'])
    try:
        R.at('input byte binding and parsing')
        binding=[]; objects={}
        for relative in R.items(BIND_PATHS):
            path=HERE/relative
            raw=p.read_bytes(path,'input_bytes' if '/inputs/' in relative else 'certificate_bytes')
            text=raw.decode('utf-8',errors='strict')
            p.require(text.encode('utf-8')==raw,'exact strict UTF-8 round trip')
            binding.append([relative,text]); R.raw_manifest.append(dict(path=relative,bytes=len(raw)))
            if not relative.endswith('proof.jsonl'):
                obj=p.parse(raw); R.walk(obj); objects[relative]=obj
            R.timer()
        R.binding=R.count(binding,'B_bind',32+4*32)
        R.at('fresh immutable-byte literal checking')
        started=time.monotonic(); sys.settrace(observe_source)
        try:
            req,raw,rows,checked=p.request(HERE/BIND_PATHS[3],HERE/BIND_PATHS[4])
        finally:
            sys.settrace(None)
            result['indivisible_source_seconds']=time.monotonic()-started
        R.timer()
        p.require(raw.decode('utf-8')==binding[3][1] and R.eq(req,objects[BIND_PATHS[4]]),
                  'literal engine actual byte binding')
        sys.settrace(observe_source)
        try:
            result['input_bounds']=p.input_bounds(req,raw,rows,HERE/BIND_PATHS[4])
        finally:
            sys.settrace(None)
        R.timer()
        cert=objects[BIND_PATHS[0]]; inv=objects[BIND_PATHS[1]]; prior=objects[BIND_PATHS[2]]
        failed=objects[BIND_PATHS[5]]; tr=objects[BIND_PATHS[6]]; event=objects[BIND_PATHS[7]]
        p.require(checked['records']==212 and rows[78]['rule']=='axiom' and
            req['alphabet']==['y5','y4','y3','y2','y1','y0'] and
            checked['sha256']=='f779fa52af4eb63805e45aa9940620be1cd3ce6c993ff4a903a996a0b539c74e',
            'fixed literal source and alphabet')
        p.require(raw.splitlines()[79]==p.read_bytes(HERE/BIND_PATHS[3],'input_bytes').splitlines()[79],
                  'record 78 physical line 80')
        for obj in R.items([cert,inv,prior]):
            p.require(R.eq(obj['caps'],p.CAPS) and R.eq(obj['alphabet'],req['alphabet']) and
                R.eq(obj['dictionary'],req['dictionary']),'archive framing and full dictionary')
        p.require(cert['source_record']==78 and cert['boolean_event']==2643 and
            R.eq(cert['checked_source'],checked),'source provenance fields')
        p.require(failed['accepted_fixed_job'] is False and failed['completed_modes']==[] and
            failed['complete_reference_received'] is False and failed['forward_position'] is None,
            'complete failed receipt gives no surviving reference or mode')
        R.checks.append('fresh literal source and complete old failure consumed')
        R.at('syntactic source translation and L036 job regeneration')
        symbols=p.symbol_map(req['alphabet'],req['dictionary'])
        p.fields(tr,'kind formula reduced graph'); p.fields(event,'kind graph')
        p.require(tr['kind']=='translation' and event['kind']=='boolean-input' and
            R.eq(tr['formula'],rows[78]['f'][2]),'event formula/source correspondence')
        reduced=translation(rows[78]['f'][2],req['alphabet'])
        p.require(R.eq(reduced,tr['reduced']),'complete reduced syntax')
        regenerated=translated_graph(reduced)
        p.require(R.eq(regenerated,tr['graph']) and R.eq(regenerated,event['graph']),
            'every source-translation vertex/edge/label, without path expansion')
        validate(regenerated,symbols,True)
        edges=[]
        for u,v,lab in R.items(regenerated['edges']):
            if u!=regenerated['sink']:
                counts=Counter(R.items(lab))
                for token in R.items(sorted(counts)):
                    if counts[token]%2: edges.append([u,v,[token]])
        h=graph(regenerated['vertices'],edges,regenerated['source'],regenerated['sink'])
        for obj in R.items([cert,inv,prior]): p.require(R.eq(h,obj['normalized']),'all normalized inputs')
        jobs=[]
        for u in R.items(range(h['vertices'])):
            outgoing=[(i,v,lab[0]) for i,(z,v,lab) in R.items(enumerate(h['edges'])) if z==u]
            for i,v,x in R.items(outgoing):
                jobs.append((u,'product_commutator',[i],graph(edges=[[0,1,[x]]]),dict(h,source=v)))
            for pos,(i,v,x) in R.items(enumerate(outgoing)):
                for j,w,y in R.items(outgoing[pos+1:]):
                    jobs.append((u,'sum_commutator',[i,j],
                        dict(h,vertices=h['vertices']+1,source=h['vertices'],edges=h['edges']+[[h['vertices'],v,[x]]]),
                        dict(h,vertices=h['vertices']+1,source=h['vertices'],edges=h['edges']+[[h['vertices'],w,[y]]])))
        p.require(len(jobs)==245 and all(len(z['jobs'])==245 for z in (cert,inv,prior)),'ordered job count')
        u,kind,occ,f,g=jobs[7]; item=cert['jobs'][7]; counted=inv['jobs'][7]; old=prior['jobs'][7]
        p.fields(item,'index vertex kind edge_occurrences restrictions selected vertices edges label_entries records graph')
        p.require((u,kind,occ)==(6,'sum_commutator',[0,5]),'exact job 7')
        for obj in R.items([item,counted,old]):
            p.require(R.eq([obj[k] for k in ('index','vertex','kind','edge_occurrences')],[7,u,kind,occ]),'job binding')
        operands=[]; maps=[]
        for original,saved in R.items(zip((f,g),item['restrictions'])):
            meta,child=cut(original,original['source'],original['sink'],reachability(original,symbols))
            expected=dict(original=original,trimmed=child,old_to_new=meta['old_to_new'],new_to_old=meta['new_to_old'],
                retained_edge_indices=meta['retained_edges'],no_path=meta['no_path'])
            p.require(R.eq(expected,saved),'independent whole operand maps')
            operands.append(child); maps.append(expected)
        for obj in R.items([counted,old]): p.require(R.eq(maps,obj['restrictions']),'both inventory maps')
        a,b=operands
        R.checks.append('complete syntactic translation, normalized input and independently regenerated whole operands')
        R.at('all selected copy and structural occurrence checks')
        reaches=[reachability(z,symbols) for z in R.items(operands)]
        selected=[]; pairs=0
        for i,(_,_,al) in R.items(enumerate(a['edges'])):
            for j,(_,_,bl) in R.items(enumerate(b['edges'])):
                pairs+=1; labels=central(al,bl,symbols)
                if labels: selected.append(dict(f_edge=i,g_edge=j,central=labels))
        p.require(R.eq(selected,old['selected']) and len(selected)==len(item['selected'])==len(counted['selected'])==120,
                  'all pairs, including empty central lists and multiplicities')
        w=item['graph']; cursor=0; vertex=2; copies=0; copy_stats=Counter()
        for pair,part,countpart in R.items(zip(selected,item['selected'],counted['selected'])):
            p.fields(part,'f_edge g_edge central copies connecting_edges')
            p.require(R.eq(pair,{k:part[k] for k in pair}),'selected order')
            au,av,_=a['edges'][pair['f_edge']]; bu,bv,_=b['edges'][pair['g_edge']]
            specs=[(a,a['source'],au,reaches[0]),(b,b['source'],bu,reaches[1]),
                   (b,bv,b['sink'],reaches[1]),(a,av,a['sink'],reaches[0])]
            p.require(len(part['copies'])==len(countpart['copies'])==4,'four disjoint copies')
            roots=[]
            for ci,(z,s,t,reach) in R.items(enumerate(specs)):
                meta,child=cut(z,s,t,reach)
                p.require(R.eq(meta,countpart['copies'][ci]),'full retained/deleted copy inventory')
                meta.update(vertex_range=[vertex,vertex+child['vertices']],edge_range=[cursor,cursor+len(child['edges'])])
                p.require(R.eq(meta,part['copies'][ci]),'all copy ranges')
                for cu,cv,lab in R.items(child['edges']):
                    p.require(cursor<len(w['edges']) and R.eq(w['edges'][cursor],[vertex+cu,vertex+cv,lab]),
                              'every literal copied edge'); cursor+=1
                roots.append((vertex+child['source'],vertex+child['sink'])); vertex+=child['vertices']; copies+=1
                copy_stats['no_path' if meta['no_path'] else 'path_exists']+=1
                copy_stats['coincident' if s==t else 'distinct']+=1
            fp,gp,gs,fs=roots
            connectors=[[0,fp[0],['1']],[fp[1],gp[0],['1']],[gs[1],fs[0],['1']],[fs[1],1,['1']]]
            end=cursor+4+len(pair['central'])
            p.require(R.eq(part['connecting_edges'],[cursor,end]) and R.eq(w['edges'][cursor:cursor+4],connectors)
                and R.eq(w['edges'][cursor+4:end],[[gp[1],gs[0],[x]] for x in R.items(pair['central'])]),
                'all connectors and central occurrences')
            cursor=end
        p.require(vertex==w['vertices'] and cursor==len(w['edges']) and (w['source'],w['sink'])==(0,1),
                  'complete W partition')
        order,metrics=validate(w,symbols)
        for obj in R.items([item,counted]):
            p.require(all(obj[k]==metrics[k] for k in ('vertices','edges','records','label_entries')),'W ledger')
        states=[set() for _ in R.items(range(w['vertices']))]; states[0]={0}
        adj=[[] for _ in R.items(states)]
        for cu,cv,lab in R.items(w['edges']):
            p.require(len(lab)==1,'fixed structural singleton labels')
            adj[cu].append((cv,int(symbols[lab[0]][0]=='placeholder')))
        for cu in R.items(order):
            for cv,inc in R.items(adj[cu]):
                states[cv].update(k+inc for k in R.items(states[cu]))
                p.require(states[cv]<={0,1},'no multiple-placeholder structural path')
        p.require(states[1]<={1},'one placeholder per accepting path')
        result['structural']=dict(all_pairs=pairs,selected_pairs=len(selected),copies=copies,
            copy_cases=dict(copy_stats),metrics=metrics,sink_states=sorted(states[1]))
        R.checks.append('480 copies, all maps/edges/connectors/central occurrences and structural counts')
        R.at('independent whole-copy reference and ordered products')
        reference=graph(); refmaps=[]
        # Enumerate original edge pairs again; never use W's selected lists/maps.
        for i,(au,av,al) in R.items(enumerate(a['edges'])):
            for j,(bu,bv,bl) in R.items(enumerate(b['edges'])):
                labels=central(al,bl,symbols)
                if not labels: continue
                ms=[copy(reference,z,s,t) for z,s,t in R.items([
                    (a,a['source'],au),(b,b['source'],bu),(b,bv,b['sink']),(a,av,a['sink'])])]
                fp,gp,gs,fs=ms; start=len(reference['edges'])
                for x,y in R.items([(0,fp['entry']),(fp['exit'],gp['entry']),
                                    (gs['exit'],fs['entry']),(fs['exit'],1)]):
                    append_edge(reference,x,y,['1'])
                for token in R.items(labels): append_edge(reference,gp['exit'],gs['entry'],[token])
                refmaps.append(dict(f_edge=i,g_edge=j,central=labels,copies=ms,
                                    connecting_edges=[start,len(reference['edges'])]))
        fg,fgmaps=product([a,b]); gf,gfmaps=product([b,a]); comm=graph(); productmaps=[]
        for name,child,inner in R.items([('FG',fg,fgmaps),('GF',gf,gfmaps)]):
            m=copy(comm,child); begin=len(comm['edges'])
            append_edge(comm,0,m['entry'],['1']); append_edge(comm,m['exit'],1,['1'])
            productmaps.append(dict(name=name,copy=m,factor_copies=inner,connectors=[begin,len(comm['edges'])]))
        bases=[('F',a),('G',b),('W',w),('R',reference),('FG',fg),('GF',gf),('P',comm)]
        # Validate every copy against its operand with a separate full pass.
        for part in R.items(refmaps):
            for z,m in R.items(zip((a,b,b,a),part['copies'])):
                lo,hi=m['vertex_range']; start,end=m['edge_range']
                p.require(hi-lo==z['vertices'] and end-start==len(z['edges']),'whole reference copy dimensions')
                for ei,(cu,cv,lab) in R.items(enumerate(z['edges'])):
                    p.require(R.eq(reference['edges'][start+ei],[lo+cu,lo+cv,lab]),'every whole reference copied edge')
            fp,gp,gs,fs=part['copies']; start,end=part['connecting_edges']
            expected=[[0,fp['entry'],['1']],[fp['exit'],gp['entry'],['1']],
                      [gs['exit'],fs['entry'],['1']],[fs['exit'],1,['1']]]
            expected.extend([gp['exit'],gs['entry'],[x]] for x in R.items(part['central']))
            p.require(end-start==len(expected) and R.eq(reference['edges'][start:end],expected),
                      'every independent reference connector and central edge')
        for child,factors,factormaps in R.items([(fg,(a,b),fgmaps),(gf,(b,a),gfmaps)]):
            cursor=0; vertex=2; last=0
            for factor,m in R.items(zip(factors,factormaps)):
                p.require(m['vertex_range']==[vertex,vertex+factor['vertices']] and
                    m['edge_range']==[cursor,cursor+len(factor['edges'])] and
                    (m['entry'],m['exit'])==(vertex+factor['source'],vertex+factor['sink']),
                    'ordered product factor map')
                for cu,cv,lab in R.items(factor['edges']):
                    p.require(R.eq(child['edges'][cursor],[vertex+cu,vertex+cv,lab]),'product factor edge'); cursor+=1
                p.require(R.eq(child['edges'][cursor],[last,m['entry'],['1']]),'product factor connector');cursor+=1
                vertex+=factor['vertices'];last=m['exit']
            p.require(R.eq(child['edges'][cursor],[last,1,['1']]) and cursor+1==len(child['edges']) and
                      vertex==child['vertices'],'product final connector and exhaustion')
        for child,part in R.items(zip((fg,gf),productmaps)):
            m=part['copy']; off=m['vertex_range'][0]; start=m['edge_range'][0]
            for ei,(cu,cv,lab) in R.items(enumerate(child['edges'])):
                p.require(R.eq(comm['edges'][start+ei],[off+cu,off+cv,lab]),'P ordered product copy edge')
            start,end=part['connectors']
            p.require(R.eq(comm['edges'][start:end],[[0,m['entry'],['1']],[m['exit'],1,['1']]]),'P connectors')
        R.checks.append('independent reference pair enumeration and every whole copied edge')
        base_entries=[]
        for name,z in R.items(bases):
            top,met=validate(z,symbols,name in ('F','G','FG','GF','P'))
            R.graphs.append(dict(name=name,**met))
            base_entries.append(dict(name=name,graph=z,topological_order=top))
        modes=[]; byname={}
        R.at('explicit free zero axiom transports')
        def local(name,z,mode):
            out=graph(z['vertices'],[],z['source'],z['sink']); attrs=[]
            for ei,(cu,cv,lab) in R.items(enumerate(z['edges'])):
                # Parity is confined to a single original affine label.
                counts=Counter(R.items(lab))
                for token in R.items(sorted(counts)):
                    if not counts[token]%2: continue
                    symbol=symbols[token]; vstart=out['vertices']; estart=len(out['edges'])
                    if symbol[0]!='placeholder' or mode=='free':
                        append_edge(out,cu,cv,[token])
                    elif mode=='axiom':
                        words=req['dictionary']['placeholders'][symbol[1]]['polynomial']
                        for word in R.items(words):
                            last=cu
                            if not word: append_edge(out,cu,cv,['1'])
                            for wi,x in R.items(enumerate(word)):
                                dest=cv if wi+1==len(word) else out['vertices']
                                if dest!=cv:
                                    p.bound(out['vertices']+len(out['edges'])+1,'records','gadget vertex preallocation')
                                    out['vertices']+=1
                                append_edge(out,last,dest,['x'+str(req['alphabet'].index(x)+1)]); last=dest
                    attrs.append(dict(input_edge=ei,token=token,vertex_range=[vstart,out['vertices']],
                                      edge_range=[estart,len(out['edges'])]))
            top,met=validate(out,symbols,mode!='free')
            # Separate local reception: exhaust every input edge's expected
            # word paths and disjoint interiors, without any global PIT.
            cursor=0; vertex=z['vertices']
            for attr in R.items(attrs):
                cu,cv,lab=z['edges'][attr['input_edge']]; token=attr['token']; symbol=symbols[token]
                p.require(attr['vertex_range'][0]==vertex and attr['edge_range'][0]==cursor,'local partition start')
                if symbol[0]!='placeholder' or mode=='free': words=[[token]]
                elif mode=='zero': words=[]
                else:
                    words=[['x'+str(req['alphabet'].index(x)+1) for x in R.items(word)]
                           for word in R.items(req['dictionary']['placeholders'][symbol[1]]['polynomial'])]
                for word in R.items(words):
                    last=cu
                    if not word:
                        p.require(R.eq(out['edges'][cursor],[cu,cv,['1']]),'empty word gadget'); cursor+=1
                    for wi,x in R.items(enumerate(word)):
                        dest=cv if wi+1==len(word) else vertex
                        if dest!=cv: vertex+=1
                        p.require(R.eq(out['edges'][cursor],[last,dest,[x]]),'every word gadget edge');cursor+=1;last=dest
                p.require(attr['vertex_range'][1]==vertex and attr['edge_range'][1]==cursor,'local partition end')
            p.require(vertex==out['vertices'] and cursor==len(out['edges']),'local transport exhausted')
            entry=dict(name=name+'_'+mode,mode=mode,graph=out,gadgets=attrs,topological_order=top)
            R.graphs.append(dict(name=entry['name'],gadget_interiors=out['vertices']-z['vertices'],**met))
            modes.append(entry); byname[entry['name']]=out
        for mode in R.items(['free','zero','axiom']):
            for name,z in R.items([('W',w),('R',reference)]): local(name,z,mode)
        R.checks.append('every local affine/zero/word-gadget transport, full dictionary retained')
        R.at('four disjoint explicit comparison graphs')
        comparisons=[]; dimensions=[]
        for name,left,right,q in R.items([
            ('Dfree',byname['W_free'],byname['R_free'],27),
            ('Dzero',byname['W_zero'],byname['R_zero'],6),
            ('Daxiom',byname['W_axiom'],byname['R_axiom'],6),
            ('Dcomm',byname['R_axiom'],comm,6)]):
            # Disjoint union has no new connector: eta/theta select both roots.
            out=graph(0,[],0,0); maps2=[]
            for child in R.items([left,right]): maps2.append(copy(out,child))
            out['source']=maps2[0]['entry'];out['sink']=maps2[0]['exit']
            top,met=validate(out,symbols,name!='Dfree')
            for child,m in R.items(zip((left,right),maps2)):
                off=m['vertex_range'][0]; start=m['edge_range'][0]
                for ei,(cu,cv,lab) in R.items(enumerate(child['edges'])):
                    p.require(R.eq(out['edges'][start+ei],[off+cu,off+cv,lab]),'every disjoint comparison copied edge')
            alphabet=[symbols[k] for k in R.items(symbols) if k!='1' and (name=='Dfree' or symbols[k][0]=='original')]
            p.require(len(alphabet)==q,'full mode alphabet including unused placeholders')
            dims=dict(name=name,N=met['vertices'],q=q,m0=met['constant_edges'],mL=met['letter_edges'])
            dimensions.append(dims); R.graphs.append(dict(name=name,**met))
            comparisons.append(dict(name=name,alphabet=alphabet,graph=out,copies=maps2,
                eta=[m['entry'] for m in maps2],theta=[m['exit'] for m in maps2],topological_order=top))
        R.dimensions=dimensions
        transport=dict(format='L110-explicit-transport-v1',alphabet=req['alphabet'],dictionary=req['dictionary'],
            symbol_transport=[[k,v] for k,v in R.items(symbols.items())],
            source_binding=dict(record=78,physical_line=80,translation_event=2642,boolean_event=2643,
                source_check=checked,source_row=rows[78],normalized=h),
            whole_operand_maps=maps,selected_occurrences=item['selected'],reference_copies=refmaps,
            product_copies=productmaps,base_graphs=base_entries,mode_transports=modes,comparisons=comparisons)
        p.require(list(transport)==LAYOUT,'frozen strict transport key order')
        R.at('per graph exact encoding ledger')
        all_entries=base_entries+modes+comparisons
        p.require(len(all_entries)==len(R.graphs),'complete per graph ledger')
        dictionary_bytes=R.count(req['dictionary'],'full_dictionary')
        for entry,met in R.items(zip(all_entries,R.graphs)):
            p.require(entry['name']==met['name'],'per graph ledger order')
            met['graph_encoded_bytes']=R.count(entry['graph'],entry['name']+' graph')
            met['topological_order_encoded_bytes']=R.count(entry['topological_order'],entry['name']+' topology')
            met['root_encoding_bytes']=R.count([entry['graph']['source'],entry['graph']['sink']],entry['name']+' roots')
            met['name_encoding_bytes']=R.count(entry['name'],entry['name']+' name')
            met['dictionary_encoded_bytes']=dictionary_bytes
            if 'gadgets' in entry:
                met['gadget_attribution_encoded_bytes']=R.count(entry['gadgets'],entry['name']+' gadgets')
            elif 'copies' in entry:
                met['copy_attribution_encoded_bytes']=R.count(entry['copies'],entry['name']+' copies')
        R.at('complete explicit transport serialization sizing')
        # Required binding and transport are proposed together, and all graphs
        # and comparisons remain simultaneously retained. No payload is written.
        used=sum(x.stat().st_size for x in OUT.iterdir() if x.is_file())
        R.transport=R.count(transport,'B_trans',32+4*32+R.binding)
        R.checks.append('complete compact explicit transport sizing')
        R.at('symbolic coordinate endpoints and live-data ledger')
        def endpoints(full):
            wire=32+R.binding+R.transport; bits=0; ops=0; rows=[]
            for d in R.items(dimensions):
                n,q=d['N'],d['q']; rank=n if full else 0
                bb=(rank*n+7)//8; cb=(rank+7)//8; tb=(q*rank*rank+7)//8
                wire+=32+bb+cb+tb; bits+=rank*n+rank+q*rank*rank
                ops+=16*(q+1)*(rank+1)**2*(n+d['m0']+d['mL']+1)
                rows.append(dict(name=d['name'],r=rank,B_bytes=bb,c_bytes=cb,T_bytes=tb,
                    initial_comparisons=n,transition_comparisons=q*rank*n,final_comparisons=rank))
            return dict(rows=rows,wire_bytes=wire,logical_coordinate_bits=bits,algebraic_bit_operation_bound=ops)
        zero=endpoints(False); full=endpoints(True)
        # All coordinate sets are simultaneous. Separately decoded arrays add
        # P_bits; scratch is four separately rounded Nmax-bit rows. Python object
        # overhead and decoded JSON memory have no asserted exact byte bound.
        nmax=max(d['N'] for d in dimensions)
        result.update(status='MANDATORY_TRANSPORT_FITS',dimensions=dimensions,
            framing=dict(magic='J7F2C001',fixed_bundle_bytes=32,comparison_headers_bytes=128,
                B_bind=R.binding,B_trans=R.transport),zero_rank_size_baseline=zero,
            full_rank_size_endpoint=full,scratch_rows_bytes=4*((nmax+7)//8),
            full_rank_fits_bytes=full['wire_bytes']+used+1_000_000<=p.CAPS['certificate_bytes'],
            coordinate_byte_ceiling=p.CAPS['certificate_bytes']-used-1_000_000-(32+128+R.binding+R.transport),
            symbolic_equations='L110 (7)-(9), independent integer 0<=r_k<=N_k; all four arrays simultaneous',
            live_ledger=dict(wire='32+B_bind+B_trans+sum(32+ceil(r*N/8)+ceil(r/8)+ceil(q*r*r/8))',
                separate_decoded_coordinate_bits='sum(r*N+r+q*r*r)',scratch_bytes=4*((nmax+7)//8),
                raw_bound_input_bytes=sum(x['bytes'] for x in R.raw_manifest),
                decoded_JSON_and_graph_objects='retained simultaneously; exact interpreter overhead UNBOUNDED here',
                decoding_peak='wire + raw inputs + all decoded graphs/maps + coordinates + four scratch rows + receipt',
                persisted_payload_bytes=0,temporary_payload_files=0,failed_payload_prefix_bytes=0,
                old_archives='preserved; no new saved copies; proposed wire charges their literal binding bytes'),
            complete_transport_checks=True,exact_total_interpreter_bound=False)
        # Receipt reserve is administrative: insufficient space here is not a
        # mandatory-format counterexample.
        proposed=zero['wire_bytes']+used
        if proposed+1_000_000>p.CAPS['certificate_bytes']:
            raise Stop('ADMINISTRATIVE',dict(resource='receipt_reserve',actual=proposed+1_000_000,
                required=p.CAPS['certificate_bytes'],mandatory_bytes=proposed))
    except Stop as err:
        result.update(status=err.kind,stop=err.details,complete_transport_checks=False)
    except Exception as err:
        result.update(status='ADMINISTRATIVE',stop=dict(error=type(err).__name__,message=str(err)),
                      complete_transport_checks=False)
    finally:
        sys.settrace(None)
    now=time.monotonic()
    R.times.append(dict(stage=R.stage,seconds=now-R.last_time))
    result.update(caps=p.CAPS,final_stage=R.stage,item_visits=R.visits,required_item_visits=100_000_000,
        visits_by_stage=dict(R.by_stage),stage_times=R.times,elapsed_seconds=now-R.start,required_seconds=900,
        raw_binding_manifest=R.raw_manifest,sections=R.sections,graphs=R.graphs,
        binding_bytes=R.binding,transport_bytes=R.transport,known_dimensions=R.dimensions,
        completed_checks=R.checks,source_observer=dict(R.source_observer),
        buffer_peak_bytes=R.serialized_buffer_peak,observed_ru_maxrss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        ru_maxrss_units='bytes on macOS; observation, not total bound',
        counter_index_bit_lengths=dict(max_counter=R.integer_bits,max_graph_index=max(
            [g['max_index_bits'] for g in R.graphs]+[1])),
        reachability_operations=dict(R.reach_operations),reachability_bit_operation_upper=R.reach_bit_upper,
        accounting='Administrative item units charge every explicitly traversed record/label/tree/JSON value; source observer charges tree calls, request loops and comprehension resumes. JSON character scans/UTF-8/I/O and Python internals are separately byte/time work, not a claimed total interpreter bound.',
        saved_before_receipt=sum(x.stat().st_size for x in OUT.iterdir() if x.is_file()),
        required_evidence_bytes=p.CAPS['certificate_bytes'])
    size=save_small('preflight.json',result)
    used=sum(x.stat().st_size for x in OUT.iterdir() if x.is_file())
    print(json.dumps(dict(status=result['status'],item_visits=R.visits,required_item_visits=100_000_000,
        B_bind=R.binding,B_trans=R.transport,saved_evidence_bytes=used,required_evidence_bytes=200_000_000,
        receipt_bytes=size,stop=result.get('stop'),path=str(OUT/'preflight.json'))),flush=True)
    return 0 if result['status']=='MANDATORY_TRANSPORT_FITS' else 1


if __name__=='__main__':
    raise SystemExit(main())
