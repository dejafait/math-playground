"""Lossless compact verifier input for all completed forced-V cases."""
import json
from pathlib import Path

root=Path(__file__).parent
data=json.loads((root/'forced-v-mixed-result.json').read_text())
assert data['complete']
h=data['scope']['H']
out=root/'forced-v-mixed-verifier-input.txt'
with out.open('w') as f:
    f.write(str(len(data['cases']))+'\n')
    for case in data['cases']:
        records=case['mixed_records']
        row=[*case['Y'],*case['Z'],case['d'],*case['W'],*case['p_q_r'],
             *case['V'],*case['S'],*case['SS'],*case['Bprime_minus_d'],*case['T0'],
             case['V_recovery']['mu'],*(x['mu'] for x in case['selected_recoveries']),len(records)]
        for rec in records:
            row.extend([sum(1<<h.index(x) for x in rec['K']),rec['mu']])
        f.write(' '.join(map(str,row))+'\n')
print(f'exported complete cases {len(data["cases"])}; path {out}')
