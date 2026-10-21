"""Reuse the preserved step-253 malformed streams, including native float refs."""
import gzip
import json
import interned_255 as h

def main():
    base=[h.SOURCE/('regression-valid.'+m+'.jsonl.gz') for m in h.MODES]
    with gzip.open(base[0],'rb') as stream: goal=h.replay.strict_read(stream.readline())['goal']
    result=dict(complete=False,failures=[],rejections=[])
    for name,which in [('boolean-reference',0),('float-reference',0),
        ('image-boolean-reference',1),('image-float-reference',1),('wrong-image',1),('wrong-substitution',0)]:
        pair=list(base); pair[which]=h.SOURCE/('regression-'+name+'.jsonl.gz')
        try: p=h.load(pair,goal)
        except (AssertionError,ValueError,KeyError,TypeError) as error:
            result['rejections'].append(dict(name=name,error=type(error).__name__+': '+str(error)))
        else: p.syntax.close(); raise AssertionError('accepted corruption '+name)
    result['complete']=True
    (h.OUT/'supplement.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS all six preserved step-253 corruptions, including Boolean/float references in BOTH formats')
if __name__=='__main__': main()
