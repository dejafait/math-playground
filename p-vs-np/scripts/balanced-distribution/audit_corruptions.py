"""Read every corruption byte and establish the exact sole changed field."""
import gzip
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = HERE/'output'

def main():
    saved = json.loads((OUT/'certificate-172.json').read_text())
    result = dict(complete=False, failures=[], checks=[])
    dest = OUT/'audit-174-corruptions.json'
    def save(): dest.write_text(json.dumps(result,indent=2)+'\n')
    save()
    try:
        for mode,entries in saved['corruptions'].items():
            with gzip.open(OUT/('m2-variable.'+mode+'.jsonl.gz'),'rb') as stream:
                base = stream.read()
            original = [json.loads(line) for line in base.splitlines()]
            for old in entries:
                path = ROOT/old['path']
                with gzip.open(path,'rb') as stream: data=stream.read()
                rows=[json.loads(line) for line in data.splitlines()]
                assert len(rows)==len(original)
                changed=[k for k,(a,b) in enumerate(zip(original,rows)) if a!=b]
                assert len(changed)==1
                k=changed[0]; before=original[k]; after=rows[k]
                assert set(before)==set(after)
                fields=[key for key in before if before[key]!=after[key]]
                assert len(fields)==1
                if 'axiom-substitution' in path.name:
                    assert k==1 and fields==['subs'] and after['subs']==dict(before['subs'],A='BAD_SUBSTITUTION')
                elif 'forward-reference' in path.name:
                    assert k>0 and fields==['refs'] and after['refs']==[0,len(rows)-1]
                elif 'mp-antecedent' in path.name:
                    assert k>0 and fields==['refs'] and after['refs'][1]==before['refs'][1]
                    ref=after['refs'][0]
                    assert 0<=ref<k-1 and rows[ref+1]['f']!=rows[before['refs'][0]+1]['f']
                elif 'endpoint' in path.name:
                    assert k==0 and fields==['goal'] and after['goal']=='BAD_ENDPOINT'
                else: raise AssertionError('unknown corruption')
                result['checks'].append(dict(path=old['path'],bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),
                    records=len(rows),changed_record=k,changed_field=fields[0],before=before[fields[0]],after=after[fields[0]],pass_single_mutation=True))
                save()
        assert len(result['checks'])==8
        result['complete']=True; save()
        print('8/8 complete corruption archives each have exactly one intended field change; failures',result['failures'],
              'certificate',dest.relative_to(ROOT))
    except Exception as err:
        result['failures'].append(type(err).__name__+': '+str(err));save();raise

if __name__=='__main__': main()
