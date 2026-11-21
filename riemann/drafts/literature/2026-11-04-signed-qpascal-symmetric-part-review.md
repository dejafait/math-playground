# Signed matrix comparison at the exceptional diagonal — source review

TARGET: Assess whether the symmetric part of the q-Pascal-normalized actual-Xi coefficient Toeplitz matrix can certify D_(r,r-1)>0, comparing precise source hypotheses and the L765 norm obstruction, and nominate one bounded signed quadratic-form test.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step414 searched exact symmetric-part/accretivity, q-Pascal/Toeplitz/Xi and Ostrowski-Taussky statements, plus local literature/ATTEMPTS/history for these terms and 2601.18977; no earlier matching signed test was found. Reused step385/387/388 coverage and step407's condensation/multiplier stop; no novelty inference.
SOURCE_EVIDENCE: Inspected Michałowski 2607.16795v1 (2),(3), Theorem1.1, Lemma4.1 and full proof, (6), Lemmas6.1/6.2 and full proofs, Section6 normalization, Remark8.2; O'Sullivan 2007.13582v2 (1.2), Theorem1.4/(1.8), reusing assessed Section7 proof cases; new source Zhang 2601.18977v1 Section4 Lemmas4.1/4.2 and full proofs, Theorem1.5/proof and Remark4.4.
COMPARISON: Strict real accretivity supplies a known determinant-sign implication, but no inspected theorem proves it for the actual normalized matrix. The finite q-Pascal identity needs only r>=2 and 0<q<1; the far-tail bounds do not apply at k=r-1. One signed odd-coordinate test is nominated; L765's norm divergence is neither its evaluation nor its refutation.
GAP: The actual signed quadratic form, eventual q range at the new center, boundary specialization and determinant transfer require a separate mathematical check. No uniform signed bound, inertia theorem for this new condition, actual minor sign or RH conclusion is established.
REASON: Primary comparison resolves the missing general sign interface and identifies a bounded actual-coefficient discriminator before any uniform positivity attempt. This is known-method specialization; source coverage does not justify labeling the scalar calculation creative.
SCOPE: Completed literature-only step414; no lemma or mathematical-script edits and no evaluation of the proposed form. The new exact continuation is separately assessed in 2026-11-04-signed-qpascal-odd-coordinate-test.md and awaits next-turn approval.
LITERATURE_REASON: The supplied REVIEW_REQUIRED target lacked essential signed-matrix source coverage; unchanged coefficient-asymptotic and q-Pascal assessments were reused.

The main gap is actual-Xi all-degree mixed positivity. The proposed
intermediate target is a signed lower-bound mechanism for the matrix
at the exceptional coefficient edge k=r-1. If a positive symmetric
part can be transferred through a source-justified factorization with
known determinant sign, it could give exceptional signs; other shifts,
finite initial orders and the full main assembly would still need
explicit treatment. This is only a possible downstream use.

Essential inputs for assessment are the actual coefficient conventions
of L021, the precise L765 norm obstruction, and the step385/386/388
source comparison and audit. L773 is the reason for changing route,
not a mathematical input. L766's pointwise signed-integral obstruction
and step407's condensation/multiplier stop are comparisons only.
Do not assume L766's unaudited proof, L772's theta realization, actual
real-rootedness, or any all-order Turan theorem. No cross-notebook input.

The review was required to check that the named normalization exists at
k=r-1, specify its positive or signed determinant factors, and search
the exact symmetric-part/accretivity criterion and stronger known
results. It must distinguish actual signed information from an
unsigned norm already ruled out. The source factorization and the
criterion have not been read for this new purpose; this record does
not approve them by analogy.

A useful output is one specified family of vectors and an exact or
asymptotically controlled quadratic form, with a proposed lower-bound
threshold and a decisive counter-witness condition. If the mechanism
reduces to the old norm bound or merely restates positivity of the
unknown determinant, stop it during source comparison. A favorable
finite sample would not supply a uniform bound or all-order signs.

## Completed comparison — step414

The earlier nomination above records the questions at invocation; the
following source comparison resolves coverage, without solving its signed
estimate. No cross-notebook input was used.

[Michałowski v1](https://arxiv.org/html/2607.16795v1#S4), Lemma4.1,
factors V_ij=q^(ij) as L D L^T for r>=2 and 0<q<1, with L unit lower
triangular and sign(D_m)=(-1)^m. This finite identity has no tail-k
hypothesis. Section6 supplies the whitened symmetric matrix J+F and
reversal sign; its normalization prose has the inverse-diagonal issue
already corrected in audited L765. Theorem1.1 requires k>=10^18 r^3;
its bounds and Proposition4.4's r*tau<=1/64 cannot be imported at the
exceptional edge. At k=r-1 the coefficient indices run from 0 to 2r-2,
so a_0>0 from L021 makes the finite logarithms meaningful. Extending
the finite normalization is a later algebraic specialization, not an
extension of the tail theorem. Eventual 0<q<1 must still be checked.

[Teng Zhang, v1, 26 January 2026](https://arxiv.org/html/2601.18977v1#S4),
*Johnson's determinantal identity for contiguous minors of Toeplitz
matrices, with an accretive extension*, Lemma4.2 states: a real square
matrix with positive semidefinite symmetric part has nonnegative
determinant; with positive definite symmetric part its determinant is
strictly positive. Its proof uses Lemma4.1's positive congruence to
I plus a real skew-symmetric matrix, conjugate eigenvalue pairs, then
an epsilon-I limit for the semidefinite case. These proof cases were
read completely. Theorem1.5 additionally assumes real accretivity; it
does not prove that hypothesis for Xi. Remark4.4 warns against a complex
transpose-based extension. Only the real finite determinant implication
is needed here; no reproof is justified.

The proposed test object is A_r=J(J+F), with the actual finite F of the
next assessment and J=diag((-1)^m), and H_r=(A_r+A_r^T)/2. This names
a signed condition H_r>0, not an assumed fact. The source theorem
applies to A_r only if that strict condition is proved. Reconciliation
of det(A_r), the positive congruence factors and column reversal is
assigned to the later check. No inertia-preservation conclusion from
Lemma6.1 is imported after dropping its norm hypothesis. Taking the
symmetric part of J+F itself would retain an indefinite model and
would not be the proposed accretivity test.

[O'Sullivan v2](https://arxiv.org/html/2007.13582v2#S1), Theorem1.4
and (1.8), supplies arbitrary fixed-order integer-value expansions
for gamma_n=n! xi^(2n)(1/2)/(2n)!, with remainder
O_K(log(n)^K/n^K). The actual a_n=gamma_n/(8*4^n*n!) matches L021
and L765. Reuse the previously read Section7 theta-tail and Stirling
cases. This does not supply differentiated remainders, effective
onsets or a uniform expansion down to index0. The nominated low
coordinate can be extracted by triangularity; its actual index support
and amplified error must be checked before applying the expansion.

The sole nominated discriminator is e_1^T H_r e_1, with zero-based
e_1=(0,1,0,...), at integer k=r-1 as r grows. Required threshold: >0.
No value, sign or adjacent-defect identity is derived here. A rigorous
nonpositive witness excludes strict accretivity, without excluding
positive determinant or RH. A positive scalar leaves all other
directions unpaid. This differs from L765's absolute norm threshold
and uses neither all-order Turan positivity nor L766 as a premise.

Queries included `"q-Pascal" "symmetric part" Toeplitz xi`,
`"Riemann" "xi" "accretive" "Toeplitz"`,
`"q-Pascal" "signed" "Toeplitz"`,
`"xi coefficients" "symmetric part"`, and determinant/positive
symmetric-part/Ostrowski-Taussky queries. The relevant stronger
accretive-minor theorem was inspected as above; unrelated search
hits supply no claims. A JIPAM PDF lead returned 403; Zhang's fully
read matching real determinant theorem removes any essential access
blocker, so that lead is not a premise. Failed searches establish no
originality. The local exact-term search found only this nomination.

The main gap remains actual-Xi all-degree mixed positivity. The
signed mechanism merits this single prerequisite test, not a uniform
positivity conjecture asserted as a lemma. No justified creative
attempt is ready until this potential obstruction and an independent
signed estimate are addressed. Mathlib matching coverage is not
checked; no formal verification is claimed. PROOF and DAG are unchanged.
