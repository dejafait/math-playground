"""Step 508: fixed parse-call census, excluding the separately audited source phase.

No original command is run; archives and production code are read-only.
"""
from collections import Counter
from pathlib import Path
import ast
import hashlib
import json
import sys
import time
import parameterized_input as p
import preflight_job7_transport as original

HERE = Path(__file__).resolve().parent
OUT = HERE/'output-508'
LIMIT, SECONDS, RESERVE = 100_000_000, 900, 1_000_000


def main():
    p.require(not OUT.exists(), 'fresh output only')
    OUT.mkdir()
    start = time.monotonic()
    counts = Counter()
    report = dict(status='IN_PROGRESS', historical_failure_program_preserved=False,
                  total_work_bound=False, graph_regeneration=False,
                  word_expansion=False, coordinate_search=False, checks=[], parses=[])
    original_hook = p.no_duplicates

    def tick(kind, n=1):
        p.require(sum(counts.values())+n <= LIMIT, 'selected audit item/event ceiling')
        counts[kind] += n
        if counts[kind] % 4096 == 0:
            p.require(time.monotonic()-start < SECONDS, 'audit timer')

    def equal(a,b):
        tick('full_value_comparisons')
        if type(a) is not type(b): return False
        if type(a) is list:
            return len(a)==len(b) and all(equal(x,y) for x,y in zip(a,b))
        if type(a) is dict:
            return a.keys()==b.keys() and all(equal(a[k],b[k]) for k in a)
        return a==b

    def call(path, mode, label, expected_error=None):
        # Original source loops, not this wrapper, imply the scan total.
        raw = p.read_bytes(HERE/path, 'certificate_bytes')
        text = raw.decode('utf-8', errors='strict')
        expected_hooks=[]
        def independent_hook(pairs):
            result={}; keys=[]
            for key,value in pairs:
                tick('independent_duplicate_pairs')
                p.require(key not in result, 'independent duplicate rejection')
                result[key]=value;keys.append(key)
            expected_hooks.append(keys)
            return result
        def reject(token):
            raise ValueError('noninteger JSON number: '+token[:40])
        def integer(token):
            tick('independent_integer_tokens')
            p.require(len(token)<=12, 'independent strict integer cap')
            return int(token)
        options=dict(object_pairs_hook=independent_hook,parse_constant=reject)
        if mode=='strict':options.update(parse_float=reject,parse_int=integer)
        expected=None;oracle_error=None
        try: expected=json.loads(text,**options)
        except ValueError as err:oracle_error=str(err)
        p.require((oracle_error is not None)==(expected_error is not None), 'oracle failure scope')
        if expected_error is not None:
            p.require(oracle_error==expected_error,'independent exact rejected token')
        hook_index=0; pair_count=0
        def checked_hook(pairs):
            nonlocal hook_index,pair_count
            tick('original_hook_invocations')
            p.require(hook_index<len(expected_hooks),'no unexpected hook')
            keys=expected_hooks[hook_index]
            p.require(len(pairs)==len(keys),'complete hook pair length')
            for (key,_),expected_key in zip(pairs,keys):
                tick('complete_hook_key_comparisons')
                p.require(type(key) is str and key==expected_key,'complete ordered hook keys')
            hook_index+=1;pair_count+=len(pairs)
            return original_hook(pairs)
        p.no_duplicates=checked_hook
        actual=None;error=None
        try:
            if mode=='strict':actual=p.parse(raw)
            elif mode=='metadata':
                actual=json.loads(raw,object_pairs_hook=p.no_duplicates,parse_constant=p.reject_number)
            elif mode=='inventory_metadata':actual=json.loads(raw,object_pairs_hook=p.no_duplicates)
            else:raise AssertionError(mode)
        except p.Rejected as err:error=str(err)
        finally:p.no_duplicates=original_hook
        p.require(hook_index==len(expected_hooks),'all hook invocations received')
        p.require(error==expected_error,'exact original success/failure boundary')
        if error is None:p.require(equal(actual,expected),'full decoded value equality')
        p.require(p.read_bytes(HERE/path,'certificate_bytes')==raw,'unchanged complete input bytes')
        report['parses'].append(dict(label=label,path=path,mode=mode,utf8_bytes=len(raw),
            strict_scan_characters=len(text) if mode=='strict' else 0,
            completed_hook_invocations=hook_index,completed_key_pair_visits=pair_count,
            output_equal=error is None,expected_error=error,all_hook_sequences_checked=True))
        p.require(time.monotonic()-start<SECONDS,'complete parse block timer')

    try:
        p.require(p.CAPS==original.EXPECTED_CAPS,'unchanged CAPS')
        p.require(sys.gettrace() is None,'no source observer active in isolated parser audit')
        # Pin the exact source bodies; method calls in supplements are inspected
        # in the canonical proof, and retained verbatim here for reproducibility.
        programs=['preflight_job7_transport.py','check_job7_preflight_accounting.py',
                  'check_job7_inventory_fields.py','parameterized_input.py']
        report['source_snapshots']={}
        for name in programs:
            raw=(HERE/name).read_bytes(); tick('source_snapshot_bytes',len(raw))
            (OUT/name).write_bytes(raw)
            report['source_snapshots'][name]=dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
        report['parse_call_inventory']=[]
        for name in programs[:3]:
            module=ast.parse((HERE/name).read_text())
            for node in ast.walk(module):
                tick('source_ast_nodes')
                if isinstance(node,ast.Call) and isinstance(node.func,ast.Attribute) and (
                    isinstance(node.func.value,ast.Name) and
                    (node.func.value.id,node.func.attr) in [('p','parse'),('p','load'),('json','loads')]):
                    report['parse_call_inventory'].append(dict(program=name,line=node.lineno,call=ast.unparse(node)))
        report['checks'].append('complete explicit parse/load/loads call-site AST census retained')
        manifest=json.loads((HERE/'output-502/manifest.json').read_bytes())
        p.require(manifest['binding_paths']==original.BIND_PATHS,'exact eight binding paths')
        p.require(manifest['script_sha256']==report['source_snapshots'][programs[0]]['sha256'],
                  'original primary source digest match')
        for path in manifest['binding_paths']:
            if not path.endswith('proof.jsonl'):
                call(path,'strict','primary binding')
        call('output-502/preflight.json','metadata','accounting supplement report')
        call('output-502/manifest.json','metadata','accounting supplement manifest')
        call('output-489/trace/event-02642.json','strict','accounting supplement event')
        call('output-491/retained-interior-bound.json','strict','accounting supplement prior')
        call('output-502/accounting-check.json','inventory_metadata','inventory supplement receipt')
        for path in original.BIND_PATHS[:3]:call(path,'strict','inventory supplement archive')
        failure=json.loads((HERE/'output-502/helper-first-read.failure.json').read_bytes())
        prefix='parameterized_input.Rejected: '
        p.require(failure['error'].startswith(prefix) and failure['item_walk_started'] is False,
                  'preserved isolated failure scope')
        call('output-502/preflight.json','strict','isolated failed-load reconstruction',
             failure['error'][len(prefix):])
        groups={}
        for row in report['parses']:
            g=groups.setdefault(row['label'],dict(calls=0,key_pairs=0,strict_characters=0,read_bytes=0))
            g['calls']+=1;g['key_pairs']+=row['completed_key_pair_visits']
            g['strict_characters']+=row['strict_scan_characters'];g['read_bytes']+=row['utf8_bytes']
        successful=[row for row in report['parses'] if row['expected_error'] is None]
        success_pairs=sum(row['completed_key_pair_visits'] for row in successful)
        failed_pairs=report['parses'][-1]['completed_key_pair_visits']
        report.update(status='PARSER_LEDGER_CLASS_RECONCILED',groups=groups,
            new_successful_key_pair_omissions=success_pairs,
            reconstructed_failed_key_pairs=failed_pairs,
            historical_successful_partial_item_total=75_386_624+success_pairs,
            conditional_total_including_reconstructed_failure=75_386_624+success_pairs+failed_pairs,
            new_successful_separate_character_scans=sum(row['strict_scan_characters'] for row in successful),
            source_phase_pairs_already_accounted=730,source_phase_separate_scans_already_recorded=104_048,
            historical_failure_qualification='Exact failed p.load is reproducible on retained preflight bytes and matches saved error; historical failed program/other work not preserved, so complete historical work remains UNKNOWN.',
            item_qualification='Count each parser object-pair loop traversal separately from subsequent object walks/comparisons. Character scans and bytes are separate measures, not added to item subtotal.',
            unverified='Implicit/C-decoder/read/UTF-8/bit/index and complete failure/supplement work; independent graph/transport/schema/byte/live peaks; all coordinates/equalities; total interpreter resources.')
        report['checks'].append('all selected parse outputs, hook sequences and exact isolated failure match')
    except Exception as err:
        report.update(status='FAILED',failure=dict(type=type(err).__name__,message=str(err)))
    finally:
        p.no_duplicates=original_hook
        report.update(audit_units=dict(counts),audit_units_total=sum(counts.values()),
                      required_audit_units=LIMIT,elapsed_seconds=time.monotonic()-start,
                      required_seconds=SECONDS,required_evidence_bytes=200_000_000,reserve_bytes=RESERVE)
        used=sum(x.stat().st_size for x in OUT.iterdir() if x.is_file())+Path(__file__).stat().st_size
        report['program_and_evidence_bytes']=0
        while True:
            raw=json.dumps(report,ensure_ascii=True,separators=(',',':')).encode()
            n=used+len(raw)
            if report['program_and_evidence_bytes']==n:break
            report['program_and_evidence_bytes']=n
        p.require(n<RESERVE,'full source snapshots/program/receipt reserve')
        with (OUT/'parser-ledger.json').open('xb') as stream:stream.write(raw)
    print(json.dumps(dict(status=report['status'],new_key_pairs=report.get('new_successful_key_pair_omissions'),
        partial_item_total=report.get('historical_successful_partial_item_total'),
        required_item_limit=LIMIT,audit_units=sum(counts.values()),bytes=n,reserve=RESERVE,
        failures=report.get('failure'),path=str(OUT/'parser-ledger.json'))))
    return 0 if report['status']=='PARSER_LEDGER_CLASS_RECONCILED' else 1

if __name__=='__main__':raise SystemExit(main())
