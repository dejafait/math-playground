# L122 — Fixed-embedding visibility of a compatible Sha tower

## Hypotheses

Let E/Q be an elliptic curve with good reduction at p >= 5. Use L005's
classical Selmer groups and transition conventions, and put

\[
M=\varprojlim_n\operatorname{Sel}_{p^n}(E/\mathbf Q),\qquad
S=M\otimes_{\mathbf Z_p}\mathbf Q_p,\qquad
\widehat{E(\mathbf Q)}_p=\varprojlim_n E(\mathbf Q)/p^nE(\mathbf Q).
\]

Let k=(k_n) belong to M, and let c_n be the image of k_n in
Sha(E/Q)[p^n]. Thus p c_{n+1}=c_n. Suppose J/Q is an abelian variety
and i:E -> J is one fixed closed immersion of abelian varieties over Q
(in particular, a group homomorphism), such that

\[
i_*(c_n)=0\quad\hbox{in }H^1(\mathbf Q,J)\quad\text{for every }n\ge1.
\tag{1}
\]

There is no assumption that all of Sha, or its p-primary part, is finite.
Existence of i satisfying (1) is an additional arithmetic premise.

## Conclusion

Every c_n is zero. The class k is the Kummer image of a unique element
of the p-adic completion \(\widehat{E(\mathbf Q)}_p\). Consequently its
rationalization belongs to L005's image j(E(Q) tensor Q_p).

More generally, for a rational class kappa in S, choose a single a >= 0
and k in M with k tensor 1 = p^a kappa. If (1) holds for this integral
lift's entire Sha tower, then kappa belongs to that rational Kummer image.
If also kappa != 0 and lambda_p(kappa)=0, L005 gives rank E(Q) >= 2.
The condition k != 0 alone does not replace rational nonvanishing.

For a given compatible tower (c_n), existence of some fixed embedding
satisfying (1) is equivalent to c_n=0 for all n: the reverse implication
uses J=E and i=id. Thus this is a conditional criterion, not an independent
construction of rationality. Pointwise embeddings i_n:E -> J_n cannot
be substituted. No generalized Kato class, fixed ambient construction,
analytic-order comparison, or BSD case is produced.

## Proof

**Published finiteness input and applicability.** Agashe--Stein,
*Visibility of Shafarevich--Tate Groups of Abelian Varieties*,
J. Number Theory 97 (2002), 171--185, DOI 10.1006/jnth.2002.2810,
[Section 1.1, Definition 1.1, equation (1.1) and its following finiteness
paragraph, printed pp.172--173](https://wstein.org/papers/visibility_of_sha/jnt_version.pdf#page=3),
prove that

\[
G_i=\ker\bigl(H^1(\mathbf Q,E)\xrightarrow{i_*}H^1(\mathbf Q,J)\bigr)
\]

is finite. This is the fixed-embedding theorem over a number field;
Q, E, J and i meet exactly its hypotheses. In their notation the
embedding is suppressed in Vis_J, but it is fixed. Import this result;
no reproof or construction theorem from their Section 3 is needed.
Their Definition 1.2 identifies visible Sha with the intersection
Sha(E/Q) intersect G_i, so (1) places all c_n in the same finite group.
The source's Proposition 1.3, printed pp.173--174, instead chooses an
ambient variety for each individual class and supplies no such common
group. The ordinary/non-CM hypotheses of other notebook results are
unnecessary for this visibility input. Good p >= 5 is retained for the
stated strict-rank application of L005.

**Uniform exponent and transitions.** The p-primary subgroup of G_i
is finite. Choose b >= 0 such that p^b kills it. Every c_n lies in that
subgroup. For each n, compatibility through exactly b successive levels
gives

\[
c_n=p^b c_{n+b}=0.
\tag{2}
\]

For b=0 the subgroup itself is zero. The same b works for every n,
because i and G_i do not change. This argument neither computes b nor
asserts a bound for all of Sha. With varying embeddings, finiteness at
each level supplies no common b and does not justify (2).

**Integral Kummer passage.** Use the finite-level Kummer exact sequence,
with no finite-Sha assumption, cited in
[the standard inputs](../foundations/02-standard-inputs.md): Milne,
*Elliptic Curves*, second edition (2021), Chapter IV, equation (29),
printed p.113, and the transition diagram on printed p.129.
By (2), each k_n has a unique point-quotient preimage
x_n in E(Q)/p^n E(Q). Reduction of x_{n+1} has Kummer image k_n,
since Selmer transitions are induced by [p] on torsion coefficients.
Injectivity of the level-n Kummer map therefore makes that reduction
equal to x_n. Hence (x_n) is the required element of the completion;
finite-level injectivity also proves uniqueness. This uses only the
kernel of the inverse-limit map, not an unstated inverse-limit
surjectivity assertion. L005's full integral-limit argument is consistent
with this direct construction.

**Rationalization and strictness.** By Mordell's finite generation,
write E(Q) as Z^r direct-sum T with T finite. Its p-adic completion is
Z_p^r direct-sum T[p^infinity]; tensoring over Z_p with Q_p gives
E(Q) tensor_Z Q_p. Thus the preceding integral Kummer preimage gives
the claimed rational one. For an arbitrary kappa in M tensor Q_p,
localization at p expresses it as p^{-a}(k tensor 1) for some single
k and a >= 0. Explicitly, write a tensor as a finite sum and clear the
finitely many denominators of its Q_p coefficients simultaneously.
No scalar depending on n is used. Hypothesis (1) must be proved for
the resulting integral tower; rationalization alone does not prove it.
As p^a is invertible in Q_p, membership of p^a kappa implies membership
of kappa. L005's strict-class threshold then applies exactly when
the rationalized class is nonzero and strict. Integral torsion can
disappear on rationalization, so integral nonvanishing is insufficient.

For completeness, this criterion does not conceal a finite integral
Sha tower that disappears only on rationalization. The module
T_p Sha=lim Sha[p^n] is p-torsion-free: if p^d(c_n)=0 for every n,
then c_n=p^d c_{n+d}=0 for every n. Localization into T_p Sha tensor Q_p
is therefore injective. By L005's exact rational Kummer sequence,
for the chosen k the conditions that all c_n vanish and that its
rationalization be Kummer are equivalent. Together with i=id in the
zero case, this makes explicit the class-level equivalence behind
the existential fixed-embedding condition. It supplies no proof of
that premise for a proposed nonzero strict class.

This is a REPRODUCTION of a known finiteness theorem's elementary
compatible-tower specialization under the prior SPECIALIZE assessment,
not a mathematical novelty claim or progress beyond the checked sources.
No finite computation or numerical certificate is needed: (2) covers
every level. Nonzero strict-class production, the fixed embedding for
an actual proposed class, and the comparison with complex order remain
unresolved. The finite-Sha point formulas recorded in ATTEMPTS/003 and
ATTEMPTS/004 have not been imported without their premises; generic
height/tower data from ATTEMPTS/007 and ATTEMPTS/019 and auxiliary
variation from ATTEMPTS/030 are not used to supply (1).

## Mathlib

Full fixed-embedding visibility finiteness and this arithmetic
specialization: **not checked**. Supporting finite-group exponent,
inverse-limit kernel, localization and Kummer coverage: **not checked**.
Agashe--Stein and Milne are precise mathematical references, not claims
of full matching Mathlib theorems. L005 supplies the local strict-rank
threshold with its stated hypotheses.
