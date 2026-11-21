# Actual Laplace interpolation nonsingularity — review1838 of nomination1837

TARGET: Review primary criteria for nonsingularity of C033w's matrix with columns (1,k(1,sigma),k(2,sigma)) at sigma=1,3/2,2, comparing actual-kernel hypotheses with C033g and the recorded determinant stops; identify one independently testable sufficient condition or park this mechanism.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed bounded exact-expression/Chebyshev/Laplace/TP search and narrow C033w/l,C032m/n,C033g/k and stops1746/1798/1837 comparison in drafts/literature/2026-11-20-laplace-interpolation-source-notes-1838.md; no matching actual-kernel nonsingularity theorem located, with no novelty inference.
SOURCE_EVIDENCE: Reused1797's Rump Section10.3 Theorem10.2/(10.8)-(10.9), https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf ; reopened Novaes--Torregrosa UAB July2015 printed p2 all-prefix criterion and Section2 pp5-6 (5)-(9)/nonvanishing proof, https://mat.uab.cat/dpt/Publ/prep/p13_15.pdf ; reused1745's de Boor pp58-64, reopening Proposition43/(45), https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf ; reused1709/1745's primary TP comparisons as detailed in source-notes1838.
COMPARISON: C^2 real width functions with every prefix Wronskian nonzero on [1,2] satisfy the known ECT criterion; that is one sufficient test for this interpolation matrix, not verified here. Odd-kernel signs, fixed-K Hankel positivity, law positivity and conditional numerical residual bounds do not establish its hypotheses.
GAP: The source comparison is complete; actual C^2 specialization and both nonconstant prefix tests remain unpaid mathematical obligations. No determinant sign/value, conditioning, exact weights, TV or actual-Xi conclusion follows.
REASON: Known ECT theory supplies a testable conditional framework and no essential source blocker remains. One separate, newly nominated analytic application uses C032n's normalized heat evolution; assessment1838 awaits separate approval. No mathematics was derived in this review.
LITERATURE_REASON: The next target changes from finite interval arithmetic to analytic nonsingularity of an actual Laplace-kernel matrix;1809/1836 enclosure coverage and1797's numerical solve theorem do not cover the changed hypotheses.

## Completed review1838

The full source statements, relevant proof case, applicability comparison,
queries, retained qualifications and limitations are in
[source-notes1838](2026-11-20-laplace-interpolation-source-notes-1838.md).
Use all prefix Wronskians, not only the last one. The review nominates
an analytic hypothesis test, without deriving it or approving it for
execution in this literature turn. A prefix zero defeats that sufficient
criterion, not necessarily the fixed matrix. PROGRESS.md is the sole
current next-action record.

## Preserved nomination1837 below

The following text records the original, then-incomplete nomination;
its source-readiness status is superseded by the fields and review above.

## Exact scope and relevance

Use C033w's qualified k(s,sigma)=exp(-B_sigma(s)), with its actual
full divisor and probability-law interpretation, on s,sigma in[1,2].
Define only the prospective test matrix M whose three columns are
(1,k(1,sigma),k(2,sigma)) for sigma=1,3/2,2 in that order. The proposed
later mathematical target is det M!=0. No sign or magnitude is claimed.
This could remove the singularity gap for the mass-one, two-observation
interpolation problem1796 independently of the scalar construction.
It would still leave entry accuracy, quantitative conditioning, the
right-hand side m, exact weights, TV<=2 and full-interval observations
unresolved. Main gap remains L030-L032/C032a actual-Xi positivity.

Read the exact primary hypotheses and essential proof cases needed for
this matrix; reuse adequate source records first. Identify whether an
applicable criterion needs monotonic ratios, derivative signs, all-prefix
Wronskians or other conditions, without assuming any of them. Record
the actual kernel-specific obligations precisely. This review may select
one bounded later application only after the exact theorem scope and
known failures have been compared. If no distinct condition is justified,
park it. Do not run a determinant experiment or derive a new identity
during the source turn. No automatic sign transfer through exponentiation,
smoothing or Laplace transformation is allowed.

## Duplicate and failure boundary

The local records checked distinguish the objects despite their shared
letter k. The1745 normalized three-width test concerned the odd kernel
at y=1/8,3/16,1/4 and all coalescing widths. Its1746 enclosure[-3,3]
lost signed correlation, remained inconclusive and was parked. The next
review must preserve that obstruction and check for any applicable
stronger prior result; changing notation or grid density is not a
reopening idea. C033g's first ratio does not provide this Laplace matrix.
Rump1797 requires a verified numerical norm residual; no entries or such
residual are available. C033x/1798 stopped a particular scalar-generation
schedule, not the existence of this matrix or its inverse.

The completed C034a audit1837 is a valid local arithmetic result, not a
sign-regularity input. No second W=2 replay or global-ledger adjustment
is the proposed continuation. This nomination is not a completed source
assessment and authorizes no research until a separate review is ready.

Essential local inputs for that review are C033w/l, C032m for the exact
transform definitions, C033g/k for comparison only, sources1797/1745
and stops1746/1798/1837. The right-hand side m is context, not an input
to the determinant. Retain actual divisor/conjugation/multiplicity,
ordinate0 exclusion, strict strip and gamma>14, counting, through100
and retained real zero, reciprocal-square tail, heat positivity and
separate fixed-j errors, both fixed-v1 qualifications, zero drift/killing
and Gaussian half-variance. Full source-wide and finite-zero validity
remain unverified; full matching Mathlib coverage is unchecked/unknown.
No central creative mechanism or completed RH candidate is nominated.
