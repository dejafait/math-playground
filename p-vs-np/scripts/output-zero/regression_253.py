"""Small complete writer/count/strict-replay regressions, no large exports."""
import copy
import gzip
import json
import time
import nonempty_253 as h

def main():
    h.started=time.monotonic()
    dest=h.OUT/'regression.json'
    if dest.exists(): raise RuntimeError('preserve prior regression')
    o=h.b.Store({},'x'); o.root=o.p.identity('x')
    pair,written=h.pair_write(o,'regression-valid')
    goal=h.p.text(o.p.rows[o.root][0]); got=h.scan(pair,goal)
    counter=h.ByteCount()
    for mode,image in zip(h.MODES,(False,True)):
        want=len(h.enc(dict(format=mode,goal=h.p.text(o.p.rows[o.root][0],image))))
        want+=sum(counter.row(row,image) for row in o.p.rows)
        assert want==written[mode]['bytes']==got['measurements'][mode]['bytes']
    result=dict(positive_complete=True,exact_count_both_formats=True,
                writer=written,rejections=[],failures=[])
    for name,which,mutation in [
        ('boolean-reference',0,'bool'),('float-reference',0,'float'),
        ('image-boolean-reference',1,'bool'),('image-float-reference',1,'float'),
        ('wrong-image',1,'formula'),('wrong-substitution',0,'subs')]:
        with gzip.open(pair[which],'rb') as stream:
            rows=[json.loads(line) for line in stream]
        if mutation in ('bool','float'):
            row=next(r for r in rows[1:] if r['rule']=='mp')
            row['refs'][0]=bool(row['refs'][0]) if mutation=='bool' else float(row['refs'][0])
        elif mutation=='formula': rows[-1]['f']='wrong'
        else: rows[1]['subs']['A']='wrong'
        path=h.OUT/('regression-'+name+'.jsonl.gz')
        with gzip.open(path,'wb') as stream:
            for row in rows: stream.write(h.enc(row))
        bad=copy.copy(pair); bad[which]=path
        try: h.scan(bad,goal)
        except (AssertionError,ValueError) as error:
            result['rejections'].append(dict(name=name,rejected=True,error=type(error).__name__+': '+str(error)))
        else: raise AssertionError('corruption accepted: '+name)
    result['complete']=True
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS small writer/count pair and',len(result['rejections']),'strict malformed-stream rejections;',dest.relative_to(h.ROOT))

if __name__=='__main__': main()
