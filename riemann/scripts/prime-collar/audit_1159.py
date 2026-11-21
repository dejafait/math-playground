#!/usr/bin/env python3
"""Audit frozen1157 without changing the family, grid or original artifacts.

Replay the reviewed calculation/backend, instrument every outward dump,
probe the C ABI, and independently reconstruct every rectangle with exact
rationals. This is not an independent transcendental implementation.
Analytic obligations and platform qualifications remain in C750l.
"""
import contextlib
import ctypes as ct
from fractions import Fraction as F
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
from unittest.mock import patch

sys.dont_write_bytecode = True
here = Path(__file__).resolve().parent
root = here.parents[1]
source = here/'certify_1157.py'
original_path = here/'certificate-1157.json'
replay_path = here/'certificate-1157-replay-1159.json'
original_bytes = original_path.read_bytes()
original = json.loads(original_bytes)
preserved = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
             for p in here.glob('*1157*') if p.is_file()}
write_text = Path.write_text
load_module = importlib.util.spec_from_file_location
decimal_checks = {'endpoints_checked': 0, 'failures': []}


def exact_binary(m, value):
    assert m.lib.mpfr_number_p(ct.byref(value.raw))
    exponent = ct.c_long()
    p = m.lib.mpfr_get_str(None, ct.byref(exponent), 2, m.PREC,
                          ct.byref(value.raw), m.DOWN)
    digits = ct.string_at(p).decode()
    m.lib.mpfr_free_str(p)
    n = len(digits.lstrip('-'))
    mantissa = int(digits, 2)
    if mantissa == 0:
        return F(0)
    return F(mantissa) * F(2)**(exponent.value-n)


def audited_spec(*args, **kwargs):
    spec = load_module(*args, **kwargs)
    exec_module = spec.loader.exec_module

    def instrument(m):
        exec_module(m)
        original_dump = m.I.dump

        def checked_dump(interval):
            result = original_dump(interval)
            lo, hi = map(F, result)
            passed = lo <= exact_binary(m, interval.lo) <= exact_binary(m, interval.hi) <= hi
            decimal_checks['endpoints_checked'] += 2
            if not passed:
                decimal_checks['failures'].append(result)
            return result

        m.I.dump = checked_dump

    spec.loader.exec_module = instrument
    return spec


def redirect(path, data, *args, **kwargs):
    assert path.resolve() == original_path, f'Unexpected write: {path}'
    return write_text(replay_path, data, *args, **kwargs)


print('Replaying all frozen1157 nodes and checking every decimal endpoint.', flush=True)
with patch.object(Path, 'write_text', redirect), \
     patch.object(importlib.util, 'spec_from_file_location', audited_spec), \
     contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(source))
c = json.loads(replay_path.read_text())
bk = ns['bk']
print('Replay complete; checking ABI and complete exact-rational reconstruction.', flush=True)

with tempfile.TemporaryDirectory(prefix='.abi1159-', dir=here) as work:
    exe = Path(work)/'probe'
    subprocess.run(['cc', '-std=c11', '-I/opt/homebrew/include',
                    str(here/'abi_1146.c'), '-L/opt/homebrew/lib',
                    '-Wl,-rpath,/opt/homebrew/lib', '-lmpfr', '-lgmp',
                    '-o', str(exe)], check=True)
    abi = json.loads(subprocess.check_output([str(exe)], text=True))
sizes = [ct.sizeof(bk.Raw), ct.sizeof(ct.c_long), ct.sizeof(ct.c_int),
         ct.sizeof(ct.c_long), ct.sizeof(ct.c_ulong)]
offsets = [getattr(bk.Raw, key).offset for key in ('prec','sign','exp','limbs')]

checks = {
    'all_replayed_fields_identical': c == original,
    'original_bytes_preserved': original_path.read_bytes() == original_bytes,
    'source_hash_matches': hashlib.sha256(source.read_bytes()).hexdigest() == c['script_sha256'],
    'backend_hash_matches': hashlib.sha256(ns['BACKEND'].read_bytes()).hexdigest() == c['backend_sha256'],
    'no_original_verification_failures': c['verification_failures'] == [],
    'original_claims_hold': len(c['claims']) == 8 and all(c['claims'].values()),
    'outward_conversion_all_endpoints': not decimal_checks['failures'],
    'abi_sizes': abi['sizes'] == sizes,
    'abi_offsets': abi['offsets'] == offsets,
    'abi_rounding': abi['rounding'] == [bk.DOWN,bk.UP] == [3,2],
    'abi_version_precision': abi['version'] == abi['header_version'] == c['mpfr_version'] == '4.2.2'
        and abi['precision'] == bk.PREC == c['precision_bits'] == 384,
    'fixed_mesh': (c['quadrature']['first_exponent'], c['quadrature']['last_exponent'],
                   c['quadrature']['panels_per_octave'], c['quadrature']['total_panels'])
                  == (-24,4,2048,57344),
    'fixed_integrand_order': c['quadrature']['integrand_order'] == ['A_w','A_middle','K_adjacent','K_far'],
    'all_nodes_present': len(c['nodes']) == 57345,
    'all_blocks_present': len(c['cumulative_octave_bounds']) == 28,
}

def read(x):
    assert len(x) == 2
    lo, hi = map(F,x)
    assert lo <= hi
    return lo,hi

def add(x,y):
    return x[0]+y[0],x[1]+y[1]

def neg(x):
    return -x[1],-x[0]

def sub(x,y):
    return add(x,neg(y))

def mul(x,y):
    vals = [u*v for u in x for v in y]
    return min(vals),max(vals)

def div(x,y):
    assert y[0] > 0
    return mul(x,(1/y[1],1/y[0]))

def sq(x):
    assert x[0] > 0 or x[1] < 0
    return min(x[0]**2,x[1]**2),max(x[0]**2,x[1]**2)

def enc(x):
    return [str(v) for v in x]

nodes, blocks = c['nodes'], c['cumulative_octave_bounds']
lo_sums, hi_sums = [F(0)]*4,[F(0)]*4
node_failures, block_records = [],[]
previous = None
for index,node in enumerate(nodes):
    if index == 0:
        expected_s = F(1,2**24)
    else:
        octave,panel0 = divmod(index-1,2048)
        exponent,panel = octave-24,panel0+1
        width = F(2)**exponent/2048
        expected_s = F(2)**exponent*(2048+panel)/2048
    passed = read(node['s']) == (expected_s,expected_s) and len(node['values']) == 4
    values = [read(v) for v in node['values']]
    passed = passed and all(0 < lo <= hi for lo,hi in values)
    if not passed:
        node_failures.append(index)
    if previous is not None:
        for j in range(4):
            lo_sums[j] += width*values[j][0]
            hi_sums[j] += width*previous[j][1]
    previous = values
    if index and panel == 2048:
        block = blocks[octave]
        block_ordered = block['octave_exponent'] == exponent
        for key in ('cumulative_lower','cumulative_upper'):
            block_ordered = block_ordered and len(block[key]) == 4
            block_ordered = block_ordered and all(read(x)[0] > 0 for x in block[key])
        block_ordered = block_ordered and all(lo_sums[j] <= hi_sums[j] for j in range(4))
        block_records.append({'exponent':exponent, 'valid':block_ordered,
                              'independent_rectangle_enclosures':
                              [enc((lo_sums[j],hi_sums[j])) for j in range(4)]})
checks['every_node_geometry_order_sign'] = not node_failures
checks['every_block_exact_rational_reconstructed'] = len(block_records) == 28 and all(x['valid'] for x in block_records)

geometry = {k:read(v) for k,v in c['geometry'].items()}
a,w,mid,r,k = [geometry[x] for x in ('a','w','middle_length','r','k')]
delta,S = read(c['quadrature']['delta']),read(c['quadrature']['S'])
checks['delta_S_exact'] = delta == (F(1,2**24),)*2 and S == (F(16),)*2
checks['all_tail_and_overlap_hypotheses'] = (a == (F(9,4),)*2 and 0 < delta[0] < w[0]
    and w[1] < mid[0] and w[1] < a[0] < r[0] and r[0] > w[1])
pi_dump,log2_dump = ns['pi'].dump(),ns['log2'].dump()
pi,log2 = read(pi_dump),read(log2_dump)
small,large = [list(map(read,c[key])) for key in ('small_s_upper','large_s_upper')]
checks['complete_positive_tail_allowances'] = len(small) == len(large) == 4 and all(v[0] > 0 for v in small+large)
small_bounds = ['1.919e-6','2.482e-6','9.521e-7','4.734e-12']
large_bounds = ['4.903e-17','5.981e-15','4.309e-18','3.841e-20']
checks['all_small_display_bounds'] = all(v[1] < F(b) for v,b in zip(small,small_bounds))
checks['all_large_display_bounds'] = all(v[1] < F(b) for v,b in zip(large,large_bounds))
integrals = [div((lo_sums[j],hi_sums[j]+small[j][1]+large[j][1]),pi) for j in range(4)]
Aw,Am = add(mul(w,log2),integrals[0]),add(mul(mid,log2),integrals[1])
EE = mul((F(2),)*2,sub(Aw,integrals[3]))
EM = mul((F(-2),)*2,integrals[2])
MM = Am
threshold = mul((F(8),)*2,mul(k,w))
minimum = sub(sub(EE,div(sq(EM),MM)),threshold)
amplitude = div(neg(EM),MM)
determinant = sub(mul(EE,MM),sq(EM))
checks['independent_positive_response_and_gram'] = MM[0] > 0 and determinant[0] > 0
checks['independent_negative_cross'] = EM[1] < 0
bounds = {'EE':('0.29695626','0.29704288'), 'EM':('-0.11841990','-0.11837759'),
          'MM':('4.26144969','4.26187214'), 'threshold':('0.29282701','0.29282702'),
          'amplitude':('0.02777596','0.02778865'), 'minimum':('0.00083852','0.00092782')}
independent = dict(EE=EE,EM=EM,MM=MM,threshold=threshold,amplitude=amplitude,minimum=minimum)
saved = dict(EE=read(c['matrix'][0][0]),EM=read(c['matrix'][0][1]),MM=read(c['matrix'][1][1]),
             threshold=read(c['required_threshold']),amplitude=read(c['minimizing_amplitude']),
             minimum=read(c['minimum_margin']))
for name,(lower,upper) in bounds.items():
    for label,vals in [('all_node',independent),('saved',saved)]:
        checks[label+'_'+name+'_strict_display_bounds'] = F(lower) < vals[name][0] <= vals[name][1] < F(upper)
checks['matrix_symmetric'] = c['matrix'][0][1] == c['matrix'][1][0]
printed_minimum = sub(sub(saved['EE'],div(sq(saved['EM']),saved['MM'])),saved['threshold'])
checks['printed_matrix_minimum_independently_decisive'] = F('0.00083852') < printed_minimum[0] <= printed_minimum[1] < F('0.00092782')
checks['initial_failed_containment_preserved'] = json.loads((here/'certificate-output-check-1157-initial.json').read_text())['failures'] == ['all_28_cumulative_blocks_valid']
checks['all_original1157_artifacts_preserved'] = all(hashlib.sha256((root/p).read_bytes()).hexdigest() == h for p,h in preserved.items())
checks['nonnegative_test_requirement_exceeded'] = minimum[0] > 0
failures = [key for key,ok in checks.items() if not ok]
out = {
    'scope':'C750l fixed real middle-indicator family, original full J, exact original mesh; no retuning.',
    'independence':'Reviewed original source/backend replay; exact rational all-node reconstruction and fresh C ABI probe; no independent transcendental implementation or formal platform proof.',
    'abi':abi, 'ctypes_sizes':sizes, 'ctypes_offsets':offsets, 'backend_library':bk.lib_path,
    'decimal_checks':decimal_checks, 'full_node_count':len(nodes), 'full_integrand_count':4*len(nodes),
    'node_failures':node_failures, 'full_block_records':block_records,
    'all_node_integrals_exact_rational':[enc(v) for v in integrals],
    'all_node_matrix_and_minimum_exact_rational':{key:enc(value) for key,value in independent.items()},
    'printed_matrix_minimum_exact_rational':enc(printed_minimum),
    'pi':pi_dump,'log2':log2_dump,
    'small_s_upper':c['small_s_upper'],'large_s_upper':c['large_s_upper'],
    'geometry':c['geometry'],'display_bounds':bounds,'required_minimum':'>=0',
    'checks':checks,'failures':failures,'preserved_artifact_hashes':preserved,
    'original_sha256':hashlib.sha256(original_bytes).hexdigest(),
    'replay_sha256':hashlib.sha256(replay_path.read_bytes()).hexdigest(),
    'audit_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'abi_source_sha256':hashlib.sha256((here/'abi_1146.c').read_bytes()).hexdigest(),
    'replay_path':str(replay_path.relative_to(root)),
    'limitations':'Only this family is excluded; arbitrary interior response, complete budget, J-to-baseline and actual-Xi transfer unresolved.',
}
path = here/'certificate-audit-1159.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print('Audit checks:',sum(checks.values()),'required:',len(checks),'; failures:',failures)
print('Nodes:',len(nodes),'integrands:',4*len(nodes),'blocks:',len(block_records),'outward endpoints:',decimal_checks['endpoints_checked'])
print('Actual certified minimum: (0.00083852, 0.00092782); required: >=0.')
print('ABI MPFR:',abi['version'],'precision:',abi['precision'],'sizes:',sizes,'offsets:',offsets)
print('Full replay:',replay_path)
print('Full audit certificate:',path)
if failures:
    raise SystemExit(1)
