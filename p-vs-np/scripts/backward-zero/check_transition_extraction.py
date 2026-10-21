"""Complete two-format old-wrapper regression; preserve all old archives."""
import gzip
import json
from pathlib import Path
import build as b

HERE=Path(__file__).resolve().parent
suite=b.module('extraction_suite_198',HERE/'run_suite.py')
OUT=HERE/'output'


def main():
    cert={'complete':False,'failures':[], 'records_compared':0,
          'case':'existing step-192 empty-alphabet, full native/image records'}
    destination=OUT/'chain-198-extraction-regression.json'
    suite.save(destination,cert)
    try:
        library={}
        for name,goal in b.ep.fixed().items():
            folder=OUT if name in ('zeroR','zeroL','prod_zero') else HERE.parent/(
                'balanced-distribution' if name in ('dist','prod_cong') else 'balanced-slot')/'output'
            library[name]=b.aggregate.load(folder/(name+'.native.jsonl.gz'),b.ep.c.serialize(goal))
        data=json.loads((OUT/'empty-alphabet.request.json').read_text())
        paths=[OUT/('empty-alphabet-coordinate-'+str(i)+'.native.jsonl.gz') for i in range(data['N'])]
        obj=b.compile_one(data,paths,[],library)
        for mode,image in [('native',False),('not-or',True)]:
            path=OUT/('empty-alphabet.'+mode+'.jsonl.gz')
            with gzip.open(path,'rt') as stream:
                assert json.loads(next(stream))=={'format':mode,'goal':b.p.text(obj.p.rows[obj.root][0],image)}
                count=0
                for count,raw in enumerate(stream,1):
                    f,rule,refs,subs,deps=obj.p.rows[count-1]
                    row={'f':b.p.text(f,image),'rule':rule}
                    if rule=='mp': row['refs']=list(refs)
                    else: row['subs']={k:b.p.text(v,image) for k,v in subs.items()}
                    assert json.loads(raw)==row
                assert count==len(obj.p.rows)
            cert[mode]={'path':str(path.relative_to(suite.ROOT)),
                        'complete_record_equality':True,'lines':count}
            cert['records_compared']+=count
        cert['complete']=True; suite.save(destination,cert)
        print('extracted wrapper unchanged:',cert['records_compared'],
              'complete native/image records; failures 0;',str(destination.relative_to(suite.ROOT)))
    except Exception as exc:
        cert['failures'].append({'type':type(exc).__name__,'message':str(exc)})
        suite.save(destination,cert); raise


if __name__=='__main__': main()
