# L125 — Variable-degree normalized norm on algebraic units

## Hypotheses

Let p be any prime, let Omega be an algebraic closure of Q_p with its unique extended p-adic absolute value, normalized by |p|=p^(-1), and let k/Q_p be a finite embedded extension. Set

\[
d=[k:\mathbf Q_p],\qquad H=\operatorname{Gal}(\Omega/k),\qquad
U_\Omega=\{u\in\Omega^\times:|u|=1\},\qquad
M=U_\Omega/\mu(\Omega),
\]

where mu(Omega) is the group of all roots of unity in Omega. Both occurrences of M have the same natural H-action. For u in U_Omega, choose any finite subextension L/Q_p in Omega containing k and u, and consider

\[
F_k([u])=[N_{L/\mathbf Q_p}(u)]^{\,d/[L:\mathbf Q_p]} . \tag{1}
\]

Rational powers here are operations in M, not selected roots in Omega. Neither k nor L is assumed normal over Q_p. No completion of Omega, topology on M, Kummer submodule or IUT initial data is assumed.

## Conclusion

Formula (1) is a well-defined H-equivariant group homomorphism M to M. In particular, it is independent of L and of the representative of [u]. For every unit a in k,

\[
F_k([a])=[N_{k/\mathbf Q_p}(a)]. \tag{2}
\]

Equality (2) is equality of classes in M; no preferred lift of F_k to units is asserted. All conclusions hold also for p=2 and nonnormal L. This is a known-method local specialization of normalized norms modulo torsion, not a new norm-theory theorem or an IUT counterexample. Its compatibility with any source-specified structured comparison is not established.

## Proof

### Imported inputs and scope of the specialization

Use the finite-field norm defined as the determinant of multiplication in [Stacks Project, Definition 9.20.1, tag 0BIF](https://stacks.math.columbia.edu/tag/0BIF). The discussion following that definition gives multiplicativity and N_(B/A)(a)=a^[B:A] for a in A. [Lemma 9.20.5, tag 0BIJ](https://stacks.math.columbia.edu/tag/0BIJ) supplies transitivity in any finite tower. Equivalently, Conrad, [*Trace and Norm, II*, Theorem 4.3, printed pp.5–7](https://kconrad.math.uconn.edu/blurbs/galoistheory/tracenorm2.pdf#page=5), covers all finite towers, including the nonnormal case. We import these results without reproving them.

For unit preservation use [Stacks Lemmas 9.20.2–3, tags 0BIG–0BIH](https://stacks.math.columbia.edu/tag/0BIG): if P is the minimal polynomial of u over Q_p, the characteristic polynomial of multiplication by u on L is P^e, with e deg(P)=[L:Q_p], and the norm is its determinant. Each conjugate of u has the same absolute value as u, by the following precise inputs.

Import Brian Conrad, [*Some basics concerning absolute values*, Lemma 6.1, printed p.10, and Theorem 6.4, p.11](https://math.stanford.edu/~conrad/676Page/handouts/ostrowski.pdf#page=10). The base Q_p is complete and nontrivially valued; Omega/Q_p is algebraic. Thus the absolute value exists uniquely on Omega; completeness is asserted for finite extensions, not for Omega. For every Q_p-automorphism g of Omega, x -> |g(x)| is another extending absolute value, so |g(x)|=|x|.

For a Q_p-embedding j:Q_p(u) -> Omega, regard the target Omega as an algebraic closure of Q_p(u) via j. [Stacks Lemma 9.10.5, tag 09GU](https://stacks.math.columbia.edu/tag/09GU), applied to the algebraic extension Omega/Q_p(u), extends j to an embedding of Omega into that target. Its image is algebraically closed and the target is algebraic over that image, so the embedding is surjective, as in [Lemma 9.10.6, tag 09GV](https://stacks.math.columbia.edu/tag/09GV). It is therefore a Q_p-automorphism. Every root of P is obtained by such a j. All characteristic roots are consequently units, and their product, the norm, has absolute value one. Thus N_(L/Q_p)(u) belongs to Z_p^times and defines a class in M. No normality of L is used. These imported inputs were covered by the separate audit gate; this paragraph makes their applicability explicit rather than reproving valuation or extension theory.

The general quotient inputs are torsion-freeness after quotienting an abelian group by its full torsion subgroup ([Stacks Lemma 15.22.2](https://stacks.math.columbia.edu/tag/0549), with coefficient ring Z), and the Q-vector structure of a torsion-free divisible abelian group (IIT Kanpur, [*MTH302: Set Theory and Mathematical Logic*, PDF pp.160–161](https://home.iitk.ac.in/~krashu/mth302.pdf#page=160), “Torsion free divisible abelian groups”). Below we verify their local hypotheses and spell out the root operation to exclude a hidden choice of representatives.

For comparison, Fili–Miner, [*Orthogonal Decomposition of the Space of Algebraic Numbers and Lehmer's Problem*, April 3, 2010 author copy, §2.3, equation (2.2), p.9; Lemma 2.14, pp.11–12](https://web.ma.utexas.edu/users/zminer/norms.pdf#page=9), already use normalized norms modulo torsion and conjugation covariance for algebraic numbers. Their global height topology is not imported here. The work required here is the local unit restriction, normalization by d, and the stated natural H-action. Source versions and inspected ranges are recorded in `drafts/sources/2026-10-26-variable-norm-sources.md`. This proof does not claim new mathematics beyond those known methods.

### Rational powers and the natural action

Every root of unity is a unit: zeta^n=1 implies |zeta|^n=1. The torsion subgroup of U_Omega consists exactly of these elements. If u is a unit and n is a positive integer, algebraic closedness supplies r in Omega with r^n=u, and |r|^n=1 implies r is a unit. Thus U_Omega, and hence M, is divisible. If [u]^n=1 in M, then u^n is a root of unity; raising to its finite order shows u itself is a root of unity. Thus M is torsion free, and the nth-power map on M is bijective for each positive n.

For q=m/n with m an integer and n>0, x^q is therefore the unique y in M satisfying y^n=x^m. Explicitly, choose r in Omega with r^n=u^m for x=[u], and set y=[r]; r is a unit. Distinct choices of r differ by an nth root of unity. Changing u by a root of unity also changes [r] by no class: if r'^n=(u*zeta)^m, then (r'/r)^n=zeta^m is torsion, so r'/r is torsion. The definition is independent of the expression for q: if m/n=m'/n', the two candidate classes have equal (nn')th powers, so torsion-freeness makes them equal. The usual exponent composition and product identities follow in the same way by taking a common positive denominator and using injectivity of that power map. These arguments work for negative and zero m as well.

Every Q_p-automorphism of Omega preserves the absolute value by uniqueness, and preserves all roots of unity, so it acts on M by a group automorphism. Such an automorphism commutes with rational powers: applying it to y^n=x^m identifies the unique nth root of the transformed x^m. These facts justify all rational powers and actions in (1).

### Independence of the finite field and the torsion representative

If W/L/Q_p is a finite tower and u belongs to L, the imported power and tower formulas give

\[
N_{W/\mathbf Q_p}(u)
=N_{L/\mathbf Q_p}(N_{W/L}(u))
=N_{L/\mathbf Q_p}(u)^{[W:L]}.
\]

Since [W:Q_p]=[W:L][L:Q_p], uniqueness of rational powers in M gives

\[
[N_{W/\mathbf Q_p}(u)]^{d/[W:\mathbf Q_p]}
=[N_{L/\mathbf Q_p}(u)]^{d/[L:\mathbf Q_p]}. \tag{3}
\]

For two allowed choices L and L', their compositum W=LL' is a finite field in Omega containing both, so (3) identifies the answers. This does not require either extension to be normal.

If u'=u*zeta, with zeta in mu(Omega) of order n, choose a finite W containing k,u,zeta and both fields used to evaluate the two proposed values. Multiplicativity of the ordinary norm gives

\[
N_{W/\mathbf Q_p}(u')=N_{W/\mathbf Q_p}(u)N_{W/\mathbf Q_p}(\zeta),
\qquad N_{W/\mathbf Q_p}(\zeta)^n=N_{W/\mathbf Q_p}(1)=1.
\]

The latter norm is torsion, so the two norm classes agree in M. Taking their common rational power and applying (3) proves representative independence. This includes roots of unity of every order, including p-power torsion.

### Homomorphism and equivariance

For u,v in U_Omega choose one finite W containing k,u,v. Multiplicativity of N_(W/Q_p) and of rational powers in M gives

\[
F_k([uv])
=[N_{W/\mathbf Q_p}(u)N_{W/\mathbf Q_p}(v)]^{d/[W:\mathbf Q_p]}
=F_k([u])F_k([v]).
\]

The independence already proved makes this a statement about classes, not just these representatives.

Fix h in H and choose L containing k,u. Then h(L) is a finite field containing k,h(u), with [h(L):Q_p]=[L:Q_p]; h fixes k pointwise. For a Q_p-basis e_1,...,e_n of L, the images h(e_i) form a basis of h(L). If A is the multiplication matrix for u in the first basis, applying h to its entries leaves them unchanged because they belong to Q_p. The multiplication matrix for h(u) in the second basis is therefore exactly A. The determinant definition of the norm yields

\[
N_{h(L)/\mathbf Q_p}(h(u))=N_{L/\mathbf Q_p}(u).
\]

Consequently F_k(h[u])=F_k([u]). On the other hand N_(L/Q_p)(u) belongs to Q_p^times and is fixed by h. Since h commutes with the unique rational powers in M,

\[
hF_k([u])=h\bigl([N_{L/\mathbf Q_p}(u)]^{d/[L:\mathbf Q_p]}\bigr)
=[N_{L/\mathbf Q_p}(u)]^{d/[L:\mathbf Q_p]}
=F_k([u]).
\]

These two equalities give F_k(h[u])=hF_k([u]), the required equivariance. In fact the output class is fixed by every element of Gal(Omega/Q_p), by the same uniqueness-of-division argument. A chosen root representing that class need not itself belong to Q_p; invariance is asserted only in M.

### Agreement with the ordinary norm and limitations

For a in k with |a|=1 take L=k. The exponent in (1) is then d/d=1, proving (2). All other choices of L give the same class by (3). No statement about a choice of root in Q_p or a unit-valued lift is needed. Every step used finite characteristic-zero extensions and algebraic roots of units, so p=2 is included without an analytic convergence threshold. Nonnormal k,L were explicitly allowed in the tower, compositum and conjugation arguments.

The construction test and the separate step517 critical audit pass at the bare-group level. A fixed transversal is not used. This does not contradict the separate obstruction for fixed products, and that obstruction is not an input to the proof. A fixed output class and equivariance do not establish preservation of retained integral Kummer data, continuity, a prime-strip isomorphism, global localization, weighted determinant compatibility, native-pilot membership or finite B>=A. Those requirements remain unresolved.

### Critical audit, step517

The audit preserves the statement, formula, quotient and both natural H-actions. No mathematical error was found within this scope. Precise valuation and embedding citations and their applicability were added above; no hypothesis was strengthened to obtain the pass. The following potential failure points were checked against the full proof.

- **Division before choosing a field.** Power maps are bijective on M because roots exist in Omega and a finite power that is torsion forces the original element to be torsion. No surjectivity on the units of a fixed finite field is assumed. The proof takes rational powers only in M. For n divisible by p, and in particular at p=2, this same algebraic argument applies; no logarithm convergence or inverse in an integral lattice is assumed. Negative exponents are permitted because all representatives are nonzero units.
- **Unit preservation and all choices of finite field.** The imported theorems above apply to every finite L, not just a normal extension. Finite composita exist inside the algebraic closure. Equation (3) is an identity of classes obtained from the tower norm and the exact degree identity; rational exponent composition is already justified before its use. Comparing any two L through their compositum therefore covers nonnested choices as well as enlargements. No limit over fields is taken.
- **Torsion and products.** For two representatives, the common finite field contains the torsion multiplier and both original evaluation fields. Its norm of that multiplier has finite order, even for p-power roots of unity, so it dies in precisely the full torsion subgroup used to define M. Applying one common rational power and then (3) is valid. The product argument similarly uses one field containing both units before multiplying their norms; it does not multiply expressions with unrelated denominators without comparison.
- **Nonnormal action and fixed classes.** The proof never requires h(L)=L: h(L) is another allowed field because h fixes k, and the transported bases give identical matrices over Q_p. This verifies the input-side equality F_k(h[u])=F_k([u]). Separately, if x is the fixed norm class and y^n=x^m, then (hy)^n=x^m; injectivity of the power map gives hy=y. This verifies the output-side equality, without concluding that any representative of y is fixed. Together these are equivariance for the same natural actions, not for a substituted trivial action on the ambient codomain.
- **Restriction and boundary cases.** L=k is allowed for every k-unit and makes the exponent exactly one. Equation (3) extends that equality to every other evaluation field. For k=Q_p, agreement is asserted on Q_p-units; the proof does not claim the map is the identity on all of M. No step excludes p=2 or nonnormal k. Algebraic closedness, rather than completeness of Omega, supplies the required roots. Agreement is classwise throughout.

The audit therefore validates an input for possible later structured work; it establishes no result beyond the known normalized-norm methods cited above. The structured requirements in the preceding paragraph are outside the audit, not silently discharged by it.

## Mathlib

The invocation-start assessment inspected [Mathlib RingTheory.Norm.Transitivity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Norm/Transitivity.html#Algebra.norm_norm). Supporting declarations are `Algebra.norm_norm`, `Algebra.norm_eq_norm_adjoin` and `Algebra.norm_eq_prod_embeddings`; the embedding formula assumes a finite separable extension and an algebraically closed receiving field, as available here. These are finite-norm inputs, not a matching theorem for (1). Full Mathlib coverage of this particular unit quotient, rational powers and action statement has not been checked; no absence claim or Lean verification is made.
