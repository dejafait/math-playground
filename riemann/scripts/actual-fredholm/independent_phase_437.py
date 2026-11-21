"""One fixed independent-phase repair of step435. No refinement or sweep.

Reuses unchanged directed primitives/finite reduction from signed_pair_435.
Full complex DFT, provenance, inherited evidence and actual endpoints saved.
The old analytic evaluator/counting implementation remains independently
unaudited; the saved-data checker is not formal verification.
"""
import hashlib
import json
import platform
import decimal
from pathlib import Path
from signed_pair_435 import (I,C,D,UP,DN,PI,PREC,sincos,geval,load_coeff,
                             finite_data,sym)
BASE=Path(__file__).resolve().parent
SOURCE=BASE/'signed-pair-certificate-435.json'
CERT=BASE/'independent-phase-certificate-437.json'
SAVED=None

def fourier(coeff, eg, alpha, residues, outer):
    N, L = 512, 2048
    sigma, a, rho = I(9)/8, I(7)/8, I(15)/16
    assert all(x.mag() < a.lo for x in alpha)
    m_sigma = I(outer['G_boundary_lower'])/(sigma+a).square()
    mb = (1+a/sigma)**2/m_sigma
    ah, dh = [x.mid() for x in alpha], [x.mid() for x in residues]
    ej, ed = [x.err(y) for x,y in zip(alpha,ah)], [x.err(y) for x,y in zip(residues,dh)]
    assert SAVED['N'] == N and SAVED['L'] == L
    assert len(SAVED['samples']) == L
    samples, phases = SAVED['samples'], []
    phase_width = D(0)
    for j, sample in enumerate(samples):
        assert sample['j'] == j
        quadrant, rem = divmod(j, L//4)
        sn, cs = sincos(2*PI*rem/L)
        z = C(cs, sn)
        for _ in range(quadrant):
            z = C(-z.im, z.re)
        assert z.pair() == sample['z'], ('phase provenance', j)
        phase_width = max(phase_width, UP.subtract(z.re.hi,z.re.lo),
                          UP.subtract(z.im.hi,z.im.lo))
        # Retain every old input error; this is a same-settings containment
        # and provenance check, not a new evaluator or independent audit.
        val = geval(coeff, eg, z*2048)
        assert val.pair() == sample['G'], ('G provenance', j)
        pp = (z-C(alpha[0]))*(z-C(alpha[1]))
        bv = pp*pp/(z*z*val)
        assert bv.pair() == sample['b'], ('b provenance', j)
        phases.append(z)
    sums = [C() for _ in range(N+1)]
    for j, sample in enumerate(samples):
        bv = C(I(*sample['b'][0]), I(*sample['b'][1]))
        for n in range(1,N+1):
            # Periodicity and integer De Moivre: z_j^(-n)=z_((-jn) mod L).
            # No recursively multiplied phase rectangles occur here.
            sums[n] += bv*phases[(-j*n) % L]
        if j % 256 == 255:
            print('independent-phase samples',j+1,'/',L,flush=True)
    beta, epsilon, enclosures, aliases = [], [], [], []
    # b=P^2/(z^2 G) has negative Laurent indices only -2,-1;
    # 1<=n<=512<2048-2 excludes ALL negative aliases.
    assert N < L-2
    for n in range(1, N+1):
        alias = mb/(sigma**(n+L))/(1-I(1)/(sigma**L))
        val = sums[n]/L
        assert (val.im+sym(alias)).lo <= 0 <= (val.im+sym(alias)).hi
        enc = val.re+sym(alias)
        bh = enc.mid()
        beta.append(bh)
        epsilon.append(enc.err(bh))
        enclosures.append(enc.pair())
        aliases.append(alias.pair())
    h_b = sum((n*I(b).square() for n,b in enumerate(beta,1)), I(0)).sqrt()
    q = I(1)/sigma.square()
    tn = q**(N+1)*((N+1)-N*q)/(1-q).square()
    db = (sum((n*I(e).square() for n,e in enumerate(epsilon,1)), I(0))+mb.square()*tn).sqrt()
    t = rho-a
    ms = sum((I(x.copy_abs())/t for x in dh), I(0))
    es = sum((I(e)/t+I(d.copy_abs())*j/t.square() for d,j,e in zip(dh,ej,ed)), I(0))
    hB, dB = ms*rho/(1-rho.square()), es*rho/(1-rho.square())
    # Schatten product inequality, including the cross term, gives TRACE norm.
    err = db*hB+h_b*dB+db*dB
    finite = finite_data(beta, ah, dh)
    kn = I(*finite['finite_norm'])
    original_norm = I(max(D(0),DN.subtract(kn.lo,err.hi)),UP.add(kn.hi,err.hi))
    hat_trace = I(*finite['finite_trace_norm'])
    actual_trace_upper = hat_trace+err
    det_error = err*(1+actual_trace_upper).exp()
    exact_det = I(*finite['finite_determinant'])+sym(det_error)
    sep = exact_det.lo > 0 and original_norm.lo >= 1
    decision = ('SIGNED_SEPARATION' if sep else ('NO_NORM_SEPARATION' if original_norm.hi < 1 else 'INCONCLUSIVE'))
    return {'N':N,'L':L,'sigma':sigma.pair(),'a':a.pair(),'rho':rho.pair(),
            'm_sigma':m_sigma.pair(),'M_b':mb.pair(),
            'alpha_hat':list(map(str,ah)),'residue_hat':list(map(str,dh)),
            'alpha_error':list(map(str,ej)),'residue_error':list(map(str,ed)),
            'samples':samples,'independent_phases':[z.pair() for z in phases],
            'phase_index_rule':'(-j*n)%2048', 'phase_component_width_upper':str(phase_width),
            'DFT_enclosures':[ (sums[n]/L).pair() for n in range(1,N+1)],
            'beta_enclosures':enclosures,'beta_hat':list(map(str,beta)),
            'epsilon':list(map(str,epsilon)),'DFT_alias_errors':aliases,
            'h_b':h_b.pair(),'delta_b':db.pair(),'M_S':ms.pair(),'E_S':es.pair(),
            'h_B':hB.pair(),'delta_B':dB.pair(),'T_N':tn.pair(),
            'finite':finite,'trace_norm_error':err.pair(),'actual_trace_norm_upper':actual_trace_upper.pair(),
            'determinant_perturbation_error':det_error.pair(),'signed_determinant':exact_det.pair(),
            'original_norm':original_norm.pair(),'required_det_lower':'0',
            'required_norm_lower':'1','decision':decision}


def main():
    global SAVED
    assert not CERT.exists(), 'One run only: preserve existing certificate'
    data=json.loads(SOURCE.read_text())
    assert data['pair']==[3,2048] and data['evaluation']['precision']==75
    assert data['evaluation']['uniform_disk_radius']==4096
    assert data['inner_contour']['count_with_multiplicity']==2
    assert data['outer_contour']['count_with_multiplicity']==2
    SAVED=data.pop('signed')
    data['inherited_failures_435']=data.pop('failures')
    data.update(step=437,status='UNFINISHED',failures=[],
        runtime={'python':platform.python_version(),'decimal':decimal.__version__,
                 'libmpdec':decimal.__libmpdec_version__},
        reuse_provenance={'input':'scripts/actual-fredholm/signed-pair-certificate-435.json',
            'input_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            'primitive_sha256':hashlib.sha256((BASE/'signed_pair_435.py').read_bytes()).hexdigest(),
            'scope':'All evaluation/count/root data inherited unchanged; every phase/G/b sample replayed at identical settings; no independent analytic audit.'})
    CERT.write_text(json.dumps(data,indent=2)+'\n')
    try:
        coeff,eg=load_coeff(data['evaluation'])
        alpha=[I(*z['alpha']) for z in data['zeros']]
        residues=[I(*z['residue']) for z in data['zeros']]
        data['signed']=fourier(coeff,eg,alpha,residues,data['outer_contour'])
        signals={}
        from signed_pair_435 import RN
        for name,ctx in [('DN',DN),('UP',UP),('RN',RN)]:
            flags=[key.__name__ for key,value in ctx.flags.items() if value]
            assert set(flags)<={'Inexact','Rounded'},(name,flags)
            signals[name]=flags
        data['context_flags']=signals
        assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==data['reuse_provenance']['input_sha256']
        data['status']=data['signed']['decision']+'_PENDING_INDEPENDENT_AUDIT'
    except Exception as exc:
        data['failures'].append({'type':type(exc).__name__,'message':str(exc)})
        data['status']='FAILED_PARK_REPAIR'
        CERT.write_text(json.dumps(data,indent=2)+'\n')
        raise
    CERT.write_text(json.dumps(data,indent=2)+'\n')
    n=data['signed']
    print(json.dumps({'status':data['status'],'failures':data['failures'],
        **{k:n[k] for k in ['signed_determinant','original_norm','trace_norm_error',
          'determinant_perturbation_error','delta_b','delta_B','h_b','h_B',
          'phase_component_width_upper','required_det_lower','required_norm_lower']},
        'certificate':str(CERT)},indent=2),flush=True)

if __name__=='__main__':
    main()
