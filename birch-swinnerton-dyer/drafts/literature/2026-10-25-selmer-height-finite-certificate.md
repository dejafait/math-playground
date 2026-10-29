# Finite Selmer and height certificate — source comparison

TARGET: Assess whether a finite p-Selmer dimension bound and a certified nonzero rational p-adic height minor can certify L118's V_2=0 without assuming finite Sha, identifying the exact finite-precision hypotheses.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped searches compared L001/L002/L003/L118, L019 and ATTEMPTS/002/031; external exact-interface and stronger-result searches located Harvey's explicit ordinary-height precision theorem and Stein--Wuthrich's existing algorithms; primary passages inspected are specified below.
SOURCE_EVIDENCE: Milne, Elliptic Curves, second edition (2021), IV equation (29) p.113 and Theorem 3.1 p.114; Harvey arXiv:0708.3404v1, Theorems 1--3 pp.1--2 and Section 5 pp.11--12; Stein--Wuthrich (2013), Sections 4/4.1 pp.1770--1771 and Theorem 6.1 p.1776; reuse foundations/04 and its Ray Theorem 3.4 coverage for the sufficient implication including CM.
COMPARISON: L001 already supplies the finite rank-bound mechanism and L003 supplies the conditional characteristic-order criterion; Harvey supplies certified point-height precision for p>=5. Only the explicit finite-input composition, independence/full-space check and determinant error propagation warrant specialization; the arithmetic theorems must be imported.
GAP: No certificate composition or implementation has been proved here. The next specialization must show that its sharp torsion-corrected Selmer bound and rational height determinant establish the hypotheses of L003 and the conclusion V_2=0 of L118; this review supplies no p=3 computation contract or successful curve.
REASON: The source comparison replaces unverified Sha/nondegeneracy premises by a proposed finite-input contract with ready supporting theorems, while rejecting an arbitrary smaller minor or an unsharp Selmer bound as adequate evidence.
SCOPE: E/Q, good ordinary p>=5, classical cyclotomic conventions of L118, exact rational points and a rigorous full p-Selmer upper bound; CM is allowed for the sufficient implication via the already checked Ray statement. No finite Sha, full-height nondegeneracy or analytic-order comparison is assumed.
LITERATURE_REASON: Startup coverage was REVIEW_REQUIRED; the changed finite-descent/height-precision interface was essential and was not covered by the ready conditional L003 assessment.
COVERED_TARGET: Specialize L001, L003 and L118 for p>=5 to a finite V_2=0 certificate from a bound dim_Fp Sel_p <= k + dim_Fp E(Q)[p] and a certified nonzero k-by-k ordinary p-adic height determinant on rational points, including determinant error propagation.

## Gap, target and decision test

The main gap remains rational rank versus arbitrary complex analytic order
at least two. The bounded intermediate target is a finite fixed-curve
producer for L118's vanishing second layer. Its downstream use is removal
of the augmentation defect for eligible inputs; uniform production of
points, sharp descent bounds and nonvanishing heights, and comparison with
complex order, remain independent gaps.

Continue with the covered specialization only if finite inputs establish
all its premises, rather than assuming finite Sha or full-space height
nondegeneracy. An unsharp bound, a determinant enclosure containing zero,
or a mismatch of height conventions is an inconclusive certificate.
Failure at that threshold does not refute BSD or prove height degeneracy.
The source coverage is ready for the stated p>=5 specialization, subject
to separate next-turn approval. This literature-only step derives no new
lemma and changes no mathematical script or canonical proof.

## Duplicate and failure checks

Read L001, L002, L003's criterion and its applicability argument, and the
complete audited L118. L001 already explains that a certified rational
lower bound can close its torsion-corrected finite Selmer upper bound.
L003(2) already removes delta under finite p-primary Sha and nonzero
regulator. Reproducing either as a new theorem would be redundant.
The proposed addition is their explicitly checkable input interface with
height precision and L118, not a new height or descent theorem.

Reused [the earlier height comparison](2026-10-25-height-augmentation-defect.md)
and [foundations/04](../../foundations/04-cyclotomic-height-criterion.md).
ATTEMPTS/002 retains the insufficiency of characteristic order plus
control. ATTEMPTS/031 retains the missing ordinary-to-strict localization
implication. L019's statement and first-height model show why a
nondegenerate pairing on a marked rational subspace cannot silently be
treated as control of the full Selmer space or Sha quotient. None of
these stops forbids a sharp finite bound supplied by actual descent.
No cross-notebook theorem is used.

## Primary source evidence

J. S. Milne, *Elliptic Curves*, second edition (2021),
[IV, equation (29), p.113 and Theorem 3.1, p.114](https://www.jmilne.org/math/Books/EC2.pdf#page=118):
read the global/local Kummer diagram, definitions, exact-sequence
argument and finiteness statement. The exact sequence has no Sha
finiteness hypothesis. With n=p it is the source behind L001's rank
bound, including the rational p-torsion correction. Merely computing a
proper subgroup of Sel_p gives no upper bound; local conditions at all
places and coverage of the full Selmer group need certification.

David Harvey, *Efficient computation of p-adic heights*,
[arXiv:0708.3404v1, 24 August 2007](https://arxiv.org/pdf/0708.3404v1),
Theorems 1--3, pp.1--2; Section 2.2, p.4; Section 5, pp.11--12.
Read the complete theorem hypotheses and the precision argument through
Lemma 8 and Proposition 9's statement. Assume an integral Weierstrass
equation, good ordinary p>=5, and M>=2. Set n1=#E(Fp), n2=lcm of
Tamagawa numbers, n=lcm(n1,n2), and M'=M+2v_p(n). Theorem 3 computes
h_p(P) modulo p^M from sigma_p modulo I_(M'+1), where
I_N=(p^N,p^(N-1)t,...,t^N). Theorem 2 requires N>=4 and E2 modulo
p^(N-3) to produce sigma_p modulo I_N; Theorem 1 supplies E2 to
specified precision. The proof accounts for multiplication by n,
division by n^2, sigma substitution and the logarithm on units.
Proposition 9 requires nonsingular reduction at bad primes; Section 5
first multiplies by n2. Its implementation proof was not independently
audited. These are point-height guarantees, not a ready matrix certificate.

William Stein and Christian Wuthrich, *Algorithms for the arithmetic of
elliptic curves using Iwasawa theory*, Math. Comp. 82 (2013), 1757--1792,
[Sections 4/4.1, pp.1770--1771; Theorem 6.1, p.1776](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=14):
inspected polarization, torsion vanishing, ordinary sigma height and
the complete order criterion. The criterion requires finite p-primary
Sha and nondegenerate height; it does not produce either premise.
The standing non-CM restriction is retained when using this source.
Harvey's sigma/d convention and this paper's d/sigma convention must
be matched by an explicit nonzero scalar before use; nonvanishing is
unchanged, but absolute precision must follow the chosen normalization.
Algorithm 11.1 (pp.1783--1784), whose opening hypotheses and rank/regulator
steps were inspected for comparison, uses a different
p-adic L-series route and additionally assumes surjective residual
representation. Those assumptions are not inputs to the present
descent-based proposal. The all-CM sufficient order theorem is reused
from Ray, Theorem 3.4, in foundations/04; Schneider's original proof
remains unread as recorded there.

## Exact proposed finite-input contract and remaining work

The next turn may specialize the sources under the following proposed
contract, with its implications still to be written out and checked:

1. An explicitly verified E/Q with good ordinary p>=5; the classical
   control/cotorsion conventions are foundations/03's. Fix k>=0 exact
   rational points and t=dim_Fp E(Q)[p], with a certificate for t.
2. A rigorous integer upper bound b for the dimension of the **full**
   p-Selmer group satisfying b<=k+t. A bound for a different prime,
   an isogeny-Selmer group without comparison, a lower bound, or a
   conjectural database rank is not interchangeable with this input.
3. For k>0, a square height matrix on precisely those k points, using
   the ordinary cyclotomic height. Point and sum heights used for
   polarization must have certified absolute errors. Handle zero or
   torsion sums explicitly; do not evaluate a nonzero-point formula
   there. Any conversion of normalization must retain precision loss.
4. A proved enclosure D_hat+p^B Z_p for the determinant, with
   v_p(D_hat)<B, so zero is excluded. Entrywise precision alone is
   not a determinant error certificate. The residual algebraic work
   is to give a rigorous propagation rule after an explicitly justified
   integral scaling, including nonintegral heights and division factors.
   The empty k=0 determinant is 1 and needs separate treatment.

The next specialization must use the Kummer sequence to check that this
sharp dimension threshold actually removes the Sha obstruction, and
bilinearity to justify independence and spanning before invoking L003.
It must justify passage from the given point lattice to the rational
space without claiming a saturated integral basis or a numerical formula
for the full regulator. L118 then supplies the already proved relation
between semisimplicity and higher layers. Do not replace these checks
by a height-radical surjection. A proper nonzero minor without the sharp
dimension bound is outside approved sufficient coverage.

The special case allowing nontrivial finite Sha with an unsharp p-Selmer
bound is not covered by this certificate contract. Nor is p=3: a search
located Balakrishnan's *On 3-adic heights on elliptic curves* (JNT 161
(2016), 119--134), but its theorem and precision proof were not inspected.
That is an unread lead, not a justification to extend Harvey's theorem.
No curve, descent implementation, matrix output or precision threshold
has been computed here. The specialization can yield a reusable
conditional certificate; it supplies no new BSD case by itself.

## Search record and Mathlib

External queries were `elliptic curves p adic height regulator rigorous
precision Selmer rank bound finite Tate Shafarevich Stein Wuthrich`,
`p-adic height algorithms certified precision Balakrishnan Besser Muller
elliptic ordinary regulator`, `David Harvey Efficient computation
p-adic heights Theorem precision pdf`, `Selmer group rational points
rank bound Shafarevich finite p descent exact sequence elliptic curves
Milne theorem`, `"Selmer" "p-adic height" "independent points"`, and
`"Selmer" "height pairing" "finite precision"`.
Only the primary passages specified above support this decision.
Unrelated higher-genus results, software examples and unreviewed broad
claims were not imported. Search failure establishes no novelty.

Full matching combined certificate and supporting arithmetic Mathlib
coverage: not checked. Determinant multilinearity and the ultrametric
valuation law suffice for the planned elementary error analysis; that
analysis is reserved for a subsequent approved research step. Reuse the
canonical results instead of re-proving the arithmetic theorems.
