# L022 — Mixed seventh-power local crystalline lift

## Hypotheses

Use the primitive signed nonzero solution, geometric weight-two representation and residual representation rho of L019. Set K=Q(sqrt(5))_(7), now regarded as the **base** local field. Thus K/Q_7 is unramified quadratic, its residue field is F_49, and rho restricted to G_K is finite flat with determinant chi_7. Choose either embedding of the residual coefficient field F_49 into an algebraic closure of F_7.

Hodge–Tate weights use the convention of Breuil–Diamond Theorem 3.2.2: the 7-adic cyclotomic character epsilon has weight 1. No exceptional-algebra, local splitting, global absolute irreducibility or semistable-reduction hypothesis is imposed.

## Conclusion

After a finite coefficient enlargement, there is a continuous lift

\[
r:G_K\longrightarrow\mathrm{GL}_2(A),
\]

where A is the ring of integers of a finite unramified extension L/Q_7, such that:

1. r modulo the maximal ideal of A is the same local rank-two residual representation rho, including any nonsplit local extension;
2. r tensor L is crystalline, with weights (0,1) at each of the two embeddings K into L;
3. det(r)=epsilon on the whole local Galois group.

The assertion holds for either coefficient embedding, separately; it does not assert that the two chosen lifts are components of a single global compatible system. This is a REPRODUCTION of the covered local lifting mechanism. It neither assumes crystalline reduction of the original Jacobian in every valuation case nor establishes global modular location or a signature exclusion.

## Proof

**Sources and why specialization is needed.** The general inputs are [Fontaine–Laffaille, *Construction de représentations p-adiques*, Ann. Sci. ENS 15(4) (1982), 547–608, Sections 9.10–9.12, pp. 604–606](https://www.numdam.org/article/ASENS_1982_4_15_4_547_0.pdf#page=59), for finite-flat classification and the generic-fibre identification, and [Clozel–Harris–Taylor (CHT), *Automorphy for some l-adic lifts of automorphic mod l Galois representations*, Publ. Math. IHES 108 (2008), 1–181, Section 2.4.1 and Lemma 2.4.1, pp. 33–35](https://www.numdam.org/item/10.1007/s10240-008-0016-1.pdf#page=33), for coefficient-linear Fontaine–Laffaille liftability. The latter requires graded multiplicities at most one at each base embedding and does not fix the determinant. The argument below checks these differences. It uses the unchanged SPECIALIZE assessment `drafts/literature/2026-10-05-mixed-seventh-local-barsotti-tate-lift.md`; no stronger global claim is imported.

We also use the supporting simple-object and tame-inertia description in Fontaine–Laffaille Sections 4.3–4.4 and Theorem 5.3, pp. 566–570, and its integral inverse-limit and crystalline comparisons in Sections 7.14–7.15 and Theorem 8.4, pp. 593–596. These are named source inputs, not independent reproofs of Fontaine–Laffaille theory. The tame formula is used below only to compute a determinant from the two filtration multiplicities; it does not assume residual irreducibility.

**Coefficient action and rank.** Fix the chosen coefficient embedding. Descend the residual module to a finite field k_0 containing F_49, enlarged if necessary to contain F_2401 and its inertia eigenvalues. Extending coefficients preserves the underlying finite-flat property: as F_7 representations, tensoring a representation with a finite coefficient extension is a direct sum of copies. Apply L019 at the base prime (7).

Let H be a finite flat model of this underlying F_7 representation, killed by 7. Fontaine–Laffaille 9.11–9.12 gives a filtered module M with Fil^0 M=M, Fil^2 M=0 and contravariant generic-fibre functor U_S(M)=rho. Generic-fibre full faithfulness in this range transports every k_0 coefficient endomorphism to M. The action is contravariant, but k_0 is commutative, so it is still a field action. Uniqueness preserves its addition, multiplication and unit identities. Thus M is a module over

\[
\mathbf F_{49}\otimes_{\mathbf F_7}k_0\simeq k_0\times k_0.
\]

Write M_0,M_1 for its two base-embedding summands. Divided Frobenius is coefficient-linear and permutes these summands; modulo 7 its map from gr M to M is an isomorphism. Consequently dim_(k_0) M_0=dim_(k_0) M_1. The length/rank comparison for the functor gives their sum as 2 dim_(k_0) rho=4. Hence each M_j has dimension two. This verifies coefficient rank, rather than inferring it from the underlying F_7 dimension without decomposing the base action.

**The determinant forces both filtration multiplicities.** Put

\[
d_j=\dim_{k_0}\operatorname{Fil}^1 M_j\in\{0,1,2\},\qquad j=0,1.
\]

Normalize a level-two fundamental character omega_2 so that chi_7 on inertia is omega_2^8. The Fontaine–Laffaille simple-object formula gives

\[
\det U_S(M)|_{I_K}=\omega_2^{d_0+7d_1},
\tag{1}
\]

up to cyclically relabeling the two base embeddings. Here is the relevant specialization of that formula, including the local irreducible case. For a scalar local constituent, Frobenius conjugates tame inertia by its 49th power. Its inertia character therefore has level dividing two; its Fontaine–Laffaille digits are i_0,i_1 in {0,1}, and its character is omega_2^(i_0+7i_1). These digits are the filtration degrees at the two embedding summands. In a locally reducible module, apply this to the submodule and quotient. Exactness and strictness of the filtered functor add their filtration dimensions, and determinants multiply. This proves (1) also for a nonsplit extension.

If the local module is absolutely irreducible of dimension two, wild inertia is trivial: invariants under its finite 7-group image are nonzero and stable under G_K, hence fill the module. Tame inertia is semisimple. Scalar inertia would leave a Frobenius eigenline invariant; otherwise its two eigenlines must be interchanged by Frobenius. Their characters are omega_4^s and omega_4^(49s), where omega_4^50=omega_2. The simple-object classification and Theorem 5.3 express

\[
s=i_0+7i_1+49i_2+343i_3,\qquad i_j\in\{0,1\}.
\]

The Frobenius orbit visits each base embedding twice, so its filtration dimensions are d_0=i_0+i_2 and d_1=i_1+i_3, after a possible cyclic relabeling. The determinant is omega_2^s, and s modulo 48 is d_0+7d_1. This proves (1) in this case too. If the representation becomes locally reducible only after coefficient enlargement, the first case applies over that enlargement; dimensions and determinants are unchanged. These cases concern the local module only and do not use L020 or L021.

L019 gives det(rho)=chi_7. Since omega_2 has order 48, (1) implies

\[
d_0+7d_1\equiv8\pmod{48}.
\]

The integer on the left lies between 0 and 16, so it equals 8. If d_1=0 then d_0=8 is impossible; if d_1=2 then d_0=-6 is impossible. Therefore d_0=d_1=1. Cyclic relabeling gives the same conclusion. At each embedding, gr^0 M and gr^1 M consequently both have dimension one; all other graded pieces vanish. This supplies CHT's regular-multiplicity hypothesis.

**Convention and compatible integral lifts.** Take A=W(k_0) and L=Frac(A). It contains both embeddings of the unramified quadratic base K. At p=7 CHT defines its covariant functor by

\[
G(M)=U_S\bigl(\operatorname{Hom}(M,K/O_K\{5\})\bigr)(-5).
\]

This is the complementary filtered dual: a filtration degree i becomes 5-i; U_S has cyclotomic weight 5-i, and the displayed Tate twist subtracts 5. Thus G has weight -i. Equivalently the perfect complementary evaluation pairing identifies G(M) with U_S(M)^vee. The dual here is coefficient-linear: the trace pairing for the finite étale extension k_0/F_7 identifies its coefficient dual with its underlying F_7 dual, with coefficient action by precomposition. The same identification holds integrally for the unramified coefficient ring A. Thus no coefficient embedding or action is lost in taking this dual. The complementary degrees 4 and 5 stay in CHT's allowed range 0 through p-2; the original degrees are 0 and 1. This is precisely the dual/twist conversion in CHT Section 2.4.1, not a further twist of a finite-flat geometric representation. Hence our M is in the covariant image for rho^vee, with the graded multiplicities just verified.

Apply CHT Lemma 2.4.1 successively to A/7^(n+1) -> A/7^n. Each kernel is killed by the maximal ideal, as required for a small extension. Its filtered-basis proof lifts the direct-summand filtration and divided-Frobenius maps while keeping their ranks. Choose each lift compatibly with the preceding one, and lift the chosen residual frame. No semisimplicity of the local representation is a hypothesis of that proof, so this procedure lifts rho^vee itself, including its extension class.

The inverse limit is a free rank-two A lattice with a continuous G_K action. More explicitly, the embedding summands have compatible free rank-two bases; their Fil^1 summands have rank one; and divided Frobenius maps have compatible limits generating the module. After inverting 7 this is a strongly divisible filtered module. Fontaine–Laffaille 7.14–7.15 identifies its Galois lattice with the inverse limit of the finite-level lattices. Apply 8.4 to the underlying Q_7 representation over the unramified base K, retaining its commuting coefficient action, and use CHT's complementary dual and twist. This identifies the rational representation as crystalline without requiring the enlarged coefficient field to be a subfield of K. Thus no mere collection of unrelated Artinian lifts is substituted for a characteristic-zero lift. CHT's covariant lift r_* has weights (0,-1). Dualize its free lattice to obtain r_0=r_*^vee, reducing to rho and having weights (0,1) at each embedding. Crystalline representations are closed under duality. Reduction of the free dual lattice is the residual dual, so this step restores the original module exactly.

**Full determinant correction.** The character

\[
\delta=\det(r_0)\epsilon^{-1}
\]

is crystalline, has weight zero at both embeddings, and reduces to one on all of G_K. A rank-one crystalline character with all weights zero is unramified. In the present small-weight situation this also follows directly from the filtered description: its rank-one module has only Fil^0, and the product of the Frobenius maps around the base-embedding cycle is a unit by weak admissibility. The unramified character with that Frobenius scalar has this filtered module. The crystalline equivalence (Fontaine–Laffaille 8.1 and 8.4) identifies the two characters. In particular there is no finite ramified weight-zero character left over; weight zero alone without crystallinity would not suffice.

For arithmetic Frobenius phi, set a=delta(phi) in 1+7A. Since 2 is a unit, Hensel's lemma gives a unique b in 1+7A with b^2=a^(-1). Define the unramified character u by u(phi)=b. This is continuous: the powers of b extend from the integers to Z_7, and the unramified quotient maps continuously from the profinite integers to Z_7. It reduces to one and is crystalline of weight zero. The equality u^2=delta^(-1) holds on the whole unramified quotient and both characters are trivial on inertia. Finally put

\[
r=r_0\otimes u.
\]

Then det(r)=det(r_0)u^2=epsilon on G_K. The twist preserves crystallinity, the two weight multisets, and the full residual module because u is identically one modulo 7. This corrects the whole determinant, rather than only its inertia restriction. The construction works for the initially arbitrary coefficient embedding, proving the stated assertion through both embeddings separately.

**Threshold and remaining gaps.** The local threshold is achieved: same residual module, weights (0,1) at both base embeddings, and full cyclotomic determinant. This is a useful local input for a prospective Breuil–Diamond prescribed-type application. Global prescriptions at 3 and 5, ordinary/nonordinary choices at 7, the global theorem application, modular-packet exhaustion and exceptional-algebra applicability remain separate. Uniform residual-signature emptiness remains unproved. None of the local lifts is asserted to come from the original Jacobian with good reduction at 7.

## Mathlib

The full matching local-lift specialization and its supporting finite-flat, Fontaine–Laffaille, crystalline and determinant-correction results: **not checked**. The cited primary theorems are mathematical inputs; no Mathlib absence, formal verification or progress beyond the checked literature is claimed.
