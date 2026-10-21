# L253 — Joint-kernel freezing and the gradient-base remainder

## Hypotheses

Use L252(1)--(2)'s explicitly defined whole-grid trace S^b_(i,N,epsilon),
with its clamped extensions of h_k and v_l, compact zero extension of
u_1, and unchanged raw paths and endpoint filters. Use L250's smooth
coefficient and complete continuum heat bounds and exactly L104(6)'s
K_(i,G). The original quantity is L103's complete gradient-base pair
R_gx, under the same SU(2) relative all-face cube, lower-rooted
direction-1 forest, admitted even N, a=8/N, tau=1/16, stored coordinates,
bare-first order and actual probes i=3,6. There is no outside factor 3.

All relative source/end rows, allowed constant component indices,
upper cumulative tail and heat labels remain in the imported
comparisons. L251's inverse-removal bound and L252's boundary transfer
are imported with their stated qualifications. Their separate audits
and this lemma's audit are recorded in their respective Proof sections;
these do not recursively certify upstream inputs.

## Conclusion

Uniformly for 0<epsilon<=1 and sufficiently large admitted N,

    |S^b_(i,N,epsilon)-a^(-3)K_(i,G)|
                             <=C_i [N^2+N^3 epsilon].             (1)

In particular, at epsilon=N^(-2/3), L252(5) gives

    |R_gx(i,N)-a^(-3)K_(i,G)|<=C_i N^(5/2),                       (2)

which is within the requested O(N^(5/2)log(eN)^2) component budget.
The separate critical audit in proof section 6 accepts the bulk
comparison and assembly (2), relative to the qualified imported inputs.

This is a component remainder, not a complete quantitative L011
assembly, a logarithmic coefficient, an interacting error <=c_box/2,
a continuum construction or a finite positive infrared mass.
There is no complete-solution candidate and no claim of discovery
beyond the sources checked.

## Proof

### 1. Uniform coefficient bounds and scalar conventions

Fix a level t and exterior labels k,l. All indices below are whole-grid
tail indices n in Z^3; the physical transverse point is y_n=-4+a n.
Identify each component edge/plaquette array with a copy of l2(Z^3)
using its original tail. Write

    R=(Delta+epsilon)^(-1),
    T_j=I-S_j,  Delta=sum_j T_j* T_j,

where S_j has symbol exp(i theta_j). Here T_j is a component of
L252's incidence, and j ranges over {2,3,4}. Denote the distinct
centered difference in W by s_mu; its symbol is i sin(theta_mu).
Thus the exact whole-grid operator is

    W_mu=-C_mu* M_u s_mu,   W_mu*=-s_mu* M_u C_mu.                (3)

The C_mu are the actual endpoint-average filters. No filter has
been replaced by an unfiltered difference.

The component h_j(n) means
h_(k,j)(-4+at,pi(y_n+a e_j/2)). The coefficients in zeta are
f(n)=v_(l,mu)(-4+at,pi(y_n))+v_(l,nu)(-4+at,pi(y_n)),
or its other signed combination -(v_(l,nu)-v_(l,mu)).
Consequently, for a fixed polynomial p independent of N,t,epsilon,

    ||h_j||_infinity<=C p(k),
    |h_j(n-r)-h_j(n)|<=C a p(k)|r|,
    ||f||_infinity<=C p(l),
    |f(n+r)-f(n)|<=C a p(l)|r|.                                (4)

Indeed L250/L249's supporting mode bounds give polynomial C^1
bounds for the full upper primitive h and the lower-prefix v on the
closed physical cube. The coordinate clamp pi is 1-Lipschitz, so
composition preserves these bounds globally as Lipschitz estimates.
No smooth derivative of pi is needed. In particular h need not be
compact. The displacement u(n)=u_1(-4+at,y_n) is uniformly bounded
and has at most C N^3 nonzero entries, all with fixed physical
clearance from the transverse faces. If its axial slice is empty,
every term below is zero.

The complete continuum heat matrix satisfies

    sum_(k,l)|c_(i;kl)|p(k)p(l)<infinity                           (5)

after any fixed enlargement of p. This retains both probe
polarizations and every allowed constant index. We prove all
pairwise bounds with this polynomial envelope before summation.

### 2. The joint kernel estimates needed here

We use the named Plancherel theorem for the Fourier transform on Z^3,
including multiplication by the lattice coordinate versus weak
differentiation on the torus, and the Cauchy--Schwarz inequality.
The following checks specialize them to the actual finite stencils.

Let b(theta) be the symbol of a fixed product of q first-difference
stencils and bounded finite-shift filters, with q in {1,2,3}. Each
first-difference stencil used below vanishes at zero, has absolute
value <=C sqrt(lambda), and has bounded first derivatives, where

    lambda(theta)=sum_j |1-exp(i theta_j)|^2.

A raw path row times T also has these properties: its row has bounded
finite-shift symbol and T has symbol tau with |tau|=sqrt(lambda).
The same applies to C_mu D_(p,mu)* and to s_mu or T_j*. The product
rule gives

    |b|<=C lambda^(q/2),
    |partial_theta b|<=C lambda^((q-1)/2),
    |partial_theta lambda|<=C sqrt(lambda).                     (6)

Finite shifts do not change these bounds except for a constant.
The kernels K with symbol b/(lambda+epsilon) therefore satisfy

    ||K||_l2 <= C                    for q>=1,
    || |n| K(n)||_l2 <= C            for q>=2,                   (7)

uniformly in 0<epsilon<=1. To verify both claims on the entire torus,
away from lambda=0 all expressions are bounded. Near zero,
lambda is comparable to |theta|^2 and

    |b/(lambda+epsilon)|^2<=C lambda^(q-2).

For q=1 the worst singularity is lambda^-1, integrable in three
dimensions; q=2,3 are better. Differentiating the quotient in (6)
gives, for lambda>0,

    |partial_theta[b/(lambda+epsilon)]|
      <=C {lambda^((q-1)/2)/(lambda+epsilon)
                 +lambda^((q+1)/2)/(lambda+epsilon)^2}
      <=C lambda^((q-3)/2).

For q=2 its square again has only lambda^-1 singularity; for q=3
it is bounded. Plancherel proves (7). Each fixed positive mass has
a smooth periodic multiplier, so there is no weak-derivative domain
issue; the displayed integrable bounds make the estimates uniform.

It follows in particular that kernels A,B with difference counts
(3,1) or (2,2) obey

    sum_r |r| |A(r)B(-r)|<=C,
    sum_r |A(r)B(-r)|<=C.                                      (8)

Put the spatial weight on A in Cauchy--Schwarz. For counts (2,1)
or (1,2) the second, unweighted bound still holds. These are joint
absolute product bounds. They assert no separate first absolute
moment of a projected alternating kernel, and do not use the
stopped premise in ATTEMPTS/032.

### 3. Exact ordered reduction with the local commutator retained

Expand zeta over its three plane rows and its two raw path rows:
each summand is M_f B_path, where f has the signs specified in
section 1. For a plane p and an output component mu set

    J=C_mu D_(p,mu)*,  P=B_path T.

Both J and P are fixed scalar convolution stencils of first-difference
order in (6); a zero stencil contributes nothing. They retain the
original raw b,q paths, not endpoint-averaged exterior paths.
On the whole grid E_j selects the tail value, so the exact X is

    X=sum_j (T_j* M_hj-M_hj T_j).                               (9)

By cyclicity at the compact factor M_u, a summand of the original
trace R X R W* D* zeta T is exactly

    -Tr[M_u J M_f P R T_j* M_hj R s_mu*]
    +Tr[M_u J M_f P R M_hj T_j R s_mu*].                        (10)

All operators are bounded at positive mass and M_u is finite rank.
Thus this rectangular-to-scalar expansion and cyclicity are valid
on the infinite grid. No coefficient has crossed an inverse.

Use the exact local identity

    J M_f=M_f J+[J,M_f].

Writing J=sum_r j_r S_r, over a fixed finite set of shifts, gives

    [J,M_f]=sum_r j_r M_(f(n+r)-f(n)) S_r.                      (11)

The commutator is not discarded. In its first word in (10), the two
convolution factors on either side of M_hj are

    A=S_r P T_j* R,   B=R s_mu*,

of difference orders (2,1). In its second word they are

    A=S_r P R,        B=T_j R s_mu*,

of orders (1,2). The multiplier at the start is
u(n)[f(n+r)-f(n)], with absolute value <=C a p(l), supported on at
most C N^3 vertices. By (4), the unweighted part of (8), and direct
expansion of the diagonal of M_g A M_hj B, each commutator trace is
bounded by

    C a N^3 p(k)p(l).                                         (12)

The finite number of shifts and components is absorbed in C.
This estimate keeps every convolution input and output.

For the principal words, combine only the adjacent multipliers
M_u M_f=M_(uf), and commute only constant-coefficient convolutions
with each other. Their exact forms are

    -Tr[M_(uf) A_1 M_hj B_1],
      A_1=J P T_j* R,  B_1=R s_mu*,                            (13)
    +Tr[M_(uf) A_2 M_hj B_2],
      A_2=J P R,       B_2=T_j R s_mu*.                        (14)

The two counts are (3,1) and (2,2), precisely those in (8).
No multiplication operator is commuted through a Green inverse,
and no projection or cumulative prefix is deleted.

### 4. Freeze only within the closed two-kernel diagonal

For either word in (13)--(14), with g=uf, the diagonal formula is

    Tr[M_g A M_hj B]
       =sum_n g(n) sum_r A(r) h_j(n-r) B(-r).                   (15)

The outer sum is finite. The inner sum is absolutely convergent by
(4), (7), so this identity follows directly from kernel multiplication.
Replacing h_j(n-r) by h_j(n) costs at most

    sum_(n in supp u) |g(n)| C a p(k)
                             sum_r |r| |A(r)B(-r)|
                         <=C a N^3 p(k)p(l).                  (16)

This uses the whole clamped cumulative coefficient, including values
outside the compact displacement support. It does not truncate r,
the upper axial primitive, or the lower prefix in v.

The remaining midpoint sample h_j(n) differs from
h_(k,j)(-4+at,y_n) by <=C a p(k) wherever u(n) is nonzero.
The support lies inside the cube for large N; the same estimate also
follows from the Lipschitz clamp. The unweighted product bound in
(8) controls this change by another (16). Thus all three physical
coefficients are now evaluated at the same original vertex point.

For each frozen word the convolution diagonal (A B)(0) is its
torus integral, by Plancherel (or Fourier inversion for the smooth
positive-mass symbols). Restoring both signs in (13)--(14), every j,
plane, component and raw path, gives exactly

    F_(kl,epsilon)(x)=integral_(T^3)
      [sigma_k(x,theta)/(lambda+epsilon)^2]
        w(x,theta)* c(theta)* z_(v_l)(x,theta) tau(theta)
                                                   dtheta/(2pi)^3. (17)

Here all symbols are precisely L104(3)--(5). To check the sign,
(9)'s frozen symbol is sum_j h_j(bar(tau_j)-tau_j)
=2i sum_j h_j sin(theta_j)=sigma_k. The minus in (10) comes
from W*, whose symbol is the original -u s_mu* C_mu.
The two words supply -bar(tau_j)+tau_j, exactly the product of
X's contribution with the minus in W*.
J contains the actual circulation adjoint, P the signed raw row
times tau; summing them restores c* z_v tau. Therefore (17)
is the original massive frozen symbol, without a changed half,
orientation, color or outside factor.

Combining (12), (16), and the finite component enumeration gives
the uniform finite-level estimate

    |Tr[R X R W* D* zeta T]
                  -sum_n F_(kl,epsilon)(-4+at,y_n)|
                         <=C a N^3 p(k)p(l).                  (18)

The same estimates without coefficient differences bound both traces
by C N^3 p(k)p(l), uniformly in positive mass. Thus all exterior
series used here are absolutely summable under (5).

### 5. Full normalization, quadrature and frozen mass removal

Define K_(i,G,epsilon) as exactly L104(6) with lambda^-2 replaced
by (lambda+epsilon)^-2. Multiplying (18) by a^4(at), summing all
levels and complete heat labels, and using

    a^4 N^3 sum_(t=1)^(N-1)(at)<=C

gives an O_i(a) error in a^3 S^b. This accounts for all local and
nonlocal freezing errors, without a polynomial-range loss.

The numerator of (17) has four differences, with

    |sigma_k w* c* z_v tau|<=C p(k)p(l)lambda^2.                 (19)

Each first physical derivative obeys the same bound with an enlarged
fixed polynomial: derivatives act only on h,u,v. On the support of
u these are the smooth functions on the original cube. The integrand
of (17), its first physical derivatives, and the full heat-summed
density with weight x_1+4 are therefore uniformly bounded, since
lambda^2/(lambda+epsilon)^2<=1. The density has compact support
through u, including axial clearance.

The four-dimensional rectangle sum with mesh a consequently differs
from its integral by C_i a uniformly in epsilon. Explicitly, compare
each cell's value at its vertex with all its points using the uniform
first derivative bound and diameter 2a, then sum its volume; only a
fixed bounded physical neighborhood of the support contributes.
The original t=1,...,N-1 contains every nonzero axial sample for
large N. Transverse n ranges over the whole grid, with zero density
outside the support. No axial end row is dropped from the trace;
its exact u coefficient is zero there. The primitive defining h
still extends to 4.

It follows that

    |a^3 S^b_(i,N,epsilon)-K_(i,G,epsilon)|<=C_i a.              (20)

For mass removal in the frozen density, (19) and positivity of the
scalar denominators give the absolute majorant

    lambda^2[lambda^-2-(lambda+epsilon)^-2]
       =1-lambda^2/(lambda+epsilon)^2
       <=2epsilon/(lambda+epsilon)<=2epsilon/lambda.           (21)

The integral of lambda^-1 on the full three-dimensional torus is
finite; near zero this is the integral of C|theta|^-2. The value
at the one zero-frequency point is immaterial. The physical domain
is bounded and (5) applies, so

    |K_(i,G,epsilon)-K_(i,G)|<=C_i epsilon.                    (22)

This is an absolute estimate for a signed density, not a positivity
claim for the response. It is uniform before any mass is chosen.
Combining (20)--(22) and a=8/N proves (1).

At epsilon=N^(-2/3), the two errors in (1) are O(N^2) and
O(N^(7/3)). L252(5) supplies the original-pair comparison
O(N^(5/2)), already counting L250, L251 and L102/L103's removed
terms once. Hence (2) follows by the triangle inequality. This
uses finite uniform estimates throughout, not a fixed-mass limit
evaluated at a varying mass. All imported qualifications remain.

This is RESEARCH / REPRODUCTION under the unchanged approved EXPLORE
assessment `drafts/literature/2026-10-20-gradient-base-crossed-quantitative-remainder.md`.
Plancherel and Cauchy--Schwarz are imported standard named theorems;
the scalar ordered specialization is proved because the assessed
general trace/decay sources do not provide this cumulative remainder.
No general theorem is reproved. L249's coarse comparison is preserved,
and the failed free-operator, termwise projection and separate absolute
moment shortcuts are not used.

### 6. Separate critical audit, 2026-10-20

The audit accepts (1)--(2) under the unchanged EXPLORE assessment
`drafts/literature/2026-10-20-gradient-base-complete-remainder-critical-audit.md`.
L251 section 5 and L252 section 5 record the corresponding separate
checks of the two comparisons used here. This is RESEARCH /
REPRODUCTION: it certifies the existing component argument relative to
its imports, without a new estimate or progress beyond checked sources.
No failed identity, boundary case or norm placement was found.

**Literal scalar words and adjoints.** On the bulk tail-indexed grid,
each E_j is the identity between its scalar vertex and component-edge
copies. Thus X is exactly (9). For each of the three planes p=(mu,nu),
zeta has the two terms M_beta Bq and -M_chi Bb, and there are no other
terms. The signed raw traversal is

    +e_mu at n, +e_nu at n+e_mu,
    -e_mu at n+e_nu, -e_nu at n.

Its first-two and second-plus-third rows are precisely b_p and q_p
in L104(4). Hence using f=beta or f=-chi in each path term retains
both raw rows and their signs. For each W output component m,
W_m*=-s_m* M_u C_m. Starting with

    -Tr[R X R s_m* M_u C_m D_(p,m)* M_f B_path T]

and cycling only to M_u gives (10), on expanding X's two terms.
This confirms both signs and both adjoints for every plane/path/j/m
combination. J=C_m D_(p,m)* and P=B_path T are scalar convolution
stencils; a zero D entry simply contributes zero. The centered
difference s_m has symbol i sin(theta_m), whereas the incidence has
symbol tau_m=1-exp(i theta_m). They are not identified.

**The local commutator is exhaustive.** The only variable multiplier
encountered between M_u and the first constant convolution is M_f.
The exact identity J M_f=M_f J+[J,M_f] gives (11), with every shift
of the finite stencil J included. Its coefficient is bounded by
C a p(l), on the compact support selected by u. No inverse has
been commuted past a multiplier. Within the commutator words the
two numerator orders are (2,1) and (1,2); the bounded h multiplier
therefore needs only the unweighted l2 kernel pairing. The resulting
bound is C a N^3 p(k)p(l), uniformly in mass. In the principal words
only constant convolutions are collected, leaving exactly (13)--(14).
These have orders (3,1) and (2,2), respectively. This enumeration
retains each original endpoint-average filter inside J or s_m's
specified stencil and does not replace a raw path by an averaged one.

**Uniform joint moments.** Near the only singular torus point,
lambda is comparable to |theta|^2. For a q-difference numerator,
the squared unweighted multiplier is bounded by C lambda^(q-2).
For q=1 its worst behavior is |theta|^-2, integrable with the
three-dimensional volume element. For q>=2 the derivative estimate
in (7) has square bounded by C lambda^(q-3); at q=2 its worst
behavior is again |theta|^-2. All filters are finite shifts with
bounded derivatives, so these bounds hold for every actual J,P,T_j
and s_m factor, with uniform constants. Away from zero all are
bounded uniformly in positive mass. Lattice Plancherel thus proves
the stated unweighted l2 bounds and weighted l2 bounds for q>=2.
For (3,1) put |r| on the q=3 factor; for (2,2) either q=2 factor
suffices. Cauchy--Schwarz proves the full joint first moment in (8),
including all r, without an individual first absolute moment.

The clamped h remains globally bounded and Lipschitz, including
outside the support of u. In the complete closed diagonal (15),
|h_j(n-r)-h_j(n)|<=C a p(k)|r|. The joint bound just verified
therefore proves (16) before any spatial truncation or mass choice.
The midpoint-to-tail change costs the same O(a) by that Lipschitz
bound and the unweighted pairing. Thus no coefficient placement is
left unestimated: f was handled by the local commutator, h by the
closed two-kernel difference and its midpoint change, and u has been
the exact trace anchor throughout. Every convolution input/output
remains. The stopped factorwise shortcuts are not used.

**Exact frozen density.** With the coefficients frozen at the original
vertex x, X has symbol

    sum_j h_j (bar(tau_j)-tau_j)=sigma_k.

The W adjoint has symbol -u s_m* C_m, where C_m is the conjugate
of the endpoint-average symbol (1+exp(i theta_m))/2 in L104(5).
Summing J over m restores W* D*, and summing the signed f B_path
rows restores z_(v_l). The final incidence supplies tau. The two
resolvents supply exactly (lambda+epsilon)^-2. This recovers (17)
with precisely the adjoints and signs of L104(6). In particular the
two signs -bar(tau_j)+tau_j in the expanded words include W*'s
minus sign; they do not introduce a second minus or a missing half.

The four numerator differences are from X, s_m, D* and the final T;
the raw row z and the endpoint filters are bounded. Hence (19) and
its first physical derivatives are valid. Physical derivatives act
only on smooth h,u,v on the support of u, which has fixed clearance;
the nonsmooth clamp is never differentiated there. This gives
mass-uniform rectangle quadrature and retains the full lower-distance
weight at=x_1+4. The heat matrices are exactly the continuum matrices
already in L250/L252; no finite-label approximation is made here.
Their Gaussian envelope sums every polynomial needed for coefficients
and derivatives, including both probe polarizations and allowed
constant indices. L250 already controlled omitted mesh labels.

**Normalization, endpoint and final assembly.** The physical integral
in (20) uses a^4 times the vertex/level sum, with the same identity
a^4 N^3 sum_t(at)=(8^5/2)(1-1/N) checked in L251. The retained
primitive h integrates all the way to 4; no upper endpoint or
moving-cut contribution is removed here. L250's qualified comparison
accounts for their finite-mesh discrepancies. Vanishing u at axial
end collars removes no nonzero row. There is no extra color factor
or outside factor 3.

The elementary scalar inequality (21) is valid for every lambda>0.
The full torus integral of lambda^-1 is finite in dimension three,
so frozen mass removal costs O(epsilon) after heat summation. Thus
(20)--(22) yield O(N^2+N^3 epsilon) before scheduling. At
epsilon=N^(-2/3), this is O(N^(7/3)); L252(5) contributes the larger
O(N^(5/2)) and already includes L251, L250 and the removed original
pair terms once. The triangle inequality proves (2), with no
varying-mass use of a qualitative theorem. Independent component
rates, complete quantitative L011 assembly and every interacting,
continuum and infrared construction requirement remain unresolved.

## Mathlib

Full matching ordered gradient-base remainder: **not checked**.
Supporting lattice Fourier Plancherel, Fourier differentiation,
trace cyclicity, Cauchy--Schwarz, and rectangle quadrature: **not
checked**. Unknown availability is not evidence of absence. The
verification here is analytic; no numerical certificate or mathematical
script is used. Structural validation cannot audit the proof.
