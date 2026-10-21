# L221 — A quantitative pinned-trace comparison with the finite diagnostic

## Hypotheses

Keep all of L079's hypotheses and definitions: SU(2), the fixed relative
cube, straight lower-rooted direction-1 forest, admitted even N with
a=8/N, tau=1/16, the actual two L010 probes i=3,6, and the
small-coupling coefficient taken at fixed mesh before refinement.
In particular J_(i,N), D_(i,a) and gamma are exactly L079(1)–(2),
with no continuum replacement of D_(i,a). All norms below use ordinary
dimensionless vertex coordinates. Keep every pinned transverse end
edge, every axial level and the complete exterior heat sum.

Use L079's coefficient bounds and exact finite-source representation,
L045's monopole energy projection, and the exact frozen angular tensor
of L070 as used in L079(15)–(17). The scalar Green inputs are Lawler
and Limic, *Random Walk: A Modern Introduction* (Cambridge, 2010),
Theorem 4.3.1, printed pp. 81–84, and Proposition 4.6.2(a), printed
p. 97, including its transient proof:
[author-hosted primary text](https://www.math.uchicago.edu/~lawler/srwbook.pdf).
Only their simple symmetric nearest-neighbor walk specialization in
dimension three is used. Their applicability was inspected in
`drafts/literature/2026-10-17-first-pair-pinned-trace-quantitative-rate.md`.

## Conclusion

For constants C_i independent of N and all sufficiently large admitted N,

    |a^3 J_(i,N)-2 gamma D_(i,a)| <= C_i N^(-1/2).       (1)

This is stronger than the approved threshold with the additional
factor log(eN)^2. L078's O(N^2) comparison also gives

    |a^3 F_(i,N)^circ-2 gamma D_(i,a)| <= C_i N^(-1/2). (2)

Equivalently, the unscaled comparison errors are O_i(N^(5/2)).
Neither statement gives an O(N^2) remainder, a quantitative continuum
limit for D_(i,a), or a rate for the complete L011 coefficient.
Independent L101 and other component rate gaps, finite matching,
the interacting reflected error <=c_box/2, continuum axioms and finite
positive infrared mass remain unresolved. This is a local mathematical
input obtained by specializing standard scalar estimates; the saved
EXPLORE assessment does not certify originality. The separate critical
audit below accepts this quantitative specialization relative to its
stated imported inputs; it does not independently audit all upstream
lemmas or establish any other component rate.

## Proof

### 1. Scalar estimates and their normalization

Put Omega_N={1,...,N-1}^3, let Delta_N be its scalar nearest-neighbor
Dirichlet Laplacian, and let G_N=Delta_N^(-1). Thus all six incident
edges, including edges to pinned zero vertices, contribute to the
diagonal. On Z^3 write Delta=6(I-P), where P is the transition
operator of simple symmetric nearest-neighbor random walk. Its Green
kernel g is one sixth of the walk Green function. The cited Theorem
4.3.1 supplies

    g(x)=c_3/|x|+O(|x|^(-3)) as |x| -> infinity,         (3)

with the appropriately rescaled positive constant c_3. We need no
value for c_3. Isotropy of the simple walk makes the leading norm in
that theorem a constant multiple of the Euclidean norm. In particular,
for each fixed bounded integer offset e,

    |g(x)| <= C/(1+|x|),
    |g(x+e)-g(x)| <= C_e/(1+|x|)^2.                     (4)

For |x|>2|e|, subtract the two leading terms in (3), whose difference
is O_e(|x|^-2); the two undifferentiated remainders are each
O_e(|x|^-3). Enlarge the constant on the remaining finite set.
This does not differentiate an asymptotic remainder.

For y in the fixed compact physical set K in L079(6), its lattice
distance from the complement of Omega_N is at least delta N for a
fixed delta>0 and sufficiently large N. Constants below may depend
on K and the fixed source stencil radius, but not on y or N.

### 2. A finite differentiated source has l2 comparison error O(N^-1/2)

Let t_y be supported in a fixed-radius neighborhood of y, have
sum_z t_y(z)=0 and ||t_y||_1<=B. These conditions include each
source sum_mu T_mu^T f_mu in L079(6), since its support is strictly
interior and each centered-difference adjoint has zero total mass.
They also include the coefficient-freezing error sources there.
Let

    h_infinity(x)=sum_z t_y(z)g(x-z),
    h_N=G_N t_y on Omega_N, extended by zero elsewhere.

Subtract g(x-y) inside the first sum and use (4), telescoping bounded
offsets if necessary. This gives

    |h_infinity(x)| <= C B/(1+|x-y|)^2,
    ||h_infinity||_2 <= C B.                              (5)

Proposition 4.6.2(a), multiplied by 1/6 and then summed against the
finite signed source, gives exactly, for x in Omega_N,

    h_N(x)=h_infinity(x)-E_x[h_infinity(S_exit)],          (6)

where S_exit is the first walk exit position from Omega_N. The walk
exits almost surely because the domain is finite; the boundary
function in (6) is bounded. Every possible exit position is distance
at least delta N minus a fixed stencil radius from the source.
Consequently (5) gives

    sup_(x in Omega_N)|h_N(x)-h_infinity(x)| <= C B N^-2.

There are at most N^3 interior vertices, so the squared l2 error
there is at most C B^2/N. Outside Omega_N, the squared error is at
most C B^2 sum_(|x-y|>=delta N)(1+|x-y|)^(-4), which is also
at most C B^2/N by three-dimensional shell counting. Thus

    ||h_N-h_infinity||_2 <= C B N^-1/2,
    ||h_N||_2 <= C B.                                    (7)

These estimates hold for signed sources and coefficients depending
on N, s and y, subject only to their stated uniform bounds. In
particular (6) retains all output rows, rather than restricting the
Green output to the compact source set. No assertion about an l2
monopole or a bounded inverse on arbitrary l2 sources is used.

### 3. Quantify the monopole energy projection

Use L045's energy completion, with
||f||_E^2=sum_(x,j)|f(x+e_j)-f(x)|^2. Let g_y(x)=g(x-y), and
extend g_(N,y)=G_N delta_y by zero. L045(5)–(6) prove exactly that
g_(N,y) is the energy orthogonal projection of g_y onto fields
supported in Omega_N, including the pinned end-edge energy.

Choose R=cN, with a fixed sufficiently small c>0 depending on K,
and a sampled cutoff chi_R equal to one on |x-y|<=R, zero on
|x-y|>=2R, bounded by one and with neighbor differences at most C/R.
Its support lies inside Omega_N. The edge product identity and (4)
give

    ||g_y-chi_R g_y||_E^2
       <= C sum_(|x-y|>=R-1)(1+|x-y|)^(-4)
          + C R^-2 sum_(R-1<=|x-y|<=2R+1)(1+|x-y|)^(-2)
       <= C/R.                                           (8)

The first shell sum is O(R^-1), and the second sum before its
R^-2 factor is O(R). The expression uses actual edge differences
of the energy-completion element g_y, already identified in L045;
chi_R g_y is finitely supported. Projection optimality therefore gives

    ||g_(N,y)-g_y||_E <= C N^-1/2.                        (9)

Every centered difference f(x-e_j)-f(x+e_j) has l2 norm at most
2||f||_E, by writing it as two nearest-neighbor differences. Hence
(9) also controls the centered derivative comparison on the whole
zero-extended lattice. The separate finite monopole l2 estimate
needed below is L079(11),

    ||g_(N,y)||_2 <= C sqrt(N),                           (10)

which follows from its full pinned sine expansion. This finite norm
is not an l2 norm for g_y.

### 4. Freeze the variable left coefficient with the same rate

Retain R_(k,a)=r_k/a^2 of L079 and write p(k) for one fixed
polynomial bounding its uniform physical C1 norm. Let R^y_j be its
value on the positive j-edge from y. Formula L079(12), equivalently
the exact stencil in L076(8), decomposes C_(R_(k,a))g_(N,y) on
interior vertices into

    sum_j R_j(w-e_j)[g_(N,y)(w-e_j)-g_(N,y)(w+e_j)]
      + sum_j [R_j(w-e_j)-R_j(w)]g_(N,y)(w+e_j).          (11)

Every boundary vertex value of g_(N,y) in this identity is its
pinned zero. By (10), the second line has l2 norm at most
C a p(k)sqrt(N)<=C p(k)N^-1/2.

In the first line, first replace the centered derivative of g_(N,y)
by that of g_y. The error is at most C p(k)N^-1/2 by (9), without
moving a coefficient across G_N. Next freeze the coefficient. If
r=|w-y|, the bounded physical C1 norm gives

    |R_j(w-e_j)-R^y_j| <= C p(k) min((r+1)/N,1).

By (4) the centered derivative of g_y is at most C/(1+r)^2.
Consequently its weighted squared l2 error is at most

    C p(k)^2 sum_(w in Z^3) min((|w-y|+1)/N,1)^2
                                             (1+|w-y|)^(-4)
       <= C p(k)^2/N.                                   (12)

Indeed the shells r<=N contribute at most C N/N^2 and the shells
r>N contribute at most C sum_(m>N)m^-2. The frozen infinite vector
outside Omega_N has squared norm at most C p(k)^2/N, again by (4)
and source-boundary separation. This last term explicitly accounts
for zero extension; (11) was used only on interior output vertices.
Both finite and infinite C_R are skew, so the same estimates apply
to their transposes. We have proved the quantitative version of
L079(13):

    || C_(R_(k,a))^T g_(N,y)-C_(R^y)^T g_y ||_2
                                      <= C p(k)N^-1/2.  (13)

The finite vector is zero-extended in (13). Both vectors have norm
at most C p(k). No unsupported smoothness of a rough Green output
or physical-face extension of the forest potential enters (11)–(13).

### 5. Freeze the right source, keeping its differentiated form

Use the exact h_(N,s,l,y) and finite f_mu in L079(5)–(6). For each
s<N and nonzero-source y, L079 section 1 bounds every coefficient
and its physical first derivative by C p(l), uniformly in s.
All nonzero-source y lie in the same K. On the fixed source stencil,
replace u_(a,1)(s) and the exterior alternating path coefficients
bar t_l/a by their frozen values u_(a,1)(s,y) and v_(l,a)(s,y).
As in L079 section 4, this changes sum_mu ||f_mu||_1 by at most
C a p(l). Crucially its resulting source error still has the form
sum_mu T_mu^T f_mu: the freezing occurs inside this divergence,
not after it. Its total mass is zero and its support radius is fixed.
By (7) its finite Green image therefore has norm at most C a p(l).
Apply (7) once more to the frozen source itself, with B<=C p(l).
With translation of y to the origin, this proves

    || h_(N,s,l,y)
        -G_infinity V_(u_(a,1)(s,y))^T
                        D^T Q_(v_(l,a)(s,y)) T delta_0 ||_2
                                      <= C p(l)N^-1/2.  (14)

Both vectors have norm at most C p(l). The finite stencil identity
D T=0 used in L079 makes the same Q and path coefficients occur
here; no rough path or Green factor is frozen as a smooth field.
All source and bound constants are uniform in s, y and the mesh.

### 6. Restore the exact tensor and sum every heat mode

Insert (13)–(14) in L079(5)'s l2 pairing b_(N,s,k,l,y).
Cauchy–Schwarz bounds its difference from the frozen pairing by
C p(k)p(l)N^-1/2. L079(15)–(16), using L070's full angular tensor
with its distinct incidence orientations, evaluates that pairing
exactly as -4 gamma u_(a,1)(s,y) R^y dot v_(l,a)(s,y).
The diagnostic's adjacent-edge vertex average U_(k,a)(y) differs
from R^y by at most C a p(k). Thus

    | b_(N,s,k,l,y)
       +4 gamma u_(a,1)(s,y) U_(k,a)(y) dot v_(l,a)(s,y) |
                               <= C p(k)p(l)N^-1/2.      (15)

Outside K the finite source and b vanish. Wherever the diagnostic
term is nonzero, u_(a,1)(s,y) is nonzero and y is in K as well.
Hence (15) covers every retained vertex, including the zero-source
ones, by taking K to include this fixed finite-stencil enlargement
of the displacement support.

L079's exact diagonal representation and diagnostic normalization
now give

    |a^3 J_(i,N)-2 gamma D_(i,a)|
       <= (a^5/2) sum_(k,l)|c_(i;kl)|
                      sum_(s=1)^(N-1) s sum_(y in Omega_N)
                                      C p(k)p(l)N^-1/2
       <= C (aN)^5 N^-1/2
                            sum_(k,l)|c_(i;kl)|p(k)p(l)
       <= C_i N^-1/2.                                   (16)

The final bound is the complete uniform heat summability L079(4);
p has only a fixed polynomial degree. In particular no constant
depending on a growing exterior-mode cutoff is hidden in (16).
The tensor sign is unchanged: the exact prefactor -a^2/2 times
the frozen -4 gamma gives +2 gamma, and a^4(sa)=a^5 s in the
finite diagnostic. This proves (1). Finally L078's O_i(N^2)
unscaled remainder contributes O_i(N^-1) after a^3 scaling, proving
(2). This does not change the other component comparisons.

### 7. Scope of the specialization and checks against known failures

The imported scalar theorems concern Delta_N on transverse vertices,
not the four-dimensional relative edge inverse. L078's exact
co-closed cancellation has already produced that scalar operator
before this argument begins. The only additional work is the
quantitative zero-mass-source comparison, energy cutoff, variable
coefficient estimate and restoration of the exact heat-summed trace;
the scalar Green asymptotic and killed-domain theorem are cited,
not reproved. The proof preserves the finite D_(i,a), the true upper
forest jump through the original finite reduction, all axial levels,
and the original residual including both subtractions through L079.
It does not reopen ATTEMPTS/024–025's bulk axial-profile deletion or
absolute-norm power-gain tests. The result quantifies the error after
subtracting the generally nonzero diagnostic coefficient; it does not
bound the original selected trace by O(N^(5/2)). No numerical
certificate or finite-mode preview supplies an analytic premise.

### 8. Separate critical audit, 2026-10-17

**Verdict: accepted relative to the stated imported inputs.** This audit
uses the prior SPECIALIZE coverage in
`drafts/literature/2026-10-17-first-pair-quantitative-rate-critical-audit.md`.
It checks the new estimates and their application, rather than
reproving the named random-walk results or all upstream reductions.
No new bound stronger than (1)–(2) is claimed.

The scalar normalization is consistent: for the killed simple walk
P_N, Delta_N=6(I-P_N), so both G_N and g are one sixth of their
walk Green kernels. The same factor therefore cancels nowhere in
(6); it is already included in both terms. Theorem 4.3.1's
simple-walk, transient and bipartite cases are covered by the saved
source assessment. Subtracting two O(r^-3) remainders gives O(r^-3),
which is sufficient for the O(r^-2) bounded-offset estimate (4).
No differentiated-remainder theorem is being imported implicitly.

For the right source, L079(6) places multiplication inside T_mu^T.
Its finite support stays strictly interior, so summing T_mu^T f_mu
over all vertices gives zero, for both the original and error sources.
Exit points are uniformly separated from that entire source support.
The maximum exit value is O(B N^-2); N^3 output vertices give squared
error O(B^2/N). The zero extension adds the full exterior shell sum
sum_(m>=delta N) O(m^2 m^-4)=O(1/N). Thus (7) is an all-output
comparison, not an interior-only estimate. Freezing f_mu changes its
l1 norm by O(a p(l)) and keeps zero mass, so the finite-image error
in section 5 is indeed O(a p(l)), uniformly in axial level.

For the left source, L045(5)–(6) applies to the ordinary scalar
Dirichlet energy with all normal end edges. The cutoff support fits
inside the box for a fixed c depending only on K. The derivative
tail in (8) is O(R^-1), and the cutoff-gradient term is
O(R^-2) times an O(R) annular sum. Projection therefore gives
O(N^-1/2) in energy and hence for each centered derivative. The only
monopole l2 norm used is finite: its sine expansion gives
C N^-3 sum_q lambda_q^-2 <= C N sum_(m>=1)m^-2.

The variable-coefficient stencil (11) agrees with L076(8), including
both transverse end edges. On interior output rows the bounded
coefficient multiplies the full derivative comparison before
freezing. Its derivative-free remainder costs
a p(k)||g_(N,y)||_2=O(p(k)N^-1/2). For the frozen derivative,
shells 1<=m<=N each cost O(p(k)^2/N^2), and shells m>N cost
O(p(k)^2 m^-2), giving (12). This shell majorant may be summed on
Z^3 without defining R outside the finite domain: the actual
coefficient difference is used only on interior rows. The omitted
infinite output is the separate tail already counted in section 4.
Finite C_R is skew by its defining difference of transpose pairs;
the infinite constant-coefficient stencil is skew as well. Hence the
transpose comparison introduces no extra boundary term or sign.

Finally, in b=<C_R^T g_N,h_N> the scalar trace contains C_R, not
C_R^T. L070's T=-i d and L078's centered incidence in V=+i u
diag(c_j^2)d are distinct. With Q=bar Q/a, the exact symbols give
(-2i)(-i)(2)=-4 and the normalized angular integral is
-4 gamma u R.v. The R-to-U average changes this by O(a p(k)p(l)).
The exact trace prefactor is -a^2/2: it is L078's -1/(2a),
times a^2 from r and a from bar Q. Thus the sign and coefficient
are +2 gamma, and scaling the trace by a^3 gives the diagnostic
weight a^5 s=a^4(sa). There are at most N^3 transverse vertices
and sum_s s<=N^2/2. The total error is consequently bounded by
C(aN)^5 N^-1/2 sum_(k,l)|c_(i;kl)|p(k)p(l).
L079(4)'s uniform complete heat sum applies to this fixed polynomial;
no cutoff-dependent constant is introduced. L078's separate O(N^2)
remainder contributes only O(N^-1) after scaling. This verifies both
(1) and (2) for i=3,6 under the imported hypotheses.

The audit needs no numerical values for gamma or D_(i,a), and no IEEE
enclosure premise. It accepts a comparison with the finite diagnostic,
not a continuum-diagnostic rate or a complete-response remainder.
ATTEMPTS/022–025's failed parity, centering, axial-profile and generic
norm shortcuts are not used. All construction gaps stated above
remain open. The DAG inputs are unchanged because every mathematical
input checked here was already a direct input of L221.

## Mathlib

Coverage of the full quantitative variable-coefficient pinned-trace
statement: **not checked**. Coverage of the cited transient-walk Green
asymptotic and killed-domain identity, discrete energy projections,
shell sums and l2 inequalities: **not checked**. No absence claim or
full matching formal theorem is asserted. The precise scalar inputs
and normalization are given above; qualitative local inputs retain
their existing qualifications.
