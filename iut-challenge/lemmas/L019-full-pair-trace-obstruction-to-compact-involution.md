# L019 — No full model MLF×-pair lift of the compact involution

## Hypotheses

Let K=Q_3(pi), pi^27=3, O=O_K, J=log(O^times), I=J/6, and G_K=Gal(kbar/K). Retain the **full model MLF×-pair** G_K acting on O_kbar^times. An automorphism is a pair (alpha,beta) of a topological group automorphism alpha of G_K and a monoid automorphism beta of O_kbar^times, satisfying beta(sigma x)=alpha(sigma)beta(x). No geometricity, ramification-filtration compatibility, or identity restriction on alpha is imposed. Neither an isolated invariant lattice nor a torsion quotient replaces the pair.

Use L016's complete logarithm image, continuous logarithm homomorphism, and inverse log/exp on U_14=1+pi^14 O. Use L017's fixed Q_3-linear involution g preserving I (hence J), its actual logarithm q=q_1, and the exact data

\[
q=\sum_{r=0}^{26}c_r\pi^r\in J,\qquad c_0=16/9,\quad c_{26}=0,\qquad g(q)=54\pi q.
\]

The last identity is also established in L018. Use L018's justified exponent/logarithm specialization: for lambda in Zhat^times and any unit u of K,

\[
\log(u^\lambda)=\lambda_3\log(u),\qquad \lambda_3\in\mathbb Z_3^\times.
\]

Import these precise primary inputs, reusing the prior SPECIALIZE assessment:

- **Hoshi, Introduction to Mono-anabelian Geometry**, Publications mathématiques de Besançon (2021), 5–44, DOI 10.5802/pmb.42: Lemma 1.7(i–iii), pp. 15–16; Proposition 3.11(i,iv), p. 22; Definition 4.1(i) and Proposition 4.2(i), pp. 25–26; Theorem 7.6(i–ii) with proof, pp. 39–40, and Corollary 7.7, p. 43. The reciprocal-unit identifications are topological; reconstruction on the algebraic closure uses transfer and is functorial. Full-pair lifts over a fixed alpha form a Zhat^times-torsor under target exponentiation. [Published primary PDF](https://www.numdam.org/item/10.5802/pmb.42.pdf).
- **Hoshi, Topics in the Anabelian Geometry of Mixed-characteristic Local Fields**, author-hosted **June 2018 revised RIMS1882 preprint**, Lemma 4.1(iii) and proof, pp. 33–34; Proposition 4.9(i), pp. 36–37; Remark 4.12.1, p. 39; Theorem 4.13(i) and its proof, p. 40. The absolute norm of a reconstructed multiplicative element is identified with the field norm to the minimal field Q_p. A surjective open cyclotomically compatible homomorphism preserves this norm under the canonical coefficient identification; every open injection is cyclotomically compatible. No absolutely abelian hypothesis is needed for these particular assertions. The unit case of Lemma 4.1(iii) is Nm_(K/Q_3)(u)=chi_3(rec_K(u))^(-1). [Inspected preprint version](https://www.kurims.kyoto-u.ac.jp/~yuichiro/rims1882revised.pdf#page=33). These locators refer to this preprint, not to presumed identical pages in the Hiroshima Mathematical Journal 49 (2019), 323–398 version.

These classification and norm theorems are imported, not reproved. The proof below supplies only their fixed-field logarithmic specialization and the exact witness test. Source coverage and its version qualifications are in the prior assessment `drafts/literature/2026-10-05-degree-27-nonidentity-galois-lift.md`.

## Conclusion

Every full-pair automorphism (alpha,beta) induces a well-defined bijection h of J by h(log u)=log beta(u). For some lambda_3 in Z_3^times it satisfies

\[
\operatorname{Tr}_{K/\mathbb Q_3}(h(y))
=\lambda_3\operatorname{Tr}_{K/\mathbb Q_3}(y)\quad(y\in J).
\]

The fixed g violates this necessary condition:

\[
\operatorname{Tr}(q)=48\ne0,\qquad \operatorname{Tr}(g(q))=0.
\]

Thus **no full model MLF×-pair automorphism, with any G_K component, induces g on J**. Entire units, unit torsion and the kernel of logarithmic trace are preserved; unconditional preservation of each higher unit filtration is neither used nor asserted. This stops this exact full-pair witness route. It does not exclude g from every original ind2 action, decide forgotten structures, furnish tensor/initial-theta-data realization, or demonstrate an essential IUT flaw.

## Proof

### Reconstruction supplies a reference lift with the required unit action

Put M=O_kbar^times. The reciprocity maps at all finite extensions of K, with transfer as transition maps, give the G_K-equivariant monoid isomorphism

\[
R:M\longrightarrow O^\times(G_K)
\]

of Hoshi's Proposition 4.2(i). On the fixed units O_K^times=M^(G_K), its restriction is precisely the reciprocity identification of Proposition 3.11(i). This is a selected model identification; we do not assert it is determined by the bare pair independently of all exponent choices.

Functoriality of Definition 4.1(i), the same reconstruction used in the proof of Theorem 7.6(i), gives an isomorphism (alpha,O^times(alpha)) of the reconstructed pair. Conjugating by R produces a full model pair automorphism (alpha,C), where

\[
C=R^{-1}O^\times(\alpha)R.
\]

Invariants are transported to invariants because alpha is surjective. Explicitly, if x is fixed by G_K and tau=alpha(sigma), then C(x)=C(sigma x)=tau C(x). Applying the inverse proves equality of the invariant sets. The same argument applies to beta. The invariant set of M is exactly O_K^times by the fixed-field theorem.

On these units the reconstruction acts by alpha_ab on the inertia image in G_K^ab. The cited reciprocal identification therefore gives the exact formula

\[
C(u)=\operatorname{rec}_K^{-1}\bigl(\alpha_{ab}(\operatorname{rec}_K(u))\bigr),\qquad u\in O_K^\times.
\]

This restriction is a topological unit-group automorphism: alpha_ab is continuous, the inertia image is preserved by reconstruction, and reciprocity is a topological isomorphism on the unit group. No field automorphism or valuation preservation of logarithms is inferred.

The cited absolute-norm compatibility now applies to alpha. It is an open surjective homomorphism, and Remark 4.12.1 gives cyclotomic compatibility. Its coefficient field is Q_3 on both sides, with the canonical identification, not a freely rescaled line. Proposition 4.9(i) and Theorem 4.13(i) consequently imply

\[
\operatorname{Nm}_{K/\mathbb Q_3}(C(u))=\operatorname{Nm}_{K/\mathbb Q_3}(u)\quad(u\in O_K^\times).
\tag{1}
\]

The unit formula from Lemma 4.1(iii) also makes (1) explicit: the reciprocal action is alpha_ab, chi_3 composed with alpha equals chi_3, and the valuation factor is 1 for units. Hence the two cyclotomic evaluations giving their norms agree. These are two descriptions of the same cited input, not two independent norm reconstructions.

By Theorem 7.6(ii), any other full-pair lift (alpha,beta) differs from (alpha,C) by exponentiation on the target. Thus a single lambda in Zhat^times satisfies

\[
\beta(x)=C(x)^\lambda\quad(x\in M).
\tag{2}
\]

In particular beta on O_K^times is continuous, by continuity of C there and of profinite exponentiation on the compact unit group. The theorem's torsor, rather than an assumed arbitrary-GL lifting rule, is essential here.

### Descent through the logarithm and the norm/trace specialization

For clarity, the logarithm kernel on O_K^times is exactly its torsion subgroup. If log u=0, take a positive integer m annihilating the finite quotient O_K^times/U_14. Then u^m lies in U_14 and log(u^m)=m log u=0. The inverse log/exp on U_14 implies u^m=1. Conversely a torsion unit has zero logarithm because K has characteristic zero and log is a homomorphism. This is the necessary specialization of L016's deep inverse theorem; it does not assume log is injective on all units.

Group isomorphisms C and beta preserve torsion. Therefore log u=log v implies log C(u)=log C(v) and log beta(u)=log beta(v). This defines bijections h_C and h of J, with inverses obtained from C^(-1) and beta^(-1). L018's continuous exponent calculation applied to (2) gives

\[
h(y)=\lambda_3 h_C(y)\quad(y\in J),\qquad \lambda_3\in\mathbb Z_3^\times.
\tag{3}
\]

There is no topology assertion about the completed algebraic closure hidden here: all limits for exponentiation and log are in the fixed finite field K.

For u in O_K^times we have the ordinary logarithmic norm identity

\[
\log_3\operatorname{Nm}_{K/\mathbb Q_3}(u)
=\operatorname{Tr}_{K/\mathbb Q_3}(\log_K u).
\tag{4}
\]

Here is its applicability justification in this field. Write u=(-1)^epsilon v, v in 1+pi O. In a finite normal closure E of K, every Q_3-embedding sigma sends v to a principal unit: the extended valuation is invariant under such embeddings. The convergent logarithm series commutes with sigma, since sigma is continuous and the series converges in this fixed finite extension. Its homomorphism property gives the logarithm of the finite product of the conjugates as the sum of their logarithms. The sign factors contribute zero. The product is the field norm and the sum is the field trace. On Q_3 units the same logarithm has log_3(-1)=0 and restricts compatibly from E. This proves (4) without exchanging an infinite family of conjugates or assuming K is Galois.

Apply log_3 to (1) and use (4). For y=log u this yields Tr(h_C(y))=Tr(y), independently of the chosen u representing y. Equation (3) and Q_3-linearity of trace give the claimed necessary relation Tr(h(y))=lambda_3 Tr(y) on all of J. In particular a full-pair lift preserves the trace-zero part of J. This quotient-character restriction does not identify the higher unit filtrations.

### Exact failure on the fixed logarithm

The Eisenstein polynomial X^27-3 is irreducible and separable. Its 27 roots in E are pi*zeta^j for a primitive 27th root of unity zeta and 0<=j<=26. Consequently

\[
\operatorname{Tr}(1)=27,\qquad
\operatorname{Tr}(\pi^r)=\pi^r\sum_{j=0}^{26}\zeta^{jr}=0\quad(1\le r\le26).
\]

The vanishing follows from the finite geometric sum and zeta^r!=1. Thus trace of a power-basis element sum c_r pi^r is exactly 27c_0. L017's actual q has c_0=16/9, so Tr(q)=48. Multiplication by pi has constant coordinate 3c_26; for this q it is zero. Hence

\[
\operatorname{Tr}(g(q))=54\operatorname{Tr}(\pi q)=0.
\]

Since q is in the complete J, this is a valid test input. If g were induced by any full-pair lift, the necessary relation would give 0=lambda_3*48, impossible in Q_3 because lambda_3 is a unit. This exact algebraic calculation needs no new numerical precision, logarithm recomputation, or mathematical script. It also avoids the invalid shortcut of assuming all Galois automorphisms preserve the valuation of logarithms.

The result strengthens only the restricted realization stop in L018. Hoshi's existence of some lift over every alpha remains consistent with it: that theorem does not prescribe the action g. The original comparison's actual tensor shell, permitted forgotten-structure actions, initial data, ind3, pilot, essentiality and normalized finite B>=A remain unresolved. Classification is **REPRODUCTION**, a specialization of the cited restrictions to an existing exact map, with no claim of mathematical novelty beyond the checked literature.

## Mathlib

Full matching MLF×-pair transport, absolute-norm reconstruction and this exact degree-27 nonliftability result: **not checked**. Supporting profinite exponentiation, continuous logarithm, finite-extension norm/trace and geometric-sum trace coverage: **not checked**. Named primary theorems supply the source inputs; unknown Mathlib availability is not evidence of absence. No formal verification or complete IUT resolution is claimed.
