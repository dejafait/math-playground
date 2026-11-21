# Compact unconditional triangular-Mobius contour audit

TARGET: Audit BCF Lemma 2 on fixed compact subsets of 0<Re(s)<1 away from zeta zeros, using Inoue Proposition 1 to justify contour-ordered all-zero residues without RH or simplicity.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the parent's exact-polynomial discovery; targeted unconditional residue-convergence searches led to Inoue's published good-height input. No novelty claim for the explicit formula or compact audit.
SOURCE_EVIDENCE: Direct primary PDFs inspected 2026-11-03: https://arxiv.org/pdf/1211.5191v1 (BCF Lemma 2 and proof p. 6); https://www.numdam.org/item/10.5802/jtnb.1162.pdf (Inoue Proposition 1 p. 279, Lemma 2 p. 288, proof pp. 291--292, Theorem 4 proof pp. 297--298). Parent assessment retains the separate conditional norm comparison.
COMPARISON: BCF states the identity; Inoue provides unconditional good heights, including Q=1. The difference is explicit ordering, compact-uniform applicability and zero-pole qualification for the shifted squared kernel. The conditional norm asymptotic is excluded.
GAP: Audit the finite rectangle, all multiplicity residues, both horizontal edges, far-left edge, endpoint weight and order of limits. No absolute individual-zero sum or L2 interchange may be assumed.
REASON: The primary identity lacks an explicit limiting convention; the available height bound makes a bounded audit independent of the inaccessible refinement possible. This is source specialization, not a creative RH mechanism.
SCOPE: L018 actual zeta; fixed N>=2 and compact K in {0<Re(s)<1,zeta(s)!=0}; constants may depend on K,N. All nontrivial and trivial zeros retained. No RH, simplicity, finite-off-line-zero or reciprocal-derivative assumption.

Use z=s+w so height selection is explicit. Check modulus-one
applicability before citing Inoue with alpha=13,Q=1. Give the finite
identity and legitimate contour sequence before any limit; retain top
and bottom edges and specify the limit order. Exclude s=rho from K.
The n=N taper vanishes, so handle the integer endpoint explicitly.

Pass: cite the known identity with a complete compact-uniform audit
and any actual repair. Fail: record the unbounded edge or unjustified
limit; park that form of the identity. A compact identity does not
pay full-line L2 convergence or E_N decay; those require a separately
assessed target and summable norm estimates.

No mathematical derivation performed in preparing this assessment.
Matching Mathlib coverage unchecked. Purpose: conceptual audit.
Source gate repaired and assessment approved in the separate literature
step 2026-11-03-compact-contour-source-gate-repair-228. No proof audit
has yet been performed. The exact target and SPECIALIZE scope persist.

## Primary-source approval record

[Bettin--Conrey--Farmer, v1, 22 November 2012](https://arxiv.org/pdf/1211.5191v1),
Lemma 2 and its complete proof, printed p. 6, were inspected directly.
The source calls this identity unconditional, uses residues at distinct
nontrivial zeros, and shifts to Re(w)=-Re(s)-2M-1 before M tends to
infinity. It does not specify the infinite zero-sum ordering or justify
horizontal limits. Its adjacent Lemma 3 assumes RH, simplicity and the
negative moment; those estimates are outside the approved audit.
The wording that F_s(z) is entire needs a branch qualification, already
recorded in the parent: only the positive argument 1/N is needed here.

[Inoue, JTNB 33 (2021), 273--315](https://www.numdam.org/item/10.5802/jtnb.1162.pdf),
Proposition 1, printed p. 279, assumes alpha>=13, T>=T0(alpha),
1<=Q<=(log T)^(alpha/4). It selects t in [T,2T] with reciprocal
L bound exp(C alpha (log log(QT))^2), simultaneously for
1/2<=sigma<=2 and primitive characters of modulus at most Q.
The modulus-one character has conductor one and L=zeta; Q=1 is
explicitly permitted. The proof's far-from-half and near-half cases,
pp. 291--292, were inspected. Lemma 2, p. 288, supplies functional-
equation estimates for |t|>=1, sigma<=1/2 and for |t|<=1 on negative
half-integer lines. Theorem 4's proof, pp. 297--298, retains multiplicity
residues, sends the left edge away, splits the top into three real-part
ranges, and treats the bottom by conjugation. This is a model contour
argument with kernel x^z/z, not the requested shifted squared kernel.
No assumption from its separate Theorem 6 is imported.

## Scope of approval and future discriminating test

Reuse the parent comparison and prior failure record; no repeat search
for unconditional full-line decay is needed. This step repairs source
traceability, without establishing a new estimate or the target identity.
The audit may specialize these inputs; it must still prove uniformity
over the stated K, justify every edge for its actual kernel, account for
z=s and all zero multiplicities, handle n=N, and state a valid limit
order. No absolute convergence of individual residues, arbitrary-height
ordering, uniformity as N grows, or full-line norm conclusion is approved.
If a necessary edge or limit remains unpaid, identify it and park this
identity in that form. Mathlib matching coverage remains unchecked.
