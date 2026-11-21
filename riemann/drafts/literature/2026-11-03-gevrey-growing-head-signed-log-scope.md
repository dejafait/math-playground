# Source comparison: Gevrey growing-head signed logarithmic loss

TARGET: Assess whether one fixed L703 profile has [A_n(e^(H_n))-A_n(e)]_+=o(n) for H_n=ceil(n^(2/3)) in L695's full L666 response.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 145 made fourteen bounded queries on growing-degree Mahler/logarithmic stability, zeros and Gevrey data; reused the step-114/126 comparisons and checked the precise L695/L702 stops. No inspected theorem covers the exact growing-head loss; the failed search establishes neither novelty nor impossibility.
SOURCE_EVIDENCE: Reinspected Dimitrov--Habegger arXiv:1909.06051v2 Appendix A, Lemmas A.4--A.5 pp.47--48 including the normalized proof and constant case; Brunault--Guilloux--Mehrabdollahei--Pengo arXiv:2203.12259v2 Theorem 4.6, Remarks 4.7--4.9 pp.9--10 and Proposition 4.10 with complete proof p.11. Reuse the previously inspected Jensen, Boyd, Gevrey and Picard sources in the named assessments.
COMPARISON: The sources retain coefficient normalization, term-count or slice-complexity dependence and logarithmic zeros; they do not turn L703 weighted decay into a signed complete-mean estimate. L695 stops a different absolute cost, and L702 stops endpoint-only extension. A paired tail replacement with explicit singular-log payment remains an unproved family-specific test.
GAP: Establish or obstruct the exact positive-part o(n) loss for one fixed L703 profile at H_n=ceil(n^(2/3)), paying all numerator, denominator, normalization, zero and growing-degree costs. No uniform transversality, coefficient proximity, Fourier gap for the head or intermediate profiles, or favorable signed variation is known.
REASON: Essential comparison is sufficient for one bounded signed tail-replacement test, with the discriminating payment criterion below; no source proves the target. This literature-only step derives no new estimate and edits no lemma or mathematical script. The completed assessment needs the supervisor's separate approval before research.
LITERATURE_REASON: The changed observable compares full responses of a fixed exact Gevrey profile and an n-dependent head; prior ready coverage concerned infinite-profile regularity and does not settle this signed finite logarithmic loss.
SCOPE: Only TARGET; n=12q+3, q->infinity, original anchor, unit masses, real cap 1/8, inverse denominator angle, j=0, both available endpoints -2q and 2q-1, and every M=n/3 spatial moment. The actual profile and its positive centered gap are fixed before n. No cross-notebook input.

The original continuation nomination is preserved below. Its pending
source-review language is superseded by the completed review at the end;
its mathematical estimates remain unproved. The intended future mechanism is signed
logarithmic stability for a sublinear growing head, using the newly
audited regularity together with the exact profile equation. A first
creative attempt is justified only after the essential comparison is
complete; no estimate is asserted in this file.

Use exactly L695's definitions of G_(n,e), A_n(e) as its normalized
two-circle mean log|G_(n,e)|, and e^(H)_m=e_m for |m|<=H and zero
otherwise. Here H=H_n=ceil(n^(2/3)). Each comparison response retains
all available nodes and their unit masses: setting a displacement to
zero does not remove its atom. The comparison profile depends on n;
the actual L703 profile does not. No centered gap is assumed for the
truncated comparison. Retain logarithmic zeros and their integrability;
do not replace log|G| by a clipped or sampled value.

The precise proposed threshold is the positive part of the difference
of the complete means, divided by n, tending to zero. It is not a
termwise absolute-error threshold, an integral of the pointwise
positive logarithmic difference, or a finite-head ordered limit. The
particular sublinear cutoff makes the proposal independently testable;
its suitability is unproved. Stretched-exponential tails alone must
not be said to pay exponential amplification in the original factors.

If established, this would control one signed truncation loss relevant
to the unresolved complete logarithmic compensation. A bound for the
growing-head mean itself would still be needed; L695's fixed-head
limit is not uniform in H and cannot simply be substituted. H/support,
Xi realization and actual-Xi all-degree positivity remain separate.
Even a successful intermediate estimate would not solve RH.

Reuse the prior Mahler/Jensen and growing-degree comparisons in
`2026-11-03-summable-displacement-complete-log-transfer.md` and
`2026-11-03-centered-gap-complete-logarithmic-sign.md` before new
searches. Check exact statements, stronger results, relevant proof
cases and known obstructions for the changed hypotheses. A usable
signed estimate must pay its n-dependent constants and zero sets.
Do not repeat generic divisor accounting or L695's stopped absolute
closure, and do not discard L702's nonzero signed interior.

Continue to a bounded mathematical test only upon an importable match
or a documented mechanism capable of testing this o(n) loss. Record
an informative obstruction if the proposed mechanism necessarily
pays order n or greater. Failure of one sufficient mechanism, or of
one selected profile, does not refute existence for every L703 profile.
Any different cutoff scale or observable needs its own covered scope.
Full matching Mathlib coverage is not checked.

## Completed comparison — 3 November 2026, step 145

### Exact scope and local overlap

Use the definitions above without changing TARGET. L703 supplies an
existential choice of fixed cutoffs, r,w,c and a unique associated
profile; this does not approve every possible Picard choice. All these
choices precede n. No effective lower bound on c or gap width is
assumed. The proposed loss is for the complete means and their signed
difference, followed by positive part; it is not the mean of a
pointwise positive part. The n-dependent head retains every atom.

Read L695's full statement/proof and its original method-stop record;
L666's precise hypotheses and rational continuation; L657's complete
charge statement, clearing and source scope; L692's sharper support
bound and annihilation setup; L703's hypotheses/conclusion/imports and
relevant audit passage; L702's restricted conclusion, source scope and
its updated stop record; step-115 history. Reuse the supplied L703
conceptual-audit conclusion without reopening that proof. No matching
signed growing-head bound was found in these scoped local records.
This is a scoped duplicate check, not a claim about the entire archive.

L695 (1) treats each fixed H. Neither its fixed-H limit nor an
unjustified substitution H=H_n settles TARGET. Its explicit (5) and
(8), and L692's support/onset hypotheses, are available to a future
attempt, which must justify any use with growing H. L695's absolute
counterprofile is not asserted to be a centered-gap L703 profile.
L702 supplies an actual surviving signed interior at -1 for the
selected smallness class; a single-angle modulus is not a complete
logarithmic mean. Both stops retain their original scopes. The earlier
n-dependent numerical optimization and scalar-charge rewrites are not
new evidence for this fixed-profile asymptotic question.

### Primary statements and essential proof cases

V. Dimitrov and P. Habegger, *Galois Orbits of Torsion Points near
Atoral Sets*, [arXiv:1909.06051v2](https://arxiv.org/pdf/1909.06051v2),
24 March 2022, Appendix A, Lemmas A.4--A.5, printed pp.47--48.
For nonzero complex d-variable polynomials P,Q with at most k>=2
terms each, maximum-coefficient norm and delta=|P-Q|/|Q|<=1/2,
A.5 gives

    m(P)<=m(Q)+C(d,k)*delta^(1/(8*(k-1))).

Reinspected normalization, the split at |Q|=sqrt(delta), the
small-value logarithmic integral from A.4, and the constant-Q case.
No atoral or algebraicity hypothesis is imposed in A.5. This is an
upper comparison in the displayed order; reversing endpoints changes
the relative-norm obligation. Its constants and exponent retain k.
No bound for our cleared-numerator distance or term count follows
from displacement decay alone. Reuse the complete proof comparison
in `2026-11-03-summable-displacement-complete-log-transfer.md`;
no general continuity theorem is reproved.

F. Brunault, A. Guilloux, M. Mehrabdollahei and R. Pengo,
*Limits of Mahler Measures in Multiple Variables*,
[arXiv:2203.12259v2](https://arxiv.org/pdf/2203.12259v2), 27 June 2022,
Theorem 4.6/Remarks 4.7--4.9 pp.9--10, Proposition 4.10 p.11.
For a Laurent polynomial P with k>=2 terms, d variables,
L_infinity(P)=1, 0<alpha<1, integer m-by-d matrix A,
m<=d and rho(A)>diam(P), Proposition 4.10 bounds the nonnegative
regularization error by

    C_2(d,k,alpha)*epsilon^((1-alpha)/(2*(k-1))),
    C_2=12*k^2*(18*d*k^2)^(d-1)*alpha^(1-d)/(1-alpha).

A=I_d covers the ordinary torus under the conventions reused from
step 114. Read the layer-cake proof through its final sine bound.
Theorem 4.6 improves the small-value exponent using slice term count
kappa; reinspected the monomial-slice case. Remark 4.9 retains a
multiplicity obstruction for general polynomials. This includes
logarithmic zeros, but does not estimate our endpoint comparison.
The relevant normalization, k and kappa remain unpaid. Reuse the
step-114 formulas rather than deriving a new rate here.

Reuse Boyd's fixed-degree continuity and the precise Jensen/root
formula with boundary-root handling from the two prior assessments.
L657's polynomial K and denominator Q have growing angular degree;
the actual N=M family permits degree M(n-1). Small parameter changes
do not themselves verify a source's relative coefficient hypothesis.
The Gevrey/Picard inputs already inspected for L703 establish exactly
the weighted profile stated there; no new source extraction for these
unchanged inputs is needed. No source above imports TARGET by citation.

The Chern--Vaaler 2001 Theorem 4 attribution was encountered in
Grizzard--Gunther, *Slicing the Stars*, Theorem 9.4. The original
DOI https://doi.org/10.1515/crll.2001.084 did not open in this tool;
its original statement/proof was not inspected. Treat it as an unread
lead, not a new imported comparison or an essential missing premise.
The existing primary continuity/regularization coverage suffices for
this bounded test, so this access failure is not SOURCE_BLOCKED.
No claim is based on search snippets, the attribution or an imagined
stronger Chern--Vaaler theorem.

### Search record

New query strings, 3 November 2026:

- `"Mahler measure" "continuity" "degree" perturbation roots`
- `polynomial logarithmic integral perturbation "zeros" quantitative continuity`
- `rational functions logarithmic mean stability perturbations Jensen zero counting`
- `"Mahler measure" "Hölder" "perturbation"`
- `"logarithmic" "stability" "Cartan" analytic functions`
- `"Mahler measure" "Lipschitz" zeros`
- `Chern Vaaler 2001 distribution values Mahler measure theorem 4 pdf`
- `"Mahler measure" "continuity" "unit circle" roots perturbation quantitative`
- `"Chern" "Vaaler" "distribution" filetype:pdf`
- `"The distribution of values" "Mahler" "Theorem 4"`
- `"Mahler" "measure" "root perturbation" continuity`
- `"Gevrey" "Mahler measure"`
- `"logarithmic mean" "perturbation" polynomial zeros`
- `"Chern" "Vaaler" "crll.2001.084" pdf`

The searches returned the compared Mahler papers, the attribution above,
random-root and fixed algebraic-family results, and unrelated uses of
logarithmic stability. None was inspected as a matching theorem for
our fixed unit-residue rational family with growing head. Those other
results remain screened leads, not mathematical inputs. Failure to
find a match establishes neither originality nor a counterexample.

### One bounded mechanism and its decision test

EXPLORE licenses one family-specific signed tail-replacement attempt
on exactly TARGET, after separate supervisor approval. Compare the
head and actual endpoints through the admissible straight tail path
which holds the head fixed and moves each available tail displacement
from zero to e_m. Use exact paired node factors before estimating the
complete logarithm; keep all spatial moments and original endpoints.
This is a proposed test, not an asserted identity or bound for that path.

The proposed discriminating step is to seek a regularization scale
and a signed comparison for the complete normalized numerators whose
endpoint regularization losses, normalization changes, denominator
contributions and signed variation together are o(n). Source
regularization can justify removal of zeros only with its actual
n-dependent k, coefficients and constants paid. A proof using a direct
root/charge comparison instead must retain the same payments and every
crossing. No singular-log derivative, exchange of limits or uniform
transversality is preapproved. The exact Picard equation may be used
only for the actual endpoint: neither the head nor an intermediate
path profile is assumed to have its Fourier gap or weighted solution
identity. Any recovery of cancellation there is mathematical work.

The new possible input is the audited stretched-exponential profile
and this fixed sublinear cutoff, absent in the general-l1 attempt.
The proposed refinement pairs tail replacements and keeps their sign
through the logarithmic comparison. It does not restart L695's sum of
absolute costs or L702's discarded-interior extension. It is not enough
to restate Jensen, invoke continuity or insert the Gevrey tail into an
unproved coefficient bound. No favorable scale balance is asserted.

Continue if the attempt gives the stated o(n) loss or a useful signed
partial bound with all outstanding losses explicit. Stop this mechanism
if its proved estimates necessarily leave order n or larger loss, or
if it produces no paid comparison beyond the old generic degree costs;
preserve the failed scale/estimate before selecting another mechanism.
A rigorous linear-loss subsequence for the same fixed L703 profile
would refute that profile's test. It would not refute existence for
every L703 selection. Finite samples and failed sufficient estimates
are not such counterexamples. Do not repeat an unsuccessful attempt
without materially new input or a refined discriminating mechanism.

The growing-head mean remains an independent obligation in using this
loss for complete compensation; L695's fixed-head limit is not assumed
uniform. H/support, realization and actual-Xi positivity remain open.
Full matching Mathlib coverage is unchecked; reuse only the supporting
root-formula coverage recorded in L657/L695. No formal-coverage absence
claim, new lemma, mathematical certificate, RH candidate or progress
beyond the inspected sources is asserted in this literature-only step.
