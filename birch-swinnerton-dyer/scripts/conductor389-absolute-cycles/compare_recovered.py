#!/usr/bin/env python3
"""Post-recovery comparison only; never called by recovery or its verifier."""
import json
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
paths=[HERE/'certificate.json',HERE/'verification.json',ROOT/'scripts/calibrated-symbols/certificate.json']
new,verification,old=[json.loads(p.read_text()) for p in paths]
checks={
    'new replay binds current certificate': verification['certificate_sha256']==sha256(paths[0].read_bytes()).hexdigest(),
    'complete production replay passed': verification['failures']==[] and verification['summary']['generator_values_actual']==390,
    'same model and whole generator count': new['source_scope']['model']==old['instance']['model']==[0,1,1,-2,0]
        and old['instance']['level']==389 and old['instance']['generator_count']==390,
    'same structural bytes':new['inputs']['scripts/relative-t2/certificate.json']==old['input_sha256']['scripts/relative-t2/certificate.json'],
    'independently recovered scalar agrees':F(new['normalization']['beta_over_total_period'])==F(old['scale']),
    'all 390 exact values agree':len(new['normalization']['generator_values'])==len(old['integral_generator_values'])==390
        and list(map(F,new['normalization']['generator_values']))==list(map(F,old['integral_generator_values'])),
    'least denominator agrees':new['normalization']['common_denominator']==old['denominator']['lcm']}
failures=[label for label,ok in checks.items() if not ok]
report={'inputs':{str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest() for p in paths},
        'checks':checks,'values_compared':390,'failures':failures,
        'qualification':'L032 is a post-recovery comparison only; no twist ratio used by producer or verifier.'}
out=HERE/'comparison.json';out.write_text(json.dumps(report,indent=2)+'\n')
print('Post-recovery comparison:',sum(checks.values()),'/',len(checks),'checks; all',report['values_compared'],'/ required 390 values; failures:',failures,'; path:',out)
if failures:raise SystemExit(1)
