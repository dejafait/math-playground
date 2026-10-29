# L124 — Fixed-coset products and the natural local Galois action

## Hypotheses

Let p be any prime, let Omega be an algebraic closure of Q_p, with the unique extended p-adic absolute value normalized by |p|=p^(-1), and let k be a finite extension of Q_p embedded in Omega. Put

\[
G=\operatorname{Gal}(\Omega/\mathbf Q_p),\qquad
H=\operatorname{Gal}(\Omega/k),\qquad
U_\Omega=\{u\in\Omega^\times:|u|=1\}.
\]

Let mu(Omega) be the group of all roots of unity in Omega and write M=U_Omega/mu(Omega), multiplicatively. Both occurrences of M below carry the same natural H-action. Let T be a finite set containing exactly one representative of each coset tH in G/H. No normality of H or k/Q_p is assumed. Define

\[
P_T(u)=\prod_{t\in T}t(u),\qquad
\overline P_T([u])=[P_T(u)].
\]

Automorphisms are composed as (ab)(u)=a(b(u)). In an IUT application k may be the actual K_v, with its actual inclusion H into G; this statement does not construct complete IUT initial data or identify a source Kummer operation with this formula.

## Conclusion

The map overline P_T is a well-defined group homomorphism M -> M. It is H-equivariant if and only if T={1}. Since T is a full transversal, this can occur only when k=Q_p; in that case T={1} gives the identity map.

Consequently:

- If [k:Q_p]>1, every fixed transversal T fails the required equivariance, whether or not k/Q_p is normal.
- If k=Q_p, a transversal is a singleton {t}. The identity choice works; every choice t != 1 fails. A normalized choice of the identity representative therefore has no obstruction in this degree-one case.

For every failing T there exist h in H, a finite normal extension L/Q_p in Omega containing k, and u in L with

\[
|u-1|<p^{-1/(p-1)},\qquad
R=\frac{P_T(h(u))}{h(P_T(u))}\in L^\times,
\qquad [R]\ne[1]\text{ in }M.
\]

The proof specifies a finite-dimensional witness procedure and the exact nonzero logarithmic discrepancy. It supplies an existential finite-level certificate for each given k,T, not a numerical example for unspecified native data. In particular, failure is not merely inequality of representatives that disappears after quotienting by torsion.

This is a known-method specialization of the cited slimness, embedding-independence and logarithm theorems. It stops this fixed finite-product extension mechanism. It is neither a classification of all equivariant homomorphisms nor an obstruction to the ordinary finite field norm, and does not demonstrate an essential IUT flaw, native-pilot membership or finite B>=A.

## Proof

### Imported results and their applicability

1. **Slimness.** Mochizuki, *The Absolute Anabelian Geometry of Hyperbolic Curves*, Definition 0.1(i), printed p.3, and [Theorem 1.1.1(ii), printed p.6](https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Geometry.pdf#page=6), assert that the decomposition group at a nonarchimedean place of a number field is slim. In the definition, the centralizer in that group of every open subgroup is trivial. Apply this with the number field Q and its p-place: the decomposition group is the absolute Galois group of Q_p, giving

   \[
   C_G(V)=\{1\}\quad\text{for every open subgroup }V\leq G.
   \]

   The standard identification of the decomposition group with the completion's absolute Galois group is used here, not an identification of algebraic closures with completed algebraic closures. This is the precise local consequence already covered by the invocation-start assessment. The saved author copy has SHA-256 `49719f4a75006314fee99dd704fb347b716fe140eb2705f7e38e9b57ed3980ba`. No slimness reproof is needed.

2. **Independence of embeddings.** [Stacks Project, Section 9.13, tag 0CKK, Lemma 9.13.3](https://stacks.math.columbia.edu/tag/0CKK) states that distinct field homomorphisms from a field to a field are linearly independent over the target field as functions. Below the source and target are the same finite normal field L, and the functions are distinct Q_p-automorphisms of L. The coefficients are integers, viewed in L of characteristic zero. This is linear independence; no multiplicative independence is assumed.

3. **Strict-disc logarithm and exponential.** Conrad, *Infinite Series in p-Adic Fields*, [Theorems 8.5, 8.7 and 8.13, printed pp.27–30, with the last proof through p.33](https://kconrad.math.uconn.edu/blurbs/gradnumthy/infseriespadic.pdf#page=27), supplies log(ab)=log(a)+log(b) on |a-1|,|b-1|<1, the logarithm isometry on the stricter disc, and mutually inverse maps

   \[
   \exp:D_L\longrightarrow 1+D_L,\qquad
   \log:1+D_L\longrightarrow D_L,
   \qquad D_L=\{x\in L:|x|<r_p\},\quad
   r_p=p^{-1/(p-1)}.
   \]

   Here L is finite over Q_p, hence complete with the required normalization. The strict inequality is used also for p=2; the larger principal-unit disc is not substituted. The saved author copy has SHA-256 `2b6789abb4b3e5b762b493fbf59a667bd0173f6212556098b3a6c76f9ef10e5d`. These theorems are imported, not reproved by unjustified power-series composition.

The source copies and precise inspected extracts are recorded in `drafts/sources/2026-10-26-norm-scope-sources.md`. The routine finite Galois facts used below are extension of the Q_p valuation, normal closures of finite separable extensions, and restriction to a finite normal subfield.

### Well-definedness and the finite conjugation obstruction

Every element of G preserves the absolute value and takes roots of unity to roots of unity. Thus P_T takes units to units and is multiplicative. If u is replaced by u*zeta for zeta in mu(Omega), its image changes by the root of unity product over t in T of t(zeta). This proves that overline P_T is well-defined.

Suppose first that hTh^(-1)=T for every h in H. Fix t in T. Its H-conjugacy orbit is finite, so its stabilizer C_H(t) has finite index in H. This stabilizer is closed because it is the inverse image of {t} under the continuous map h -> hth^(-1). A closed finite-index subgroup of H is open: its complement is the finite union of its other closed cosets. Since H is open in G, C_H(t) is open in G. Now t centralizes C_H(t), so the imported slimness theorem gives t=1. As t was arbitrary and T is nonempty, T={1}.

It follows that whenever T != {1}, there exists h in H such that

\[
hTh^{-1}\ne T,\qquad\text{equivalently }hT\ne Th.
\tag{1}
\]

These are equalities of finite subsets of G, not equalities in a quotient group. No quotient-group structure on G/H has been used. We next show that (1) produces failure on the torsion quotient; a mismatch of sets alone would not yet suffice.

### A finite normal field detecting the mismatch

Fix h satisfying (1), and let S=Th union hT, a finite subset of G. For each distinct pair sigma,tau in S, choose b_(sigma,tau) in Omega with sigma(b_(sigma,tau)) != tau(b_(sigma,tau)); such an element exists because these are distinct automorphisms of Omega. Let L be the normal closure over Q_p, inside Omega, of the finite extension generated by k and all these finitely many elements. Then L/Q_p is finite and normal, and every sigma in S preserves L. Moreover, their restrictions to L remain pairwise distinct, as witnessed by the chosen elements already in L.

Set

\[
c_\sigma=\mathbf1_{Th}(\sigma)-\mathbf1_{hT}(\sigma),
\qquad
D:L\longrightarrow L,\quad
D(a)=\sum_{t\in T}(th)(a)-\sum_{t\in T}(ht)(a)
     =\sum_{\sigma\in S}c_\sigma\sigma(a).
\tag{2}
\]

Left or right multiplication by h is injective, so there are no repeated elements within either Th or hT. By (1) at least one coefficient c_sigma, which lies in {-1,0,1}, is nonzero. The cited independence of the distinct restricted embeddings implies that D is a nonzero function. Choose any Q_p-basis e_1,...,e_d of L, where d=[L:Q_p]. The map D is Q_p-linear. Hence at least one basis element a=e_j satisfies

\[
D(a)\ne0.
\tag{3}
\]

This gives a finite certificate procedure after h and the separating field L are chosen: evaluate (2) on the d basis elements and retain one with (3). The assertion is existential; it assumes no effective presentation of the original profinite transversal.

### Strict-disc witness and the quotient by all torsion

Choose an integer m>=0 such that, with v_p(p)=1,

\[
m+v_p(a)>\frac1{p-1},\qquad x=p^m a.
\tag{4}
\]

Every automorphism of L/Q_p is isometric. Thus all (th)(x) and (ht)(x) belong to D_L, and the ultrametric inequality gives

\[
|D(x)|\le |x|<r_p,\qquad
D(x)=p^mD(a)\ne0.
\tag{5}
\]

Let u=exp(x). Since the series converges in the finite complete field L, u belongs to L itself and therefore to Omega; there is no use of exponential on an incomplete algebraic closure. By the imported inverse theorem u lies in 1+D_L and log(u)=x.

The set 1+D_L is a multiplicative subgroup: for y,z in D_L,

\[
|(1+y)(1+z)-1|=|y+z+yz|<r_p,
\qquad |(1+y)^{-1}-1|=|y|<r_p,
\]

because r_p<1. All the finite products and ratios below therefore remain in that same strict disc. For sigma in Gal(L/Q_p), continuity and the rational coefficients of the convergent logarithm series give log(sigma(u))=sigma(log(u))=sigma(x). Continuity is justified by the isometry of sigma; only limits within L are used.

Define

\[
R=\frac{P_T(h(u))}{h(P_T(u))}
 =\frac{\prod_{t\in T}(th)(u)}{\prod_{t\in T}(ht)(u)}\in1+D_L.
\]

The imported multiplicativity of log, applied finitely many times, now gives the exact discrepancy

\[
\log R=\sum_{t\in T}(th)(x)-\sum_{t\in T}(ht)(x)
      =D(x)=p^mD(a)\ne0.
\tag{6}
\]

If R were any root of unity in Omega, its order would be some positive integer n, and R^n=1 in L, since R is already in L. All its powers belong to 1+D_L. Consequently 0=log(R^n)=n log R, contradicting (6) in characteristic zero. This excludes roots of unity of every order, including p-power torsion; no smaller torsion quotient is being used. Thus [R] != [1] in M, which is precisely

\[
\overline P_T(h\cdot[u])\ne h\cdot\overline P_T([u]).
\]

This proves non-equivariance for every T != {1}, with a finite normal field and a strict-disc algebraic unit witness. Conversely T={1} gives the identity, so is equivariant. Since |T|=[G:H]=[k:Q_p], the conclusions for proper k and for k=Q_p follow.

### Scope of the obstruction

The proof concerns this fixed finite list of lifted embeddings acting on one copy of the algebraic units with the same natural H-action in source and target. It imposes no normality, splitting, native-data completeness or downstairs split-reduction assumption. On the ordinary k-units the usual finite norm remains well-defined; the failed requirement is its proposed extension by this same fixed product to all algebraic units. The full-packet base-change norm and operations depending on a variable finite field containing u are not tested by (2).

No statement is made about invariants commuting with a torsion quotient, continuity on a completed field, open-subgroup-indexed Kummer submodules, localization, weighted determinants, the native pilot, or the original finite B>=A assertion. In particular, an individual native place with k=Q_p admits the identity formula; this result does not assert that every native place has degree greater than one. L123 supplies only contextual separation between numerical and structured stages and is not a mathematical input to this proof.

## Mathlib

Full matching coverage is unchecked. The inspected literature assessment did not identify a matching formalization of local Galois slimness, this finite-transversal obstruction, or the combined strict-disc witness on the quotient by all roots of unity. General linear-independence documentation alone does not establish formal coverage of the cited field-embedding theorem. No Lean verification or mathematical script was performed; unknown availability is not an assertion of absence.
