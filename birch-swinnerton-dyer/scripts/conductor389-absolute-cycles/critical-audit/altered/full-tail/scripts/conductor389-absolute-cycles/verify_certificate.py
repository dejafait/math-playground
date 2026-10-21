#!/usr/bin/env python3
"""Full fixed-instance replay, without importing the producer.

External homology, optimality, Manin and period-lattice premises are in L044.
Model coefficients are checked independently with a residue histogram.
"""
import json
import subprocess
import sys
from fractions import Fraction as F
from hashlib import sha256
from math import factorial, gcd, isqrt, lcm
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
INPUT_NAMES = ['scripts/relative-t2/certificate.json',
               'scripts/dual-kernel/conductor389-certificate.json',
               'scripts/dual-kernel/conductor389-arithmetic.json']
SCHEDULE = [(256,64),(1024,96),(4096,128)]


def replay(data, checks):
    def need(label, condition):
        if not condition:
            raise ValueError(label)
        checks.append(label)

    def mul(a,b):
        need('nonempty matrix shapes', len(a)>0 and len(b)>0 and
             all(len(row)==len(b) for row in a) and all(len(row)==len(b[0]) for row in b))
        return [[sum(row[k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for row in a]

    def dot(x,y):
        need('exact vector shapes',len(x)==len(y))
        return sum(a*b for a,b in zip(x,y))

    need('schema',data['schema']=='conductor389-full-absolute-v1')
    need('complete input bindings', data['inputs']=={name:sha256((ROOT/name).read_bytes()).hexdigest() for name in INPUT_NAMES})
    structural,dual,arithmetic=[json.loads((ROOT/name).read_text()) for name in INPUT_NAMES]
    need('exact source scope',data['source_scope']=={
        'model':[0,1,1,-2,0],'N':389,'optimal_label':'389a1','absolute_Manin_constant':1,'components':2,
        'published_optimality_qualification':'L031 optimality only; complete isogeny class and two-period comparison'})
    need('arithmetic instance',arithmetic['model']==[0,1,1,-2,0] and arithmetic['conductor']==389)
    upstream=HERE/'upstream-replay'
    upstream.mkdir(exist_ok=True)
    result=subprocess.run([sys.executable,str(ROOT/'scripts/dual-kernel/verify_certificate.py'),
                           str(ROOT/INPUT_NAMES[1]),'--structural',str(ROOT/INPUT_NAMES[0]),
                           '--arithmetic',str(ROOT/INPUT_NAMES[2]),'--out',str(upstream/'dual-verification.json')],
                          capture_output=True,text=True)
    (upstream/'replay.txt').write_text(result.stdout+result.stderr)
    report=json.loads((upstream/'dual-verification.json').read_text())
    need('fresh full structural and dual replay',result.returncode==0 and report['failures']==[])
    need('fresh byte binding',report['certificate_sha256']==data['inputs'][INPUT_NAMES[1]])
    p=structural['presentation']
    coords,lifts,sat=[p[k] for k in ('integral_generator_coordinates','integral_quotient_basis_lifts','saturated_relation_basis')]
    need('whole integral presentation shapes',(len(coords),len(lifts),len(sat))==(390,65,325)
         and all(len(x)==65 for x in coords) and all(len(x)==390 for x in lifts+sat)
         and len(structural['relations'])==780)
    endpoints=[]
    def cusp(num,den):
        if den==0:
            return [1,0]
        v=F(num,den)
        return [v.numerator,v.denominator]
    for a,b,c,d in structural['SL2_lifts']:
        endpoints.append([cusp(b,d),cusp(a,c)])
    boundary=data['boundary']
    need('complete endpoint witnesses',len(boundary['endpoint_witnesses'])==390)
    raw=[]
    for i,pair in enumerate(endpoints):
        need('both cusp witnesses',len(boundary['endpoint_witnesses'][i])==2)
        flags=[]
        for j,(num,den) in enumerate(pair):
            w=boundary['endpoint_witnesses'][i][j]
            flag=int(den%389==0)
            tp,tq=(1,0) if flag else (0,1)
            u=w['unit']
            need('reduced cusp and class',den>=0 and gcd(num,den)==1 and w['cusp']==[num,den] and w['class']==flag)
            need('both cusp equivalence congruences',type(u) is int and 1<=u<389
                 and (tq-u*den)%389==0 and (u*tp-num)%gcd(den,389)==0)
            flags.append(flag)
        raw.append(flags[1]-flags[0])
    need('all oriented raw boundaries',raw==[-1]+[0]*388+[1] and boundary['raw_reduced']==raw)
    need('complete cusp target',boundary['cusp_order']==['zero','infinity'] and boundary['raw_full']==[[-v for v in raw],raw])
    source=[dot(raw,row) for row in structural['relations']]
    saturated=[dot(raw,row) for row in sat]
    need('all 780 source and 325 saturated boundaries',source==boundary['source_images']==[0]*780
         and saturated==boundary['saturated_images']==[0]*325)
    B=[dot(raw,row) for row in lifts]
    need('integral quotient boundary',B==boundary['quotient_reduced']==[0]*64+[1]
         and boundary['quotient_full']==[[-v for v in B],B])
    need('boundary descent on every generator',[dot(B,row) for row in coords]==raw)
    k=data['kernel']; T,Ti=k['unimodular_transform'],k['inverse']
    need('whole integer transform',len(T)==len(Ti)==65 and all(len(x)==65 for x in T+Ti)
         and all(type(v) is int for row in T+Ti for v in row))
    identity=[[int(i==j) for j in range(65)] for i in range(65)]
    need('both unimodular inverse products',mul(T,Ti)==mul(Ti,T)==identity)
    need('full boundary normal form',mul([B],T)==k['boundary_after_transform']==[[1]+[0]*64])
    basis=[[row[j] for row in T] for j in range(1,65)]
    need('entire integer kernel',basis==k['basis_columns']==[[int(i==j) for i in range(65)] for j in range(64)])
    raw_basis=[[dot(col,row) for row in zip(*lifts)] for col in basis]
    need('all absolute raw lifts',raw_basis==k['raw_basis_columns']
         and [mul([row],coords)[0] for row in raw_basis]==basis)
    phi=list(map(F,dual['line']['v']))
    need('full nonzero relative functional',len(phi)==65 and any(phi))
    image=[dot(phi,col) for col in basis]
    need('every absolute functional value',list(map(F,k['functional_values']))==image)
    den=lcm(*(x.denominator for x in image)); integers=[int(x*den) for x in image]
    need('full denominator clearing',den==k['common_denominator'] and integers==k['integer_values'])
    gg=gcd(*integers)
    need('complete gcd Bezout primitivity',k['gcd']==gg>0 and len(k['bezout'])==64
         and all(type(v) is int for v in k['bezout']) and dot(k['bezout'],integers)==gg)
    g=F(gg,den)
    need('positive image and all primitive values',g==F(k['positive_image_generator'])==F(1,2)
         and list(map(F,k['primitive_values']))==[x/g for x in image]
         and all((x/g).denominator==1 for x in image))
    values0=[dot(phi,row) for row in coords]
    expected=[]
    for t in range(1,389):
        if not values0[t]:
            continue
        cc=pow(389,-1,t) if t>1 else 1
        if t>1 and cc>t//2:
            cc-=t
        a=(1-389*cc)//t
        M=[a,-1,389*cc,t]
        if cc<0:M=[-v for v in M]
        expected.append((abs(cc),t,M))
    expected.sort()
    need('bounded independent candidate selection',len(data['candidates'])==min(3,len(expected))
         and data['candidate_policy']=='first three sorted (abs(c),generator index) from all nonzero reversed fixed paths; least absolute inverse c, positive lower-left matrix')
    for cycle,(_,t,M) in zip(data['candidates'],expected[:3]):
        rawcycle=[0]*390;rawcycle[t]=-1
        xy=[-x for x in coords[t]]
        a,b,C,d=M
        need('complete oriented raw cycle',cycle['generator_index']==t and cycle['raw']==rawcycle
             and cycle['path']==list(reversed(endpoints[t]))==[[0,1],[-1,t]])
        need('absolute cycle and nonzero functional',cycle['coordinates']==xy and dot(B,xy)==0
             and F(cycle['phi'])==dot(phi,xy)==-values0[t]!=0)
        need('Gamma0 determinant cusp and orientation',cycle['matrix']==M and a*d-b*C==1
             and C>0 and C%389==0 and F(b,d)==F(-1,t))
        ar,ai=map(F,cycle['alpha']); nr,ni,dr,di=a*ar+b,a*ai,C*ar+d,C*ai
        mapped=[(nr*dr+ni*di)/(dr*dr+di*di),(ni*dr-nr*di)/(dr*dr+di*di)]
        need('both exact interior endpoints',[ar,ai]==[F(-d,C),F(1,C)]
             and mapped==list(map(F,cycle['M_alpha']))==[F(a,C),F(1,C)] and ai>0)
    need('bounded attempts',1<=len(data['attempts'])<=9 and data['selected_attempt']==len(data['attempts'])-1)
    for ix,attempt in enumerate(data['attempts']):
        ci,si=divmod(ix,3)
        need('exact ordered candidate schedule',attempt['candidate_index']==ci and attempt['schedule_index']==si and ci<len(data['candidates']))
        a,b,C,d=data['candidates'][ci]['matrix']; f=attempt['fourier']
        nmax,bits=SCHEDULE[si];D=1<<bits
        need('permitted truncation precision and degrees',(f['T'],f['bits'],f['atan_count'],f['exp_count'],f['cos_degree'])
             ==(nmax,bits,bits//2+16,64,48) and f['scale']==D and F(f['height'])==F(1,C))
        def exact(x):
            need('ordered dyadic endpoints',len(x)==2 and all(type(v) is int for v in x) and x[0]<=x[1])
            return [F(v,D) for v in x]
        def outer(lo,hi):
            need('ordered rational endpoints',lo<=hi)
            return [(lo*D).__floor__(),-((-hi*D).__floor__())]
        def product(x,y):
            ends=[u*v for u in exact(x) for v in exact(y)]
            return outer(min(ends),max(ends))
        def times(x,v):
            return outer(*sorted(t*v for t in exact(x)))
        ab=[]
        for inv in (5,239):
            ac=f['atan_count'];s=sum((F((-1)**j,(2*j+1)*inv**(2*j+1)) for j in range(ac)),F(0))
            ab.append(sorted([s,s+F((-1)**ac,(2*ac+1)*inv**(2*ac+1))]))
        need('all atan alternating evidence',f['atan_brackets']==[[str(v) for v in row] for row in ab])
        t2=2*F(1,5)/(1-F(1,25));t4=2*t2/(1-t2*t2)
        need('Machin exact tangent identity',(t4-F(1,239))/(1+t4*F(1,239))==1)
        pi_exact=[16*ab[0][0]-4*ab[1][1],16*ab[0][1]-4*ab[1][0]]
        need('full pi enclosure',f['pi_exact']==list(map(str,pi_exact)) and f['pi']==outer(*pi_exact))
        h=times(f['pi'],F(2,C));ex=[]
        need('exact positive exponential argument',h==f['h'])
        for x in exact(h):
            need('alternating exponential domain',0<x<1)
            ec=f['exp_count'];s=sum(((-x)**j/factorial(j) for j in range(ec+1)),F(0))
            ex.append(sorted([s,s+(-x)**(ec+1)/factorial(ec+1)]))
        rex=[ex[1][0],ex[0][1]];r=f['r']
        need('complete exponential evidence',f['exp_exact']==list(map(str,rex)) and r==outer(*rex) and 0<r[0]<=r[1]<D)
        residues=sorted({min(v%C,C-v%C) for n in range(1,nmax+1) for v in (a*n,-d*n)})
        need('all and only required cosine residues',[row['j'] for row in f['cosines']]==residues)
        cosines={}
        for row in f['cosines']:
            j=row['j']
            if j==0:
                need('zero angle cosine',row=={'j':0,'interval':[D,D]})
            else:
                theta=sorted(2*F(j,C)*v for v in exact(f['pi']));mid=sum(theta)/2;rad=(theta[1]-theta[0])/2
                degree=f['cos_degree'];poly=sum((F((-1)**m)*mid**(2*m)/factorial(2*m) for m in range(degree+1)),F(0))
                err=abs(mid)**(2*degree+2)/factorial(2*degree+2)+rad
                need('full cosine Taylor Lipschitz arithmetic',row['theta']==list(map(str,theta)) and F(row['midpoint'])==mid
                     and F(row['radius'])==rad and F(row['polynomial'])==poly and F(row['error'])==err
                     and row['interval']==outer(poly-err,poly+err))
            cosines[j]=row['interval']
        primes=[ell for ell in range(2,nmax+1) if all(ell%j for j in range(2,isqrt(ell)+1))]
        need('complete prime set',[row['p'] for row in f['point_counts']]==primes)
        aps={}
        for row in f['point_counts']:
            ell=row['p']; histogram=[0]*ell
            # Counts every y once; lookup is equivalent to exhausting all pairs.
            for y in range(ell):histogram[(y*y+y)%ell]+=1
            xs=[histogram[(x*x*x+x*x-2*x)%ell] for x in range(ell)]
            if ell==2:
                pairs=[[x,y] for x in range(ell) for y in range(ell) if (y*y+y-x*x*x-x*x+2*x)%ell==0]
                need('all F2 pairs',row['pairs']==pairs)
            else:
                need('all discriminant characters independently counted',row['characters']==[v-1 for v in xs])
            aps[ell]=ell-sum(xs)
            need('complete affine trace',row['affine']==sum(xs) and row['a_p']==aps[ell])
            if ell==389:need('multiplicative Euler factor',aps[ell]==1)
        coeffs=[0,1];factors=[]
        for n in range(2,nmax+1):
            rem,val,fs=n,1,[]
            for ell in primes:
                if rem%ell:continue
                k=0
                while rem%ell==0:rem//=ell;k+=1
                powers=[1,aps[ell]]
                for _ in range(2,k+1):powers.append(aps[ell]*powers[-1]-(0 if ell==389 else ell)*powers[-2])
                val*=powers[k];fs.append([ell,k,powers])
            need('all coefficient factorizations',rem==1);coeffs.append(val);factors.append([n,fs])
        need('every model-derived Fourier coefficient',coeffs==f['coefficients'] and factors==f['factorizations']
             and all(abs(coeffs[n])<=n for n in range(1,nmax+1)))
        need('all Fourier terms',len(f['terms'])==nmax)
        power,partial=[D,D],[0,0]
        def cosres(v):v%=C;return cosines[min(v,C-v)]
        for n,row in enumerate(f['terms'],1):
            power=product(power,r);x,y=cosres(a*n),cosres(-d*n);diff=[x[0]-y[1],x[1]-y[0]]
            term=times(product(power,diff),F(coeffs[n],n));partial=[partial[0]+term[0],partial[1]+term[1]]
            need('complete Fourier term '+str(n),row=={'n':n,'power':power,'difference':diff,'term':term,'partial':partial})
        nxt=product(power,r);tail_exact=2*F(nxt[1],D)/(1-F(r[1],D));tail=-((-tail_exact*D).__floor__())
        need('full two-series geometric remainder',f['next_power']==nxt and f['tail_upper']==tail and F(tail,D)>=tail_exact>0)
        period=[partial[0]-tail,partial[1]+tail]
        need('complete signed enclosure',period==f['period_interval'])
        nonzero=period[0]>0 or period[1]<0
        need('stop at first strictly nonzero enclosure',nonzero==(ix==len(data['attempts'])-1))
    # Last iteration is the independently successful attempt.
    cycle=data['candidates'][data['attempts'][-1]['candidate_index']]
    psign=1 if period[0]>0 else -1
    sign=psign*(1 if F(cycle['phi'])>0 else -1)
    scale=F(sign)/(2*g);values=[scale*x for x in values0];common=lcm(*(x.denominator for x in values))
    denprimes=[ell for ell in range(2,common+1) if all(ell%j for j in range(2,isqrt(ell)+1)) and common%ell==0]
    n=data['normalization']
    need('derived scale from full image and sign',n['beta_sign']==sign and F(n['beta_over_total_period'])==scale)
    need('all 390 normalized generators',len(n['generator_values'])==390 and list(map(F,n['generator_values']))==values)
    need('entire normalized relations',[dot(values,row) for row in structural['relations']]==[0]*780
         and [dot(values,row) for row in sat]==[0]*325)
    need('complete least denominator and all primes',n['common_denominator']==common and n['denominator_primes']==denprimes)
    need('all-level p integrality',all(ell<5 for ell in denprimes) and n['C_for_p_ge_5_good_ordinary']==0)
    need('no producer failures',data['failures']==[])
    return {'kernel_rank_actual':64,'kernel_rank_required':64,'image':str(g),'primitive_image':'Z',
            'period_interval':period,'scale':D,'required_orientation':'strict exclusion of zero',
            'attempts_actual':len(data['attempts']),'attempts_maximum':9,'terms_actual':nmax,'terms_required':SCHEDULE[si][0],
            'cosine_residues':len(residues),'prime_counts':len(primes),'normalizing_scalar':str(scale),
            'generator_values_actual':len(values),'generator_values_required':390,
            'all_generator_denominator':common,'denominator_primes':denprimes,'tail_upper':tail,
            'upstream_report':'upstream-replay/dual-verification.json'}


if __name__=='__main__':
    path,out=HERE/'certificate.json',HERE/'verification.json'
    checks,failures,summary=[],[],None
    try:summary=replay(json.loads(path.read_text()),checks)
    except Exception as error:failures.append(type(error).__name__+': '+str(error))
    report={'certificate_sha256':sha256(path.read_bytes()).hexdigest(),'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'summary':summary,'checks_passed':len(checks),'checks':checks,'failures':failures}
    out.write_text(json.dumps(report,indent=2)+'\n')
    print('Complete absolute-cycle replay:',summary,'; checks:',len(checks),'; failures:',failures,'; report:',out)
    if failures:raise SystemExit(1)
