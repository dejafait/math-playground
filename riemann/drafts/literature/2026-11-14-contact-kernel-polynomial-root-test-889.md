# Contact kernel polynomial: completed finite algebraic coverage review

TARGET: Assess coverage for a finite Hankel-jet test of whether C466b's contact minor signs force a real-rooted kernel polynomial, starting at m=3 and keeping actual-density realizability separate.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Step890 completed bounded exact/stronger-result searches for indefinite Hankel kernel roots, formal orthogonality, negative recurrence coefficients and sign-regular Hankel matrices; inspected primary statements and relevant proof cases below. Narrow local searches found no ready assessment or exact finite-jet result for these contact signs. Search failure is not evidence of novelty.
SOURCE_EVIDENCE: Bakan--Berg arXiv:1605.01196v2, Section1 (1.12)-(1.22), Theorem2 and Section5.3 (5.6)-(5.10); Kimsey arXiv:2006.08692v1, Theorem7.4 and both proof directions, Corollary7.5; NIST DLMF 18.2(i),(vi),(viii),(ix). Exact hypotheses and applicability limits are recorded below.
COMPARISON: Formal Hankel orthogonality supplies a polynomial construction, not the needed real-root conclusion. The inspected real-zero proof requires positive raw leading determinants, whereas C466b's m=3 signs include a negative raw second determinant. Kimsey requires rank-preserving extension, diagonalizable shifts and a real variety for minimal real signed support; those hypotheses cannot be inferred from the supplied signs by citation alone.
GAP: No inspected source proves real-rootedness or an exact counterexample under precisely D_1,D_2>0,D_3=0. Approve only the bounded m=3 finite-jet diagnostic below; actual-density realizability, first-contact neighborhood and weighted forcing remain separate.
REASON: Source comparison is now adequate for one exact algebraic test. A direct citation does not settle its signed boundary case; an elementary finite-dimensional calculation is justified as a diagnostic, without a novelty claim or a generic density conclusion.
SCOPE: Real entries a_0,...,a_4; m=3; signed leading minors D_1,D_2>0,D_3=0; normalized kernel polynomial from C466b (14). Only these pointwise signs and the finite Hankel structure are tested. No density construction, global PF claim, higher-order sweep or weighted-sign estimate is covered.
COVERED_TARGET: Test at m=3 whether C466b's finite Hankel contact signs force a real-rooted kernel polynomial, using an exact proof or finite-jet counterexample and keeping actual-density realizability separate.
LITERATURE_REASON: Required first theorem-level comparison for the finite Hankel-jet target, outside assessment888's global density-class scope; this completes its missing essential coverage.

Essential local input: C466b's rank-one-adjugate reduction (14), using
C466a's notation and inherited L018/L024 normalisation only to identify
the actual object. For a proposed algebraic diagnostic at m=3, use real
jet entries a_0,...,a_4, A=[a_(i+j)]_(0<=i,j<3), the signed leading
minors D_j=(-1)^(j(j-1)/2) det[a_(i+k)]_(0<=i,k<j), D_1,D_2>0 and
D_3=0. The rank is two and the kernel vector is normalised by v_2=1,
as in C466b; the question is the root location of P(z)=v_0+v_1 z+z^2.
These define the proposed test, not a new conclusion about its outcome.

The bounded test is now ready after the comparison below. A generic
jet obstruction, if later established, would rule out an inference
from the minor signs alone. It would not exhibit a contact or a failure
for the actual density, nor refute the actual sign-variation bound.
Conversely, a real-root theorem would still leave the action of its
factors on p, sign-interval geometry and C466b (7)/(9) unpaid.

Continuation/abandonment test for the proposed later calculation:
either justify the real-root inference under exactly these signs or
give an exact finite-jet obstruction; then stop this diagnostic. No
repeated scalar domination, global PF assumption or smooth-density
realization is included. Preserve the L874/L611/U12 stops and the
independent simultaneous-contact, propagation and L030 gaps.

## Primary sources actually inspected

Write Delta_j for the raw size-j Hankel determinant in this comparison,
to distinguish it from C466b's signed D_j. The m=3 source comparison
uses Delta_1>0, Delta_2<0, Delta_3=0, directly translating the supplied
definition. This is not the positive-definite moment hypothesis.

1. Andrew Bakan and Christian Berg, *Solvability of the Hankel
   determinant problem for real sequences*,
   [arXiv:1605.01196v2, 9 May 2016](https://arxiv.org/html/1605.01196v2).
   Section1 equations (1.12)-(1.16) define determinant polynomials for
   arbitrary real sequences and their formal orthogonality. Equations
   (1.18)-(1.22) distinguish general nonzero recurrence coefficients
   from positivity; quasi-definiteness concerns all nonzero leading
   determinants and must not be asserted at this contact. Theorem2
   assumes a nonzero real sequence and a nonzero size-r determinant:
   the degree-r determinant polynomial has full degree and no common
   zeros with its predecessor or second-kind polynomial. It asserts
   no real-root location. Section5.3 (5.6)-(5.10) proves real, simple
   roots under positivity of every raw leading determinant through
   size r. Read the nonreal-root exclusion and simplicity arguments:
   both use the positive Christoffel--Darboux sum. Their positivity
   premise fails for the signed second minor here. No infinite-rank
   extension or source theorem is imported as a root certificate.

2. David P. Kimsey, *On a minimal solution for the indefinite truncated
   multidimensional moment problem*,
   [arXiv:2006.08692v1, 15 June 2020](https://arxiv.org/html/2006.08692v1).
   Theorem7.4: a real truncated multisequence with rank r has an
   r-atomic quasi-complex representing measure exactly when its
   moment matrix has a rank-preserving extension and the associated
   shifts are diagonalizable. The support equals the extension's
   variety. Real support is an additional variety condition;
   Corollary7.5 includes it in the equivalence for a minimal signed
   real measure. Both proof directions were read, including (7.4)'s
   shift/diagonal representation and the final real-support step.
   This distinguishes real and conjugation-symmetric complex nodes;
   it does not certify the contact's kernel roots from leading signs.
   No extension, diagonalizability or real-variety hypothesis is
   established for the proposed jet. A general representing measure
   is also different from a minimal rank-r representation.

3. [NIST DLMF 18.2](https://dlmf.nist.gov/18.2), checked 2026-11-14:
   (i) imposes a nonnegative integrable weight with all absolute
   moments, positive weights on discrete supports, or a positive
   measure; (vi) gives simple real zeros in the orthogonality interval;
   (viii) states the positive-measure Favard conclusion with its
   coefficient inequalities; (ix), (18.2.27)-(18.2.30), gives determinant
   and recurrence formulas, citing Gautschi (2004), Theorems2.1-2.2.
   These are comparison references, not a positive measure for the
   derivative jet. Positivity of the underlying density p does not
   identify its derivatives at one point with positive raw moments.

The relevant applicability comparison is only that the supplied signs
do not meet the inspected positive-minor theorem. It does not prove
that the polynomial has nonreal roots. No new example, discriminant,
recurrence specialization or obstruction theorem was derived this turn.

## Search, overlap and bounded continuation

Queries actually used: `indefinite Hankel matrix orthogonal polynomial
real zeros quasi definite moment functional signed leading minors`;
`Hankel matrix rank two kernel polynomial real roots indefinite moment
problem`; `"Hankel" "sign regular" "zeros" polynomial imaginary`;
`"orthogonal polynomials" "negative" "recurrence coefficients"
"zeros" quasi definite`; `"Hankel" "kernel polynomial" "real"
"rank" indefinite`. Search snippets and abstracts served discovery
only. The Gautschi book mirror, Cvetkovic--Milovanovic software paper,
Tyaglov sign-regular/Hurwitz lead and binary-form decomposition lead
were not inspected as primary theorem inputs. The present diagnostic
needs no claim from them; full sign regularity is not a supplied
assumption. No inaccessible source remains essential to this test.

Local checks used C466b's hypotheses and rank-one-adjugate reduction
(14), C466a's normalization, assessment888's completed source stop,
the contact-score/reciprocal-Hankel failure records, the common-Favard
stop at L796, and the Laurent source comparison in the L918 null-row
assessment. The last concerns PSD raw moments, not these signed jets;
L796 concerns a common positive measure for a different actual theta
polynomial family. Neither settles this finite diagnostic. No sibling
notebook or full archive was loaded. L874/L611/U12 stops are preserved.

The main gap is L030-L032/C032a's actual-Xi all-degree algebraic-square
positivity. This intermediate question tests only a possible real-factor
premise for C466b's differential operator. A positive answer could
support later factor-by-factor sign analysis; a negative answer removes
an unjustified inference from contact signs. Neither supplies the
actual weighted masses or a sign-preserving barrier.

For the next calculation check the whole proposed finite certificate:
real entries, D_1,D_2>0, D_3=0, rank two, Av=0 with v_2=1, and the
quadratic root discriminant. A counterexample must have discriminant
strictly negative; a universal positive conclusion needs a proof for
all admissible jets, not a sample search. If neither is obtained in one
bounded attempt, record the unresolved constraint and stop; do not
extend the order or construct densities in this diagnostic. Even an
exact counterexample would concern only the pointwise relaxation,
not an actual contact, first-contact neighborhood or actual-V bound.

Outcome EXPLORATION: essential comparison completed and the single
covered calculation is ready; no mathematical advance or informative
finite-jet negative is claimed. Full matching Mathlib coverage was not
checked; unknown availability is not evidence of absence. No lemma,
mathematical script, DAG or PROOF change is needed for this source review.
