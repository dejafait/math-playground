# One real odd carrier obstruction test — source-gate approved specialization

TARGET: Test the 3/2 joint arithmetic bound on C759a's fixed W using a phase-recurrent real odd sine carrier, exact projection off modes1..120, and a rigorously evaluated constant-envelope comparison; stop after this one obstruction test.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step796's completed joint-prime comparison795, including exact-target searches, L743 overlap, the neutral-prime-only stop and the distinct separated-cell/source-scope failures. No exact real-odd120-mode result was located; no originality claim.
SOURCE_EVIDENCE: Clark, 159-page author PDF https://plclark.github.io/PeteLClark/Expositions/geometryofnumbers.pdf#page=72, Theorem13.3/Corollary13.4 p72; Fillmore-Stampfli-Williams, Acta Sci.Math.33(1972), https://acta.bibl.u-szeged.hu/14354/1/math_033_fasc_003_004_179-192.pdf#page=10, Theorem5.1/Corollary pp188-189; both directly retrieved 2026-11-13; standard named Riemann-Lebesgue lemma; L743 Sections1-2 and C759a Sections1-3 supply local scope.
COMPARISON: Finite-delay recurrence and bounded quadratic-form continuity are covered. L743's complex cell-neutral equality does not apply directly to real odd W. Develop only the sine-carrier, exact finite projection and fixed scalar comparison needed for this diagnostic; do not reprove approximation or numerical-range theory.
GAP: Prove or refute that the proposed sequence in W has arithmetic Rayleigh values approaching the constant-even-envelope value, and rigorously compare that value to3/2. No sequence limit, scalar formula, inequality or attained extremum is asserted by this assessment.
REASON: Test a specific finite-codimension obstruction before spending work on a joint upper certificate, with no source blocker. This is an established-mechanism specialization/REPRODUCTION, not a creative central-gap mechanism. Separate literature approval completed in step797; direct primary URLs and cited scopes checked without deriving the proposed specialization.
SCOPE: Only A on real L2(-1,1), W odd orthogonal to sin(pi*j*x),1<=j<=120, all n=2,3,4,5,7; one constant even envelope and one recurrent sine-carrier/projection family. No cutoff/envelope search, exact supremum theorem, neutrality, full Q sign or RH consequence.

## Exact bounded mathematical proposal, not a derived result

Take C759a's zero-extended shifts and
A=sum_n (Lambda(n)/sqrt(n))(T_log(n)+T_log(n)^*),
n=2,3,4,5,7. Write P for the L2 projection onto the first120
odd sine modes and f0(x)=1/sqrt2 on(-1,1), zero outside.
The proposed tests are
u_t(x)=(I-P)[f0(x)sin(tx)], normalized only when nonzero.
Use simultaneous returns t tending to infinity for all five phases;
do not choose or numerically hunt a return frequency.

The single test is whether the normalized arithmetic Rayleigh values
of this family approach <A f0,f0>, and whether that scalar is strictly
greater than3/2. Both are questions for the later attempt. No scalar
formula or numerical enclosure was derived in the nomination turn.
Keep the oscillatory norm factor and both adjoint terms;
prime-power4 has coefficient log(2)/2, not log(4)/2. Retain actual
zero-extension overlap lengths; periodic shifts would change A.

Check real odd parity, exact membership in W, nonzero normalization
and vanishing finite projection errors. Every Riemann-Lebesgue use
needs an L1 integrand on its actual overlap. Use L743's finite-list
recurrence argument as a tool, not its cell-neutral equality at a
different length. The constant envelope with endpoint jumps is an
L2 arithmetic test; if relevance to C759a's form domain is asserted,
verify logarithmic Fourier integrability after modulation/projection
using C759a's domain description. No complete energy is asserted to
remain bounded along this sequence.

If both limit and strict comparison hold, conclude only that3/2 is
not an upper bound on this fixed W, with a rigorous strict margin or
eventual witness. If either fails or the scalar does not exceed3/2,
preserve the exact failure and stop this family; failure does not prove
the upper bound. No higher cutoff, different envelope or complete-Q
conjecture is authorized in this attempt. Success would delimit a
proposed replacement for C759a's arithmetic cost, not exclude joint
arithmetic/archimedean estimates or parity ordering.

Essential local inputs: C759a for the split/domain; L743's bounded-form
and finite-delay tools; L744(6) for the downstream sign convention.
L741's normalization is restated there. No RH, source positivity
computation, neutral-cell conclusion or cross-notebook input is used.
Remaining main-gap assumptions: complete odd lower floor, coupling/
Schur sign, even simplicity/sign, Xi realization with multiplicities
and shifted/global actual-Xi mixed positivity.

Primary URLs appear directly in SOURCE_EVIDENCE above; comparison795
retains the earlier search record and inspected proof cases. Full
matching Mathlib coverage is not checked. Canonical proofs/citations
belong in a lemma only after an approved research turn establishes a
result; this file is no proof.

## Separate source-gate approval — 13 November 2026, step797

LITERATURE_REASON: Supervisor recovery identified missing direct source
URLs in this ready assessment. This bounded source check repairs that
omission, reusing comparison795 rather than repeating discovery.

Opened both primary PDFs at the direct URLs above. Clark's current
159-page file, printed p72 (PDF page72), states Theorem13.3 for real
linear forms and Corollary13.4 for any finite real list and integer
M>1, with a positive integer denominator below M and simultaneous
nearest-integer errors at most M^(-1/d). No independence assumption
appears. Its proof invokes Minkowski's linear-forms theorem and leaves
details to the reader. Import that theorem; reuse L743 Section2's
already written bounded/unbounded denominator cases rather than
reproving approximation. This review establishes no carrier limit.

Fillmore--Stampfli--Williams, pp179,187-189 (PDF pages1,9-11), specifies
a bounded operator on a complex separable infinite-dimensional Hilbert
space. Theorem5.1 and its corollary characterize essential numerical
range by weakly-null unit sequences and limiting Rayleigh values.
Read the finite-rank compression implication and the orthonormal
subsequence/Hilbert--Schmidt compression proof case. These are
qualitative supporting results; they neither select the scalar nor
provide real odd vectors. Direct finite projection remains the planned
specialization, not a new proof of this abstract theorem.

The reused standard named Riemann--Lebesgue lemma requires L1
integrands. Its overlap hypotheses, parity, normalization, projection
errors and weighted form-domain application remain obligations for
the next research turn. Rechecked C759a's fixed real odd W and domain
description, L743 Sections1-2, and the recorded neutral-prime-only
stop. That stop is on a different complex cell-neutral space and
does not settle this test. No new duplicate search or novelty claim.

Approval: SPECIALIZE remains adequate for the exact unchanged TARGET.
This is a process repair, with no new mathematical evidence and no
progress beyond inspected sources. No lemma, mathematical script,
PROOF or DAG change is warranted. The single-test stopping rule above
remains binding.
