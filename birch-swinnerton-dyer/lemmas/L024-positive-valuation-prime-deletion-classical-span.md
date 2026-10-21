# L024 — Classical prime-deletion classes with bounded finite-defect index

## Hypotheses

Let E/Q be non-CM, and let p >= 5 be good ordinary. Assume that E[p]
is surjective, p divides neither #E(F_p), the Manin constant nor any
Tamagawa factor, and E(Q_p)[p] = 0. For the classical Selmer group
S = Sel(Q,E[p^infinity]), grant corank_Z_p S = 2 and nonvanishing of
some residual Kurihara number in Sakamoto's N_(1,0). These are the
arithmetic hypotheses of L021 and L023; rational rank two, finite
p-primary Sha and any complex vanishing order are not assumed.

Put F = S/S_div and h = length_Z_p F. Fix m > 2h, R = Z/p^m Z,
T = E[p^m], and one of the pairs ell_1, ell_2 selected in L023 at
this depth. Thus both primes belong to P_(m,0): they are distinct
primes of good reduction with ell_i = 1 mod p^m and
E(F_(ell_i))[p^m] cyclic of order p^m. Write N = ell_1 ell_2.
Use precisely L023's actual Sakamoto Kato-derived rank-zero system,
its generators of G_ell and its singular-quotient trivializations.
Denote its scalar at N by delta = delta_m(N); L023 gives v_p(delta)=h.

Write M = Sel(Q,T). A strict condition means zero at the specified
primes; a relaxed condition means all of H^1 locally. Elsewhere retain
the classical Kummer conditions. Use the induced Weil self-duality.
The approved extraction target and its source coverage are in
[the prior assessment](../drafts/literature/2026-10-05-positive-valuation-prime-deletion-extraction.md).

## Conclusion

After trivializing each component's G_(N/ell_i) factor by the fixed
generator, the actual classes

\[
c_i=\kappa_{N/\ell_i,\ell_i}\quad (i=1,2)
\]

belong to M. Their localization at ell_j is zero when j != i.
Let f_i be finite localization at ell_i followed by finite-singular
comparison and scalarization using its fixed G_(ell_i) generator.
Then, with the tensor identifications specified below,

\[
(f_1,f_2)(c_1)=(-\delta,0),\qquad
(f_1,f_2)(c_2)=(0,-\delta).
\tag{1}
\]

For C = R c_1 + R c_2, the finite quotient satisfies

\[
\operatorname{length}_R(M/C)\leq 3h,
\qquad [M:C]\leq p^{3h}.
\tag{2}
\]

When h=0, the classes form an R-basis of M. For h>0, no basis of M,
zero finite quotient, rational Kummer membership, common primes at
all depths, or compatible family of these spans is asserted. The bound
is a conditional finite-depth specialization of known duality and
class relations; it is not a BSD candidate or a claim of originality.

## Proof

**Inputs and the dual structures.** L023 supplies the surjection

\[
\lambda:M\longrightarrow
 U_1\oplus U_2,\qquad
 U_i=H^1_{\rm ur}(\mathbf Q_{\ell_i},T)\simeq R,
\tag{3}
\]

on the representation and its Cartier dual. Its strict kernel K is
isomorphic as an R-module to F and has length h. Its coefficient
identification also gives M isomorphic to R^2 direct sum F. These
already justified structure and prime-selection results are reused
without reproof.

Import Ryotaro Sakamoto, *p-Selmer group and modular symbols*,
Documenta Mathematica 27 (2022), 1891–1922, DOI 10.4171/DM/X21,
[Theorem 2.1, p. 1897](https://ems.press/content/serial-article-files/29299?nt=1#page=7),
and [Definitions 2.3–2.4 and Lemma 2.6, p. 1898](https://ems.press/content/serial-article-files/29299?nt=1#page=8).
The classical structure is self-dual; duality exchanges strict and
relaxed conditions at N. The representation and local hypotheses
are exactly those retained in L023, at n=0. The classical condition
at each ell_i is unramified. In the source's
[Section 2.3, p. 1902](https://ems.press/content/serial-article-files/29299?nt=1#page=12),
eligibility gives the direct sum of finite and transverse lines and
free rank-one local modules. These inputs justify the inclusions and
dual structures used next. We import Poitou-Tate rather than reprove it.

Let B be the global group relaxed at both primes of N. Apply Theorem
2.1 to the strict structure at N contained in the classical structure.
Under the Weil identification, the resulting exact sequence is

\[
0\longrightarrow K\longrightarrow M\xrightarrow{\lambda}
 U_1\oplus U_2\longrightarrow B^\vee
 \xrightarrow{\mathrm{res}}M^\vee\longrightarrow0.
\tag{4}
\]

Here vee means Hom(-,Q_p/Z_p), and res is restriction along M included
in B. Surjectivity in (3) makes the map U_1 direct sum U_2 -> B^vee
zero. Thus res has zero kernel and is onto. Equivalently,
(B/M)^vee=0. The Pontryagin dual separates elements of a finite
p-group, so B/M=0 and B=M as global subgroups of H^1(Q,T).
This needs no vanishing of K: positive h is retained. It is precisely
the strict/classical comparison used in the proof of the source's
[Corollary 4.10, p. 1920](https://ems.press/content/serial-article-files/29299?nt=1#page=30),
with (3) supplying surjectivity instead of residual minimality.
We do not import that corollary's mod-p basis conclusion at positive h.

**Classical membership and tensor factors.** By
[Sakamoto, Definition 2.18, p. 1903](https://ems.press/content/serial-article-files/29299?nt=1#page=13),
the component kappa_(N/ell_i,ell_i) has a relaxed condition at ell_i,
a transverse condition at ell_j (j != i), and the classical conditions
at all other primes, including p. These local conditions are contained
in those of B. The tensor factor can be trivialized without changing
this assertion: if G_d is cyclic of order p^b with b>=m, its chosen
generator identifies any R-module A with A tensor_Z G_d, since
A tensor_Z Z/p^b Z = A/p^b A = A. For d=ell_j this applies directly;
for d=N the tensor of the two generators has order
p^min(b_(ell_1),b_(ell_2)), again at least p^m, as checked in L023.

Consequently each scalarized c_i lies in B=M. At ell_j it is both
unramified and transverse. Those lines have zero intersection, so
its entire localization there is zero, not merely its singular image.
This checks both auxiliary conditions and every remaining condition
for the actual classes, without canceling any scalar.

For the diagonal entries, choose an eligible q outside N; the prime
set used in L023 is infinite, so this auxiliary choice is available.
The source's last rank-zero relation, with d=N/ell_i and ell=ell_i,
and the definition of delta on p. 1904 give

\[
\delta(\kappa)_N=v_q(\kappa_{N,q})
       =-\varphi_{\ell_i}^{fs}
                 (\kappa_{N/\ell_i,\ell_i}).
\tag{5}
\]

This equality is in R tensor_Z G_N: finite-singular comparison adds
the G_(ell_i) factor to the component's G_(N/ell_i) factor. Order the
two tensor factors as in L023; exchanging them uses the usual tensor
symmetry, with no exterior-power sign. Write the component as c_i
with the chosen G_(N/ell_i) generator and define f_i by taking the
finite local coordinate, applying finite-singular comparison, then
using the chosen singular and G_(ell_i) generators. Both sides of
(5) then use the same generator of R tensor_Z G_N. Equation (5)
becomes f_i(c_i)=-delta. Since c_i is classical, this is its actual
finite coordinate, not a projection concealing a transverse error.
The cross coordinates vanish by the preceding paragraph. This proves
(1). Unit changes of bases preserve its ideal and the following index
bound; no comparison with another scalar family is used.

**The nonunit quotient estimate.** Finite-singular comparison is an
isomorphism on each finite line, with its G factor retained. Hence
f=(f_1,f_2): M -> R^2 is surjective, and ker(f)=K. Equation (1) gives

\[
f(C)=\delta R\oplus\delta R=p^h R\oplus p^h R.
\tag{6}
\]

The equality of ideals uses v_p(delta)=h<m. It does not divide by
p^h: writing a generator of the ideal as p^h times a unit is only an
ideal calculation. The map f induces the exact sequence

\[
0\longrightarrow K/(K\cap C)\longrightarrow M/C
 \longrightarrow R^2/f(C)\longrightarrow0.
\tag{7}
\]

Indeed a coset mapping to zero has a representative x with f(x) in
f(C); choose c in C with f(c)=f(x). Then x-c lies in K, and the
kernel of K -> M/C is K intersect C. This proves exactness even
though M need not be free and f restricted to C need not be injective.

For 0<=h<m, R/p^h R has length h. Thus the right term in (7) has
length 2h, and the left term has length at most length(K)=h. Additivity
of length yields (2), more precisely
length(M/C)=3h-length(K intersect C). A finite R-module of length a
has p^a elements, which translates the length estimate into the
stated group index. Equivalently the localization image of C has
length 2(m-h), against length(M)=2m+h; this independently checks the
same upper bound 3h without assuming C is free.

For h=0, K=0 and delta is a unit. Equations (1), (3) identify c_1,c_2
with a diagonal R-basis of R^2, proving the basis assertion. For
positive h and m>2h, h<m ensures the nonzero ideal and the quotient
length calculation apply; neither scalar reduction modulo p nor any
proper-divisor vanishing was used. All estimates are at the approved
depth m>2h. No stronger depth conclusion or passage to an inverse
limit is needed for this result.

The continuation/abandonment test is met at this conditional level:
both actual classes are classical and the achieved index is at most
the required p^(3h). The full group still has its strict kernel F,
and no relation between classical and rational directions has been
proved. The earlier residual error models and the stop on removing
F from primitivity do not contradict this application; they lack
its granted working-depth localization surjection. The argument
reuses the published comparison and class relations and supplies the
finite-module quotient estimate; no source construction is reproved.

**Critical audit, 2026-10-06.** Equations (4), (5) and (7) survive
independent checking under exactly the stated hypotheses. In (4) the
last arrow is the dual of the actual inclusion M into B, not an
abstract isomorphism between groups of the same length. Self-duality
identifies the strict dual with the relaxed structure at both primes
simultaneously. Surjectivity of lambda therefore kills (B/M)^vee;
it does not kill K. The local conditions outside N, including the
classical condition at p, are identical in this comparison.

Here is the explicit applicability check for the local splitting and
comparison used in (5). Import Mazur--Rubin, *Kolyvagin Systems*,
Mem. AMS 168 (799) (2004),
[Definition 1.2.2 and Lemmas 1.2.3--1.2.4, pp. 10--11](https://webusers.imj-prg.fr/~christophe.cornut/ES/Ref/KolySys.pdf#page=16).
At an eligible ell, ell differs from p, T is unramified and finite
free over the artinian R, ell-1 annihilates R, and its Frobenius
coinvariants are free of rank one. Thus the cited comparison is an
isomorphism with its residue-unit-group tensor factor retained.
Passing from F_ell^* to its p-primary quotient G_ell induces an
isomorphism after tensoring with any R-module: the kernel has order
prime to p and its tensor product with that module is zero. For the
transverse condition, put L=Q_ell(mu_ell) and let L_p be its maximal
p-subextension. Restriction from H^1(L_p,T) to H^1(L,T) is injective,
since corestriction composed with restriction is multiplication by
the prime-to-p integer [L:L_p]. Consequently restriction from
Q_ell to L and to L_p has the same kernel. This is precisely the
passage to Sakamoto's transverse condition; no splitting is lost.

For each i, d=N/ell_i and a prime q outside N satisfy all three
index conditions in Definition 2.18. Scalarization on its last
relation uses g_(N/ell_i) tensor g_(ell_i), reordered to the fixed
g_N. It introduces no additional p-power or exterior sign. Membership
in B is established before using the finite projection in that
relation. The other-prime localization lies in the intersection of
the finite and transverse lines and is therefore zero. This checks
the diagonal matrix, including its sign, without a residual-unit
assumption or a changed scalar family.

Finally, (7) follows from the preimage identity f^(-1)(f(C))=K+C;
its first term is (K+C)/C, canonically K/(K intersect C). In
particular, neither C nor M was assumed free. For h>0 the two
cokernel summands each have length h, and the remaining term has
length between zero and h. For h=0 both terms vanish, and the
displayed diagonal matrix is invertible. The audit retains m>2h
and the bound p^(3h), with no strengthening of either claimed.
No error or additional arithmetic hypothesis was found. This
confirms the conditional argument, not a new theorem beyond the
checked inputs or a solution of rational membership. Compatibility
as depths and selected primes vary remains unproved.

## Mathlib

Full matching positive-valuation extraction/index theorem: not checked.
Supporting Poitou-Tate, finite-singular comparison, finite-module tensor
identifications and length additivity: Mathlib coverage not checked.
The specialized argument is written above, but no formalization or
absence claim is made.
