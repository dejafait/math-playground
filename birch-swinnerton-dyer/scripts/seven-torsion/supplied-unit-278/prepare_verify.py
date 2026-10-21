from pathlib import Path
R=Path('scripts/seven-torsion/supplied-unit-278');O=R.parent/'coordinate-norm-273'
s=(O/'verify_norms.py').read_text()
s=s[:s.index('    matrices={}')].replace("read(R/'coordinate-matrices.json')","read(R/'supplied-matrices.json')").replace("read(R/'coordinate-norms.json')","read(R/'supplied-norms.json')")
s+='''    out['location']='independent full source units'
    P=Horner(Rational(),tuple(map(Q,point['f'])))
    pc=P.reduce(tuple(map(Q,[46224,-3024,0,1])))
    az=(P.zero,P.zero);ao=(P.one,P.zero)
    def am(u,v):return (P.add(P.mul(u[0],v[0]),P.mul(pc,P.mul(u[1],v[1]))),P.add(P.mul(u[0],v[1]),P.mul(u[1],v[0])))
    def apow(u,n):
        r=ao
        while n:
            if n%2:r=am(r,u)
            n//=2
            if n:u=am(u,u)
        return r
    def af(u):return u[0]+u[1]
    def au(v):
        if len(v)!=48:raise ValueError('full_source_48_shape')
        w=tuple(map(Q,v));return (w[:24],w[24:])
    def convert(v,mat):return tuple(sum((Q(mat[i][j])*v[j] for j in range(48) if v[j] and Q(mat[i][j])),Q(0)) for i in range(48))
    supplied=read(R/'supplied-inputs.json')['elements'];labels=('a','b','a_prime','scalar2')
    need(set(supplied)==set(labels),'exact_supplied_unit_labels')
    a=(P.vector((Q(0),Q(1))),P.one);b=(P.one,P.one)
    wanted={'a':a,'b':b,'a_prime':am(a,apow(b,7)),'scalar2':(P.vector((Q(2),)),P.zero)}
    def input_test(rows):
        if set(rows)!=set(labels):raise ValueError('supplied_input_labels')
        for label in labels:
            row=rows[label]
            for key in ('standard','inverse_standard','power','inverse_power'):
                if len(row[key])!=48:raise ValueError('full_source_48_shape')
            u=au(row['standard']);ui=au(row['inverse_standard'])
            if u==az:raise ValueError('zero_is_not_a_supplied_unit')
            if am(u,ui)!=ao:raise ValueError('full_source_unit_inverse_product')
            if u!=wanted[label]:raise ValueError('exact_mixed_input_value')
            for key,dest in (('power','standard'),('inverse_power','inverse_standard')):
                v=tuple(map(Q,row[key]));w=tuple(map(Q,row[dest]))
                if convert(v,point['matrix'])!=w or convert(w,point['inverse'])!=v:raise ValueError('all_input_basis_transports')
    input_test(supplied);need(True,'all_full_source_inputs_inverses_and_transports')
    rejections=[]
    def reject(case,data,fn,expected):
        save('mutant-'+case+'.json',data)
        try:fn(data)
        except ValueError as exc:
            need(str(exc)==expected,'intended_'+case)
            rejections.append({'case':case,'rejected':True,'condition':str(exc),'full_malformed_replay':False,'scope':'named full-data condition only'})
        else:raise ValueError('accepted mutant '+case)
    bad=copy.deepcopy(supplied);bad['a']['inverse_standard'][0]=str(Q(bad['a']['inverse_standard'][0])+1)
    reject('inverse-one-coefficient',bad,input_test,'full_source_unit_inverse_product')
    bad=copy.deepcopy(supplied);bad['a']['standard']=['0']*48
    reject('zero-supplied-unit',bad,input_test,'zero_is_not_a_supplied_unit')
    bad=copy.deepcopy(supplied);bad['a']['power']=bad['a']['power'][:-1]
    reject('missing-source-coordinate',bad,input_test,'full_source_48_shape')
    def im(u,v):return (E.add(E.mul(u[0],v[0]),E.mul(constant(cp),E.mul(u[1],v[1]))),E.add(E.mul(u[0],v[1]),E.mul(u[1],v[0])))
    def ipow(u,n):
        r=(E.one,E.zero)
        while n:
            if n%2:r=im(r,u)
            n//=2
            if n:u=im(u,u)
        return r
    def pull(u):
        def evalp(v):
            r=E.zero
            for z in reversed(v):
                r=E.shift(r);r=E.add(r,constant(L.vector((d([z]),))))
            return r
        return (evalp(u[0]),E.mul(evalp(u[1]),yf))
    pulls={};invpulls={};oldpull=read(R/'input-pullbacks.json')
    for label in labels:
        row=supplied[label];pulls[label]=pull(au(row['standard']));invpulls[label]=pull(au(row['inverse_standard']))
        need(im(pulls[label],invpulls[label])==(E.one,E.zero),'all_incidence_inverse_coefficients_'+label)
        for key,v in (('element',pulls[label]),('inverse',invpulls[label])):
            need(iff(*v)==tuple(map(Q,oldpull[label][key])),'all_336_pullback_coefficients_'+label+'_'+key)
    need(am(au(supplied['a']['standard']),apow(au(supplied['b']['standard']),7))==au(supplied['a_prime']['standard']),'full_source_representative_change')
    need(im(pulls['a'],ipow(pulls['b'],7))==pulls['a_prime'],'full_incidence_representative_change')
    save('independent-inputs.json',{'elements':{label:{'element':iff(*pulls[label]),'inverse':iff(*invpulls[label]),'inverse_product':iff(*im(pulls[label],invpulls[label]))} for label in labels},'source_products':{label:af(am(au(supplied[label]['standard']),au(supplied[label]['inverse_standard']))) for label in labels}})
    matrices={}
    for name,(a,b) in list(pulls.items())+[('zero',(E.zero,E.zero))]:
        cols=[]
        for j in range(7):
            cols.append([(a[i],b[i]) for i in range(7)])
            if j<6:a,b=E.shift(a),E.shift(b)
        matrices[name]=[[cols[j][i] for j in range(7)] for i in range(7)]
    flat={name:[[bf(v) for v in row] for row in mat] for name,mat in matrices.items()}
    def matrix_test(data):
        if set(data)!=set(matrices) or any(len(data[k])!=7 or any(len(row)!=7 or any(len(v)!=48 for v in row) for row in data[k]) for k in data):raise ValueError('full_matrix_48_shape')
        if {k:[[tuple(map(Q,v)) for v in row] for row in mat] for k,mat in data.items()}!=flat:raise ValueError('all_matrix_coefficient_comparison')
    matrix_test(produced['matrices']);need(produced['rational_slots']==11760,'all_11760_matrix_slots')
    save('independent-matrices.json',{'matrices':flat,'rational_slots':11760})
    bad=copy.deepcopy(produced['matrices']);bad['a'][0][0][24]=str(Q(bad['a'][0][0][24])+1)
    reject('odd-V-matrix-coefficient',bad,matrix_test,'all_matrix_coefficient_comparison')
    print('Independent full source units, pullbacks and 11760 matrix slots pass.',flush=True)
'''
old=(O/'verify_norms.py').read_text();s+=old[old.index('    def mm(a,b):'):old.index('    norms={}')] # independent recurrence unchanged
s+='''    norms={}
    for name in ('zero','scalar2','a','b','a_prime'):
        out['location']='Faddeev '+name
        norms[name]=faddeev(matrices[name],name)
        lap=read(R/('laplace-'+name+'.json'))
        need(tuple(map(Q,lap['norm']))==bf(norms[name])==tuple(map(Q,savednorm['norms'][name])),'all_48_determinant_coefficients_'+name)
    need(norms['zero']==bz and norms['scalar2']==bs(bo,128),'independent_zero_scalar_norms')
    def bp(u,n):
        r=bo
        while n:
            if n%2:r=bm(r,u)
            n//=2
            if n:u=bm(u,u)
        return r
    representative=bm(norms['a'],bp(norms['b'],7))
    need(representative==norms['a_prime'],'all_norm_representative_change_coefficients')
    for key in ('lhs','rhs'):need(tuple(map(Q,savednorm['representative_change'][key]))==bf(representative),'saved_full_representative_'+key)
    def bu(v):
        if len(v)!=48:raise ValueError('full_B_shape')
        w=tuple(map(Q,v));return tuple(tuple(tuple(w[e*24+i*8+j] for j in range(8)) for i in range(3)) for e in range(2))
    root=savednorm['positive_scalar_control'];beta=bu(root['beta']);betai=bu(root['beta_inv'])
    need(beta==bs(bo,2) and betai==bs(bo,Q(1,2)) and bm(beta,betai)==bo and bp(beta,7)==norms['scalar2'] and tuple(map(Q,root['beta7']))==bf(bp(beta,7)),'full_positive_scalar_root_and_inverse')
    def norm_test(data):
        if set(data)!=set(norms) or any(len(data[k])!=48 or tuple(map(Q,data[k]))!=bf(norms[k]) for k in data):raise ValueError('all_norm_coefficient_comparison')
    norm_test(savednorm['norms']);bad=copy.deepcopy(savednorm['norms']);bad['a'][0]=str(Q(bad['a'][0])+1)
    reject('norm-one-coefficient',bad,norm_test,'all_norm_coefficient_comparison')
    save('rejections.json',rejections)
    save('verification-summary.json',{'norms':{k:bf(v) for k,v in norms.items()},'all_matrix_coefficients_equal':True,'all_norm_coefficients_equal':True,'representative_change':{'lhs':bf(representative),'rhs':bf(norms['a_prime'])},'positive_scalar_control':root,'rejections':rejections,'mixed_root_claim':False})
    out.update(passed=True,rational_matrix_slots=11760,norm_slots=240,element_count=5,rejection_count=len(rejections))
except Exception as exc:out['failures'].append(type(exc).__name__+': '+str(exc))
finally:finish('verification',out,t)
sys.exit(0 if out['passed'] else 1)
'''
(R/'verify_norms.py').write_text(s)
