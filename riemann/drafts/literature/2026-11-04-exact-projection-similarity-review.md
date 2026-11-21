# Exact projection similarity — source assessment

TARGET: Review the exact projection weighting in the proposed similarity between L777's signed fixed-pair determinant and I-JQ, without assuming any Nevanlinna membership.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step445 searched finite-rank determinant, divided-difference/power-series/Hankel and diagonal-similarity terminology; read de Boor's primary statements/proofs and function extension, and reused the ready Duits/Bornemann assessment. Queries and local comparisons below; no exact Xi bridge was found in the inspected sources and no novelty is inferred.
SOURCE_EVIDENCE: Carl de Boor, Divided Differences, Surveys in Approximation Theory 1 (2005), 46–69, Example2/(10) p.49, Proposition21/proof p.51, Proposition25/(26)/proof pp.53–54, Example7 p.55, Proposition35/proof and Definition37 pp.58–59 https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf and arXiv:math/0502036v1 https://arxiv.org/pdf/math/0502036v1; reused Duits DPP2 AppendixA Lemmas66/69 pp.51–52 https://people.kth.se/~duits/static/media/DPP2.44e051d148b79af222fa.pdf, as qualified below.
COMPARISON: Standard divided differences and finite-rank determinant algebra cover the interfaces without Nevanlinna membership. They do not identify the actual projected pairing with the proposed Q. That normalization check is a bounded known-method specialization; L777's norm-compression matrix cannot replace Y*U.
GAP: A later calculation must justify convergence and the diagonal limit, retain row start i=r+1, determine the exact invertible diagonal similarity and every sign, and transfer only the determinant. The identity and separate J-Q inertia/nullity threshold remain unproved here.
REASON: Essential source coverage is available for one fixed real/simple pair. Continue with its exact normalization calculation after separate approval; abandon the proposed formula on an unremovable mismatch, without reopening the closed Taylor-index or positive-block tests.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED because its exact weighting/divided-difference interface had not been assessed; reuse ready determinant coverage and step443's class-scope comparison rather than repeat that broader search.
SCOPE: Literature-only step445; fixed (r,R)=(3,2048), exact b=p/F and simple real negative nodes certified by L779 under its retained contracts. No new identity, bound, lemma or mathematical script is derived. The newly ready continuation receives separate supervisor approval next turn.
COVERED_TARGET: At (r,R)=(3,2048), check the proposed diagonal similarity between I-C(Y*U) and I-JQ by an exact convergent-series and diagonal-scaling calculation, including the diagonal divided-difference limit.

## Original step444 nomination — preserved scope

This nomination is not an approval for mathematical work. The next
turn is literature-only, unless a prior adequate exact-target assessment
is identified and its applicability is established through the gate.
Do not repeat the broad half-plane membership search to fill a quota.
Use only the exact real/simple pair (r,R)=(3,2048) certified in L779,
L777's b=p/F, signed residue matrix C and projected pairing Y*U, and
the proposed h_r,K,E,Q,J already recorded in the parent comparison.
The question is the exact weighting identity, not a claim about its
sign or its ability to close RH. L781 supplies only the completed
diagnostic outcome, not an input proving a weighting formula.

Downstream use: a correct identity could make a signed-inertia test
relevant to the actual Fredholm determinant while allowing L780's
negative blocks. Continue only with source coverage for an exact
identity or a bounded, separately approved specialization retaining
every projection factor and denominator. If an unremovable sign,
normalization or convergence mismatch appears, record that obstruction
and abandon this proposed formula. Global membership, the J-Q inertia
threshold, general grouping and all mixed minors remain independent.
No new formula is derived or approved in this nomination. No
cross-notebook input is needed; full matching Mathlib coverage unchecked.

## Completed source review — step445

The main gap remains actual-Xi all-degree mixed positivity. The single
intermediate target is the exact fixed-pair weighting bridge. It could
connect the paid signed determinant to a symmetric matrix whose inertia
could then be studied, without supplying that inertia estimate itself.

### Primary statements inspected and reuse

De Boor's author PDF is the published 24-page article, dated
21 December2004, volume1 (2005), pp.46–69; arXiv v1 is dated
1 February2005. Example2/(10) states the two-node quotient and its
coincident-node derivative convention. Proposition21 proves continuity
for polynomial divided differences. Proposition25/(26) represents
polynomial divided differences as entries of a polynomial evaluated at
the lower bidiagonal node matrix, including repeated nodes. Read its
Newton-basis proof and extension by continuity, pp.53–54. Example7's
matrix-power argument treats monomials. Proposition35 and Definition37
extend the definition to functions possessing the required Hermite
data; they do not assert the desired infinite-sum interchange. These
algebraic identities have no monotonicity, real-zero or half-plane-class
premise. No reproof of the general results is needed.

The extracted exponent in display(27) is ambiguous; this review does
not import that display or silently correct it. Use Proposition25/(26)
and Example2/(10), whose statements and proofs were readable. The
coefficient regrouping and analytic limit remain obligations of the
subsequent calculation. This qualification does not block those
independent primary statements.

Reuse `2026-11-04-signed-rank-two-fredholm-diagnostic.md` for Duits,
AppendixA Lemma66 and Lemma69(2), pp.51–52, including their complete
proofs and inner-product translation. Selected statements/proofs were
also retrieved from the accessible author PDF this turn. Lemma66 covers
arbitrary compatible rectangular complex matrices; Lemma69 reduces a
finite-rank kernel to its pairing matrix. Use only the finite-dimensional
restriction/algebra already justified in L779, not an unchecked extension
of the finite-measure setup. Neither theorem requires norm<1, independent
columns or selfadjointness. They cover determinant transfer, not the
proposed weighting. The ready assessment also supplies Bornemann v2,
0804.2543, Section3/(3.2) p.10 for finite-rank determinants. No new
perturbation estimate or excluded positive-selfadjoint lemma is needed.

### Exact applicability and remaining specialization

The supplied overview/DAG preceded detailed proof reads. Read L777's
hypotheses, normalization(1), columns(2)–(4), exact U-entry formula
and Laurent bound; L779's grouping/residues and signed-pairing ranges;
and L780's statement and balancing proof. L017/L018/L021/L776 remain
inherited inputs, without a new audit of their full proofs.

L779 certifies two distinct negative nonzero nodes inside the disk,
complete nonzero signed residues, and a zero-free F neighborhood with
sigma=9/8. L777 supplies the geometric beta bound and projected operator.
These are the local hypotheses available for a future application;
real/simple grouping is not assumed globally. Retain L779's arithmetic
and software qualifications. No coefficient certificate was opened or
replayed here.

Use exactly the proposed h_r,K,E,Q,J in step443's preserved definition
block. Keep that K separate from L777's singular-value compression K.
Start with S=Y*U, the one-based U entries and rows i>r, rather than the
Gram matrix Y*Y. Check unequal-node entries and K_ii=h_r'(alpha_i),
with absolute/local-uniform convergence before regrouping or
differentiating. Exhibit an invertible real diagonal change of
coordinates, checking orientation and all residue/node factors. Matching
determinant signs or eigenvalues is not a matrix-equality check. L780's
existing balancing checks conventions, not the proposed new weighting.

SPECIALIZE is appropriate because general identities and convergent
input data are available, but the projection offset and its exact
diagonal factors are not stated by the sources. The future derivation
is an application and normalization check; no new formula or specialized
conclusion has been established in this literature turn.

### Duplicates, failures and bounded decision

Reused step443's automatic-class-import stop and read step444's
fixed-Taylor-index stop. The latter misses its rejection threshold and
does not prove N_1 membership. Read the relevant balanced-Schur source
comparison and L780's negative-block conclusion; the proposed identity
must allow that evidence. L779's positive determinant and norm>1 are
an existing benchmark, not a substitute for a matrix equality. None
settles the unpaid weighting calculation. No historical stop is treated
as a global ban and no cross-notebook input was used.

Queries: `site.people.kth.se duits DPP2 Lemma 66 Lemma 69 determinant`;
`divided difference power series Hankel matrix Loewner matrix analytic
function finite rank projection`; `Carl de Boor Divided differences
2005 monomial complete homogeneous polynomial equation`; and
`diagonal symmetrizable matrix diagonal similarity signed diagonal
symmetric matrix`. Search-only leads included rational Hankel/Loewner
realizations and integer symmetrizable matrices. They are not theorem
inputs: their rationality/integer hypotheses do not identify this tail.
No comprehensive absence or novelty follows.

Continue once, after separate approval, with the COVERED_TARGET above.
Success means an exact similarity retaining every factor and a justified
diagonal limit, not numerical agreement or an RH sign. An unremovable
offset/sign/scaling discrepancy abandons this proposed formula and must
be preserved. No size/precision/radius sweep is authorized. Even success
leaves n_0(J-Q)=0 and the prescribed negative-index equality unpaid,
as well as half-plane membership, complex/multiple grouping, growing
orders/radii and all mixed minors.

Essential primary statements were accessible as PDF text. The screenshot
wrapper supplied no inspectable image and a local curl download failed
DNS; neither is essential because no claim depends on display(27).
Full matching Mathlib coverage is unchecked. No lemma, mathematical
script, PROOF or DAG changed. Outcome EXPLORATION records source work,
not an established identity or progress beyond checked sources.
