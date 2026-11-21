# Actual Newton-moment zero-padding rank test — nomination2052

TARGET: Test rank(D_6)<=2 for D_6=H_7-diag(H_6,0) of C029m's full Jensen-weighted family by certifying the fixed principal minor on monomial indices 0,1,2 with unchanged C029n constants.
CHECKED: 2026-11-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed exact-family/consecutive-Newton/Hankel displacement searches and scoped duplicate/failure comparison in review2051, completed2052; no adequate rank-two cross-degree theorem identified. Reuse that search; no novelty inference.
SOURCE_EVIDENCE: Direct primary URLs https://arxiv.org/pdf/1609.09494v1 (Theorem2.1, Section5.2/Corollary5.4), https://arxiv.org/pdf/0912.4703v3 (Section4.1(4.1)-(4.4)), https://perso.univ-rennes1.fr/michel.coste/polyens/SAG.pdf (Exercise1.13, prior inspection reused); reuse review2051/comparison2052's primary Beckermann–Townsend (1.1)/Theorem2.1/Section5.2, Holtz–Tyaglov Section4.1(4.1)–(4.4), and review2019's fixed-size/common-Hankel qualifications; review2001/comparison2012 cover Kuznetsov finite coefficients, Coste Exercise1.13 Newton identities and Hermite interpretation. C029n/audit2012 and C029q/audit2024 supply the unchanged certified constants and degree6/7 inputs.
COMPARISON: This fixes zero-padding in monomial Newton-sum coordinates, distinct from C029q's affine-quotient multiplication of descending-basis derivative Bezoutians. Standard displacement rank, positive definite Hankel approximation and one-polynomial rank formulas give no bound for this changing-degree difference. Direct finite coefficient certification is therefore necessary to test the ansatz.
GAP: The fixed minor has not been calculated. No rank-two identity or relative sign control is known. Even an exact zero minor proves no rank upper bound; initialization, singular/degree-drop cases, eventual uniformity and C029m's index premise remain open.
REASON: A single preselected minor gives a bounded, independently checkable necessary-condition test for a coefficient-defined low-dimensional evolution mechanism, without fitted embeddings or repeating an endpoint signature. Separate literature approval and direct-URL repair completed in step2053; no calculation performed in either literature turn.
SCOPE: Only N=6,7; all odd coefficients retained; unchanged exact constants; fixed principal index set {0,1,2}; no degree/precision sweep, fitted normalization or root estimates. Reuse the source coverage in drafts/literature/2026-11-21-consecutive-hermite-displacement-review-2051.md.

## Intended finite attempt after separate approval

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
Intermediate target: determine whether the rank-two necessary condition
survives this one fixed inter-degree minor test. Plausible use: a small
coefficient-defined update could help describe changes of negative
directions towards C029m, provided independent signs and uniformity
were later supplied. This attempt supplies neither of those premises.

Use exactly T_N and the multiplicity-aware H_N of C029m/C029l.
Reconstruct U_6,U_7=T_N/S using C029q's finite formulas and each
degree's own Jensen weights; verify coefficient identities and leading
coefficient separation against C029n/C029q. S is the same positive
constant in both inputs, and root moments may be obtained from U_N.
Do not identify the derivative Bezoutian's entries with Newton sums.
Use the Newton identities covered by review2001 (Coste Exercise1.13),
with the two cases k<=degree and k>degree handled correctly. Division
by a leading coefficient requires its certified separation from zero.
Use s_(6,0)=6 and s_(7,0)=7, counting algebraic multiplicities; root
approximation and simplicity are unnecessary.

Save the full coefficient specification, degree evidence, unchanged
constant enclosures, s_(6,0),...,s_(6,10) and
s_(7,0),...,s_(7,12), both Hermite matrices and their zero-padded
difference. The selected minor uses rows and columns 0,1,2 only;
fix these indices before any sign inspection. Evaluate its determinant
using all six signed permutation products with exact rational interval
operations, including interval division only by separated denominators.
Retain full endpoints and all failure conditions on disk. Print only
the resulting enclosure, the required exclusion of zero, actual degree
checks, failures and artifact paths. No floating signature is evidence.

Continue/abandonment test: a determinant enclosure excluding zero
rejects rank(D_6)<=2 and stops this prescribed rank-two ansatz at the
pair. It does not reject eventual-only variants, C029m or RH. An
enclosure containing zero is inconclusive, including an exact-zero
minor; stop and retain the reasoning without checking more minors or
raising degree/precision automatically. A genuine rank<=2 certificate
would need independent evidence, outside this single-minor attempt.
Any later signed propagation mechanism requires its own source review.

Essential inputs: C029m (exact family/conditional eventual index),
C029l (actual-degree Newton-sum convention), C029n (constants),
C029q (full coefficient formulas and degree6/7), C029p (degree-six
inertia contrast only). C029q/r/v and stops2042/2044/2047 are preserved.
C029w is not the weighted H_6. No cross-notebook theorem is needed.
Weighted convergence/upstream[9] and Xi transfer are unused by the
finite rank test and remain qualified for any future RH application.
Mathlib matching coverage is unchecked. No reproof of standard rank,
Newton or root-count theorems is proposed. A finite specialization
must be reported as such, with no assertion of certified originality.

## Separate source approval and URL repair — step2053

21 November 2026. The exact TARGET, constants, index set and failure
policy above are unchanged. This is a process repair, not new mathematics
or a new search result. Reuse review2051 and reviews2001/2012/2019;
their duplicate and failure comparisons remain applicable.

Direct primary references are now present in this assessment itself:

- Beckermann–Townsend, [arXiv:1609.09494v1](https://arxiv.org/pdf/1609.09494v1),
  29 September 2016, (1.1), Theorem2.1 printed pp4–5 and Section5.2/
  Corollary5.4 pp17–18. Reaccessed the statement and Hankel scope:
  normal operator matrices and prescribed displacement factorization
  yield singular-value bounds; the Hankel corollary assumes positive
  definiteness and gives approximation bounds. These do not certify
  exact rank for the cross-degree difference. The full proof inspection
  in review2051 is reused; Lemma5.3 is not imported.
- Holtz–Tyaglov, [arXiv:0912.4703v3](https://arxiv.org/pdf/0912.4703v3),
  uploaded 9 March 2011 (internal revision 9 February 2011), Section4.1,
  (4.1)–(4.4), printed pp66–67. Reaccessed the real degree-n hypothesis,
  positive leading coefficient, logarithmic derivative and multiplicity
  formula. These concern one polynomial, not an inter-degree rank bound.
- Coste, *An Introduction to Semialgebraic Geometry*, October 2002,
  [author PDF](https://perso.univ-rennes1.fr/michel.coste/polyens/SAG.pdf),
  Section1.4.1 pp17–18, Exercise1.13/Theorem1.14. Today's reaccess timed
  out; reuse review2001's actual inspection of Newton identities and
  repeated-root conventions. No new Coste inspection is claimed.
- Kuznetsov, *Expansion of the Riemann Xi function in Meixner–Pollaczek
  polynomials*, Canadian Mathematical Bulletin 51 (2008), 561–569,
  [publisher DOI](https://doi.org/10.4153/CMB-2008-055-0).
  Reuse reviews2001/2019's finite-coefficient inspection, not a fresh
  retrieval or an unconditional weighted-convergence claim.

Approval remains EXPLORE for only the finite minor certificate.
No essential coverage has changed; the isolated failed Coste reaccess
is not an essential source blocker because inspected coverage is retained.
No derivation, lemma or mathematical script was made. Mathlib matching
coverage remains unchecked. No progress beyond the checked sources is claimed.
