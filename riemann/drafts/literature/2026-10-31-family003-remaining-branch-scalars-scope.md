# Remaining one-prime branch scalars — completed source comparison

TARGET: Assess primary coverage for L546 (1)'s remaining branch-scalar formulas, distinguishing j=0 and j=4 and reusing L557/L558 for Gauss norms and finite Fourier values.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Queried exact reflection-row-phase/omega and finite-field Gauss inverse-variable/principal-character terminology; inspected pinned primary proof cases 2086–2122 and compared L546's existing all-six-exponents paragraphs, L547's identities, L557/L558, their ready assessments, relevant family003 audit notes/histories and the full-cusp approval-loop stop. Existing prose already contains the assembly mechanism, although the scalar premise remains formally retained. No novelty inference or independent new derivation is made.
SOURCE_EVIDENCE: OpenAI pinned TeX https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex , 30 September 2026: definitions/conventions 1551–1618, columns/scalars 1655–1725, Fourier cases 1881–1914, multiplier/additive identities and complete local branch proof 2047–2122. Reuse the inspected Conrad Theorem 2.2, Gauss scaling and finite-group orthogonality/inversion evidence in the prime-sextic and all-exponents Fourier assessments; no new upstream theorem is needed for this finite application.
COMPARISON: The primary proof explicitly claims every requested branch and its exact normalization. L547 supplies the frequency-dependent multiplier and additive phase; L558 supplies all Fourier coefficients; L557's norm argument supplies unit modulus for nonprincipal Gauss factors. L546 already sketches each branch and L548 reuses that computation. The only justified follow-up is an application/premise-status audit, not another general Gauss theorem, a new lemma or a reproof of the existing branch calculation.
GAP: Essential source coverage is complete for the bounded finite assembly. A separate audit must verify that L547/L557/L558 suffice without assuming L546 (1), check each phase and q_p power for all dual residues and both residue degrees, then reconcile the retained premise with the existing proof. The full global scalar normalization and analytic reflection remain outside this finite discharge.
REASON: The start-of-turn REVIEW_REQUIRED target lacked inspection of the actual branch proof and its overlap with existing local reasoning. Those cases are now inspected. SPECIALIZE permits a later reproduction audit using ready inputs; this literature turn does not discharge a premise or modify a lemma.
SCOPE: Fixed S containing primes above 6, good primary p, source additive character e, the c/sigma_p/epsilon_p conventions of L546, and its canonical cusp imports. Preserve both residue degrees, zero extensions and the distinct exceptional branches. Exclude a new Gauss norm/DFT proof, marked expansion, composite propagation, varying-S estimates, global closure and actual-Xi signs.

LITERATURE_REASON: The nominated REVIEW_REQUIRED target needed its essential primary branch proof and a duplicate comparison; the existing norm/DFT assessments do not themselves cover this assembly interface. They were reused rather than refreshed.

## Source cases and independent coverage

The pinned primary proof at 2086–2108 separates the multiplier,
nonprincipal branches, the exponent-four Ramanujan case and active
exponent zero. Lines 2113–2122 handle inactive/absent compatibility.
These are inspected source claims, not verifications performed here.
No individual Gauss root is evaluated there. Its precise displays
are already transcribed canonically in L546 (1) and its column table.

For the later application, the coverage map is:

| Obligation | Available input and required check |
|---|---|
| Frequency phase before summation | L547 (1)–(2), with its reduced numerator a=sigma_p h_p modulo p. Check conjugation of the multiplier, keeping chi_p(sigma_p)^(-2) outside the h_p sum. |
| j=1,2,3,5 | L558 (1), unit inverse-variable substitution and finite-field Gauss scaling from its ready assessment. Check the two normalized Gauss factors, epsilon exponent, all q_p powers and vanishing at p dividing x. |
| j=4 | L558's nonprincipal Fourier coefficient followed by additive orthogonality, not a nonprincipal exponent-zero Gauss theorem. Check the two values of the column, including its q_p^(-1/2) normalization. |
| Active j=0 | L558's coefficient -q_p^(-1); the second Gauss character has exponent two. Check the negative sign, epsilon phase and remaining q_p^(-1/2) column for units and nonunits x. |
| Inactive j=0 | L558's zero-frequency coefficient and L547's simultaneous compatibility. Keep its conductor distinct from the active branch's conductor. |
| Unit modulus | Only nonzero Gauss indices occur in L546 (1). Reuse L557's Conrad norm/character-transport argument for both additive signs; its mixed-Jacobi product identity is unnecessary. |

The independent standard inputs are Keith Conrad, *Gauss and Jacobi
sums on finite fields and Z/mZ*, Definition 2.1/Theorem 2.2, pp. 1–2,
and the unit scaling discussed in Lemma 4.16, pp. 14–15, referring to
Lemma 3.10, p. 6; and *Characters of finite abelian groups (short
version)*, Theorem 4.1/Corollary 4.2, p. 10, (4.2)–(4.4), p. 11.
Their exact hypotheses and source links are retained in
[the ready Fourier assessment](2026-10-31-family003-prime-fourier-all-exponents-review.md)
and [the ready sextic assessment](2026-10-31-family003-prime-sextic-product-review.md).
No new reading of those unchanged sources is claimed. L556's
field/additive normalization, already used by L557/L558, is sufficient
for split and inert primes. Neither finite-field theorem is restricted
to prime-sized fields. The principal character is zero at zero.

## Overlap, limitations and bounded continuation

L546, Proof, “All six local exponents,” already discusses these local
sums. L548's hypotheses explicitly reuse that computation, and its
independent review repeats the exceptional cases. This overlap changes
the proposed work: reconcile a retained premise with existing reasoning
and now-checked inputs; do not create a duplicate theorem. L548 is not
an independent input for proving this finite step, since it uses L546.
Its separately checked -i/81 normalization is not being reopened.
No extra theta transformation or raw cusp calculation is required beyond
L547 for this scope; its raw DR imports retain their qualifications.

The searched phase/Mellin source notes and prime histories retain the
finite contracts rather than recording a failed scalar equality.
The [full-cusp approval-loop stop](../../ATTEMPTS/2026-10-31-full-cusp-approval-loop-closure.md)
warns against repeated unchanged approvals; it does not forbid the
present changed finite application. The exact-term web query produced
no usable independent assembly theorem. The broader query surfaced
Conrad's already assessed notes; snippets and other hits were not used
as theorem evidence. A direct shell download failed DNS resolution;
the browser retrieved the pinned TeX and all essential cases, so there
is no source blocker. No novelty is inferred from the search.

Main gap: actual-Xi all-degree positivity. The finite discharge could
remove one explicit premise from L546 and the reflected-energy assembly;
it supplies no signed-Xi transfer. Continue only if every branch follows
from the named ready inputs without using its own displayed scalar as
a premise. Retain and isolate any missing case or dependency instead.
Raw source proofs, marked/composite applications, uniform/global closure
and actual-Xi signs remain separately qualified. No justified creative
central mechanism is nominated: an actual-Xi signed transfer identity
is still missing. No cross-notebook input.

Reuse L558's Mathlib record: gaussSum_mulShift_eq, gaussSum_one_left,
gaussSum_one_right and gaussSum_one_one support the local cases;
L557 records the norm support. Complete matching Eisenstein branch
assembly coverage remains unchecked. No Lean run is claimed.

The exact proposed application and its separate approval gate are in
[the continuation assessment](2026-10-31-family003-remaining-branch-scalars-audit.md).
No lemma, mathematical script, DAG or argument overview was changed.
