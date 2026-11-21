# Corollary C030x: direct reciprocal-Xi finite-reference variation obstruction

## Hypotheses

Let c_0=xi(1/2)>0 and h(z)=xi(1/2+sqrt(z))/c_0, with the entire
normalization in C466a. In particular h(0)=1. Fix one finite list of
C030w rates q_1,...,q_n: conjugate pairs a_l +/- i b_l with a_l>0,
followed by any specified copies of a positive real r. Repeats and
zero phases are allowed. The list and n do not depend on s. Set

    P(s)=prod_(j=1)^n (1+s/q_j),   F(s)=P(s)/h(s).

Suppose a real finite signed Borel measure nu on [0,infinity) satisfies

    F(s)=integral_[0,infinity) exp(-s*u) d(delta_0+nu)(u),
                                                    every real s>0. (H)

The displayed identity includes its asserted finiteness wherever it is
used. Only sufficiently small and sufficiently large positive s are
needed for the conclusion. There is no positivity assumption on nu.

## Conclusion

The two transform limits force

    nu({0})=-1,   nu([0,infinity))=0,
    nu((0,infinity))=1,   ||nu||_TV>=2.                       (1)

Consequently no measure satisfying (H) has ||nu||_TV<1. This rejects
the direct global identification with delta_0 plus a small signed
correction for any fixed finite C030w rate list.

If such a measure were supported on C030w's compact interval
[0,t-s_*], its actual weighted budget would satisfy epsilon>=2,
where the criterion requires epsilon<1. No global version of that
compact criterion is asserted. The bound is necessary, not an
existence assertion or a claim that equality in ||nu||_TV>=2 occurs.

This is REPRODUCTION under the unchanged SPECIALIZE assessment1246,
source review1247, completed in attempt1248. It is an elementary
application of the inspected growth and signed-convergence results,
not a result claimed beyond those sources. Independent audit1249 passes
with the hypotheses and scope unchanged; its checks are recorded below.

## Proof

### Imported analytic input and the fixed polynomial

Reuse only C466a's positive-real expansion (1), not its density or PF
assertions. Its primary source is S. Sra, *On some positivity properties
of the Riemann Xi function*,
[arXiv2611.02944v1, 2 November 2026](https://arxiv.org/html/2611.02944v1),
Appendix B.4, proof of Lemma 2.4, (B.5); the more precise expansion
appears in Proposition C.25, (C.64), of that arXiv version. The Hub
version used in C466a has a different proposition number. These give

    B(s)=log h(s)=(1/4)*sqrt(s)*log(s)+O(sqrt(s)), s->infinity. (2)

This is the real logarithm for sufficiently large positive s. The
completion and Stirling inputs are
[NIST DLMF 25.4.4](https://dlmf.nist.gov/25.4#E4) and
[5.11.1](https://dlmf.nist.gov/5.11#E1), with the positive-real
remainder case in Section 5.11(ii), as inspected in source review1247.
There is no need to rederive Stirling or the source's saddle estimate.

For every s>=0 a pair contributes

    (1+s/(a+i*b))*(1+s/(a-i*b))
                  =((s+a)^2+b^2)/(a^2+b^2)>0,

and each real rate contributes 1+s/r>0. Thus P(s)>0, P(0)=1,
and its leading coefficient is 1/R, where R=prod_j q_j>0. Since
the polynomial and n are fixed,

    P(s)=s^n/R*(1+O(1/s)),
    log P(s)=n*log s-log R+O(1/s), s->infinity.             (3)

Subtracting (2) from (3) yields

    log F(s)/(sqrt(s)*log s) -> -1/4.

Indeed the O(sqrt(s)) term divided by this denominator is O(1/log s),
and n*log s divided by it is n/sqrt(s)->0. The quotient F is
positive eventually, so this proves

    lim_(s->infinity) F(s)=0.                              (4)

At the other endpoint, h is continuous and h(0)=1; hence it is nonzero
on a sufficiently small real neighborhood of zero. Together with
P(0)=1, this proves

    lim_(s->0+) F(s)=1.                                    (5)

These limits use neither the density construction nor a zero-location
hypothesis. In particular they introduce no assertion about analytic
continuation of 1/h across other points.

### Signed convergence, with the origin atom retained

Import A. Rainer, *Real Analysis*, Vienna lecture notes for the Spring
2014/2016 courses, author-hosted 104-page version inspected 2026-11-17,
[Theorem 3.22, printed p24; Theorem 5.1 and Section 5.1, pp53-54](https://www.mat.univie.ac.at/~armin/lect/real_analysis.pdf).
The former is dominated convergence on a positive measure space.
The latter supplies finite total variation, finite positive Jordan
parts nu^+,nu^-, and signed integration as their difference. We apply
dominated convergence separately to these two finite positive measures;
we do not reprove the imported theorem or assume nu is positive.

For any sequence s_k>0 tending to infinity, u->exp(-s_k*u) is Borel
measurable on [0,infinity), bounded in absolute value by 1, and
converges pointwise to 1_{ {0} }(u). The constant 1 is integrable
against both Jordan parts since nu is finite. Therefore

    lim_(s->infinity) integral exp(-s*u)dnu(u)=nu({0}).     (6)

Every such sequence has this limit, proving the stated real-parameter
limit, without a monotonicity assumption on nu. The delta_0 term in
(H) is exactly 1 for every s>0. Equations (4) and (6) give

    0=1+nu({0}),

so nu({0})=-1. For any positive sequence tending to zero the same
dominator applies, now with pointwise limit 1 at every finite u>=0.
Thus (5) and (H) give

    1=1+nu([0,infinity)),

so the total mass of nu is zero and its mass on (0,infinity) is 1.

Total variation on a singleton is the absolute value of its mass,
and on any measurable set it dominates the absolute value of its
mass, by the cited Jordan/variation theorem. Additivity on the disjoint
partition {0}, (0,infinity) therefore gives

    ||nu||_TV=|nu|({0})+|nu|((0,infinity))
             >=|-1|+|1|=2.

This proves (1). The weaker lower bound 1 already follows from the
origin atom and already contradicts the required strict unit budget;
the small-s limit supplies the stronger bound 2.

### Conditional convolution interface and the actual compact weight

For clarity, (H) is a necessary transform identity if one proposes the
global convolution theta_1=f_b*(delta_0+nu), with f_b as in C030w
and theta_1 the mass-one density whose transform is h^(-1) in C466a.
This paragraph explains that interface conditionally; the density
theorem is not a premise of the preceding limit/atom argument.

For Re(q)>0, e_q(u)=q*exp(-q*u) on u>0 is absolutely integrable,
with L1 norm |q|/Re(q). Its Laplace transform for real s>0 is
q/(q+s). Finite convolution of these kernels is L1; absolute
integrability of the multiple integral follows from the product of
their L1 norms. The same check for convolution against
mu=delta_0+nu is bounded by this product times ||mu||_TV<infinity.
All variables are nonnegative, so inserting exp(-s*sum u_j) only
reduces that absolute-integral bound. Rainer Theorem 3.27(1)-(3),
printed p26 of the same notes (Tonelli/Fubini for sigma-finite positive
measures and absolutely integrable complex functions), therefore
applies to Lebesgue measure and each Jordan part of mu. It gives

    Laplace(f_b)(s)=prod_j q_j/(q_j+s)=1/P(s),
    Laplace(f_b*mu)(s)=Laplace(f_b)(s)*Laplace(mu)(s).

Neither q_j nor q_j+s vanishes for real s>0, because Re(q_j)>0.
Division consequently yields (H) from the proposed global equality.
This checks complex kernels and signed convolution, without treating
the individual kernels as positive measures. The normalized density
here must be theta_1, not Theta=theta_1/c_0.

Finally, if nu also has C030w's support [0,t-s_*], that criterion's
weight is

    B_t(u)^2=exp(q_max*u+(37/2)*M*(t^2-(t-u)^2)),
    q_max=max_j Re(q_j)>0,   M=sum_l b_l^2>=0.

For 0<=u<=t-s_*<=t, t^2-(t-u)^2=u*(2t-u)>=0, so B_t(u)^2>=1.
Hence its unchanged, compact-domain budget obeys

    epsilon=integral_[0,t-s_*] B_t(u)^2 d|nu|(u)
               >=||nu||_TV>=2>1.

We do not evaluate this formula beyond its compact domain, change its
degree/phase hypotheses, or assert any global determinant criterion.
If nu is not compactly supported there, C030w is not applicable in
the first place; the unweighted obstruction (1) still holds.

### Scope of the stop

This stops exactly the global equality to one fixed finite reference
with a correction of variation less than one. It does not prove that
no finite signed representation exists with a larger norm, or refute
a local equality of functions or finite jets near a chosen positive
time. A local equality does not imply the global Laplace identity
(H). Infinite reference factors, moving lists, and independently paid
local representations require separate analysis. The source's infinite
complement is not removed by this argument.

No theta signing, graph realization, global PF property or all-degree
L030-L032/C032a algebraic-square positivity follows. RH remains open
in this notebook. There is no candidate solution or numerical evidence
in this calculation.

### Independent audit1249, 17 November 2026

The unchanged SPECIALIZE assessment1246/review1247 covers this audit.
The complete proof above was replayed, using only the normalization and
positive-real expansion in C466a and the finite-rate conventions and
compact weight in C030w. No new density theorem or global PF assertion
is imported. No mathematical defect was found.

The analytic check retains the fixed-list quantifier: R is positive
by conjugate pairing and positive real rates, and n is constant as
s tends to infinity. Thus log P(s)=O(log s), whereas
log h(s)/(sqrt(s)*log s) tends to 1/4. Eventual positivity permits the
real logarithm and forces F(s) to zero. At zero, continuity and h(0)=1
give F(s) tending to one on a zero-free neighborhood. Neither check
needs a global zero-free assertion about h. Repeated rates, zero
phases and absence of r entries do not change these conclusions.

For each endpoint and every approaching positive sequence, the
integrands are measurable and dominated by 1 against each finite
Jordan part. Their limits are respectively the indicator of {0} and
the constant 1. Keeping the separate delta_0 contribution gives
nu({0})=-1 and nu([0,infinity))=0. Variation is additive on the
disjoint partition {0},(0,infinity), so the separate absolute masses
force the bound 2. There is no positivity assumption on the second
restriction, no cancellation inside total variation, and no claim
that a measure attaining the bound exists.

The conditional convolution check uses the product of the finite
L1 norms |q_j|/Re(q_j), multiplied by the finite variation of
delta_0+nu. The Laplace factor has modulus at most one for positive
real s, so the cited signed Fubini application is valid even for
complex rates. All q_j+s are nonzero, justifying division by the
finite-reference transform. This interface remains conditional on
the stated global equality; it is not needed for the endpoint proof.

Finally, on exactly C030w's support, u(2t-u)>=0 and q_max*u>=0;
therefore B_t(u)^2>=1 and epsilon>=2. The degenerate support s_*=t
does not evade the argument: a measure on {0} cannot satisfy both
forced mass identities. No weight outside the compact domain, moving
rate list, local-jet identity or all-degree positivity is inferred.
This first independent audit validates the existing qualified stop;
it is local verification, not new mathematics beyond the cited inputs.
The direct global small-correction ansatz remains parked.

## Mathlib

Full matching coverage for this exact reciprocal-Xi/finite-reference
statement is not checked. The imported ingredients are the precise
growth and measure theorems cited above; no matching Mathlib theorem
or absence of such a theorem is claimed. Formalization and unrelated
PF theorems are not premises of this source application.
