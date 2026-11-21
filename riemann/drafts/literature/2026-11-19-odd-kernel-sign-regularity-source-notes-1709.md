# Odd-kernel sign-regularity source review1709

19 November 2026. Literature only; no determinant, new kernel identity,
counterexample, lemma or mathematical script was produced.

## Local scope and duplicate screening

Read C032m's hypotheses, definitions and conclusions; C032n's full
evolution statement and source scope; C032q's hypotheses and cone
alternative; C032l/o's hypotheses, conclusions and cited input scopes.
Reused coefficient-span review1531/source-notes1532 and read
ATTEMPTS/2026-11-18-odd-kernel-width-recursion-inconclusive-1534.md.
Targeted searches in these files for total positivity, sign regularity,
Chebyshev systems and ordered minors found no matching theorem.
This is a scoped duplicate check, not a claim about the entire archive.

C032m defines the complete actual-divisor kernel on widths [1,2];
C032n gives regularity in a positive-width neighborhood and a variable
coefficient evolution, not scalar-span closure. C032l excludes finite
signed mixtures under its source qualifications. C032o stops the direct
compact-transform interface. Neither stop addresses the proposed minor.
Gamma certification remains parked1708; this review does not reopen it.

## Discovery record

Queries included the exact strings `"exp(-E" "sinh(O" kernel total
positivity` and `"Some positivity properties of Riemann Xi under
smoothing" "total"`; also Gaussian strict total positivity/composition,
complex shifts, entrywise preservers, multivariate transforms, and
Chebyshev orthogonality/sign changes. No matching theorem for the exact
nonlinear actual-divisor family was located. Failed exact searches
establish no novelty. Search snippets and third-party mirrors were leads
only; the following primary texts supplied the comparison.

## Primary sources actually inspected

1. A. Belton, D. Guillot, A. Khare and M. Putinar, *Totally positive
   kernels, Polya frequency functions, and their transforms*,
   [arXiv:2006.16213v5](https://arxiv.org/pdf/2006.16213v5),
   dated 27 November 2021, deposited 7 December 2021.
   Read Section6.1, Notation6.1/Proposition6.2 and its complete
   Cauchy--Binet proof, printed pp24-25; Theorem4.1 and its complete
   order-two proof, pp14-16.
   For kappa>0 the Gaussian exp(-kappa*(x-y)^2) is TP on real ordered
   arguments. Proposition6.2 starts with a TN_p kernel on A times B,
   A,B subsets of R, and ordered samples of lengths n,N>=p. Gaussian
   multiplication on both sides gives TN_p and TP_min(p,r), where r is
   the sampled rank. Strictness uses nonzero minors; entry positivity
   alone is insufficient. Theorem4.1's order-two entrywise preservers
   are exactly c*t^alpha, c,alpha>0. Its proof tests arbitrary TP
   matrices, takes boundary limits, and obtains a multiplicative
   functional equation. These are universal preservation statements,
   not tests for one particular transformed kernel.

2. S. S. Damase and A. Khare, *Multivariate transforms of total
   positivity*, [arXiv:2411.03391v2 PDF](https://arxiv.org/pdf/2411.03391v2),
   PDF dated 2 December 2024, arXiv header 29 November 2024.
   Read Definitions1.1-1.2, Theorem1.6(2), printed pp2-4;
   Proposition3.3 and Theorem3.2 with their proofs, pp12-14;
   order-two sufficiency in the proof of Theorem1.6, p18.
   For ordered X,Y and input orders k_j, output order l, put
   N=min(|X|,|Y|,l). For N=2, universal transforms of TP kernel tuples
   are c*product(t_j^alpha_j), with c>0, alpha_j>=0, not all zero,
   and alpha_j=0 if k_j<2. The domain is the positive orthant.
   Necessity uses monotonicity, continuity, Vandermonde embeddings
   and TN approximation; sufficiency multiplies positive two-by-two
   inequalities. These hypotheses do not include signed or complex
   kernels. The HTML rendition was also inspected, but displays a
   different document date; the fixed PDF is the cited version.
   A separate MRR announcement PDF returned HTTP403; it is not used.

3. O. R. Musin, *Chebyshev systems and zeros of a function on a convex
   curve*, [arXiv:0903.1908v2](https://arxiv.org/pdf/0903.1908v2),
   27 April 2009. Read Section2's definitions, Theorem1 and complete
   proof, printed pp2-4. For continuous functions on an interval,
   an n-dimensional Chebyshev system means each nontrivial linear
   combination has at most n-1 distinct zeros. A continuous function
   orthogonal to it with a continuous constant-sign weight has at
   least n sign changes if the weighted function is not identically
   zero. The proof uses a system element with prescribed sign changes
   and a nonzero constant-sign integral. Only the interval case,
   integrable continuous densities and weight 1 are prospective here;
   endpoint atoms and arbitrary finite signed measures are not covered
   by this citation. The system hypothesis still needs verification.

Screenshots were requested for selected statements; this interface
returned no inspectable image content, and one timed out. The textual
theorem statements and proof passages above were inspected; no claim
of visual verification is made. No inaccessible source is essential
to the bounded target below.

## Comparison with the exact target

The existing definitions are retained without rederivation:

    k_sigma(y)=Im(kappa_(i*y)(sigma)),
    D(s,t)=k_s(1/8)*k_t(1/4)-k_s(1/4)*k_t(1/8),
    1<=s<t<=2.

The Gaussian source fixes its Gaussian parameter while ordering two
real spatial variables. Our ordered variable is width; the divisor
locations gamma-i*delta need not be real, even before the spatial
quotient, primitives and nonlinear operations. No TN input kernel on
these ordered variables is established. Neither Gaussian convolution
nor a positive multiplicity in the divisor verifies the assumptions
of Proposition6.2. No order-preserving change of coordinates or
admissible real composition representing this full kernel is known.

The entrywise classifications exclude a universal exp/sinh preservation
shortcut. They neither disprove this particular minor nor classify
strict sign regularity with possibly signed entries. Even a future
positive factorization would need its own hypotheses: two factors
depending jointly on width and y cannot be treated as positive row
or column rescalings without proof. Taking an imaginary part is
outside the positive real input assumptions. Do not use positive
semidefinite Schur-product theorems as total-positivity theorems.

The useful possible continuation is narrower than a completeness claim.
A strict common minor sign could support a two-function Chebyshev
structure, with the determinant/zero-count implication checked in a
later mathematical turn. Musin's theorem would then constrain
continuous annihilator densities with fewer than two sign changes.
This is a possible continuum restriction beyond finite-family
independence. No such restriction is established in this source turn.
Extension to arbitrary signed measures and any use in excluding all
mass-one annihilators require additional arguments. Two functions do
not supply constant membership in C032q's full scalar span, all-order
regularity, positive output, exponential moments or Xi realization.

## Decision and bounded continuation

Reject automatic Gaussian/nonlinear preservation as an import route;
no matching kernel theorem was found. Permit one kernel-specific
EXPLORE attempt at the original minor, after separate approval of
the new continuation assessment. Seek a proof covering every ordered
pair including endpoints and arbitrarily close widths, or rigorous
evidence refuting the common strict sign. A finite grid or a truncated
divisor without a certified remainder does not decide it. A zero at
one strictly ordered pair refutes strictness; a diagonal zero does not.
Failure of an attempted estimate is only inconclusive.

Continue after that test only with a verified sign plus a concrete
Chebyshev application, or an informative obstruction changing the route.
If neither is achieved, preserve partial work and reassess; do not
repeat grids, relabel the old recurrence, or infer all-order positivity.
This is development of an intermediate structural diagnostic, not a
source-supported creative mechanism closing the central Xi sign gap.
Full matching Mathlib coverage remains unchecked and unknown.
