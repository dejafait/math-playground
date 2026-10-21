# L259 — Fifth-difference source comparison for the complete massless static rate

## Hypotheses

Use exactly L258(1)'s C_i,N, L257's U_i^triangle and L256's
U_i^0(F^0), with all their qualifications: the relative SU(2) box
(-4,4)^4, admitted even N, a=8/N, straight lower-rooted forest,
ordinary stored coordinates, bare-first order, both actual probes
i=3,6 and tau=1/16. Keep the full continuum heat matrices, both
generator orders, every source/end row, and the sole -6. Write
V_N={1,...,N-1}^3, Delta_N=6I-T_N and G_N=Delta_N^(-1).
Use L179(1)'s H_k, q_l and c_(i;kl)^cont without changing either
physical axial level. Both Q subtractions enter only through L175's
already imported comparison with V_i.

Import L180 proof section 1, (9), including its separate critical
audit in section 5: after summing all axial stencil offsets and
closing with both S endpoints, the frozen component-1 row depends
only on displacement component b_1. For mu=2,3,4 define its finite
scalar source stencil beta_mu by

    beta_mu(U)=sum_(r in Z, f a positive mu-link)
       Gamma(e_1)_((r,U,1),f) S_(f,(0,0)).                  (1)

Here e_1 in Gamma is the displacement basis vector; all stencils
are precisely L179(2). In the inherited raw Laurent convention its
symbol is

    b_mu(z)=(z_mu-z_mu^(-1))/8
                  [sum_(nu=2)^4 X_nu^2-lambda X_mu],
    X_nu=2-z_nu-z_nu^(-1), lambda=sum_(nu=2)^4 X_nu.     (2)

Thus this COMPLETE row has five differences. Formula (2) is an
imported exact finite-stencil identity, not an assertion about an
individual generator order. No new stencil script or reproof of
L180 is needed. A reversal of Fourier-transform convention reverses
all Laurent exponents consistently and changes none of the estimates
below; definitions (1) and (6) fix the actual signed coefficient.

The scalar inputs are Lawler--Limic, *Random Walk: A Modern
Introduction* (Cambridge, 2010), Theorem 4.3.1, printed pp. 81--84,
and Proposition 4.6.2(a), p. 97, in the inspected author-hosted text
<https://www.math.uchicago.edu/~lawler/srwbook.pdf>. Their hypotheses
are the symmetric irreducible finite-range transient nearest-neighbor
walk on Z^3. With Delta=6(I-P_walk), g=G_walk/6 satisfies

    0<=g(z)<=C/(1+|z|),
    G_N(Y,X)=g(Y-X)-E_Y[g(S_exit-X)].                       (3)

These are precisely the normalizations and primary statements
already imported and specialized in L221 proof sections 1--2. We
use only the bound and killed-domain identity, not a new asymptotic
reproof or any relative vector Green theorem. The other standard
input is Fourier Plancherel on Z^3, including weak torus derivatives
and lattice-coordinate moments.

## Conclusion

For both complete actual probes, with constants independent of N,

    |C_i,N-a^(-3)K_(i,Vmix)| <= C_i N^2,
    |U_i^0(F^0)-a^(-3)K_(i,Vmix)| <= C_i N^(5/2).          (4)

The coefficient is EXACTLY L179(7), identified below through the
already established qualitative limit. No zero-mass substitution in
L179(5) is assumed. Consequently the imported L256--L258 comparisons
also give

    |V_i-a^(-3)K_(i,Vmix)|
                      <=C_i N^(5/2)sqrt(log(eN)).           (5)

This establishes the approved component threshold, relative to the
imported premises; it is stronger than N^(5/2)log(eN)^2. The separate critical audit in proof section 6 accepts this
specialization relative to the stated imported premises. Pending
upstream qualifications remain. Classification is REPRODUCTION of standard
Fourier, Dirichlet energy and quadrature tools for this exact word;
no progress beyond the sources checked or originality is claimed.
Other component rates, quantitative L011 assembly, interacting
reflected control, continuum axioms and finite positive infrared mass
remain independent unresolved requirements. There is no solution
candidate.

## Proof

### 1. The source potential has enough weighted square summability

On Z^3 let w_mu=g*beta_mu. This is a finite linear combination of
translates of g, with Fourier multiplier b_mu/lambda. Fix a consistent
Fourier convention for (1)--(2). For 0<r=|theta|<=1 and every
multi-index alpha with |alpha|<=4, the product and quotient rules give

    |partial^alpha(b_mu/lambda)|<=C_alpha r^(3-|alpha|).

Indeed lambda is comparable to r^2; its reciprocal derivatives have
bounds C_alpha r^(-2-|alpha|), obtained inductively by differentiating
lambda lambda^(-1)=1. Each of the five difference factors in (2)
vanishes to at least first order, so derivatives of b_mu through order
four have bounds C_alpha r^(5-|alpha|). This remains true for its
finite sum of products. Away from zero the periodic multiplier is
smooth. The worst displayed square singularity is r^-2, integrable
in dimension three.

These classical derivatives off zero are the weak derivatives on
the whole torus. To check this rather than assume it, integrate by
parts outside a ball of radius epsilon at each derivative order.
At order m<=4 the boundary term from a derivative of order m-1
is bounded by C epsilon^2 epsilon^(4-m), which tends to zero.
The derivatives are locally integrable, so the removed ball contributes
nothing in the distribution limit. All derivatives through order four
are therefore in L2, with no point-supported distribution at zero.

Multiplying the symbol by any forward-difference factor or by the
J_j symbol gives the same bounds or better ones: these factors are
smooth, vanish at zero, and have bounded derivatives. Plancherel and
the coordinate/weak-derivative identity now give

    sum_z (1+|z|)^8 [ |w_mu(z)|^2
             +sum_nu |D_nu w_mu(z)|^2
             +sum_j |J_j w_mu(z)|^2 ] <= C.                 (6)

Here D_nu is a unit forward difference on the full grid. To pass
from coordinate monomials to the radial weight, expand
(1+sum z_nu^2)^4 and use the finitely many derivatives just proved.
The energy and all these moments are finite; no l2 property of the
undifferentiated monopole g is asserted. Also

    ||J_j w_mu||_1<=C,                                     (7)

by Cauchy--Schwarz against (1+|z|)^(-2), whose square is summable
on Z^3, using the weaker second spatial moment already in (6).
The identity Delta w_mu=beta_mu follows by Fourier multiplication.
All constants in (6)--(7) are fixed stencil constants.

### 2. Finite source comparison by a full Dirichlet energy projection

Let X have distance at least delta N from the complement of V_N,
where delta>0 is fixed. Translate beta_mu and w_mu to center X,
and put w_(N,X)=G_N beta_(mu,X), extended by zero outside V_N.
For sufficiently large N the entire fixed source stencil lies inside
V_N. Every finite Dirichlet edge, including edges to pinned vertices,
is retained in this definition.

For any v supported in V_N, finite summation by parts gives

    <D w_(N,X),D v>=<beta_(mu,X),v>=<D w_(mu,X),D v>.

All products are well-defined by (6). Hence w_(N,X) is the energy
orthogonal projection of w_(mu,X) onto the subspace of arrays
supported in V_N. This subspace is finite dimensional and the
Dirichlet energy is positive definite on it.

Choose a lattice cutoff chi equal to one on |z-X|<=cN, zero on
|z-X|>=2cN, with 2c<delta and |D chi|<=C/N. The test array
chi w_(mu,X) is supported in V_N. Orthogonal projection and the
exact discrete product rule imply

    ||D(w_(N,X)-w_(mu,X))||_2
      <=||D[(1-chi)w_(mu,X)]||_2 <= C_delta N^(-4).       (8)

For the last inequality the tail of Dw beyond cN is at most C N^-4
by (6); the cutoff-gradient term is at most (C/N) times the l2 tail
of w beyond cN-1, itself at most C N^-4. Bounded shifts of the
cutoff region change only constants. This proves (8) on the ENTIRE
infinite edge set after zero extension; it includes all boundary
edges and all exterior tail edges. No output/source row is restricted.
Since a centered difference is a sum of two adjacent forward
differences, (8) gives, in particular,

    ||J_j(w_(N,X)-w_(mu,X))||_(l2(V_N))<=C_delta N^(-4). (9)

The J_j in the finite trace is exactly the full centered difference
of the zero-extended finite array, restricted to V_N.

### 3. Ordered local contraction: boundary transfer and action freezing

For a bounded physical C1 function q on the closed transverse box,
write q_N(Y)=q(-4+aY) and q_X=q(-4+aX). Define

    T_(N;jmu)(q,X)
       =sum_(Y in V_N) G_N(X,Y) q_N(Y) (J_j w_(N,X))(Y),
    t_(jmu)=sum_(z in Z^3) g(-z)(J_j w_mu)(z).           (10)

The last sum is absolutely convergent by (3) and (7). Both expressions
are in the original G q J G beta order. We prove the uniform estimate

    |T_(N;jmu)(q,X)-q_X t_(jmu)|
                         <= C_delta ||q||_(C1)/N.        (11)

First replace J_j w_(N,X) by J_j w_(mu,X), leaving q in place.
L257(6) supplies ||G_N(X,.)||_2<=sqrt(3N) on the complete finite
space. Cauchy--Schwarz with (9) bounds this error by
C_delta ||q||_infinity N^(-7/2).

Next replace G_N(X,Y) by g(Y-X) only in that retained expression.
Symmetry and (3) give, for every Y in V_N,

    |G_N(X,Y)-g(Y-X)|<=C_delta/N,

because every possible exit vertex is at distance at least delta N
from X. Sum against |q_N(Y) J_j w_(mu,X)(Y)| and use (7): the
error is at most C_delta ||q||_infinity/N. This bound includes Y
adjacent to each face; compactness is required only of X.

Now freeze the deterministic action coefficient, rather than commute
it through an inverse. The line segment from -4+aX to -4+aY stays
in the closed cube, so

    |q_N(Y)-q_X|<=a ||q||_(C1)|Y-X|.

By (3), |Y-X|g(Y-X)<=C. The change in the sum is consequently
at most C a ||q||_(C1)||J_j w_mu||_1<=C ||q||_(C1)/N.
Finally extend the constant-coefficient sum from V_N to Z^3.
For all added rows |Y-X|>=delta N, so (3),(7) bound the added tail
by C_delta |q_X|/N. Adding these four explicit errors proves (11).
There is no coefficient/inverse commutation, boundary-source deletion,
or smoothness assumption on any rough Green column.

### 4. Apply the complete source contraction to exactly C_i,N

In L258(1) the cut is t>s, the weight is s and the deterministic
H_(k,mu)(x_a) is independent of the bounded stencil offsets e,f.
All nonzero u(x_a) have a fixed physical clearance from every face.
For such x=(s,X), all r,f in its local generator stencil are actual
variable links for large N. The sum over those r is therefore the
FULL axial offset sum in (1), including the two original generator
orders. Neither t nor q_l(t,Y) depends on r. L180's imported identity
(1)--(2) gives the EXACT finite-space reduction

    C_i,N=-6 a^3 sum_(k,l) c_(i;kl)^cont
      sum_(1<=s<t<N) s sum_(X in V_N) u_1(x_a)
        sum_(j,mu=2)^4 H_(k,mu)(x_a)
               T_(N;jmu)(q_(l,j)(-4+at,.),X).             (12)

The mu=1 contribution is zero since H_(k,1)=0. The transverse
displacement components vanish only in the complete summed source
identity; they were not removed from either individual generator
order. Formula (12) sums axial STENCIL offsets, not the two physical
levels s,t. Every original action row Y remains in T_N.

All mode C1 norms of q_l and H_k on the closed box/interior generator
region are bounded by fixed polynomials p(l),p(k); enlarge the p
in L258(4)--(6) if necessary. This follows by differentiating the
same finite sine/cosine products and the physical lower primitive
in L179(1). The allowed constant axial mode contributes its linear
primitive and has the same polynomial bounds. In particular q_l's
bound holds globally, without continuing a pinned forest potential.

Define F_i,N by replacing each T_N in (12) by
q_(l,j)(-4+at,-4+aX) t_(jmu). For every nonzero u row, apply (11)
with the same clearance delta. The exact axial count L258(8) and
the full transverse count give

    |C_i,N-F_i,N|
      <=C a^3 N^3 N^3 N^(-1)
           sum_(k,l)|c_(i;kl)^cont|p(k)p(l)
      <=C_i N^2.                                         (13)

The complete Gaussian majorant in L258(6) makes this sum finite.
No exterior cutoff, omitted heat label, component index or constant
axial mode has been discarded. Absolute convergence needed to
regroup (12) follows already from L258; estimates (7),(11) also give
it directly for its contracted expression.

### 5. Quantitative quadrature and identification of the same coefficient

Let K_i^* be the following absolutely convergent physical integral:

    K_i^*=-6 sum_(k,l)c_(i;kl)^cont
      integral_(y in (-4,4)^3) integral_(xi=-4)^4 integral_(eta=xi)^4
        (xi+4) u_1(xi,y)
          sum_(j,mu=2)^4 H_(k,mu)(xi,y) q_(l,j)(eta,y)
                                    t_(jmu) d eta d xi d y. (14)

For each fixed pair, the integrand before the triangular indicator
has C1 norm at most C p(k)p(l). The finite t_(jmu) are constants.
Exactly a^3 F_i,N is the five-dimensional mesh sum with cell weight
a^5 and xi+4=as: a^3 times the a^3 s in (12) is a^5(as).
Thus both physical axial levels and the physical lower-distance
weight agree with (14).

Cover the five-dimensional rectangular box by mesh cubes. Cubes
meeting eta=xi have total volume O(a), and the difference between
the strict s<t grid region and the continuous triangular region
is confined to this strip and outer face strips of total volume
O(a). Bound their contribution by the supremum norm. On all other
cubes the mean-value estimate bounds integral-minus-sample by C a
times the C1 norm times the cell volume. The whole domain has fixed
volume. This proves a pairwise quadrature error C a p(k)p(l),
including the retained axial endpoints. Sum with the full heat
majorant to obtain

    |a^3 F_i,N-K_i^*|<=C_i/N,
    |C_i,N-a^(-3)K_i^*|<=C_i N^2.                       (15)

The second statement follows from (13), a^(-3)=N^3/512 and the
first. In particular a^3 C_i,N tends to K_i^*. Independently,
L258(3), through the controlled L257/L256 comparison and L179(7),
already proves that its limit is K_(i,Vmix). Uniqueness of limits
therefore identifies

    K_i^*=K_(i,Vmix).                                    (16)

This does not insert zero mass into L179(5), invoke a qualitative
limit at a varying mass, or require evaluating a new torus integral.
The new absolute source comparison establishes (14)--(15) first;
the independent existing limit supplies only its exact name.

Equations (15)--(16) prove the first line of (4). Add L258(2)'s
complete O(N^(5/2)) static matching error ONCE to obtain the second
line of (4). Alternatively add L258(3)'s already combined comparison
with V_i once to obtain (5); its two Q subtractions are not added
again. All imported audit qualifications remain in these conclusions.

The meaningful mathematical checks are the imported full row (2),
its fourth weak-derivative integrability in three dimensions, the
full-edge energy projection (8), all four ordered errors in (11),
the exact axial source sum (12), the N^6 weighted count (13), and
the five-dimensional normalization and unique-limit identification
(15)--(16). They are analytic. No finite numerical preview, new
mathematical script or upstream audit is substituted for them.

### 6. Separate critical audit of the static rate

The 2026-10-21 proof audit accepts (4)--(5) relative to the stated
imported premises. No mathematical correction, bound change, new
mathematical input or numerical check is needed. In particular this
is not an independent acceptance of the pending L257/L258 estimates,
L176's earlier replacement, or the upstream construction assumptions.
The following checks cover every new analytic step of this proof.

**Exact source and order.** L180(9) and its separate section-5 audit
identify the complete integer-tail row obtained by summing the axial
stencil offsets and both S endpoints. They apply to precisely
L179(2)'s Gamma, used in L258(1). For each closing vertex, H is
already independent of e,f and the cut t>s is independent of r.
Thus that sum can be taken before any inverse estimate. Compact
support of u puts every participating e,f in the actual variable-link
set; it places no restriction on Y. The row is linear in b, and its
transverse displacement rows are zero, giving exactly u_1 beta_mu.
H_1=0 removes the remaining column. This verifies (12), with the
original G q J G order, both physical levels and the sole -6 intact.
The Laurent sign convention causes no identification ambiguity:
(1) defines the actual source, and both the finite contraction and
its independently identified limit use that same definition.

**Moments at zero frequency.** Each term of (2) contains one first
difference and two second differences. Its derivatives through order
four have the displayed r^(5-m) bound. Dividing by lambda gives
r^(3-m). The radial L2 integral for order m is bounded by a constant
times integral_0^1 r^(8-2m) dr, finite also at m=4. In the weak
integration-by-parts check, the removed-sphere term at order m is
O(epsilon^(6-m)), tending to zero for all m<=4. No delta term at
the origin is hidden. The finite smooth symbols D_nu and J_j
preserve these bounds. Plancherel consequently supplies all coordinate
moments needed for (6). For (7), use the weighted l2 norm with weight
(1+|z|)^4 and the summable reciprocal square (1+|z|)^(-4).
This is a property of the collected source potential w_mu, never of
the monopole g.

**Full finite energy.** Zero extension from V_N makes its quadratic
Dirichlet form exactly the sum over all infinite-grid positive
nearest-neighbor edges, including every edge to a pinned vertex.
Delta w_mu=beta_mu and finite summation by parts therefore give
the stated orthogonal projection. The cutoff is a valid finite-space
test because the entire source and its buffer lie in V_N. From (6),
the squared tail of Dw beyond cN is O(N^-8), and the cutoff-gradient
term is bounded by C N^-2 times the squared tail of w, hence
O(N^-10). Projection optimality proves (8). The exact finite J_j
is the centered difference of this same zero extension, so (9)
follows without a dropped face row or an inverse Poincare loss.

**All four ordered errors.** The first source-potential replacement
costs O(sqrt(N) N^-4)=O(N^(-7/2)) by the full finite Green row
norm. For the second replacement use symmetry to write the killed
Green identity with the walk starting at Y and the fixed target X.
Every exit position is at distance at least delta N from X; (3)
therefore bounds the correction uniformly in every Y by C_delta/N.
Its pairing with J_j w is bounded by (7). The third replacement
uses only the deterministic Lipschitz estimate and
|z|g(z)<=C, again paired with (7). The fourth error is the omitted
exterior sum, whose g factor is O(1/N) since X has clearance.
These prove exactly (11), uniformly for all globally C1 action
modes, with q retained at its original axial level throughout.

**Full count, heat sum and coefficient.** For every s the closing
transverse count is at most N^3, and
sum_(1<=s<t<N) s=N(N-1)(N-2)/6. Multiplying the local O(N^-1)
error by a^3 N^6 gives O(N^2), as in (13). The finitely many extra
physical derivatives used here only enlarge the polynomial mode
majorant; L258(6)'s complete Gaussian series remains summable. This
includes both probe matrices, the constant axial mode and omitted
mesh labels. Finally a^3 times the trace prefactor a^3 s is
exactly a^5(as). The triangular and face strips have total physical
volume O(a), and the C1 rectangle error is O(a); the same full heat
majorant sums both. Equations (15) follow with no missing power of
a or axial sum. L258's independently established qualitative limit
then identifies K_i^* with exactly L179(7). This use of uniqueness
of limits cannot erase its generally nonzero coefficient. Adding
L258(2) or its already combined (3) once yields respectively (4)
or (5), with both Q subtractions already accounted for by L175.

The accepted static O(N^(5/2)) rate is within the approved
O(N^(5/2)log(eN)^2) threshold. Its smooth-action consequence retains
the imported sqrt(log(eN)) factor. No other component rate,
quantitative L011 assembly, interacting reflected control, continuum
axiom or finite positive infrared mass is established by this audit.
Mathlib coverage and the original source assessment are unchanged.

## Mathlib

Full matching theorem: **not checked**. Supporting Fourier Plancherel
with weak derivatives, discrete energy projection, Cauchy--Schwarz,
finite-dimensional Dirichlet inversion and C1 quadrature: **not
checked**. Unknown coverage is not evidence of absence. Reuse the
unchanged [assessment](../drafts/literature/2026-10-20-smooth-action-ordered-static-rate.md).
The scalar Green theorems are imported by precise citation and their
normalization is justified above. The new specialization is needed
because their statements alone do not contract this ordered product,
retain its two physical levels, or provide its quantitative heat-summed
trace rate. L180's known algebra is imported without reproof. The
separate proof-section-6 audit accepts the finite-source/moment comparison
relative to the named imported premises; no upstream proof acceptance
or full Yang--Mills conclusion is inferred.
