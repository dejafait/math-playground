# Corollary C034i: actual-divisor curvature and the negative final width prefix

## Hypotheses

Retain exactly C034b/c's qualified actual-zero family. Let Z+ be the
multiset of positive-ordinate nontrivial zeros rho=beta_rho+i*gamma_rho,
with every occurrence of every multiplicity labeled separately, and put
z_rho=gamma_rho-i*delta_rho, delta_rho=beta_rho-1/2. The multiset of z_rho
is conjugation invariant, gamma_rho>14, |delta_rho|<1/2, and
N(T)=O(T log(T+2)). There is no ordinate-zero member. Displacement is
zero for every gamma_rho<=100, and a real member r in (14,15) is retained.
For Gaussian half-variance sigma>0 set

    G_sigma(v)=exp(-v^2/(4*sigma))/sqrt(4*pi*sigma),
    p_sigma(x)=(1/2)sum_rho[G_sigma(x-z_rho)+G_sigma(x+z_rho)],
    R_sigma(w)=int_0^infinity
                   (p_sigma(x)-p_sigma(i*w))/(x^2+w^2) dx,
    b_sigma(w)=4*int_0^w t*R_sigma(t) dt
                              +2*pi*int_0^w p_sigma(i*t) dt.

Use the continuous removable quotient and the zero-normalized
primitives, as in C034b and C032n. The regularity and common spatial
majorants hold on I=[1/2,3], with differentiation on its interior.
Only sigma in [1,2] is a sign domain. Define, for j=1,2,

    k_j(sigma)=exp(-b_sigma(sqrt(j))),
    d_j=partial_sigma b_sigma(sqrt(j)),
    e_j=partial_sigma^2 b_sigma(sqrt(j)),
    Q_j(x)=4*j*(3*x^2+j)/(x^2*(x^2+j)^2), x>0,
    C=d_1*e_2-d_2*e_1,
    T=d_1*d_2*(d_1-d_2)+C,
    S_p=sum_rho gamma_rho^(-p), p=4,8.

For the probability interpretation retain C034b's full inherited
C033w/C033l/C032q identification
k_j=int_[0,infinity) exp(-j*u) dnu_sigma(u), with zero drift and
killing. This retains both fixed-v1 preprint qualifications, heat
positivity, the separate fixed-j=0,1 heat-error inputs, the verified
zeros through100, the retained real zero and the qualified tail
sum_(gamma>100) gamma^-2<1. Source-wide validity and the finite-zero
data are not independently validated here. These probability inputs
are not a proof that p_sigma or p_sigma-p_sigma(0) is nonnegative.
The analytic argument uses the stated divisor conditions and the
audited analytic conclusions of C034b/c/h; it assumes no RH, positive
spatial profile or signed-width realization.

## Conclusion

For every sigma in the entire closed interval [1,2],

    C < -50*S_4*S_8 < 0,                                   (1)
    T < -50*S_4*S_8-S_4^3/5 < 0.                           (2)

With columns (1,k_1,k_2) and rows indexed by increasing width
derivative order, the final prefix satisfies

    W(1,k_1,k_2)=k_1*k_2*T
       < -k_1*k_2*(50*S_4*S_8+S_4^3/5) < 0.               (3)

The lower prefixes are W(1)=1 and C034b's W(1,k_1)<0.
Thus C034c(20)'s sufficient scalar inequality and C034b's missing
final-prefix sign hold under the stated qualifications. No ECT theorem,
fixed-site nonsingularity or conditioning conclusion is invoked here.
The countable assembly is a local specialization of standard absolute
integration and already audited estimates, not a claim of mathematical
novelty. This proof from attempt1868 passes conceptual audit1870 below
on exactly the stated qualified domain.
It is not a candidate proof of RH.

## Proof

### Imported result and scope

Use the pre-invocation SPECIALIZE assessment1867,
`drafts/literature/2026-11-20-laplace-actual-divisor-assembly-attempt-1867.md`.
Import the standard Fubini theorem in John K. Hunter, *Measure Theory*,
Section5.6, Theorem5.18 and Example5.19, printed p61,
[primary notes](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch5.pdf).
For sigma-finite measure spaces and a measurable real or complex
function, a finite iterated absolute integral implies integrability
on the product and equality of the iterated integrals. Example5.19
specializes to absolutely summable complex double series with counting
measure. The statements were inspected in the reused source coverage;
no proof is printed there, and no inspection of such a proof is claimed.
For parameter limits use Hunter, Section4.5, Theorem4.24, printed p49,
and Section4.6, p50,
[primary notes](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf):
measurable pointwise limits with an integrable common dominator may be
integrated termwise, including the complex-valued extension. The reused
coverage inspected that proof. Source revision dates remain unverified.

The checks below establish the required absolute integrals for this
specialization. They do not reprove Fubini, dominated convergence or
the signed estimate C034h(1). No infinite shifted contour is used.

### Full labeled member sums and their dominators

For each labeled occurrence rho define exactly C034h's complete member

    h_rho(x)=Re([G_sigma(x-z_rho)+G_sigma(x+z_rho)]/2),
    A_rho(x)=h_rho(x)-h_rho(0),
    B_rho(x)=h_rho''(x)-h_rho''(0),
    D_j(rho)=int_0^infinity A_rho(x)*Q_j(x) dx,
    E_j(rho)=int_0^infinity B_rho(x)*Q_j(x) dx.             (4)

The primes here are spatial derivatives. C032n(8)-(9), applied as in
C034c(21) and audit1845, give an integrable bound before any signed
summation. The precise applicability check is as follows. Put

    U_(rho,k)=sup_(sigma in I, 0<=x<=1)|h_rho^(k)(x)|,
    V_rho(x)=exp(-(x-gamma_rho)^2/24)
                              +exp(-(x+gamma_rho)^2/24).

For k=0,2,4, U_(rho,k)<=c_k*exp(-(gamma_rho-1)^2/24), and each
sum_rho U_(rho,k) is finite by the counting hypothesis. Every h_rho
is even. Hence on 0<x<=1,

    |A_rho(x)|+|B_rho(x)|
       <=(x^2/2)*(U_(rho,2)+U_(rho,4)).

Since x^2 Q_j(x)<=12j, this gives a summable constant envelope for
the weighted integrands on (0,1]. On x>=1 the same Gaussian estimate
gives, with one constant c independent of rho,sigma,x,

    |A_rho(x)|+|B_rho(x)|<=c*(V_rho(x)+V_rho(0)).

Here Q_j<=12j/x^4, sum_rho V_rho(0)<infinity, and C032n(9) gives
int_1^infinity sum_rho V_rho(x)/x^2 dx<infinity. Consequently the
two displayed envelopes define nonnegative functions M_(rho,j)(x)
such that

    sup_(sigma in I) (|A_rho(x)|+|B_rho(x)|)*Q_j(x)
          <=M_(rho,j)(x),
    sum_rho int_0^infinity M_(rho,j)(x) dx < infinity.       (5)

All profiles and their subtracted integrands are measurable, being
continuous for x>0 and sigma in I. The divisor labels with counting
measure form a countable, hence sigma-finite, space; (0,infinity)
with Lebesgue measure is sigma-finite. Thus (5) meets the cited Fubini
hypotheses. It also dominates measurable limits in width, since every
fixed member is continuous in sigma. No raw integral of h_rho(0)Q_j
or h_rho''(0)Q_j is separated at the origin.

Normal convergence, conjugation invariance and reality of the total
profile identify sum_rho h_rho=p_sigma and sum_rho h_rho''=p_sigma''.
Indeed the normally convergent complex summands occur with their
conjugates; taking their real parts and summing does not change the
sum. Both conjugate labels remain, even when their real members are
identical. Every multiplicity remains, and the factor1/2 in each member
is exactly the factor1/2 in p_sigma. Therefore C034c(16),(21) give

    sum_rho D_j(rho)=d_j,
    sum_rho E_j(rho)=e_j.                                (6)

Both series converge absolutely. Equation (5) gives a single dominating
series of member integral bounds on I, so they also converge uniformly
there. The identities for the normalized derivatives, including the
subtracted origin term in e_j, are those already established in C034b/c.

### The independent ordered-pair normalization

For two independently chosen labeled occurrences rho,tau put

    P_(rho,tau)=[D_1(rho)E_2(tau)+D_1(tau)E_2(rho)
                    -D_2(rho)E_1(tau)-D_2(tau)E_1(rho)]/2.

This is exactly C034h's P(z_rho,z_tau). The set of pairs is the full
ordered Cartesian square, including its diagonal and every unequal
pair; no restriction to conjugate pairs is made. If
a_j=sum_rho |D_j(rho)| and b_j=sum_rho |E_j(rho)|, (5) implies

    sum_(rho,tau) |P_(rho,tau)| <= a_1*b_2+a_2*b_1 < infinity.

This bound holds also with the absolute member integrals in place of
|D_j| and |E_j|. Thus, if products are expanded into two spatial
integrals, the same bound verifies Fubini on the two independent
counting and Lebesgue factors. In particular the counting-measure
Example5.19 permits reordering and factoring the four scalar sums.
Using (6) gives exactly

    sum_(rho,tau) P_(rho,tau)
      =[d_1*e_2+d_1*e_2-d_2*e_1-d_2*e_1]/2=C.             (7)

There is no additional normalization by the divisor's size or by the
mass of a spatial measure. The ordered-pair symmetry cancels precisely
the factor1/2 in P and preserves the determinant order defining C.

### Quantitative strictness and the final prefix

The count implies S_p<infinity for p=4,8: on the dyadic block
2^n<gamma<=2^(n+1), its contribution is O((n+1)*2^(-n*(p-1))).
Finitely many initial blocks are harmless. The retained real label
rho_0 with gamma in (14,15) gives S_p>15^-p>0. Define

    s_(rho,tau)=gamma_rho^-4*gamma_tau^-8
                                  +gamma_rho^-8*gamma_tau^-4.

The nonnegative series has sum 2*S_4*S_8<infinity. Every pair meets
C034h's hypotheses, including independent strict displacements and
zero displacement through100. Thus at any fixed sigma in [1,2],

    q_(rho,tau)=-P_(rho,tau)-25*s_(rho,tau)>0.

The series of q is finite, by the absolute summability of P and s.
It is strictly positive since it includes q_(rho_0,rho_0)>0. Summing
this identity and using (7) proves

    -C-50*S_4*S_8=sum_(rho,tau) q_(rho,tau)>0,

which is (1). This argument supplies strictness after the infinite
sum; it does not merely pass to a limit of strict finite inequalities.
The nonempty divisor suffices for this strictness. The retained real
zero supplies a specific available label and the optional numerical
floors for S_p. No lower bound on an unknown off-line population is used.

C034c(19), with h=d_2-d_1, already proves
h*d_1*d_2>S_4^3/5, using d_1>S_4/2 and d_2>S_4 as well as the joint
signed difference bound. Hence T=C-h*d_1*d_2 gives (2). In particular
C<0<S_4^3/5 establishes C034c(20) with a strictly stronger scalar
threshold. C034b(1),(4) supply k_j>0 and
W(1,k_1,k_2)=k_1*k_2*T with the stated row and column order. Multiplying
(2) by k_1*k_2 yields (3), without differentiating any inequality.

The argument applies directly at sigma=1 and sigma=2: C034h's sign
domain includes both, and all derivative identities hold on the open
neighborhood (1/2,3). Equation (5), the product envelopes and the cited
dominated-convergence theorem also give continuity of the assembled
integrals there. All limits are measurable. We do not infer endpoint
strictness from interior signs, nor extend the sign to [1/2,3].

This closes only the scalar assembly gap left by C034b/c. It does not
assert pointwise spatial positivity or remove any correction in the
historical representations. ECT application, a fixed-site matrix and
its inverse, entries/residual m, exact weights, TV<=2, the full observation
constraints, signed-height cancellation and actual-Xi realization
remain separate. The inherited source-wide and finite-zero qualifications
remain, and global Sobolev membership is neither needed nor established.

### Conceptual audit1870 — 20 November 2026

**Verdict and scope.** Equations (1)-(7) pass under unchanged SPECIALIZE
assessment1868, separately approved1869. This verifies the previously
unaudited countable specialization, with no mathematical repair,
stronger constant or new hypothesis. C034h/audit1866 is used as the
audited finite-pair input, not reproved. C034b/audit1841 and
C034c/audit1845 supply the normalized derivatives and cubic estimate.
The integration statements cited above are reused with their actual
absolute-integrability hypotheses. This is reproduction of the local
argument, not a claim of progress beyond those inputs or originality.

**Uniform absolute member bounds.** Apply C032n(8) with imaginary
part bounded by 1/2, width in I=[1/2,3], and spatial orders 0,2,4.
The constants are independent of the label and real spatial center.
For 0<=x<=1 and gamma>14, both real distances to the centers are at
least gamma-1. Thus its Gaussian bound gives exactly the displayed
summable bounds for U_(rho,k). On the dyadic block
2^n<gamma<=2^(n+1), the counting hypothesis bounds the number of
labels by O((n+1)2^n); this proves exponential summability and the
reciprocal-square summability used in C032n(9), with multiplicities.

Every h_rho is even, including when delta is nonzero. Consequently
h_rho'(0)=h_rho'''(0)=0, and Taylor's integral remainder proves both
quadratic origin bounds in (5) before summation. For j=1,2 and t=x^2,

    x^2 Q_j(x)=4j(3t+j)/(t+j)^2<=12j,  0<x<=1,
    Q_j(x)<=12j/x^4,                 x>=1.

For the first inequality use 3t+j<=3(t+j) and t+j>=1; for the
second use t(3t+j)<=3(t+j)^2. A concrete choice of the majorant in
(5), with the same Gaussian constant c enlarged if necessary, is

    M_(rho,j)(x)=6j*(U_(rho,2)+U_(rho,4)),          0<x<=1,
    M_(rho,j)(x)=12jc*(V_rho(x)+V_rho(0))/x^4,     x>1.

Its summed integral is finite: the origin part is summable as just
checked, the constant tail contributes 4jc*sum_rho V_rho(0), and
the remaining tail is at most 12jc*int_1^infinity P(x)/x^2 dx,
where P=sum_rho V_rho is precisely C032n(9)'s nonnegative majorant.
Continuity in width makes these suprema measurable: take the supremum
over a countable dense subset of I. Thus
sum_rho int sup_sigma (|A_rho|+|B_rho|)Q_j<infinity,
which is stronger than a uniform bound on signed or absolute totals
at separate widths. No nonintegrable origin constant is split out.

**Labels, derivatives and product measure.** The divisor is a
countable labeled multiset; its counting measure and spatial Lebesgue
measure are sigma-finite. All member integrands and the preceding
majorants are measurable. Normal convergence of the complex Gaussian
series and its derivatives permits taking real parts termwise.
Conjugation invariance makes the total real on the real axis, so
sum h_rho=p_sigma and sum h_rho''=p_sigma''. If two conjugate labels
have the same real h, both remain in these sums, just as both were
present in the original complex divisor. Real labels retain their
two translates with weights 1/2; no extra pairing factor occurs.

The two subtracted sums therefore identify (6) with C034b(6) and
C034c(16),(21). The latter's differentiated identity uses
partial_sigma(p_sigma(x)-p_sigma(0))=p_sigma''(x)-p_sigma''(0);
it does not discard the differentiated origin term. Write
m_(rho,j)=int M_(rho,j) and m_j=sum_rho m_(rho,j)<infinity.
Each absolute member integral for D_j or E_j is at most m_(rho,j).
For the four terms of P expanded on the two independent spatial
variables, their summed absolute integrals after the factor1/2
are at most 2*m_1*m_2. The corresponding half-sum of the four
products of M is a width-independent pointwise dominator with that
finite integral. It verifies absolute Fubini on the full counting-square
and spatial-square product, before any factoring or rearrangement.

In the resulting ordered sum, the first two terms each sum to d_1 e_2
and the last two each sum to d_2 e_1. This checks the factor1/2 and
the sign in (7). In particular the diagonal is present once and an
unequal ordered pair has its separate reverse; neither is deleted.
There is no normalization by a probability mass or number of labels.

**Strictness, orientation and endpoints.** The same dyadic argument
gives 0<S_4,S_8<infinity, with the retained r<15 giving the stated
strict lower floors. Each independently chosen pair meets C034h's
gamma>14, strict displacement strip and through100 conditions.
Its hypothesis explicitly permits coincident and nonconjugate pairs.
For fixed sigma in [1,2], q_(rho,tau)>0 and
q_(rho,tau)<=|P_(rho,tau)|+25*s_(rho,tau). Thus its sum is finite,
and the single retained diagonal q_(rho_0,rho_0)>0 prevents loss of
strictness in the infinite limit. Since sum s=2*S_4*S_8, (1) follows
with exactly the coefficient50, without a positive-profile premise.

C034c(19) gives (d_2-d_1)d_1d_2>S_4^3/5. Subtracting this from
C gives (2). Expansion of the determinant with rows of width
derivative order 0,1,2 and columns (1,k_1,k_2) gives

    k_1'k_2''-k_2'k_1''
      =k_1*k_2*(-d_1*(d_2^2-e_2)+d_2*(d_1^2-e_1))
      =k_1*k_2*(d_1*d_2*(d_1-d_2)+C).

This verifies (3)'s orientation, using positivity of the real
exponentials. Both endpoints meet C034h's closed sign domain directly;
the derivative identities are valid on the larger open neighborhood
(1/2,3). The member and product majorants also justify continuity
by dominated convergence. Endpoint strictness is not inferred by
taking a limit of interior strict signs; the diagonal-slack argument
applies at each endpoint itself. No sign is claimed outside [1,2].

All inherited source-wide, finite-zero and probability qualifications
remain. In particular the two fixed-v1 sources, separate fixed-j=0,1
errors, heat positivity, reciprocal-square tail, zero drift/killing
and half-variance are not replaced by an assumption of spatial
positivity. No global Sobolev assertion is used. ECT, fixed-site
solvability, conditioning, exact weights/TV, full observations,
signed height/cancellation and Xi realization remain unproved here.
The direct inputs in the existing DAG suffice and are unchanged;
C034g is unused. No mathematical script or numerical mesh is needed
for this audit of absolute convergence and signs.

## Mathlib

Full matching coverage is unchecked and unknown. No Mathlib theorem
is used or asserted absent. The standard absolute-integration and
dominated-convergence inputs have supporting mathematical roles here;
no matching formal theorem for this qualified divisor family, the
complete pair inequality or its final-prefix specialization has been
verified. Conceptual audit1870 validates the informal local proof under
its unchanged qualifications; it supplies no formalization or
independent source-wide validation.
