# Retained-field integral action — critical-audit source coverage

TARGET: Critically audit L063's retained-N reference-lift compatibility, torsion quotient and two-sided preservation of J and I=J/6.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused discovery queries and failure comparisons in drafts/literature/2026-10-15-retained-field-torsion-paired-action.md; read complete L063 and history/235, and searched ATTEMPTS/015,016,019,020,024 for the excluded lift, coordinate and torsion-free transfers. Direct primary-source retrieval below adds proof-specific coverage; no new novelty search was needed.
SOURCE_EVIDENCE: Hoshi PMB 2021 DOI 10.5802/pmb.42, Lemma 1.2(i,ii,iv,v), printed p.11; Proposition 3.11(i,iv), p.22; Definition 4.1(i), Proposition 4.2(i,iii) and proof, pp.25–26; Theorem 7.6(i,ii) and proof, pp.39–40. Hoshi–Nishio revised June 2022 RIMS1931, Lemma 2.3(ii), statement p.6 and logarithm proof diagram p.7. Kondo arXiv:2512.09231v2, section 0 and section 1, Theorem 1.1, Theorem 1.3 proof through all three displayed automorphism families and their index qualifications, directly read on 2026-10-15.
COMPARISON: Primary passages cover the unit structure, reciprocal fixed/closure comparisons, reconstructed logarithm action and actual paired generators needed for this bounded audit. They do not give a theorem already certifying L063's assembled choices, integral quotient topology or composition argument; these are precisely the pending specialization checks.
GAP: Perform the separate mathematical audit of the common reciprocity identification, fixed-unit inclusion, torsion quotient topology/scalars, inverse/composition preservation and J versus J/6; coverage approval does not certify those arguments.
REASON: Essential source coverage for the exact proof-specific audit is now adequate; SPECIALIZE authorizes only its critical review and any necessary qualification, with no new action, basis, coordinates or numerical bound.
LITERATURE_REASON: L063 was newly written after the construction assessment; its common-reference inclusion and integral torsion-quotient obligations had only proposed REVIEW_REQUIRED audit coverage at invocation start.
SCOPE: Only the exact TARGET and L063 on the unchanged L042,L045,L048 packet; no dependent numerical or native-action test.

## Retrieved theorem passages

[Hoshi, published 2021 text](https://www.numdam.org/item/10.5802/pmb.42.pdf):
Lemma 1.2 allows finite p-primary unit torsion and identifies the logarithm
kernel. Proposition 3.11 supplies topological fixed-unit and logarithm
diagrams. Definition 4.1 uses transfer transitions; Proposition 4.2 uses
finite-field reciprocity maps for the closure-unit and additive diagrams.
The proof of Theorem 7.6(i) transports through reconstructed pairs;
(ii) identifies the fiber ambiguity. Reuse Definitions 5.1–5.3 from
the construction assessment. These statements concern general mixed
characteristic local fields, without torsion-free units. The audit must
compare the actual maps at the base-field term of the transfer system,
rather than rely only on the existence of some full-pair lift. Its topology
check concerns fixed-field units, not a topology on closure units.

[Hoshi–Nishio, June 2022 revised text](https://www.kurims.kyoto-u.ac.jp/~yuichiro/rims1931revised.pdf):
Lemma 2.3 concerns an arbitrary absolute-Galois automorphism. Its (ii)
proof explicitly displays the commuting unit/log-shell action diagram,
and then distinguishes the logarithm image 2pI from the full additive
space. This supplies the exact comparison passage for the J-versus-I
check, without imposing the absolutely abelian hypotheses of later
results. The essential diagram is on printed/PDF p.7; the broader
pp.7–8 locator in the construction record includes more than needed.

[Kondo, version 2, 12 December 2025](https://arxiv.org/html/2512.09231v2#S1):
Section 0 specifies the reconstructed rational action. Theorem 1.1
requires odd p and includes the even-degree relator. Theorem 1.3's proof
sets the even-case pair count to (d-2)/2, indexes adjacencies one fewer,
and gives all three generator words and unchanged-generator clauses.
This is the passage against which to check L063's 83/82 indexing,
fixed x_0,x_1,x_2, and fixed b_(i+1). No integral presentation basis or
absolute-abelian assumption is supplied by these passages. No reproof
of the presentation theorem is needed for the audit.

## Duplicate, stopping and applicability boundary

The earlier construction assessment remains adequate for discovery and
known-result comparisons. L024/L032 concern other fields with no
3-primary unit torsion; they cannot certify this quotient argument.
ATTEMPTS/015–016 exclude a particular old involution, /019 an unsupported
universal field-line restriction, /020 prescribed reciprocal coordinates,
and /024 whole-kernel irreducibility transfer. Preserve those stops.
The exact new object to review is L063; repeating its construction or
reviving these failed coordinate mechanisms is outside this target.
No claim of originality follows from this scoped duplicate check.

The unchanged inputs are L042,L045,L048 and the complete proof of L063.
Retain N=Q_3(zeta_420,3^(1/7)), degree 168, e=14,f=12, and the same
E_0,F,K_glob,Omega,u,w,H,q_0, full 30-torsion, M>=max(M_tors,31),
origin,U,alpha,psi,gamma,0_B,Q,c and stable logs. No F_mod=Q,
K_glob=N, q_0=3^30 or torsion-free unit group is assumed. The audit
may use these canonical field inputs without reopening their proofs;
if a genuine dependence becomes doubtful, identify it explicitly.

## One bounded mathematical continuation

The main gap is still original finite B>=A and actual
input/action/pilot/essentiality. The intermediate target is a separate
critical audit of the retained-field integral reference action. Its
plausible downstream use is a later, separately assessed action test
on the retained admissibility packet, with no convenient coordinates.

Check R i=j r against the base term of the reciprocal transfer system;
then check compatibility of its induced fixed-unit map with the
reconstructed additive diagram. Check that all unit torsion is retained
in the full pair, and verify quotient topology, scalar structure,
rank/fullness, inverses and composition as distinct proof obligations.
Finally check that scaling the additive image by 1/6 does not assert
multiplicative division of torsion or surjectivity of units onto I.
These are tasks for the next mathematical turn, not results of this
source review.

Continue only if every required arrow and both preservation directions
survive that audit; otherwise identify and qualify the failed claim
before dependent numerical work. Native field/rho, independent initial
data, actual action/input membership, numerical volume and essentiality
remain unresolved. Mathlib coverage for the complete reconstructed
lifting statement and its supporting quotient facts is not checked;
unknown coverage is not absence. No lemma or mathematical script was
modified in this literature-only step.
