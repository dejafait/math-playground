# L254 — Complete quartic-residual remainder

## Hypotheses

Keep exactly L149–L152's relative SU(2) cube D=(-4,4)^4, straight
lower-rooted direction-1 forest, ordinary stored coordinates, admitted
even N, a=8/N, tau=1/16, and actual probes i=3,6. The bare coefficient
is taken at each fixed mesh before refinement. Keep all three colors,
every covariance source and normal end row, all allowed constant
component indices, both signed insertion subtractions and the full
external heat sums. The displacement and insertion coefficients have
fixed compact interior support. All fixed stencil enlargements thus
have distance at least delta N from the lattice boundary for sufficiently
large N, with delta>0 independent of N.

Use precisely L152(2)–(8)'s tensors, midpoint offsets, continuum exterior
kernel and coefficient Lambda_i. No numerical evaluation or sign of
Lambda_i is assumed. L150's projection-row bound and frozen parity,
L151's exact heat representations and spectral bounds, and L222/L248's
supporting modal/probe estimates are imported with their qualifications;
their different diagnostic and trace conclusions are not imported.
This proof does not independently audit those inputs.

## Conclusion

For sufficiently large admitted N, constants C_i independent of N give

    |a^3 kappa_0(f_(i,0),r_2)-Lambda_i|
                         <= C_i N^(-1/2) log(eN)^(3/4),       (1)
    |kappa_0(f_(i,0),r_2)-a^(-3)Lambda_i|
                         <= C_i N^(5/2) log(eN)^(3/4).        (2)

Consequently the approved O(N^(5/2) log(eN)^2) threshold holds for
this complete quartic insertion. The connected factor twelve appears
once, with no outside factor three. Section 5's separate critical audit
accepts this specialization relative to the stated imported inputs.
It supplies one component remainder, not a
complete L011 rate, a finer coefficient, an interacting reflected-error
bound, continuum axioms or finite positive infrared mass.

## Proof

### 1. Quantitative local projected covariance comparison

Write H_N and H_inf for L151(3)–(5)'s co-closed local covariances,
distinct from the exterior kernel H_i below. We first prove, uniformly
over all supported local stencil pairs,

    |H_N((s,l),(t,m))-H_inf((s,l),(t,m))| <= C_delta/N. (3)

All heat times in this section are dimensionless. Let A_N(v) be the
axial Dirichlet heat entry at s,t and A_inf(v)=h_v(s-t). Let
B_N(v) be the transverse entry of exp(-v Delta_T)(I-P), and B_inf
its infinite-grid counterpart. L151 supplies the exact representations

    H_N = integral_0^infinity A_N(v) B_N(v) dv,
    exp(-v Delta_T)P
        = integral_v^infinity T exp(-w Delta_0) T^T dw,    (4)

with the corresponding infinite formulas. Its full spectral estimates
give, for either finite or infinite entries,

    |A(v)| <= C(1+v)^(-1/2),
    |B(v)| <= C(1+v)^(-3/2),
    |[T exp(-w Delta_0)T^T]_(l,m)|
                                    <= C(1+w)^(-5/2).   (5)

These estimates include times greater than N^2 and every low mode.
They imply an outer integral tail C/(1+V) and an inner projection
tail C(1+W)^(-3/2). We use the entrywise inner bound, not the slower
row-norm tail.

Here is a uniform finite-time comparison with an explicit growing
time range. The dimensionless axial, transverse component and vertex
Laplacians, finite and infinite, have norms at most M=16. Their
interior coefficients agree and their range is one lattice step.
The two incidence maps in the projection sandwich have uniformly
bounded norms and add at most two steps to a polynomial path.
Take d_N=floor(delta N/4), reducing delta if necessary. For large
N, all local entries of powers through degree d_N agree exactly
between finite and infinite operators; this also holds after the
two incidence maps. This follows by expanding a matrix power as
a sum over paths starting at the selected interior row. Every
intermediate index stays inside the identical interior coefficients.
The reflected normal component and pinned vertex boundary operators
therefore cause no change to these entries.

Put T_N=d_N/(100M). For 0<=w<=T_N the degree-d_N Taylor polynomial
of exp(-wL) has operator remainder at most

    exp(Mw) (Mw)^(d_N+1)/(d_N+1)!
      <= exp(d_N/100) (e/100)^(d_N+1)
      <= C exp(-c d_N).                                  (6)

The factorial bound n! >= (n/e)^n is sufficient. The same estimate
holds on the infinite Hilbert space since L is bounded. Local
polynomial equality and the bounded incidence norms now imply

    |A_N(v)-A_inf(v)| <= C exp(-c_delta N),
    |[exp(-v Delta_T)-exp(-v Delta_inf)]_(l,m)|
                                           <= C exp(-c_delta N),
    |[T exp(-w Delta_0) T^T
          -T_inf exp(-w Delta_0,inf) T_inf^T]_(l,m)|
                                           <= C exp(-c_delta N) (7)

for v,w<=T_N. The differences here compare only the specified
interior entries; they are not global operator-difference estimates.
No projection is claimed to have finite propagation.

For v<=T_N, integrate the third comparison in (7) over [v,T_N].
For [T_N,infinity), use the two complete inner tails from (5).
Together with the second comparison in (7), this gives

    |B_N(v)-B_inf(v)|
          <= C[(1+T_N) exp(-c_delta N)+(1+T_N)^(-3/2)].   (8)

Telescope A_N B_N-A_inf B_inf as
(A_N-A_inf)B_N+A_inf(B_N-B_inf). Integrating up to T_N, use
the integrable (1+v)^(-3/2) bound for B_N in the first term and
integral_0^T_N (1+v)^(-1/2)dv <= C(1+T_N)^(1/2) in the second.
The result is at most

    C[(1+T_N)^(3/2) exp(-c_delta N)+(1+T_N)^(-1)].

The two outer tails are also O((1+T_N)^(-1)) by (5).
Since T_N is a fixed positive multiple of N up to a bounded error,
this proves (3). This is an estimate of the exact integrals with
uniform finite errors, not insertion of a varying cutoff into a
qualitative convergence assertion.

For the full local forest covariance C_e, combine (3) with L085(2)
as used in L151, and import L150(5), equivalently L151(11):

    |(P-P_inf)_(l,m)| <= C N^(-3/2) log(eN)^(3/4).

The factor min(s,t) is at most N. Thus, with C_e^0=j_*p_nu,
the exact L151(12) decomposition becomes

    C_e-C_e^0 = S_nu+E_e+D_e,
    max |D_e| <= C epsilon_N,
    epsilon_N=N^(-1/2) log(eN)^(3/4),                    (9)

where E_e=-|s-t|P_inf/2+H_inf retains the original orientation and
color factors. Its entries are uniformly bounded and it is inversion
even. S_nu is precisely L152(2)'s axial slope. L150/L151's exact
signed inversion gives K_e^0:U_i^0:E_e=0 for the complete frozen
tensor and any spatially constant component/color matrix U_i^0.
It does not remove S_nu.

For every force or insertion stencil we also retain L150's simpler
comparison, with its own center c and d(c)=c_1+4:

    |a C_e-d(c)p_e| <= C a.                              (10)

Indeed C_e-j_*p_e is uniformly bounded and aj_*=d(c).
The insertion stencils have the same fixed-radius interior property.
All these comparisons are local entries of the full pinned covariance;
no covariance source row has been truncated.

### 2. Quantitative first derivatives of the actual raw exterior

We next quantify L152(10)–(12). This is necessary even though frozen
parity already cancels the diagonal term. For a retained relative
product-mode label k, let r=|k|>=sqrt(3), and use
A_(k,a)=f_k/sqrt(lambda_(k,a)), A_k=f_k/sqrt(lambda_k).
The exact samples and normalization, including zero own-direction
indices, are those in L028 and L222. The supporting estimates
L222(2)–(3) give for every fixed nonnegative m

    ||A_(k,a)||_(C^m)+||A_k||_(C^m) <= C_m r^(m-1),
    ||A_(k,a)-A_k||_(C^m) <= C_m a^2 r^(m+1).          (11)

For component 1 define J A(x)=integral_(-4)^x_1 A(t,x_perp)dt.
If k_1>0, L152(9)'s exact midpoint cosine sum has the smooth
extension

    Phi_(k,a)(x)=q_(k_1,a) J A_(k,a,1)(x),
    q_(k_1,a)=theta/sin(theta), theta=pi k_1/(2N).       (12)

For k_1=0 set q=1; the primitive is exactly the linear lower-distance
factor. If the mode component is not 1, both primitives vanish.
At each actual axial level, (12) is exactly the prefix sum, not
an approximate quadrature rule.

On 0<=theta<=pi/2, sin(theta)>=2theta/pi and Taylor's remainder
gives 0<=theta-sin(theta)<=theta^3/6. Consequently
|q|<=pi/2 and |q-1|<=C a^2 r^2, uniformly over retained labels.
For the finite set of derivative orders used here, integration over
an interval of length at most 8 and differentiation at its moving
upper endpoint show

    ||J A_(k,a,1)||_(C^m)+||J A_(k,1)||_(C^m)
                                                  <= C_m r^(m-1).

For derivatives with no axial derivative this uses length 8;
with at least one axial derivative it uses the corresponding
derivative of A of order one less. The weaker displayed bound
holds for both since r>=1. Apply the same argument to the difference
in (11). Equations (11)–(12) then imply

    ||Phi_(k,a)-J A_(k,1)||_(C^m)
                                                  <= C_m a^2 r^(m+1),
    ||Phi_(k,a)||_(C^m) <= C_m r^(m-1).                 (13)

At a transverse-link midpoint x, L248(4),(6), or L028(9), reads
exactly

    ell_(k,a,mu)(x)
        =A_(k,a,mu)(x)-delta_(mu,a) Phi_(k,a)(x), mu>1,
    ell_(k,a,1)=0,                                     (14)

where delta is the centered endpoint quotient of L028(3). The
one-sided formula at a vertex becomes (14) upon using its actual
link midpoint. It involves no averaging of different raw links.
The continuum column is ell_(k,mu)=A_(k,mu)-partial_mu J A_(k,1),
exactly L152(5).

Use L028(4)'s C^m centered-difference remainder and (13), with
one additional derivative for the primitive difference. For 0<=m<=2,

    ||ell_(k,a)-ell_k||_(C^m) <= C_m a^2(1+r)^(m+2),
    ||ell_(k,a)||_(C^m)+||ell_k||_(C^m)
                                            <= C_m(1+r)^m. (15)

The second bound uses the integral formula for delta, independently
of the first bound; it is uniform even near the mode cutoff.
All norms are on a fixed compact interior enlargement. Formula
(12) extends the interior samples only; it does not continue the
forest across its separately pinned upper value.

Let c_(i;kl,a) and c_(i;kl) be the complete heat-weighted normalized
probe matrices in L248(10)–(11). They are the coefficients of
L152(6), since both use L149(9)'s square-root-covariance columns
and L008's normalized quadratic form. For s=|l| and c0=tau/16,
the already matched supporting estimate is

    |c_(i;kl,a)|+|c_(i;kl)| <= C_i exp[-c0(r^2+s^2)],
    |c_(i;kl,a)-c_(i;kl)|
            <= C_i a(1+r+s)^4 exp[-c0(r^2+s^2)].         (16)

For i=3 this retains the four separate products in the average of
squares, with its 1/4; for i=6 it retains both polarized clover
products, their 1/2, all plane indices and strains. These are the
same actual forms, not the endpoint-averaged diagnostic exterior.

Insert (14) into the finite two-point exterior series H_(i,a).
Differentiate with respect to each argument separately, to total
order at most two. Telescoping its coefficients and its two columns,
using (15)–(16), bounds each retained-pair discrepancy by

    C_i a(1+r+s)^8 exp[-c0(r^2+s^2)].                   (17)

For example, derivatives of the column product contribute at most
degree two to the coefficient-error term; a column difference
contributes at most degree four before the other column. Degree
eight is a common upper bound. The independent value bounds in
(15) avoid multiplying two error estimates.

The full polynomial Gaussian pair sum in (17)/a is finite, with
constant component indices retained. For omitted continuum labels,
one index is at least N, as in L248's retained-mode comparison.
Their differentiated terms are bounded by the same type of polynomial
Gaussian envelope. Splitting exp[-c0(r^2+s^2)] into two equal factors
bounds their sum by C_i exp(-c0 N^2/2), hence by C_i a.
Therefore

    ||H_(i,a)-H_i||_(C^2(K times K)) <= C_i a,
    ||H_(i,a)||_(C^2)+||H_i||_(C^2) <= C_i.             (18)

Here K contains every supported stencil. No internal covariance
receives these heat weights.

For a force stencil centered at c, freeze
U_i^0=a^2 H_(i,a)(c,c), keeping the two component/color indices.
The exact exterior samples and Taylor's theorem, followed by (18),
give the quantitative replacements

    a^(-2)U_i = H_i^0(c)+O_i(a),
    a^(-2)U_i^0 = H_i^0(c)+O_i(a),
    a^(-3)(U_i-U_i^0) = H_(i,nu)^1(c)+O_i(a).          (19)

The last line uses the separate directional derivative
h_alpha dot partial_x+h_beta dot partial_y before setting y=x;
it is not a common derivative of the diagonal. Its Taylor remainder
after the indicated normalization is O_i(a), by the uniform C^2
bound. The first line also applies to every insertion stencil.

### 3. Displacement and both insertion comparisons

L028(4)'s coefficient extensions give O(a^2) convergence of u_a,w_a,s_a
in every fixed C^m norm, on the same fixed compact support. With
L152's finite linear tensor map F_nu, Taylor expansion at the actual
central-edge midpoint therefore yields

    a K_e^0 = F_nu^0(c)+O(a^2),
    K_e-K_e^0 = F_nu^1(c)+O(a).                         (20)

The second estimate divides a displacement increment by a; the
uniform second derivative bound controls its remainder, while the
first derivative coefficient discrepancy is O(a^2).
All endpoint offsets in F_nu^1 are unchanged.

For the plaquette subtraction, the four-vertex average tilde b_p
differs from (w_mu+w_nu)(c_p) by O(a), using its fixed shifts and
bounded first derivatives, as well as the O(a^2) coefficient error.
For the vertex subtraction s_a(c)-s(c)=O(a^2). The word tensors
themselves are finite and a-independent. Thus both full signed
insertion tensors obey

    M_(t,a)=M_t(c_t)+O(a),                              (21)

with exactly the signs, colors and three degree splittings of
L149(7), as defined in L152(4). Neither insertion is discarded.

### 4. Assemble the entire contraction and quadrature error

Use the exact L152(15) decomposition at each central edge. Its
frozen term vanishes identically by L150, before any estimate.
After division by a, its first two terms are exactly

    (K_e-K_e^0):(a^(-2)U_i):(a C_e),
    (a K_e^0):[a^(-3)(U_i-U_i^0)]:(a C_e).

By (10),(19),(20), these differ by O_i(a), uniformly over supported
placements, from

    d F_nu^1:H_i^0:p_nu,
    d F_nu^0:H_(i,nu)^1:p_nu,                          (22)

respectively. The third term, divided by a, is exactly

    (a K_e^0):(a^(-2)U_i^0):(C_e-C_e^0).

Apply (9) and the exact contraction of E_e to zero. The remaining
term differs from F_nu^0:H_i^0:S_nu by O_i(a+epsilon_N).
The matrices multiplying D_e are bounded by (19),(20), so no
additional factor of N is lost here. For every insertion the
per-placement term divided by a is exactly

    M_(t,a):(a^(-2)U_i):(a C_e);

it differs from d M_t:H_i^0:p_t by O_i(a).

There are O(a^(-4)) supported placements, with fixed stencil sizes
and color counts. Multiplying the complete response by a^3 converts
all these divided terms into their a^4 volume sums. The resulting
total error is at most C_i(a+epsilon_N). This retains all four
central-edge types, six plaquette types and six vertex/plane types,
and the factor twelve from L149(2) once.

The density left in these sums is exactly the four terms in
L152(8), including the displacement jet, the two-argument exterior
jet, axial slope, and both types of insertion. Each type is on
its own shifted grid with one placement per cell. Its density is
compactly supported and C^1 with bounded norm: derivatives of the
exterior jet use the C^2 bound in (18), and the displacement and
insertion coefficients are smooth. The tensors p and S depend
only on the fixed offsets, not on c.

L222(5)'s rectangle-quadrature argument applies unchanged to each
shifted grid: a cell and its sampling point differ by at most C a,
and compact support eliminates the boundary cells for small a.
The sum-to-integral error is C_i a. Its integral is precisely
Lambda_i, with no further evaluation or cancellation.
We have therefore proved

    |a^3 kappa_0(f_(i,0),r_2)-Lambda_i|
                                      <= C_i(a+epsilon_N).

Since a=8/N, this proves (1). Multiplication by a^(-3)=N^3/512
gives (2), which is below the requested logarithmic threshold.

### Qualifications and checks

The polynomial comparison acts only on local heat entries, while
both projection and covariance integrals retain their full tails.
The frozen even covariance part is removed only by the complete
tensor identity. The growing gradient covariance is retained in
the displacement/exterior/insertion terms, and its projection-row
error remains the dominant allowance. Raw links are compared at
their actual midpoints; the constant axial prefix and upper pin
are not equated. Full mode bounds precede every heat sum.

This is a new local quantitative specialization under the saved
EXPLORE assessment, not certified originality or a new general
heat-kernel theorem. The primary scalar-walk theorems inspected
there are not needed as additional inputs: the proof quantifies
L151's already established bounded-operator heat calculus.
The separate review of (3), (15)–(19), and the complete normalization
in section 4 is recorded below; it does not recursively verify the
imported inputs.

### 5. Separate critical audit, 2026-10-20

**Verdict: accepted relative to the imported inputs in the hypotheses.**
This audit uses the prior EXPLORE scope in
`drafts/literature/2026-10-20-quartic-residual-rate-critical-audit.md`.
It checks the proposed rate against exactly L152(8), without using
L153/L154's values or signs. No unsupported estimate or normalization
was found within this scope. The following checks verify the existing
argument; they introduce no stronger bound or new lemma.

**Local heat comparison and full tails.** L151(5),(9) give precisely
the two integrals in (4), on the same relative component and pinned
vertex spaces. The dimensionless axial norm is at most 4 and each
transverse norm at most 12, so M=16 is sufficient. A local entry of
T L^j T^T uses paths of length at most j+2 from its specified edge.
For d_N=floor(delta N/4) these paths remain interior, including
their initial and final incidences, for all sufficiently large N.
The same assertion for a component heat entry needs only j steps.
This proves the exact polynomial comparison on the rectangular
spaces; it does not restrict an exact heat operator's source rows.

For 0<=w<=d_N/(100M), the exponential remainder is bounded by
exp(d_N/100)(e/100)^(d_N+1), using
Mw/(d_N+1)<=1/100. Its decay is exponential in N, uniformly for
the finite and bounded infinite operators. The two gradients have
fixed operator norms, so their insertion changes only the constant.
For B_N-B_inf, the two tails of the projection integral are each
O(T_N^(-3/2)), by the entry estimate L151(10), not its row norm.
Consequently the integrated error on [0,T_N] is bounded by

    C exp(-cN) integral_0^T_N (1+v)^(-3/2) dv
      + C[T_N exp(-cN)+(1+T_N)^(-3/2)]
                         integral_0^T_N (1+v)^(-1/2) dv
    <= C[(1+T_N)^(3/2) exp(-cN)+(1+T_N)^(-1)].

Each outer tail is O((1+T_N)^(-1)) by L151(8).
This proves (3) uniformly over every supported pair. In particular
the long-time bounds are used beyond N^2 as established in L151;
no zero or lowest mode is deleted.

The remaining exact covariance error is
min(s,t)(P-P_inf)+(H_N-H_inf). Its first term is at most
C N^(-1/2)log(eN)^(3/4) by the imported L150(5) row estimate.
The min(s,t) factor is bounded by N, not by a constant. Subtracting
j_*P_inf leaves exactly the axial slope and the absolute-value kink
in (9). L151(13)'s signed permutation removes E_e only after
contraction with the complete K_e^0 and spatially constant U_i^0.
Neither the slope nor D_e is removed by parity. The bounded-offset
condition and L150(4) also justify (10) for each insertion center.

**Raw derivatives, including the cutoff.** L152(9) is an identity
for the midpoint sum to a transverse link's axial level. Dividing
it by the continuum cosine primitive gives theta/sin(theta);
the formula extends by q=1 at the zero axial index. All retained
theta lie in [0,pi/2), so the bounds used in (12) hold without
assuming ar is small. If a multi-index has no axial derivative,
J is bounded by its integration length 8. If it has an axial
derivative, differentiation of its upper endpoint reduces the
needed derivative of A by one. Thus for every fixed m,

    ||J(A_(k,a)-A_k)||_(C^m) <= C_m a^2 r^(m+1),
    ||J A_(k,a)||_(C^m) <= C_m r^(m-1).

Multiplication by the spatially constant q gives (13). This also
checks the case m=0, when the second bound is C/r, and the linear
lower-distance primitive at k_1=0.

To check the derivative loss in (15), write its prefix difference as
delta_(mu,a)(Phi_(k,a)-J A_k)
plus (delta_(mu,a)-partial_mu)J A_k. The first term in C^m is at
most ||Phi_(k,a)-J A_k||_(C^(m+1)); the second is at most
C a^2||J A_k||_(C^(m+3)). Both are bounded by
C_m a^2 r^(m+2). The direct A difference is smaller.
Separately the integral formula for delta bounds its C^m value
by ||Phi_(k,a)||_(C^(m+1))<=C_m r^m. These estimates establish
both lines of (15) for m<=2, independently of the size of their
error at high labels. The largest primitive derivative used is
order five, permitted by the all-fixed-order imported mode bounds.
Changing the raw one-sided vertex quotient to its link midpoint is
exact; no endpoint averaging or extension across the upper pin occurs.

**Complete exterior and its two arguments.** L149(9)'s column T_a e_k
is exactly a ell_(k,a). Its coefficient matrix is the same normalized
B_(i,a;kl) used in L248(10), so U_i=a^2 H_(i,a) with the stated
component/color indices. L248(10)--(11) covers both full probes,
with the four triplet products and both shear polarizations intact.
No diagnostic-specific upper row is inserted into this exterior.

For separate derivatives of orders p,q with p+q<=2, telescoping
the coefficient and the two columns gives a bound by a constant times

    exp[-c0(r^2+s^2)] {
       a(1+r+s)^4(1+r)^p(1+s)^q
       + a^2(1+r)^(p+2)(1+s)^q
       + a^2(1+r)^p(1+s)^(q+2) }.

This is bounded by (17), using a<=1. There are finitely many component
choices, and polynomial-Gaussian sums over the two four-dimensional
labels converge. On the omitted-label set r>=N or s>=N, splitting
the exponential in half gives the claimed uniform exponentially small
tail, including derivatives. These observations verify (18).
Taylor expansion at (c,c) then gives (19), with the first-order
operator h_alpha dot partial_x+h_beta dot partial_y. Its remainder
uses the uniform C^2 bound; its derivative comparison uses the
C^1 part of (18). No first-order expansion of the diagonal coefficient
is needed, and the two offsets cannot be replaced by one common offset.

**Five terms, signs and volume normalization.** L152(15) is exact
after deleting only the frozen zero. Its first, second and third
terms divided by a have respectively the factors

    (K-K^0), a^-2 U, a C;
    a K^0, a^-3(U-U^0), a C;
    a K^0, a^-2 U^0, C-C^0.

Every product therefore has exactly the original normalization 1/a.
For the first two terms the bounded normalized factors and
(10),(19),(20) give O(a) errors. For the third, exact frozen parity
removes E_e before any continuum substitution. The retained slope
is bounded; D_e contributes O(epsilon_N) because its two other
normalized factors are bounded. Each insertion divided by a is
M_(t,a):(a^-2 U):(a C), with O(a) error from (10),(19),(21).
The plaquette plus sign 4 tilde b Tr W_4 is minus j_(3,4);
the vertex plus sign 2s sum Tr(C C) is minus j_(6,4), precisely
as in L149(7) and L152(4). Neither sign is changed by calling
these contributions subtractions.

L149(2)'s connected count is twelve: the other three pairings
factor into the removed covariance product. Explicit color indices
remain in its quartic tensor and exterior; no further color factor
three is allowed. Four central-edge types and six types of each
insertion are counted once on their original shifted grids.
Multiplying the finite response by a^3 converts the terms divided
by a into a^4 sums. Their uniformly bounded weighted placement
count turns the per-placement error into C_i(a+epsilon_N).
The resulting five densities are exactly L152(8). All have a
uniform C^1 norm and compact support, so integrating the difference
between a sample and its shifted cell costs O(a) in total.
This proves the claimed comparison with Lambda_i and no other
coefficient. Finally a^-3=N^3/512 converts (1) to (2).

The DAG row already lists the direct inputs used here. No new
dependency, numerical premise or general theorem was introduced.
This is separate verification of an existing local quantitative
input, not a new rate or progress beyond the checked sources.
The failed absolute count and bounded raw-loop premise in
ATTEMPTS/036 and ATTEMPTS/011 are not used. Three other complete
rate blocks, quantitative L011 assembly, interacting reflection
control, continuum axioms and finite positive infrared mass remain
unresolved. Full matching Mathlib coverage remains not checked.

## Mathlib

Full matching theorem and supporting relative-lattice/forest coverage:
**not checked**; unknown availability is not absence. Taylor's theorem
with remainder is used in its standard form, with the precise source
already imported in L222: NIST DLMF, section 1.4(vi), equations
(1.4.35)–(1.4.37), <https://dlmf.nist.gov/1.4#vi>.
The exponential series and finite/infinite bounded spectral calculus
are applied explicitly in (6), not reproved as general theorems.
L151 provides the exact heat identities and full spectral tails;
L150 supplies its quantitative projection-row estimate and signed
parity. The new rate is necessary because those imported results
and L152's qualitative limit do not themselves state (1).
The unchanged source assessment is
`drafts/literature/2026-10-20-quartic-residual-quantitative-remainder.md`.
