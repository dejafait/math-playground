import hashlib, json, sys
from pathlib import Path
sys.set_int_max_str_digits(10000)
root = Path(__file__).resolve().parents[2]
src = root / 'scripts/seven-torsion/nonmonic-order-283/discriminant.json'
raw = src.read_bytes()
d = json.loads(raw)
D = abs(d['order_discriminant'])
primes = (2, 3, 7, 389)

def is_prime_trial(n):
    if n < 2: return False
    q = 2
    while q*q <= n:
        if n % q == 0: return False
        q += 1
    return True

rows=[]
for p in primes:
    assert is_prime_trial(p)
    rem=D; e=0; divisions=[]
    while rem % p == 0:
        before=rem; rem//=p; e+=1
        divisions.append({'before':before,'quotient':rem,'remainder':0})
    rows.append({'prime':p,'prime_trial':True,'exponent':e,'divisions':divisions,'residual':rem,'terminal_remainder':rem%p})
    D=rem
cert={'source':'scripts/seven-torsion/nonmonic-order-283/discriminant.json','source_sha256':hashlib.sha256(raw).hexdigest(),'input_sign':-1 if d['order_discriminant']<0 else 1,'input_abs':abs(d['order_discriminant']),'primes':rows,'cofactor':D,'reconstruction':2**rows[0]['exponent']*3**rows[1]['exponent']*7**rows[2]['exponent']*389**rows[3]['exponent']*D,'outcome':'SUPPORTED' if D==1 else 'REFUTED'}
cert['replay']={'sign_matches':cert['input_sign']==(-1 if d['order_discriminant']<0 else 1),'input_matches':cert['input_abs']==abs(d['order_discriminant']),'all_primes_trial_certified':all(r['prime_trial'] for r in rows),'all_divisions_exact':all(x['before']==r['prime']*x['quotient']+x['remainder'] and x['remainder']==0 for r in rows for x in r['divisions']),'terminal_nondivisibility':all(r['terminal_remainder']!=0 for r in rows),'reconstruction_matches':cert['reconstruction']==cert['input_abs']}
# Independent replay from the preserved original, checking each emitted division and terminal remainder.
R=abs(json.loads(src.read_bytes())['order_discriminant'])
for row in rows:
    p=row['prime']; assert is_prime_trial(p)
    for x in row['divisions']:
        assert R==x['before'] and divmod(R,p)==(x['quotient'],0)
        R=x['quotient']
    assert R==row['residual'] and R%p==row['terminal_remainder']!=0
assert R==cert['cofactor'] and cert['reconstruction']==abs(d['order_discriminant'])
cert['replay']['independent_replay_passed']=True
out=Path(__file__).parent/'certificate.json'
out.write_text(json.dumps(cert,separators=(',',':'))+'\n')
print(json.dumps({'outcome':cert['outcome'],'sign':cert['input_sign'],'digit_count':len(str(cert['input_abs'])),'prime_exponents':{r['prime']:r['exponent'] for r in rows},'cofactor_digits':len(str(cert['cofactor'])),'cofactor':str(cert['cofactor']) if cert['cofactor']<10**80 else 'retained in certificate','replay':cert['replay'],'certificate':str(out.relative_to(root))}))
