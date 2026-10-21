# Fourth-order-pole attempt in progress

2026-10-20, step 375. Approved target and prior SPECIALIZE assessment:
`drafts/literature/2026-10-20-order-four-pole-dictionary-uniform-upper.md`.
Inputs C012a and foundations/01–02; L099–L100 are contrasts, not premises.
This is one REPRODUCTION / proof_attempt, without new source research.

Completion note: the initial reasoning below is preserved as the
pre-computation checkpoint. The completed proof and qualifications are
canonical in [L101](../lemmas/L101-order-four-pole-dictionary-and-upper-test.md).
The cap/T lies in (3676307,3676308), so this estimate is parked.
All 4143 construction and 2488 reconstruction checks pass. A separate
critical proof audit remains pending, with REVIEW_REQUIRED coverage.

Main gap: arbitrary-center 67/68 safety. Intermediate target: the complete
67-agreement dictionary and one absolute character-sieve upper certificate
for the approved fourth-order-pole family. Downstream use: exclude this
family if the cap is at most T; otherwise park this estimate. Independent
centers, exact boundary and ABF comparison remain unresolved.

Unfinished reasoning saved before computation: write P=X^68+A, with
A=a0+a1 X+a2 X²+a3 X³, a0 nonzero. Every ambient candidate gives monic
G=P-X^4 f of degree 68. For a chosen 67-subset S of agreement roots,
G=g_S(X)(X-r). Its constant term gives r=-a0/g_S(0) in E*, so G and f
descend to E. Other tuple rows vanish. Conversely each such pair with
G=A modulo X^4 gives a degree-at-most-63 message. Distinct G give
distinct messages; a residual root in S repeats a root, while a residual
root in H minus S gives 68 distinct agreements. Thus the intended exact
list formula is M67-67 N68, with M67 the pair count and N68 the count of
68-subsets whose root products equal A modulo X^4. This must be fully
proved, not treated as a raw subset bijection.

Intended one-shot certificate: use the full group
G4=(E[X]/X^4)* of size (Q-1)Q³, with log coordinates
(c,u,v-u²/2,w-uv+u³/3). The residual factor ranges over all E*;
copying L100's constant-H denominator is invalid. Orthogonality gives
M67=|G4|^(-1) sum_chi chi(A)^(-1) W_chi R_chi, with
R_chi=sum_(r in E*) chi(X-r). The principal term is binomial(1024,67)/Q³.
Every nonprincipal constant-only character has R_chi=0. For each other
character, all powers 1 through 67 remain nonconstant on the additive
log coordinates, including all index-64 twists. Li–Wan Lemma 4.1 with
modulus X^4 should give both |R_chi|<=3 sqrt(Q)<769 and restricted
cycle bounds <=3 sqrt(Q)<769. The assessed weighted sieve then gives
|W_chi|<=binomial(835,67). Test exactly
U=binomial(1024,67)/Q³+(1-Q^(-3))*769*binomial(835,67)
against T=Q^28/2^128. No retuning if it fails. These formulas are
unverified working reasoning until the canonical proof and certificate
are completed. Full character hypotheses and multiplicities remain
explicit proof obligations at this checkpoint.
