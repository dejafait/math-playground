"""Complete corrected checkpoint replay after discovering numeric type aliasing.

The original run and original source remain preserved. This worker repairs only
internal checkpoint type comparison, then rechecks the entire joined boundary.
"""
import copy
import gzip
import importlib.util
import json
import pickle
import time
import copier_257 as c

def main():
    started=time.monotonic(); path=c.OUT/'strict-reload.json'
    assert not path.exists()
    result=dict(complete=False,stage='startup',failures=[],rejections=[])
    path.write_text(json.dumps(result,indent=2)+'\n')
    joined=None
    try:
        prior=json.loads((c.OUT/'certificate.json').read_text()); assert prior['complete'] and not prior['failures']
        expected=prior['segments']
        for seg in expected:
            seg['paths']=tuple(seg['paths']); seg['substitutions']=tuple(tuple(x) for x in seg['substitutions'])
        with gzip.open(c.OUT/'joined.pkl.gz','rb') as stream:
            snapshot=pickle.load(stream); assert stream.read()==b''
        # Direct discriminators cover values for which ordinary equality would
        # accept the corruption; no production field is assumed unequal by type.
        def reject(name,mutate):
            bad=dict(snapshot); bad['segments']=copy.deepcopy(snapshot['segments'])
            bad['locations']=list(snapshot['locations']); mutate(bad)
            try: q=c.restore(bad,expected)
            except (AssertionError,ValueError,TypeError,KeyError,IndexError) as error:
                result['rejections'].append(dict(name=name,error=type(error).__name__+': '+str(error)))
            else: q.syntax.close(); raise AssertionError('accepted '+name)
        for key in ('start','count','root','goal'):
            reject('float-segment-'+key,lambda z,key=key:z['segments'][0].__setitem__(key,float(z['segments'][0][key])))
        reject('boolean-start',lambda z:z['segments'][0].__setitem__('start',True))
        reject('float-saved-lines',lambda z:z['segments'][0]['checked']['measurements']['native'].__setitem__('lines',37000.0))
        for value in (True,1.0):
            reject('location-global-'+type(value).__name__,lambda z,value=value:z['locations'].__setitem__(0,(*z['locations'][0][:3],value)))
        assert snapshot['segments'][0]['start']==True and not c.exact(True,1) and not c.exact(1.0,1)
        joined=c.restore(snapshot,expected)
        assert c.exact(joined.snapshot(),snapshot)
        spec=importlib.util.spec_from_file_location('strictcontract257',c.ROOT/'scripts/actual-tree/verify.py')
        v=importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
        envelope=json.loads((c.h.SOURCE/'source-envelope.json').read_text())
        goals=v.contract(envelope['source'],envelope['edges'],envelope['request'])
        old=json.loads((c.h.SOURCE/'certificate.json').read_text())['certified_locals']
        result['stage']='complete archive fields'; path.write_text(json.dumps(result,indent=2)+'\n')
        result['comparison']=c.compare(joined,goals,old)
        assert c.exact(result['comparison'],prior['after_checkpoint'])
        result.update(complete=True,stage='complete',strict_types=True,
            complete_replayed_rows=len(joined.rows),complete_locations=len(joined.locations),
            repair='Type-sensitive recursive segment/location equality replaces numeric-coercing equality; no copying or mathematical operation changed.')
    except BaseException as error:
        result['failures'].append(type(error).__name__+': '+str(error)); raise
    finally:
        result['elapsed_seconds']=time.monotonic()-started
        path.write_text(json.dumps(result,indent=2)+'\n')
        if joined: joined.syntax.close()
    print('PASS corrected strict checkpoint; all',result['complete_replayed_rows'],'rows replayed; all native/image archive fields compared; numeric-type corruptions rejected',len(result['rejections']))

if __name__=='__main__': main()
