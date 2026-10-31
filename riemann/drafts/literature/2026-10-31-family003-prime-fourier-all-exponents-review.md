# Good-prime Fourier formulas — completed source comparison

TARGET: Audit L546 Hypothesis 2's good-prime finite Fourier formulas for all six character exponents and every frequency, retaining the zero-at-zero principal convention.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched finite field multiplicative character Fourier transform trivial character zero at zero Gauss sum Fourier scaling; inspected the pinned local formula, Conrad's finite-group orthogonality/inversion and Gauss scaling cases, and official Mathlib GaussSum/MulChar source. Narrow searches of the prime assessments/notes/histories and ATTEMPTS found no completed exact all-exponents audit or recorded failure for it; internal Poisson Fourier audits concern different interfaces.
SOURCE_EVIDENCE: OpenAI pinned TeX 1581d4cbdd69a0faf34b2089614fe2a814316a6a, lines 557–591, 1688–1692, 1881–1909; Conrad, Gauss and Jacobi sums on finite fields and Z/mZ, Definition 2.1/Theorem 2.2, pp. 1–2, Example 4.11/Definition 4.13 and Lemma 4.16, pp. 13–15, with its unit-case referral to Lemma 3.10, p. 6; Conrad, Characters of finite abelian groups (short version), Theorem 4.1/Corollary 4.2, p. 10, (4.2)–(4.4), p. 11; official Mathlib GaussSum.lean lines 63–76 and 102–133, MulChar/Basic.lean lines 64–68 and 94–107. L556's additive normalization is reused.
COMPARISON: The pinned source already asserts every requested case. Independent known inputs cover scaling, orthogonality and the principal zero extension over arbitrary finite fields; the sextic product is unnecessary for this transform identity. Remaining work is exact notebook specialization, not a new theorem or an inference from Gauss norms.
GAP: Essential source coverage is complete. A later application audit must check exact order/nonprincipality of the five nonzero powers, the self-dual additive pairing for both residue degrees, the negative base additive character, P normalization and all zero cases, without applying a primitive-multiplicative theorem to the principal character.
REASON: The changed target's previously missing principal/zero-frequency coverage is now inspected. SPECIALIZE permits a separate bounded reproduction audit after next-turn approval; no premise is discharged or new result derived in this literature-only step.
SCOPE: Good primary p outside S over 6; O=Z[omega], lambda=1+2omega, P=N(p), e(z)=exp(2pi i Tr(z/lambda)), H=chi_p Euler sextic, every power including H^0 zero at zero. Include both residue degrees, all residue frequencies and the source's normalized transform, with its sign and scaling. Exclude composite propagation, theta coefficients, arithmetic uniformity and Xi signs.

LITERATURE_REASON: REVIEW_REQUIRED explicitly identified essential unread principal-character and zero-frequency coverage outside the ready sextic-product assessment. This review supplies it; further browsing is not the default continuation.

## Exact source interface (transcription, not a local proof)

The [pinned OpenAI TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
dated 30 September 2026, defines e and the zero extensions at lines
557–591 and tau at 1688–1692. Its entire local Fourier passage,
1881–1909, was read. It asserts, with H=chi_p and psi(x)=e(x/p),

\[
 C_{p,j}(h)=P^{-1}\sum_{x\in k}H(x)^j\psi(-hx),\qquad
 \tau_{p,j}^-=P^{-1/2}\sum_{x\in k}H(x)^j\psi(-x),
\]
\[
 C_{p,j}(h)=\begin{cases}
 P^{-1/2}\tau_{p,j}^-H(h)^{-j},&j\ne0,\ h\ne0,\\
 0,&j\ne0,\ h=0,\\
 -P^{-1},&j=0,\ h\ne0,\\
 1-P^{-1},&j=0,\ h=0.
 \end{cases}
\]

Here j is in {0,...,5} and h ranges over k=O/(p). In particular H^0
is the unit indicator, not the constant function one. The source uses
positive exponentials in reconstruction and includes zero frequencies;
it explicitly avoids DR's unit-Fourier-support formula. This is the
claim to audit, not independent evidence of its correctness.

## Independent known inputs and applicability boundary

Keith Conrad, [*Gauss and Jacobi sums on finite fields and Z/mZ*](https://kconrad.math.uconn.edu/blurbs/gradnumthy/Gauss-Jacobi-sums.pdf),
author-hosted, no inspected version date, accessed 2026-10-31:
Definition 2.1 extends even the principal character by zero. Theorem
2.2 gives its Gauss sum -1 and nonprincipal modulus sqrt(P).
Example 4.11 identifies primitive multiplicative characters on a field
with nonprincipal ones. Definition 4.13 and Lemma 4.16 give
G_r(A)=conj(A(r))G(A) for primitive A, including r=0. Read its
field-relevant zero case and its referred unit-case proof in Lemma 3.10;
the latter uses a bijective unit substitution without primitivity.
The principal character must be treated separately. Browser PDF text
loses conjugation bars; the exact inverse orientation is independently
unambiguous in the Mathlib statement below. No screenshot verification
is claimed.

Keith Conrad, [*Characters of finite abelian groups (short version)*](https://kconrad.math.uconn.edu/blurbs/grouptheory/charthyshort.pdf),
author-hosted, no inspected version date, accessed 2026-10-31:
Theorem 4.1, p. 10, gives sum_G A=|G| for the principal group character
and zero otherwise. Read both orthogonality statements, their proof,
Corollary 4.2 and the complete finite Fourier reconstruction (4.2)–(4.4),
p. 11. These apply to k additively and k^* multiplicatively. Inversion
uses a negative sign in the coefficient and a positive sign in the
reconstruction, with the group cardinality dividing the coefficient.
No restriction to cyclic additive groups or rational-prime fields occurs.

L556 already proves psi's nontriviality and finite-field trace transport
for f=1 and f=2. Reuse that result, rather than assume that inert primes
have prime-sized residue fields. The application audit still must identify
the pairing with the complete additive dual, verify exact order six for
H, use psi(-x) as the base Gauss character, and account for both displayed
P factors. These are bounded specialization obligations; this review
does not perform them. No new quadratic/sextic phase evaluation is needed.
L547's principal-frequency value is a retained premise, not a proof;
L557's product provides context only and is not an essential input here.

## Mathlib and search qualifications

Inspected official [GaussSum.lean](https://raw.githubusercontent.com/leanprover-community/mathlib4/master/Mathlib/NumberTheory/GaussSum.lean),
master as accessed 2026-10-31, including the full proof bodies at
lines 63–76 and 102–133. `gaussSum_mulShift_eq` requires a unit a
and gives G(A,psi.mulShift(a))=A^(-1)(a)G(A,psi), without a
nonprincipal hypothesis. `gaussSum_one_right` requires nonprincipal A
and a domain codomain, with trivial additive character, and gives zero.
`gaussSum_one_left` requires a finite field, domain codomain and
nontrivial additive character, and gives -1 for principal A.
`gaussSum_one_one` gives the unit-group cardinality for both principal
characters. These are independent supporting statements for all four
cases, with hypotheses explicit; their Eisenstein-normalized assembly
is not a matching theorem found in these files. No Lean verification ran.

Inspected [MulChar/Basic.lean](https://raw.githubusercontent.com/leanprover-community/mathlib4/master/Mathlib/NumberTheory/MulChar/Basic.lean)
at the same access date: `MulChar` sends nonunits to zero and `trivial`
is the unit indicator. Thus its character identity convention matches
the source rather than pointwise complex 0^0. Availability elsewhere
of a complete matching specialization was not checked.

The search query is recorded in SEARCH_EVIDENCE. Casselman's
*Finite fields* was a search lead whose PDF fetch timed out; it is not
an input and is unnecessary given the inspected coverage. Other search
hits were not used as theorem evidence. The failed fetch is not an
essential source blocker. Reused the ready cubic/sextic assessments
only within their scopes; did not re-search their mixed Jacobi identity.
The local internal Poisson Fourier assessments are different targets;
no claim about the entire archive follows from the narrow duplicate scan.

## One bounded continuation

Retain the exact TARGET. Essential local inputs are L546's definitions
and target interface, L547's convention and L556's established field and
additive normalization, with the cited finite-field/group statements.
Unresolved application obligations are listed above; coefficient,
composite-modulus, arithmetic-uniform and signed-Xi claims are excluded.
Equality in all four cases for all six exponents and both residue degrees
is the continuation threshold. Any unresolved zero-extension,
zero-frequency, inverse, sign or scaling mismatch stops discharge;
moduli alone do not pass. This can remove one finite premise from the
conditional reflection route, while actual-Xi positivity stays open.

Newly ready coverage requires separate next-turn approval before the
mathematical application. No new lemma, mathematical script or Fourier
derivation was written this turn. No cross-notebook input. This routine
specialization is not a justified creative central-Xi mechanism: no
independent realization/sign test is supplied by these finite identities.
