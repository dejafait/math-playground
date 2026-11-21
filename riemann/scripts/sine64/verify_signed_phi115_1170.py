"""Exact full-record assembly check; does not independently audit primitives."""
from fractions import Fraction as F
from pathlib import Path
import json


def main():
    path=Path(__file__).with_name('signed-phi115-1170.json')
    cert=json.loads(path.read_text())
    scale=int(cert['scale'])
    failures=[]

    def check(name, ok):
        if not ok:
            failures.append(name)

    def bounds(item):
        check('scale',int(item['scale'])==scale)
        a,b=int(item['lo']),int(item['hi'])
        check('ordered interval',a<=b)
        return F(a,scale),F(b,scale)

    def mul(a,b):
        values=[x*y for x in a for y in b]
        return min(values),max(values)

    # Check complete retained set without relying on its saved count.
    expected={2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,
              37,41,43,47,49,53,59,61,64,67,71,73,79,81,83,89,97}
    check('all35 terms',set(t['n'] for t in cert['prime_powers'])==expected
          and len(cert['prime_powers'])==35)
    prime=[bounds(t['contribution']) for t in cert['prime_powers']]
    check('complete prime sum',bounds(cert['prime_expectation'])==
          (sum(a for a,b in prime),sum(b for a,b in prime)))
    b=bounds(cert['parameters']['b'])
    pi=bounds(cert['parameters']['pi'])
    lo=hi=F(0)
    cells=cert['cells']
    check('cell count',len(cells)==51100)
    for k,cell in enumerate(cells):
        check(f'index {k}',cell['k']==k)
        check(f'midpoint {k}',F(cell['midpoint'])==1+F(2*k+1,200))
        G=bounds(cell['G'])
        log=bounds(cell['log_symbol'])
        value=mul(mul(mul(mul((F(1,100),)*2,log),b),G),G)
        value=mul(value,(1/pi[1],1/pi[0]))
        a,z=bounds(cell['contribution'])
        check(f'outward contribution {k}',a<=value[0] and value[1]<=z)
        lo+=a
        hi+=z
    check('complete midpoint sum',bounds(cert['complete_midpoint_sum'])==(lo,hi))
    rlo,rhi=bounds(cert['full_R'])
    check('final positive rational enclosure',F(61177,100000)<rlo<rhi<F(62173,100000))
    check('required width',rhi-rlo<=F(1,50))
    check('original checks',all(cert['checks'].values()) and cert['failures']==[])
    result=dict(scope='Full finite record assembly; analytic and primitive audit remains open.',
                source=str(path.name),cells_checked=len(cells),terms_checked=len(prime),
                complete_midpoint_sum=cert['complete_midpoint_sum'],
                full_R=cert['full_R'],actual_width=str(rhi-rlo),required_width='1/50',
                failures=failures,passed=not failures)
    out=path.with_name('signed-phi115-assembly-1170.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('All51100 cells and all35 terms inspected; passed:',not failures)
    print('Actual width:',rhi-rlo,'required <=1/50; failures:',failures)
    print('Full assembly certificate:',out.relative_to(Path.cwd()))
    raise SystemExit(bool(failures))


if __name__=='__main__':
    main()
