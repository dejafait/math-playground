# Lemma 402: quantitative measure of the physical positive-discriminant set

## Hypotheses

Use the fixed actual real functions F=F_0,G and positive gamma envelope
A of L390/L401 on t>=40. All primes are ordinary height derivatives.
Set

    T=1+t, L=log(2+t), f=F/A,
    R=exp(i phi), Z=zeta(5/2+it), a=Re(RZ), W=a f,
    D=(2F'G'-FG''-F''G)^2-4(F'^2-FF'')(G'^2-GG''),
    Delta=D/(A^4 T^4 L^4).

R is the actual gamma carrier, with |R|=1 on this real ray. Z is the
complete right-line zeta value, not a finite response head. The weight
W is exactly L401's direction u=(1,0,0), v=0. H tends to infinity
through all real values. Use L401's audited positive weighted mean,
L390's complete physical second-moment bound, and L391's audited
critical-line consequence of Bourgain's theorem. No RH, phase
independence, weight lower bound, eighth-moment estimate, simplicity,
disjointness, growing head, common-zero upper bound or total L367
pencil-margin assumption is made.

## Conclusion

There exist fixed constants c_+>0 and H_+>=40 such that for every real
H>=H_+,

    meas{t in [H,2H]:D(t)>0} >= c_+ H^(1/3)(log H)^4.       (1)

Here meas is Lebesgue measure. Constants and onset are existential and
are not evaluated. The lower bound is sublinear; it proves no fixed
positive proportion and no optimal exponent. The separate step 90 critical
audit below validates this local REPRODUCTION application of known tools.
It supplies no global mixed positivity, total L367 margin, actual
common-zero upper count, Laguerre sign, zero-exclusion range or RH
conclusion.

## Proof

The unchanged prior SPECIALIZE assessment is
`drafts/literature/2026-10-12-positive-discriminant-measure.md`.
The primary inputs are imported, not reproved:

- J. Bourgain, *Decoupling, exponential sums and the Riemann zeta
  function*, J. Amer. Math. Soc. 30 (2017), 205–224,
  [arXiv:1408.5794v2, Theorem 5/(0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2):
  for each fixed epsilon>0,
  |zeta(1/2+it)|<<_epsilon t^(13/84+epsilon) as t tends to infinity.
- H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function
  Z(t)*, [arXiv:2304.05178v1, Theorem 3 and its defining asymptotic](https://arxiv.org/html/2304.05178v1):
  unconditional fixed-order fourth product moments of ordinary Hardy
  derivatives. L390 already specializes the orders zero through two
  to the complete physical second-moment upper bound used here.
  The sign-set integral Cauchy–Schwarz application is also used in
  that source, (3)–(4).

The family-specific task is to apply these inputs to L401's exact
response-dependent square weight and its positive signed mean. None
of these source statements is imported as the conclusion (1). No new
source moment theorem is proved or assumed.

### Exact square-weight upper bound

L391 (3), restricted to the real ray and to order zero, gives the
zero-safe identity

    f(t)=-R(t) zeta(1/2+it),
    |f(t)|=|zeta(1/2+it)|.                              (2)

This is not a division by zeta and remains valid at zeros. Choose the
fixed epsilon=1/168 in Bourgain's theorem. Since

    13/84+1/168=9/56<1/6,

there are fixed C_f>0 and t_0>=40 such that |f(t)|<=C_f t^(1/6)
for every real t>=t_0, as already used in L391. Absolute convergence
of the complete right-line Dirichlet series gives

    |a(t)|<=|R(t)Z(t)|=|Z(t)|<=zeta(5/2).

Consequently, for every H>=t_0 and every t in [H,2H],

    0<=W(t)^2=a(t)^2 f(t)^2<=B H^(1/3),
    B=2^(1/3) zeta(5/2)^2 C_f^2>0.                    (3)

This bounds the exact square weight, including its actual carrier.
It imposes no lower bound at any height and makes no independent-phase
replacement. Only the order-zero pointwise bound is needed; logarithmic
derivative losses are absent.

### Positive-part restriction and full second moment

Put ell=log H. L401 (1), (3) gives, for this fixed weight,

    (1/H) integral_[H,2H] Delta(t)W(t)^2 dt
        =gamma ell^4+o(ell^4),
    gamma=Psi/(71680 pi^2 zeta(2))>0.                   (4)

Psi is L401's positive, finite-valued, absolutely convergent infinite
arithmetic sum; it is not a truncated response sum. The statement of
L401 takes H through all real values. Thus there is a fixed H_1 such
that the absolute little-o term is at most (gamma/2)ell^4 for every
real H>=H_1. In particular the unnormalized integral satisfies

    integral_[H,2H] Delta W^2 >= (gamma/2) H ell^4.      (5)

L390 (1) gives a fixed C_Delta>0 and H_2 such that for every real
H>=H_2,

    integral_[H,2H] |Delta|^2 <= C_Delta H ell^4.       (6)

Indeed its normalized L^2 norm is O(ell^2), so squaring that norm
gives precisely (6). This is the complete physical Delta, with its
envelope-curvature correction and response tails; the leading
replacement d is not substituted for Delta in this proof. A sharper
square-moment asymptotic from L393 is unnecessary.

Let E_H={t in [H,2H]:Delta(t)>0}. All functions here are smooth on
the ray, and the divisor A^4T^4L^4 is strictly positive. Therefore
E_H is measurable and equals {t in [H,2H]:D(t)>0}. On the compact
interval all integrals below are finite. Since W^2>=0 and Delta<=0
on the complement of E_H, (5) implies

    (gamma/2)H ell^4
       <= integral_[H,2H] Delta W^2
       <= integral_[E_H] Delta W^2.                    (7)

For H at least max(t_0,H_1,H_2), using (3), Delta>0 on E_H,
integral Cauchy–Schwarz on E_H and then (6), we have

    integral_[E_H] Delta W^2
       <= B H^(1/3) integral_[E_H] Delta
       <= B H^(1/3) sqrt(meas(E_H) integral_[E_H] Delta^2)
       <= B H^(1/3) sqrt(meas(E_H) C_Delta H ell^4).    (8)

All sides are nonnegative. Squaring (7)–(8) and keeping every power
gives

    (gamma^2/4) H^2 ell^8
       <= B^2 C_Delta H^(5/3) ell^4 meas(E_H),
    meas(E_H) >= [gamma^2/(4 B^2 C_Delta)] H^(1/3)ell^4.

Take c_+=gamma^2/(4 B^2 C_Delta)>0 and enlarge H_+ to be at least
max(40,t_0,H_1,H_2,e). This proves (1) for every real H>=H_+.
The constants are independent of H; no response-head limit is taken
in this application. The achieved lower bound equals the approved
threshold. Since H^(-2/3)(log H)^4 tends to zero, it is consistent
with the interval length H and does not assert positive density.

The exact weight is essential: the stopped fixed-jet, mollifier and
Wronskian-square directions in L394/L399/L400 have negative leading
means. Their failures are preserved and are not reopened. L389's
negative-set bound is a comparison, not a premise of (7). Neither
sign-set bound controls a pointwise total pencil margin or excludes
an off-line zeta zero.

### Separate critical audit — 2026-10-12, step 90

This REPRODUCTION proof_audit uses the unchanged prior SPECIALIZE
assessment `drafts/literature/2026-10-12-positive-discriminant-measure-critical-audit.md`.
The conclusion (1) passes with its stated existential constants and
all-real-H quantifiers. The only clarification is that Psi is an infinite
absolutely convergent sum, not a finite sum. No mathematical hypothesis,
threshold or input is changed. This verifies a local known-tool application,
not a new source theorem, certified originality or an RH candidate.

**Exact physical functions and sign.** L401's direction u=(1,0,0), v=0
has p=x=f and r=0, hence W=a f exactly. There is no factor c=1/(4pi)
inside W: that factor is already squared in L401's coefficient. Indeed
c^2/4480=1/(71680 pi^2), so its gamma is exactly (4). The complete
Z=zeta(5/2+it) is used throughout. L401's scalar satisfies 1<=Psi<infinity;
its audited summable majorant is 16(mn)^(-3/2). Thus gamma is a fixed,
strictly positive real number, independent of H or a response cutoff.

The inherited envelope is A=(t^2+1/4)|Gamma(1/4+it/2)|pi^(-1/4).
On t>=40 the gamma argument is never a pole, gamma has no zeros,
and every displayed factor is positive. Thus A,T,L are smooth and
strictly positive. F,G and their derivatives are real and smooth there,
so Delta is continuous and real. Its divisor A^4 T^4 L^4 is positive,
even when F or G vanishes. Hence E_H={Delta>0} is a relatively open,
measurable subset of [H,2H] equal to {D>0}, and all integrands used in
(5)–(8) are bounded on that compact interval. The envelope's decay at
infinity causes no compact-interval integrability defect.

**Pointwise budget for the square.** The order-zero case of audited
L391 (3) is the identity f=-R zeta(1/2+it), not a quotient by zeta.
Since |R|=1 on the real ray, it gives (2), including at every zero.
Bourgain's stated theorem applies to every fixed epsilon>0; fixing
epsilon=1/168 gives 9/56<1/6, with a constant independent of height.
For t>=max(t_0,1), replacing t^(9/56) by t^(1/6) is legitimate.
Absolute convergence gives |Re(RZ)|<=zeta(5/2), without any phase or
nonvanishing premise. Squaring f's bound and using t<=2H gives
exactly W^2<=B H^(1/3) with B as in (3). The proof uses a bound for
W^2, not W, and never needs a lower bound for that weight.

**Complete norm and uniform absorption.** In L390 the normalized norm
is ||Delta||_(2,H)=(H^(-1) integral |Delta|^2)^(1/2).
Its O(ell^2) upper bound therefore gives (6), with ell^4 after squaring
and H after undoing normalization. The bound applies to physical Delta:
its proof retains the envelope-curvature term and complete response,
and combines ||Delta-d||_(2,H)=O(ell) with ||d||_(2,H)=O(ell^2).
It follows from fixed ordinary Hardy fourth moments through order two;
neither an eighth moment nor the sharper L393 coefficient is required.

L401's audited sharp mean (1) is for all real H tending to infinity.
Its complete-tail argument fixes a head and smoothing width before
taking the height limit, and then removes them with absolute errors.
For any fixed tolerance it consequently supplies a single height beyond
which the full mean is within that tolerance at every real H. Choose
the tolerance gamma/2 after fixing the present direction. This yields
H_1 in (5); there is no dependence of gamma or the weight on a head
chosen as a function of H. L390 similarly supplies fixed C_Delta,H_2.
Increasing positive constants when necessary, t_0,H_1,H_2 and e can
therefore be absorbed into one H_+ independent of H.

**Both positivity restrictions and the final powers.** On E_H's
complement Delta W^2<=0, so deleting that complement can only increase
the signed integral. On E_H itself Delta>0, which licenses replacing
W^2 by its upper bound; that replacement on the full signed interval
would be unjustified. Integral Cauchy–Schwarz with 1 and Delta on E_H,
followed by the complete norm bound, gives

    (gamma/2) H ell^4
      <= B H^(1/3) [meas(E_H) C_Delta H ell^4]^(1/2).

Every factor is nonnegative. Squaring produces H^2 ell^8 on the left
and B^2 C_Delta H^(5/3) ell^4 meas(E_H) on the right. Since H>1,
division is valid and yields precisely c_+ H^(1/3)ell^4 with
c_+=gamma^2/(4 B^2 C_Delta)>0. This also rules out meas(E_H)=0;
no prior positive-measure assumption is used. The threshold is below
H eventually, since its ratio to H tends to zero.

The audit reaches the approved threshold without a numerical certificate
or reproof of a cited moment theorem. It provides no density assertion,
effective onset, upper bound on common zeros or total signed pencil
margin. The separate stopped weights L394/L399/L400 remain stopped;
global actual-theta mixed positivity and RH remain unresolved.

## Mathlib

Full matching coverage of this physical positive-set theorem, L401's
weighted mean, the Hardy moment theorem and Bourgain's subconvexity
is not checked. The prior assessment inspected the
[Holder module](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/Holder.html)
for supporting bilinear/Lp infrastructure, without identifying an exact
integral Cauchy–Schwarz declaration. The mathematical inequality is
the standard integral Cauchy–Schwarz inequality, also used in Bui–Hall
(3)–(4). No absence of a matching Mathlib theorem is claimed.
