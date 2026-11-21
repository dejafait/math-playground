# Complete-support centred moment — independent audit coverage

TARGET: Independently audit and reproduce Planat–Raymond v1 Theorem 3.3's complete-support bound M32<81/4 on its full closed parameter rectangle and all 151 index leaves.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step135's completed exact-filename/source comparison in drafts/literature/2026-11-10-complete-support-centred-moment-134.md; the target and assumptions are unchanged from its proposed audit. Scoped searches found no completed local moment replay; no novelty claim.
SOURCE_EVIDENCE: Planat–Raymond arXiv:2611.06245v1, 4 November2026, Section3.8.1 Theorem3.3 full statement/proof and Section3.9; complete core/analytic/check_centred_moment_01568.py at commit18dbc01ea36bf9a24d8f79822b5ce06b545e4ace; associated version/hash/environment metadata and official python-flint0.9.0 arithmetic/comparison/serialization documentation inspected in step135.
COMPARISON: The source states exactly the required premise; reproduce and audit its finite proof rather than claiming a stronger theorem. Independent implementation/examination is justified by its unrefereed computer-assisted status; no full release, Gram construction or Newman theorem is needed.
GAP: Independently justify the source reduction and obtain fresh directed certificates for every closed leaf, including natural support, coefficient comparison, tail monotonicity and antiderivative evaluation; verify all individual strict bounds instead of a midpoint-selected maximum.
REASON: Essential executable coverage is now available, and a bounded independent reproduction can discharge one explicit L960 premise. This newly prepared ready assessment requires separate approval next turn before mathematical work.
SCOPE: Only Theorem3.3 with the exact domain and formulas below; no other analytic bound, stability theorem, lower heat endpoint or global transfer is covered.

## Exact domain and source locators

Let a=98/625, T=1/5, X=6000000185827, Wg=120000000000000,
C=690988, H=3100000, K=128 and kappa=log32. For a<=t<=T,
X<=x<=Wg use N=floor(sqrt(x/(4*pi)+t/16)), with the right natural
index at exact walls. The target is the complete sum

    sum_(n=1)^N exp(t*log(n)^2/4-(1/2+t*c_pol(x))*log(n))*|log(n/32)| <81/4,
    c_pol(x)=log(sqrt(1+x^2)/(4*pi))/4-1/(2*(1+x^2)).

Primary [Theorem3.3 and proof](https://arxiv.org/html/2611.06245v1#S3),
[complete pinned checker](https://raw.githubusercontent.com/Dale-Dug/planat-raymond-collision-exclusion-0156821/18dbc01ea36bf9a24d8f79822b5ce06b545e4ace/core/analytic/check_centred_moment_01568.py),
[official arithmetic semantics](https://python-flint.readthedocs.io/en/stable/general.html#inexact-numbers-and-numerical-evaluation).
The completed step135 assessment gives the full case map, provenance and
access qualifications; its hash declarations have not been checked locally.

## Bounded audit contract, not a proved result

1. Audit the source's c_pol monotonicity and both natural-index wall
   implications. Rebuild the exact integer endpoint recurrence starting at C,
   repeatedly min(H,floor(101*n/100)); certify151 adjacent closed leaves,
   their union and terminal H. Handle N equal to either leaf wall explicitly.
2. Use x_L=X on the first leaf and 4*pi*(L^2-T/16) thereafter. Justify
   x>=x_L and the source's coefficientwise heat/spatial comparison for
   every n<=N, including n=1. Certify x_L>=X and logU<4*c_pol(x_L).
3. Independently check the source's convex derivative quadratic and both
   endpoint signs, the decreasing-tail comparison from128 toU and extension
   beyond N. Include the complete128-term prefix and exact zero at n=32.
4. Verify the displayed erfi antiderivative before using it. Preserve the
   source's B=sigma_L-1, E, I and J conventions recorded in step135; no
   quadrature samples or unproved cancellation replace interval enclosures.
5. Produce fresh Arb evidence at192 bits, with a256-bit replay if useful
   for checking sensitivity to the cancellation. Retain exact input values,
   every leaf's endpoints, enclosures, required bounds and failures. Verify
   the eight global and six per-leaf gate families and the claimed914 count.
   Counts and PASS strings alone never establish a gate. Check every leaf's
   upper bound<81/4; compute the maximum of certified upper endpoints, not
   the author's midpoint-selected display. Record actual library versions.

Use an explicitly labelled independent implementation if literal source
bytes cannot be downloaded; do not claim a byte-identical or hash-verified
replay in that case. The complete source text has been inspected, so no
new literature search is required for this same target. A local executable
may be written only after approval, and all certificates must stay in the
active notebook. No API key, shared-infrastructure edit or full-release
execution is authorized by this contract.

Continue on complete analytic and directed-arithmetic success; fail or
narrow the reproduction on a false reduction, omitted wall/support term,
failed/indeterminate inequality or unresolvable implementation issue. A
successful result is KNOWN reproduction of the cited bound, not a new
mathematical discovery. A genuinely unavailable arithmetic dependency is
a blocker, not a passing numerical experiment.

L960 is the conditional consumer; L019/L058 fix its eventual normalization,
not the proof of this moment estimate. Even a pass leaves its local
remainder/derivative, companion, phase/support and complete stable-model
premises independent, as well as initialization, seams, infinite exterior,
zero time and L030–L032/C032a positivity. Mathlib full coverage is not
checked. No cross-notebook input. Proposed task: proof_audit/routine_audit,
standard/high, REPRODUCTION; this is elementary reduction and finite
directed replay rather than a new mechanism at the central RH gap.
