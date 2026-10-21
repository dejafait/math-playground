# Surjective mod-7 image with the prescribed local approximation — source assessment

TARGET: Establish whether L044's integer cubic approximation can be chosen with global mod-7 image GL_2(F_7) while preserving its full local 210-torsion module.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Targeted local searches found no prior global-image proof; external searches for Jones's Serre-curve density and Zywina's large-image results led to the primary fixed-level integral-model bound, Proposition 5.7.
SOURCE_EVIDENCE: Read Zywina's author-hosted 15-page version, section 1.1 and Definition 5.1, Proposition 5.7 and its full proof, Proposition 5.5's proof, the relevant prime case of Lemmas A.10/A.8, and the Q-case assertion in Lemma 2.4's proof; read Milne II.2's coordinate changes and Theorems 2.1/2.4(b), plus II.1 Proposition 1.5 and proof.
COMPARISON: The inspected source bounds exceptional integral short models at each fixed torsion level; only the coefficient-congruence and coordinate-change specialization to L044 remains, rather than a new generic-image or Hilbert irreducibility theorem.
GAP: A separate proof must retain L044's monic cubic neighborhood, exhibit a full-rank affine lattice of integral short models, compare its count with the exceptional bound, and transport full torsion modules through a Q-defined pointed isomorphism.
REASON: Primary fixed-level coverage replaces the unread generic-image lead with a known-method specialization; no existence result or new lemma is established during this literature-only turn.
SCOPE: Exactly TARGET with reselected integer coefficients and arbitrary fixed sufficient precision M; fixed Omega,H,N and local 210-torsion retained. No prescribed coefficient bound, effective M, mod-7 image after restriction to F or sufficient initial theta data is covered.
LITERATURE_REASON: The startup gate requires the first comparison for the new global-image condition, outside the ready local-constancy and adjunction coverage.

## Primary source and exact input

[David Zywina, *Elliptic curves with maximal Galois action on their
torsion points*](https://pi.math.cornell.edu/~zywina/papers/MaximalGalois.pdf),
author-hosted 15-page version retrieved 2026-10-11; published in
*Bull. London Math. Soc.* 42 (2010), 811–826,
[DOI](https://doi.org/10.1112/blms/bdq039).
Numbers/pages here refer to that undated author version, not the
distinct 14-page arXiv v1.

For a number field k and fixed norm, B_k(X) consists of integral
pairs (a,b) defining nonsingular curves y^2=x^3+ax+b, within norm X.
Definition 5.1, p.6, defines B_{k,m}(X) by failure of the m-torsion
image to contain SL_2(Z/mZ). Proposition 5.7, p.8, gives

|B_{k,m}(X)| / |B_k(X)| <<_{k,norm,m} log(X)/X^([k:Q]/2).

Its proof uses determinant-one conjugacy classes, Proposition 5.5
and Lemma A.10. The relevant prime case reduces to A.8 with d=1;
the exceptional (3,-1) case does not arise at m=7. There is no
minimal-model, good-reduction or non-CM restriction. Lemma 2.4's
proof, p.5, identifies containment of SL_2 with full GL_2 image over Q.
Import these assertions without reproof. Theorem 1.3's exclusion
of Q does not apply to Proposition 5.7.

## Supporting coordinate coverage

[J.S. Milne, *Elliptic Curves*, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf),
II.2, pp.50–53: the characteristic-not-2-or-3 changes preceding
Theorem 2.1 remove the quadratic term; Theorem 2.1(b) supplies
short-model scaling, and Theorem 2.4(b) gives general pointed
Weierstrass coordinate formulas. Read their statements, the proof
of 2.1 and the stated proof qualification for 2.4 (same argument
with more algebra). II.1, Proposition 1.5 and proof, p.49, show
that pointed isomorphisms preserve the elliptic group law.
Apply over Q, which has characteristic zero. Equal j-invariants
or geometric twists are not substituted for base-field isomorphisms.

## Comparison and approved proof obligations

The main gap remains original finite B>=A. This target could supply
the global mod-7 prerequisite for a replacement choice of L044's
E_0, after which L045 would be reusable. Independent bridges remain.

The fixed-level bound is sufficient coverage; the stronger
Serre-curve theorem is unnecessary. The separate attempt is approved to:

1. Reuse L044's squarefree monic Q_3 cubic and local precision M
   from Bisatt–Dokchitser Theorem 2.2. Fix an integer quadratic
   coefficient in its prescribed class and retain both remaining
   coefficient progressions. Do not replace this cubic by a short
   cubic congruent in an unrelated neighborhood.
2. Use the inspected Q-defined translation and scaling to obtain
   integral short models. Write the actual maps in both directions,
   verify the point at infinity, and compute the parameter map.
   Prove that permitted parameters give a full-rank affine lattice
   in the short coefficients, of finite index fixed with M and the
   quadratic coefficient. Check integrality carefully: the
   translation divides by 3.
3. Prove its elementary count in growing coefficient boxes, with
   a positive leading constant, accounting for singular models.
   Compare explicitly with Proposition 5.7 for k=Q, m=7. A
   one-dimensional family or bare density assertion without that
   comparison would fail. Keep M fixed as the archimedean bound
   grows; uniformity in M is unnecessary.
4. Transport the global representation through the pointed
   Q-isomorphism and apply L044's finite-torsion argument to the
   original monic cubic. Retain all E[210] as a G_Q_3-module and
   the embedded full-kernel identities over H. A point, cyclic
   subgroup or x-coordinate field alone would not suffice.

These are next-turn obligations, not a proof executed here.
The parameter/counting specialization explains SPECIALIZE rather
than IMPORT. No reproof of large sieve, generic monodromy or torsion
constancy is needed. REPRODUCTION is the approved research
classification; no novelty or effective construction is claimed.

## Search record, alternatives and recorded failures

Queries: `Jones almost all elliptic curves are Serre curves theorem
congruence arxiv`; `Zywina Hilbert irreducibility elliptic curves
prescribed congruence integral coefficients mod l surjective`;
`Zywina elliptic curves maximal Galois action torsion points B_k(x)
Theorem 1.6`.

Also inspected Nathan Jones, *Almost all elliptic curves are Serre
curves*, *Trans. AMS* 362 (2010), 1547–1570,
[author-hosted published PDF](https://homepages.math.uic.edu/~ncjones/almostall.pdf):
Theorems 2/4, Definition 3 and the introduction's model-counting
qualification, pp.1549–1550. Zywina's Theorem 1.6 and its section
7.2 proof were inspected as an alternative. These stronger results
are not inputs; their full proofs were not audited. The original
generic-division/Hilbert lead is unused; no generic monodromy theorem
is claimed inspected. Zywina's 2022 fixed-curve surjectivity algorithm
and a 2026 7-adic classification were discovery leads only.
A failed duplicate search is not evidence of originality.

Targeted local checks covered L044's model/approximation argument,
the 2026-10-11 finite-torsion and adjunction assessments, histories
142–145 and ATTEMPTS/022,025,026,027. No earlier result establishes
this global-image condition. L043's exact-curve stop persists:
only the finite local module is retained. The old field-factor and
tensor-component stops are not reopened by changing the global curve.
One attempted shell PDF retrieval failed at DNS; the primary PDF
was fully accessible through the web reader, so this is not an
essential source blocker.

## Continuation test and remaining scope

Continue if the full-rank integral parameter count dominates the
fixed-level exceptional count and the original cubic remains within
L044's congruences. Abandon this specialization if it yields only a
thin family, loses those congruences or uses a geometric rather than
Q-defined isomorphism. Record any genuine failure; no source blocker
currently prevents the separate attempt.

Essential local inputs are audited L044 and its retained L042 packet.
L045 is downstream, not a premise for global surjectivity.
No preservation of the image after adjoining 30-torsion and zeta_60
is assumed. Geometric-parameter/full initial-data, native/input/action,
pilot transport, essentiality and original finite B>=A remain open.
Full matching Mathlib coverage was not checked. No lemmas,
mathematical scripts, DAG rows or PROOF argument changed here.
