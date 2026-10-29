"""Run exact endpoint enumeration; save complete counts and independent checks."""
from pathlib import Path
from itertools import combinations
from hashlib import sha256
import json
import struct
import subprocess

BASE = Path(__file__).resolve().parent
REPORT = BASE / 'endpoint-pair-count.json'


def main():
    result = {'failures': [], 'checks': [], 'small_instances': []}

    def check(name, actual, required):
        result['checks'].append({'name': name, 'actual': actual, 'required': required})
        if actual != required:
            result['failures'].append(name)

    binary = BASE / 'endpoint-pair-count-bin'
    source = BASE / 'endpoint_pair_count.c'
    subprocess.run(['cc', '-O3', '-std=c11', '-Wall', '-Wextra', str(source), '-o', str(binary)], check=True)

    def run(q, H, reps, hist_path, tag):
        input_path = BASE / (tag + '-input.txt')
        output_path = BASE / (tag + '-counts.txt')
        input_path.write_text(f'{q} {len(H)} {len(reps)}\n' + ' '.join(map(str, H)) + '\n' + ' '.join(map(str, reps)) + '\n')
        subprocess.run([str(binary), str(input_path), str(hist_path), str(output_path)], check=True)
        return {int(b): {'same': int(s), 'different': int(d), 'total': int(s)+int(d)}
                for b, s, d in map(str.split, output_path.read_text().splitlines())}

    for q, n in [(17,8), (17,16), (41,8), (97,16)]:
        H = [a for a in range(1,q) if pow(a,n,q)==1]
        check(f'{q}_{n}_order', len(H), n)
        remaining = set(range(1,q)); reps=[]
        while remaining:
            u=min(remaining); reps.append(u)
            remaining.difference_update(u*a%q for a in H)
        pairs=list(combinations(H,2))
        points=[((a+b)%q,a*b%q) for a,b in pairs]
        rows=[]
        for u in [None,0]+reps:
            row=[0]*q
            for s,t in points: row[s if u is None else (t-u*s)%q]+=1
            rows.append(row)
        hist_path=BASE/f'endpoint-small-{q}-{n}.u32'
        hist_path.write_bytes(b''.join(struct.pack('<'+'I'*q,*row) for row in rows))
        computed=run(q,H,reps,hist_path,f'endpoint-small-{q}-{n}')
        brute={b:{'same':0,'different':0,'total':0} for b in H if b!=1}
        T=0
        for i,j,k in combinations(range(len(pairs)),3):
            edges=[pairs[i],pairs[j],pairs[k]]
            endpoints=set(sum((list(e) for e in edges),[]))
            if len(endpoints)!=6: continue
            (s,t),(v,w),(y,z)=[points[l] for l in (i,j,k)]
            if ((v-s)*(z-t)-(y-s)*(w-t))%q: continue
            T+=6
            if 1 in endpoints:
                A=next(e for e in edges if 1 in e)
                for b in endpoints-{1}:
                    brute[b]['same' if b in A else 'different']+=6
                    brute[b]['total']+=6
        check(f'{q}_{n}_all_counts', computed, brute)
        result['small_instances'].append({'q':q,'n':n,'ordered_count':T,'counts':computed,'brute_counts':brute})

    manifest=json.loads((BASE/'l122-full-count.json').read_text())
    hist_path=BASE/'l122-full-count-histograms.u32'
    digest=sha256(hist_path.read_bytes()).hexdigest()
    check('audited_histogram_digest',digest,'4f8161677371fe052b12ead70436b92c0ceb508883a5bd658a593086043aa681')
    H=manifest['H']; reps=[r['slope'] for r in manifest['rows'][2:]]
    check('H_all_roots',sorted(H),[a for a in range(1,65537) if pow(a,1024,65537)==1])
    check('coset_partition',sorted(u*a%65537 for u in reps for a in H),list(range(1,65537)))
    counts=run(65537,H,reps,hist_path,'endpoint-pair')
    check('all_nonidentity_ratios',sorted(counts),sorted(set(H)-{1}))
    T=2298250371072; singleton=6*T//1024
    check('singleton_integrality',6*T%1024,0)
    check('sum_same',sum(c['same'] for c in counts.values()),singleton)
    check('sum_different',sum(c['different'] for c in counts.values()),4*singleton)
    check('all_endpoint_pairs',512*sum(c['total'] for c in counts.values()),15*T)
    check('inverse_ratio_symmetry',all(c==counts[pow(b,-1,65537)] for b,c in counts.items()),True)
    maximum=max(c['total'] for c in counts.values())
    attainers=sorted(b for b,c in counts.items() if c['total']==maximum)
    upper=T-61*singleton+1830*maximum
    incidence_upper=T-(61*singleton+5)//6
    # Without pair intersections: elementary singleton-only upper and union-bound lower.
    result.update({'q':65537,'n':1024,'ordered_count':T,'counts':counts,
                   'maximum':maximum,'attainers':attainers,'antipodal':counts[65536],
                   'singleton':singleton,'deletion':{'core_size':61,'bonferroni_upper':upper,
                   'singleton_only_upper':T-singleton,'union_bound_lower':T-61*singleton,
                   'incidence_only_upper':incidence_upper,
                   'upper_improvement':incidence_upper-upper},
                   'histogram_sha256':digest,'c_sha256':sha256(source.read_bytes()).hexdigest(),
                   'python_sha256':sha256(Path(__file__).read_bytes()).hexdigest()})
    check('nontrivial_upper_improvement', upper < incidence_upper,True)
    result['complete']=not result['failures']
    REPORT.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['complete','maximum','attainers','singleton','deletion','failures']} | {'certificate':str(REPORT.relative_to(Path.cwd()))}))
    return 0 if result['complete'] else 1


if __name__=='__main__':
    raise SystemExit(main())
