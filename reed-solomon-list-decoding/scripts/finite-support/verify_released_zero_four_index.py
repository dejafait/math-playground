#!/usr/bin/env python3
"""Independent Möbius incidence coverage and Gaussian minor reconstruction.

Imports no constructor/notebook routines. Verifies complete saved congruences.
"""
import hashlib
import itertools as it
import json
import re
from fractions import Fraction as Q
from math import comb
from pathlib import Path
ROOT=Path(__file__).resolve().parent
NB=ROOT.parent.parent
OUT=ROOT/'released-zero-four-index-verification.json'

def enc(x):
    x=Q(x);return [x.numerator,x.denominator]

def det(matrix):
    a=[row[:] for row in matrix];answer=Q(1)
    for k in range(len(a)):
        j=next((j for j in range(k,len(a)) if a[j][k]),None)
        if j is None:return Q(0)
        if j!=k:a[j],a[k]=a[k],a[j];answer=-answer
        answer*=a[k][k]
        for j in range(k+1,len(a)):
            t=a[j][k]/a[k][k]
            for h in range(k+1,len(a)):a[j][h]-=t*a[k][h]
    return answer

def main():
    source=ROOT/'released-zero-four-index-results.json'
    manuscript=NB/'lemmas/L056-released-zero-five-shell-nonexclusion.md'
    lp_path=ROOT/'delsarte-lp-results.json'
    saved=json.loads(source.read_text());lp=json.loads(lp_path.read_text())
    z={(int(r),int(q)):Q(x) for r,q,x in re.findall(r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$',manuscript.read_text(),re.M)}
    p=[Q(1)]+[Q(0)]*4+[Q(x['numerator'],x['denominator'])/(2*comb(68,i)*comb(956,i))
                           for i,x in enumerate(lp['exact']['primal'],5)]
    rho=(Q(comb(1024,64),comb(68,64))+1)/(2*comb(1024,68))
    failures=[];checks=0
    def check(name,condition,where=None):
        nonlocal checks
        checks+=1
        if not condition:failures.append({'check':name,'where':where})
    check('valid_constructor',saved['verdict']=='PASS' and saved['errors']==[])
    check('input_hashes',all(hashlib.sha256((NB/path).read_bytes()).hexdigest()==value for path,value in saved['source_sha256'].items()))
    check('normalization',saved['normalization']=={'rho':enc(rho),'p5':enc(p[5]),'p6':enc(p[6])} and rho>0)
    # Intersections of three supports and all four are the only free data.
    # Pair intersections force these inclusive lower/upper bounds.
    intersections={0:1024,1:68,2:68,4:68,8:68,3:63,5:63,9:62,6:63,10:63,12:63}
    atoms_list=[]
    for a,b,c,d,e in it.product(range(58,64),range(57,63),range(57,63),range(58,64),range(52,63)):
        f={**intersections,7:a,11:b,13:c,14:d,15:e}
        atoms=[sum((-1)**((t^s).bit_count())*f[t] for t in range(16) if t&s==s) for s in range(16)]
        if min(atoms)>=0:atoms_list.append(tuple(atoms))
    lookup={tuple(record['atoms_by_D_E_F_G_bitmask']):record for record in saved['records']}
    check('unique_independent_atoms',len(atoms_list)==len(set(atoms_list))==150)
    check('exhaustive_equal_coverage',len(lookup)==len(saved['records'])==len(atoms_list) and set(lookup)==set(atoms_list))
    verified=[];minor_count=0;zero_minors=0;nonPSD=0
    for atoms in atoms_list:
        record=lookup[atoms];cursor=0;points=[set() for _ in range(4)]
        for mask,size in enumerate(atoms):
            for j in range(4):
                if mask>>j&1:points[j].update(range(cursor,cursor+size))
            cursor+=size
        supports=list(map(frozenset,points))
        tag=record['parameters']
        check('partition_weight',cursor==1024 and all(len(s)==68 for s in supports),tag)
        distances=[len(supports[i]^supports[j])//2 for i,j in it.combinations(range(4),2)]
        check('fixed_distances',distances==record['distances']==[5,5,6,5,5,5],tag)
        # Independently recover constructor's removed/added parameters.
        D,E,F,G=supports
        removed=[D-S for S in (E,F,G)];added=[S-D for S in (E,F,G)]
        parameters=[len(removed[i]&removed[j]) for i,j in it.combinations(range(3),2)]
        parameters += [len(removed[0]&removed[1]&removed[2]),len(added[0]&added[1]&added[2])]
        check('parameter_reconstruction',parameters==tag,tag)
        triple_values={}
        for ids in [(0,1,2),(0,1,3),(0,2,3)]:
            common=len(supports[ids[0]]&supports[ids[1]]&supports[ids[2]])
            values=[];anchor_records=[]
            for anchor in ids:
                other=[i for i in ids if i!=anchor]
                A,B,C=[supports[i] for i in [anchor]+other]
                if len(A^B)!=10 or len(A^C)!=10:continue
                r=63-common;q=len(B^C)//2-r
                regions=[len(A-(B|C)),len((A&C)-B),len((A&B)-C),common,
                         len((B&C)-A),len(B-(A|C)),len(C-(A|B)),1024-len(A|B|C)]
                check('independent_full_triple_regions',regions==[5-r,r,r,63-r,5-q,q,q,951-q],tag)
                value=p[5]*z[r,q]/(comb(5,r)*comb(63,r)*comb(5,q)*comb(951,q))
                values.append(value)
                anchor_records.append({'anchor':anchor,'order':[anchor]+other,'relation':[r,q],'regions':regions})
            key=','.join(map(str,ids));stored=record['triples'][key]
            check('complete_eligible_anchors',anchor_records==stored['eligible_anchors'],[tag,ids])
            check('unordered_values',len(set(values))==1 and enc(values[0])==stored['moment_over_rho'],[tag,ids])
            triple_values[frozenset(ids)]=values[0]
        families=[frozenset([0]),frozenset([0,1]),frozenset([0,2]),frozenset([0,3])]
        def moment(ids):
            if len(ids)==1:return Q(1)
            if len(ids)==2:
                i,j=sorted(ids);return p[len(supports[i]^supports[j])//2]
            return triple_values[ids]
        matrix=[[moment(I|J) for J in families] for I in families]
        check('all_family_union_entries',record['matrix_over_rho']==[[enc(x) for x in row] for row in matrix],tag)
        expected_subsets=[list(s) for n in range(1,5) for s in it.combinations(range(4),n)]
        check('complete_minor_subsets',[x['indices'] for x in record['principal_minors_over_rho']]==expected_subsets,tag)
        verified_minors=[]
        for subset,stored in zip(expected_subsets,record['principal_minors_over_rho']):
            value=det([[matrix[i][j] for j in subset] for i in subset])
            check('minor_rational_identity',enc(value)==stored['value'],[tag,subset])
            check('minor_positive',value>0,[tag,subset]);minor_count+=1;zero_minors+=value==0
            verified_minors.append({'indices':subset,'value':enc(value)})
        columns=[[Q(*x) for x in col] for col in record['congruence_columns']]
        congruence=[[sum(v[i]*matrix[i][j]*w[j] for i in range(4) for j in range(4)) for w in columns] for v in columns]
        check('congruence_invertible',det(columns)!=0,tag)
        check('complete_congruence_identity',record['congruence_diagonal_matrix']==[[enc(x) for x in row] for row in congruence],tag)
        check('diagonal_and_pivots',all(congruence[i][j]==0 for i in range(4) for j in range(4) if i!=j)
              and record['pivots']==[enc(congruence[i][i]) for i in range(4)],tag)
        passed=all(congruence[i][i]>0 for i in range(4));nonPSD+=not passed
        check('PSD_verdict',record['PSD']==passed,tag)
        verified.append({'atoms':list(atoms),'matrix_over_rho':[[enc(x) for x in row] for row in matrix],
                         'minors':verified_minors,'congruence_pivots':[enc(congruence[i][i]) for i in range(4)]})
    check('aggregate_counts',saved['counts']=={'feasible_atoms':150,'candidate_count':150,'principal_minors':2250,
          'zero_minors':0,'singular_PSD':0,'nonPSD':0} and minor_count==2250 and zero_minors==nonPSD==0)
    result={'source_sha256':{str(path.relative_to(NB)):hashlib.sha256(path.read_bytes()).hexdigest() for path in [source,manuscript,lp_path]},
            'checks':checks,'failures':failures,'coverage':{'independent_atoms':len(atoms_list),'minors':minor_count},
            'records':verified,'verdict':'VERIFIED_PASS' if not failures else 'INVALID'}
    OUT.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print('Verdict:',result['verdict'],'; checks:',checks,'; failures:',len(failures))
    print('Independent actual/required: atoms',len(atoms_list),'/150; minors',minor_count,'/2250; nonPSD',nonPSD)
    print('Full certificate:',OUT)
    assert not failures,failures
if __name__=='__main__':main()
