# Corollary C033s: a uniform signed-exponential omitted-part budget

## Hypotheses

Use the actual-zero normalization and qualified external inputs of
C032s and C033i/j/m/r. In particular the full positive-ordinate divisor
counts multiplicity, z_rho=gamma_rho-i*(beta_rho-1/2), with conjugation,
excluded ordinate zero, strict strip |beta_rho-1/2|<1/2 and gamma_rho>14.
Retain the explicit counting inequality, verified real zeros through100,
retained real zero in(14,15), reciprocal-square tail, heat positivity,
separately controlled fixed-j heat errors through j=2, Gaussian
half-variance convention and both fixed-v1 preprint qualifications.
Neither source-wide correctness nor finite-zero data is independently
certified here. No RH, sign of a width difference, moments, cancellation
or unsmoothed Xi realization is assumed.

On X=[0,infinity), for 1<=sigma<=2, set

    u_sigma(t)=t/(1+4*sigma*t), K(u)=sqrt(u)*H(u),
    D_sigma(t)=ell_sigma(t)-ell_1(t)
              =t^(-3/2)*(K(u_sigma(t))-K(u_1(t))),
    Q_sigma(dt)=D_sigma(t)dt, M_sigma=Q_sigma(X),
    R_sigma=exp(-M_sigma)*E(Q_sigma),
    E(Q)=sum_(j>=0) Q^{*j}/j!, Q^{*0}=delta_0.

C033j supplies these exact signed measures. C033i supplies
P(dt)=ell_1(t)dt restricted to [1,3/2], m=P(X)>0 and
lambda=exp(m)*E(-P). Fix the base Gaver order n=1 and delta=1/16
in C033r, without imposing its positive-separation parameter tests.
Thus x_-=15/16, x_+=17/16, a_x=log(2)/x and

    K_x(t)=2*a_x*exp(-a_x*t)*(1-exp(-a_x*t)),
    S(theta)=integral_X (K_(x_-)(t)-K_(x_+)(t)) dtheta(t).

The width measure eta is any finite real signed Borel measure on
[1,2] with eta([1,2])=1 and |eta|([1,2])<=2; all atoms and singular
parts are allowed. R_eta is the setwise mixture from C033j.

## Conclusion

Uniformly for sigma in [1,2] and t>0,

    |D_sigma(t)| <= 12*t^(-1/2)/(1+4*t),
    ||Q_sigma||_TV <= 6*pi <24.                         (1)

Let a=2^-256, b=2^256, Qc_sigma=Q_sigma restricted to [a,b],
and Mc_sigma=Qc_sigma(X). Define the finite approximants

    Rtilde_sigma=exp(-Mc_sigma)*sum_(j=0)^128 Qc_sigma^{*j}/j!,
    lambdatilde=exp(m)*sum_(j=0)^128 (-1)^j P^{*j}/j!.

Put

    E_cut=60*3^48*2^-128,
    E_series=3^24*24^129/129! *130/106,
    E_lambda=3^21*21^129/129! *130/109.

Then

    ||R_sigma-Rtilde_sigma||_TV <= E_R:=E_cut+E_series,
    ||lambda-lambdatilde||_TV <= E_lambda.             (2)

The finite approximants have bounded Borel width dependence. Write
Rtilde_eta for their signed-width mixture. The combined omitted-part
error in the paired observable is at most

    |[S(lambda)-S(R_eta)]
          -[S(lambdatilde)-S(Rtilde_eta)]|
       <= E_lambda+2*E_R <2^-44 <2^-20.                (3)

This passes the declared order/cutoff budget, including the normalization
and width TV cap. Compact convolution integrals and their scalar
normalizations remain exact unevaluated objects, not certified numerical
values. No feasible runtime, compact quadrature accuracy, positive
separator at these parameters, or actual-Xi positivity is concluded.
This is a local quantitative specialization under assessment1778,
not a mathematical discovery beyond the checked sources. Its conditional
omission claims pass conceptual audit1787 below; external-input and
implementation qualifications remain unchanged.

## Proof

### Inputs and scope of specialization

Reuse SPECIALIZE assessment1778 and source-notes1778. The explicit
heat/counting/displacement inequalities are C032s(10)-(12), proved
there from S. Sra, *On some positivity properties of the Riemann Xi
function*, fixed2610.00584v1, 20 October2026,
[Section2.1 (2.1)-(2.3), Lemma2.1 and PropositionB.1 proof/AppendixB.3,
printed pp.3-4,17](https://hexagonmath.org/pdf/2610.00584v1).
The exact Gaussian identity used in C033j is Sra, *Some positivity
properties of Riemann Xi under smoothing*, fixed2611.00345v1,
[Proposition3.1 (3.2)-(3.3), pp.5-6; proof C.1,
p.21](https://hexagonmath.org/pdf/2611.00345v1).
No source counting theorem or smoothing identity is reproved here.

For finite real signed measures import the convolution exponential
and ||E(Q)||<=exp(||Q||) from V. Cekanavicius and P. Vellaisamy,
*On closeness of two discrete weighted sums*, Modern Stochastics:
Theory and Applications 5(2) (2018), 207-224,
[Section1 after(1), and (23)-(24)](https://www.vmsta.org/journal/VMSTA/article/114/read),
DOI10.15559/18-VMSTA103. The continuous finite-measure framework
applies; its later lattice approximation results are unused.
The new application consists of all-width numerical constants,
endpoint integration and finite-series error propagation. Qualitative
C033j bounds alone do not supply these constants.

### Uniform absolute envelope

Write A=1/(8*sqrt(pi)) and C=1869/400. C032s(10),(12), using
S(u)=sqrt(u)*K'(u), give the two-sided absolute consequence

    |u*K'(u)| <= A+sqrt(u)*(C+log(1/u)/16), 0<u<=1.

This combines separately proved inequalities, without differentiating
an asymptotic remainder or assuming K' has a sign. The derivative of
sqrt(u)*(C+log(1/u)/16) is
(C+log(1/u)/16-1/8)/(2*sqrt(u)), positive on (0,1/4].
Since A<1/8 and log(4)<2, for 0<u<=1/4 the displayed bound is
strictly below 1/8+C/2+1/16=2019/800<3.

For every t>0 and sigma in [1,2], 0<u_sigma(t)<=u_1(t)<1/4.
The exact width identity and the fundamental theorem of calculus give

    |D_sigma(t)|
      <=3*t^(-3/2)*log(u_1(t)/u_sigma(t))
      =3*t^(-3/2)*log(1+4*(sigma-1)*t/(1+4*t))
      <=12*t^(-1/2)/(1+4*t).

Here log(1+y)<=y for y>=0 and sigma-1<=1; the case sigma=1
is included. Substituting y=2*sqrt(t) integrates this envelope to
12*integral_0^infinity 1/(1+y^2)dy=6*pi<24. This proves(1).
For t>=b the same envelope is at most3*t^(-3/2); near zero it is
at most12*t^(-1/2). Consequently

    epsilon_sigma:=||Q_sigma-Qc_sigma||
      <=24*sqrt(a)+6/sqrt(b)=30*2^-128=:epsilon.       (4)

This bounds the omitted jump measure, including all large jumps,
rather than cutting only the observed sum variable. Q_sigma has no
endpoint atoms. It is not assumed positive.

### Normalization and convolution orders

Use K0=24. Both Q_sigma and Qc_sigma have norm at most K0;
their real total masses M_sigma,Mc_sigma have absolute value at
most K0 and differ by at most epsilon. For two such measures Q,Qc,
the telescoping product identity and convolution norm inequality give

    ||Q^{*j}-Qc^{*j}||<=j*K0^(j-1)*||Q-Qc||, j>=1.

Absolute summation yields ||E(Q)-E(Qc)||<=epsilon*exp(K0).
The real scalar mean value theorem likewise gives
|exp(-M)-exp(-Mc)|<=epsilon*exp(K0). Therefore

    ||exp(-M)E(Q)-exp(-Mc)E(Qc)||
      <=2*epsilon*exp(2*K0)<=E_cut.                   (5)

This pays the change in normalization instead of silently retaining
the full mass. The zero atom in both exponentials is their j=0 term;
its change is included in(5).

For j>=129 consecutive scalar series terms K0^j/j! have ratio
at most24/130. Hence

    exp(K0)*sum_(j>=129) K0^j/j!
      <=exp(24)*24^129/129! /(1-24/130)
      <E_series.                                     (6)

This controls every omitted order, with no restriction on the support
of their convolution sums. Equations(5)-(6) give the first part of(2).

C033m(3)-(4) gives ell_1(t)=sqrt(pi)*t^(-3/2)*p_(1+1/(4t))(0)
on [1,3/2], with |p_sigma(0)|<21 on the relevant width interval.
Thus ell_1(t)<42 there and 0<m<21. P is wholly inside [a,b], so
no jump-measure spatial omission is needed for lambda. The signs
(-1)^j do not reduce the safe TV bound. Its order tail is

    exp(m)*sum_(j>=129) m^j/j!
       <=exp(21)*21^129/129! /(1-21/130)<E_lambda.     (7)

The elementary e<3 used in(5)-(7) follows, for example, by bounding
1/j!<=1/2^(j-1) for j>=2, strictly for j>=3, in its positive series.
No numerical exponential routine or asymptotic error is used.

### Paired observable and exact arithmetic

For t>=0 put y=exp(-a_x*t) in [0,1]. Since y(1-y)<=1/4,
0<=K_x(t)<=a_x/2. With a_x<=16*log(2)/15<16/15, both kernels
take values in [0,8/15], so their difference has absolute value at
most8/15<1. In particular S is bounded by the total variation norm
on every finite signed measure. Both kernels vanish at zero; their
zero-atom contributions are exactly retained, without discarding
the atoms in the measure estimates above.

C033j proves sigma->Q_sigma continuous in TV. Restriction to [a,b]
is a contraction, total mass is continuous and each finite convolution
power is continuous in TV. The same holds for Rtilde_sigma, uniformly
bounded in norm. Its signed mixture exists by the same bounded-Borel
integration argument as C033j. Integrating(2) against |eta| with
mass at most2 gives the bound E_lambda+2*E_R in(3). A positive
width integral has not been substituted for a signed one.

All constants in that final bound are rational. The complete exact
calculation is saved in scripts/smoothed-law/paired_truncation_1779.json
and reproduced by

    python3 scripts/smoothed-law/paired_truncation_1779.py

It verifies E_lambda+2*(E_cut+E_series)<2^-44 by integer comparison,
and also checks the required2^-20 threshold and declared order/cuts.
The upper allowance is approximately2.8129500967e-14; that decimal
is explanatory, while the rational comparison is the certificate.
No compact integral or function value is approximated by this script.

### Conceptual audit1787 — 19 November 2026

**Verdict.** Claims (1)-(3) pass under precisely the stated conditional
inputs, cuts, orders and width class. This is independent verification
of the existing application, not a new estimate or a verification of
either fixed-v1 preprint or its finite-zero data. The prior SPECIALIZE
assessment1785 and its source comparison cover this audit. C033t,
compact evaluation, separation parameters and actual-Xi transfer are
outside it. No mathematical input or DAG edge changes.

1. **Absolute heat input and the whole transformed domain.**
   C032s(10) and (12) imply
   |S(u)+A/sqrt(u)|<C+log(1/u)/16, where S(u)=sqrt(u)*K'(u).
   Multiplying by sqrt(u), then using the triangle inequality, yields
   the absolute bound on |u*K'(u)| in this proof. C032s's one-sided
   inequality (13) would not suffice and is not used. The derivative
   of sqrt(u)*(C+log(1/u)/16) has the stated positive numerator on
   (0,1/4]. Its endpoint bound is 2019/800<3. For every finite t>0
   and width in [1,2], the entire integration interval
   [u_sigma(t),u_1(t)] lies inside (0,1/4), so the fundamental-calculus
   argument is valid even as t tends to zero or infinity. At sigma=1
   the interval has length zero. Local heat convergence supplies the
   differentiability here; no asymptotic remainder is differentiated.

2. **Integrated envelope and both endpoints.** With y=2*sqrt(t),
   t^(-1/2)dt=dy and 1+4t=1+y^2, giving exactly 6*pi<24.
   The discarded intervals contribute at most
   integral_0^a 12*t^(-1/2)dt=24*sqrt(a) and
   integral_b^infinity 3*t^(-3/2)dt=6/sqrt(b).
   At a=2^-256,b=2^256 their sum is 30*2^-128. The density has
   no endpoint atoms. This restriction is on individual jumps;
   convolutions may have arbitrarily large sum variables.

3. **Signed normalization, including its atom.** Restriction contracts
   total variation, so both jump norms and both absolute masses are
   at most24. The convolution telescoping identity gives the factor
   j*24^(j-1); summing it gives epsilon*exp(24). On [-24,24],
   the derivative magnitude of x->exp(-x) is at most exp(24), so
   the scalar mass change has the same bound. Splitting the normalized
   difference into its series change and scalar change gives
   2*epsilon*exp(48), hence E_cut by e<3. This does not presume
   either mass is nonnegative. The changed coefficient of delta_0
   is included in the scalar change; j=0 is not dropped.

4. **Compact positive mass and both order tails.** C033m(3) maps
   the closed interval [1,3/2] to the closed width interval [7/6,5/4],
   contained in [1,2]. Its (4) gives |p_width(0)|<21 there;
   explicitly its P_0 bound is less than 3+9+17/2=41/2<21.
   Since sqrt(pi)<2 and t>=1, ell_1(t)<42, and positivity retained
   from the hypotheses gives 0<m<21 after integrating length1/2.
   This step neither changes Gaussian variance nor doubles the divisor.
   For the omitted orders the first term is j=129; every subsequent
   ratio is <=24/130, respectively <=21/130. Multiplication by the
   scalar normalizations costs at most exp(24), respectively exp(21).
   The geometric sums are therefore exactly bounded as in (6)-(7).
   P is supported inside [a,b], so it has no further spatial loss.
   The alternating signs of lambda do not reduce its TV allowance.

5. **Borel dependence and genuine signed mixtures.** The common
   integrable envelope and pointwise continuity give TV continuity
   of Q_sigma, also established in C033j. Restriction, convolution,
   total mass and the scalar exponential preserve this continuity.
   Thus every Borel evaluation of Rtilde_sigma is continuous, and
   ||Rtilde_sigma||<=exp(24)*sum_(j=0)^128 24^j/j!<=exp(48)
   uniformly. The same bound holds for R_sigma. For disjoint Borel
   sets, their finite-union evaluations are bounded by exp(48) and
   converge pointwise to the union evaluation. Dominated convergence
   against the finite measure |eta| therefore proves countable
   additivity of both mixtures. For every finite Borel partition,
   the sum of absolute mixed-error masses is at most
   integral ||R_sigma-Rtilde_sigma|| d|eta|<=2*E_R.
   Taking the supremum gives the claimed TV loss. Bounded simple
   approximation justifies integration of the paired kernel through
   the mixture, exactly as in C033j. No density, absence of singular
   widths, positivity of eta or finite-support assumption is needed.

6. **Paired kernel and exact comparison.** Each kernel takes values
   in [0,8/15], so their difference has magnitude <=8/15<1;
   bounding the difference by the sum would unnecessarily lose this
   bound. Both vanish exactly at zero. The two TV errors therefore
   imply (3), with the factor2 belonging to the width variation cap.
   The independent script scripts/smoothed-law/paired_truncation_audit_1787.py
   reconstructs the order129 terms by recurrence, rather than the
   original factorial expression, and checks all four saved rational
   allowances, the combined value, parameters and thresholds in full.
   Run it by

       python3 scripts/smoothed-law/paired_truncation_audit_1787.py

   Its full certificate is
   scripts/smoothed-law/paired_truncation_audit_1787.json.
   For combined=N/D in lowest terms, the inspected exact comparison is

       D - 2^44*N = 2722668868834682711590823434442454472976270511588013619500156432910590681258788343967435470623659114059579503264849095694551713478269120151059747347087936199161142455765753408187147485184 > 0.

   Thus combined<2^-44; since 2^-44<2^-20, the declared requirement
   also holds. All18 rational consistency/comparison checks passed.
   The allowance is approximately2.81295009666e-14 versus
   2^-44 approximately5.68434188608e-14. These decimals are only
   explanatory; neither previews nor the old boolean flags were
   accepted as verification. No compact integral was evaluated.

The audit establishes the claimed conditional omitted-part input only.
It supplies no positive separation at n=1,delta=1/16, no certification
of the continuum evaluator, and no bound on unrestricted width variation.
The actual-divisor, conjugation/multiplicity, ordinate-zero exclusion,
strict-strip/gamma>14, counting, real zeros through100, retained real
zero, reciprocal-square tail, heat positivity, separate errors through
j=2, Gaussian half-variance and both fixed-v1 qualifications all remain.
The main all-degree positivity, signed-height and realization gaps are
unchanged. PROOF's argument and the ID-only DAG need no modification.

## Mathlib

Full matching coverage for this actual-zero uniform numerical
truncation result is unchecked/unknown. Supporting finite-measure,
convolution, integral and exponential tools do not certify a matching
theorem. Audit1787 is an informal audit of the conditional specialization;
no Lean verification, source-wide audit or zero-data certification is claimed.
