#!/usr/bin/env python3
"""Bounded L039 audit; preserve inputs, replay full evidence, test persistence.

Arithmetic implications are justified in L039, not by success flags here.
Run from the active notebook root. No builder is imported or executed.
"""
import copy
import hashlib
import importlib.util
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path

ROOT = Path('scripts/conductor-eleven')
OUT = ROOT/'critical-audit'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2)+'\n')


def read(path):
    return json.loads(path.read_text())


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    checks, failures, evidence = {}, [], {}

    def need(label, condition):
        checks[label] = bool(condition)
        if not condition:
            raise ValueError(label)

    files = [ROOT/x for x in ('certify_arithmetic.py', 'arithmetic-input.json',
             'arithmetic-certificate.json', 'structural-certificate.json',
             'dual-certificate.json', 'dual-verification.json',
             'dual-verification-structure/general-verification.json')]
    files += [Path('scripts')/folder/name for folder in ('general-relative', 'dual-kernel')
              for name in ('build_certificate.py', 'verify_certificate.py')]
    files += [Path(__file__).relative_to(Path.cwd()) if Path(__file__).is_absolute() else Path(__file__)]
    before = {str(p): sha(p) for p in files}
    try:
        for p in files:
            dest = OUT/'originals'/p
            dest.parent.mkdir(parents=True, exist_ok=True)
            if not dest.exists():
                dest.write_bytes(p.read_bytes())
            need('preserved '+str(p), sha(dest) == before[str(p)])
        write(OUT/'pre-replay-manifest.json', before)

        ar, old = read(ROOT/'arithmetic-input.json'), read(ROOT/'arithmetic-certificate.json')
        need('fixed model and conditional input', ar['model'] == [0,-1,1,-10,-20]
             and ar['conductor'] == 11 and ar['certification'] == 'SUPPLIED_CONDITIONAL')
        # Independently use the c4,c6 identity to compute Delta, then compare
        # the producer's b-invariant discriminant expression and all values.
        a1,a2,a3,a4,a6 = ar['model']
        b2,b4,b6 = a1*a1+4*a2, a1*a3+2*a4, a3*a3+4*a6
        b8 = a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
        c4,c6 = b2*b2-24*b4, -b2**3+36*b2*b4-216*b6
        delta = Fraction(c4**3-c6**2,1728)
        invariants = dict(zip(('b2','b4','b6','b8','c4','c6','Delta'),
                              (b2,b4,b6,b8,c4,c6,int(delta))))
        need('complete invariant comparison', delta.denominator == 1 and invariants == old['invariants'])
        need('prime and complete factorization', all(11 % q for q in range(2,isqrt(11)+1))
             and delta == -11**5 and old['discriminant_factorization'] == {'sign':-1,'factors':[[11,5]]})
        need('local minimality and multiplicative premises', 5 < 12 and c4 % 11 == 1
             and old['local_cases']['11'] == {'v_Delta':5,'minimality_required_upper_bound':12,
                                              'c4_mod_11':1,'type':'I_5','conductor_exponent':1})
        j = Fraction(c4**3,delta)
        need('nonintegral reduced j', j.denominator == 11**5 and str(j) == old['j'])
        pairs = [{'x':x,'y':y,'lhs':(y*y+a1*x*y+a3*y)%2,
                  'rhs':(x**3+a2*x*x+a4*x+a6)%2} for x in range(2) for y in range(2)]
        for pair in pairs:
            pair['on_curve'] = pair['lhs'] == pair['rhs']
        # Every nonzero F2 projective triple is its own scalar-equivalence class.
        projective = [[x,y,z] for x in range(2) for y in range(2) for z in range(2)
                      if (x,y,z) != (0,0,0) and
                      (y*y*z+a1*x*y*z+a3*y*z*z-x**3-a2*x*x*z-a4*x*z*z-a6*z**3)%2 == 0]
        infinity = [p for p in projective if p[2] == 0]
        need('complete affine and projective count', pairs == old['F2']['all_affine_pairs']
             and all(p['on_curve'] for p in pairs) and len(projective) == 5 and infinity == [[0,1,0]])
        need('smoothness and trace binding', delta % 2 == 1 and a1 % 2 == 0 and a3 % 2 == 1
             and old['F2']['infinity_FZ'] == 1 and old['F2']['point_count'] == 5
             and old['F2']['trace'] == -2 and [(t['prime'],t['trace']) for t in ar['traces']] == [(2,-2)])
        need('arithmetic original provenance', old['adapter_input_sha256'] == sha(ROOT/'arithmetic-input.json')
             and old['program_sha256'] == sha(ROOT/'certify_arithmetic.py')
             and len(old['checks']) == 12 and all(old['checks'].values()) and not old['failures'])
        evidence['arithmetic'] = {'invariants':invariants,'j':str(j),'all_F2_projective_points':projective,
                                  'valuation_actual':5,'minimality_required':'<12','trace':-2}

        script = Path('scripts/dual-kernel/verify_certificate.py')
        spec = importlib.util.spec_from_file_location('l039_dual_audit',script)
        verifier = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(verifier)
        report = verifier.verify(ROOT/'dual-certificate.json',ROOT/'structural-certificate.json',
                                 ROOT/'arithmetic-input.json',OUT/'verification.json')
        previous = read(ROOT/'dual-verification.json')
        need('full accepted replay and linear equality', not report['failures'] and
             report['checks'] == previous['checks'] and report['summary'] == previous['summary'])
        need('current outer program and certificate binding', report['checker_sha256'] == sha(script)
             and report['certificate_sha256'] == sha(ROOT/'dual-certificate.json'))
        need('one complete structural replay', len(report['structural_replays']) == 1)
        manifest = report['structural_replays'][0]
        sub = read(Path(manifest['report']))
        need('entire subordinate equality and current binding', sub == read(ROOT/'dual-verification-structure/general-verification.json')
             and sub['sha256'] == sha(ROOT/'structural-certificate.json')
             and manifest['report_sha256'] == sha(Path(manifest['report']))
             and manifest['program_sha256'] == sha(Path('scripts/general-relative/verify_certificate.py')))
        need('all domain thresholds and path segments', not sub['failures'] and
             all(sub['actual'][k] == v for k,v in sub['required'].items())
             and sub['actual']['paths'] == 60 and sub['actual']['segments'] == 218)
        cert, structure = read(ROOT/'dual-certificate.json'), read(ROOT/'structural-certificate.json')
        matrices = [structure['operators'][key]['B']['entries'] for key in ('J','T2')]
        B = [[Fraction(mat[j][i])-value*(i==j) for j in range(3)]
             for mat,value in zip(matrices,(1,-2)) for i in range(3)]
        need('complete displayed dual matrix', B == [[-2,1,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,-1,5]])
        v = list(map(Fraction,cert['line']['v']))
        determinant = B[0][0]*B[5][1]-B[0][1]*B[5][0]
        need('independent both rank bounds', v == [Fraction(5,2),5,1] and any(v)
             and all(sum(x*y for x,y in zip(row,v)) == 0 for row in B) and determinant == 2)
        need('exact dimension threshold', report['summary']['d'] == 3 and report['summary']['rank'] == 2
             and report['summary']['nullity'] == 1 and report['summary']['arithmetic_status'] == 'SUPPLIED_CONDITIONAL')
        evidence['summary'] = report['summary']
        evidence['structural'] = {key:sub[key] for key in ('summary','actual','required')}
        evidence['structural_checks'] = len(sub['checks'])

        # Exercise the previously vulnerable failure-persistence obligation in
        # this adapter, seeding a stale success at its actual subordinate path.
        corrupt = copy.deepcopy(structure)
        seg = next(seg for path in corrupt['basepaths'] for side in ('start_chain','end_chain')
                   for seg in path[side]['segments'])
        seg['lookup']['gamma'][0] += 1
        bad_structure, bad_dual = OUT/'corrupt-structure.json', OUT/'corrupt-dual.json'
        write(bad_structure,corrupt)
        changed = copy.deepcopy(cert)
        changed['bindings']['structural_sha256'] = sha(bad_structure)
        write(bad_dual,changed)
        stale_path = OUT/'failure-verification-structure/general-verification.json'
        write(stale_path,sub)
        rejected = verifier.verify(bad_dual,bad_structure,ROOT/'arithmetic-input.json',OUT/'failure-verification.json')
        persisted = read(stale_path)
        need('actual Gamma0 corruption rejected', bool(rejected['failures']) and
             'h times inverse lift in Gamma0' in rejected['failures'][0])
        need('fresh subordinate failure replaces stale success', bool(persisted['failures'])
             and persisted['sha256'] == sha(bad_structure) and persisted['summary'] is None
             and persisted != sub and rejected['summary'] is None)
        evidence['expected_rejection'] = {'outer':rejected['failures'],'subordinate':persisted['failures'],
                                          'corrupt_sha256':sha(bad_structure),'stale_success_replaced':True}
        need('all original inputs and programs unchanged', before == {str(p):sha(p) for p in files})
    except Exception as error:
        failures.append(type(error).__name__+': '+str(error))
    finally:
        result = {'checks':checks,'failures':failures,'evidence':evidence,'input_program_hashes':before,
                  'qualification':'Fixed L039 evidence audit only; supplied generic arithmetic remains conditional.'}
        write(OUT/'manifest.json',result)
        print('audit actual/required checks:',sum(checks.values()),'/',len(checks),'; failures:',failures,
              '; rank required=2, nullity required=1; full evidence:',OUT/'manifest.json')
    raise SystemExit(bool(failures))


if __name__ == '__main__':
    main()
