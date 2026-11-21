# Exact log-height packet: analytic compatibility coverage

TARGET: Test whether, for fixed a,h>0, W_(a,h)(z)=exp(-(Log z-log a)^2/(2h^2)) can agree on a real open interval containing a with any function holomorphic on |Im z|<1/2+epsilon for some epsilon>0.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The step-353 paid-packet review checked exact log-height/lognormal test terminology, analytic extension and local duplicates; no inspected theorem states this exact specialization. Reuse that bounded review, without an originality claim.
SOURCE_EVIDENCE: Direct primary URLs verified 2026-11-04: https://dlmf.nist.gov/4.2.i (4.2.1--4.2.6); https://dlmf.nist.gov/1.10 (i--ii); https://warwick.ac.uk/fac/sci/maths/people/staff/peter_topping/teaching/ma3b8_cplxanal_24_07_29.pdf (29 July 2024, Theorems 7.3--7.5 and complete proofs, printed pp.67--69); https://arxiv.org/html/2403.17803v1#S2.SS2 (26 March 2024, Section 2.2 Lemma 4).
COMPARISON: Standard analytic uniqueness and finite-order factorization cover the necessary tools; the explicit formula fixes the full-strip requirement. The composition-specific applicability calculation remains separate and must not be inferred just from Log's branch cut.
GAP: No extension or impossibility proof has been supplied. Check connected-overlap uniqueness and the real-axis behavior toward zero against both the finite-order and identically-zero analytic cases.
REASON: The full paid packet lacks an admissible global test. A single routine compatibility calculation can decide this necessary prerequisite before any sign or cost research; direct primary links and essential theorem scope have now been rechecked in a separate literature-only recovery turn; the mathematical specialization remains unperformed.
SCOPE: Fixed finite positive a,h, the principal logarithm on Re z>0, exact agreement on an interval inside (0,infinity), and the stated full horizontal strip. No approximating tests, parameter limits, shifts, cutoffs, Mellin superpositions, sign claims or arithmetic estimates.

The main gap is actual-Xi all-degree mixed positivity. This modest
intermediate target could close the exact packet's admissibility gap
or exclude its proposed full-strip implementation. It supplies no
positivity and is not a new central mechanism or claimed new theorem.

The primary citations, versions and reads are recorded in
`2026-11-04-log-height-gaussian-paid-packet.md`. Import identity and
zero-order theorems by citation; do not reprove them. Apply uniqueness
on a connected domain where both functions are holomorphic, keeping
zero as an interior point only of the proposed extension's domain.
The needed parameter-specific asymptotic comparison is the reason
for a specialization rather than claiming the literature states W's
answer verbatim. No such comparison was performed in the source turn.

Discriminator: either exhibit an extension satisfying the exact
agreement or prove nonexistence for all fixed a,h>0, including any
apparently exceptional values. A branch-cut assertion or numerical
plot is insufficient. If nonexistence holds, stop this exact packet
implementation and preserve the obstruction. If existence holds, record
it as a prerequisite only: full decay, both pole values, all-frequency
coverage, baseline, complete complementary-zero remainder and prime/
archimedean/contour costs remain unresolved and unapproved. Changed
or approximate packets require their own assessment.

L018 sets the Xi coordinates and L757 motivated the packet, but neither
is a mathematical input to this purely analytic compatibility test.
L753/C753a and L754 are contrasts only. No RH, spacing, simplicity,
zero-free extension or actual off-line zero is assumed. Mathlib matching
coverage has not been checked; unknown availability is not absence.

## Direct-source recovery — step 354

LITERATURE_REASON: Repair the supervisor-reported missing direct source URLs in this ready assessment; preserve its exact target and reuse step 353's overlap search.

All four primary URLs in SOURCE_EVIDENCE were opened successfully on
4 November 2026. DLMF 4.2(i) gives the principal logarithm on the slit
plane, real on the positive axis; 1.10(i)--(ii) gives Taylor expansion
and continuation. The connected-domain formulation below governs use.

Topping's printed pp.67--69 (PDF pages 67--69, zero-based 66--68)
were inspected through the complete proofs of Theorems 7.3--7.5.
Theorem 7.3 assumes a finite-order zero of a holomorphic function on
an open set and factors out its order with a locally nonzero factor.
Theorem 7.4 requires a connected open set and an interior infinite-order
zero to conclude identical vanishing. Theorem 7.5 requires two
holomorphic functions on a connected open set and agreement accumulating
inside it. Its proof uses the preceding two results. No boundary
accumulation suffices. These are cited inputs, not results to reprove.

Carneiro--Milinovich v1 Lemma 4 and its proof referral were rechecked:
analyticity in the full closed strip of half-width 1/2+epsilon and
power decay of order 1+delta, with epsilon,delta>0, precede its complete
zero/pole/prime formula. The proof cites Iwaniec--Kowalski Theorem 5.12;
that book proof was not newly inspected. Only the stated admissibility
requirement motivates this test; the explicit formula is not needed
to decide the purely analytic extension question. Adjacent RH-dependent
Lemma 5 is excluded.

The assessment remains SPECIALIZE. This repairs access/citation metadata
and confirms tool scope, without supplying the packet's asymptotic
comparison, a new obstruction, or progress beyond the checked sources.
No new duplicate search is needed for the unchanged target; step 353's
recorded failures remain in force. No lemmas or mathematical scripts
were changed. Full matching Mathlib coverage remains unchecked.
