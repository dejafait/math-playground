# Fixed theta=0 Hermite certificate — work2049

Approved target: certify the Hermite negative index of P_{6,0} using
the unchanged C029n enclosures; assessment2048 is SPECIALIZE and was
saved before this invocation. Main gap is L030-L032/C032a actual-Xi
mixed positivity; C029m's eventual index premise is also unpaid.

Use P_{6,0}/S=sum_(k=0)^6 q_k p_k, with all weights one, all odd
coefficients retained, and S=sin(pi/8)/sqrt(2)>0. C029n supplies exact
coefficient formulas and audited 60-decimal Machin/isqrt input intervals;
C029l supplies the multiplicity-aware Hermite interpretation. Reuse
Coste Exercise1.13 and p19 Jacobi as recorded in review2001; Rump's
enclosing operations, including nonzero-divisor requirement, are covered
by assessment2048. No source refresh or mathematical expansion of scope.

Plan: reconstruct all exact coefficients and the rational basis recurrence,
compare q_k with the pinned C029n certificate, enclose the monomial
coefficients, certify the leading coefficient, normalize, compute Newton
sums s_0,...,s_10 in both degree ranges, and form H=(s_(i+j))_(0<=i,j<6).
Use literal finite Leibniz sums for all six leading minors. Save all terms,
intervals, input hashes, checks and failures in scripts/pollaczek/.

Discriminator: every minor must exclude zero before Jacobi is applied.
Index>=2 rejects only the proposed whole-path ceiling; <=1 is a finite
pass; unresolved signs are inconclusive. Stop after this fixed test and
necessary correctness checks; no precision/parameter/degree campaign.
Whole-path multiplicities, varying-N initialization, eventual uniformity,
qualified weighted convergence/upstream[9] and actual-Xi positivity remain
open. Prior stop2042/2044 and C029q/r/v are contrasts, not premises.

Completed: [C029w](../lemmas/C029w-undamped-pollaczek-sixth-hermite-index.md)
records degree six, strict determinant signs (+,+,+,-,-,-), inertia
(5,1,0), four simple real roots and one simple conjugate pair. This is
a finite known-method pass only, not a whole-path or eventual bound.
The calculation's 28 checks and the separate stored-sum integrity check's
34 checks pass. Full coefficients, all Newton sums, all 873 determinant
terms and exact endpoints are retained in
`scripts/pollaczek/jensen-zero-endpoint-2049.json`; no precision change,
runtime installation or additional parameter/degree was attempted.
Full source/Newton/product independent audit is the nominated continuation,
with its newly saved readiness subject to separate supervisor approval.
No RH candidate; Mathlib unchecked.
