"""Fresh step-194 remaining discriminator streams; preserve step-192 evidence."""
import run_suite as suite

def main():
    out=suite.OUT
    out.mkdir(exist_ok=True)
    path=out/'certificate-194.json'
    cert={'complete':False,'failures':[],'library':{},'cases':[],
          'all_size_ledger_status':'L062_INFORMAL_BOUND_INSTRUMENTED_AUDIT_PENDING',
          'target_complete':False,'critical_audit_pending':True}
    suite.save(path,cert)
    try:
        lib=suite.library(cert)
        suite.save(path,cert)
        cases=[('194-nonpower-selection',suite.request(N=3,n=0,k=1,r=[1,1,1],R=[[1,1,1]]),False),
               ('194-zero-row',suite.request(k=1,r=[0,0],G=[[[1,1],[0,0]]],
                                             R=[[1,1]],T=[[[0]]]),True),
               ('194-used-next-row',suite.request(k=1,r=[1,0],G=[[[1,0],[0,0]]],
                                                  R=[[1,0]],T=[[[1]]]),False)]
        for name,d,deep in cases:
            print('begin',name,flush=True)
            suite.run_case(name,d,lib,cert,deep=deep,uniform=True)
            suite.save(path,cert)
        cert['complete']=True
        cert['target_complete']=True
        cert['target_complete_qualification']='Conditional local construction with L062 informal ledger; independent critical review pending, not a complete L055 receiver.'
        suite.save(path,cert)
        print('remaining complete streams and uniform thresholds pass;',path.relative_to(suite.ROOT),flush=True)
    except Exception as err:
        cert['failures'].append({'type':type(err).__name__,'message':str(err)})
        suite.save(path,cert)
        raise

if __name__=='__main__':
    main()
