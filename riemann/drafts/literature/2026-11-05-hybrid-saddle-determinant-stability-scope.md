# Hybrid actual/saddle coefficients — determinant stability assessment

TARGET: Review determinant-stability coverage for D_(r,r-1) using b_j=a_j for j<12000 and b_j=H_*(j)/(8*4^j Gamma(2j+1)) otherwise, retaining L831's full coefficient-error budget.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step658 searched structured/componentwise distance to singularity, Toeplitz corner perturbations and exact hybrid/xi/saddle determinant terminology; primary hypotheses, finite determinant identities and relevant counterexample cases were read below. No matching hybrid sign or uniform conditioning theorem was established.
SOURCE_EVIDENCE: Rump 1997 Proposition2.6 and proof (author PDF printed pp.11–12); Rump 2003 Section9 (9.1)–(9.3), Theorem9.2/general-Toeplitz case (journal pp.49–54); Böttcher–Fukshansky–Garcia–Maharaj 1406.7594v2 Theorem3.1/proof (8)–(10), Section5 hypotheses/Theorem5.1; Duits DPP2 AppendixA Lemmas66/69 and proofs (printed pp.51–52). Precise links and qualifications follow.
COMPARISON: Known finite regularity tools apply conditionally; fixed-symbol/fixed-corner Toeplitz asymptotics do not supply the moving hybrid margin. Rump's structured examples forbid reading a failed crude inverse bound as a structured singularity certificate. Regularity and positive coefficients do not supply the independent reference sign.
GAP: Pay a hybrid structured regularity margin and independently a reference sign, then growing-order control and other mixed signs. None is established here. A separately nominated first-corner test isolates regularity without assuming a sign.
REASON: Inspected theorem scope rejects automatic asymptotic sign transfer and distinguishes structured instability from failure of a sufficient norm bound. Standard finite rank-one tools support one bounded test; no new creative sign mechanism is ready.
SCOPE: Completed literature-only review; no matrix experiment, new derivation, lemma or mathematical-script edit. Original nomination below is retained as historical scope. A separately written first-corner assessment awaits next-turn approval.

## Original nomination — retained; completed review follows

Use the normalization in L776: a_j=lambda_j/(8*4^j), with
lambda_j=H(j)/Gamma(2j+1). H_* is exactly L831's branch-fixed
function; use it only at positive integers j>=12000. The proposed
matrix is B_r=[b_(r-1+q-p)] for 0<=p,q<r. These definitions
nominate an object for review; no determinant sign, asymptotic margin,
matrix bound or finite-rank assertion is established here.

Main gap: actual-Xi all-degree mixed positivity, especially k=r-1.
The intermediate question is whether a reference-matrix sign and a
quantitative stability margin can be certified while paying the actual
remainder. Its plausible downstream use is a genuinely quantitative
exceptional-minor comparison. The independent all-order and low-index
sign questions remain open; exact low coefficients are not a sign proof.

Search precise terminology for structured determinant perturbation,
Toeplitz conditioning, and signed determinant/inertia stability. Read
primary hypotheses and relevant cases, and distinguish an applicable
stability theorem from an unpaid estimate of its inverse or singular
value. Compare any promising mechanism with L772's generic stop,
L780's failed positive-block requirement, C785a's equivalent-sign
identity, L817's fixed-model obstruction, and L790's distinct range.
Read those canonical proofs only if their specific claim is needed;
they are contrasts, not assumed inputs to a new sign argument.

Continuation test: identify a precise bound on B_r and the full error
matrix that can be tested without assuming the target minor's sign.
The initial review must state its dimension/range and required margin
before nominating a mathematical attempt. If available theorems merely
rename the missing sign or require an unmotivated inverse bound, record
that limitation and reject automatic transfer. Do not approve generic
parameter searches or repeat a stopped fixed-model test.

Essential prospective input IDs are L018/L021 for normalization,
L776 for the minor, and L830/L831 for the analytic estimate. Reference
sign, conditioning, degree uniformity and sufficiency of the actual
remainder are unresolved assumptions. No cross-notebook input is used;
matching Mathlib coverage is unchecked. A creative proof attempt is
not yet ready: determinant-source coverage and a concrete margin test
must be supplied first.

## Completed review — step658, 5 November 2026

The main gap remains actual-Xi all-degree mixed positivity, especially
k=r-1. The reviewed intermediate target is a hybrid reference sign plus
a quantitative stability margin; downstream it could transfer a proved
reference sign to the actual exceptional minor. Regularity alone is a
useful possible intermediate input, with the sign explicitly independent.

### Searches and local overlap

Queries included `Rump componentwise distance singularity regularity
radius |A inverse| Delta theorem`, `Toeplitz determinant perturbation
growing dimension smallest singular value stability Higham`,
`"hybrid" "saddle" "xi" "determinant"`, `"Riemann xi" "Toeplitz"
"perturbation"`, and `"Toeplitz" "determinant" "componentwise"
"stability"`. These bounded searches do not establish novelty.

Read relevant hypotheses/conclusions and source-specialization passages
of L772/L780/C785a/L817/L790, L776's normalization and determinant
identity, and L830/L831's exact bounds/domains. L772 blocks the generic
Turan implication; L780 stops its specified positive Schur block;
C785a gives an equivalent sign, not an independent certificate; L817
stops its fixed central model. None bans the hybrid. L790's derivative
estimate at k>=10^9 does not pay k=r-1 determinant conditioning.
Its named cubic-wedge preprint appeared in searches; no additional
theorem from it was imported. Lin's Willow-transform title and a claimed
de Bruijn–Newman solution were uninspected leads, not theorem evidence.
No cross-notebook mathematical input was read.

### Primary theorem statements and applicability

1. S. M. Rump, *Almost sharp bounds on the componentwise distance to
   the nearest singular matrix*, Linear and Multilinear Algebra42
   (1997),93–107, [author PDF](https://www.tuhh.de/ti3/paper/rump/Ru97b.pdf),
   definition(1), (2)–(3), Proposition2.6 (22)–(24) and full proof,
   PDF printed pp.1–2,11–12. For real nonsingular n-by-n A and E>=0,
   d(A,E) is the least alpha>=0 permitting singular A+F with
   |F|<=alpha E, or infinity if none exists. With rho the spectral
   radius, 1/rho(|A^-1|E)<=d(A,E)<=gamma(n)/rho(|A^-1|E), where
   n<=gamma(n)<=(3+2sqrt(2))n. The proof handles nonnegative E by
   continuity; zero spectral radius corresponds to infinite distance.
   Thus rho<1 is a sufficient full-box regularity test. This is an
   unstructured theorem: failure of that sufficient test is inconclusive,
   and an unstructured singular member need not preserve Toeplitz
   coefficient correlations. No actual hybrid inverse is supplied.

2. S. M. Rump, *Structured perturbations Part II: Componentwise
   distances*, SIAM J. Matrix Anal. Appl.25 (2003),31–56,
   [author PDF](https://www.tuhh.de/ti3/paper/rump/Ru03g.pdf), Section9,
   (9.1)–(9.3), journal pp.49–50; general-Toeplitz example following
   (9.7) and Theorem9.2, pp.53–54, including its determinant argument.
   For nonsingular real A in a prescribed linear structure and weight
   E, (9.2) characterizes structured distance by maximizing moduli of
   real eigenvalues of A^-1 F over allowed structured F. This is not
   an estimate for our B_r. Theorem9.2 exhibits Toeplitz matrices with
   arbitrarily large structured componentwise solution condition number
   and structured relative distance to singularity1. Hence poor
   conditioning alone cannot reject structured stability. These
   examples are not positive hybrid xi coefficients; no hybrid sign
   or instability follows. No reproof is needed.

3. A. Böttcher, L. Fukshansky, S. R. Garcia and H. Maharaj,
   *Toeplitz determinants with perturbations in the corners*,
   [arXiv:1406.7594v2](https://arxiv.org/pdf/1406.7594v2),21 July2014,
   Theorem3.1 and full proof (8)–(10), printed pp.4–5; Section5's
   hypotheses and Theorem5.1, pp.15–16. Theorem3.1 fixes a piecewise
   continuous circle symbol whose completed range avoids0 and has
   winding number0, and fixes corner blocks of size m0 as n grows.
   It supplies an asymptotic ratio via inverse corner limits. Section5
   assumes a>=0 a.e., a in L1 and log a in L1, giving Hermitian positive
   definite sections. Neither set of hypotheses is established for
   our moving shifted hybrid. Fixed low coefficients do not establish
   a fixed symbol or fixed perturbation corners as r grows. Finite
   identity(8) is usable after paying invertibility; no theorem here
   supplies the requested quantitative hybrid threshold.

4. M. Duits, *Determinantal point processes*,
   [DPP2 author PDF](https://people.kth.se/~duits/static/media/DPP2.44e051d148b79af222fa.pdf),
   AppendixA Lemma66 (Sylvester's identity), printed p.51, and Lemma69,
   p.52; both full proofs inspected. Finite rectangular U,V satisfy
   det(I+UV)=det(I+VU) without positivity or invertibility of U,V.
   This includes the finite rank-one case. Factoring a reference B
   separately requires B nonsingular. The identity pays no inverse
   entry, cofactor ratio or reference sign. Import it; do not reprove it.

Higham's *A Survey of Componentwise Perturbation Theory* (1994),
[author PDF](https://eprints.maths.manchester.ac.uk/651/1/SURVEY.pdf),
Theorem2.4 and Section3's distance discussion were inspected for
terminology/reference checking, not as a stronger hybrid theorem.
Hartman–Hladik, [arXiv:1806.09988](https://arxiv.org/html/1806.09988),
introduction and Section2.4, were inspected as leads. Its positive
rank-one radius scaling assumes strictly positive factors and is not
the sparse-corner case; it is not used for that specialization.
Poljak–Rohn's original formula was not read and is not an imported input.

### Full tolerance, bounded test and decision

Keep a_j=lambda_j/(8*4^j), b_j as nominated, and L831's branches.
Its real-integer specialization supplies the tolerances

    e_j=(30/T_j)b_j, T_j=j/W_0(2j/pi) for j>=12000;
    e_j=0 for j<12000.

For each r the full weight is E_r=[e_(r-1+q-p)]. Repeated coefficients
on each diagonal share the same actual error. Enlarging to independent
entry intervals is safe for a sufficient test, not for an instability
claim in the smaller coefficient class. The complex logarithmic and
curvature bounds of L830/L831 remain available; this pointwise box is
an enclosure, not a characterization of analytically admissible errors.

A useful sign transfer must pay both a reference sign and structured
distance>1 for this entire tolerance (or another sufficient certified
margin). The inspected sources supply neither. Automatic asymptotic
transfer is therefore rejected, without globally stopping the hybrid.

Nominate just r=6001, the first order reaching coefficient12000, as a
finite rank-one regularity test. Its attempt must first verify the
index support, then pay a scalar sensitivity against the full interval,
with no assumed sign. This is a routine specialization, not a creative
sign mechanism. A positive regularity certificate still leaves the
reference sign and all growing-order questions open. The detailed
new nomination is in `2026-11-05-first-hybrid-corner-regularity-test.md`
and requires separate approval before mathematics.

Continue only with a paid margin or an informative precise obstruction;
stop this finite test if it merely renames an unpaid exceptional-minor
ratio. A singular member defeats the pointwise robust certificate only,
not actual-Xi positivity or analytic correlations. A failed sufficient
norm bound alone is inconclusive. No matrix was evaluated or new result
derived here. Matching Mathlib coverage is unchecked; no absence claim
or RH conclusion is made.
