# L257 — Massless moving-cut comparison in the ordered static trace

## Hypotheses

Use exactly L256(1)'s U_i^0(F^0), equivalently L178(2)'s W_i[G,G],
for the relative SU(2) box (-4,4)^4, admitted even N, a=8/N, the
straight lower-rooted direction-1 forest, stored coordinates, bare-first
order and both actual probes i=3,6 at tau=1/16. Here G=Delta_T^(-1)
on V_T={1,...,N-1}^3, with Delta_T=6I-T_N. Keep L175's J_j, S,
A^gen, h_k, m_(j,l) and the complete finite-mesh heat coefficients
c_(i;kl,a). Both generator orders, all action/source/end rows and
allowed constant component indices remain. The two Q subtractions
are already accounted for in L256's imported comparison with V_i.

The following expansion defines a second finite expression without
commuting any of its factors. Put x=(s,X), e=(r,U,1), where x is an
interior vertex and e a positive component-1 variable link. For each
j,k,l set

    B_(jkl)(s,t,X;e,f)
      = sum_(Y in V_T) G_(XY) m_(j,l)(t,Y) (J_j G)_(YU)
                    (A^gen)_(ef) (h_k)_f S_(f,x).             (1)

Here 1<=s,t<N, X,U in V_T, 0<=r<N, f ranges over every variable
positive link, and J_j acts on V_T. Every term of (1) has the same
ordered matrix contraction as L178(6); only its Z index has been
summed into J_j G. Define the triangular comparison by

    U_i^triangle
      =-6 sum_(k,l) c_(i;kl,a) sum_(j=2)^4
          sum_(s,t,X,e,f) s 1_(t>s) B_(jkl)(s,t,X;e,f).        (2)

The action remains at t and the generator/probe at their original
rows near s. Neither Green inverse nor any coefficient is frozen.
This is a trace-sum comparison, not a replacement covariance law.

## Conclusion

For sufficiently large admitted N, with mesh-independent constants,

    |U_i^0(F^0)-U_i^triangle| <= C_i N^(5/2), i=3,6.          (3)

Before the heat sum, the j,k,l error is bounded by
C p(k)p(l)N^(5/2) for a fixed polynomial p. Thus (3) is inside the
proposed N^(5/2)log(eN)^2 static-error budget. It addresses only the
moving-cut part of that error.

Relative to the imported L256(3) and L179(7), it also gives

    |V_i-U_i^triangle| <= C_i N^(5/2)sqrt(log(eN)),
    lim_(N->infinity) a^3 U_i^triangle = K_(i,Vmix).          (4)

There is no quantitative bound here for
|U_i^triangle-a^(-3)K_(i,Vmix)|. Boundary transfer, transverse
coefficient freezing and complete raw coefficient/heat matching still
require proof. The limit in (4) identifies the coefficient by the
already established limit, not by inserting zero mass into L179(5).
This is REPRODUCTION of elementary finite spectral/trace estimates
for the specified ordered word, with no claim of progress beyond the
sources checked. The separate critical audit in proof section 5 accepts this
specialization relative to its stated imports. It supplies no complete component or L011 remainder,
interacting reflected bound, continuum construction or mass gap.

## Proof

### 1. Uniform full-source Green column bounds

The normalized scalar Dirichlet eigenfunctions are

    phi_q(X)=(2/N)^(3/2) product_(d=2)^4 sin(pi q_d X_d/N),
    lambda_q=4 sum_(d=2)^4 sin^2(pi q_d/(2N)),
                          1<=q_d<N.                         (5)

The finite sine orthogonality identity gives an orthonormal basis;
substitution into 6I-T_N verifies the eigenvalues, including the
diagonal six on end rows. Since sin(pi q/(2N))>=q/N for 1<=q<N,
lambda_q>=4|q|^2/N^2 and |phi_q(X)|^2<=8/N^3. A shell
max_d q_d=m has at most 3m^2 labels. Consequently, uniformly over
every X in V_T,

    G_(XX) <= (8/N^3)(N^2/4) sum_q |q|^(-2) <= 6,
    (G^2)_(XX) <= (8/N^3)(N^4/16) sum_q |q|^(-4)
               <= (3N/2) sum_(m=1)^(N-1) m^(-2) <= 3N.     (6)

For the last inequality, sum_(m>=1)m^(-2)<=1+integral_1^infinity
x^(-2)dx=2. These estimates retain every transverse label, including
the lowest ones, and need no compactness of X.

Let v be an arbitrary scalar vertex array with zero values at pinned
boundary vertices. Then (J_j v)(Y)=v(Y+e_j)-v(Y-e_j). Write this
as the sum of its two adjacent forward differences and use
|b+c|^2<=2|b|^2+2|c|^2. Each directional edge occurs at most twice
in the vertex sum, including end edges. Thus

    ||J_j v||_2^2 <=4 <v,Delta_T v>.

With v=G delta_U, symmetry and Delta_T G=I give

    ||G_(X,.)||_2^2=(G^2)_(XX)<=3N,
    ||J_j G_(.,U)||_2^2<=4G_(UU)<=24.                        (7)

For any real diagonal multiplier m on this same space, finite
Cauchy--Schwarz now yields the ordered bound

    |sum_Y G_(XY) m(Y) (J_j G)_(YU)|
                       <=sqrt(72N) ||m||_infinity.           (8)

It is essential to sum the signed J_j difference before applying
(8). The multiplier is on its left and stays there. No J_j/G or
multiplier/inverse commutation, positivity of the response, bound on
an infinite-volume inverse, or deletion of boundary inputs is used.

### 2. Exact cut difference and local closing indices

L178(6), with Q_1=Q_2=G, gives exactly

    U_i^0(F^0)=-6 sum_(k,l) c_(i;kl,a) sum_(j=2)^4
       sum_(s,t,X,e,f) min(s,t) 1_(r<t)
                                     B_(jkl)(s,t,X;e,f).    (9)

The component-1 level r includes both end edges. P_(t,r)=1_(r<t)
does not depend on Y or Z, so its extraction in (9) commutes no
spatial operator. On t>s, min(s,t)=s. Subtracting (2) from (9)
therefore changes precisely the scalar weight to

    min(s,t) [1_(r<t)-1_(s<t)].                              (10)

L178 proof sections 1--2 give fixed constants R,b,C such that
A^gen has finite range R, bounded row/column degree b and entries
bounded by C/a. This includes the full adjoint orientation and its
variable coefficient differences. S_(f,x) is nonzero only when f is
one of the at most eight positive links incident to x. For each such
f only a fixed number of e can have (A^gen)_(ef) nonzero. In
particular |r-s|<=R' for a fixed R', and the number of allowed (e,f)
for a fixed x is bounded independently of N. These assertions use
the local generator, not localization of a Green source.

For such a term the two indicators in (10) differ only between r
and s. In particular |t-s|<=R'+1 and there are at most 2R'+3
possible t for a fixed s. This includes the diagonal row t=s whenever
it contributes; it is bounded as an error, not assigned a vanishing
weight by convention. Also min(s,t)<=N on every retained row.

### 3. Actual coefficient scales and the full heat sum

L178(4)--(5) give, for a fixed enlarged polynomial p,

    ||m_(j,l)(t,.)||_infinity<=C a^3 p(l),
    |(A^gen)_(ef)(h_k)_f S_(f,x)|<=C p(k)                  (11)

whenever (A^gen)_(ef)S_(f,x) is nonzero. The second bound is the
product of C/a, C a p(k), and the bounded endpoint incidence.
The h bound is used only on the compact input support of A^gen.
It asserts no smooth extension of the upper forest jump. The first
bound holds at every action level and transverse source row by the
actual smooth action extension Lh_l=Lv_l; no action cutoff is added.

Apply (8) and (11) to (1) before counting (10). There are at most
N^4 closing vertices x=(s,X); each permits a bounded number of e,f
and changed t. Combining their weights gives, for each j,k,l,

    sum_(changed s,t,X,e,f)
          |min(s,t) B_(jkl)(s,t,X;e,f)|
       <= C N^4 N a^3 sqrt(N) p(k)p(l)
       <= C p(k)p(l) N^(5/2),                            (12)

because a=8/N. All transverse Y and Z sums were already retained
in (8), and all end rows remain in the finite spectrum and energy
inequality. There is no extra boundary collar or unspecified source
remainder in (12).

L156(8) supplies, uniformly in N for either complete actual probe,
sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i. Its positive physical spectral
gap and Gaussian heat factors accommodate this fixed polynomial,
with every allowed constant component index retained. Sum (12)
over j,k,l with the sole -6 from (9), using absolute heat weights
only for the bound. This proves (3), for both probe polarizations
without a finite heat cutoff or any numerical premise.

### 4. Coefficient identification and the remaining threshold

Combine (3) with L256(3) by the triangle inequality to obtain the
first line of (4). Multiplying by a^3 gives an error at most
C_i N^(-1/2)sqrt(log(eN)), tending to zero. L179(7)'s existing
limit for a^3 V_i then proves the second line of (4). This uses no
mesh-dependent mass or interchange of limits. Both Q subtractions
enter once through L256's imported comparison; none is added to (2).

The remaining exact quantitative question is the difference between
(2) and a^(-3)K_(i,Vmix). Its action coefficient still depends on
(t,Y), its generator/probe on the closing local rows near (s,X),
and it still contains both massless finite Green inverses. In
particular (3) does not permit their replacement by a frozen bulk
kernel. The full static target remains open, although its moving-cut
error now meets the required budget at zero mass. L179's earlier
fixed-mass/fixed-degree strip count did not give this uniform estimate.
The proof requires only finite sine sums and the ordered estimate
(8); no mathematical script or numerical experiment is needed.

### 5. Separate critical audit, 2026-10-21

The audit accepts (3)--(4) relative to the stated imports. It checks
the exact finite expansion, all-source estimate and count, not the
upstream derivation of V_i or L179's successive-limit theorem. No
correction, changed exponent or new mathematical input is required.
The unchanged ordered-static source assessment covers this audit.

**Exact weight and domains.** L178(2),(6) have vertex indices
(s,X),(t,Y),(t,Z) and component-1 link index (r,U), with
1<=s,t<N and 0<=r<N. Summing Z gives precisely J_j G, since
P_(t,r) is independent of Z. The original weight is min(s,t)1_(r<t).
The proposed weight is s1_(s<t). The identity
s1_(s<t)=min(s,t)1_(s<t) holds also at t=s, so their difference
is exactly (10). For r<s the changed integers satisfy r<t<=s;
for r>s they satisfy s<t<=r, with the opposite sign. For r=s
there are none. Intersecting these intervals with 1<=t<N retains
the diagonal and all admissible end cases. Locality of the complete
A^gen and incidence of S give |r-s|<=R', so there are at most
R' changed t for each nonzero closing term; the stated larger
constant is valid. Neither physical coefficient level is equated.

**Finite Green estimate including end rows.** The tensor sine modes
are orthonormal on exactly V_T. With shell max q_j=m, the number
of labels is m^3-(m-1)^3<=3m^2 and |q|>=m. Hence (5) gives
G_XX<=6(N-1)/N<=6 and
(G^2)_XX<=(3N/2) sum_(m>=1)m^(-2)<=3N.
For a zero-boundary vertex vector, J_j v is the sum of the two
incident forward differences. Their squared sum is at most four
times the complete directional edge energy, including both pinned
end edges, and that energy is at most <v,Delta_T v>. Substituting
v=G delta_U proves ||J_j G delta_U||_2^2<=24 for every U.
Cauchy--Schwarz with ||G delta_X||_2<=sqrt(3N) now gives (8)
with exactly sqrt(72N). All Y sources remain in both norms. In
particular this is not a bound on the absolute entries of J_j times
G, and it does not require a commuting multiplier.

**Local factors and power count.** L178(4)--(5) apply to both
orders of A^gen, including its coefficient differences. Each closing
vertex permits a bounded number of incident f and corresponding e;
no additional sum of N axial edges is hidden in this local count.
On these input links |h_k|<=C a p(k), while |A^gen|<=C/a.
The action multiplier is globally bounded by C a^3 p(l), including
all source levels and transverse rows, by L175's specified extension
and L156(10). Thus (8) bounds each contracted summand before its
cut weight by C a^3 sqrt(N)p(k)p(l). At most N^4 closing vertices,
a bounded changed strip, and min(s,t)<=N give
C a^3 N^(11/2)=C' N^(5/2). This confirms (12) without a
source cutoff or a smooth extension of the forest exterior.

**Heat and coefficient identification.** L156(8) sums any fixed
polynomial envelope uniformly over the complete relative spectrum
of each probe. The allowed constant component indices are present;
the positive physical gap excludes only a nonexistent all-zero mode.
The factor -6 occurs once. Adding L256(3) once yields the first
line of (4); its cubic-normalized error is
O(N^(-1/2)sqrt(log(eN))). L179(7), imported as a theorem here,
then identifies the same K_(i,Vmix). Both Q subtractions have already
entered through L175 and are not added again. No coefficient is set
to zero, nor is a mass chosen inside a qualitative limit.

This validates the moving-cut comparison only. L258's deterministic
comparison and L259's sampled static estimate have their own audit
records; they are not consequences of (3) alone. The preserved failures
ATTEMPTS/030/038/045 concern different shortcuts. No complete-response
rate, interacting estimate or construction follows from this audit.

## Mathlib

Full matching theorem: **not checked**. Supporting finite sine
orthogonality, Cauchy--Schwarz, Dirichlet spectral and trace-sum results:
**not checked**. Unknown availability is not evidence of absence.
Reuse the unchanged [source assessment](../drafts/literature/2026-10-20-smooth-action-ordered-static-rate.md).
No new external result is imported or reproved. The elementary proof
above is needed to remove the fixed-positive-mass dependence in the
moving-cut step for this exact ordered static expression.
