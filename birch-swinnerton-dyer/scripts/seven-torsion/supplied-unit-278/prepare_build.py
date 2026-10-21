from pathlib import Path
R=Path('scripts/seven-torsion/supplied-unit-278');O=R.parent/'coordinate-norm-273'
s=(O/'build_norms.py').read_text()
s=s[:s.index('    matrices={}')] + '''    out['location']='source unit construction'
    P=Sparse(Rat(),tuple(map(Q,point['f'])))
    pc=P.reduce(tuple(map(Q,[46224,-3024,0,1])))
    az=(P.zero,P.zero);ao=(P.one,P.zero)
    def am(u,v):return (P.add(P.mul(u[0],v[0]),P.mul(pc,P.mul(u[1],v[1]))),P.add(P.mul(u[0],v[1]),P.mul(u[1],v[0])))
    def apow(u,n):
        r=ao
        for _ in range(n):r=am(r,u)
        return r
    def pdiv(a,b):
        a=list(P.trim(a));b=P.trim(b);need(bool(b),'nonzero_Euclidean_divisor')
        quot=[Q(0)]*max(0,len(a)-len(b)+1)
        while len(a)>=len(b):
            j=len(a)-len(b);z=a[-1]/b[-1];quot[j]=z
            for i,c in enumerate(b):a[i+j]-=z*c
            a=list(P.trim(a))
        return P.trim(quot),P.trim(a)
    def pmulfree(a,b):
        v=[Q(0)]*max(0,len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):v[i+j]+=x*y
        return P.trim(v)
    def pinv(a):
        r0,r1=P.mod,a;s0,s1=(),(Q(1),)
        while r1:
            q,r=pdiv(r0,r1);r0,r1=r1,r;s0,s1=s1,P.add(s0,P.neg(pmulfree(q,s1)))
        need(len(r0)==1 and r0[0]!=0,'unit_Euclidean_gcd')
        result=P.reduce(tuple(x/r0[0] for x in s0))
        need(P.mul(a,result)==P.one,'whole_source_denominator_inverse')
        return result
    def ainverse(u):
        den=P.add(P.mul(u[0],u[0]),P.neg(P.mul(pc,P.mul(u[1],u[1]))));di=pinv(den)
        return (P.mul(u[0],di),P.neg(P.mul(u[1],di)))
    def af(u):return tuple(u[e][i] if i<len(u[e]) else Q(0) for e in range(2) for i in range(24))
    def topower(v):return tuple(sum((Q(point['inverse'][i][j])*v[j] for j in range(48) if v[j] and Q(point['inverse'][i][j])),Q(0)) for i in range(48))
    def frompower(v):return tuple(sum((Q(point['matrix'][i][j])*v[j] for j in range(48) if v[j] and Q(point['matrix'][i][j])),Q(0)) for i in range(48))
    a=((Q(0),Q(1)),P.one);b=(P.one,P.one);ai=ainverse(a);bi=ainverse(b)
    aprime=am(a,apow(b,7));api=am(ai,apow(bi,7))
    elements={'a':a,'b':b,'a_prime':aprime,'scalar2':((Q(2),),P.zero)}
    inverses={'a':ai,'b':bi,'a_prime':api,'scalar2':((Q(1,2),),P.zero)}
    inputs={}
    for label,u in elements.items():
        need(am(u,inverses[label])==ao,'source_unit_'+label)
        v,iv=af(u),af(inverses[label]);tv,tiv=topower(v),topower(iv)
        need(frompower(tv)==v and frompower(tiv)==iv,'input_power_roundtrips_'+label)
        inputs[label]={'standard':v,'inverse_standard':iv,'power':tv,'inverse_power':tiv}
    need(am(a,apow(b,7))==aprime,'source_representative_change')
    save('supplied-inputs.json',{'elements':inputs,'source_basis':'X^i, X^i Y; 0<=i<24','power_basis':'Y^j; 0<=j<48'})
    print('All supplied source units and representative identity saved.',flush=True)
    def pairmul(u,v):return (E.add(E.mul(u[0],v[0]),E.mul((cp,),E.mul(u[1],v[1]))),E.add(E.mul(u[0],v[1]),E.mul(u[1],v[0])))
    def ipow(u,n):
        r=(E.one,E.zero)
        for _ in range(n):r=pairmul(r,u)
        return r
    def pull(u):
        def evalp(v):
            r=E.zero
            for c in reversed(v):r=E.add(E.mul(r,X),ec([c]))
            return r
        return (evalp(u[0]),E.mul(evalp(u[1]),yf))
    pulls={};ipulls={}
    for label,u in elements.items():
        pulls[label]=pull(u);ipulls[label]=pull(inverses[label])
        need(pairmul(pulls[label],ipulls[label])==(E.one,E.zero),'full_incidence_unit_'+label)
    need(pairmul(pulls['a'],ipow(pulls['b'],7))==pulls['a_prime'],'incidence_representative_change')
    save('input-pullbacks.json',{label:{'element':iflat(*pulls[label]),'inverse':iflat(*ipulls[label])} for label in elements})
    out['location']='full matrices'
    matrices={}
    for name,(a,b) in list(pulls.items())+[('zero',(E.zero,E.zero))]:
        columns=[];aa=a;bb=b
        for col in range(7):
            columns.append([B.trim((aa[row] if row<len(aa) else L.zero,bb[row] if row<len(bb) else L.zero)) for row in range(7)])
            if col<6:aa=E.mul(aa,X);bb=E.mul(bb,X)
        matrices[name]=[[columns[col][row] for col in range(7)] for row in range(7)]
    full={name:[[bflat(v) for v in row] for row in mat] for name,mat in matrices.items()}
    save('supplied-matrices.json',{'matrices':full,'rational_slots':11760,'F':F,'y_V_factor':yf})
    print('Full five matrices saved: 11760 rational slots.',flush=True)
    norms={};unfinished={}
    def determinant(mat,label):
        records={};unfinished[label]=records
        @lru_cache(None)
        def det(cols):
            if not cols:return B.one
            row=7-len(cols);s=B.zero
            for j,col in enumerate(cols):
                if mat[row][col]!=B.zero:
                    term=B.mul(mat[row][col],det(cols[:j]+cols[j+1:]))
                    s=B.add(s,term if j%2==0 else B.neg(term))
            records[','.join(map(str,cols))]=bflat(s)
            return s
        value=det(tuple(range(7)))
        save('laplace-'+label+'.json',{'norm':bflat(value),'ordered_remaining_column_minors':records,'row_rule':'7 - len(columns)','empty_minor':bflat(B.one)})
        del unfinished[label]
        return value
    for name in ('zero','scalar2','a','b','a_prime'):
        out['location']='Laplace '+name;print(out['location'],flush=True)
        norms[name]=determinant(matrices[name],name)
        save('norm-'+name+'.json',{'norm':bflat(norms[name])})
    need(norms['zero']==B.zero and norms['scalar2']==B.trim((L.trim((d([128]),)),)),'scalar_zero_norm_controls')
    def bpow(u,n):
        r=B.one
        for _ in range(n):r=B.mul(r,u)
        return r
    need(B.mul(norms['a'],bpow(norms['b'],7))==norms['a_prime'],'full_norm_representative_change')
    beta=B.trim((L.trim((d([2]),)),));betai=B.trim((L.trim((d([Q(1,2)]),)),))
    need(B.mul(beta,betai)==B.one and bpow(beta,7)==norms['scalar2'],'exact_scalar_root_witness')
    save('supplied-norms.json',{'norms':{k:bflat(v) for k,v in norms.items()},'representative_change':{'lhs':bflat(B.mul(norms['a'],bpow(norms['b'],7))),'rhs':bflat(norms['a_prime'])},'positive_scalar_control':{'beta':bflat(beta),'beta_inv':bflat(betai),'beta7':bflat(bpow(beta,7))},'mixed_root_claim':False})
    out.update(passed=True,rational_matrix_slots=11760,norm_slots=240,element_count=5)
except Exception as exc:
    out['failures'].append(type(exc).__name__+': '+str(exc))
    if 'unfinished' in globals() and unfinished:save('unfinished-minors.json',{'location':out.get('location'),'partial_minors':unfinished,'complete_norm_claim':False})
finally:finish('construction',out,t)
sys.exit(0 if out['passed'] else 1)
'''
(R/'build_norms.py').write_text(s)
