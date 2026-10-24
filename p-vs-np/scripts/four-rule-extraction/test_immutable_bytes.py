"""Step 466: bounded interface regressions; old archives are read only.

No source proof synthesis and no all-size resource theorem are attempted.
"""
import ast
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
import platform
from pathlib import Path
from unittest.mock import patch

import parameterized_input as p
import receive_parameterized as receiver

HERE = Path(__file__).resolve().parent
OUT = HERE/'output-466'
CHECKER = HERE.parent/'parity-four-rule/checker.py'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def write(name, value):
    p.write_json(OUT/name, value)


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def verdict(call):
    try:
        return dict(accepted=True, receipt=call())
    except Exception as error:
        return dict(accepted=False, exception=type(error).__name__, reason=str(error))


def equivalent_engine():
    old = ast.parse((OUT/'checker-before.py').read_text())
    new = ast.parse(CHECKER.read_text())
    f = next(x for x in old.body if isinstance(x, ast.FunctionDef) and x.name == 'check')
    g = next(x for x in new.body if isinstance(x, ast.FunctionDef) and x.name == '_check_stream')
    assert isinstance(f.body[3], ast.With)
    body = f.body[1:3]+f.body[3].body+f.body[4:]
    assert ast.dump(ast.Module(body=body, type_ignores=[])) == ast.dump(
        ast.Module(body=g.body, type_ignores=[]))
    return dict(original_engine_ast_equal=True,
                qualification='Expected-tree normalization remains in both public wrappers.')


def checker_tests(old, new):
    fixtures, framing, mutations = [], [], []
    tags = set()
    for folder in sorted((HERE/'output-457').iterdir()):
        source, request = folder/'source.jsonl', folder/'request.json'
        if not source.is_file() or not request.is_file():
            continue
        req = p.load(request, 'input_bytes')
        raw = source.read_bytes()
        a = verdict(lambda: old.check(source, req['goal']))
        b = verdict(lambda: new.check(source, req['goal']))
        with patch.object(Path, 'open', side_effect=AssertionError('byte checker opened a path')):
            c = verdict(lambda: new.check_bytes(raw, req['goal'], len(raw)))
        assert a == b == c and a['accepted'], folder
        q, retained, rows, receipt = p.request(source, request)
        assert p.exact_equal(q, req) and retained == raw and receipt == a['receipt']
        assert rows == [p.parse(x) for x in raw.splitlines()][1:]
        tags.update(receipt['rule_counts'])
        fixtures.append(dict(name=folder.name, path=str(source.relative_to(HERE)),
                             bytes_actual=len(raw), bytes_required=len(raw),
                             path_before=a, path_after=b, immutable_bytes=c,
                             complete_request_records_and_dictionary_retained=True))
    assert tags == {'axiom','true','not-false','expansion','contraction','association','cut'}
    source = HERE/'output-457/old-nonzero/source.jsonl'
    raw = source.read_bytes()
    header, *rows = [p.parse(x) for x in raw.splitlines()]
    goal = header['goal']
    variants = dict(LF=raw, CRLF=raw.replace(b'\n',b'\r\n'),
                    missing_final_LF=raw[:-1], blank_line=raw.replace(b'\n',b'\n\n',1),
                    lone_CR=raw.replace(b'\n',b'\r'),
                    internal_CR=raw.replace(b'"format":',b'"format"\r:',1))
    for name, data in variants.items():
        path = OUT/('framing-'+name+'.jsonl')
        path.write_bytes(data)
        a, b, c = verdict(lambda: old.check(path,goal)), verdict(lambda:new.check(path,goal)), verdict(
            lambda:new.check_bytes(data,goal,len(data)))
        assert a == b == c, name
        assert a['accepted'] == (name not in ('blank_line','lone_CR')), name
        framing.append(dict(name=name,path=str(path.relative_to(HERE)),
                            bytes_actual=len(data),bytes_required=len(data),
                            path_before=a,path_after=b,immutable_bytes=c))
    for tag in sorted(tags):
        damaged = copy.deepcopy(rows)
        index = next(i for i,r in enumerate(damaged) if r['rule']==tag)
        damaged[index]['f'] = 'false'
        data = ('\n'.join(json.dumps(x,separators=(',',':')) for x in [header]+damaged)+'\n').encode()
        path = OUT/('literal-'+tag+'.jsonl')
        path.write_bytes(data)
        a, b, c = verdict(lambda:old.check(path,goal)), verdict(lambda:new.check(path,goal)), verdict(
            lambda:new.check_bytes(data,goal,len(data)))
        assert a == b == c and not a['accepted'], tag
        mutations.append(dict(tag=tag,path=str(path.relative_to(HERE)),
                              path_before=a,path_after=b,immutable_bytes=c))
    for name, expected in [('header-endpoint','true'), ('last-endpoint',rows[-2]['f'])]:
        data = raw
        if name == 'last-endpoint':
            h = dict(header,goal=expected)
            data = (json.dumps(h,separators=(',',':')).encode()+b'\n'+raw.split(b'\n',1)[1])
        path = OUT/(name+'.jsonl')
        path.write_bytes(data)
        a,b,c = verdict(lambda:old.check(path,expected)), verdict(lambda:new.check(path,expected)), verdict(
            lambda:new.check_bytes(data,expected,len(data)))
        assert a == b == c and not a['accepted'], name
        mutations.append(dict(test=name,path_before=a,path_after=b,immutable_bytes=c))
    cap_cases = []
    class BytesSubclass(bytes):
        pass
    cases = [('overflow',raw,len(raw)-1),('negative-limit',raw,-1),
             ('bool-limit',raw,True),('float-limit',raw,float(len(raw))),
             ('bytearray',bytearray(raw),len(raw)),('memoryview',memoryview(raw),len(raw)),
             ('string',raw.decode(),len(raw)),('bytes-subclass',BytesSubclass(raw),len(raw))]
    for name,data,limit in cases:
        with patch.object(new,'_check_stream',side_effect=AssertionError('parsed before cap/type check')):
            result = verdict(lambda:new.check_bytes(data,object(),limit))
        assert not result['accepted'] and result['exception']=='Invalid', name
        cap_cases.append(dict(test=name,bytes_actual=len(data),byte_limit=limit,result=result))
    return dict(fixtures=fixtures,framing=framing,primitive_rejections=mutations,
                preparse_cap_and_type_rejections=cap_cases,tags=sorted(tags))


def guarded_reads():
    source = HERE/'output-457/old-nonzero/source.jsonl'
    request = source.with_name('request.json')
    raw = source.read_bytes()
    original_open = Path.open
    original_spec = importlib.util.spec_from_file_location
    reports = []
    variants = dict(stable=raw, whitespace=raw.replace(b'"format":',b'"format" :',1),
                    oversized=b' '*(p.CAPS['input_bytes']+1),
                    deep=b'['*(p.CAPS['json_depth']+1)+b']'*(p.CAPS['json_depth']+1),
                    malformed=b'not JSON')
    for name,replacement in variants.items():
        reads, calls, parsed, first = [], [], [], []
        original_parse = p.parse
        class Trace(io.BytesIO):
            def read(self,n=-1):
                assert n == p.CAPS['input_bytes']+1
                data = super().read(n)
                reads.append(dict(requested=n,returned=len(data),sha256=sha(data)))
                if len(reads)==1:
                    first.append(data)
                return data
        def opened(path,*args,**kwargs):
            if path == source and args and args[0]=='rb':
                assert len(reads)<2, 'third source open'
                return Trace(raw if not reads else replacement)
            return original_open(path,*args,**kwargs)
        def tracked_parse(data):
            parsed.append(sha(data if type(data) is bytes else data.encode()))
            return original_parse(data)
        def spec(name,path):
            result = original_spec(name,path)
            execute = result.loader.exec_module
            def instrument(mod):
                execute(mod)
                original_bytes = mod.check_bytes
                def checked(data,goal,limit):
                    assert type(data) is bytes and data is first[0] and data == raw
                    assert limit == p.CAPS['input_bytes']
                    with patch.object(Path,'open',side_effect=AssertionError('byte checker opened a path')):
                        receipt = original_bytes(data,goal,limit)
                    calls.append(dict(bytes_actual=len(data),bytes_required=limit,receipt=receipt,
                                      first_retained_object=True,no_path_open=True))
                    return receipt
                mod.check_bytes = checked
                mod.check = lambda *a: (_ for _ in ()).throw(AssertionError('legacy path used'))
            result.loader.exec_module = instrument
            return result
        with patch.object(Path,'open',opened), patch.object(p,'parse',tracked_parse), patch.object(
                p.importlib.util,'spec_from_file_location',spec):
            try:
                req,retained,records,receipt = p.request(source,request)
                result = dict(accepted=True,receipt=receipt)
            except p.Rejected as error:
                result = dict(accepted=False,reason=error.args[0])
        assert len(reads)==2, name
        assert len(calls)==(1 if name=='stable' else 0), name
        assert result['accepted'] == (name=='stable'), name
        if name not in ('stable','oversized'):
            assert result['reason']=='source changed during checking', name
        if name=='oversized':
            assert result['reason']['actual']==p.CAPS['input_bytes']+1
            assert result['reason']['required']==p.CAPS['input_bytes']
        assert name=='stable' or sha(replacement) not in parsed
        reports.append(dict(test=name,replacement_bytes=len(replacement),
                            replacement_sha256=sha(replacement),reads=reads,
                            checker_calls=calls,result=result,replacement_never_parsed=name!='stable'))
    assert source.read_bytes()==raw
    return reports


def regressions():
    import test_parameterized as driver
    driver.OUT = OUT/'replay'
    driver.OUT.mkdir(exist_ok=True)
    with (OUT/'replay.log').open('w') as log, contextlib.redirect_stdout(log):
        driver.main()
    summary = p.load(driver.OUT/'summary.json')
    assert summary['accepted_cases']==6 and summary['accepted_roots']==35
    assert summary['rejected']==47 and not summary['failures']
    old_mutations = p.load(HERE/'output-457/mutation-results.json')
    new_mutations = p.load(driver.OUT/'mutation-results.json')
    assert len(old_mutations)==len(new_mutations)
    for a,b in zip(old_mutations,new_mutations):
        assert a['name']==b['name'] and a['accepted']==b['accepted']
        # Only output paths may differ in cap diagnostics.
        assert a.get('reason','').replace('output-457','output-466/replay')==b.get('reason','')
    for item in p.load(driver.OUT/'accepted-cases.json'):
        name = item['name']
        for file in ('source.jsonl','request.json','certificate.json'):
            assert (HERE/'output-457'/name/file).read_bytes()==(driver.OUT/name/file).read_bytes()
    foreign = verdict(lambda:receiver.receive(HERE/'output-457/singleton/certificate.json',
        HERE/'output-457/old-nonzero/source.jsonl',HERE/'output-457/old-nonzero/request.json'))
    assert foreign == dict(accepted=False,exception='Rejected',reason='source retention')
    return dict(summary=summary,all_accepted_certificates_byte_identical=True,
                all_mutation_verdicts_and_reasons_match=True,foreign_caller=foreign)


def main():
    old = module('step466_baseline',OUT/'checker-before.py')
    new = module('step466_current',CHECKER)
    write('engine-comparison.json',equivalent_engine())
    checks = checker_tests(old,new)
    write('checker-tests.json',checks)
    races = guarded_reads()
    write('guarded-reads.json',races)
    replay = regressions()
    write('regression-comparison.json',replay)
    before = p.load(OUT/'archives-before.json')
    after = {path:sha(Path(path).read_bytes()) for path in before}
    assert before==after
    write('archive-preservation.json',dict(files=len(before),unchanged=True,hashes=after))
    result = dict(accepted=True,failures=[],python=platform.python_version(),
                  fixtures=len(checks['fixtures']),framing_cases=len(checks['framing']),
                  primitive_endpoint_rejections=len(checks['primitive_rejections']),
                  cap_type_rejections=len(checks['preparse_cap_and_type_rejections']),
                  guarded_read_cases=len(races),replay_accepted=6,replay_rejections=47,
                  preserved_archive_files=len(before),
                  source_bytes_actual_max=max(x['bytes_actual'] for x in checks['fixtures']),
                  source_bytes_required=p.CAPS['input_bytes'],
                  scripts={str(path.relative_to(HERE.parent.parent)):sha(path.read_bytes())
                           for path in (CHECKER,HERE/'parameterized_input.py',Path(__file__))},
                  limitations=['No total interpreter work/memory or blocking-latency bound',
                               'No positive occurrence endpoint proof or full H composition',
                               'Trusted caller paths and SHA assumptions persist',
                               'No proof existence, universal witness or SAT conclusion'])
    write('verification.json',result)
    print(json.dumps(dict(result,evidence=str(OUT/'verification.json'))))


if __name__=='__main__':
    try:
        main()
    except Exception as error:
        write('failure.json',dict(accepted=False,failure=repr(error)))
        raise
