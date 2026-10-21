# Explicit-descent localization comparison

TARGET: Assess whether explicit p-descent can represent a classical E[p]-Selmer class and certify its nonzero localization in E(Q_p)/pE(Q_p) under L062 with supplied e=0.
CHECKED: 2026-10-15
DECISION: IMPORT
SEARCH_EVIDENCE: Full-p-descent/local-Kummer searches led to the author-hosted Schaefer--Stoll long version and its Schaefer evaluation reference; notebook-local explicit-descent/Schaefer/Stoll searches found no completed matching import. Queries and inspected ranges are recorded below.
SOURCE_EVIDENCE: Schaefer--Stoll, author long version dated 2001-06-13, Proposition 4.6, Section 5/(5.1), Proposition 6.4, Corollaries 7.1/7.9 and Propositions 7.8/7.10, printed pp. 7--19; Schaefer, corrected arXiv:1507.08325v1 (2015-07-29), Theorem 2.3 with proof/local extension, pp. 6--7, Proposition 2.4 and discussion, pp. 8--9. Precise links below; audited L062 is reused.
COMPARISON: Known full-cohomology representation and injective local evaluation cover the proposed certificate format for odd p, including p>=5, without a global rational-point witness. This is method coverage, not production or guaranteed nonzero localization; generic number-field computations remain substantial.
GAP: No actual descent representative, certified number-field/local quotient computation or successful localization is supplied. D=D_div remains independent; rational membership and complex-order comparison remain unresolved.
REASON: Complete missing source coverage as a known-result import and permit a later conditional certificate specification; do not claim a successful class or new theorem.
SCOPE: Every L062/L026 premise; supplied e=0,n=1; multiplication-by-p descent using the full nonzero E[p] algebra, full-cohomology image and classical Kummer conditions. No isogeny-only, CM-only, fake quotient or deeper p^n extension is covered.

Main gap: arbitrary higher-analytic-order rank equality. Intermediate
target: the exact TARGET above, with p>=5 and every retained L026
hypothesis. Here e=0 independently supplies D=D_div; this is not inferred
from primitivity, corank two or L064's zero. Set n=1 only for this first
source comparison; deeper p^n-descent and exponent production are outside
its proposed scope.

Plausible downstream use: a successful finite localization could activate
L062 without identifying the class with a global rational point or a
prescribed prime-deletion component. Essential existing inputs are
L061/L062 and their ready coefficient/localization assessments; L024
motivates the gap but need not supply the candidate class. No
cross-notebook input is needed. Rational-direction, Sha and complex-order
limitations remain. The scalar cap stays closed.

Continue only if primary statements and essential proof cases identify a
full E[p]-cohomology representative and computable local Kummer image in
the actual point quotient, retaining kernel ambiguities and coefficient
matching. Fake-only data, requiring a global rational point, or assuming
the desired nonzero localization must be recorded as obstructions. Do not
turn algorithmic existence into a successful class. This was the startup
test; its comparison is completed below. No theorem was derived or
mathematical attempt performed. Mathlib is not checked.

## Inspected primary statements and essential cases

Schaefer--Stoll, *How to do a p-descent on an elliptic curve*, Trans. AMS
**356** (2004), 1209--1231,
[DOI 10.1090/S0002-9947-03-03366-X](https://doi.org/10.1090/S0002-9947-03-03366-X).
The text inspected is the author's
[34-page long version dated 13 June 2001](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf);
all numbering here refers to that version, not the published layout.
Read Proposition 4.6 (p. 7), Section 5/(5.1) (pp. 8--10), Proposition
6.4 and Corollary 7.1 (pp. 12--13), and Proposition 7.8, Corollary 7.9
and Proposition 7.10 (pp. 18--19). Together these give the finite Selmer
intersection, global/local injectivity, full cohomology image via scalar
and incidence-norm kernels, and local divisor evaluation. Unit/class
arithmetic and generic degree p^2-1 costs remain inputs/qualifications.

Proof cases read: Lemma 6.1's prime-to-p, normal p-Sylow and SL(2)
cases; Corollary 6.2's extension-field argument; Proposition 6.4's
fixed-point case; Lemma 7.4's two exact sequences; Lemmas 7.6--7.7's
affine-line argument, including the exceptional top monomial; and all of
Proposition 7.8's proof. Its final invariant-surjectivity check is brief
in the source. These are cited results, not independently reproved
theorems. The introduction and start of Section 8 were also inspected
for feasibility qualifications; historical practical examples do not
establish generic p>=5 feasibility today.

Followed the evaluation reference to Schaefer, *Computing a Selmer group
of a Jacobian using functions on the curve*, Math. Ann. **310** (1998),
447--471, specifically
[corrected arXiv:1507.08325v1](https://arxiv.org/pdf/1507.08325).
Read its construction and Assumptions I/II, Theorem 2.3's full proof
(pp. 6--7), its local-field extension, and Proposition 2.4 with the
supporting discussion (pp. 8--9). Evaluation equals the
Weil-pairing/Kummer composition under those assumptions. The local
multiplication-by-p quotient size is covered; retain the corrected
version, rather than importing an old general-isogeny formula.

## Applicability and comparison

The later import takes K=Q and theta=[p]; p>=5 lies within the odd-prime
scope. The origin supplies the divisor-class base point. Use the full
nonzero p-torsion scheme, for which global/local injectivity is covered,
and a finite set containing p and all bad primes. Keep unramifiedness
outside that set. No minimal-place optimization or smaller torsion
algebra is required. Rename the descent algebra: the source's A is not
L061's A=E[p^infinity] or D=Sel(Q,E[p^infinity]).

The method addresses the actual local Kummer image. Its local
injectivity is the needed coverage for a later comparison with the
identity power class. Retain both zero and nonzero outcomes. Global
nontriviality alone is insufficient. Full cohomology-image membership
and every classical local condition remain essential: no quotient by
base-field scalars, fake Selmer group or isogeny-only class substitutes
for them. Local divisor representatives do not require a global rational
point, and do not prove that the global class is rational Kummer.

This supplies coverage missing from ATTEMPTS/033's scalar reconstruction;
it does not reconstruct that route's prescribed classes. Reuse L062's
audited implication and L061's coefficient matching without another Kim
review. Preserve L014 and ATTEMPTS/021/031/032. No conclusion D=D_div,
successful localization, rational-rank improvement or complex-order
comparison follows from the descent algorithm. No advance beyond known
methods is claimed.

Continue only to a conditional import/specification with supplied exact
arithmetic evidence. Do not promise a generic implementation on an
unspecified curve. Park an instance lacking certified full-cohomology
membership, classical local membership or exact power-class separation.
A zero image is an unsuccessful witness, not selection of L061's other
branch. The original production test remains unresolved.

## Search and access record

Queries: `Schaefer Stoll How to do a p-descent on an elliptic curve local
images full Selmer group 2004 pdf`; `explicit descent elliptic curves p
Selmer injective H1 E[p] local Kummer Schaefer Stoll`; `"How to do a
p-descent" pdf Stoll`; `"Schaefer" "Stoll" "Theorem 4.8"`; and
`Schaefer "Computing a Selmer group of a Jacobian using functions" pdf
Theorem 2.3`. Explicit n-descent and second-descent results were leads
only, not inspected imports. Failed searches imply no novelty claim.

The AMS PDF and guessed short author PDF failed to open; shell DNS also
prevented downloading the long PDF. The browser supplied the long version
and corrected evaluation paper, including relevant proof ranges. This
is not SOURCE_BLOCKED. No source binary, descent calculation or
mathematical script was produced. Mathlib coverage remains not checked.
