# L247 — Transverse freezing with the raw reverse-trace data retained

## Hypotheses

Keep L246(1)--(2)'s equal-level bulk trace B_i^eq, for the relative
SU(2) cube, lower-rooted direction-1 forest, admitted even N, a=8/N,
tau=1/16, stored coordinates, bare-first order and actual probes i=3,6.
All imported comparisons retain their separate-audit qualifications;
this proof does not audit them. Use L228(1)'s same compact Lipschitz
extensions at each level, and L105(2)'s complete filtered W_t.

Identify each bulk transverse component grid with its integer tail
index Z^3, retaining the component-dependent finite stencil shifts.
Write v_(k,a)(t,j) for the three normalized raw exterior values used
in these extensions. They have support of at most C N^3 indices on
any slice, supremum <=C p(k), and index Lipschitz constant <=C a p(k).
Choose u_(a,t)(j) to be the raw displacement sample at the common
index. Every displaced sample occurring in W differs from this value
by O(a), with a constant independent of the masses. This follows
from the bounded shifts and the displacement's neighboring-difference
bound, not from convergence to a continuum coefficient. In particular
u_(a,t) has fixed physical support separated from all faces.

For vectors v,v' and a scalar u, let J_delta(v,v',u;theta) be exactly
L245(1)'s two-term numerator, using L107(1)'s raw symbols z_v,z_v'
and w_u, with these arguments in place of the continuum mode values.
It is bilinear in v,v' and linear in u. For positive masses <=1 define

    F_i^raw(epsilon,h,delta)
      =(a/2) sum_(t=1)^(N-1) sum_(j in Z^3) sum_(k,l)c_(i;kl,a)
        integral J_delta(v_(k,a)(t,j),v_(l,a)(t,j),u_(a,t)(j);theta)
                  /[(lambda+epsilon)(lambda+h)] dtheta/(2pi)^3. (1)

Here lambda=sum_(mu=2)^4 |1-exp(i theta_mu)|^2. The spatial sum is
finite because of u. All original finite-mesh heat labels and raw
exterior samples are retained. This definition has the full axial
half-sum; it is not L245(2)'s finite-sum continuum comparison F_i,N.
No raw-to-continuum coefficient or heat matching is assumed.

## Conclusion

There are constants C_i,c>0 such that

    |B_i^eq-F_i^raw|
      <=C_i [N^2 epsilon^(-1/2)
                    +N^3 epsilon^(-1) exp(-c N sqrt(epsilon))]. (2)

The bound is uniform in h,delta in (0,1]. At epsilon=N^-1,
h=N^(-4/3), delta=N^(-2/3), it is O_i(N^(5/2)). Consequently,
using L246's imported comparison,

    |R_R-F_i^raw(N^-1,N^(-4/3),N^(-2/3))|
                                      <=C_i N^(5/2) log(eN). (3)

This is a partial component estimate. A quantitative comparison of
(1)'s complete raw samples and finite-mesh heat series with L245's
continuum frozen density remains unproved here. Thus neither the
complete registered remainder relative to a^-3 K_(i,R) nor a complete
L011 remainder follows. There is no outside factor 3. Independent
component rates, interacting reflected error <=c_box/2, continuum
axioms, infrared control and finite positive mass remain unresolved.
This is REPRODUCTION using the saved reverse-remainder assessment,
without a claim of progress beyond checked sources. The separate
critical audit in proof section 6 accepts this specialization relative
to its imported inputs; it does not audit the upstream comparisons.

## Proof

### 1. Sum the finite axial range without changing transverse order

Fix t,k,l in L246(2). All coefficients and U_t=T G_h W_t* are now
independent of s. Thus the covariance can be summed in its original
leftmost position. L245(8)--(10)'s scalar resolvent identities give,
by spectral calculus on the whole transverse grid,

    sum_(s=1)^(N-1) S_st R_(s-t)
       =(1/2)(Delta_T+epsilon)^-1-E_t,
    E_t=sum_(d>=N-t) r_d(Delta_T+epsilon).                (4)

The infinite tail is only a comparison error, not an extension of the
response coefficients. If W_t is nonzero, its compact displacement
implies N-t>=c_0 N. Since 0<=lambda<=12 and epsilon<=1, the same
geometric calculation as L245(10) proves

    ||E_t||<=epsilon^-1 exp(-c N sqrt(epsilon)).          (5)

For all other t the original trace is zero. L246(8)--(9) gives
||U_t||<=C independently of h; it has rank <=C N^3 because W_t
is finite rank. All Z factors, D and Q_delta are bounded, with their
mode-polynomial factors. The trace bound rank times operator norm,
then the original a prefactor, at most N levels and the complete
heat envelope, bounds the error in (4) by

    C_i N^3 epsilon^-1 exp(-c N sqrt(epsilon)).          (6)

Every convolution input remains present in (4)--(6). The diagonal
half is responsible for 1/2; no additional lower-end deficit occurs
because S_st vanishes for s<t. For the remaining transverse argument
put R=(Delta_T+epsilon)^-1 and keep this factor 1/2 outside.

### 2. Replace bounded-offset raw coefficient samples, with an error

Let z_j, j=2,3,4, denote the constant convolution stencil with symbol
z_(e_j) in L107(1), mapping transverse edges E to plaquettes F.
The raw path formula of L244(2), whose traversal symbols are checked
in L104(4), gives the exact decomposition on each slice

    Z_k=sum_j M_(v_(k,a),j) z_j+E_k,
    ||E_k||<=C a p(k),   rank(E_k)<=C N^3.              (7)

Indeed each raw coefficient is a sum or difference of exterior samples
at boundedly separated indices. Replacing them by their values at
the common output index costs C a p(k). Bounded row and column
multiplicity gives the operator bound; the fixed enlargement of their
compact support gives the rank bound. After replacement the exterior
b,q coefficients are v_mu+v_nu and v_nu-v_mu, exactly z_v. This
accounts for shifts in adjoints too: the adjoint of the principal
part is sum_j z_j* M_(v_(k,a),j), in that order.

Write the filtered generator in the form

    W_t*=sum_mu L_mu M_(u_(a,t)) J_mu+E_W*,
    L_mu=-D_mu* C_mu*,   J_mu=C_mu pi_mu,               (8)

where pi_mu selects the mu edge component. All these are the actual
bulk endpoint filters and differences of L105(2); component scalar
grids are identified with Z^3 only for notation. If their raw common
multiplier samples already coincide, E_W=0. Otherwise their bounded
offsets change the displacement by O(a). The error is a sum of terms
-C_mu* M_(e_mu) C_mu D_mu with ||e_mu||_infinity<=C a.
Consequently the same gradient-energy argument as L246(8) gives

    ||T G_h E_W*||<=C a,
    ||T G_h sum_mu L_mu M_u J_mu||<=C,
    rank(T G_h E_W*)<=C N^3.                           (9)

Here both T and D_mu stay attached to the inverse: their normalized
gradient factors are contractions, and Delta_0/(Delta_0+h)<=1.
There is no h^-1 operator estimate for the middle inverse in isolation.
The displacement errors remain in a compact support enlarged by a
fixed number of cells. Its axial support also has fixed clearance.

Telescope both Z positions and the W position in the two ordered
products after (4). Their principal and error parts have finite rank
<=C N^3 and bounded norms with the indicated mode factors. In each
trace, R D* stays adjacent and

    ||R D*||<=sup_(lambda>=0) sqrt(lambda)/(lambda+epsilon)
                                                     <=C epsilon^-1/2.

All other factors, including either middle energy sandwich, are
bounded uniformly in h,delta. Hence the sum of these errors on one
slice, before a/2, is <=C a N^3 epsilon^-1/2 p(k)p(l).
After a sum over at most N slices and the full heat sum it is

    <=C_i N^2 epsilon^-1/2.                            (10)

This estimate justifies the local sample replacements; it does not
assume that a finite propagation range alone makes freezing valid.

### 3. Squared symbol moments for the actual remaining orders

All quantities below are bulk convolutions in three dimensions.
Suppress t and let f=v_(k,a),j, g=v_(l,a),m and u=u_(a,t).
Cyclically moving the last exterior multiplier to the front gives
the two exact principal words

    Tr_F[M_g A M_f H M_u K],                            (11)

with the following distinct choices (and the original subtraction):

    first:  A=D R D*,       H=z_j T G_h L_mu,
                           K=J_mu Q_delta z_m*;
    second: A=z_m R D*,     H=z_j T G_h L_mu,
                           K=J_mu D*.                 (12)

Only rectangular trace cyclicity is used here. In particular the sole
Q_delta in the first word has not crossed any multiplier and is not
made idempotent. The second word has only one circulation adjacent
to R. All fixed stencils and their integer-index phases remain.

For a matrix convolution B let ||B||_(L2 sym) and ||partial B||_(L2 sym)
mean the Frobenius L2 norms of its symbol and all three first frequency
derivatives, with normalized torus measure. The following bounds hold:

    ||A||_(L2 sym)<=C in both cases,
    ||A_first||_op+||partial A_first||_(L2 sym)<=C,
    ||partial A_second||_(L2 sym)<=C epsilon^-1/4,
    ||H||_op+||partial H||_(L2 sym)<=C,
    ||K||_op+||K||_(L2 sym)<=C.                         (13)

The constants in H,K are uniform in h,delta. Here are the singular
corner checks. Put r=sqrt(lambda), comparable with |theta| near zero.
The symbols of D,T,L_mu are O(r), their derivatives O(1); z_j,J_mu
and their derivatives are bounded. For A_first the symbol is
c c*/(lambda+epsilon), bounded by C, and its derivative is bounded
by C(1+1/r), uniformly in epsilon. Its squared derivative is integrable
in three dimensions. For A_second, the symbol is bounded by
C r/(r^2+epsilon), whose square has bounded integral. Its derivative
is bounded by C[1+(r^2+epsilon)^-1]. The squared integral is at most
C epsilon^-1/2: radially, split integral r^2/(r^2+epsilon)^2 dr at
sqrt(epsilon). Taking its square root gives epsilon^-1/4.

For H, the two gradient factors around G_h give symbol size
C r^2/(r^2+h)<=C. Differentiating gives a bound C(1+1/r), since
r/(r^2+h) and r^3/(r^2+h)^2 are <=1/r. This is again square
integrable uniformly in h. Finally Q_delta is a contraction, so K
has the stated bounded symbol and L2 norm without differentiating
Q_delta. All derivatives are of smooth periodic integer-index symbols
at positive masses. The fixed staggered phase derivatives add only
bounded multiples of the already controlled symbols. These estimates
cover the entire torus; away from zero every denominator is bounded
below independently of the masses.

### 4. Collect common scalars by global Hilbert--Schmidt commutators

For any of the compact scalar arrays b in (11), with supremum B,
index Lipschitz constant a L and support <=C N^3, Fourier-series
Plancherel gives

    ||[B0,M_b]||_HS<=C a L N^(3/2)
                                      ||partial B0||_(L2 sym),
    ||M_b B0||_HS+||B0 M_b||_HS
                                  <=C B N^(3/2)||B0||_(L2 sym). (14)

The first formula also holds for rectangular convolutions, using
scalar multiplication by the same array on the corresponding grids.
To verify it completely, the commutator kernel at x,y is
B0(x-y)[b(y)-b(x)]. For fixed displacement z=x-y, the difference
can be nonzero at no more than 2C N^3 indices, and its absolute value
is at most a L |z|_1. Squaring, summing and applying Plancherel yields
(14). The second formula follows by the exact squared norm of every
translated kernel row or column. All input and output indices remain
in these sums; neither formula restricts a Green source. Products of
our scalar arrays have the same support count and appropriate product
bounds for B,L.

Use three exact identities, in order:

    A M_f=M_f A+[A,M_f],
    H M_u=M_u H+[H,M_u],
    A M_u=M_u A+[A,M_u].                               (15)

They express (11) as Tr_F[M_(g f u) A H K] plus the three errors

    Tr[M_g [A,M_f] H M_u K],
    Tr[M_(g f) A [H,M_u] K],
    Tr[M_(g f) [A,M_u] H K].                           (16)

For the first, cycle to pair [A,M_f] with H M_u K M_g.
The latter has Hilbert--Schmidt norm <=C N^(3/2), with the mode
factors from g and u, by ||H||,||M_u|| and (14) for K M_g.
The commutator norm is <=C a N^(3/2) epsilon^-1/4 with the f
factor, by (13)--(14). For the second error pair M_(g f) A, whose
Hilbert--Schmidt norm is <=C N^(3/2) by A's uniformly bounded symbol
L2 norm, with [H,M_u] K, whose norm is <=C a N^(3/2).
For the third pair [A,M_u] with H K M_(g f), using ||H|| and the
same localized K norm. Hilbert--Schmidt trace duality therefore bounds
all three errors on one slice by

    C a N^3 epsilon^-1/4 p(k)p(l).                     (17)

Finite sums over j,m,mu are harmless. At positive masses all original
words are trace class because of compact multipliers; every error
above is a product of Hilbert--Schmidt and bounded operators, which
also justifies each cyclic rearrangement. No trace positivity,
operator-small projection commutator, or first absolute kernel moment
is used. In particular the required moment of A_second is a squared
moment with its explicit epsilon dependence.

After the original a/2, at most N levels and the full heat envelope,
(17) gives a total <=C_i N^2 epsilon^-1/4. Since epsilon<=1, this
is bounded by the first term of (2). This is a uniform finite inequality
before a mesh-dependent mass schedule is selected.

### 5. Identify the frozen word and combine the estimates

The collected word is exactly a compact scalar multiplier times a
convolution. Its trace is the spatial sum of the scalar times the
zero-offset matrix diagonal, which equals the full torus integral
of tr[A(theta) H(theta) K(theta)]. This follows from Fourier inversion
of the bounded, integrable product at positive masses, or directly
from its matrix elements. Summing j,m,mu restores z_v,z_v' and w_u.
The first case of (12) gives

    tr[c c* z_v tau w_u* q_delta z_v'*]
                                    /[(lambda+epsilon)(lambda+h)],

and the second gives

    tr[z_v' c* z_v tau w_u* c*]
                                    /[(lambda+epsilon)(lambda+h)].

Finite matrix cyclicity makes these exactly L245(1)'s first and
second numerators respectively, with the original subtraction. The
constant-coefficient W symbol is precisely L104(5), including both
endpoint filters and the forward/centered difference convention;
it is not the tail-minus-head incidence tau. The overall a/2 from
(4) remains. Thus the resulting expression is exactly (1), with the
same raw data and c_(i;kl,a), rather than a continuum replacement.

Combining (6), (10) and (17) proves (2). At epsilon=N^-1 its first
term is N^(5/2), while the second is N^4 exp(-c sqrt(N)), smaller
for sufficiently large N. No h or delta loss occurs. L246(4) then
proves (3) at the stated schedule. Its inherited comparison is used
once. This completes the promised transverse freezing attempt only.

To compare (1) with L245, one must still bound the complete difference
between its normalized raw common-index exterior values/displacement
and the continuum values, and between its finite-mesh heat series and
the full continuum series, with omitted labels included. Neither
pairwise convergence nor a qualitative heat domination supplies the
needed quantitative rate. Those estimates are not assumed here.
All finite ranges, source/end rows and constant indices remain in
the imported comparisons; the axial extension used here has the
explicit error (6). There is no R_L transpose transfer, assumption of
smoothness of a rough kernel, or fixed-mass theorem applied at varying
mass. All conclusions remain conditional on the stated imported inputs.

### 6. Separate critical audit — 2026-10-20

This audit accepts (2)--(3) under the stated hypotheses and imported
qualifications. It uses the saved SPECIALIZE assessment
`drafts/literature/2026-10-19-reverse-crossed-transverse-freezing-audit.md`.
L248 is not a premise. No stronger exponent, new source theorem or
upstream verification is asserted. The following checks concern the
actual ordered products, rather than a scalar surrogate.

**Finite axial range.** For a fixed t, the allowed offsets are
d=0,...,N-1-t, with weight 1/2 only at zero. L245(8)--(10) therefore
gives exactly R/2 minus the tail beginning at N-t. There is no missing
negative-offset contribution: the triangular selector is zero there.
At positive epsilon these scalar kernels are absolutely summable in
operator norm, so their sum can replace the covariance in its original
position. For nonzero W_t the actual displacement and its fixed stencil
enlargement give N-t>=c_0 N. The function
arcosh(1+mu/2)/sqrt(mu) has a positive lower bound on 0<mu<=13,
giving (5). Each remaining product has rank O(N^3), regardless of
the nonlocal output of T G_h. Its norm after removing E_t is bounded
by C p(k)p(l). The original a, N levels and full heat envelope give
a N N^3 epsilon^-1 exp(-cN sqrt(epsilon)), exactly (6).

**Raw replacements and energy order.** L104(4)'s four traversals are
e_mu, S_mu e_nu, -S_nu e_mu, -e_nu. Their two relevant sums have
constant-exterior values v_mu+v_nu and v_nu-v_mu, respectively.
L228(1)'s fixed-offset neighboring bounds therefore give (7), including
its adjoint z_j* M_f and every original staggered shift. No endpoint
average or continuum value is substituted. For a displacement error,
E_W has components -C_mu* M_(e_mu) C_mu D_mu. On the dense spectral
domain away from zero,

    ||E_W Delta_0^(-1/2)v||^2
      <=C a^2 sum_mu ||D_mu Delta_0^(-1/2)v||^2
      =C a^2 ||v||^2.

Thus ||E_W Delta_0^(-1/2)||<=C a, and the exact factorization is

    T G_h E_W*=(T Delta_0^(-1/2))
          [Delta_0/(Delta_0+h)] (E_W Delta_0^(-1/2))*.

It extends boundedly with norm C a. Replacing e_mu by the bounded
common u proves the principal bound in (9). No multiplier crosses an
inverse, and neither inverse half is assigned a bounded norm alone.
In every Z or W replacement trace, the unchanged R D* can still be
bounded by C epsilon^-1/2; the other curl, if present, is bounded.
Finite-rank trace duality then gives C a N^3 epsilon^-1/2 p(k)p(l)
per slice. Multiplying by a and summing N levels gives (10), because
a^2 N^4=64 N^2. Cross-error terms in telescoping are covered by the
same bounded principal/error norms, since a is bounded on admitted
meshes. Every convolution source remains in these operator bounds.

**Literal words and squared moments.** Cycling the first trace puts
M_g immediately before D R D*, while cycling the second puts it
immediately before z_m R D*. The rest of both words is exactly
M_f z_j T G_h L_mu M_u J_mu, followed respectively by
Q_delta z_m* or D*. Thus (11)--(12) have compatible rectangular
domains and retain the subtraction and the sole Q_delta.
Common-index scalar multiplication on each component space means the
same numerical array; all staggered offsets stay inside the convolution
stencils. It does not identify physical component centers.

Near zero, the first A and H have bounded symbols and first derivative
bounded by C(1+r^-1); their squared derivative integral is finite in
three dimensions, uniformly in the respective masses. For the second
A its squared symbol integral is bounded by
C integral_0^C r^4/(r^2+epsilon)^2 dr<=C'. Its squared derivative
integral is bounded by C[1+integral_0^C r^2/(r^2+epsilon)^2 dr]
<=C' epsilon^-1/2, by splitting at sqrt(epsilon). This confirms the
epsilon^-1/4 norm in (13), rather than a mass-uniform derivative norm.
The fixed phase and stencil derivatives multiply already controlled
symbols. Outside a neighborhood of zero all denominators are bounded
below. K only needs its bounded symbol and L2 norm: Q_delta is never
differentiated, commuted or treated as idempotent.

**All three commutators.** Entrywise Fourier-series Plancherel for
the positive-mass periodic matrix symbols proves (14). For each
displacement the union of the two translated coefficient supports
has at most 2C N^3 indices, including indices outside the physical
box. Both input and output are summed. The scalar grids in the
rectangular H commutator use the same array, so its kernel difference
is also exactly b(y)-b(x). Applying the three product identities in
(15) gives precisely the three errors in (16), with no additional
placement. Their Hilbert--Schmidt dual pairs are, in order,

    [A,M_f]              and H M_u K M_g,
    M_(g f) A            and [H,M_u] K,
    [A,M_u]              and H K M_(g f).

The respective bounds are
(C a N^(3/2) epsilon^-1/4, C N^(3/2)),
(C N^(3/2), C a N^(3/2)), and the first pair's bounds again,
with the appropriate p(k)p(l) factors. Only the second A's L2 norm,
not its operator norm, is used in the middle pair. Hence the global
trace cost is exactly (17). Positive masses make every original
factor bounded and compact multipliers finite rank; the displayed
error products are trace class by Hilbert--Schmidt trace duality.
These facts justify rectangular cyclicity and all infinite-grid traces.

**Normalization and conclusion.** Restoring the finite component sums
turns sum_mu L_mu u J_mu into the adjoint of exactly L105(2)'s W,
whose raw symbol is L104(5), not tau. The diagonal of the collected
convolution is its normalized full-torus integral. Cyclic finite-matrix
traces therefore yield the two numerators displayed in section 5,
with their original subtraction and a single a/2. The full finite-mesh
envelope sum|c_(i;kl,a)|p(k)p(l)<=C_i covers both actual probes and
all allowed constant indices before any mass choice. The commutator
cost sums to C_i a^2 N^4 epsilon^-1/4=C'_i N^2 epsilon^-1/4,
which is below (10) for epsilon<=1. Adding (6) proves exactly (2).
At epsilon=N^-1 the tail is N^4 exp(-c sqrt(N))=O(N^(5/2));
all estimates remain uniform in h,delta. Importing L246(4) once gives
(3), including its logarithm and no outside factor 3.

This verifies the local specialization only. L244's boundary transfer,
L246's axial replacement and upstream inverse/projection comparisons
retain their separate audit qualifications. Raw-to-continuum heat
matching is not used here. The complete quantitative L011 assembly,
interacting comparison and Yang--Mills construction remain open.

## Mathlib

Full matching ordered transverse reverse-freezing theorem: **not
checked**. Supporting Fourier-series Plancherel, rectangular
Hilbert--Schmidt trace duality, spectral calculus, integrability and
finite-rank trace coverage: **not checked**. Unknown is not absence.
The raw symbol and filtered-energy identifications are imported from
L104, L105, L107 and L244; their specialization and squared-moment
bounds are justified above. The saved literature assessment covers
these standard methods but supplies no complete matching theorem by
citation, so the specialization is written out rather than claimed
as an imported rate.
