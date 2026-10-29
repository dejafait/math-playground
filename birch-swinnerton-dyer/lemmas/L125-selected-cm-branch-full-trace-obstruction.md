# L125 — A selected CM branch need not be a normalized full Hecke trace

## Hypotheses

Retain L124's hypotheses, notation and actual finite indexed CM list
{h_t}; retain the complete-integral domain and projection restrictions
inherited there from L123. In particular, the character is trivial,
the CM conductor is one, the integration prime p is inert and split
multiplicative for A, and w_p=1. This w is L124's finite tame adele,
not Fornea's auxiliary place, which is infinity here.

For the obstruction assume that q>=3 is a prime distinct from p,
split in K and prime to the conductor of A. Thus B_q is split and
the tame level U=(K_m)_q is PGL_2(Z_q), independently of m. In an
integral basis diagonalizing O_K tensor Z_q=Z_q x Z_q, assume the
chosen rational normalizer n, and hence w_q=n_q^{-1} in PGL_2(Q_q),
has a representative

\[
 w_q=\begin{pmatrix}0&q u\\1&0\end{pmatrix},
 \qquad u\in\mathbf Z_q^\times.                         \tag{1}
\]

This is an additional, testable local condition, not an assertion
about every choice of n. It is permitted by L124: given such a q,
a rational normalizer can be chosen with (1), as proved below.
No particular curve, prime q or previously unspecified n is being
silently instantiated. The result disproves an automatic full-trace
identification in the generality of L124; it does not prove that
every permissible n has this obstruction.

The imported normalization is Fornea, *Plectic Heegner classes*,
[arXiv:2603.28327v2, 13 April 2026](https://arxiv.org/html/2603.28327v2),
Section 2.1.2 and (15) (sum of right cosets, without division by degree),
Section 2.2 (levels), (22), Corollary 3.9, and (67)--(68)/Corollary 4.24
with proof (the trivial-character CM sum). These are the already
assessed inputs. The calculation below checks the missing local
stabilizers and their effect on this particular selected sum; it does
not reprove the source construction or posit a new Hecke normalization.

## Conclusion

Put C_m=K_m intersect w K_m w^{-1}, as in L124, and use the maps a_m,b_m
of its (10). At q the full a_m-fiber has q+1 coset branches. Two have
maximal split CM order Z_q x Z_q; the other q-1 have order

\[
 \mathcal O(q)=\{(a,b)\in\mathbf Z_q^2:a\equiv b\pmod q\}.
                                                               \tag{2}
\]

The selected branch represented by 1 in K_m/C_m has maximal order.
The compact CM torus fixes each of the two maximal-order branches;
it acts transitively on the other q-1, with stabilizer given by
a/b=1 modulo q. Thus the selected branch is not a torus orbit
representing the full fiber, even with a common scalar multiplicity.

More precisely, for each fixed deep p-cell xi define the effective
divisors on X_{K_m}

\[
 D_{\rm sel}=\sum_t[z,h_t^{-1}w\xi]_{K_m},\qquad
 D_{\rm full}=\sum_t\sum_{j\in\mathcal J}
                   [z,h_t^{-1}u_jw\xi]_{K_m},                \tag{3}
\]

where u_j are representatives for K_m/C_m, supported away from p,
and u_0=1. The index set and representatives can be taken independent
of m. D_full is the source-normalized full correspondence trace on
the divisor with finite coordinates h_t^{-1}xi. Its support includes
CM points with local order (2), while every point in D_sel has maximal
local order at q. Consequently D_full is not any scalar multiple of
D_sel in the free Q_p-vector space on geometric CM points. This
continues to hold after the entire indexed CM sum and all genuine
CM-point identifications, with multiplicities retained.

For the actual M-valued measures and complete weighted integrals the
exact statement is only

\[
 \begin{split}
 \mu_{\rm full}&=\sum_{t,j}\Phi(h_t^{-1}u_jw)(z),\\
 \mu_{\rm miss}&=\sum_{t,j\ne0}\Phi(h_t^{-1}u_jw)(z),\\
 J_{\rm full}&=\int_Xq_\tau\,d\mu_{\rm full}
                =J_n+J_{\rm miss},\qquad
 J_{\rm miss}=\int_Xq_\tau\,d\mu_{\rm miss}.                \tag{4}
 \end{split}
\]

There is no conclusion that J_miss or its projected class is nonzero.
If J_full tensor 1 has the required projection/descent domain and
its descended value is lambda b, then the same domain holds for
J_miss tensor 1 by subtraction from J_n tensor 1. In that case

\[
 b_n=\lambda b-b_{\rm miss},\qquad
 b_n=\epsilon b\quad\Longleftrightarrow\quad
 b_{\rm miss}=(\lambda-\epsilon)b.                          \tag{5}
\]

The domain and scalar premises in this sentence are conditional;
neither lambda nor epsilon is evaluated. Divisor inequality does not
imply inequality after a Jacobian, completion or cohomology map.
In particular, no nonscalarity of b_n, value of R, new BSD case or
elliptic-curve counterexample follows.

## Proof

**Integral coordinates and the allowed rational choice.** At this good
split prime, the two idempotents of O_K tensor Z_q split the stable
rank-two lattice into rank-one Z_q summands. Choosing their bases
diagonalizes the torus without changing U=PGL_2(Z_q). Every local
normalizer inducing the nontrivial field automorphism is antidiagonal.
After central scaling it has the form [[0,r],[1,0]], r in Q_q^times.
Its square is central, so its inverse has the same PGL_2 class.

Starting with any rational normalizer n_0 from L124, replace it,
before fixing n, by psi(a)n_0 for a in K^times. If a has local
components (a_1,a_2), the valuation of r changes by
v_q(a_1)-v_q(a_2). Prescribe this difference to be 1-v_q(r).
The Chinese remainder theorem in O_K supplies a nonzero a with
these exact valuations: prescribe valuations max(d,0), max(-d,0)
at the two primes over q, using congruences modulo one higher power,
where d=1-v_q(r). Also impose a=1 modulo the prime over p.
These ideals are coprime. Thus the p-component of a is a unit and
L124's compactness at p is preserved. No restrictions on the new
tame components at other primes were imposed by L124. The resulting
normalizer has (1), including its possibly nontrivial unit u. This
justifies the permitted local test for any given q satisfying the
stated hypotheses. It is not a change of n inside an asserted equality.

**Fiber and its torus stabilizers.** Let Lambda_0=Z_q e_1+Z_q e_2.
Write w_q=diag(q,1)v with v in GL_2(Z_q). Then
w_q Lambda_0=q Z_q e_1+Z_q e_2. The subgroup U intersect w_q U w_q^{-1}
is precisely the stabilizer in U of this index-q sublattice, or
equivalently of the line F_q e_2 in Lambda_0/q Lambda_0. Indeed its
integral representatives have upper-right entry divisible by q.
Reduction modulo q is surjective onto PGL_2(F_q), which acts
transitively on the q+1 lines. The index is therefore q+1, and the
lattices of all coset branches are exactly

\[
 \Lambda_L=\{v\in\Lambda_0:v\bmod q\in L\},
 \qquad L\in\mathbf P^1(\mathbf F_q).                       \tag{6}
\]

The diagonal torus acts by scaling the two coordinates. It fixes the
lines F_q e_1,F_q e_2. Every other line is F_q(e_1+r e_2),
r in F_q^times, and diag(a,b) sends r to (b/a)r. The compact torus
Z_q^times x Z_q^times modulo diagonal units is transitive on these
q-1 lines; the stabilizer is a/b=1 modulo q. All q+1 cosets occur
once in the source's Hecke sum. If different cosets later give the
same geometric CM point, the sum retains their positive multiplicity.

**Local CM orders.** For a lattice Lambda let its multiplier order be
{x in K_q:x Lambda subset Lambda}. For either coordinate line in (6),
the lattice is a direct sum of two fractional Z_q ideals, and its
multiplier order is Z_q x Z_q. For a noncoordinate line write
Lambda_L={(x,y) in Z_q^2:y=r x modulo q}. Both projections of this
lattice onto Z_q are surjective. Thus any diagonal multiplier (a,b)
preserving it has a,b integral. The condition on the image of
(x,y) now reads r(b-a)x=0 modulo q for all x, which is equivalent
to a=b modulo q. Conversely this congruence suffices. This proves (2),
including equality of orders rather than only an inclusion. Its unit
group gives exactly the noncoordinate torus stabilizer computed above.

For a global CM point [z,g] the same local order is

\[
 \psi(K_q)\cap g_q M_2(\mathbf Z_q)g_q^{-1},                \tag{7}
\]

identified with an order of K_q. Right multiplication by U and central
rescaling leave (7) unchanged. Left multiplication by a torus element
also leaves it unchanged, since that element commutes with psi(K_q).
Finally, two representatives with the same z can be identified in
the Shimura double quotient only by a rational element stabilizing z.
Such an element also stabilizes its conjugate eigenline, hence belongs
to psi(K)^times modulo the center. It again leaves (7) unchanged.
Thus different orders in (7) cannot be identified as geometric points.

At q every h_t is a torus element and xi has component 1. The selected
coordinate h_t^{-1}w therefore has maximal multiplier order, for
every t. In the full sum choose a noncoordinate branch at q and the
identity branch at every other tame prime; it has order (2). The
global coset set is the product of the finite local coset sets,
so these choices occur. All coefficients in (3) are positive
integers. Summing over t, including repetitions or CM stabilizer
identifications, cannot cancel this support. No scalar multiplying
D_sel supplies it. This proves the asserted failure of proportionality.
The calculation works at every deep p-level; it makes no shallow
identification of those levels or their p-adic CM conductors.

**Weights, maps and the stopping boundary.** Since w_p=1,
C_m=C^p x K_{p^m}; all u_j may be chosen tame and fixed as m varies.
They commute with each cell representative xi, which is supported at p.
Corollary 3.9 therefore gives each cell of the measures in (4) by
applying exactly the same j_m varphi_m to the corresponding sums
in (3). In particular the map (22), including its unit denominator,
has not been commuted through w or replaced by another projection.
Each summand is an actual M-valued measure. The finite sums are
measures too, so integration against the unchanged continuous q_tau
is linear in the complete module M. This proves (4), with all
q-dependent multiplicities retained. There is no interchange with
pr_A, and no pointwise pr_A is used.

If an averaged Hecke convention is preferred, pass first to a rational
coefficient space where division by d(w)=[K_m:C_m] is defined. There
J_average=J_full/d(w) and (4) reads J_n=d(w)J_average-J_miss.
No division by a possibly p-divisible degree in the raw module M is
assumed. Averaging does not remove the missing term. The norm weight,
which is a function on the
p-domain, supplies no additional selection of q-branches. It can
still yield cancellations after integration and the coefficient
maps, so the divisor support argument is not a nonvanishing argument
for J_miss. Under the explicit domain premises in the conclusion,
linearity gives (5) and nothing stronger.

This is the concrete obstruction sought by the bounded branch test:
the original trivial-character CM trace does not automatically
convert a selected normalizer branch into a normalized full tame
Hecke trace. The tested inference stops. A torus-translation/degree-one
normalizer comparison would be a different mechanism, requiring
its own full-domain and operator justification. The scalar comparison
itself remains open. The result is a standard local Hecke-geometry
calculation specialized to L124 (REPRODUCTION), not a claim of progress
beyond the checked sources. It has not received a separate critical audit.

## Mathlib

The full selected-branch/CM-order statement, its Shimura-curve application,
and the completed moment identity: **not checked**. Supporting formal
coverage for index-q lattices, projective lines, Chinese remaindering
and finite measure sums was not inspected. No absence claim or formal
verification is made.
