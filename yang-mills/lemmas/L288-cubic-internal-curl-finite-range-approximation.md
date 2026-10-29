# L288 — Uniform finite-range approximation of the cubic internal-curl operator

## Hypotheses

Use L280's SU(2) relative cube D=[-4,4]^4, even N>=2 and a=8/N.
Pin boundary-contained links, fix gauges at boundary vertices and retain
every other link, including both normal endpoint cases. All matrices use
Euclidean counting measure. Let C be the complete relative plaquette
incidence, B the relative vertex incidence, L=C*C+BB*, and G the extended
transverse covariance in L280(18). Pinned slots are extended by zero.

Use the exact ambient all-link Wilson cubic jet on this same slice as
in L287(1), with its ordered signed plaquette slots and all three colors.
In particular, retain the quadratic random polynomial

\[
 \mathsf B(u;x)=\sum_p(Cx)_p\cdot D\zeta_p(x)[u],\qquad
 u^*E_N^{\rm int}v=2\mathbb E_G[\mathsf B(u;x)\mathsf B(v;x)] .
                                                               \tag{1}
\]

Here u,v are arbitrary real edge/color vectors. L287's proof of the
exact vertex and its bounds uses L286; their separate audits accept
those inputs under their stated hypotheses. No nonlinear forest
jet is transported to this slice.

For the source conclusion below, use L002/L282's exact nonnegative
product bump h_+=f_*, h_-=theta f_*, supported in
[-1/4,1/4]^3 times [1,2] and [-2,-1], respectively. Source derivatives
are at zero in (|s|+|t|)||f_*||_infinity<eta<1. Keep L281's source maps
and both source orders in G_-+, and L287's complete group M_{3,N}.

## Conclusion

For m>=0 put M=m+1 and reuse L283(5)'s geometric polynomial

\[
 h_m(\lambda)=\frac1{16}\sum_{j=0}^m(1-\lambda/16)^j,
 \quad \widehat G_{N,m}=C^*C\,h_m(L)^2,
 \quad R_{N,m}=G-\widehat G_{N,m}.                            \tag{2}
\]

The hat distinguishes this positive transverse approximation from
L283's different entrywise approximation. Define E_{N,m}^{int} by (1)
with a Gaussian of covariance widehat G_{N,m} tensor I_3. There is a
constant K, independent of N,m, such that

\[
 0\le E_N^{\rm int}-E_{N,m}^{\rm int}\le\frac K{m+1}I,
 \qquad \|E_{N,m}^{\rm int}\|\le K.                          \tag{3}
\]

For fixed m, E_{N,m}^{int} has finite lattice range at most c(m+1),
with c independent of N,m. Every row farther than c'(m+1) lattice
units from the boundary agrees exactly with its infinite-lattice
polynomial construction. The estimate (3) holds on every row of the
actual relative box, without removing boundary layers or vertex pairs.

The corresponding complete source contraction satisfies

\[
 \sup_{N\ {\rm even}}N^{-2}
 \left|\frac14\operatorname{Tr}
       ((E_N^{\rm int}-E_{N,m}^{\rm int})G_{-+})\right|
       \le\frac{C_f}{m+1}.                                  \tag{4}
\]

Thus, with ell_N=log(eN),

\[
 \left|N^{-2}M_{3,N}
       -\frac1{4N^2}\operatorname{Tr}(E_{N,m}^{\rm int}G_{-+})\right|
 \le C_f\left(\frac1{m+1}+\frac{\sqrt{\ell_N}}N
                                 +\frac{\ell_N}{N^2}\right).  \tag{5}
\]

This controls a complete internal approximation and its source sandwich,
not a hard truncation of the original kernel. No bulk coefficient or
limit of M_{3,N}/N^2 is evaluated. Both mixed insertion/action groups,
the distinct-line cubic group and compensation with L285(4) remain
unresolved. So do subleading control, a uniform higher remainder,
continuum axioms/positivity, a nonzero sector and finite positive mass.
This is partial local progress within the existing EXPLORE assessment,
not certified originality or a complete-solution candidate. The separate
audit in section 5 accepts this approximation under the stated hypotheses.

## Proof

### 1. A positive transverse approximation and two residual diagonals

L280(21)–(23) gives the orthogonal invariant splitting into im B and
H=ker B*. On H, L=C*C and G=L^-1; on im B, C*C and G vanish.
Also C*C commutes with L, since CB=0. For 0<lambda<16 set

\[
 r_m(\lambda)=(1-\lambda/16)^M,\qquad
 d_m(\lambda)=1-(\lambda h_m(\lambda))^2=2r_m-r_m^2.
\]

Consequently widehat G has eigenvalue lambda h_m(lambda)^2 on H,
and R has eigenvalue d_m(lambda)/lambda there. Both vanish on im B.
In particular,

\[
 \begin{gathered}
 0\le\widehat G\le G,\quad 0\le R\le L^{-1}d_m(L),\quad
 \|\widehat G\|\le M/16,\quad \widehat G_{ee}\le30,\\
 0\le C\widehat G C^*\le CGC^*\le I,\qquad
 0\le CRC^*\le I,\qquad 0\le d_m(\lambda)\le2e^{-M\lambda/16}.
                                                               \tag{6}
 \end{gathered}
\]

The norm estimate uses h_m<=M/16 and lambda h_m<=1; the diagonal
bound and projection statement are L280(22)–(23) and L287(8).

Here are uniform estimates including small N and both endpoints.
For any of L280(21)'s component mode sets, an eigenvector has squared
point value at most 16/N^4. The eigenvalue obeys lambda_k>=4r^2/N^2
when max k=r>=1, with at most 15r^3 indices in that shell. For beta>0,
integrating over the disjoint intervals [r-1/2,r] gives

\[
 \sum_{r\ge1}r e^{-\beta r^2}\le\frac2\beta,
 \qquad
 \sum_{r\ge1}r^3 e^{-\beta r^2}\le\frac8{\beta^2}.           \tag{7}
\]

Indeed x>=r/2 and e^{-beta x^2}>=e^{-beta r^2} on that interval;
the summands are at most four times its integral of x e^{-beta x^2},
or sixteen times its integral of x^3 e^{-beta x^2}, respectively.
Extend the sum of integrals to [0,infinity). With beta=M/(4N^2),
shell summation therefore gives, for each component mode set,

\[
 N^{-4}\sum_k\lambda_k^{-1}e^{-M\lambda_k/16}\le30/M,
 \qquad N^{-4}\sum_k e^{-M\lambda_k/16}\le1920/M^2.           \tag{8}
\]

The sets exclude the all-zero index. Enlarging them to all nonnegative
indices with max k>=1 only increases these estimates.

For a relative plaquette p of orientation mu nu, only component mu
and component nu one-form modes contribute to (Cv_k)_p. For a mode
in component mu, the difference is in coordinate nu. L003 section 2's
exact sine-to-midpoint-cosine difference, now in counting normalization,
gives

\[
 |(Cv_{\mu,k})_p|^2
       \le\frac{16}{N^4}\,4\sin^2(\pi k_\nu/(2N))
       \le\frac{16\lambda_k}{N^4}.                          \tag{9}
\]

There is one such component term in a basis eigenvector, not the sum
of two components. This formula includes first and last normal links:
vertex modes vanish at the boundary and their difference on each end
interval is the same midpoint cosine identity. Boundary-contained
plaquettes have zero relative row. Zero own-direction cosine indices
are included; differentiating a zero mode gives zero when applicable.

Use (8) and d_m<=2e^{-M lambda/16} in the positive comparison (6).
For the curl diagonal, multiply that comparison by C and C*, and
apply (9) separately to the two allowed components. This proves the
explicit, deliberately coarse bounds

\[
 \sup_e R_{ee}\le960/M,\qquad
 \sup_p(CRC^*)_{pp}\le122880/M^2.                            \tag{10}
\]

These are estimates on the complete finite relative matrices. They do
not assert small operator norm for R or CRC* as N grows.

### 2. Independent Gaussian splitting controls the whole operator

Couple independent centered real Gaussian edge/color vectors y,z with
covariances widehat G tensor I_3 and R tensor I_3, respectively. Then
x=y+z has covariance G tensor I_3. Singular covariances cause no
problem: use their finite positive square roots on independent standard
normal vectors. Since D zeta(x)[u] is linear in x,

\[
 \begin{split}
 \mathsf B(u;y+z)={}&\mathsf B(u;y)+\mathsf B(u;z)
                         +\mathsf X(u;y,z)+\mathsf Y(u;y,z),\\
 \mathsf X(u;y,z)={}&\sum_p(Cy)_p\cdot D\zeta_p(z)[u],\\
 \mathsf Y(u;y,z)={}&\sum_p(Cz)_p\cdot D\zeta_p(y)[u].       \tag{11}
 \end{split}
\]

All sums retain all plaquette orientations and actual signed slots.
As in L287(10), each polynomial is a fixed finite sum of types with
fixed coefficients. A type has coefficient vector alpha_p=u_{e(p)}^b
on one plaquette orientation and a product (Cw)_p^a w'_{f(p)}^c,
where a!=c. Slot signs are absorbed into the fixed coefficient. Every
edge-selection map has bounded multiplicity mu independent of N, so
sum_p |alpha_p|^2<=mu ||u||^2. One may take the same mu=24 as L287.

We use L287(11)'s finite Schur-product inequality: for positive matrices
A,K, ||A circle K||<=||A|| max_p K_pp. It follows by factoring K into
rank-one terms and testing the quadratic form; it holds on the full
plaquette set and under repeated edge selection. An edge selection
matrix S obeys ||S||^2<=mu. Thus a selected covariance has norm at most
mu times its original norm and its diagonal is an actual edge diagonal.

For one type in B(u;z), its L2 norm squared is the quadratic form of
(CRC*) circle (S R S*) on alpha. The two colors a!=c are independent.
By (6), (10), and the selection bound, it is at most
(960 mu/M)||u||^2 times the square of its fixed coefficient.
For a type in X the matrix is (C widehat G C*) circle (S R S*),
and the same bound holds by independence of y,z and (6).

For a type in Y the matrix is (CRC*) circle (S widehat G S*).
Apply the same inequality with the factors interchanged. Its norm is
at most

\[
 \|S\widehat G S^*\|\max_p(CRC^*)_{pp}
       \le (\mu M/16)(122880/M^2).
\]

The alpha norm bound gives again a constant times M^-1 ||u||^2.
This step uses the stronger residual curl diagonal, rather than
incorrectly requiring ||CRC*|| to tend to zero. Taking the finite L2
triangle bound over all exact monomial types and the three polynomials
gives, for Z_u=B(u;z)+X(u;y,z)+Y(u;y,z),

\[
 \mathbb E[Z_u^2]\le K_0M^{-1}\|u\|^2.                    \tag{12}
\]

This estimate keeps every cross term between types: no independence
between different types is assumed. The number and coefficients of
types depend only on the four-slot SU(2) vertex, not on the mesh.

Each B(u;z) is centered because its two field colors are distinct.
Each mixed term in (11) has conditional mean zero over z for fixed y.
Hence E[Z_u|y]=0. In particular B(u;y) is orthogonal in L2 to Z_v
for every u,v. Expanding (1) using (11) therefore gives the exact identity

\[
 u^*(E_N^{\rm int}-E_{N,m}^{\rm int})v=2\mathbb E[Z_uZ_v].   \tag{13}
\]

Positivity and (12) prove the first part of (3). The retained covariance
operator itself is positive, so E_{N,m}^{int}<=E_N^{int}; L287(4)
gives its uniform bound. All internal pairs and boundary slots were
included throughout, with no spatial or color truncation.

### 3. Finite range and exact bulk agreement

The matrices C*C and L have fixed local range on the relative cubical
complex, and h_m has degree m. Thus widehat G=C*C h_m(L)^2 is a
polynomial path expression of range at most c_0(m+1). Multiplication
by C or C* enlarges that range by only a fixed number of cell steps.

The covariance defining E_{N,m}^{int} is obtained by the two crossing
Gaussian pairings of the quadratic expressions (1). A pairing contains
either a curl-curl entry times an edge-edge entry, or two curl-edge
entries, all formed from widehat G. Its external edge slots lie in the
respective plaquettes. If their distance exceeds c(m+1), these entries
vanish. The coefficients are products and sums of finite local paths;
when all these paths and incident plaquettes avoid the boundary, they
equal exactly the full-lattice paths. Increasing the distance constant
by a fixed amount includes the incident plaquettes and every path used
in a whole row. This proves the stated bulk agreement. End links and
corners remain in the relative construction; no bulk identity is
claimed for a path touching them.

This section gives exact locality of the approximant, not a claim that
its boundary layer contributes negligibly to a later source limit.
Such a passage still has to use actual source fields and their norms.

### 4. Source normalization and comparison with the original group

Global color rotations leave B and the scalar-color covariances
invariant, so the two E operators and their difference are scalar
in external color, as in L287 section 3. Let D_0 be the one-color
block of E_N^{int}-E_{N,m}^{int}. L287(14), with the rectangular
separated matrix denoted by mathsf T, gives

\[
 \|U_\pm\|\le\sqrt{F/12}\,N,\qquad
 \|\mathsf T\|_1\le8^4F C_{\rm sep},\qquad F=\|f_*\|_\infty.
\]

Equation (3) therefore implies
||U_+* D_0 U_-||<=K F N^2/(12M). Exactly as in L287(17),

\[
 \frac14\operatorname{Tr}((E_N^{\rm int}-E_{N,m}^{\rm int})G_{-+})
       =\frac32\operatorname{Tr}(U_+^*D_0U_-\mathsf T).       \tag{14}
\]

The factor is three external colors times two source orders times 1/4.
Internal colors are already included in D_0. The finite trace-norm
inequality |Tr(V mathsf T)|<=||V|| ||mathsf T||_1 proves (4), including
empty source sets. Combining (4) with L287(5)'s complete external-curl
error proves (5). No interchange of m,N limits was used in these
uniform estimates. L287(6)'s external tail remains available; it does
not itself evaluate the finite-range source sandwich or the other
cubic groups.

### 5. Separate critical audit (2026-10-26)

This audit accepts (3)–(5), including positivity and uniformity on all
relative rows. On H the retained covariance has eigenvalue
lambda h_m(lambda)^2=(1-r_m)^2/lambda; its residual is
(2r_m-r_m^2)/lambda. Both are nonnegative, and both vanish on im B.
Thus the independent Gaussian splitting used here is legitimate;
it is distinct from the correlated source approximation in L291.

The shell estimates can be checked directly from their constants.
For beta=M/(4N^2), the first sum in (8) is bounded by
15/(4N^2) times 2/beta=30/M; the second by
15/N^4 times 8/beta^2=1920/M^2. Multiplying the former by
16 times 2 gives 960/M. For the curl diagonal there are two
component modes; their difference bound (9) cancels the inverse
eigenvalue. Hence 2 times 16 times 2 times 1920/M^2 gives
122880/M^2. The endpoint sine-to-midpoint-cosine identity is the
same at the first and last normal links, and pinned rows vanish.
The interval argument for (7) works for every beta>0, so these
bounds also cover M large compared with N^2 and small even N.

For B(u;z) and X, the selected residual edge diagonal is O(M^-1)
and the curl covariance norm is at most one. For Y, these roles
must be interchanged: the selected retained edge norm is O(M),
while the residual curl diagonal is O(M^-2). This yields O(M^-1)
again. The finite type count and bounded slot multiplicity make all
three statements estimates on the whole L2 polynomial, including
cross terms. No small norm of R or CRC* is needed or claimed.

Every residual has conditional mean zero given y. In particular
B(u;z) has zero mean because each of its monomials uses distinct
colors, even when the spatial slots coincide. This establishes the
orthogonality used in (13), and hence the positive operator difference
and its K/M bound. Path locality of the polynomial covariance implies
finite range of both Wick products defining E_m and exact agreement
of an entire interior row. It does not by itself discard the boundary.
Finally the source norms, nuclear-norm tail and the factor 3/2 in
(14) give the normalized K_f/M trace error with both orders and all
colors. These estimates are uniform before any m,N limit. Evaluation
of the bulk coefficient and boundary passage remain separate steps.

## Mathlib

Coverage of the full Wilson-specific relative-box operator approximation
is not checked; no absence or matching-theorem claim is made. The proof
reuses L003's exact relative sine/cosine modes, L280's quadratic Hodge
decomposition, L283's geometric polynomial, and L287's exact vertex,
finite Schur-product inequality and source estimates (from L281).
The new specialization is the positive covariance splitting and its
uniform summed two-vertex error. The shell estimates are displayed
because both powers and endpoint uniformity are essential; no new
external heat-kernel, renormalization or continuum theorem is imported.
