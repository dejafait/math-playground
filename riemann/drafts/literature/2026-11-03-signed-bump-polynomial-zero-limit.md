# Source assessment: logarithmic limit of the exact inverse-kernel polynomial

TARGET: Determine the locally uniform limit on |zeta|<1 of n^(-1)*log(H_n(zeta)/H_n(0)) for L714's exact polynomials along n=12q+3, using the logarithm equal to zero at zeta=0.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 176 searched Euler-operator zero asymptotics, finite-free multiplicative limits, coefficient-ratio limits and exponential profiles; inspected the primary statements and convergence cases below. Scoped local searches found no earlier assessment of this exact limit; the signed-remainder and older absolute-contour/positive-blend stops were checked. This bounded search does not establish novelty.
SOURCE_EVIDENCE: Jalowy--Kabluchko--Marynych arXiv:2504.11593v1 Definition 1.2, Theorem 2.2, Theorem 5.2 and Section 5.2, https://arxiv.org/pdf/2504.11593v1 ; Arizmendi--Fujie--Perales--Ueda arXiv:2408.09337v2 Theorem 1.1, Section 2.4.3, Propositions 7.3/7.9 and their proofs, https://arxiv.org/pdf/2408.09337v2 ; Jalowy--Kabluchko--Marynych arXiv:2509.11248v1 Sections 2.3/4.6/5.2, Theorems 4.9/5.14, https://arxiv.org/html/2509.11248v1 . Page numbers, reading limits and qualifications below.
COMPARISON: The primary profile theorem supplies weak zero convergence and identifies the Cauchy transform for arbitrary growing coefficient arrays with nonpositive roots; fixed operator parameters are unnecessary. L714 supplies the finite object but not its coefficient profile. The remaining specialization must verify that profile, the subsequence/degree normalization and a locally uniform complex logarithm normalized at zero. No inspected source states this particular H_n limit or its outer signed bump rate.
GAP: Establish the exact coefficient profile (or all-diagonal consecutive normalized-coefficient ratios), apply a cited convergence theorem without presupposing its limit measure, and justify the complex logarithm on every closed subdisk. No limiting formula, convergence, boundary value or cancellation estimate is established in this review.
REASON: Essential coverage is ready for a bounded theorem specialization on the unchanged target. Use the profile theorem as the primary route; deriving a new Euler-operator limit theorem is unnecessary. Source mathematics is known; the local coefficient calculation and complex-normalization argument remain for a separate research turn.
LITERATURE_REASON: At turn start L714's new real-root Euler-operator polynomial lacked essential comparison with known root-distribution and logarithmic-limit results. This review completes that source comparison; it does not repeat the ready saddle assessment.
SCOPE: Exactly TARGET for the polynomials defined in L714 with U=121/64 and N=n-1. Do not replace the fixed actual L703 bump, alter the finite family, assume a limiting root measure, or infer a signed R_n rate from this limit alone.

## Preserved nomination and purpose

The nomination below records step 175's scope and discriminating test.
Its demand for a separate source review is discharged by step 176;
its mathematical restrictions remain in force.

Use L714's exact coefficients and identity (9); no new limiting
mathematics is established in this nomination. The real-root proof
places every root strictly above one and specifies the logarithm
unambiguously in the open unit disk. This does not assert convergence
of the sequence of logarithms or any boundary behavior.

The main gap remains actual-Xi all-degree positivity. This target
could give the exponential scale of the exact inverse kernel g_n
on the fixed positive bump through L714's (5), avoiding an assumed
single saddle for the original rational contour. The resolvent
convolution, the final signed bump integral, exceptional/zero
subsequences and comparison with P_n would still require proof.
Other frequencies/comb/tails/moments, angular persistence,
complementary defect, amplitude/full charge, H/support and Xi
realization remain independent.

## Required source comparison and discriminating test

Search the exact coefficient/variable definitions and the terminology
for real-root polynomials produced by products of Euler differential
operators. Compare relevant finite convolution, multiplier and
varying-parameter polynomial-zero results only if their actual
theorem hypotheses fit this array. These are search leads, not
inspected theorems or assertions of coverage. Check local duplicates
and preserve the two older stops and the step-175 inconclusive record.

Retrieve primary theorem hypotheses and essential convergence cases
before larger extracts. In particular distinguish fixed degree,
fixed parameters and real-variable asymptotics from this growing
array and a locally uniform complex logarithm. A numerical root
picture or a collection of subsequential limits is not the requested
limit. Do not infer novelty from a failed search. Full matching
Mathlib coverage is not checked.

Continue only after importing a matching theorem with its exact
specialization or saving EXPLORE/SPECIALIZE coverage for a concrete
limit proof. Abandon that particular theorem route if its parameter
or convergence hypotheses cannot be met. This source review does
not authorize mathematics on the new target in the same turn and
does not prejudge the unresolved outer cancellation. The nomination
does not invalidate the completed step-175 reduction.

## Completed source comparison — step 176, 3 November 2026

### Local inputs and failure comparison

Read L714 in full: exact coefficients, (4), (5), (9) and Section 3 are
the proposed inputs, still unaudited. Reused
`drafts/literature/2026-11-03-signed-bump-remainder-rate.md` for the
outer cancellation boundary. Scoped searches of the dated signed-bump
assessments and relevant records found no existing root-limit theorem
for this object. Read the specific failure records
`ATTEMPTS/2026-11-03-signed-bump-rate-inconclusive.md`,
`ATTEMPTS/2026-11-03-spatial-boundary-absolute-contour-stop.md` and
`ATTEMPTS/2026-11-02-positive-blend-signed-saddle-stop.md`.
They concern unpaid signed cancellation, an absolute horizontal-contour
certificate and different blended weights, respectively. None refutes
this polynomial limit. No zero-free-region, reciprocal-series or parked
arithmetic route is reopened.

### Queries and inspected primary results

Queries included `polynomial zeros products Euler differential operators
asymptotic distribution finite free multiplicative convolution`,
`finite free multiplicative convolution infinitesimal arrays polynomials
zeros limit S transform`, `polynomials binomial coefficients varying
zero distribution differential operators`, and searches for
`Zeros and exponential profiles` and `S-transform in finite free
probability`. Euler/Bernoulli-name hits were irrelevant. Abstracts and
snippets were discovery aids, not theorem evidence.

1. **Preferred profile route.** J. Jalowy, Z. Kabluchko and A. Marynych,
   *Zeros and exponential profiles of polynomials I: Limit distributions,
   finite free convolutions and repeated differentiation*,
   [arXiv:2504.11593v1](https://arxiv.org/pdf/2504.11593v1), 15 April 2025.
   Definition 1.2, PDF p.3, requires nonnegative coefficients, degree
   at most n and a finite pointwise exponential coefficient profile
   on a nonempty interval in [0,1], with limit minus infinity outside
   its closure; endpoint values are not required. Theorem 2.2(a),(b),(e),
   pp.5--6, additionally requires eventually nonpositive real roots.
   It gives weak convergence on the one-sided compactification,
   identifies the Cauchy transform via the inverse of exp(-g'), and
   specifies masses at zero and infinity. It accepts arbitrary arrays.
   Read the compactification/Bernoulli argument in Section 5.2,
   pp.25--26, Theorem 5.2's subsequence-uniqueness proof, pp.24--25,
   and Theorem 2.2's normalization proof, pp.26--27. These provide
   full convergence. Remark 5.4, p.26, warns that weak convergence
   does not control an unbounded unnormalized logarithmic potential.

2. **Coefficient-ratio alternative.** O. Arizmendi, K. Fujie, D. Perales
   and Y. Ueda, *S-transform in finite free probability*,
   [arXiv:2408.09337v2](https://arxiv.org/pdf/2408.09337v2), 5 February 2025.
   Theorem 1.1, pp.2--3, concerns degree-d polynomials with nonnegative
   roots. The finite S-transform is e-tilde_(k-1)/e-tilde_k, using
   binomially normalized elementary coefficients and the index -k/d.
   Convergence is required along EVERY k/d tending to interior t,
   within the domain determined by the limit's atom at zero.
   Section 7.2, Proposition 7.3 and proof, pp.26--27, handles compact
   support containing zero. Read converse Proposition 7.9 and proof,
   pp.28--29: positive finite diagonal limits on (-1+t_0,0),
   0<=t_0<1, produce the measure, so it need not be assumed first.
   Its last proof paragraph prints t_0 in an interval where the
   hypothesis uses 1-t_0; this apparent typo is not silently repaired
   or used. Prefer route 1. The 2026 journal landing page was located
   (Adv. Math. 489, 110803, DOI 10.1016/j.aim.2026.110803), but its
   proof was not read and is not substituted for the versioned source.

3. **Nearby explicit families.** The same profile authors' *Zeros and
   exponential profiles of polynomials II: Examples*,
   [arXiv:2509.11248v1](https://arxiv.org/html/2509.11248v1),
   14 September 2025, Section 4.6, Theorem 4.9, fixes finite parameter
   vectors for hypergeometric limits. Section 5.2 defines a fixed
   finite operator word and an exponential flow on monomials for
   Theorem 5.14. Read these definitions/statements and Section 2.3's
   normalized-potential discussion, not their proofs. Neither supplies
   a verified representation of L714's growing word. They are not
   direct imports here; Part I's profile theorem avoids the mismatch.
   Van Assche--Fano--Ortolani (SIAM J. Math. Anal. 18(6), 1987,
   1597--1615) remains an unread historical lead from Part I Section 2.2,
   not a relied-upon theorem.

### Authorized specialization and discriminating test

The primary candidate is H_n(-t)/H_n(0). L714's stated coefficient
signs and reflected root location supply the sign/root hypotheses
of route 1; the coefficient-profile hypothesis remains unpaid.
The next attempt should verify that profile from the exact coefficients,
including factorial/product estimates, the degree N=n-1 versus n
normalization and the congruence subsequence. A fixed-parameter
operator theorem is unnecessary. The factorial tool can reuse
[DLMF 5.11.1](https://dlmf.nist.gov/5.11#E1), already covered by the
unchanged signed-remainder assessment; no special-function asymptotic
for this polynomial has been imported. Route 2 would instead need the
correctly normalized reversed polynomial and every-diagonal ratio
convergence; it is optional, not an additional task.

After the cited weak-convergence theorem, explicitly justify the
complex logarithm, zero at zeta=0, uniformly on each |zeta|<=r<1.
Use L714's root location to check the normalized log kernel's
boundedness/continuity, including roots escaping to infinity, or
justify the corresponding compact reciprocal-root argument.
A real-only potential limit, convergence off the real axis alone
or an unbounded log|rho| integral does not settle the target.
No analytic extension of the bump is needed for this polynomial step.

Continue only with the coefficient hypothesis and one identified
analytic limit on the whole open unit disk. Stop that theorem
application if a required hypothesis cannot be verified; record which
one failed rather than substitute subsequences or numerical roots.
A successful specialization should be REPRODUCTION, cite the general
theorem and put its array verification/complex-log upgrade in a
canonical lemma. Reproving general profile/zero convergence is unnecessary.

This review derives no profile, root law, complex limit or signed rate.
Full matching Mathlib coverage is not checked. L713/L714 remain
unaudited, and all outer cancellation and realization gaps above remain.
