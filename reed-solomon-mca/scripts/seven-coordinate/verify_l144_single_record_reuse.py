"""Independent derivative/row-elimination replay of the single binding.

Imports only previously inspected linear-algebra utilities, not the producer.
"""
import json
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from verify_l139_literal_reuse import rref, det

HERE=Path(__file__).resolve().parent
P=97


def run():
    assert __debug__
    path=HERE/'l144-single-record-reuse.json'
    report=json.loads(path.read_bytes())
    assert report['failures']==[] and report['original_inputs_unchanged']
    for name,value in report['input_sha256'].items():
        assert sha256((HERE/name).read_bytes()).hexdigest()==value, name
    assert report['code_sha256']==sha256((HERE/'l144_single_record_reuse.py').read_bytes()).hexdigest()
    s=[1,8,12,18,22,27,33]
    h=[x for x in range(1,P) if pow(x,16,P)==1]
    j=sorted(set(h)-set(s))
    pairs=list(combinations(range(7),2))
    universe=[[list(a),list(b)] for a in combinations(s,2) for b in combinations(j,2)]
    master=json.loads((HERE/'new-pair-filter.json').read_bytes())
    rows=[dict(I=universe[n][0],K=universe[n][1]) for n in master['first_indices']+[239,647]]
    assert rows==report['rows'] and report['indices']==[239,647]
    shard=json.loads((HERE/'new-pair-filter/third-239.json').read_bytes())
    old=json.loads((HERE/'l141-l142-literal-reuse.json').read_bytes())
    assert report['complete_original_record']==shard['cases'][182]
    assert report['complete_prior_overlay']==old['overlay'][1]
    assert report['historical_residual_occurrences']==master['residual_occurrences']
    assert report['historical_mismatches']==old['unmatched_indices']
    rebuilt=[]
    for row,saved in zip(rows,report['row_inputs']):
        i,k=row['I'],row['K']
        values={}
        for x in s+k:
            denominator=1
            for y in s+k:
                if x!=y:
                    denominator=denominator*(x-y)%P
            assert denominator
            values[x]=16*pow(x,15,P)*pow(denominator,-1,P)%P
            assert values[x]
        z=min(set(s)-set(i))
        q=[[((int(y==x)*pow(values[x],-1,P)-int(y==z)*pow(values[z],-1,P))
             *values[x]*values[z])%P for y in s] for x in s if x not in i and x!=z]
        block=[[ (a[x]*b[y]-a[y]*b[x])%P for x,y in pairs] for a,b in combinations(q,2)]
        assert saved['original_block']==dict(I=i,K=k,pivot=z,covectors=q,matrix=block)
        assert saved['g_values_on_S_union_K']=={str(x):v for x,v in values.items()}
        coefficients=[1]
        roots=[y for y in j if y not in k]
        for root in reversed(roots):
            coefficients=[-root*coefficients[0]%P]+[(coefficients[n-1]-root*coefficients[n])%P
                        for n in range(1,len(coefficients))]+[coefficients[-1]]
        assert saved['z']==z and saved['g_roots']==roots and saved['g_coefficients_ascending']==coefficients
        rebuilt.extend(block)
    assert rebuilt==report['original_matrix']
    columns,basis=rref(rebuilt)
    assert columns==report['rank_minor_columns'] and basis==report['kernel_basis']
    minor=[[rebuilt[r][c] for c in columns] for r in report['rank_minor_rows']]
    residue=det(minor)
    assert residue==report['rank_minor_residue']==73 and len(columns)==19
    residuals=[[sum(a*b for a,b in zip(v,r))%P for r in rebuilt] for v in basis]
    assert residuals==report['kernel_residuals']==[[0]*24]*2
    source=json.loads((HERE/'first-l143-mismatch-locus-gates.json').read_bytes())
    replay=json.loads((HERE/'first-l143-mismatch-locus-gates-replay.json').read_bytes())
    assert basis==source['kernel_basis']==report['source']['kernel_basis']
    assert source['complete_projective_parameter_locus']==[[1,0],[0,1]]
    assert source['infinity_is_decomposable']
    assert all(report['source']['imported_locus'][key]==source[key] for key in report['source']['imported_locus'])
    pivot_count=0
    for pi,binding in enumerate(report['point_row_bindings']):
        point=source['points_and_all_row_gates'][pi]
        gate=point['row_gates'][1]
        assert binding==report['source']['point_bindings'][pi]
        assert binding['unchanged_rejecting_gate']==gate
        assert binding['row_input']==report['row_inputs'][1]
        assert binding['source_point_index']==pi and binding['source_row_number']==2
        assert binding['plane_representative']=={key:point[key] for key in ('u','v','bivector','pivot_indices')}
        u,v=point['u'],point['v']
        assert [(u[a]*v[b]-u[b]*v[a])%P for a,b in pairs]==basis[pi]==point['bivector']
        inp=report['row_inputs'][1]
        q=inp['original_block']['covectors']
        qu,qv=[[sum(a*b for a,b in zip(c,w))%P for c in q] for w in (u,v)]
        assert qu==gate['Q_u'] and qv==gate['Q_v']
        assert [(qu[a]*qv[b]-qu[b]*qv[a])%P for a,b in combinations(range(4),2)]==gate['projection_minors']==[0]*6
        n=next(n for n in range(4) if qu[n] or qv[n])
        alpha,beta=-qv[n]%P,qu[n]
        hh=[(alpha*a+beta*b)%P for a,b in zip(u,v)]
        vals={int(x):v for x,v in inp['g_values_on_S_union_K'].items()}
        lam=hh[s.index(inp['z'])]*pow(vals[inp['z']],-1,P)%P
        error=[(hh[s.index(x)]-lam*vals[x])%P for x in inp['I']]+[-lam*vals[x]%P for x in inp['K']]
        assert gate['projection_rank']==1 and gate['direction_coefficients']==[alpha,beta]
        assert gate['intersection_vector']==hh and gate['lambda_value']==lam==0
        assert gate['error_weights']==error and gate['overlap_weights']==error[:2]
        assert error[2:]==[0,0] and gate['passes'] is False
        assert gate['failed_gates']==['lambda_zero']+['overlap_weight_zero_at_'+str(x) for x,e in zip(inp['I'],error) if not e]
        edict=dict(zip(inp['I']+inp['K'],error))
        moments=[(sum(hh[n]*pow(x,d,P) for n,x in enumerate(s))-sum(e*pow(x,d,P) for x,e in edict.items()))%P for d in range(1,9)]
        identity=[((hh[s.index(x)] if x in s else 0)-edict.get(x,0))%P for x in h]
        assert moments==gate['moment_residuals']==[0]*8
        assert identity==gate['h_minus_error_minus_lambda_g_on_H']==[0]*16
        assert gate['g_values_on_S_union_K']==inp['g_values_on_S_union_K']
        assert gate['prescribed_finite_gate']==dict(D_coefficient=alpha,C_coefficient=-beta%P)
        assert gate['original_first_coefficient']=='(D*alpha-C*beta)/(AD-BC)'
        assert gate['original_basis_convention']=='u_original=A*u+B*v; v_original=C*u+D*v; AD-BC!=0'
        expected_row=dict(point_index=pi,row_number=2,Q_u=qu,Q_v=qv,h=hh,error={str(x):e for x,e in edict.items()},moments=moments,finite_gate_coefficients_D_C=[alpha,-beta%P])
        expected_row['lambda']=lam
        assert binding['original_row_replay']==expected_row
        assert expected_row==next(r for r in replay['all_row_replay'] if r['point_index']==pi and r['row_number']==2)
        skew=[[0]*7 for _ in range(7)]
        for (a,b),value in zip(pairs,basis[pi]):
            skew[a][b],skew[b][a]=value,-value%P
        pivots=[]
        for (a,b),value in zip(pairs,basis[pi]):
            if not value:
                continue
            uu=[skew[x][b]*pow(value,-1,P)%P for x in range(7)]
            vv=skew[a]
            qa,qb=[[sum(x*y for x,y in zip(c,w))%P for c in q] for w in (uu,vv)]
            for n in range(4):
                if not (qa[n] or qb[n]):
                    continue
                aa,bb=-qb[n]%P,qa[n]
                hv=[(aa*x+bb*y)%P for x,y in zip(uu,vv)]
                ix=next(x for x,w in enumerate(hh) if w)
                scalar=hv[ix]*pow(hh[ix],-1,P)%P
                assert scalar and hv==[scalar*x%P for x in hh]
                pivots.append(dict(point=pi,exterior_pivot=[a,b],row=2,projection_component=n,direction=[aa,bb],scalar=scalar,h=hv,lambda_value=0,error_weights=[scalar*x%P for x in error]))
        assert pivots==binding['all_nonzero_pivot_replay']==[r for r in replay['all_pivot_replay'] if r['point']==pi and r['row']==2]
        pivot_count+=len(pivots)
    assert len(report['point_row_bindings'])==2 and report['literal_complete_ordered_kernel_equal']
    assert report['disposition']=='excluded'
    result=dict(certificate_sha256=sha256(path.read_bytes()).hexdigest(),verifier_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),summary=dict(actual_records=1,required_records=1,matrix_entries=504,null_residuals=48,rank=19,minor_residue=residue,complete_kernel_vectors=2,point_row_bindings=2,required_bindings=2,projection_pivot_bindings=pivot_count,original_moments=16,pointwise_entries=32),failures=[],qualification='Independent same-step derivative and row-elimination binding replay; shared Python/residue arithmetic. Not a separate critical audit.')
    out=HERE/'l144-single-record-reuse-replay.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(f'Replayed 1/1 record; 504 entries; 48 null residuals; minor {residue} != 0; bindings 2/2; pivots {pivot_count}; moments 16; failures 0; {out}')


if __name__=='__main__':
    run()
