# L258 — Complete deterministic coefficient matching in the massless static trace

## Hypotheses

Use L257's exact U_i^triangle and L256's U_i^0(F^0), for the
relative SU(2) box (-4,4)^4, admitted even N, a=8/N, the straight
lower-rooted direction-1 forest, stored coordinates, bare-first order
and both actual probes i=3,6 at tau=1/16. All imported qualifications
remain. Write G=Delta_T^(-1) on V_T={1,...,N-1}^3 and keep L175's
J_j and endpoint sum S. No covariance is changed in this result.

Use exactly L179(1)'s H_k, q_l=d^*d A_l and continuum heat
coefficients c_(i;kl)^cont, and L179(2)'s unit-grid Gamma(b), including
both generator orders and all endpoint/clover filters. For a closing
vertex x=(s,X) put x_a=(-4+as,-4+aX), and put
y_(t,Y)=(-4+at,-4+aY). The action remains at y_(t,Y).

Define a finite-space, continuum-coefficient comparison by

    C_i,N=-6 a^3 sum_(k,l in the full continuum spectrum) c_(i;kl)^cont
      sum_(j=2)^4 sum_(1<=s<t<N) sum_(X,Y in V_T)
      sum_(e=(r,U,1), f a variable positive link)
        s G_(XY) q_(l,j)(y_(t,Y)) (J_j G)_(YU)
          Gamma(u(x_a))_(e-x,f-x) H_(k,mu(f))(x_a) S_(f,x).       (1)

The component-1 link e includes both axial end levels, with U in V_T.
The relative endpoint convention for S is unchanged. Only boundedly
many e,f contribute for each x, because S is incident to x and Gamma
has fixed finite range. All nonzero frozen generator rows lie in a
fixed compact interior set for sufficiently large N. Thus the local
unit-grid entries in (1) refer to actual variable links. The definition
neither restricts Y nor replaces a finite Green column by a bulk one.
H_k is sampled only at interior generator points, never at the pinned
upper forest value. Its component 1 is zero as in L179(1).

## Conclusion

The full heat sum in (1) is absolutely convergent for each admitted
sufficiently large N, and

    |U_i^triangle-C_i,N| <= C_i N^(5/2),
    |U_i^0(F^0)-C_i,N| <= C_i N^(5/2), i=3,6.                    (2)

The first comparison accounts jointly for the raw exterior samples,
the complete local generator, the action-mode extension at its original
level and spatial point, both heat coefficient matrices, and all omitted
continuum labels. Every retained-pair error has a polynomially weighted
Gaussian envelope. The second comparison uses L257 once.

Relative to L257(4),

    |V_i-C_i,N| <= C_i N^(5/2)sqrt(log(eN)),
    lim_(N->infinity) a^3 C_i,N = K_(i,Vmix),                    (3)

where the coefficient is exactly L179(7). There is no estimate here
for |C_i,N-a^(-3)K_(i,Vmix)|. In particular (1) still contains two
finite massless inverses and the nonconstant action multiplier between
them. Boundary transfer, transverse coefficient freezing and the final
quantitative spatial/axial quadrature remain unproved.

This is REPRODUCTION: a local specialization of already recorded raw
mode, heat and finite-matrix estimates, not progress beyond the sources
checked. Its separate critical audit in proof section 5 accepts the comparison
relative to its stated imports. It is not
a complete smooth-action or L011 remainder, an interacting bound, or
a Yang--Mills construction.

## Proof

### 1. Uniform normalized coefficient estimates

Let k,l be retained finite-mesh labels and let p(k)=(1+|k|)^6,
enlarging constants below if necessary. On the fixed compact interior
enlargement supporting the actual or frozen generator, set

    b_(k,f)=h_(k,f)/a,     g_(ef)=a (A^gen)_(ef),
    d_(j,l)(t,Y)=m_(j,l)(t,Y)/a^3.

For all local closing entries allowed by either stencil,

    |b_(k,f)|+|H_(k,mu(f))(x_a)| <= C p(k),
    |b_(k,f)-H_(k,mu(f))(x_a)| <= C a p(k),
    |g_(ef)|+|Gamma(u(x_a))_(e-x,f-x)| <= C,
    |g_(ef)-Gamma(u(x_a))_(e-x,f-x)| <= C a.                   (4)

The raw exterior bounds are precisely L248 proof section 1,
(3)--(8): its normalized unaveraged transverse link is
A_(k,a,mu) minus the transverse forward difference of the actual
lower midpoint prefix, divided by a. Its continuum value is exactly
H_(k,mu) in L179(1). That proof gives O(a(1+|k|)^2) error at the
link's initial vertex, and O(1+|k|) physical first derivatives of H.
Moving to x_a costs the same type of bound, since f is incident to x.
For mu=1, both values are exactly zero on these interior forest links.
The constant axial cosine mode is retained in the prefix formula.
Nothing is asserted about the separately pinned upper forest jump.

The last two lines of (4) are L178(4) and L179(10). Their applicability
is entrywise: a A^gen is the sum of the two actual finite stencil
products with coefficient u_a at intermediate vertices. Every such
vertex is within O(a) of x_a, u_a-u=O(a^2), and u is Lipschitz.
Replacing those finitely many coefficients by u(x_a) has O(a) error
in each entry, including the adjoint coefficient differences. This
is not a commutation through G. Use the union of the actual and frozen
stencil supports, with zero entries supplied where one stencil vanishes.
That union has bounded incidence and lies in a common compact interior
enlargement; (4) holds also in its support fringe.

At *every* action level and transverse vertex, including the rows
adjacent to each face, one also has

    ||d_(j,l)(t,.)||_infinity
       +||q_(l,j)(y_(t,.))||_infinity <= C p(l),
    ||d_(j,l)(t,.)-q_(l,j)(y_(t,.))||_infinity <= C a p(l).   (5)

Here the definition matters: L175 defines m by evaluating the smooth
componentwise extension of L h_l=L v_l at vertices. L156(10) and
L179 proof section 1 identify its normalized extension as
d_a^*d_a A_(l,a), on the relative sine/cosine modes. The supporting
mode normalization estimate L248(3), for m=0,1,2, is

    ||A_(l,a)-A_l||_(C^m) <= C_m a^2(1+|l|)^(m+1),
    ||A_(l,a)||_(C^m)+||A_l||_(C^m) <= C_m(1+|l|)^(m-1).

Each incidence derivative replaces a sine/cosine factor by its paired
factor with coefficient omega_(nu,a)=2 sin(pi l_nu/(2N))/a.
With omega_nu=pi l_nu/8, Taylor's inequality |sin z-z|<=|z|^3/6
gives |omega_(nu,a)-omega_nu|<=C a^2 |l_nu|^3 and
|omega_(nu,a)|<=C |l_nu|. Each second-order coefficient of the
action is a sum of a fixed number of products of two such factors.
Replacing those factors and the normalization therefore costs at
most C a^2(1+|l|)^3 at identical componentwise trigonometric arguments.
If the indexing convention introduces any bounded midpoint/vertex
shift, its contribution is at most C a(1+|l|)^2, by one more physical
derivative of the second-order product mode. These bounds imply (5)
with the displayed p and a<=1. All zero derivative factors are retained.

These identities hold for the global action extension, not for a
continued forest potential. In particular normal end-edge derivatives
are the same relative-mode derivatives used in L156(10). No action
collar, action face or Green source is removed to obtain (5).

Finally L248(11), proof section 2, applies to exactly the same actual
probe matrices and gives, for some c0>0 independent of N,

    |c_(i;kl,a)|+|c_(i;kl)^cont| <= C_i exp[-c0(|k|^2+|l|^2)],
    |c_(i;kl,a)-c_(i;kl)^cont|
       <= C_i a(1+|k|+|l|)^4 exp[-c0(|k|^2+|l|^2)].           (6)

This imports only that coefficient estimate, not L248's different
reverse-trace conclusion. Its proof compares the four terms of the
triplet average with factor 1/4 and both polarized clover terms with
factor 1/2, including the full strains and transition regions. The
heat and stored-coordinate normalizations agree with L156(8) and
L179(1); hence no additional factor or probe sector is introduced.

### 2. The complete ordered finite-space envelope

L257(6)--(8) proves for arbitrary real vertex multipliers v, uniformly
in X,U and including every source and end row,

    |sum_Y G_(XY) v(Y) (J_j G)_(YU)|
                                    <= sqrt(72N) ||v||_infinity. (7)

In particular J_j is summed into its right Green column before taking
absolute values. The multiplier remains on its original left side.
Apply (7) to v=d_(j,l)(t,.), to v=q_(l,j)(y_(t,.)), and to their
difference. Equations (5) bound these respectively by
C sqrt(N)p(l), C sqrt(N)p(l), and C a sqrt(N)p(l).

For a fixed closing vertex x the union of allowed e,f in (4) has
bounded cardinality. S_(f,x) is bounded. There are at most N^3
choices of X, and the exact remaining axial weight satisfies

    sum_(1<=s<t<N) s
       = sum_(s=1)^(N-2) s(N-1-s)
       = N(N-1)(N-2)/6 <= N^3/6.                           (8)

Both raw and sampled pair traces, before their heat coefficient and
the common -6, consequently have absolute bounds

    C a^3 N^3 N^3 sqrt(N) p(k)p(l)
                              <= C N^(7/2) p(k)p(l).       (9)

This is only an envelope for estimating changes, not the asserted
growth of either signed trace. In deriving it no Y row was restricted,
and no level t was identified with s. All boundary information in G
is retained exactly. The a^3 follows from the original product
m A^gen h=(a^3 d)(a^-1 g)(a b).

### 3. Telescope the coefficients and sum every heat label

For a retained pair telescope the normalized integrand in the order

    d g b - q Gamma H
       =(d-q)g b + q(g-Gamma)b + q Gamma(b-H).              (10)

This is a telescoping of scalar entries after the original ordered
matrix product has been expanded, not a matrix commutation. In the
first term use (7) with d-q. In the other two use (7) with q and
the corresponding O(a) factor in (4). The finite local count and
(8) then give the pairwise comparison

    |T_(jkl,a)^raw-T_(jkl,a)^sampled|
       <= C a^4 N^(13/2) p(k)p(l)
       <= C N^(5/2) p(k)p(l).                            (11)

Here each T contains the factor a^3 but neither c nor -6; raw T is
the relevant part of L257(2), and sampled T is the corresponding
part of (1). The exponents in (11) use a=8/N and include all N^5
closing/action points and the extra weight s, before the sqrt(N)
Green estimate. Thus there is no omitted axial sum.

Multiply (11) by the first bound in (6). For the heat-coefficient
change itself, multiply (9) for the sampled trace by the second
bound in (6); its extra factor a again yields N^(5/2). Summing
over the finite relative spectrum is bounded by the full continuum
sum of a fixed polynomial in k,l times exp[-c0(|k|^2+|l|^2)].
That sum is finite: expand or dominate the polynomial by finitely
many coordinate powers and factor into one-dimensional Gaussian
series. There are only four component choices per mode. The allowed
zero own-direction indices remain, and the physical gap prevents a
zero total mode. This proves the claimed retained-pair error for
both complete probes without a finite exterior cutoff.

For omitted continuum pairs, at least one index lies beyond the
corresponding finite relative spectrum, so |k|+|l|>=N. The continuum
value bounds in (4)--(5), with no finite-mesh normalization, hold
for these labels as well. Apply (9) and the continuum heat bound to
obtain

    sum_(omitted pairs) |c_(i;kl)^cont T_(jkl,a)^sampled|
      <= (C_i N^(7/2)/N) sum_(all pairs)
          (|k|+|l|) p(k)p(l) exp[-c0(|k|^2+|l|^2)]
      <= C_i N^(5/2).                                    (12)

The same full Gaussian sum without the indicator proves absolute
convergence of (1). Restore the three transverse j values and the
sole -6 once. Equations (11)--(12) prove the first inequality of (2).
The second follows by adding L257(3)'s moving-cut error once.

### 4. Identification without a zero-mass density substitution

L257(4) gives |V_i-U_i^triangle|<=C_i N^(5/2)sqrt(log(eN))
and lim a^3 U_i^triangle=K_(i,Vmix). Add (2) to prove the first
line of (3). Since a^3 N^(5/2)=512 N^(-1/2) tends to zero,
the second line follows from the same imported limit. This identifies
the coefficient through L179(7); it does not set epsilon=0 in
L179(5), assume a bounded bulk inverse, or vary a mass in a qualitative
convergence theorem. Both Q subtractions enter once through L175
inside L257's imported comparison with V_i.

The deterministic comparison has removed the raw/continuum and heat
matching obligation at the required scale. The remaining expression
(1) still has q_(l,j)(y_(t,Y)) between G and J_j G. Replacing Y by
X or either G by a bulk kernel is a different, unproved step. Even
with smooth sampled coefficients, (9)'s O(N^(7/2)) absolute envelope
does not by itself give the required subcubic remainder. The exact
triangular weight, distinct physical levels and both frozen generator
orders are retained for that continuation.

The mathematical checks in this step are the exact coefficient
identifications (4)--(6), full-source bound (7), full axial count (8),
ordered telescoping (10) and omitted-label bound (12). They are
analytic; no numerical experiment or mathematical script is needed.
L178/L179 supplied only a fixed-mass limit, and L248's response rate
is for a different word, so neither already proves (2). Their
supporting coefficient estimates suffice for this specialization.

### 5. Separate critical audit, 2026-10-21

The audit accepts (2)--(3) relative to the stated imports, without a
correction. Its scope is the deterministic matching in this exact
ordered word, including the global action extension, both complete
heat matrices and omitted labels. L248's separately audited raw/heat
estimates are reused; its reverse-trace conclusion is not transferred.
L179's coefficient-limit theorem and the preceding V_i reductions
remain imports rather than conclusions of this audit.

**Raw exterior and generator.** L156(8)'s stored square-root covariance
column is a A_(k,a), so h/a is precisely the unaveraged retraction
in L248(6). Its prefix contains a times the sum of midpoint values;
its transverse quotient is divided by a. The minus sign therefore
matches L179(1)'s H, with no extra mesh factor. L248(8) gives
O(a(1+|k|)^2) error and independent uniform values. Its physical
first-derivative bound controls the shift from the incident f to x.
The interior component-1 forest value and H_1 are both zero. The
constant axial cosine mode has its actual linear lower prefix, while
compact generator support excludes the separately pinned upper jump.

L178(4) and L179(10) compare the full two generator products entrywise.
The coefficient at every intermediate stencil vertex is within O(a)
of u(x_a), including the reversed order. The union of both stencil
supports has uniformly bounded incidence and a common compact interior
enlargement. An entry absent from one stencil is set to zero before
comparison, so the support fringe also satisfies (4). There is no
implicit deletion of a generator boundary row or additional color factor.

**Global action extension.** This check is distinct from the compact
exterior comparison. L175 defines m by the componentwise relative-mode
extension of Lh_l=Lv_l, not by extending h_l. L156(10), L159(6)
and L179 proof section 1 give this extension as
m/a^3=d_a^*d_a A_(l,a), evaluated at vertices. It is defined on
the whole box and uses the same sine/cosine derivative identities at
normal end edges. Each first derivative has multiplier omega_(nu,a),
including zero for a constant cosine factor. For r=1+|l|,
|omega_(nu,a)-omega_nu|<=C a^2 r^3 and |omega_(nu,a)|<=C r.
A difference of two derivative products is therefore O(a^2 r^4);
multiplication by the mode amplitude O(r^(-1)) gives O(a^2 r^3).
The normalization difference O(a^2 r), multiplied by two derivative
factors O(r^2), has the same bound. A bounded component-grid shift
costs O(a r^2), since a third physical derivative of the normalized
mode is O(r^2). These bounds imply (5) with p=r^6, for every retained
label, not just fixed labels. They hold uniformly up to every source
face. No smallness of ar at large labels is needed: the polynomial
error is summed against heat only later. Fixed tangential boundary
values and normal end-edge derivatives retain their relative conventions.

**Ordered envelope and telescoping.** The audit of L257 confirms (7)
for arbitrary real multipliers and every X,U. Its use on d-q is
legitimate because neither g,b nor their sampled counterparts depend
on Y. For each closing X there are only boundedly many local e,f.
The remaining axial sum is exactly
sum_(s=1)^(N-2) s(N-1-s)=N(N-1)(N-2)/6.
Consequently a^3 N^3 N^3 sqrt(N)=O(N^(7/2)) bounds either
pair trace. In (10) the first difference is inside the ordered
Green pairing; the other two are outside its Y sum. Each supplies
one factor a while all unchanged normalized factors remain bounded
by fixed mode polynomials. Thus the error is
a^4 N^(13/2)=O(N^(5/2)), with no uncounted axial or source sum.
This is an absolute error envelope, not a growth lower bound.

**Both probes and the full spectrum.** The matrices in L156(8),
L179(1) and L248(11) have the same physical relative modes,
square-root covariance factors and tau. L248's coefficient audit
retains the four triplet products with factor 1/4 and both polarized
shear products with factor 1/2. Thus (6) changes neither probe.
Multiplying its O(a) discrepancy by the O(N^(7/2)) envelope gives
the same N^(5/2) error. All additional mode powers have convergent
Gaussian sums. The finite label ranges are the componentwise subsets
of the continuum relative spectrum, with allowed own-direction zero
indices retained. An omitted pair has |k|+|l|>=N, so its indicator
is at most (|k|+|l|)/N. Using this inequality before summation gives
exactly (12), and the unweighted Gaussian sum proves absolute
convergence of (1). No finite heat cutoff or numerical premise enters.

Restore the sole -6 and add L257(3) once to obtain both statements
of (2). For (3), the preceding V_i comparison already includes both
Q subtractions. The cubic-normalized matching error tends to zero,
so L257(4), conditional on L179(7), fixes exactly K_(i,Vmix).
The action stays at (t,Y), and the generator and exterior stay at
(s,X); this proof does not freeze those levels or the Green kernels.
Together with L259's separately audited sampled comparison, these
accepted estimates validate the stated static N^(5/2) rate relative
to the imported coefficient theorem. They provide no independent
audit of that theorem, full L011 rate or interacting construction.

## Mathlib

Full matching theorem: **not checked**. Supporting finite sums,
Cauchy--Schwarz, sine remainder and Gaussian-series summability:
**not checked**. Unknown availability is not evidence of absence.
Reuse the unchanged [source assessment](../drafts/literature/2026-10-20-smooth-action-ordered-static-rate.md).
No new external theorem is imported or reproved. The specialization
above is needed to quantify deterministic replacement in this exact
massless ordered word, where the full finite Green envelope costs
sqrt(N). All imported audit qualifications remain; the separate critical review
in proof section 5 accepts this specialization without changing its inputs.
