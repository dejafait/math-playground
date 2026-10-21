"""Five complete corruptions on the fully verified empty-case inputs/exports."""
import json
import run as h


def main():
    initial=json.loads((h.OUT/'certificate-202.json').read_text())
    case=initial['cases'][0];assert case['complete']
    cert=dict(step=202,positive_base='scripts/left-closure/output/certificate-202.json',
        positive_case='empty',rejections=[],failures=[],complete=False)
    h.DEST=h.OUT/'rejections-202.json';h.save(cert)
    lib={}
    for name,goal in dict(h.b.ep.fixed(),close_cancel=h.ep.cancellation()).items():
        if name=='close_cancel':path=h.OUT/'close_cancel.native.jsonl.gz'
        elif name in ('zeroR','zeroL','prod_zero'):
            path=h.HERE.parent/'backward-zero'/'output'/(name+'.native.jsonl.gz')
        else:
            folder='balanced-distribution' if name in ('dist','prod_cong') else 'balanced-slot'
            path=h.HERE.parent/folder/'output'/(name+'.native.jsonl.gz')
        lib[name]=h.b.aggregate.load(path,h.ep.e.c.serialize(goal))
        assert lib[name]['measurement']['sha256']==initial['library'][name]['native']['sha256']
    d=json.loads((h.ROOT/case['request']).read_text())
    paths=[h.ROOT/path for path in case['inputs']]
    try:
        h.rejections(d,paths,lib,case,cert)
        cert['complete']=True;h.save(cert)
        print('PASS five complete rejection cases;',h.DEST.relative_to(h.ROOT),flush=True)
    except BaseException as exc:
        cert['failures'].append(type(exc).__name__+': '+str(exc));h.save(cert);raise

if __name__=='__main__':main()
