# L023 — A source-realized square-zero reference action in degree 27

## Hypotheses

Let K=Q_3(pi), pi^27=3, fix an algebraic closure kbar, and put G=Gal(kbar/K), O=O_K, J=log(O^times), and I=J/6. Use the full model MLF×-pair G acting on M=O_kbar^times. Use L016's continuous unit logarithm, torsion kernel as justified in L019, and deep ideal H=pi^14 O contained in J. Use L019's selected reciprocity reconstruction isomorphism R:M → O^times(G), reference lift, and exponent-torsor descent; L018 supplies the continuous exponent/logarithm formula used there.

Import **Hoshi–Nishio, On the Outer Automorphism Groups of the Absolute Galois Groups of Mixed-characteristic Local Fields**, author-hosted **June 2022 revised RIMS1931**, §1 setup and logarithm diagram, PDF pp. 3–4; **Theorem 1.5 and proof, PDF p. 5**; and the logarithm compatibility in the proof of **Lemma 2.3(ii), PDF pp. 7–8** ([primary text](https://www.kurims.kyoto-u.ac.jp/~yuichiro/rims1931revised.pdf)). For a group of MLF-type with odd p(G) and d(G)>1, Theorem 1.5 supplies an automorphism alpha whose induced action a on k_+(G) is nonidentity and satisfies (a-id)^2=0. We use its n=1 case. The source setup identifies p(G_K), d(G_K) with residue characteristic and absolute degree, and identifies K additively with k_+(G_K) through reciprocity and logarithm. These are cited inputs; neither the presentation theorem nor Theorem 1.5 is reproved.

The full-pair input is **Hoshi, Introduction to Mono-anabelian Geometry**, Publications mathématiques de Besançon (2021), 5–44, DOI 10.5802/pmb.42, **Proposition 3.11(i,iv), p. 22**, Definition 4.1(i), **Proposition 4.2(i,iii), pp. 25–26**, Definition 5.5 and Remark 5.5.1, p. 30, and **Theorem 7.6(i–ii), pp. 39–40** ([published primary text](https://www.numdam.org/item/10.5802/pmb.42.pdf)). Its application and model identifications are justified in L019. The two logarithm diagrams and their compatibility are made explicit below. No geometricity or higher-unit-filtration preservation is assumed.

## Conclusion

There exist alpha in Aut(G) and a full-pair reference lift (alpha,C) whose logarithmic action extends to a Q_3-linear automorphism h of K such that

\[
h(J)=J,\qquad h(I)=I,\qquad h|_J\ne\mathrm{id}_J,\qquad (h-\mathrm{id}_K)^2=0.
\]

For this alpha, every other full-pair lift induces lambda_3 h on K, where lambda_3 is a unit of Z_3. The square-zero assertion is for the chosen reference action; it is not asserted for every such twist.

This is a specialization of known existence and lifting results, classified **REPRODUCTION**. It does not identify h with L022's shear, specify any field-valued witness or power-basis matrix, or establish an envelope bound, a native IUT action or an essential IUT flaw.

## Proof

**Applicability.** By L016's Eisenstein calculation, K is a finite degree-27 extension of Q_3 with residue characteristic 3. Thus G is of MLF-type, p(G)=3 is odd and d(G)=27>1. Theorem 1.5 needs no even-degree, Galois-over-Q_3 or absolute-abelianness hypothesis. Choose the supplied alpha and additive action a. Let F:K_+ → k_+(G) be the source's reciprocity/logarithm identification, with the canonical Q_3 coefficient structure. Set h=F^(-1)aF. It is Q_3-linear and invertible. Conjugation gives (h-id)^2=0 and h≠id.

**Agreement with an actual full-pair lift.** Use the selected R of L019 and put C=R^(-1)O^times(alpha)R. Functoriality gives (alpha,C) as a full model pair automorphism. L019 proves that its restriction to O^times is the reciprocal unit action, including topological continuity and invariance of the fixed units. The source's §1 logarithm diagram identifies the additive rationalization of principal units with K_+. Equivalently, the logarithm compatibility displayed in the proof of Lemma 2.3(ii) states, under these same reciprocal identifications,

\[
h(\log u)=\log C(u)\quad(u\in O^\times).
\]

Here is the precise compatibility of the choices, checked in the critical audit. Write U_rec for the reconstructed fixed-field units, U_bar,rec for the reconstructed algebraic-closure units, r:O^times → U_rec for Proposition 3.11(i), and j:U_rec → U_bar,rec for the base-field inclusion in Definition 4.1(i). If i:O^times → M is inclusion, Proposition 4.2(i), constructed using reciprocity and transfer, gives R i=j r. In particular j is injective. Functoriality gives O^times(alpha) j=j alpha_U, where alpha_U is the fixed-field reconstructed action. Thus C preserves the fixed units and r C=alpha_U r on them. This follows from the selected R, rather than from arbitrary lift existence.

Let ell:U_rec → k_+(G) be the natural rationalization map. Proposition 3.11(iv) gives F log=ell r, and the reconstructed action satisfies a ell=ell alpha_U. Hoshi–Nishio §1 explicitly uses this same diagram. Therefore, for u in O^times,

\[
F\log C(u)=\ell rC(u)=\ell\alpha_U r(u)
=a\ell r(u)=aF\log u=Fh(\log u).
\]

Injectivity of F proves the asserted equality. Proposition 4.2(iii) is the compatible full-object logarithm diagram; restriction through the same base-field inclusion recovers this calculation. No interchange of invariants with rationalization, or continuity on the completed algebraic closure, is needed.

For the principal-unit formulation in Hoshi–Nishio §1, C preserves principal units by the left-hand square of Proposition 3.11(i). Every unit of this field is a sign times a principal unit; C fixes the sign because -1 is the unique nonidentity element of order two in O^times. Both signs have logarithm zero. L019's torsion-kernel argument also verifies independence of a representative under log, without assuming injectivity of log on all units. Applying the equality to C and its inverse yields h(J)=J. The natural map into the log-shell in Proposition 3.11(iv) is log itself; its image is J, whereas the shell is I=J/6. Q_3-linearity gives h(I)=I without replacing J by I in the unit diagram.

**Nonidentity on the genuine image.** H⊆J by L016: the inverse log/exp theorem applies at 14/27>1/2. Its displayed basis for H consists of 3pi^r for 0≤r<14 and pi^r for 14≤r≤26. These 27 vectors are a Q_3-basis of K, so H is a full Z_3-lattice and J spans K over Q_3. No numerical certificate or finite logarithm approximation is needed for this spanning claim. If h fixed every element of J, linearity would force h=id on K, contrary to Theorem 1.5 transported by F. Thus the restriction to J is nonidentity. This establishes existence of a genuine logarithm moved by h without labeling a source-presentation basis vector as a power-basis element or claiming a particular logarithm is moved. The square-zero identity restricts to J as well.

**Exponent ambiguity.** L019's full-pair torsor says that any other lift beta over alpha is C followed by one profinite-unit exponent lambda. L018's continuous exponent calculation, reused by L019, gives log beta(u)=lambda_3 log C(u). Therefore its induced action on J is lambda_3 h, and its Q_3-linear extension to K is the same scalar multiple because J spans K. For clarity, writing N=h-id gives

\[
(\lambda_3h-\mathrm{id})^2
=(\lambda_3-1)^2\mathrm{id}+2\lambda_3(\lambda_3-1)N,
\qquad N^2=0.
\]

Thus no transfer of the reference square-zero assertion to arbitrary twists is used. All logarithmic limits are in the fixed finite field, as in L018–L019.

**Scope and downstream test.** The continuation test required an action on the fixed logarithm image and an actual full-pair reference lift; both are obtained. The existence theorem provides no identification of its presentation coordinates with this notebook's q_1, q_2 or power basis. Consequently it supplies no radius, no violating field-valued point and no realization of the prescribed L022 map. It could serve as a reference input to a separately assessed coordinate or bound test. Original ind2/native identification, actual ind3 input, initial theta data, higher powers, pilot transport, essentiality and finite B≥A remain independent unresolved gaps.

## Mathlib

Full matching Hoshi–Nishio square-zero existence and Hoshi full-pair reconstruction/lifting coverage: **not checked**. Supporting Q_3-linear conjugation, lattice spanning, continuous logarithm and exponentiation coverage: **not checked**. Unknown availability is not evidence of absence. Primary named theorems supply the essential inputs; this notebook gives only their fixed-field applicability and compatibility specialization, without claiming novelty or formal verification.
