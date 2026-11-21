# Lemma 793: uniform relative-coefficient tolerance with mesh loss

## Hypotheses

Let d>=1 be an integer and Q>1 a real number. Let

    p(z)=sum_(k=0)^d p_k z^k = a product_(j=1)^d (z-rho_j)

be a real polynomial of exact degree d, where a!=0,
0<rho_1<...<rho_d, and rho_(j+1)/rho_j>=Q for 1<=j<d.
Let e(z)=sum_(k=0)^d e_k z^k have real coefficients, allowing degree
less than d. Define

    h=(Q-1)/(Q+1), eta=h/2,
    epsilon(d,Q) = h/[2(4+h)] * [h/(2+h)]^(d-1)
                 = (Q-1)^d/[2(5Q+3)(3Q+1)^(d-1)].

Assume |e_k|<=epsilon(d,Q)|p_k| for every k=0,...,d, including
the constant and leading coefficients. For d=1 the ratio hypothesis
is empty; Q is still any specified number greater than one.

## Conclusion

The polynomial p+e has exact degree d and d simple positive roots.
Each open disk |z-rho_i|<eta rho_i contains exactly one of these
roots, counted with multiplicity, and these disks have disjoint closures.
In particular its ith root lies in
((1-eta)rho_i,(1+eta)rho_i). The tolerance depends only on d,Q,
with 0<epsilon(d,Q)<1, and is invariant under multiplying p and e
by a common nonzero real scalar or replacing z by c z with c>0.

This is a quantitative specialization of the standard componentwise
perturbation/Rouche method. It does not assert optimal tolerance,
preservation of the input mesh Q, a verified actual-Xi residual bound,
growing-degree model existence or separation, all-degree signs, or RH.
The separate step494 critical audit accepted this finite statement,
with the source qualifications and unchecked Mathlib coverage below.

## Proof

**Imported method and scope of the specialization.** Stef Graillat and
Philippe Langlois, *More on pseudozeros for univariate polynomials*,
[author preprint P32](https://perso.lip6.fr/Stef.Graillat/papers/P32.pdf),
6 January 2004, Theorem 3 and proof, pp.6--7, and Corollary 5,
p.9, equation (8), give the finite componentwise perturbation certificate
with weights f_k=|p_k| and all indices 0 through d, permitting a varying
leading coefficient. Only its sufficient exclusion direction is needed.
For the zero count use Rouche's theorem as stated in Alen Alexanderian,
*On continuous dependence of roots of polynomials on coefficients*,
[author note](https://aalexan3.math.ncsu.edu/articles/polyroots.pdf),
28 January 2022, Theorem 2.2, pp.1--2. Its Theorems 3.2 and 3.5,
with proofs pp.3--5, supply the disjoint-disk and real-coefficient
conjugation mechanism. The monic absolute-perturbation statement of
Theorem 3.2 alone is not used as an all-coefficient relative theorem.
The approved SPECIALIZE assessment is
`drafts/literature/2026-11-05-mesh-losing-root-disk-specialization.md`.
The difference proved here is the explicit scale-uniform boundary bound;
none of the imported general theorems is reproved.

**Majorant and geometry.** Since the roots are positive, expansion
of the product gives p_k=a(-1)^(d-k) times the (d-k)th elementary
symmetric polynomial in the roots. Every such symmetric polynomial
is positive, including the zeroth one, so all p_k are nonzero and,
for every t>=0,

    A(t):=sum_(k=0)^d |p_k|t^k
         = |a| product_(j=1)^d(t+rho_j) >0.                 (1)

For i!=j the larger root divided by the smaller is at least Q:
multiply consecutive ratios if necessary. Because (u-1)/(u+1)
is increasing for u>0, this gives

    |rho_i-rho_j| >= h(rho_i+rho_j).                      (2)

Here 0<h<1 and 0<eta=h/2<h. Let D_i be the open disk centered
at rho_i with radius eta rho_i. By (2), the distance between two
centers is strictly greater than the sum eta(rho_i+rho_j) of their
radii. Thus the closed disks are pairwise disjoint. Each closed disk
lies in Re z>0 since rho_i-eta rho_i>0. The only zero of p in D_i
is its simple zero rho_i; no zero of p lies on its boundary.

**Uniform boundary ratio.** Fix any i and any z with
|z-rho_i|=eta rho_i. Formula (1) yields the exact ratio

    |p(z)|/A(|z|) = product_(j=1)^d
                          |z-rho_j|/(|z|+rho_j).         (3)

For j=i, |z|<=rho_i+eta rho_i gives

    |z-rho_i|/(|z|+rho_i)
        >= eta/(2+eta) = h/(4+h).                        (4)

For j!=i, using (2) and rho_i<=rho_i+rho_j,

    |z-rho_j| >= |rho_i-rho_j|-|z-rho_i|
              >= h(rho_i+rho_j)-eta rho_i
              >= (h-eta)(rho_i+rho_j),
    |z|+rho_j <= (1+eta)rho_i+rho_j
              <= (1+eta)(rho_i+rho_j).

All denominators are positive, and h-eta>0, so

    |z-rho_j|/(|z|+rho_j)
        >= (h-eta)/(1+eta) = h/(2+h).                   (5)

Multiplying (4) and all d-1 instances of (5) in (3) gives

    |p(z)| >= [h/(4+h)] [h/(2+h)]^(d-1) A(|z|)
            = 2 epsilon(d,Q) A(|z|).                   (6)

For d=1 this multiplication uses an empty product equal to one,
so the same estimate remains valid without using (2) or (5).
There is no lower or upper root-scale bound in (1)--(6), and no
upper bound on consecutive root ratios has been used.

**Perturbation, counts and real roots.** By the coefficient hypothesis,

    |e(z)| <= sum_(k=0)^d |e_k||z|^k
            <= epsilon(d,Q) A(|z|) < |p(z)|             (7)

on every boundary circle. The strict inequality follows from (6),
A(|z|)>0 and epsilon(d,Q)>0, even when some coefficient bounds
are attained. Both polynomials are entire, so Rouche's theorem applies
on and inside each circle and gives exactly one zero of p+e in D_i,
counted with multiplicity. Also 0<h/(4+h)<1 and
0<h/(2+h)<1, whence 0<epsilon(d,Q)<1/2<1. In particular

    |p_d+e_d| >= (1-epsilon(d,Q))|p_d| >0.

Thus p+e has exact degree d. The d disjoint disks already account
for all its d zeros, by the fundamental theorem of algebra. Each disk
is invariant under complex conjugation and p+e has real coefficients.
A nonreal zero in a disk would therefore give a distinct conjugate
zero in that same disk, contradicting its multiplicity-one zero count.
Its unique zero is consequently real, simple and, since Re z>0 in
the disk, positive. The disjoint real intervals are ordered as the
centers, establishing the indexed localization in the conclusion.

Finally, multiplication by a common nonzero scalar multiplies all
|p_k| and |e_k| by its absolute value. Under z->c z the kth
coefficient is multiplied by c^k and every root and disk radius by
1/c. The coefficient inequalities and root ratios are preserved in
both cases; epsilon itself depends on neither operation. This proves
all the claimed invariances and finishes the specialization.

**Separate critical audit, step494 (2026-11-05).** Independent replay
against the approved primary-source cases found no failed inequality
or missing hypothesis. In particular, the weights in the componentwise
certificate are strictly positive by (1); the entire polynomials meet
Rouche's analytic hypotheses on every closed disk; and (6) gives a
factor-two margin, so weak coefficient bounds still imply the strict
inequality (7). The displayed expression in Q follows from

    h/(4+h)=(Q-1)/(5Q+3),
    h/(2+h)=(Q-1)/(3Q+1).

Thus both formulas for epsilon agree. The empty product at d=1,
nonzero varying leading coefficient, exhaustion of the degree,
conjugation within each disk, positivity, arbitrary scales and the two
invariances were all checked. No lower bound on a root, upper bound on
a root ratio, monicity, or input-root premise for p+e was inserted.
The general source results are imported; this audit validates only the
explicit quantitative specialization. It provides no actual residual
comparison or new result beyond the cited method's finite application.
The inherited SPECIALIZE scope is recorded in
`drafts/literature/2026-11-05-relative-root-disk-bound-audit.md`.

## Mathlib

Full matching coverage of this explicit d,Q tolerance has not been
checked. Mathlib coverage of the componentwise certificate, Rouche
disk count and conjugation inputs is also unchecked; no absence is
inferred. This is a checkable informal proof with primary citations,
not a Lean verification or a numerical certificate.
