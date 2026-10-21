# Two fixed separators on the same column family — finite specialization approved

TARGET: Determine whether L078's and L080's separator inequalities admit a common point in L076's nonnegative four-parameter column family.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 283 searched the author-site convex feasibility/quadratic/KKT terminology and two-quadratic S-procedure leads; inspected the primary slides passages below and local L076,L078,L079,L080 hypotheses and ATTEMPTS/061–062. No inspected source supplies this prescribed-data intersection verdict.
SOURCE_EVIDENCE: Reuse foundations/04,09,10,12 and the ready L079/L080 assessments. Fresh primary reading: Boyd–Vandenberghe–Nobel revised 402-page author slides, PDF pp.108,157,174–175,186–187,372–373; QCQP statement, dual lower-bound proof, KKT sufficiency, feasibility alternative and phase-I boundary case.
COMPARISON: Known finite quadratic feasibility and sufficient certificate methods cover the proposed test after exact coefficient, curvature and domain checks; neither a one-weight maximum nor either fixed-point rejection decides the common intersection. No general exact SDP alternative is imported.
GAP: Assemble the second unchanged family pairing and test both necessary inequalities on the identical original four-parameter nonnegative domain; require an exact common witness or a global certificate covering every point.
REASON: Changed joint-feasibility scope is now compared with inspected primary statements; existing decomposition/range coverage is reusable. The sources supply methods, not this coefficient-specific verdict, so a finite specialization remains necessary.
SCOPE: Original L021/L053 pairs and rho; L073/L075 dictionary; L076 affine family; L078 and L080 exact unchanged dual weights. No scalar upper rows, other-anchor matrices, alternate dual search, retuned base, signed completion or RS claim.

The main gap is arbitrary-center 67/68 safety; the bracket stays 955–957.
This target changes the test from another single-column completion or
single-weight maximum to simultaneous compatibility of two existing
necessary separator inequalities. It must retain L079's positive
old-weight maximum and L080's rejection of its chosen attaining point;
neither result licenses an answer to the new test.

Essential inputs: L021,L053,L073,L075,L076,L078,L079,L080 and their
canonical certificates. The new second pairing has not been assembled.
Reuse the reviewed full-key domain, singular-range and coherent
normalization contracts only within their exact hypotheses. A point
passing both inequalities would remain only a necessary-condition witness,
not a simultaneous PSD completion. A family rejection would require
rigorous exclusion of every domain point, not numerical search failure.

Downstream use: a rigorous incompatibility verdict could exclude this
entire prescribed column family; a common admissible witness would show
that these two separators alone are insufficient and identify a distinct
column for a separately assessed completion test. Continue with the approved bounded test below, seeking a concrete exact
witness or global certificate.
If the joint test remains inconclusive, record that limit rather than
repeat rejected point choices. Preserve ATTEMPTS/060–062. Other pair/base
moments, actual-label constraints, global extension and RS realization
remain independent unresolved gaps. Full Mathlib coverage is not checked.


## Step 283 source comparison and bounded application contract

LITERATURE_REASON: The joint intersection was outside the previous single-weight and fixed-point assessments; essential quadratic-feasibility scope required approval, not another review of unchanged decomposition coverage.

Stephen Boyd and Lieven Vandenberghe, revised slides with Parth Nobel,
*Convex Optimization*, [author PDF](https://stanford.edu/~boyd/cvxbook/bv_cvxslides.pdf),
402 pages, retrieved 17 October 2026; revision date unasserted. Read PDF
p.108/slide 4.21 (QCQP), p.157/slide 5.2 (complete dual lower-bound
proof), pp.174–175/slides 5.19–5.20 (KKT and sufficiency), pp.186–187/
slides 5.32–5.33 (feasibility and dual alternative), pp.372–373/slides
11.19–11.20 (phase I). PSD quadratic Hessians permit convex quadratic
constraints; singular curvature is allowed. A strictly positive dual
lower bound certifies infeasibility without a constraint qualification.
KKT sufficiency assumes convexity; the converse needs Slater. A zero
phase-I optimum is ambiguous. No attainment or strict feasibility of
this notebook instance follows. These passages cover certificate methods,
not its coefficients.

Searches: `site.web.stanford.edu boyd convex optimization convex feasibility
quadratic inequalities KKT sufficient`; `"quadratic" "S-procedure" "two"
inequalities Boyd convex optimization`. The book Appendix B.2 appeared
as a lead, but its PDF timed out and was not inspected. It is not imported:
no lossless S-procedure with additional domain inequalities is needed.
The web.stanford.edu slides URL also timed out; the stanford.edu author
URL supplied the complete relevant text. No essential source blocker remains.
No novelty inference follows from these searches.

Reused primary imports retain their precise scope: Schrijver (2005),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64)
for the finite mode algebra (foundations/04,09); Sano (2026), Section 2,
Corollary 2.2 and Theorem 2.6 for singular Schur ranges (foundations/10);
Polak arXiv:1703.05171v1 Sections 1.1–1.2 with the recorded constant-weight
qualification (foundations/12); Goemans Lecture 3 (19 September 2001),
Theorems 1 and 3 for affine nonnegative separation (foundations/10).
The previously approved family and critical-audit assessments record their
primary proof inspections; no fresh inspection of these sources is claimed.

The later research step must use exactly t=(t56,t63,t69,t78) and the
85 inequalities c+A*t>=0. It must reconstruct both original 81-weight
vectors, and the common 81 right-side functions, retaining all forced
entries and the full anchor/range costs. The new L080-weight family
pairing has not been assembled or evaluated in this review. Check its
coefficients and any claimed curvature exactly before using convex QCQP
or KKT arguments. A pointwise witness does not require an optimization
existence theorem. For infeasibility, supply an explicit globally valid
bound or sufficient dual certificate in the original coordinates; do
not assume certificate necessity or rational witness existence. Numerical
proposals may guide work but must be replaced by exact evidence.

Retain L079's family-wide full-key/range identities only under its
unchanged pairs/base and domain. Both nonnegative-moment residual signs
remain essential. Common feasibility concerns two necessary inequalities
only, not the full 81-mode completion. Incompatibility must cover the
whole four-dimensional domain, including its boundary and unbounded
possibilities, unless boundedness is separately proved. An inconclusive
bounded search records EXPLORATION and the actual obstruction; it cannot
license another claimed rejection of the family. No new alternate dual,
scalar upper rows, anchor test or retuning is approved here.

No lemmas or mathematical programs were changed. Full matching Mathlib
coverage for this prescribed intersection or its convex certificate
methods is not checked; no absence claim is made.
