"""Supplementary original-template and nested-optional retention checks.

No emitter import. Full output primitive/image replay and whole-import equality
are supplied by composition-241/certificate.json; this checks the remaining
exact specialization and transported map against original objects.
"""
import copy
import gzip
import importlib.util
import json
import sys
from itertools import zip_longest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts/backward-zero'))
spec=importlib.util.spec_from_file_location('retention241_scanner',ROOT/'scripts/backward-zero/audit_archives.py')
a=importlib.util.module_from_spec(spec); spec.loader.exec_module(a)
OUT=ROOT/'scripts/output-zero/output/composition-241'
DEST=OUT/'retention-check.json'


def read(path): return a.read(path.read_bytes())
def records(path):
    with gzip.open(path,'rb') as stream:
        a.read(stream.readline())
        for raw in stream: yield a.read(raw)


def subst(text,env):
    def visit(t):
        if isinstance(t,str): return env.get(t,t)
        return tuple([t[0]]+[visit(x) for x in t[1:]])
    return a.ep.c.serialize(visit(a.ep.c.parse(text,'native')[0]))


def main():
    assert not DEST.exists(), 'preserve earlier evidence'
    result=dict(complete=False,failures=[])
    def save(): DEST.write_text(json.dumps(result,indent=2)+'\n')
    save()
    try:
        cert=read(OUT/'certificate.json')
        assert cert['complete'] and cert['failures']==[] and len(cert['rejections'])==7
        env={k:a.ep.c.parse(v,'native')[0] for k,v in cert['trans']['environment'].items()}
        original=ROOT/'scripts/balanced-slot/output/trans.native.jsonl.gz'
        transformed=OUT/'trans-substituted.native.jsonl.gz'
        count=0
        for left,right in zip_longest(records(original),records(transformed)):
            assert left is not None and right is not None
            expected=dict(f=subst(left['f'],env),rule=left['rule'])
            if left['rule']=='mp': expected['refs']=left['refs']
            else: expected['subs']={k:subst(v,env) for k,v in left['subs'].items()}
            assert expected==right, ('substituted original record',count)
            count+=1
        assert count==1449
        result['entire_original_trans_substituted_records']=count
        old=read(ROOT/'scripts/backward-zero/output/actual-zero-232-r1/locations.json')
        sup=read(ROOT/'scripts/backward-zero/output/actual-zero-232-r1/source-interface-ledger.json')
        oldcert=read(ROOT/'scripts/backward-zero/output/actual-zero-232-r1/certificate.json')
        reception=read(ROOT/oldcert['provenance']['prior'])
        loc=read(OUT/'locations.json'); shifted=copy.deepcopy(old); offset=loc['chain']['start']
        assert offset==1634 and loc['chain']['root']==offset+377086
        for imp in shifted['coordinate_imports']:
            for k in ('start','root'): imp[k]+=offset
        for row in shifted['rows']:
            for k in ('start','end'): row[k]+=offset
            row['required_roots']=[x+offset for x in row['required_roots']]
        assert shifted==loc['transported_chain']
        expected=[]
        for item in sup['nested_optional_occurrences']:
            new=dict(item); new['start']+=offset; new['end']+=offset; expected.append(new)
        assert expected==loc['optional_occurrences']
        locals_=[]
        for co,imp in enumerate(oldcert['imports']):
            for lo,item in enumerate(reception['imports']):
                locals_.append(dict(coordinate=co,local=lo,start=offset+imp['start']+item['start'],
                    lines=item['lines'],root=offset+imp['start']+item['root']))
        assert locals_==loc['local_occurrences']
        assert loc['nested_earlier_coordinate_root']==offset+122742+122741
        # Directly compare all forty original optional occurrences in each
        # output format. The rest of each local/coordinate occurrence is covered
        # by full chain equality and the separate audited input retention.
        syntax=a.Syntax(); wanted={m:{} for m in ('native','not-or')}
        for item in expected:
            package=reception['original_received'][item['optional']]
            original_rows=list(records(ROOT/package['path']))
            assert len(original_rows)==item['lines']==5
            for j,row in enumerate(original_rows):
                native=copy.deepcopy(row)
                if row['rule']=='mp': native['refs']=[x+item['start'] for x in row['refs']]
                image=copy.deepcopy(native)
                image['f']=syntax.text(syntax.parse(native['f']),True)
                if 'subs' in image: image['subs']={k:syntax.text(syntax.parse(v),True) for k,v in native['subs'].items()}
                for m,value in [('native',native),('not-or',image)]: wanted[m][item['start']+j]=value
        result['nested_optional_records_per_format']={}
        for m in wanted:
            matched=0
            for index,row in enumerate(records(OUT/f'output-zero.{m}.jsonl.gz')):
                if index in wanted[m]:
                    assert row==wanted[m][index], ('nested optional record',m,index)
                    matched+=1
                if index==max(wanted[m]): break
            assert matched==40
            result['nested_optional_records_per_format'][m]=matched
        result.update(transported_coordinate_occurrences=2,transported_local_occurrences=4,
            transported_optional_blocks=8,transported_source_row_root=offset+377086,
            original_chain_actual_final_root=377086,output_actual_final_root=cert['root'],
            qualification='Full primitive/image and all bridge/chain/substituted-trans records were checked in the main certificate. This supplement directly compares original trans specialization, transported maps and every nested original optional record; it does not repeat the full audit.')
        result['complete']=True; save()
        # The main accounting left 10000 bytes for growth; the supplement uses
        # its independently source-defined ancillary bound, not that allowance.
        assert DEST.stat().st_size<10000
        assert cert['actual_accounting']['ancillary_before_final_accounting_bytes']+20000<=cert['required']['metadata_bytes']
        print('PASS',count,'original trans records; 2 coordinate/4 local/8 optional maps;',
              '40 optional records/format; failures',result['failures'],'certificate',DEST.relative_to(ROOT),flush=True)
    except BaseException as error:
        result['complete']=False
        result['failures'].append(dict(type=type(error).__name__,message=str(error))); save(); raise


if __name__=='__main__': main()
