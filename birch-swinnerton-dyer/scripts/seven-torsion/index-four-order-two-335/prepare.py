"""Source generation only, executed inside the sole watchdog before mathematics."""
from pathlib import Path
D=Path(__file__).resolve().parent; S=D.parent

def put(name,s):
    with (D/name).open('x') as f:f.write(s)
def replace(s,a,b):
    if s.count(a)!=1:raise ValueError('nonunique source adaptation '+a[:80])
    return s.replace(a,b)

# The repaired input verifier reconstructs the entire actual S lattice.
s=(S/'preserved-table-replay-331/verify.py').read_text()
s=replace(s,"'verification-report.json'","'input-report.json'")
s=replace(s,"'preservation-verifier.json'","'preservation-input.json'")
put('input_verify.py',s)

# A separate producer uses polynomial reduction and triangular conversion,
# rather than the independent input verifier's polynomial-zero identities.
s=(S/'index-two-order-two-325/produce.py').read_text()
a=s.index('def inventory():'); b=s.index('\ndef mm(',a)
s=s[:a]+'''def inventory():
    names=json.loads((OUT/'canonical-input-hashes.json').read_text())
    return {p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in names}
''' +s[b:]
a=s.index("    b=json.loads((OLD/'basis.json')"); b=s.index('    def remainder(poly):',a)
s=s[:a]+'''    b=json.loads((OLD/'basis.json').read_text())
    original=json.loads((ROOT/'scripts/seven-torsion/certificate.json').read_text())
    nb=json.loads((OUT/'basis.json').read_text())
    H=b['H'];bp=b['basis_to_power'];bases=b['basis']
    need(H==original['primitive_integer_factors'][0] and H[-1]==343 and len(H)==49
         and [F(x,343) for x in H]==list(map(F,original['h'])) and reduce(math.gcd,H)==1,'original_H')
    M=rational(nb['basis_in_b']); C=rational(nb['b_to_basis'])
    need(all(F(x).denominator==1 for row in C for x in row),'integral_S_inverse')
    C=[[int(x) for x in row] for row in C]
    Q=[[124*x for x in row] for row in M]
    need(all(F(x).denominator==1 for row in Q for x in row),'scaled_S_basis_integral')
    Q=[[int(x) for x in row] for row in Q]
    need(mm(M,C)==I and mm(C,M)==I,'S_basis_inverse_both')
    polys=transpose(mm(bp,Q)); identity=nb['identity']
    need(polys==nb['scaled_polynomials'] and nb['scale']==124 and nb['input_scale']==62
         and nb['original_scale']==31 and nb['index']==4,'actual_scale_124_S')
    nto=rational(nb['to_L067']); nfr=rational(nb['from_L067'])
    need(mm(nto,nfr)==I and mm(nfr,nto)==I,'S_two_coordinate_transports')
    need(identity==[C[i][0] for i in range(N)]
         and mm(M,transpose([identity]))==transpose([I[0]]),'actual_identity')
    save('input-basis.json',{'H':H,'M':strings(M),'inverse':C,'scaled_polynomials':polys,
        'to_L067':strings(nto),'from_L067':strings(nfr),'identity':identity,'scale':124})
''' +s[b:]
s=replace(s,"(PREV/('product-%02d.json'%i))","(OUT/('product-%02d.json'%i))")
s=replace(s,',3844)',',15376)')
s=replace(s,'Actual L084 R+ producer. One shared stage, scale 62.','Actual L086 S producer. One shared stage, scale 124.')
put('produce.py',s)

# Independent kernel/action verifier uses only already fully validated S inputs;
# its arithmetic imports none of the producer's helpers.
s=(S/'index-two-order-two-325/verify.py').read_text()
a=s.index('def inventory():');b=s.index('# Aliases',a)
s=s[:a]+'''def inventory():
    names=load(HERE/'canonical-input-hashes.json')
    return {p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in names}
''' +s[b:]
a=s.index('    original=load(SRC/');b=s.index("    REPORT['input_product_slots']",a)
s=s[:a]+'''    got=load(HERE/'basis.json');H=got['H'];V=got['scaled_polynomials'];polys=V
    table=[load(HERE/('product-%02d.json'%i)) for i in range(48)]
    for row in table:shape(row,48,48,True)
    identity=got['identity'];B=rat(got['basis_in_b']);BI=rat(got['b_to_basis'])
    coords=rat(got['to_L067']);coords_back=rat(got['from_L067'])
    Hnz=[(i,x) for i,x in enumerate(H) if x]
    validation=read('input-report.json')
    require(validation['status']=='PASS' and not validation['failures']
        and validation['product_slots']==110592 and validation['product_identities']==2304
        and validation['division_certificates']==2304 and validation['transport_entries']==18432
        and validation['inverse_products']==8 and validation['identity_actions']==96
        and validation['index']==4,'complete_prior_input_validation')
    ib=read('input-basis.json')
    require(ib['H']==H and rat(ib['M'])==B and rat(ib['inverse'])==BI
        and ib['scaled_polynomials']==V and rat(ib['to_L067'])==coords
        and rat(ib['from_L067'])==coords_back and ib['identity']==identity
        and ib['scale']==124,'every_new_input_basis_slot')
    REPORT.update(product_slots=110592,product_identities=2304,remainder_coefficients=218880)
''' +s[b:]
s=replace(s,"        for k in range(94,47,-1):\n            x=p[k]", "        dividend=p[:]; quotient=[0]*47\n        for k in range(94,47,-1):\n            x=p[k]")
s=replace(s,"            else:q=x/343\n            for j,h in Hnz", "            else:q=Fraction(x,343)\n            quotient[k-48]=q\n            for j,h in Hnz")
s=replace(s,"        require(not any(p),label+'_entire_original_H_remainder')", "        require(not any(p),label+'_entire_original_H_remainder')\n        return {'dividend':dividend,'quotient':[str(x) for x in quotient],'remainder':[str(x) for x in p]}")
s=replace(s,"        for j in range(48):\n            compare(polys[i],Wpolys[j],[62*x for x in expansion[j]],'action_'+str((i,j)))", "        divisions=[]\n        for j in range(48):\n            cert=compare(polys[i],Wpolys[j],[124*x for x in expansion[j]],'action_'+str((i,j)))\n            divisions.append({'j':j,**cert})")
s=replace(s,"        REPORT['action_slots']+=2304;actions.append(A)", "        save('action-division-%02d.json'%i,{'i':i,'products':divisions})\n        REPORT['action_slots']+=2304;actions.append(A)")
s=replace(s,'transport_entries=13824,inverse_products=6,','transport_entries=18432,inverse_products=8,action_division_certificates=2304,')
s=replace(s,"load(HERE/'input-hashes.json')", "load(HERE/'canonical-input-hashes.json')")
put('verify.py',s)
