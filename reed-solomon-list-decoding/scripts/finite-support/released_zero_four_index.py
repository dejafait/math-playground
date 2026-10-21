#!/usr/bin/env python3
"""Complete fixed-distance four-index test, exact rational certificates."""
import hashlib
import itertools as it
import json
import re
from fractions import Fraction as Q
from math import comb
from pathlib import Path
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'released-zero-four-index-results.json'

def enc(x):
    x = Q(x)
    return [x.numerator, x.denominator]

def det(m):
    ans = Q(0)
    for order in it.permutations(range(len(m))):
        term = Q((-1)**sum(order[i]>order[j] for i in range(len(m)) for j in range(i+1,len(m))))
        for i,j in enumerate(order): term *= m[i][j]
        ans += term
    return ans

def regions(weights, pairs, triple, capacity):
    a,b,c = weights
    ab,ac,bc = pairs
    h = triple
    return [capacity-a-b-c+ab+ac+bc-h,
            a-ab-ac+h,b-ab-bc+h,ab-h,c-ac-bc+h,ac-h,bc-h,h]

def congruence(m):
    n = len(m)
    v = [[Q(i==j) for i in range(n)] for j in range(n)]
    def bil(a,b): return sum(a[i]*m[i][j]*b[j] for i in range(n) for j in range(n))
    pivots=[]
    for k in range(n):
        a = bil(v[k],v[k]); pivots.append(enc(a))
        if a < 0: return False, pivots, v[k], a
        if a == 0:
            j = next((j for j in range(k+1,n) if bil(v[k],v[j])),None)
            if j is not None:
                b,c = bil(v[k],v[j]),bil(v[j],v[j])
                t = -b/(abs(c)+1)
                witness = [x+t*y for x,y in zip(v[k],v[j])]
                return False,pivots,witness,bil(witness,witness)
        else:
            for j in range(k+1,n):
                t = bil(v[k],v[j])/a
                v[j] = [x-t*y for x,y in zip(v[j],v[k])]
    return True,pivots,v,[[enc(bil(x,y)) for y in v] for x in v]

def main():
    paths=[NB/'lemmas/L056-released-zero-five-shell-nonexclusion.md',ROOT/'delsarte-lp-results.json',
           ROOT/'selected-triple-sdp-results.json',ROOT/'released-zero-five-shell-results.json']
    manuscript=paths[0].read_text()
    lp,selected,released=[json.loads(p.read_text()) for p in paths[1:]]
    p=[Q(1)]+[Q(0)]*4+[Q(a['numerator'],a['denominator'])/(2*comb(68,i)*comb(956,i))
                              for i,a in enumerate(lp['exact']['primal'],5)]
    z={(int(r),int(q)):Q(v) for r,q,v in re.findall(r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$',manuscript,re.M)}
    d={key:v/(comb(5,key[0])*comb(63,key[0])*comb(5,key[1])*comb(951,key[1])) for key,v in z.items()}
    rho=(Q(comb(1024,64),comb(68,64))+1)/(2*comb(1024,68))
    checks=0; errors=[]
    def check(name,condition,where=None):
        nonlocal checks
        checks+=1
        if not condition: errors.append({'check':name,'where':where})
    check('complete_fixed_pairs',len(p)==69 and list(map(enc,p))==selected['p']==released['parameters']['p'])
    check('complete_coefficients',list(z)==[(r,q) for r in range(6) for q in range(6) if r+q>=5]
          and list(map(enc,z.values()))==released['exact']['primal'])
    check('positive_rho',rho>0)
    check('p5_p6',p[5]==Q(1,68881143660) and p[6]==Q(133,9357995374380))
    records=[]; negative=[]; seen=set(); minor_count=zero_minors=singular=0
    candidate_count=0
    for a,b,c in it.product(range(6),range(1,6),range(1,6)):
        A,B,C=5-a,6-b,6-c
        for h in range(max(0,a+b-5,a+c-5,b+c-6),min(a,b,c)+1):
            for H in range(max(0,A+B-5,A+C-5,B+C-6),min(A,B,C)+1):
                candidate_count+=1
                inside=regions((5,5,6),(a,b,c),h,68)
                outside=regions((5,5,6),(A,B,C),H,956)
                check('nonnegative_partitions',min(inside+outside)>=0,[a,b,c,h,H])
                sizes=[0]*16
                for mask in range(8):
                    # Removed bit means absent from E,F,G inside D.
                    sizes[1|((7^mask)<<1)]=inside[mask]
                    sizes[mask<<1]=outside[mask]
                key=tuple(sizes)
                check('unique_atoms',key not in seen,[a,b,c,h,H]);seen.add(key)
                atoms=[];cursor=0
                for size in sizes:
                    atoms.append(set(range(cursor,cursor+size)));cursor+=size
                supports=[frozenset().union(*(atoms[mask] for mask in range(16) if mask&(1<<j))) for j in range(4)]
                check('full_ground_and_weights',cursor==1024 and all(len(s)==68 for s in supports),[a,b,c,h,H])
                distances=[len(supports[i]-supports[j]) for i,j in it.combinations(range(4),2)]
                check('six_distances',distances==[5,5,6,5,5,5],[a,b,c,h,H])
                triple_records={}
                def moment(family):
                    ids=sorted(family)
                    if len(ids)==1:return Q(1)
                    if len(ids)==2:return p[len(supports[ids[0]]-supports[ids[1]])]
                    assert len(ids)==3
                    key=','.join(map(str,ids))
                    if key in triple_records:return Q(*triple_records[key]['moment_over_rho'])
                    eligible=[]
                    for anchor in ids:
                        others=[i for i in ids if i!=anchor]
                        S,T,U=[supports[i] for i in [anchor]+others]
                        if len(S-T)!=5 or len(S-U)!=5:continue
                        r=5-len(S-(T|U));q=5-len((T&U)-S)
                        direct=[len(S-(T|U)),len((S&U)-T),len((S&T)-U),len(S&T&U),
                                len((T&U)-S),len(T-(S|U)),len(U-(S|T)),1024-len(S|T|U)]
                        check('full_triple_dictionary',direct==[5-r,r,r,63-r,5-q,q,q,951-q],[a,b,c,h,H,ids,anchor])
                        eligible.append({'anchor':anchor,'order':[anchor]+others,'relation':[r,q],'regions':direct})
                    check('represented_triple',bool(eligible),[a,b,c,h,H,ids])
                    values=[p[5]*d[tuple(item['relation'])] for item in eligible]
                    check('unordered_consistency',len(set(values))==1,[a,b,c,h,H,ids])
                    triple_records[key]={'eligible_anchors':eligible,'moment_over_rho':enc(values[0])}
                    return values[0]
                indices=[frozenset([0])]+[frozenset([0,i]) for i in range(1,4)]
                matrix=[[moment(I|J) for J in indices] for I in indices]
                minors=[]
                for size in range(1,5):
                    for subset in it.combinations(range(4),size):
                        value=det([[matrix[i][j] for j in subset] for i in subset])
                        minors.append({'indices':list(subset),'value':enc(value)})
                        minor_count+=1;zero_minors+=value==0
                passed,pivots,v,result=congruence(matrix)
                check('minors_congruence_agreement',passed==all(Q(*item['value'])>=0 for item in minors),[a,b,c,h,H])
                record={'parameters':[a,b,c,h,H],'atoms_by_D_E_F_G_bitmask':sizes,
                        'distances':distances,'triples':triple_records,
                        'matrix_over_rho':[[enc(x) for x in row] for row in matrix],
                        'principal_minors_over_rho':minors,'PSD':passed,'pivots':pivots}
                if passed:
                    record['congruence_columns']=[[enc(x) for x in col] for col in v]
                    record['congruence_diagonal_matrix']=result
                    singular+=any(Q(*x)==0 for x in pivots)
                else:
                    record['negative_vector']=list(map(enc,v));record['negative_value']=enc(result)
                    check('strict_negative_witness',result<0,[a,b,c,h,H])
                    negative.append(len(records))
                records.append(record)
    check('complete_count',len(records)==candidate_count==len(seen) and minor_count==15*candidate_count)
    result={'source_sha256':{str(path.relative_to(NB)):hashlib.sha256(path.read_bytes()).hexdigest() for path in paths},
            'normalization':{'rho':enc(rho),'p5':enc(p[5]),'p6':enc(p[6])},
            'scope':'Exactly (DE,DF,DG,EF,EG,FG)=(5,5,6,5,5,5); full 16 atoms.',
            'counts':{'feasible_atoms':len(records),'candidate_count':candidate_count,'principal_minors':minor_count,
                      'zero_minors':zero_minors,'singular_PSD':singular,'nonPSD':len(negative)},
            'checks':checks,'errors':errors,'negative_record_indices':negative,'records':records,
            'verdict':'INVALID' if errors else 'FAIL' if negative else 'PASS'}
    OUT.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print('Verdict:',result['verdict'],'; checks:',checks,'; errors:',len(errors))
    print('Coverage actual/required:',len(records),'/',candidate_count,'full atom vectors;',minor_count,'/',15*candidate_count,'minors')
    print('NonPSD:',len(negative),'; zero minors:',zero_minors,'; singular PSD:',singular)
    if negative:print('First negative record index:',negative[0],'; parameters:',records[negative[0]]['parameters'])
    print('Full certificate:',OUT)
    assert not errors,errors
if __name__=='__main__':main()
