#!/usr/bin/env python3
"""Complete frozen Schur test; analytic error ledger is in C744w.

IEEE binary64 round-to-nearest operations, correctly rounded sqrt, and
the standard dot-product gamma bound are the numerical contracts.
Transcendentals use Decimal or explicit Taylor polynomials. NumPy
Cholesky proposes factors; the reconstruction residual certifies them.
"""
import json
import math
import importlib.util
from decimal import Decimal, localcontext
from pathlib import Path
import numpy as np

FOLDER = Path(__file__).parent
N, K, BLOCK, TAU = 512, 65536, 512, 1.43
ENTRY_ERROR = 1e-7
PI_TEXT = '3.141592653589793238462643383279502884197169399375105820974944592307816406'


def constants():
    with localcontext() as ctx:
        ctx.prec = 80
        pi = Decimal(PI_TEXT)
        ell = Decimal(3).ln()/2
        fourth = Decimal(3).sqrt().sqrt()
        return dict(ell=float(ell), pi=float(pi), fourth=float(fourth),
                    logpi=float(pi.ln()),
                    weights=[float(Decimal(p).ln()/Decimal(n).sqrt()) for n,p in POWERS],
                    deltas=[float(7*ell-Decimal(n).ln()) for n,p in POWERS])


POWERS = [(29,29),(31,31),(32,2),(37,37),(41,41),(43,43),
          (47,47),(49,7),(53,53),(59,59),(61,61),(64,2),
          (67,67),(71,71),(73,73),(79,79)]


def sincos(x, pi):
    # Reduce by the nearest multiple of pi/2. Ten Taylor terms on
    # [-pi/4,pi/4] have remainder less than 2e-22.
    q = np.rint(x/(pi/2)).astype(np.int64)
    r = x-q*(pi/2)
    r2 = r*r
    sn = r.copy() if isinstance(r, np.ndarray) else r
    cs = np.ones_like(r)
    ts, tc = r, np.ones_like(r)
    for j in range(1, 11):
        ts = -ts*r2/((2*j)*(2*j+1))
        tc = -tc*r2/((2*j-1)*(2*j))
        sn = sn+ts; cs = cs+tc
    quadrant = q % 4
    sine = np.where(quadrant == 0, sn, np.where(quadrant == 1, cs,
                    np.where(quadrant == 2, -sn, -cs)))
    cosine = np.where(quadrant == 0, cs, np.where(quadrant == 1, -sn,
                      np.where(quadrant == 2, -cs, sn)))
    return sine, cosine


def atan_nonnegative(x, pi):
    inverse = x > 1
    t = np.where(inverse, 1/np.maximum(x, 1e-300), x)
    for _ in range(3):
        t = t/(1+np.sqrt(1+t*t))
    total, term = t.copy(), t.copy()
    for j in range(1, 10):
        term = -term*t*t
        total += term/(2*j+1)
    total *= 8
    return np.where(inverse, pi/2-total, total)


def psi_imag(k, pi):
    # psi(z)=log(z+64)-1/[2(z+64)]-sum_(j<64)1/(z+j)+R.
    # L744(8)'s cited DLMF remainder: |R| <= sqrt(2)/(6|z+64|^2).
    y, a = k/2, 64.25
    value = atan_nonnegative(y/a, pi)+y/(2*(a*a+y*y))
    for j in range(64):
        value += y/((j+.25)**2+y*y)
    remainder = np.sqrt(2)/(6*(a*a+y*y))
    return value, remainder


def head_diagonal(k, con):
    y, a = k/2, 64.25
    with localcontext() as ctx:
        ctx.prec = 80
        logs = np.array([float((Decimal('64.25')**2+(Decimal(float(t))/2)**2).ln()/2)
                         for t in k])
    h = logs-a/(2*(a*a+y*y))-con['logpi']
    for j in range(64):
        h -= (j+.25)/((j+.25)**2+y*y)
    diag = np.zeros(N)
    for start in range(0, 65536, 1024):
        c = 2*np.arange(start,start+1024)+.5
        diag += np.sum(c[None,:]**2/(c[None,:]**2+k[:,None]**2)**2,axis=1)
    cj = 131072.5
    diag += 1/(2*cj)
    diag_error = (1/cj**2+2*k*k*(1/(6*cj**3)+1/cj**4))
    return h, diag, diag_error


def assemble():
    con = constants(); ell, pi = con['ell'], con['pi']
    n = np.arange(K); k = n*pi/ell
    norm = np.full(K,np.sqrt(2/ell)); norm[0]=1/np.sqrt(ell)
    parity = np.where(n%2==0,1.,-1.)
    imag, rem = psi_imag(k,pi)
    b, be = k*imag/2, k*rem/2
    h, diag, diagerr = head_diagonal(k[:N],con)
    moments = np.array([norm*c*(parity*(con['fourth'] if c>0 else 1/con['fourth'])-1)
                        /(c*c+k*k) for c in [.5,-.5]])
    covs = {key:np.zeros((N,N)) for key in ['00','cc','gg','0c','0g','cg']}
    normsq = np.zeros(3); response_error_sq = 0.; head_error = 0.
    head = {}
    def translation(rows, delta):
        kn, km = k[rows,None], k[None,:N]
        sn, cn = sincos(k[rows]*delta,pi)
        sm, cm = sincos(k[:N]*delta,pi)
        signs = parity[rows,None]*parity[None,:N]
        denominator = kn*kn-km*km
        if rows.start==0:
            denominator[np.arange(N),np.arange(N)]=1
        if delta>0:
            numerator = -signs*kn*sn[:,None]+km*sm[None,:]
        else:
            numerator = kn*sn[:,None]-signs*km*sm[None,:]
        out = numerator/denominator
        if rows.start==0:
            values = np.empty(N)
            values[0]=ell-abs(delta)
            values[1:]=((ell-abs(delta))*cm[1:]/2
                        -np.sign(delta)*sm[1:]/(2*k[1:N]))
            out[np.arange(N),np.arange(N)]=values
        return out*np.outer(norm[rows],norm[:N])

    for start in range(0,K,BLOCK):
        rows = slice(start,start+BLOCK)
        kn, km = k[rows,None], k[None,:N]
        denominator = kn*kn-km*km
        if start==0:
            denominator[np.arange(N),np.arange(N)]=1
        same = parity[rows,None]==parity[None,:N]
        scale = 2*np.outer(norm[rows],norm[:N])*same
        response = (b[rows,None]-b[None,:N])/denominator
        error = (be[rows,None]+be[None,:N])/abs(denominator)
        if start==0:
            response[np.arange(N),np.arange(N)]=diag
            error[np.arange(N),np.arange(N)]=diagerr
        for j in range(64):
            c=2*j+.5
            response -= ((3.**(-j)/con['fourth'])*parity[rows,None]
                         *c*c/((c*c+kn*kn)*(c*c+km*km)))
        response *= scale; error *= scale
        t, tt = np.zeros_like(response), np.zeros_like(response)
        for delta, weight in zip(con['deltas'],con['weights']):
            t += weight*translation(rows,delta)
            tt += weight*translation(rows,-delta)
        for j in range(1,8):
            c=2*j+.5
            decay=3.**(-j)/con['fourth']
            minus=norm*c*(1-parity*decay)/(c*c+k*k)
            plus=norm*c*(parity-decay)/(c*c+k*k)
            prefactor=3.**(-6*j)/(3*np.sqrt(3.))
            t += prefactor*np.outer(minus[rows],plus[:N])
            tt += prefactor*np.outer(plus[rows],minus[:N])
        w0=response+256*moments[:,rows].T@moments[:,:N]
        wc,wg=(t+tt)/2,(t-tt)/2
        if start==0:
            m0=w0.copy(); m0[np.arange(N),np.arange(N)]+=h
            # Exact head matrices are Hermitian / skew-Hermitian.
            head=dict(m0=(m0+m0.T)/2,mc=(wc+wc.T)/2,mg=(wg-wg.T)/2)
            head_error=float(np.linalg.norm(error))+float(max(rem[:N]))
        else:
            response_error_sq += float(np.sum(error*error))
            normsq += [np.sum(w0*w0),np.sum(wc*wc),np.sum(wg*wg)]
            covs['00'] += w0.T@w0; covs['cc'] += wc.T@wc
            covs['gg'] += wg.T@wg; covs['0c'] += w0.T@wc
            covs['0g'] += w0.T@wg; covs['cg'] += wc.T@wg
        if start in [0,16384,32768,49152]:
            print(f'Complete covariance prefix: through {start+BLOCK-1} / {K-1}',flush=True)
    norms=np.sqrt(normsq)
    base_error=math.sqrt((K-N)*N)*ENTRY_ERROR
    f_error=math.sqrt(response_error_sq)+3*base_error
    m_error=head_error+3*N*ENTRY_ERROR
    # Gamma bounds for each blocked dot product, all additions and
    # subsequent norm calculations are below this deliberately loose cap.
    covariance_rounding=1e-6
    schur_error=m_error+((2*sum(norms)+f_error)*f_error+covariance_rounding)/TAU
    data=dict(**head,**{'cov'+key:value for key,value in covs.items()})
    path=FOLDER/'complete-covariance-532.npz'
    np.savez_compressed(path,**data)
    error_ledger=dict(analytic_head_error=head_error,analytic_response_q_error=math.sqrt(response_error_sq),
                      elementary_error_per_entry=ENTRY_ERROR,complete_head_error=m_error,
                      finite_covariance_factor_error=f_error,covariance_rounding=covariance_rounding,
                      sampled_schur_error=schur_error,factor_frobenius_norms=norms.tolist())
    assert schur_error<.012
    assert norms[0]+base_error+math.sqrt(response_error_sq)<.7
    return data,error_ledger


def certify_phases(data):
    con=constants(); pi=con['pi']
    factors,samples=[],[]
    ident=np.eye(N)
    for j in range(65):
        theta=j*pi/64
        s,c=sincos(np.array(theta),pi)
        cov=(data['cov00']+c*c*data['covcc']+s*s*data['covgg']
             +c*(data['cov0c']+data['cov0c'].T)
             +1j*s*(data['cov0g']-data['cov0g'].T)
             +1j*c*s*(data['covcg']-data['covcg'].T))
        matrix=data['m0']+c*data['mc']+1j*s*data['mg']-cov/TAU
        matrix=(matrix+matrix.conjugate().T)/2
        factor=np.linalg.cholesky(matrix-.24*ident)
        residual=float(np.linalg.norm(matrix-.24*ident-factor@factor.conjugate().T))
        # Exact product / residual differs by <1e-6, as detailed in C744w.
        assert residual<1e-7
        assert np.max(abs(factor))<20
        assert np.max(abs(matrix))<400
        factor_normsq=float(np.sum(abs(factor)**2))
        assert factor_normsq<10000
        factors.append(factor)
        samples.append(dict(index=j,theta=float(theta),reconstruction_residual_frobenius=residual,
                            exact_stored_matrix_floor=.24-1e-6,
                            factor_frobenius_norm_squared=factor_normsq,
                            maximum_factor_entry=float(np.max(abs(factor))),
                            maximum_matrix_entry=float(np.max(abs(matrix)))))
    path=FOLDER/'phase-cholesky-factors-532.npz'
    np.savez_compressed(path,factors=np.array(factors))
    return samples


def scalar_tail():
    spec=importlib.util.spec_from_file_location('scalar531',FOLDER/'complete-schur-531.py')
    module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    I=module.I
    def atan_interval(denominator):
        q=I(1)/denominator; power=q; total=I(0)
        for j in range(80):
            total += ((-1)**j)*power/(2*j+1)
            power=power*q*q
        return I(total.lo,(total+power/161).hi)
    pi_interval=16*atan_interval(5)-4*atan_interval(239)
    decimal_pi_error=pi_interval-I(PI_TEXT)
    float_pi_error=pi_interval-I(Decimal(float(PI_TEXT)))
    assert max(abs(decimal_pi_error.lo),abs(decimal_pi_error.hi))<Decimal('1e-55')
    assert max(abs(float_pi_error.lo),abs(float_pi_error.hi))<Decimal('2e-16')
    ell=I(3).ln()/2
    # Elementary Archimedes bound pi>223/71>3.14 suffices here.
    pi_lower=I('3.14')
    fourth=I(3).sqrt().sqrt()
    a=sum((I(p).ln()/I(n).sqrt() for n,p in POWERS),I(0))
    b=4*ell*(1+I('1.5')/fourth)/(pi_lower*pi_lower)
    response=(I(256)/(K-1)).sqrt()*(1+b/K)
    prime=2*a/pi_lower*(I(512)/(K-512)).sqrt()
    continuous=1/(I(2187)*I(3).sqrt()*I('2.5')*(1-I(1)/729))
    moment_coefficient=(2/ell).sqrt()*(fourth+1)*ell*ell/(2*pi_lower*pi_lower)
    moment=256*(I(3).sqrt()-1/I(3).sqrt()).sqrt()*moment_coefficient*(I(2)/(3*(K-1)**3)).sqrt()
    total=response+prime+continuous+moment
    assert total.hi<Decimal('.5')
    assert a.hi<Decimal('7.654')
    return dict(response_tail=response.json(),prime_tail=prime.json(),
                continuous_tail=continuous.json(),moment_penalty_tail=moment.json(),
                full_factor_tail=total.json(),required_tail_norm='.5',
                prime_weight_sum=a.json(),response_coefficient=b.json(),
                machin_pi_interval=pi_interval.json(),float_pi_error=float_pi_error.json())


def main():
    data,ledger=assemble()
    samples=certify_phases(data)
    tail_certificate=scalar_tail()
    # C744w's full-mode analytic tail and phase interpolation estimates.
    tail_norm=.5; tail_debt=tail_norm**2/TAU
    second_derivative=4.71+2*(4.71**2+(.7+4.71)*4.71)/TAU
    phase_debt=second_derivative*(math.pi/64)**2/8
    lower=.24-1e-6-.012-.175-.022
    assert second_derivative<72
    assert phase_debt<.022
    assert lower>.025
    result=dict(parameters=dict(N=N,K=K,penalty=256,tau='1.43',phase_intervals=64),
                arithmetic_contract='IEEE binary64 round-to-nearest, correctly rounded sqrt, dot-product gamma bounds; Decimal and explicit Taylor elementary evaluations; see C744w',
                error_ledger=ledger,phase_checks=samples,
                scalar_tail_certificate=tail_certificate,
                full_tail_norm_upper=tail_norm,full_tail_schur_debt_upper=tail_debt,
                phase_second_derivative_upper=second_derivative,phase_interpolation_debt_upper=phase_debt,
                uniform_residual_lower=lower,required_uniform_residual_lower=0,
                rounded_debts=dict(sample_reconstruction='.000001',finite_approximation='.012',
                                   infinite_covariance='.175',phase_interpolation='.022'),
                certified_claim='C744v(C) >= 0.025 I under the stated arithmetic contract and C744v response identity',
                failures=[],independent_audit_complete=False,rh_candidate=False,
                files=['scripts/separation-seven/complete-covariance-532.npz',
                       'scripts/separation-seven/phase-cholesky-factors-532.npz'])
    path=FOLDER/'complete-residual-certificate-532.json'
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(f'Full Schur lower bound: {lower:.9f}; required >=0; claimed >0.025. Tail debt {tail_debt:.9f}; phase debt {phase_debt:.9f}; arithmetic/source-approximation debt {ledger["sampled_schur_error"]:.9f}.',flush=True)
    print(f'Failures: none; separate audit pending. Certificate: {path}',flush=True)


if __name__=='__main__':
    main()
