# Lemma 717: the actual positive-bump kernel has unbounded phase variation

## Hypotheses

Retain L714's exact fixed positive bump chi, including its original
even Gevrey plateau and fixed width, and all parameters

    U=121/64, A=27/10, d=5/4, c_0=1/8, u=(3+4i)/10,
    n=12q+3, q>=1, N=n-1, h=A/n,
    omega=A*[log(9/5)-4/5+(121/100)*log(201/121)],
    I=[omega-delta,omega+delta], 0<delta<1/3000.

Thus chi>=0, is supported in I, and equals one on the entire
J=[omega-delta/2,omega+delta/2]. Use the exact H_n, D_n and
inverse p_n of L714, its audited identity R_n(3/20)=P_n+K_n,
L715's analytic logarithm ell_n and limit F, and L716's exact
ratio Q_n and its audited uniform limit Q on I. In particular

    K_n=integral_I chi(v)*p_n(v)dv,
    p_n(v)=(D_n*H_n(0)/h)*exp(n*phi_n(v))*Q_n(v),
    phi_n(v)=-d*v/A+ell_n(exp(-u*v/A))/n.

These are signed complex quantities; no modulus has replaced an
integral. The original family, endpoints, moments and profile are
unchanged. Only this one response term is addressed.

## Conclusion

Let phi(v)=-d*v/A+F(exp(-u*v/A)). Throughout the closed I,

    Re phi'(v)>1/200,       Im phi'(v)>3/50.             (1)

For all sufficiently large permitted n, p_n is nonzero on I and
has a continuous argument theta_n there. Every such lift satisfies

    theta_n(omega+delta/2)-theta_n(omega-delta/2)
                       >n*delta/20-pi.                 (2)

Consequently, for every sufficiently large permitted n, there is
no constant phase rotation putting all p_n(v), v in J, in one
closed half-plane whose boundary passes through zero. In particular
nonnegativity of the actual chi does not give a common-phase
positivity certificate for its signed integral K_n.

This is an obstruction to that specific lower-bound mechanism, not
a bound on |K_n| or |R_n|. It proves neither cancellation nor a zero
of either integral. Their upper/lower exponential rates and comparison
with the actual P_n remain unresolved; log(0)=-infinity is allowed.
The complete spatial Jensen defect, other frequency/comb/tail/moment
terms, angular persistence, amplitude/full charge, H/support and Xi
realization remain independent. This family-specific calculation is
unaudited, not a new general theorem or an RH candidate.

## Proof

### 1. Reused coverage and exact signed reduction

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-03-signed-bump-remainder-rate.md`.
This tests the remaining outer integral within that unchanged target.
The earlier absolute-contour and positive-blend stops do not decide
this integral. L714 (2)--(3) and L716's definition of Q_n give the
displayed formula for p_n by factoring H_n(exp(-u*v/A)); its
nonzero prefactor is independent of v. All finite inversions and
fixed-bump interchanges were audited in L714. No new contour or
analytic extension of chi is used.

L715 imports the polynomial limit from J. Jalowy, Z. Kabluchko and
A. Marynych, *Zeros and exponential profiles of polynomials I*,
[arXiv:2504.11593v1](https://arxiv.org/pdf/2504.11593v1),
Definitions 1.1--1.2, p.3, and Theorem 2.2(a),(b),(e), pp.5--6.
Its positive coefficient profile, reflected real roots, missing
degree and logarithm normalization have already been specialized
and audited in L715; that theorem is not reproved or strengthened
here. The derivative convergence used below is the consequence of
Cauchy's formula in [DLMF 1.9(iii), (1.9.30)--(1.9.31)](https://dlmf.nist.gov/1.9.iii)
already assessed and applied in L716. The purpose of the present
calculation is the signed physical phase, which those sources do
not evaluate.

### 2. Enclose both components of the limiting derivative

By L715--L716, for |z|<1,

    y(z)=-z*F'(z)=sum_(k>=1) m_k*z^k, 0<=m_k<=1,
    phi'(v)=(-d+u*y(exp(-u*v/A)))/A.                   (3)

Use the audited exact moment formula in L716 (6)--(7):

    m_k=exp(-k/(2U))*c_k,
    e_(k,l)=k*(-1)^(l+1)/[(l+2)*U^(l+1)],
    h_0=1, h_m=(1/m)*sum_(l=1)^m l*e_(k,l)*h_(m-l),
    c_k=(1/k)*sum_(m=0)^(k-1) binom(k,k-1-m)*h_m.      (4)

Only k<=80 is needed. This is the same Lagrange--Bürmann
specialization verified in L716, with no new inverse branch.
For x=v/A>=2/5, |exp(-u*x)|<=exp(-3/25)<9/10. Hence the
complex tail and a derivative bound for T(x)=u*y(exp(-u*x)) are

    |T(x)-u*sum_(k=1)^80 m_k*exp(-k*u*x)|
                                  <=5*(9/10)^81=:E_tail,
    |T'(x)|<=|u|^2*sum_(k>=1) k*(9/10)^k=45/2.       (5)

The first inequality bounds the whole complex error, so each real
and imaginary component has at most that error. The same applies
to the second inequality and the displacement from a fixed center.

Set x_0=4019/10000. Enclose omega using, for each x=9/5,201/121,
r=(x-1)/(x+1),

    L(x)=2*sum_(j=0)^11 r^(2j+1)/(2j+1),
    L(x)<=log(x)<=L(x)+2*r^25/[25*(1-r^2)].            (6)

This follows from the positive geometric tail integrated from 0
to r. The resulting rational interval [omega_lo,omega_hi] gives

    x_lo=(omega_lo-1/3000)/A,
    x_hi=(omega_hi+1/3000)/A,
    D=max(|x_0-x_lo|,|x_hi-x_0|).

The certificate verifies x_lo>2/5 and x_0>2/5. Every segment from
x_0 to a point of the actual I/A therefore satisfies (5). The error
in using the complex 80-term sum at x_0 is at most

    E=E_tail+(45/2)*D.                               (7)

All arithmetic is reproduced by

    python3 scripts/one-sided-hankel/signed-bump-phase-certificate-186.py

with full exact coefficients, both components of every sum term,
interval endpoints, errors and checks in
`scripts/one-sided-hankel/signed-bump-phase-certificate-186.json`.
The program recomputes (4); it does not assume a sampled root law
or load midpoint moments from a diagnostic.

For completeness, the interval algorithms are as follows. Work
on the scale 2^120, rounding each lower endpoint down and each
upper endpoint up. Multiply intervals using all four endpoint
products. For 0<=t<=1, the degree-41 and degree-40 alternating
Taylor sums enclose exp(-t). For sine and cosine, the sums through
index 20 are upper bounds; subtracting the next term's magnitude
gives lower bounds. These terms decrease on [0,1]. Here the
arguments are 1/(2U), p*x_0, b*x_0 and 3/25, all in that range,
where p=3/10, b=2/5. Powers of the enclosed exp(-1/(2U)) and
the rational c_k give (4); complex powers of the enclosed
exp(-p*x_0)*(cos(b*x_0)-i*sin(b*x_0)) give the 80-term sum.
Division by positive A and subtraction of d apply to (3).

After subtracting BOTH errors in (7), the certified lower endpoints
for Re phi' and Im phi' have decimal previews 0.00773200098426
and 0.0655048082272 respectively. The load-bearing comparisons
are exact rational inequalities against 1/200 and 3/50 in
`/checks/real_phase_derivative_lower` and
`/checks/imag_phase_derivative_lower`, not those previews.
Both complete values were inspected; all six certificate checks
pass with no failures. Equations (3)--(7) extend these enclosures
over the entire closed I, proving (1).

The separate file
`scripts/one-sided-hankel/signed-bump-outer-rate-diagnostic-186.json`
uses binary64 quadrature to screen a possible comparison. It is
not evidence for (1), any signed rate, or a certified residue bound.
It does not evaluate or replace the actual chi. The initial diagnostic
run lacked mpmath and was replaced with a standard-library diagnostic;
the rigorous certificate is independent of both.

### 3. Finite-array phase lift and the failed lower certificate

L715 gives ell_n/n -> F uniformly on compact subdisks. The path
exp(-u*v/A), v in I, lies in |z|<9/10; a slightly larger compact
subdisk permits Cauchy's formula and hence uniform derivative
convergence. Therefore phi_n' -> phi' uniformly on I. From the
strict margins in (1), one existential onset gives

    Re phi_n'(v)>1/400,    Im phi_n'(v)>1/20,
                                           v in I.     (8)

For L716's lambda(v)=11/8+u*z_v*F'(z_v), its audited bounds are
Re lambda>=1/24 and |lambda|<=47/8. Consequently

    Re Q(v)=Re lambda(v)/|lambda(v)|^2
                    >=(1/24)*(8/47)^2>0.              (9)

Uniform convergence Q_n -> Q implies Re Q_n>0 on the whole I
after another single onset. In particular Q_n and p_n have no
zeros on I. Let a_n(v)=Arg Q_n(v) be its continuous principal
argument in (-pi/2,pi/2). For any fixed choice of argument beta_n
of the nonzero prefactor D_n*H_n(0)/h, a continuous argument of
p_n is

    theta_n(v)=beta_n+n*Im phi_n(v)+a_n(v).            (10)

Every other continuous argument differs by a constant multiple
of 2*pi, since I is connected. Integrate (8) across J, whose
length is exactly delta. The difference of endpoint values of
a_n is greater than -pi; (10) proves (2).

Because delta>0 is fixed before n, eventually n*delta/20>2*pi.
The difference in (2) then exceeds pi. If some constant rotation
put the nonzero continuous curve p_n(J) in a closed half-plane
through zero, its argument lift would lie in one connected
interval of length pi. Indeed the allowed arguments form disjoint
closed intervals of length pi separated by open intervals of
length pi, and a continuous lift cannot cross a gap. Its endpoint
difference could not exceed pi, a contradiction. This excludes
even rotations depending on n. On J the original chi is exactly
one, so the same obstruction holds for chi*p_n wherever needed
to align the entire bump integrand.

This argument permits large, small or zero values after integration.
No step gives a lower bound by integrating the modulus. In
particular the legitimate pointwise expression and derivative
limit cannot be promoted to

    log|K_n|/n = sup_(supp chi) Re phi + prefactor rate + o(1).

That unpaid inference is exactly the remaining issue. The actual
signed-rate target is not solved; this kernel-phase refinement is
parked unless a distinct cancellation-control mechanism is supplied.

## Mathlib

Full matching coverage is not checked. No formalization of this
array, actual bump, winding bound or signed-rate obstruction is
claimed. Cauchy's formula, power-series differentiation, continuous
arguments and exact rational interval arithmetic are supporting
tools, not a matching theorem for R_n. The cited JKM theorem is
used only through the existing audited L715 specialization.
