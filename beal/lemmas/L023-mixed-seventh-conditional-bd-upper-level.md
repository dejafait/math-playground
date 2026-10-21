# L023 — Conditional Breuil–Diamond upper-level specialization

## Hypotheses

Let X,Y,Z be nonzero signed integers with gcd(X,Y,Z)=1 and X^5+Y^3=Z^7. Set eta=X^5/Z^7 and assume explicitly

\[
\mathbb Q[T]/(15T^7-35T^6+21T^5-\eta)
\simeq\mathbb Q[T]/(T^7-483T^2+3955T-3945).
\]

Let F=Q(sqrt(5)), t=-X^5/Y^3, and J/F be the Jacobian of y^2=5x^6-12x^5+10tx^3+t^2. Use the geometric weight-two covariant Tate component with real multiplication defined over F, in L019's normalization. Let rho be its semisimplified reduction at the coefficient prime (7), extended from F_49 through either embedding into an algebraic closure of F_7. Hodge–Tate weights below use BD's convention: epsilon has weight 1. Base primes and coefficient primes are kept distinct.

## Conclusion

For each coefficient embedding separately, there are a cuspidal Hilbert newform f over F of parallel weight two and trivial character, a coefficient prime lambda over 7 and a residual coefficient embedding such that

\[
\bar\rho_{f,\lambda}\simeq\rho,\qquad
\mathfrak n_f\mid (3)^3(\sqrt5)^3.
\]

The form and coefficient field may differ between the two embeddings. This proves conditional upper-level location, not emptiness of the branch, the exact four-level classification, packet exhaustion or a signature exclusion.

## Proof

**Sources and purpose.** The global input is [Breuil–Diamond, *Formes modulaires de Hilbert modulo p et valeurs d’extensions entre caractères galoisiens*, Ann. Sci. ENS 47(5) (2014), 905–974, author PDF Section 3.2, definition of type p. 35 and Theorem 3.2.2 pp. 36–38](https://www.imo.universite-paris-saclay.fr/~breuil/PUBLICATIONS/extensions.pdf#page=35). We use its prescribed-type modular lift, including the line and inertia-determinant conditions. A type remembers inertia and N, not Frobenius eigenvalues. Modularity is imported from [Pacetti–Villagra Torcomian (PVT), arXiv:2512.17845v1, Theorem 2.4(1), Remark 2.2 and Section 7.1](https://arxiv.org/html/2512.17845v1#S2.SS3), with (a,b,c)=(X,-Z,Y), (q,p,r)=(5,7,3), as justified in L019. PVT Theorem 7.8 already states a stronger exact-level result. The present REPRODUCTION writes the prescriptions and line checks suppressed in that interface; it does not reprove PVT's conductor tables or establish a new location theorem.

Fix one coefficient embedding. L020 and L021 give global absolute irreducibility and absolute irreducibility on G_(F(zeta_7)), respectively, with precisely the displayed algebra hypothesis. L019 gives determinant chi_7 and ramification confined to 3,5,7. Since det(rho(c))=-1 for every real complex conjugation c, rho is totally odd. F is totally real and p=7>2; BD's p=5 exception is irrelevant. PVT Theorem 2.4(1) gives modularity of the plus system at this specialization. Remark 2.2 and L019's geometric identification ensure this is the Tate component used here, rather than an additional twist. Reducing that modular component gives residual modularity, in the same sense as BD's hypothesis.

Choose psi=epsilon and S={(3),(sqrt(5)),(7)}. The quotient psi/epsilon is trivial and psi lifts det(rho). These are all the base primes required by BD. Enlarge the coefficient field finitely to contain the chosen embedding, both embeddings of F_(7), all local prescriptions and their residual characters. Also include the quadratic extension of a finite residual field of definition, as required in BD Section 3.1 p. 33; this defines eigenvalues and any residual lines. Such extension preserves irreducibility and the residual module. Each assertion below is made for the fixed embedding; no identification with the other component is imposed.

**Local lifts and their reductions.** At v=(3) and (sqrt(5)), take the original characteristic-zero geometric Tate component R_v used in L019. It has determinant epsilon and conductor exponent at most three by the cited PVT Corollary 3.6/Table 3.2 and Proposition 3.14/Table 3.5. Prescribe its type [r_v,N_v]. Do not replace its conductor by the residual conductor. Because the global residual semisimplification is irreducible, reduction of the geometric stable lattice is itself irreducible and equals rho: a module with a single simple composition factor has no proper submodule. Thus restriction of this lattice at v reduces to rho|G_(F_v), including its local extensions. In particular R_v is an actual lift of the required local module, not merely a lift of its local semisimplification.

At v=(7), take the crystalline lift R_7 of L022 with weights (0,1) at both base embeddings and determinant epsilon on the whole decomposition group. Prescribe its trivial inertial type with N_7=0. Set T={(7)} if this actual lift is potentially ordinary, and T empty otherwise. This is a choice by a property of an existing lift, not an assertion that finite flatness forces one alternative. BD permits either alternative once its additional line premise is checked.

**The ordinary line at 7.** The ordinary definition used here is [Barnet-Lamb–Gee–Geraghty–Taylor, *Potential automorphy and change of weight*, Ann. Math. 179 (2014), 501–609, Section 1.4 pp. 528–529](https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n2-p03-p.pdf#page=28): its decreasing filtration has rank-one graded characters with strictly increasing algebraic inertia exponents. Its Hodge–Tate convention assigns epsilon weight -1. For our weight pair (0,1), the rank-one subrepresentation at the end of this filtration therefore has BD weight 1 at every embedding; the quotient has weight 0. This follows from the displayed formula HT_tau={-b_tau,1,-b_tau,2} and reversal of the sign convention, not a choice of the wrong filtration line.

Suppose R_7 is potentially ordinary. Choose a finite Galois extension K'/K, K=F_(7), over which it is ordinary, and a finite coefficient field E defining the filtration line W and containing all embeddings of K'. Such finite choices exist: potential ordinarity gives a finite base extension, which can be replaced by its Galois closure; a line over the algebraic closure of the coefficient field is defined by finitely many algebraic coordinates. Restriction preserves the ordinary filtration. In rank two, Fil^2=gr^2 is the subline, whereas gr^1 is the quotient. At every embedding tau of K', the increasing exponents are b_(tau,1)=0 and b_(tau,2)=1. Thus W has BD weight 1 at **every** embedding, not just at one of the two embeddings of K.

We use [Brinon–Conrad, *CMI Summer School Notes on p-adic Hodge Theory*, preliminary version dated 24 June 2009, Theorem 5.2.1(2), pp. 68–70; Propositions 6.3.3 and 6.3.8, pp. 77–81](https://math.stanford.edu/~conrad/papers/notes.pdf#page=68), for crystalline subobjects, strict filtered exactness and filtered base change. Apply these to underlying Q_7 representations with the commuting E-action retained. Splitting K' tensor E into its embedding factors then gives the statements at each base embedding. In particular, the two weights of R_7 remain (0,1) at every embedding after finite base or coefficient extension.

The line W is unique among G_(K')-stable E-lines with constant weight profile 1. Two distinct such lines would give a direct-sum decomposition of R_7|G_(K') and weights (1,1) at every embedding, contradicting (0,1). For g in G_K, normality of G_(K') makes gW stable under G_(K'). Indeed its character on h is sigma(g^(-1)hg). Conjugation permutes the base embeddings of K', so the constant weight profile remains 1. Uniqueness yields gW=W. This establishes a line over the original **base** K; no descent of the coefficient field E is needed. The line is a subobject of a representation already crystalline over K. We are not descending crystallinity from a ramified extension. Write sigma_7 for its character. Strictness and base change give sigma_7 weight 1 at both embeddings of K.

Here is a coefficient-valid proof of the unramified assertion used at this point, replacing the short reference to L022's determinant argument. Put delta=sigma_7 epsilon^(-1). It is crystalline over K. Over K', BLGGT's algebraic inertia formula for the terminal ordinary character has exponent 1 at every embedding, the same as epsilon in that convention. Their quotient is trivial on an open subgroup of local units. Local reciprocity therefore gives finite delta(I_(K')); since I_(K') has finite index in I_K, delta(I_K) is finite as well. This already proves the finite-inertia condition actually required by BD(iv).

To verify the stronger claim that delta is unramified, choose an arithmetic Frobenius lift phi in G_K. The image of the continuous character delta is compact. Its valuation is a compact subgroup of the discrete torsion-free group Z and is therefore zero, so a=delta(phi) belongs to O_E^*. The homomorphism n -> a^(-n) extends continuously from Z to its profinite completion: modulo each power of the maximal ideal it factors through a finite cyclic group, and these maps are compatible. Thus there is an unramified E-valued character u with u(phi)=a^(-1).

Use [Brinon–Conrad, Proposition 9.3.1 and the **finite-image representation** clause of Corollary 9.3.2, pp. 146–147](https://math.stanford.edu/~conrad/papers/notes.pdf#page=146), already inspected in the saved full-audit comparison. Proposition 9.3.1 shows that the underlying Q_7 representation of u is crystalline because its inertial restriction is trivial. Tensor products and E-linear summands preserve crystallinity, so xi=delta u is crystalline too. Its inertia image is finite and xi(phi)=1. The subgroup generated by inertia and phi is dense in G_K; consequently xi has finite image, not merely finite inertial image. Apply the first clause of Corollary 9.3.2 to this finite-image Q_7 representation of dimension [E:Q_7]. It is unramified, hence trivial because its Frobenius value is one. Therefore delta=u^(-1) is unramified. This does not apply the corollary's separate Q_7-valued-character clause to an E-valued character, and it permits ramified coefficient enlargements. In particular the asserted crystalline weight-zero conclusion holds here through either coefficient embedding.

**Nonzero monodromy away from 7.** At v=(3) or (sqrt(5)), retain the original local Tate representation R_v and its actual logarithmic monodromy. The prime-to-7 construction in [Saito, *Hilbert modular forms and p-adic Hodge theory*, arXiv:math/0612077v2, Section 1, pp. 9–10](https://arxiv.org/pdf/math/0612077v2#page=9), gives an open subgroup I_0 of inertia on which R_v(h)=exp(t_7(h)N_v). Shrink I_0 to the intersection of inertia with an open normal subgroup of the full local Galois group: an open subgroup of inertia contains such an intersection, by the subspace topology and the open normal subgroup basis of a profinite group. Thus I_0 is still open in inertia and is normal in the full decomposition group. No local–global compatibility theorem or discrete-series hypothesis is needed for this local construction.

If N_v is nonzero, rank two and nilpotence imply N_v^2=0 and rank(N_v)=1. The tame character t_7 has nonzero image on every open subgroup of inertia; otherwise its surjection onto Z_7(1) would have finite image. Hence

\[
R_v(h)=1+t_7(h)N_v\quad(h\in I_0),\qquad
V^{I_0}=\ker N_v=:W_v.
\]

This equality proves stability under the **full** decomposition group: for g in that group, h in I_0 and w in V^{I_0}, one has R_v(h)R_v(g)w=R_v(g)R_v(g^(-1)hg)w=R_v(g)w. Thus W_v is a stable line in the original representation, not just in its WD parameter. Its character sigma_v is trivial on I_0 and has finite inertia image. Since epsilon is unramified away from 7, sigma_v epsilon^(-1) has finite inertia image as required. If N_v=0 and v does not divide 7, BD(iv) requests no line. In particular no assertion that monodromy remains nonzero modulo 7 is used; reducing N_v itself would not be a valid substitute for reducing this saturated line.

**Residual characters and determinants.** Use the stable lattice Lambda in each chosen actual local lift, over the ring of integers O_E of the enlarged coefficient field, with uniformizer varpi. At 3 and 5, its reduction is the actual restriction of rho because L020 makes the global semisimplified reduction absolutely irreducible; a length-one global reduction is already simple. Scalar extension of the geometric lattice retains this fact. At 7, L022 supplies a lift of the actual local module, including its extension class. Neither argument semisimplifies the local restriction.

For each required line W_v set M_v=Lambda intersect W_v. It spans W_v: multiplying any nonzero vector in that line by a sufficiently large power of varpi puts it in Lambda. It is free of rank one and saturated, since varpi x in W_v implies x in W_v. Explicitly,

\[
M_v\cap\varpi\Lambda=\varpi M_v,
\qquad
M_v/\varpi M_v\ \hookrightarrow\ \Lambda/\varpi\Lambda
       \simeq\rho|_{G_{F_v}}.
\]

Both Lambda and W_v are stable under each g and g^(-1), so g acts invertibly on M_v. Consequently sigma_v takes unit values and its reduction is the character of the displayed nonzero residual subrepresentation. Define mu_v=bar(sigma_v) chi_7^(-1). This is a continuous character in a finite residual coefficient field, and sigma_v lifts mu_v chi_7. The line, reduction, and finite inertia quotient required by BD(iv) are now checked on the chosen lift. All determinants remain epsilon, hence agree with psi on inertia. If the chosen lift at 7 is not potentially ordinary, T is empty and this line premise at 7 is vacuous; no ordinary line is forced from finite flatness.

These verifications are independent for the two coefficient embeddings: for each, L020 identifies the geometric lattice reduction and L022 supplies its local lift; the proofs above use only those properties and the uniform weights. They do not assert that the two local lifts or their lines coincide. The local-line audit secures BD(iv) under the displayed algebra hypothesis. It does not certify the separate type-to-level passage below, which remains parked for the source qualifications recorded in `drafts/literature/2026-10-05-mixed-seventh-bd-specialization-audit.md`.

**Global lift and automorphic level.** BD supplies a weight-two modular lift R of rho, unramified outside S, with global determinant epsilon and the prescribed types. Its assertion concerns existence of a form, not a unique global lift. At 7, potential semistability with trivial inertial WD action descends to semistability over K, and N=0 makes it crystalline. To see the descent, choose a finite Galois extension over which the representation is semistable. Trivial inertial descent action on D_st removes the ramified part; unramified descent of the resulting filtered Frobenius module is ordinary Galois descent. Its invariant module has full rank over K's maximal unramified subfield, giving D_st,K of full dimension. N vanishes on it, so D_cris,K has full dimension. This does not assert good reduction of the original J.

Use Carayol's local–global compatibility theorem away from p and T. Saito's at p, in the precise weight-two form restated in [BD Section 3.1 p. 33](https://www.imo.universite-paris-saclay.fr/~breuil/PUBLICATIONS/extensions.pdf#page=33), including its displayed identification of pi_v with the local Langlands representation of WD(rho_pi). BD cites Carayol, *Sur les représentations l-adiques associées aux formes modulaires de Hilbert*, Ann. Sci. ENS 19 (1986), 409–468, and Saito, *Hilbert modular forms and p-adic Hodge theory*, Compositio Math. 145 (2009), 1081–1113. This restatement is inspected; the general theorems are imported, not reproved. It identifies the local automorphic parameter with the Frobenius-semisimplified Galois WD parameter in BD's normalization, whose difference from the standard normalization is unramified. At 7 the trivial type with N=0 gives an unramified local automorphic representation; equivalently the corresponding K-type is the trivial representation of GL_2(O_K) in BD Lemma 3.2.1. Thus 7 contributes no automorphic level. At primes outside S the Galois lift is unramified, giving unramified local factors. At 3 and 5 the prescribed inertia and N preserve the entire conductor, regardless of Frobenius eigenvalues: the WD conductor is

\[
a(r_v,N_v)=a(r_v)+\dim V^{I_v}-\dim(\ker N_v)^{I_v}.
\]

Here a(r_v) is determined by its finite inertia action and ramification filtration. Frobenius semisimplification and unramified twists do not change this expression. By local Langlands for GL_2, it is the exponent of the local newvector conductor. The original R_v had exponent at most three, so the newform's exponents do also. Taking the newform in the resulting cuspidal automorphic representation gives a level dividing (3)^3(sqrt(5))^3. In the geometric weight-two normalization det(R_f)=epsilon times the finite nebentypus character. The global determinant equality epsilon forces that character to be trivial, not merely unramified at selected places.

The input embedding was arbitrary. Applying the same construction separately to the other embedding proves the second assertion; coefficient enlargement does not collapse the two components. This meets precisely the conditional upper-level threshold. The algebra hypothesis remains unproved for arbitrary solutions. The ambient form space still needs independent packet exhaustion and trace comparison, and the other Beal signatures remain unresolved. PVT's stronger exact-level theorem is retained as a known comparison, not independently reproduced here.

## Mathlib

Full matching conditional modular-location specialization: **not checked**. Supporting Hilbert modularity, prescribed-type lifting, ordinary filtrations, p-adic Hodge descent, local monodromy and local Langlands/newvector coverage: **not checked**. The named primary sources and standard compatibility theorems above are imported mathematical inputs, not matching Mathlib declarations or independently reverified general theorems. No novelty or formal verification is claimed.
