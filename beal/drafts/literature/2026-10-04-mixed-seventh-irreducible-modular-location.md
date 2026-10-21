# Exceptional-branch irreducible modular location: source review

TARGET: Assess whether PVT Theorem 7.8 applies at residual characteristic 7 to L019's geometric representation under L020's exceptional-algebra hypothesis, retaining both coefficient embeddings and avoiding the blocked packet certificates.
CHECKED: 2026-10-05
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: Reused the trace-family and representation-applicability assessments; searched Breuil Diamond 2014 level lowering Hilbert modular forms theorem 3.2 and the finite-flat/cyclotomic-restriction terminology. Followed PVT's BD14 and BCDF25 references to primary theorem statements and the relevant restriction proof.
SOURCE_EVIDENCE: Inspected PVT arXiv:2512.17845v1 Sections 2.2–2.3, Theorems 2.1 and 2.4, Remark 2.2, Section 7.1 equation (32), and all of Theorem 7.8 and its proof in Section 7.2; Breuil–Diamond author PDF Theorem 3.2.2, printed pp. 36–37; BCDF arXiv:2205.15861v5 Section 6.2 Lemma 6.9 with its full proof and Section 8.2 Theorem 8.3 proof. No packet certificate was retrieved.
COMPARISON: PVT states the desired location for irreducible representations and includes p=7 in its setup; the inspected level-lowering input requires irreducibility on a cyclotomic restriction, which L019–L020 do not state. BCDF's available restriction lemma additionally assumes good or multiplicative reduction at every base prime above p; that hypothesis has not been established here in every coordinate case.
GAP: A source-backed justification of irreducibility on G_F(zeta_7), or a level-lowering theorem that dispenses with it, is still needed for an audited application. The four-level statement is an inspected source claim, not newly established notebook mathematics.
REASON: The primary proof exposed a precise extra hypothesis hidden by a theorem-level summary. Resolve this interface before importing the modular-location conclusion; no evidence refutes the published conclusion itself.
SCOPE: Only the original geometric plus representation at 7, in L020's conditional algebra branch, with both coefficient embeddings. Packet exhaustion and global descent remain parked.

## Relevance and bounded decision

The main gap remains uniform emptiness of residual Beal signatures. The intermediate target is location of this conditional irreducible branch in explicit weight-two Hilbert spaces; its plausible downstream use is an independent irreducible trace-exclusion argument. Even successful location would leave packet exhaustion and the original global descent unresolved. The required signature threshold is zero solutions, whereas location alone only narrows the possible representations.

The continuation test was complete hypothesis coverage at 7. The review found an unproved restriction condition in the cited proof route, so an unconditional notebook application is not yet approved. This is new negative evidence for routing, not a counterexample to PVT or Beal. There is no new lemma, calculation, or mathematical derivation in this turn.

## Primary-source scope

[PVT, arXiv:2512.17845v1, 19 December 2025, Theorem 7.8, Section 7.2](https://arxiv.org/html/2512.17845v1#S7.SS2) states a residual isomorphism with a parallel-weight-two newform of trivial character at level 3^i(sqrt(5))^j, i,j in {2,3}. Its proof identifies the level with the residual conductor, rather than merely an upper bound; the explicit cases are Theorem 7.8(i)–(ii). The setup permits p=7. Theorem 2.4(1) supplies plus modularity, and Remark 2.2 specifies the weight-two normalization. The proof cites BD14 without checking the cyclotomic restriction explicitly.

[Breuil–Diamond, *Formes modulaires de Hilbert modulo p et valeurs d’extensions entre caractères galoisiens*, Ann. Sci. ENS 47(5) (2014), 905–974; author PDF Theorem 3.2.2, printed pp. 36–37](https://www.imo.universite-paris-saclay.fr/~breuil/PUBLICATIONS/extensions.pdf#page=36), requires p>2, modularity, irreducibility on G_{F(zeta_p)}, and compatible prescribed local lifts with determinant conditions. The exceptional p=5 condition is irrelevant at 7. The PDF is an author version; printed page numbers refer to that version.

[BCDF, arXiv:2205.15861v5, Lemma 6.9 and proof, Section 6.2](https://arxiv.org/html/2205.15861v5#S6.SS2), assumes p>3 unramified in the base field, a GL_2-type variety with real multiplication, good or multiplicative reduction above p, and absolute irreducibility. It excludes reducibility on ramified quadratic extensions using Raynaud inertia. Its [Theorem 8.3 proof](https://arxiv.org/html/2205.15861v5#S8.SS2) explicitly handles cyclotomic restriction before applying BD14. That theorem concerns a different Frey family.

## Comparison with canonical local inputs

L019 already records the signed substitution (a,b,c)=(X,-Z,Y), the same specialization t=-X^5/Y^3, nonzero primitive coordinates, the geometric Jacobian and its weight-two normalization. Its prime above 7 is inert and unramified. It establishes cyclotomic determinant and finite flatness in every coordinate-valuation case. Those are available inputs, not new deductions in this review.

L020 establishes absolute irreducibility over G_F through either embedding of F_49, conditional on its explicit algebra isomorphism. Neither L019 nor L020 proves irreducibility after restricting the domain to G_{F(zeta_7)}. Enlarging or changing coefficient embeddings does not by itself supply that assertion. Consequently both embeddings must remain in the next test; one cannot replace this gap with an assertion that all coefficients lie in F_7.

The good-or-multiplicative hypothesis of BCDF Lemma 6.9 is stronger than the finite-flat residual assertion recorded in L019. L019's table includes the X- and Y-divisibility branches at 7; its proof supplies finite-flat torsion via the geometric source, without claiming good or multiplicative reduction of J in those branches. No such reduction is inferred here. A potential extension of the inertia argument to the finite-flat formulation is a distinct mathematical target needing separate assessment; it is not approved or proved in this review.

The normalization and the coordinate setup match existing canonical inputs. The exact local level formulas may be imported only as part of a justified theorem application, not reconstructed from L019's upper conductor bounds. No packet list, coefficient-field-degree bound, q=29 Hecke-spectrum exhaustion, or global algebra classification follows from the sources inspected here.

## Duplicate and failure check

The earlier trace-family assessment located Theorem 7.8 but expressly left solution applicability unaudited. The representation-applicability assessment supplies the determinant input independently and warns of the published/arXiv BCDF numbering difference. We reuse it; we do not identify the published Theorem 3.13 with an unread arXiv theorem by number alone. L020 closes only the reducible sector. The V4 archive and original-descent failures remain preserved and parked. This restriction test does not retry either blocker.

## Mathlib

Coverage of the full modular-location implication, cyclotomic restriction, and the supporting Hilbert level-lowering theorem: **not checked**. No formal verification or matching full Mathlib declaration is claimed.
