# Cubic benchmark joint-sign moment obstruction — completed source comparison

TARGET: Assess source coverage for a finite-atomic moment obstruction to deducing Delta>0 and mathcal B<0 from L388/L393/L405/L406/L409 alone.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 120 searched Richter/Rogosinski finite measurable moments, noncompact Tchakaloff cubature, support-constrained generalized Chebyshev bounds and mixed-moment quadrant obstructions; targeted local searches found no completed duplicate of this five-constraint target. No exact feasibility or impossibility theorem was established by the bounded search; no novelty is inferred.
SOURCE_EVIDENCE: Bayer–Teichmann, Proc. AMS 134 (2006), 3035–3040, arXiv:math/0502473v2 (2005-05-04), Theorem 1, Corollaries 1–2 and Remarks 1–2, manuscript pp. 2–4; di Dio–Kummer, Math. Ann. 380 (2021), 267–291, Theorem 2.2 and surrounding definitions; Bertsimas–Popescu, SIAM J. Optim. 15 (2005), 780–804, Section 2/Theorems 2.1–2.2 and Theorems 4.1/4.3 with proof qualifications; canonical statement and envelope ranges in L388/L393/L405/L406/L409.
COMPARISON: The measurable-function atomic replacement theorem covers a fixed six-coordinate moment vector and preserves the allowed support, conditional on a feasible measure; it supplies neither this exact feasible family nor a joint-sign implication. Compact SDP and strong-duality claims have additional hypotheses not supplied here.
GAP: Construct or rule out an ell-dependent law satisfying the exact four leading constants, the absolute third-moment envelope and the forbidden-quadrant support condition; positivity of the constants and atomic replacement do not decide feasibility. The actual clipped statistic remains independently unresolved.
REASON: Essential source coverage is sufficient for one later bounded scalar-moment feasibility attempt. Import atomic replacement by citation; derive only feasibility or an obstruction in the separate mathematical turn, retaining all five constraints and qualifications.
LITERATURE_REASON: This changed support-constrained finite-moment question was outside the prior signed-cubic and clipping scopes; the newly inspected measurable-map theorem and noncompact/duality qualifications fill that essential comparison.
SCOPE: Probability laws on real pairs (D,B), ell tending to infinity, only the five scalar constraints displayed below, at most six atoms with positions and weights allowed to depend on ell; no actual jets, phase independence, physical realization, all consequences of the input lemmas, clipping theorem or RH claim.
COVERED_TARGET: Test feasibility of a probability-law family on at most six real atoms satisfying all five L388/L393/L405/L406/L409 scalar constraints and no mass where D>0 and B<0.

## Original proposed scope, preserved from step 119

The proposal below records the scope before this source comparison; its
pending-review language is historical. The completed decision and bounded
continuation are recorded above and after it.

This is a continuation proposal, not an approved calculation or a
completed literature assessment. Do not reopen the unchanged step-99
clipped-asymptotic search without a specific new source or mechanism.

The proposed bounded mathematical test is whether a family of probability
laws with finite support on real pairs (D,B), indexed by ell tending to
infinity, can meet all of the following while having no mass where
D>0 and B<0:

    E D = -a ell + o(ell),
    E D^2 = b ell^4 + o(ell^4),
    E(DB) = beta ell^2 + o(ell^2),
    E(DB^2) = kappa ell^4 + o(ell^4),
    E |B|^3 = O(ell^(9/4)).

Here a,b,kappa,beta are the exact fixed positive constants in L388,
L393, L405 and L409 respectively. The B envelope is the consequence
of L406's pointwise bound by sqrt(U) and its stated power-three
integral. The next comparison must inspect the precise canonical
statements and check these normalizations; this proposal does not
silently strengthen them or assert the model exists. The atom count
should be fixed independently of ell if the source comparison supports
that bounded target. If a sharper established envelope is essential
to the intended implication, identify it explicitly before approval.

Plausible downstream use: decide whether these scalar moment benchmarks
alone can force the joint sign required for a positive negative-B
clipped weight. An admissible law without that joint sign would stop
that inference and identify the need for additional sign-sensitive or
physical information. It would not model the actual zeta jets, refute
the actual clipped mean, or preclude a theorem using the exact physical
identities. These identities are outside this proposed moment-only
implication and must not be claimed satisfied by the law.

Continue to a later mathematical turn only after exact-statement,
standard finite-moment/support terminology, stronger-result and
obstruction searches support IMPORT, SPECIALIZE or EXPLORE. Import an
applicable standard result rather than reprove it. Test feasibility with
all five displayed constraints; a law matching only the signs or fewer
scales would not settle this target. If those constraints already force
the forbidden sign, give the precise known implication instead. Neither
alternative has been derived in step 119.

Essential inputs: L388, L393, L405, L406 and audited L409; reuse their
source assessments within their original scopes. Preserve L394/L399/L400
and step-99 stop evidence. Unresolved independently: actual clipping,
regulator scale, total L367 margin/remainder, common-zero upper counts
and global mixed positivity. No RH, phase independence or actual-function
realization of an abstract law is assumed. Matching Mathlib coverage
for the proposed finite-moment question has not been checked.

## Completed comparison — 2026-10-14, step 120

This is a LITERATURE / NOVELTY_UNCHECKED step. ADVANCE records usable
source coverage, not a constructed law, a new sign theorem, a reproof of
atomic replacement or progress beyond the inspected literature. No lemma,
mathematical script or certificate was written. No essential source for
this bounded scalar-only test remains inaccessible.

### Exact local normalizations

Use the notation D for the abstract analogue of **normalized Delta**, not
for L388's unnormalized physical discriminant. B analogizes the exact
Bcal of L405. For the actual comparison, expectation means the sharp
average H^(-1) integral_[H,2H] and ell=log H. The inspected ranges were
L388 Hypotheses/Conclusion; L393 Hypotheses/Conclusion; L405
Hypotheses/Conclusion; L406 (1), (6)–(7) and its full-response audit
passage; L409 Hypotheses/Conclusion. The ready actual-moment source
assessments remain adequate for those unchanged statements; no new
zeta-moment search or reproof is needed.

The exact fixed constants for the proposed scalar test are

    c=1/(4pi), S=zeta(5)zeta(3)^2/zeta(6),
    a=S/(240pi^2),
    b=c^4 * 263 Psi/(1425600 zeta(2)),
    kappa=233 c^4 Psi/(4989600 zeta(2)),
    beta=(17 c^3/20160)
          sum_(m,n,k>=1) (mn)^(-2) k^(-3) A_(mn/gcd(mn,k)),
    A_u=u^(-2) sum_(j=1)^u gcd(j,u),
    Psi=sum_(m,n>=1) tau(m)tau(n)(mn)^(-5/2)
        product_(p^e || (m/g)(n/g)) [1+e(p-1)/(p+1)]
        /sqrt((m/g)(n/g)), g=gcd(m,n).

These are direct extractions, with the L393 square coefficient renamed
b to avoid confusing its local name beta with L409's cubic beta. The
canonical lemmas establish finiteness and strict positivity. Preserve
the constants themselves, not only their signs. For every sufficiently
large ell the proposed law must have finite absolute expectations and
satisfy

    E D       = -a ell + o(ell),
    E D^2     =  b ell^4 + o(ell^4),
    E(DB)     =  beta ell^2 + o(ell^2),
    E(DB^2)   =  kappa ell^4 + o(ell^4),
    E |B|^3   <= C ell^(9/4),

with one ell-independent finite C and support in

    K={(D,B): D<=0 or B>=0}.

All axes belong to K. The fifth constraint has no specified leading
constant: L406 supplies its power via the already proved
|Bcal|<=C sqrt(U) and average U^(3/2)=O(ell^(9/4)). No smaller
third-moment exponent was found in these canonical passages.
L406 also retains |Delta|<=CU and exact physical jet identities.
Those extra relationships are outside the **five selected scalar
constraints**. Thus a successful abstract model would refute only
an inference from that selected information; it would not reproduce
every consequence of the named lemmas or the actual functions.
Do not claim otherwise. If a later target requires another envelope or
physical identity, list it and obtain a separate scope assessment first.

### Primary atomic input and applicability

Christian Bayer and Josef Teichmann, *The proof of Tchakaloff's Theorem*,
Proc. Amer. Math. Soc. 134 (2006), 3035–3040,
DOI [10.1090/S0002-9939-06-08249-9](https://doi.org/10.1090/S0002-9939-06-08249-9).
Inspected [arXiv:math/0502473v2](https://arxiv.org/pdf/math/0502473v2)
and the [author manuscript](https://people.math.ethz.ch/~jteichma/tchakaloff120405.pdf):
Theorem 1 and Corollaries 1–2, pp. 2–4, including both the
full-dimensional and lower-dimensional proof cases and Corollary 2's
push-forward/lifting argument. Corollary 2 replaces a positive measure
concentrated on a measurable set by at most N positive atoms there,
preserving N integrable measurable coordinates. It needs no compactness.

For scope comparison use the six-coordinate map

    phi(D,B)=(1,D,D^2,DB,DB^2,|B|^3), (D,B) in K.

K is closed/Borel and each coordinate is continuous. An admissible law
must make all coordinates absolutely integrable. The constant coordinate
preserves total mass one. Corollary 2 then permits at most six atoms,
retaining the fifth coordinate's actual finite value as well as the four
signed moments. This applies separately at each ell; it supplies no
uniform atom locations or weights and no assertion of feasibility.
Import the theorem rather than reprove this reduction. A fixed atom
bound is therefore supported; solving the specific scaling constraints
is the genuinely remaining specialization.

As an independent statement check, Philipp J. di Dio and Mario Kummer,
*The multidimensional truncated moment problem: Carathéodory numbers
from Hilbert functions*, Math. Ann. 380 (2021), 267–291,
[Theorem 2.2](https://link.springer.com/article/10.1007/s00208-021-02166-x)
(Richter theorem), is formulated for a finite list of measurable functions
and gives at most the list's length in atoms for an existing moment
sequence. The surrounding definition of the moment cone was read.
This corroborates the conditional reduction, not feasibility. The
original Richter (1957), Satz 11, is a cited historical lead, not a
separately inspected source or an additional assumed input.

### Stronger optimization results and their limits

Dimitris Bertsimas and Ioana Popescu, *Optimal Inequalities in Probability
Theory: A Convex Optimization Approach*, SIAM J. Optim. 15 (2005),
780–804, DOI [10.1137/S1052623401399903](https://doi.org/10.1137/S1052623401399903).
The [final author-hosted PDF](https://web.mit.edu/dbertsim/www/papers/MomentProblems/Optimal-inequalities-in-probability-theory-A-convex-optimization-approach-SIAM15.pdf)
was inspected in Section 2, pp. 784–785, Theorems 2.1–2.2 and the
weak-duality proof; also Section 4.1, pp. 792–795, Theorems 4.1/4.3
and the relevant proof qualifications. An initial 2002 INSEAD working
paper was located/read but is superseded here by the final 2005 text.

The paper gives moment-constrained event bounds and dual polynomial
majorants. Its strong-duality theorem assumes an interior feasible
moment vector; it warns of nonattainment. Its multivariate SDP
approximation uses compact semialgebraic sets with the stated
sum-of-squares compactness certificate. Neither qualification is
established for this sparse, noncompact K-supported problem, which
also includes |B|^3 and an asymptotic upper envelope. Consequently
no exact SDP solution, automatic optimizer, strong duality or
infeasibility certificate is imported for our target. A future exact
pointwise separator may be checked directly; a failed restricted
numerical search is not an infeasibility proof.

### Discovery, duplicates and preserved failures

Searches included `Richter theorem finitely atomic measures prescribed
integrals measurable functions moment problem`, `Bayer Teichmann proof
Tchakaloff theorem noncompact support integrable moments 2006`,
`Bertsimas Popescu optimal inequalities probability theory multivariate
moments support semidefinite 2005`, `truncated moment prescribed sign
mixed support`, and `moment problem quadrant third moments`, together
with exact DB/DB^2 joint-sign and Mathlib/Richter/Tchakaloff queries.
The generic searches provided the sources above; the exact-sign
searches gave no inspected matching feasibility law or obstruction.
Some quadrant results concerned radiative-transfer moment bases with
different support/constraints, and were not used as mathematical inputs.
No absence or originality claim follows from these searches.

Targeted notebook-local searches for atomic/Richter/Tchakaloff/moment-only
claims in drafts/literature, foundations, history and ATTEMPTS found no
completed duplicate of this five-constraint sufficiency test. Read the
step-99 clipping assessment's scope/discovery and its history decision,
and the ATTEMPTS records for L394/L399/L400. Those negative
positive-leading-mean tests remain intact and do not decide the present
abstract feasibility target. Step 99's missing clipped mixed-moment
coverage remains parked; this turn supplies no new clipping source.

Mathlib: no full matching support-preserving finite-moment theorem was
established by the narrow documentation searches. Full coverage is
**not checked**, not asserted absent. Supporting convexity or integration
facts are not claimed to match the full theorem. Formalization is not
needed for this informal source comparison.

### Bounded continuation and stopping test

After the supervisor's separate approval of this newly written scope,
perform one mathematical feasibility attempt with at most six atoms
in K. Positions and positive weights may depend on ell, with weights
summing exactly to one. Prove all four stated asymptotics with their
exact constants and the uniform fifth bound for every sufficiently
large ell; finite decimal matches or leading-sign matches do not suffice.
Known atomic replacement is citation-only. No actual-function realization,
RH, independence, fixed atom locations, or full clipped-mean asymptotic
is assumed. Essential canonical inputs remain L388/L393/L405/L406/L409.

Continue this inference test if an exact family meets all five conditions,
or if an exact support/moment inequality rules out every such family.
The former stops deducing the prescribed joint sign from this selected
scalar information; the latter can motivate a joint-sign implication,
but its asymptotic errors must also be controlled. Failure of one ansatz
or a numerical solver proves neither alternative. If the bounded attempt
finds no certifiable construction or separator, preserve that evidence
and reassess the mechanism rather than relabeling it as a theorem.
No further source access is essential to start this bounded test.

Plausible use is diagnostic: identify whether an additional sign-sensitive
or physical input is necessary before returning to the negative-Bcal
clipped weight. Even a successful obstruction leaves actual clipping,
regulator choice, total L367 margin/remainder, actual common-zero upper
counts and global mixed positivity unresolved. PROOF.md and DAG.md
require no edit because the mathematical argument has not changed.
