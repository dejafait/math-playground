# L126 — Tame normalizer replacement in the complete norm moment

## Hypotheses

Retain all hypotheses and the fixed choices of L123 and L124. Thus A/Q
is modular, K/Q is imaginary quadratic, p>=5 is inert in K and split
multiplicative for A, the conductor is unramified in K, its inert part
is square-free, its split exponents are at most two, the residual image
contains SL_2(F_p), and the source's incoherence condition holds for
{p}, with auxiliary place infinity. The CM conductor is one and the
character is trivial. Retain the integral CM embedding psi, its fixed
points z at infinity and tau at p, the original rational normalizer n,
the original indexed representatives h_t, the coefficient module M,
and all normalization, completion, localization and descent maps.

Write Delta for the finite set of inert conductor primes, including p.
The finite ramification set of the indefinite quaternion algebra B is
Delta minus {p}. Let O_v be the completion of the source's Eichler
order of level n^+, and let K_0,v be the image of O_v^times in G(Q_v).
At p it is PGL_2(Z_p). At tame places this is the actual level group;
only the p-component changes in K_m. In particular no extra tame
orientation subgroup is imposed. Put T=K^times/Q^times and

\[
 U=\operatorname{im}(\widehat{\mathcal O}_K^\times\longrightarrow
                         T(\mathbb A_f)),\qquad
 \mathcal C=T(\mathbb Q)\backslash
     T(\mathbb A_f^{\Delta})/U^{\Delta}.
                                                        \tag{1}
\]

The action of T(Q) in (1) is by its truncated diagonal image.
The source's conductor-one CM list is a set of representatives t of
this finite quotient, embedded with components 1 at Delta, and
h_t=psi(t). This is the same list as in L123/L124, not a new list.
The equality with the full finite-idele quotient follows because
T(Q_v)=U_v at each inert unramified v in Delta. Source (67)--(68)
uses one summand per quotient class and no additional stabilizer weight.

Use L124's w, namely w_p=1 and w_v=n_v^{-1} for every tame v, and
q_tau=log_p N_tau on X. All integrals below take values in the same
complete raw coefficient module M before Hecke specialization.

The imported inputs are:

- John Voight, *Quaternion Algebras*, GTM 288, Springer (2021),
  [Chapter 30, pp.541--567](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_30),
  Proposition 30.5.3(a),(b), (30.6.2), Lemmas 30.6.3 and 30.6.9(a),(b).
  These are local optimal-embedding comparisons, including general
  Eichler prime powers. Their scope is specialized below; no extension
  of the square-free classical conjugation lemma is used.
- Michele Fornea, *Plectic Heegner classes*,
  [arXiv:2603.28327v2, 13 April 2026](https://arxiv.org/html/2603.28327v2),
  (2), Section 2.2 level definitions, (22), Corollary 3.9, (34)--(35),
  and (67)--(68). The projection domain and descent are the audited
  inputs already retained in L123/L124, using Lemma 4.12, Corollary
  4.15, (63), and Corollary 4.24. The comparison with Proposition 4.18
  and Theorem 4.22 is explained below; their general invariance
  statements are not interpreted as raw measure invariance.

## Conclusion

There exist a in T(A_f) and W in G(A_f) with

\[
 a_v=1\ (v\in\Delta),\qquad W_p=1,\qquad
 w=\psi(a)W,\qquad W K_m W^{-1}=K_m\quad(m\geq0).          \tag{2}
\]

At every tame place, W_v conjugates the embedded quadratic algebra
by its nontrivial automorphism. At division places one may take
W_v=w_v. Define, with the original indexed list,

\[
 \mu_W=\sum_t\Phi(h_t^{-1}W)(z),\qquad
 J_W=\int_Xq_\tau\,d\mu_W.
\]

Then the equality of **complete moments** is already valid in M:

\[
                         J_n=J_W.                         \tag{3}
\]

This is not an equality of the raw measures mu_n and mu_W. In
particular J_W tensor 1 has the same diamond-invariant projection
domain as J_n tensor 1. Its projected class has the same unique
H^1(L_1,V) lift, trivial Gal(L_1/K) character and descent. Writing
B_W=pr_A(J_W tensor 1) and b_W=desc(B_W), one obtains

\[
 B_W=B_n,\qquad b_W=b_n=c b,\qquad
 R=\operatorname{loc}_p(b+b_W).                            \tag{4}
\]

Right translation by W is a degree-one automorphism at each actual
level K_m. No assertion that its action on the specialized coefficient
module is scalar, or that b_W=epsilon b, is made. Neither R nor its
vanishing/nonvanishing, finite local membership, rational Kummer
membership, analytic rank, finite Sha or a BSD case is established.
This is a known-source specialization (REPRODUCTION), accepted by the
separate step-526 conceptual audit below, not a claim of mathematical novelty.

## Proof

**Local applicability and both tame orientations.** Source (2) with
conductor one says that the embedded maximal quadratic order is
optimally contained in the chosen Eichler order. Localizing this
intersection gives psi(O_K,v)=psi(K_v) intersect O_v. Conjugating the
domain by its nontrivial automorphism leaves that image order fixed,
so psi and psi composed with conjugation are both optimal embeddings.

If B_v is split and O_v maximal, Proposition 30.5.3(a) supplies an
O_v-unit conjugating these two embeddings. Thus there is W_v in
N(O_v) inducing the nontrivial automorphism on psi(K_v). This includes
split, unramified-field and ramified-field K_v, also at residue
characteristic two; no unit-discriminant condition is needed here.

If O_v has positive Eichler exponent e, then v divides n^+, so K_v
is split and its maximal order is Z_v times Z_v. In the local notation
of Voight, choose its generator gamma=(1,0). Its polynomial is
X(X-1), its trace is 1 and its discriminant is 1. The only roots
modulo v^e are 0 and 1: in the local ring, one of x and x-1 is a unit,
so their product can vanish modulo v^e only by the other factor
vanishing. Lemma 30.6.3 brings any optimal embedding into normalized
form up to the full normalizer. Lemma 30.6.9(a) identifies normalized
embeddings with the same root; part (b), using discriminant 1, exchanges
the two roots by the normalizer element of (30.6.2). Hence there is
one full-normalizer orbit and in particular a W_v conjugating psi to
its conjugate. This checks both orientations for e=1 and e=2, without
an odd-residue-characteristic assumption. The ramified-quadratic,
positive-Eichler-level case never occurs under the conductor hypotheses;
part (c) of Lemma 30.6.9 is not invoked.

At v in Delta minus {p}, B_v is division. Its valuation order is its
unique maximal order, so its full multiplicative group normalizes
O_v; this is also the argument in Proposition 30.5.3(b). Choose
W_v=w_v. It already induces conjugation on K_v by L124. This choice
will make a_v=1 at all these discarded coordinates.

All these assertions concern algebra embeddings, not merely an
unoriented torus image. Consequently, for each tame v, w_v W_v^{-1}
centralizes psi(K_v). The centralizer is psi(K_v)^times: for a split
quadratic algebra it is the diagonal algebra in an eigenbasis; for a
quadratic field it is its multiplication algebra on the one-dimensional
K_v-module, or the quadratic centralizer in the division algebra.
Thus w_v W_v^{-1}=psi(a_v) in G(Q_v) for a_v in T(Q_v).

Outside finitely many v the fixed rational n has a unit representative
in O_v, so w_v itself normalizes O_v. Choose W_v=w_v there as well.
The resulting local choices form restricted finite adeles. Set
W_p=a_p=1. This proves w=psi(a)W without changing n. Normalizing
O_v normalizes O_v^times and its projective image, so W normalizes
the entire tame level. Its identity p-component normalizes every deep
p-level. This proves (2); no global rational normalizer of the order
or strong-approximation assertion has been inserted.

**The full kernel under the local torus.** Every r in T(Q_p) has an
integral unit representative in the chosen GL_2(Z_p) coordinates.
Indeed the CM-stable lattice is a free rank-one O_K,p-module and
K_p/Q_p is unramified; multiply a K_p^times representative by a
central power of p to make it an O_K,p-unit. The determinant then
has valuation zero, so there is no vertex change or determinant-parity
twist. This statement applies in particular to the p-component of
every rational torus element, without assuming that component is 1.

Let R_p be such a matrix representative and put ell_tau=(1,-tau),
ell_bar=(1,-bar(tau)). These are independent left eigenvectors:

\[
 \ell_\tau R_p=\alpha\ell_\tau,\qquad
 \ell_{\bar\tau}R_p=\bar\alpha\ell_{\bar\tau},\qquad
 \det R_p=\alpha\bar\alpha.
\]

Here both CM orientations are retained; a torus element fixes each
line instead of exchanging them. The action in source (35) is
[(v,z_0)] mapped to [(R_p v,det(R_p)z_0)]. Therefore

\[
 N_\tau(r s)=N_\tau(s),\qquad q_\tau(r s)=q_\tau(s)
                     \quad(s\in X).                       \tag{5}
\]

This is an exact cancellation of the product of the two eigenvalues
against the determinant coordinate. It is unchanged by central unit
rescaling. It is not a constant-mass argument, and it does not assert
invariance of either individual f_tau or of a measure. Equivalently,
the constants from the two scalar orientations in source (66) have
sum zero. Equation (5) is the small additional specialization needed
for this norm kernel; the general source construction is not reproved.

**Representative comparison at every deep cell.** For t in
T(A_f^Delta), embedded with components 1 at Delta, put

\[
 F_W(t)=\int_X q_\tau\,d\Phi(\psi(t)W)(z).
\]

We show directly that this M-valued function factors through C in
(1). If u belongs to U^Delta, then psi(u) belongs to K_0 away from
Delta. Since W normalizes K_0 and psi(t) commutes with psi(u),

\[
 \psi(tu)W=\psi(t)W\,(W^{-1}\psi(u)W).
\]

The rightmost factor belongs to K_m for every m and has p-component
1. The CM points specifying the measures are consequently identical
at every cell, so F_W(tu)=F_W(t). This uses the actual tame unit
subgroup, not a conjectured torus stabilizer.

Now let r in T(Q), delta=psi(r) in G(Q), and let r^Delta denote
its truncated finite idele, with components 1 at Delta. Set
g=psi(t)W and let xi be supported at p with xi in K_0,p. The rational
element delta fixes the CM point z. At every v in Delta minus {p},
the extension K_v/Q_v is unramified inert; hence delta_v is the
image of an O_K,v-unit and belongs to K_0,v. Since g_v=W_v and W_v
normalizes K_0,v, the extra factor delta_v^{-1} after rational left
translation can be moved to the right of W_v into K_m,v. At p,
delta_p is compact as proved above. Thus the exact equality of
points at the original level is

\[
 [z,\psi(r^\Delta t)W\xi]_{K_m}
       =[z,\psi(t)W\delta_p^{-1}\xi]_{K_m}.                \tag{6}
\]

On the right delta_p^{-1} denotes the finite adele supported at p.
Equation (6) follows by left multiplication by delta^{-1}; no
discarded division component is set to 1 without the right-level
argument just given. The cell delta_p^{-1}xi X_m is a genuine cell
in K_0,p/K_p^m. Left translation permutes these cells and does not
require delta_p to normalize the deep subgroup.

Apply the very same j_m varphi_m from source Corollary 3.9 to the
two equal points. In particular the auxiliary-Hecke normalization
in (22), residual localization and completion have not been commuted
through a new operator or replaced by a shallow elliptic quotient.
Writing mu_g=Phi(g)(z), (6) gives

\[
 \mu_{\psi(r^\Delta t)W}(\xi X_m)
       =\mu_g(\delta_p^{-1}\xi X_m).
\]

These identities are compatible with refinement by the source measure
construction; on the entire compact domain they say that the left
measure is (delta_p)_*mu_g. Integration of a locally constant function
therefore satisfies the usual pushforward formula. Uniformly
approximating the continuous q_tau and using completeness of M gives,
with (5),

\[
 F_W(r^\Delta t)=\int_Xq_\tau(\delta_p s)\,d\mu_g(s)
                =F_W(t).                                  \tag{7}
\]

No infinite limit passes through localization or pr_A. This proves
the rational-representative invariance required for (1). It explicitly
accounts for the simultaneous rational action and the p-cell change
that would be hidden by assuming raw measure invariance. Because it
uses the sum of the two oriented scalar kernels directly, it makes
no appeal to Theorem 4.22 for a mismatched CM tuple. It is consistent
with the general projected invariance of Proposition 4.18, but is
stronger here solely because the full norm has the exact property (5).

**The complete sum and normalization.** The quotient C is a finite
abelian group. The idele a in (2) is supported outside Delta, so
multiplication by its class permutes C. Inversion also permutes C.
For each original indexed t there are another original representative
t', a rational r and a unit u in U^Delta with
t^{-1}a=r^Delta(t')^{-1}u. The representative t' is unique at the
quotient level; the possible nonuniqueness of r and u does not affect
F_W by (7) and unit invariance. Consequently

\[
 \begin{split}
 J_n
 &=\sum_t F_W(t^{-1}a)\\
 &=\sum_t F_W(t^{-1})=J_W.                                 \tag{8}
 \end{split}
\]

Every original class occurs exactly once on each side. The source
fundamental class (67) and trivial-character sum (68) have precisely
this multiplicity. No CM point stabilizer is divided out and no
Hecke fiber is inserted. The equality uses equality of integrated
representatives; it does not identify the two measures cell by cell
after discarding their rational p-actions. This proves (3).

**Projection, fields and the degree-one correspondence.** L124
already puts J_n tensor 1 in the domain of (63). Equation (3) transfers
that domain statement to J_W tensor 1, using the flat-invariant
comparison retained in L123; it is not a definition of pr_A on raw
cells. Apply pr_A to the equality of complete moments. Initially
the resulting equality is over K^ab. L124 supplies the unique lift
B_n to H^1(L_1,V), fixed by Gal(L_1/K). Use that same lift for B_W;
its uniqueness is the injective restriction established in L123.
Equivariant rational descent gives (4), including when p divides
[L_1:K]. Neither the archimedean conjugation lift nor L124's intervening
H is silently identified with a p-decomposition lift on raw coefficients.

Finally (2) makes [z,g] mapped to [z,gW] a well-defined automorphism
of X_K_m, with inverse right translation by W^{-1}. Hence its degree
is one at every deep level and it commutes with forgetting p-level.
This geometric statement does not require interchanging W with the
coefficient normalization or proving that W preserves a chosen Hecke
eigensummand. Such compatibility and a scalar evaluation are separate
questions. In particular (8) removes the earlier selected-branch
ambiguity without asserting the failed automatic full-fiber substitution.

The full comparison is proved only under the retained source inputs.
It furnishes an intermediate identity toward evaluating L123's residual;
it does not supply the independent rationality, nonvanishing, auxiliary
choice or multiplicative-prime rank-comparison inputs needed for BSD.

**Separate conceptual audit, step 526 (2026-10-27).** PASS for (2)--(8)
under the written hypotheses and the imported construction. The audit
checked the maximal split-order, split positive-Eichler-level (including
exponent two and residue characteristic two), and division cases. The
local choices give restricted adeles with the original n unchanged and
a_v=1 on Delta. No global order-normalizing rational element is required.

In (6), left multiplication by delta^{-1} cancels the rational torus
coordinate outside Delta. At a discarded division place its remaining
factor is absorbed by W_v^{-1}delta_v^{-1}W_v in the actual unit level;
at p it remains delta_p^{-1}xi. Thus the pushforward is by delta_p,
with precisely the sign used in (7), and no normalization of the deep
p-subgroup is needed. Equation (5) cancels both eigenvalues against
the determinant coordinate. Uniform integration takes place in M before
specialization. The complete source list has one term per quotient
class, also in the presence of CM automorphisms; no orbit-size or
stabilizer factor is inserted in (8).

The raw equality transfers the projection domain already proved in L124.
The equality over K^ab has the same unique L_1 lift by L123, and rational
descent remains valid for p-divisible class-field degree. The resulting
degree-one geometry does not assert coefficient equivariance for W or
a scalar action. No mathematical premise or conclusion was repaired or
strengthened; the audit verifies the existing identity, not an evaluated
R, new arithmetic input, rational Kummer class or BSD case.

## Mathlib

The complete normalizer/moment replacement, quaternionic embedding
classification, measure tower and cohomological specialization:
**not checked**. Supporting finite-quotient reindexing, centralizer
and matrix facts: **not checked**. The named primary results are
mathematical imports, not assertions of matching Mathlib declarations.
