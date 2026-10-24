# L271 — Quantitative energy-placement coefficient comparison

## Hypotheses

Use exactly Delta_en and K_(i,en) of L122(6) and L122(2), respectively,
with its real kernels g,p,H,H_N, original fixed shifts h,n, component
selectors, clamped coefficients and both original levels s,t. The
setting is the relative SU(2) cube D=(-4,4)^4, sufficiently fine
admitted even N, a=8/N, tau=1/16, straight lower-rooted direction-1
forest, ordinary stored coordinates and bare small-coupling coefficient
taken at each fixed mesh before refinement. Both actual probes i=3,6,
both Q forms, all ordered generator/path stencils and signs, every
source/end row, upper pin, constant mode and complete heat sum remain.

Import L115's exact energy-placement identity and global clamped
product bounds; L121's kernel/selector definitions; and L270 proof
sections 1, 3 and 5's quantitative joint moments, actual raw-path
C1 comparison/C2 envelopes, and full heat-matrix comparison. These
use L267(1)'s shifted full-matrix decay and the supporting L222/L248
modal, displacement, quadrature and complete probe estimates. Their
analytic and audit qualifications remain. No upstream audit is
performed here. In particular L270's scalar-placement conclusion and
its separate finite-P comparison are not energy-placement estimates.
L122 already uses P_bulk=J_1^*P_inf J_1, a compression.

## Conclusion

For both actual probes there are C_i and a common sufficiently fine
mesh threshold such that

    |Delta_en-a^(-3)K_(i,en)| <= C_i N^(5/2)
                            <= C_i N^(5/2)log(eN)^2.       (1)

The coefficient is exactly L122(2), with the positive (d_m-n_m)
product derivative, physical lower-distance weight and no outside
factor 3. The separate critical audit in proof section 6 accepts this
specialization relative to its imported premises.
It is local standard-method progress under the saved SPECIALIZE
assessment, classified REPRODUCTION, without a novelty claim beyond
the checked sources. The exterior-circulation rate, quantitative L011
assembly, upstream qualifications and interacting/continuum/infrared
construction requirements remain independent gaps. No complete
Yang--Mills candidate or interacting reflected bound is asserted.

## Proof

### 1. Reuse the quantitative joint estimates in the exact trace

Fix all finite stencil labels r,alpha,beta,h,n, write j=t-s,
J=1+|j|, and choose fixed M>=1 exceeding every stencil range.
Set w(d)=M+|d| and use exactly L121's positive majorant

    m_j(d)=||g_(r,j)(d)||_F ||s_alpha(h)||
                         ||p(-d-h+n)||_F ||s_beta(n)||.

Both |H_j(d)| and |H_N(y,d)| are at most m_j(d), including every
partial component selector in L122(5). L270(2)--(6) apply unchanged:
its g,p and all shift matrices are exactly L122's, not different
scalar-placement kernels. In particular

    sum_(j,d) w m_j <= C,
    sum_(|j|>L,d) w m_j <= C(1+L)^(-1/2),
    sum_(j,|d|>R) w m_j <= C(1+R)^(-1/2),              (2)

and, for 0<a<=1,

    sum_(j,d) w min(1,aw) m_j <= C sqrt(a),
    sum_(j,d) w min(1,a|j|) m_j <= C sqrt(a).           (3)

These are finite uniform inequalities before choosing cutoffs. Their
input is ||g_j(d)||_F<=C(J+|d|)^(-4), the shifted unweighted ell2
norm of p, and Cauchy--Schwarz. L270 gives
||w g_j||_2<=C J^(-3/2), ||w^2 g_j||_2<=C J^(-1/2)
and ||1_(|d|>R)w g_j||_2<=C(J+R)^(-3/2).
The spatial clipped sum is bounded by
C sum_j min(J^(-3/2),a J^(-1/2)), split at J=1/a;
the axial sum uses min(1,a|j|)J^(-3/2). Thus (3) does
not sum the divergent J^(-1/2) allowance alone. Constants are
uniform on the fixed stencil list, which is summed at the end.

With all labels retained, L122(6) is the exact finite identity

    Delta_en=a sum_(k,l,s,t,r,alpha,beta,h,n,y,d)
       c_(i;kl,a) min(s,t) b_(r,t)(y) H_N(y,d)
       [psi_st(y+d-n)-psi_st(y)],
    psi_st=phi_(l,alpha,s) phi_(k,beta,t).              (4)

The difference in (4) is the complete product subtraction. Its right
shift is n and its sign is positive. It retains all three terms of
L115(7) jointly, with h still in the projection kernel. No stencil
or component matrix is moved through P_bulk.

### 2. Bound the original remote rows before interior expansion

L115(4) gives, at every original clamped index,

    |psi_st(y+d-n)-psi_st(y)|/a
                                <= C p(k)p(l)w(d),     (5)

where p is a fixed polynomial enlarged when needed. The displacement
is uniformly bounded, and its input support permits at most C N^3
indices y. For fixed j the admitted levels satisfy
sum_t min(t-j,t)<=N^2. Consequently for any offset set E,

    a^3 |Delta_en[E]|
       <= C a^5 N^5 sum_(k,l)|c_(i;kl,a)|p(k)p(l)
                                  sum_((j,d) in E) w m_j. (6)

This is the original trace, with all selectors and end rows present.
The Gaussian envelope L122(10), also L248(11), makes the heat-label
sum finite uniformly in N, and a^5 N^5=8^5.

Let K be one fixed compact interior set containing the supports of
all b_(r,t), all corresponding u_(rho(r)), and their fixed stencil
enlargements for small a. Their existence and common positive
clearance eta follow from L222(4). Choose c>0 so small that the
physical shifts of lattice length cN, and their joining segments,
use less than eta/4 of that clearance. For large N, on

    |d|<=cN, |j|<=cN,                                 (7)

and on the union of the b and u supports, every y+d, y+d-n, y-h
and adjacent stencil row is interior. Both t and s=t-j are
admitted interior levels, and the interval between their physical
positions remains interior. Hence H_N=H exactly there.

Equations (2) and (6) bound the complement of (7) by C_i N^(-1/2)
after cubic normalization. No remote raw coefficient or clamp has
been replaced before this bound. The continuum derivative expressions
used below have magnitude at most C p(k)p(l)w and compact u support;
their restored offset tails obey the same normalized bound, using
a^4 times the C N^4 count of t,y. Compact input has never been
treated as compact energy-kernel output.

### 3. Quantify the complete two-factor product difference

Put xi=(-4+at,(-4,-4,-4)+ay). On the interior region in section 2,
let f_(k,beta,t)(z) be the genuine smooth transverse raw expression
agreeing with phi_(k,beta,t) at the original samples, and similarly
for the l-column. L270(12) supplies

    ||f_(k,beta,t)-phi_(k,beta)(-4+at,.)||_(C_z^1)
                                                    <= C a p(k),
    ||f_(k,beta,t)||_(C_z^2)
          +||phi_(k,beta)||_(C^2(K')) <= C p(k).        (8)

The same holds at s for the l-column. The continuum C2 bound
includes axial and mixed derivatives on a fixed interior enlargement
K'. L270 section 3 obtains the first line by differentiating the
actual one-sided prefix quotient before estimation, using prefix
matching through transverse order 2. Its second line uses the raw
prefix bound through order 3. These are quantitative statements for
all retained modes, not value errors divided by a. All original
signed traversal slots and the length-at constant axial prefix remain.

For clarity define, at fixed original levels,

    q_a(z)=f_(l,alpha,s)(z) f_(k,beta,t)(z),
    q_st(z)=phi_(l,alpha)(-4+as,z)
                                  phi_(k,beta)(-4+at,z),
    v=d-n,
    F_kl(xi;d,n)=sum_(m=2)^4 v_m
                  partial_m(phi_(l,alpha)phi_(k,beta))(xi). (9)

Product differentiation and (8) give C2 bounds C p(k)p(l) for
q_a and q_st, and a C1 matching error C a p(k)p(l). For example
the derivative error is telescoped as
(partial f_l-partial phi_l)f_k
+partial phi_l(f_k-phi_k)
+(f_l-phi_l)partial f_k
+phi_l(partial f_k-partial phi_k),
with both continuum factors at their own levels. Thus both factors
of the product, not just one, are differentiated.

The segment from z to z+av is interior by (7). The integral
difference formula yields

    [q_a(z+av)-q_a(z)]/a
          = integral_0^1 v dot grad_z q_a(z+theta av) dtheta.

Changing the gradient along this segment to its value at z costs
C a p(k)p(l)w^2 by the C2 bound. Independently, the whole
difference and the leading gradient each have size at most
C p(k)p(l)w, so this error also has that bound. Taking the
minimum gives C p(k)p(l)w min(1,aw). Changing the raw gradient
at z to that of q_st costs C a p(k)p(l)w by (8).

Finally change only the continuum l-column's axial position from
-4+as to -4+at. The product derivative changes by at most
C a|j|p(k)p(l)w, using both axial value and mixed-derivative
bounds in (8). Its separate value bound gives C p(k)p(l)w;
the smaller bound is C p(k)p(l)w min(1,a|j|).
It follows for the exact subtraction L_en in (4) that

    |L_en/a-F_kl(xi;d,n)|
       <= C p(k)p(l)w
                   [a+min(1,aw)+min(1,a|j|)].          (10)

This proves the energy-specific quantitative comparison. It does
not transfer L270's different scalar difference. Since
|b_(r,t)(y)-u_(rho(r))(xi)|<=C a by L222(4) with the
original fixed shifts, and both are bounded, replacing b in (4)
adds C a p(k)p(l)w to the same product error. All these statements
hold on the union of their supports; outside it both terms vanish.

Insert (10) and this displacement error into (4) on (7). The count
is the same a^5 N^5 as (6). Equations (2)--(3) followed by the
complete Gaussian heat sum bound their total normalized error by
C_i sqrt(a). All removed original remote rows have already been
bounded with their selectors. No Taylor formula was applied to a
clamp or across the pinned upper forest value.

### 4. Retain the min weight, complete heat sum and cell normalization

After L_en=a(L_en/a), the normalized near derivative trace is

    a^4 sum c_(i;kl,a) [a min(s,t)] u_(rho(r))(xi)
                                      H_j(d) F_kl(xi;d,n). (11)

On the compact support in (7), every t admits s=t-j. Exactly

    a min(t-j,t)=at-a max(j,0).

Replacing this weight by at=x_1+4 costs at most
C min(1,a|j|), since both original weights are bounded. Its
complete contribution is C_i sqrt(a) by (3). Restore all j,d
in the new derivative trace and sum over interior t,y. Its extra
tails cost C_i N^(-1/2) by section 2. Thus, writing D_(i,N) for
the full sum

    a^4 sum_(k,l,r,alpha,beta,h,n,j,d,t,y)
       c_(i;kl,a)(x_1+4)u_(rho(r))(xi)H_j(d)F_kl(xi;d,n),

we have the uniform finite bound

    |a^3 Delta_en-D_(i,N)|
                         <= C_i[N^(-1/2)+sqrt(a)].     (12)

Finite heat coefficients are zero on omitted mesh labels. On retained
labels L248(11), equivalently L270(18), gives for some fixed c0>0

    |c_(i;kl,a)-c_(i;kl)|
             <= C_i a p(k)p(l)exp[-c0(|k|^2+|l|^2)],
    |c_(i;kl,a)|+|c_(i;kl)|
                         <= C_i exp[-c0(|k|^2+|l|^2)]. (13)

The bound is for the triplet's four curvature products and both
polarized shear terms in full. Each omitted pair has an index at
least N, so its indicator is at most (|k|+|l|)/N. Its entire
polynomially weighted Gaussian tail is therefore O(N^(-1)).
Combining (13), (2), the bounded a^4 t,y count and this omitted-label
estimate shows that matching both complete heat matrices and restoring
all continuum labels in D_(i,N) costs C_i a. Constant own-direction
indices have not been omitted.

For each fixed heat and kernel label the function

    (x_1+4)u_(rho(r))(x) F_kl(x;d,n)

has compact support in D and C1 norm at most C p(k)p(l)w(d),
by the continuum C2 bound in (8). L222(5)'s four-dimensional
rectangle estimate costs C a p(k)p(l)w per such label.
Equations (2) and (13) sum this error absolutely to C_i a.
Every endpoint cell is accounted for; compact u makes its boundary
vertex values zero. The cell weight is exactly a^4, obtained from
a^3 times the original outside a and the a in the difference,
with a min(s,t) supplying the physical lower distance.

The resulting integral, after the absolutely convergent offset sums,
is

    sum_(k,l)c_(i;kl) sum_(r,j,m,alpha,beta)
       [sum_(h,n,d)(d_m-n_m)H_j(d)]
       integral_D (x_1+4)u_(rho(r))(x)
                     partial_m(phi_(l,alpha)phi_(k,beta))(x) dx.

The bracket is precisely B in L122(1); this is exactly K_(i,en)
in L122(2). In particular the right shift and plus sign are
unchanged, and no color, orientation, box-length or outside factor
3 has been added. We have proved

    |a^3 Delta_en-K_(i,en)|
                  <= C_i[N^(-1/2)+sqrt(a)+a]
                  <= C'_i N^(-1/2).                    (14)

Multiplication by a^(-3)=N^3/512 proves (1).

### 5. Source specialization, qualifications and traps

The invocation-start assessment is
`drafts/literature/2026-10-24-energy-placement-coefficient-quantitative-remainder.md`.
The primary Green input is imported through L267 and L270:
Lawler--Limic, *Random Walk: A Modern Introduction* (Cambridge, 2010),
section 1.1 pp. 9--11, Proposition 4.2.3 p. 79 and Theorem 4.3.1
pp. 81--83 including its bipartite proof case, in the
[author-hosted text](https://www.math.uchicago.edu/~lawler/srwbook.pdf).
Four-dimensional nearest-neighbor walk has covariance I/4 and
unnormalized Laplacian 8(I-P_walk), so its scalar inverse kernel is
G_walk/8. L267 retains all mixed shifts; no derivative estimate for
the scalar asymptotic remainder is assumed here.

Taylor's theorem with integral/Lagrange remainder is imported from
NIST DLMF v1.2.8 (2026-09-15), section 1.4(vi),
[(1.4.35)--(1.4.37)](https://dlmf.nist.gov/1.4#vi).
The required closed segments lie in the fixed interior region and
the functions are the explicit smooth mode/prefix products with the
derivative bounds (8). There is no reason to reprove that theorem;
the necessary new specialization is the exact product comparison
(9)--(10) and the complete finite accounting against L122(2).

No separate absolute projection/path moment, globally summable second
moment, compact moved output, covariance-source restriction or
projection idempotence is used. The exact original remote trace is
bounded before selector removal. The two physical coefficient levels,
both differentiated product factors, raw one-sided prefix, upper pin,
constant mode, original min weight and every heat label remain until
their controlled comparisons. All inequalities are uniform before
the cN cutoff choice; no varying cutoff enters a qualitative theorem.
ATTEMPTS/030 and ATTEMPTS/032 remain valid stopped shortcuts.
L270's finite-P error is not added: it concerns Delta_sc, whereas
(4) already contains P_bulk. No L220 cancellation, coefficient value,
numerical certificate, new upstream audit or full-response rate is
inferred. The separate critical review of (1) is recorded below.

### 6. Separate critical audit — 2026-10-24

This audit accepts (1), including the stronger bound without a logarithm,
relative to the stated imported premises. No correction, new direct
input or coefficient change is required. The invocation-start gate is
`drafts/literature/2026-10-24-energy-placement-rate-critical-audit.md`:
RESEARCH / REPRODUCTION, actual task proof_audit. This is validation
of a local standard-method specialization, not an upstream audit,
a novelty claim or a complete Yang--Mills candidate. In particular
L267's Green estimate and L222/L248's supporting mode/probe estimates
remain imports; L270's already audited sections 1, 3 and 5 are reused.

**Exact object and selectors.** Subtract L115(2) from L115(14) before
any inequality. If the energy input is y and its output is x=y+d,
the S_alpha and S_beta edge indices are y-h and x-n. Consequently
the projection entry is p(-d-h+n), and the scalar subtraction is
psi(x-n)-psi(y), with a plus sign. This reproduces L122(4)--(6)
including every chi in its (5), rather than only an interior trace.
P_bulk is already in both terms; the additional finite-P error of
L270(7) belongs to a different difference and is not an allowance here.
The three terms of L115(7) are all retained by this single subtraction.

For the finite matrix product each chi is a diagonal contraction.
The Frobenius trace inequality therefore bounds its absolute trace by
m_j(d), with the same bound for H_j. L121(1)'s finite shifts preserve
the L267 decay up to a uniform constant. The weighted squared shell
sums have numerators (q+1)^4 and (q+1)^6 over (J+q)^8, giving
J^(-3) and J^(-1); after square roots these are J^(-3/2) and
J^(-1/2). The spatial tail gives (J+R)^(-3/2). Pairing each with
the shifted unweighted ell2 norm of p proves (2). For spatial clipping,
the same complete sum is bounded by both C J^(-3/2) and
C a J^(-1/2), so their minimum may be summed at J=1/a. The result
is O(sqrt(a)). Axial clipping sums min(1,a|j|)J^(-3/2), also
O(sqrt(a)), including its zero j=0 term. The unsummable second
moment is never used without its clipped alternative.

**Remote rows and clearance.** The product Lipschitz bound is exactly
L115(4), valid at original clamped indices and both original levels.
For fixed j there are at most N pairs s=t-j,t and each min(s,t)<=N;
there are at most C N^3 input y rows. Together with the original
outside a, the difference's a and cubic normalization, the complete
count is a^5 N^5. Thus (6) controls the original remote trace, still
with every component selector, by C_i N^(-1/2) outside the cN region.
This precedes every continuum replacement and every selector removal.

The union of the displacement sample supports and the continuum support
has a fixed interior enlargement by L222(4) and the finite stencil
range. Choose c from its clearance in all four coordinates. On the
near region all shifted transverse endpoints and both axial levels
remain a fixed positive physical distance from every face. Their
segments remain there as well. Thus the actual selectors become the
identity only on this controlled region. The same argument covers rows
where one of b,u vanishes but the other does not. No upper pinned value
is interpolated, and compact input never implies compact energy output.

**Both product derivatives and both levels.** L270(12) applies to
the same raw path scalars, with their original shifts and signs.
Its C1 error uses the differentiated one-sided prefix, whereas its
C2 envelope uses the third transverse derivative of that prefix.
Continuum mixed derivatives follow from partial_1 Phi=A_1. Thus (8)
has precisely the regularity required here, including the length-at
constant axial mode; no derivative bound is inferred from value error.

At the separate original levels, expanding the four-term derivative
telescoping in section 3 gives exactly grad(q_a)-grad(q_st).
It includes both f_l grad(f_k) and grad(f_l) f_k. Its bound is
C a p(k)p(l), while both products have C2 envelope C p(k)p(l).
On the interior segment the integral difference divided by a therefore
has Taylor error C a p(k)p(l)w^2 and independent error C p(k)p(l)w.
Taking the minimum gives the spatial clipped term in (10). Matching
the gradient at y costs C a p(k)p(l)w. Changing only the continuum
l factor from s to t uses both its axial value derivative and its
mixed axial/transverse derivative; this costs C a|j|p(k)p(l)w,
with the independent C p(k)p(l)w bound giving the axial clipped term.
These are all errors in the complete product, not separate discarded
commutators. Multiplying by b and replacing b by u adds O(a) times
the joint weighted majorant. Equations (2)--(3) and the complete heat
sum put their combined cubic-normalized cost at O(sqrt(a)).

**Weight and coefficient.** The exact prefactor after cubic scaling
is a^5 min(s,t)=a^4[a min(s,t)]. For every near offset and supported
t, s=t-j is admitted. The identity a min(t-j,t)=at-a max(j,0)
has error from at bounded by C min(1,a|j|), so (3) gives
O(sqrt(a)). Restoring the full j,d derivative sums then costs
O(N^(-1/2)), by (2), without requiring original levels for the
new auxiliary continuum expression at those restored offsets.

L248(10)--(11) covers exactly the complete triplet average of four
products and both shear polarizations. Its Gaussian-polynomial error
is O(a); every omitted pair has an index at least N, making its
polynomially weighted Gaussian tail O(N^(-1)). All constant indices
remain. The continuum integrand has compact u support and C1 norm
C p(k)p(l)w, so L222(5) bounds the full a^4 quadrature error by
O(a) after the absolutely convergent kernel and heat sums. Summing
(d_m-n_m)H_j(d) gives exactly L122(1)'s B; the integral contains
the derivative of both continuum factors and at=x_1+4. This is
precisely L122(2), without any extra half, color, box-length or factor 3.

The resulting normalized allowance is
C_i[N^(-1/2)+sqrt(a)+a]. With a=8/N and a^(-3)=N^3/512 it gives
the claimed O(N^(5/2)) remainder, hence also the weaker log(eN)^2
budget. No term requiring L270's log(eN)^(3/4) projection allowance
occurs in this exact difference. No signed-growth inference, finite
mode computation or numerical certificate is used. ATTEMPTS/030/032
remain valid stops on their different shortcuts. The primary citations
and their specialization limits remain those in section 5.

PROOF.md and DAG.md are unchanged because neither the argument nor
its direct mathematical inputs changed. This canonical verdict
supersedes their historical pending-audit wording for L271 only.
The exterior-circulation rate, quantitative L011 assembly, upstream
qualifications and interacting/continuum/infrared gaps remain open.

## Mathlib

Full matching energy-placement quantitative rate: **not checked**.
Supporting Fourier Plancherel, Hilbert--Schmidt trace inequalities,
lattice Green asymptotics, Taylor remainder and quadrature coverage:
**not checked**. Unknown availability is not absence. No mathematical
script or numerical evidence supplies the proof.
