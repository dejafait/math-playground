# Full tilted T_6 derivative-Bezoutian: nominated exact test

TARGET: Construct the unrestricted-bulk derivative Bezoutian of Kuznetsov's full tilted T_6 in the descending Pollaczek basis, verify its left-metric orientation and scaling, and certify its complete inertia using the existing rational enclosures, or record an unresolved determinant sign.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse completed source comparison2013 in drafts/literature/2026-11-20-tilted-pollaczek-bezoutian-scope-2012.md, including exact-family searches, local Hermite/runtime/reciprocal-congruence comparisons and primary theorem inspection. No novelty claim.
SOURCE_EVIDENCE: Wu–Wu–Yang ELA21(2010),154–171, definition(1.1), Lemmas2.1–2.2/Corollary2.4/Propositions2.5–2.6 and proofs pp154–159, https://emis.de/ft/34467; Heinig–Rost2008-09 Example7.2/Proposition7.15/Theorem10.4 pp40/45/59–60, https://www.tu-chemnitz.de/mathematik/preprint/2008/PREPRINT_09.pdf; review2001's Coste Jacobi theorem p19 and exact Kuznetsov formulas; C029n's audited rational enclosure/scaling proof.
COMPARISON: General-basis Bezoutian construction and its Hermite inertia are known. Only the exact actual-coefficient six-dimensional application, convention checks and sign separation are unpaid. This is a finite certification alternative to the degree24 Arb implementation, not an independent uniform index mechanism.
GAP: Certify the actual full-bulk form and all required signs at N=6; eventual uniform index<=1 and the qualified weighted compact-limit input remain unresolved and are outside this test.
REASON: One bounded actual-coefficient reproduction can answer a concrete unrestricted-bulk question with existing standard-library exact arithmetic; no unchanged runtime retry, degree escalation or automatic sign import.
SCOPE: Newly nominated ready coverage; requires separate supervisor approval next turn. One N=6 coefficient/determinant test only, fixed existing input enclosures and no new algorithm or source assumptions.

The main gap is L030–L032/C032a actual-Xi all-degree mixed positivity.
C029l/C029m describe the conditional downstream use of an eventual
index bound, with arbitrary nullity. This finite test neither proves
that premise nor audits the upstream[9] compact-convergence assertion.
It is reproduction/development of an existing method, not a creative
central-gap mechanism or evidence beyond the inspected sources.

Use C029n's exact T_6 with a_k=6!/((6-k)!6^k) beta_k, all odd terms
retained, and its audited u_0,...,u_8, q_0,...,q_6=beta_k/S data,
where S=sin(pi/8)/sqrt(2)>0. Its proof certifies a_6<0 and actual
degree six. The canonical recurrence gives p_0,...,p_6. Essential
finite input: C029n, review2001 and comparison2013; C029l/C029m are
downstream context only. No cross-notebook input is proposed.

Put U=T_6/S. Define B_desc by the coefficient identity

    Phi(x)^t B_desc Phi(y)
      = (U(x)U'(y)-U(y)U'(x))/(x-y),
    Phi=(p_5,p_4,p_3,p_2,p_1,p_0)^t.

This defines the nominated matrix; no entries or signs have been
computed. Use exact arithmetic in Q(sqrt(2))[pi]. Check the polynomial
identity after multiplication by x-y and all 36 entries of symmetry.
No bulk entry is fixed to the identity. Direct coefficient conversion
uses a degree-graded basis with nonzero rational leading coefficients,
not an assumed real-rooted basis expansion theorem.

Wu uses an ascending row basis and a coefficient matrix C_Q. Its
Proposition2.6 says B_Q C_Q^t=C_Q B_Q. Check the reversal/transpose
against C029n's descending evaluation C rather than assuming that
source C_Q=C. Verify the candidate identity C^t B_desc=B_desc C
exactly, clearing only C029n's proved nonzero a_6 denominator. For
the existing A=D^(-1) C D, test the congruently scaled candidate
G=D B_desc D. Use C029n's positive D and D_i^2, and show the exact
substitution into A^t G=GA in the finite write-up. The formula for G
is a nominated convention check, not an already executed application.
Certifying inertia of B_desc suffices for its real invertible diagonal
congruence; no floating approximations to the D_i may be used to assert
the matrix identity or signs.

The target is a nonsingular form with negative index<=1. Source
congruences identify derivative-Bezoutian inertia with the Newton-sum
Hermite inertia; no separate root solver or Pontryagin theorem is
required to interpret a certified signature. If all six leading
principal determinants are nonzero, apply the Jacobi theorem inspected
in review2001: count sign changes in (1,Delta_1,...,Delta_6).
This yields the full inertia with zero nullity, and source coprimality
coverage then certifies simplicity. A singular/zero-containing case
does not meet this diagnostic's nonzero-minor method. Do not silently
use a zero-minor rule, infer simplicity or equate interval containment
of zero with exact singularity. In general the source's negative index
counts distinct conjugate pairs, not their algebraic multiplicities.

For sign certification use the existing audited 60-decimal rational
enclosures of pi and sqrt(2) from C029n, with their full Machin/isqrt
proof. Compute coefficient polynomials and the six determinants by
exact finite arithmetic (the Leibniz determinant definition suffices),
then evaluate using justified rational interval operations. The fixed
enclosures are the entire numerical budget: no precision campaign,
external package install or runtime discovery. If coefficient growth
makes a sign unseparated, preserve that exact failure and stop this
attempt. Any materially different certification method needs coverage
before use. The reason to implement rather than just cite is that no
inspected source certifies these exact finite coefficient signs.

Save full coefficients, basis conversion, kernel/metric identities,
six exact determinant polynomials and complete enclosures/signs,
actual and required inertia, all failures, reproduction command and
method in a local certificate. Print only a compact result/bounds/
failure/path summary. Use the shared inspector on selected fields;
a preview or a script's pass banner does not verify the argument.
Any claimed result belongs in one canonical lemma, with the imported
source hypotheses, full finite applicability proof and Mathlib section.

A certified index<=1 pass retains only this finite reproduction and
the possibility of a coefficient pattern to be assessed later. A
certified index>=2 rejects this threshold at N=6 only, not an
eventual-only bound or RH. Either result forbids automatic degree
escalation; further research needs a new discriminating target.
An unresolved determinant is honestly inconclusive. Existing C029n,
generic-preservation, common-Favard, runtime and summability stops
remain in force in their original scopes. Full matching Mathlib
coverage is unchecked. No mathematical calculation has been performed
or approved by the creation of this new assessment.
