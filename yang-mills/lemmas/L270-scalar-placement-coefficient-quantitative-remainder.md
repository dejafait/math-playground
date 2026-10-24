# L270 — Quantitative scalar-placement coefficient comparison

## Hypotheses

Use exactly L121's Delta_sc, K_(i,sc) in (3), kernels g and p,
shift matrices s_alpha(h), s_beta(n), selectors H_N and closed scalar
difference L in (10). Keep L113's actual common-index clamped
coefficients. The setting is the relative SU(2) cube (-4,4)^4,
sufficiently fine admitted even N, a=8/N, tau=1/16, the straight
lower-rooted direction-1 forest, ordinary stored coordinates, and
the bare small-coupling coefficient taken at each fixed mesh first.
Both actual probes i=3,6, both residual Q forms, all original ordered
generator/path stencils, coefficient levels, min(s,t), finite middle
P, normal/end rows, upper pin, constant modes and heat labels remain.

Import L121's finite identities and projection comparison, L113's
global clamped value/Lipschitz estimates, L114's full-input projection
estimate, L267(1)'s full Frobenius energy-kernel decay, and the modal,
raw-prefix and complete probe-matrix estimates of L222 and L248.
Their existing analytic and audit qualifications remain; this is not
an audit of those inputs. L269 is not an input for this different
scalar difference. Constants below may depend on fixed stencils,
support clearance and the probe, but never on N, offsets or heat labels.

## Conclusion

For i=3,6 there are C_i and a common sufficiently fine mesh threshold
such that

    |Delta_sc-a^(-3)K_(i,sc)|
        <= C_i N^(5/2) log(eN)^(3/4)
        <= C_i N^(5/2) log(eN)^2.                         (1)

The coefficient is precisely L121(3), including its n_m and
-(d_m-n_m) terms, physical lower-distance weight and no outside
factor 3. The separate critical audit in proof section 7 accepts this
specialization relative to its imported premises, without an upstream audit.
The energy-placement and exterior-circulation rates, quantitative
L011 assembly and interacting/continuum/infrared construction remain
independent gaps. This is local standard-method progress, not a
Yang–Mills solution or a claim of novelty beyond the checked sources.

## Proof

### 1. Quantitative joint tails and clipped moments

All the following estimates hold for each original finite stencil
choice. Their constants can be summed over that fixed list. Put
J=1+|j| and w(d)=M+|d|, where fixed M>=1 exceeds every stencil shift.
L121(1) is a fixed finite sum of spatial translates of e_j multiplied
by fixed matrices. L267(1), with equivalence of Euclidean and sum
norms and a constant allowing all small shifted arguments, gives

    ||g_(r,j)(d)||_F <= C (J+|d|)^(-4).                  (2)

Use L121's positive majorant

    m_j(d)=||g_(r,j)(d)||_F ||s_alpha(h)||
                     ||p(-d-h+n)||_F ||s_beta(n)||.

It bounds both |H| and |H_N(y,d)|, including partial component
selectors. By Fourier Plancherel the norm-one matrix symbol of
P_inf has ||p||_ell2<=C. Translations preserve this norm. Thus for
any nonnegative scalar f(d), Cauchy--Schwarz gives

    sum_d f(d)m_j(d) <= C ||f g_(r,j)||_ell2.            (3)

There are O((q+1)^2) lattice points in the three-dimensional shell
q<=|d|<q+1. Squaring (2) and using w<=C_M(1+|d|) yields

    ||w g_j||_2 <= C J^(-3/2),
    ||w^2 g_j||_2 <= C J^(-1/2),
    ||1_(|d|>R) w g_j||_2 <= C (J+R)^(-3/2), R>=1.    (4)

For the first two statements the shell sums are bounded respectively
by C sum_(q>=0)(q+1)^4/(J+q)^8 and
C sum_(q>=0)(q+1)^6/(J+q)^8. For q<J the sums are at most
C J^5/J^8 and C J^7/J^8. For q>=J they are bounded by the
tails of q^(-4) and q^(-2), giving the same powers. For the third,
(q+1)^4<=(J+q+1)^4 reduces the tail to
C sum_(q>=floor R)(J+q+1)^(-4)<=C(J+R)^(-3).
Taking square roots proves (4), including J=1 and small R.

Combining (3)--(4) and summing positive and negative j proves

    sum_(j,d) w(d)m_j(d) <= C,
    sum_(|j|>L,d) w(d)m_j(d) <= C (1+L)^(-1/2),
    sum_(j,|d|>R) w(d)m_j(d) <= C (1+R)^(-1/2).         (5)

The last sum uses sum_(j in Z)(1+|j|+R)^(-3/2)<=C(1+R)^(-1/2).
For 0<a<=1 define the clipped spatial and axial moduli. Equations
(3)--(4) imply

    sum_(j,d) w(d)min(1,a w(d))m_j(d) <= C sqrt(a),
    sum_(j,d) w(d)min(1,a |j|)m_j(d) <= C sqrt(a).      (6)

Indeed the first left side is at most
C sum_j min(J^(-3/2),a J^(-1/2)). Splitting at J=1/a
gives a sum <=C a(1/a)^(1/2)+C(1/a)^(-1/2).
For the second, use sum_d w m_j<=C J^(-3/2), and split
at the same point. The zero offset contributes zero there.
These are uniform finite inequalities before any mesh-dependent
cutoff is chosen. The second spatial moment in (4) is used only
with the clipped alternative; its axial sum alone diverges.
No separate first absolute moment of p or a projected path is used.

### 2. Retain the original projection error and remove remote rows

Let Delta_sc^bulk be L121(11), obtained by changing only P to
P_bulk in both terms defining Delta_sc. L121 section 2, using
L114 for the collected term and its explicitly localized uncollected
term, already gives the quantitative estimate

    |Delta_sc-Delta_sc^bulk|
                    <= C_i N^(5/2)log(eN)^(3/4).        (7)

Its compact selector restricts only projection-adjacent output rows;
all input rows remain. We import this entire comparison once, before
cutting any offsets, rather than transferring L269's different trace.

Choose a fixed compact set K inside D containing the supports of
every b_(r,t) and the corresponding continuum u_r, with a positive
clearance eta from all faces. This is possible by L222(4) and fixed
stencil enlargement. Choose fixed c>0 small enough that 8c<eta/4.
For sufficiently large N, if |d|<=cN and |j|<=cN, every transverse
point y, y+d, y+d-n, y-h and adjacent stencil endpoint at a
nonzero b or u row is interior. The segments joining these points
stay a fixed positive distance from the transverse faces. Both
levels s=t-j and t and the interval between their physical positions
are also interior. In this region H_N(y,d)=H_j(d), with exactly
the original component matrices and shifts.

For remote offsets retain the original H_N and the original clamped
coefficients. L113's Lipschitz and value estimates give L121(14):

    |L(y,d,n)|/a <= C p(k)p(l)w(d),                    (8)

where p denotes a fixed polynomial, enlarged below as necessary.
There are O(N^3) y rows, and for fixed j,
sum_t min(t-j,t)<=N^2. Hence L121(11) gives, on any offset set E,

    a^3 |Delta_sc^bulk[E]|
       <= C a^5 N^5 sum_(k,l)|c_(i;kl,a)|p(k)p(l)
                            sum_((j,d) in E) w(d)m_j(d). (9)

The complete Gaussian heat majorant makes the label sum finite,
uniformly in N. Since aN=8, (5) bounds the part with |d|>cN
or |j|>cN by C_i N^(-1/2) after scaling. No remote clamped
sample has been replaced by a smooth continuum value in this step.
All finite component/end rows are included in (9).

The same bound applies to the corresponding tails of the continuum
derivative expression and coefficient (3) of L121: their scalar
density is at most C p(k)p(l)w(d), with compact u support. Thus
restoring all offsets at the end also costs C_i N^(-1/2).

### 3. Quantify derivatives of the actual raw path coefficients

This step strengthens the raw-value comparison, rather than assigning
L248(8)'s value error to a difference divided by a. Use its exact
unaveraged formula (4)--(6). At physical axial position x_1=-4+at,
write its smooth transverse prefix as

    F_(k,a,t)(z)=a sum_(ell=0)^(t-1)
                         A_(k,a,1)(-4+(ell+1/2)a,z),
    Phi_k(x_1,z)=integral_(-4)^(x_1) A_(k,1)(v,z)dv.

For r_k=|k|>=sqrt(3), L222(3) supplies at every fixed derivative
order m the bounds C_m r_k^(m-1) for A_(k,a), A_k and
C_m a^2 r_k^(m+1) for their difference. For each transverse
multi-index beta of order q<=2, summing the cell midpoint errors
over the prefix of length at most 8 gives

    ||partial_z^beta(F_(k,a,t)-Phi_k(x_1,.))||_infinity
                      <= C_q(a r_k^q+a^2 r_k^(q+1)).    (10)

In detail, on a cell the integral minus its midpoint sample is at
most C a^2 ||partial_1 partial_z^beta A_(k,a,1)||_infinity.
There are at most 8/a cells. The normalization discrepancy integrated
over length 8 is bounded by 8 C a^2 r_k^(q+1). This proves (10)
uniformly in all existing levels and retained labels. Direct summation
also gives ||F_(k,a,t)||_(C_z^m)<=C_m r_k^(m-1) for m<=3.

The normalized raw positive mu-link is exactly

    v^r_(k,a,mu)(t,z)=A_(k,a,mu)(x_1,z+(a/2)e_mu)
                  -integral_0^1 partial_mu F_(k,a,t)(z+av e_mu)dv.
                                                               (11)

Differentiate (11) in z before estimating. For q=0,1 the error
against partial_z^beta of (A_(k,mu)-partial_mu Phi_k) at (x_1,z)
has the following bounds: the direct midpoint shift costs
C a r_k^q; direct normalization costs C a^2 r_k^(q+1);
shifting the prefix derivative costs C a r_k^(q+1); and
(10) at order q+1 costs C(a r_k^(q+1)+a^2 r_k^(q+2)).
With a<=1 these are all <=C a p(k) for a fixed polynomial.
Differentiating (11) twice and using the direct C^2 and prefix C^3
bounds separately gives ||v^r_(k,a,mu)(t,.)||_(C_z^2)<=C p(k).

Each L113 phi_(k,alpha,t) in the interior is a fixed signed sum
of these raw links at its original shifted transverse points.
The four traversal slots in L248 retain their signs; their continuum
limits are V_mu+V_nu and -V_mu+V_nu, exactly L121's phi_(k,alpha).
Applying the preceding estimates to each slot, including its fixed
shift, therefore proves on the interior segments from section 2

    ||phi_(k,alpha,t)^sm-phi_(k,alpha)(x_1,.)||_(C_z^1)
                                                       <= C a p(k),
    ||phi_(k,alpha,t)^sm||_(C_z^2)
                      +||phi_(k,alpha)||_(C^2(K')) <= C p(k).    (12)

Here sm is the genuine trigonometric/prefix expression agreeing with
the raw samples there, and K' is their fixed interior enlargement.
Continuum axial derivatives use partial_1 Phi_k=A_(k,1), and its
further derivatives; hence the displayed C^2 bound also covers the
mixed axial/transverse derivatives needed to change s to t. For
component-1 axial index zero the prefix is exactly at/sqrt(8) times
its transverse factor and normalization. For other components it is
zero. Thus (10)--(12) retain every allowed constant mode. No value
at the separately pinned upper level N is matched or interpolated.

### 4. Compare the complete scalar difference before summation

Put xi=(-4+at,(-4,-4,-4)+ay) and define

    F_kl(xi;d,n)=sum_(m=2)^4
       [n_m phi_(l,alpha)(xi) partial_m phi_(k,beta)(xi)
        -(d_m-n_m) partial_m phi_(l,alpha)(xi)
                                      phi_(k,beta)(xi)].         (13)

All path and component labels are still present. L121's exact identity is

    L=phi_l,s(y)[phi_k,t(y+d)-phi_k,t(y+d-n)]
       +[phi_l,s(y)-phi_l,s(y+d-n)]phi_k,t(y+d-n).       (14)

On the near offsets use the integral difference formula in each
bracket. Replacing the first derivatives along its segment by those
at y, and its multiplying values by their values at y, costs
C a p(k)p(l)w(d)^2 after division by a, by (12).
The leading raw expression at y has precisely the coefficients
n_m and -(d_m-n_m) in (13). Matching its raw values and derivatives
at their respective levels s,t by (12) costs C a p(k)p(l)w(d).
Changing only the continuum l-column from axial position s to t
costs C a|j|p(k)p(l)w(d), using its axial and mixed derivatives.

For the spatial error a separate bound C p(k)p(l)w(d) follows
from (8) and the first derivative/value bounds for its leading raw
expression. For the axial change the separate value bound gives
the same alternative. Taking the smaller bounds in each step yields

    |L/a-F_kl(xi;d,n)|
       <= C p(k)p(l) w(d)
          [a+min(1,a w(d))+min(1,a|j|)].                (15)

Only actual smooth interior expressions enter this Taylor estimate.
The clipped alternatives make no smoothness claim for boundary clamps.
The displacement estimate from L222(4), with its original endpoint
shifts, is |b_(r,t)(y)-u_(rho(r))(xi)|<=C a. The value bound
for L/a or F is C p(k)p(l)w(d); replacing this displacement
therefore adds only C a p(k)p(l)w(d).

Insert these errors into the exact trace (11) of L121 on near
offsets. Its normalized count is the same a^5 N^5 as (9).
Equations (5)--(6), before the complete heat sum, consequently give
a total normalized error <=C_i sqrt(a). With (9), this proves
the same bound for replacement by the full derivative trace,
apart from the explicitly retained projection error (7).

### 5. Match the original level weight, full heat matrices and quadrature

After L=a(L/a), multiplication of L121(11) by a^3 leaves

    a^4 [a min(s,t)] c_(i;kl,a) u_(rho(r))(xi)
                                         H_j(d) F_kl(xi;d,n).   (16)

For near |j| and nonzero u, the original s=t-j is admitted for
every t on this support by the chosen clearance. Exactly,

    a min(t-j,t)=at-a max(j,0).

Replacing this by at=x_1+4 costs at most
C p(k)p(l)w(d)min(1,a|j|), since both weights are bounded
on the original levels. Equation (6) puts its full normalized
contribution below C_i sqrt(a). This is a uniform error estimate,
not an equal-level identity or a fixed-offset limit at growing j.

For clarity the resulting comparison is the full sum over all
j,d with H_j(d), and over interior t,y of

    a^4 c_(i;kl,a) (x_1+4) u_(rho(r))(xi)
                                         H_j(d) F_kl(xi;d,n).   (17)

Restoring its removed offset tails costs C_i N^(-1/2) by (5),
as already accounted for in section 2. The finite c's vanish on
omitted mesh labels. L248(10), L222(2) and the mean value theorem
for the heat exponential imply for retained pairs

    |c_(i;kl,a)-c_(i;kl)|
        <= C_i a p(k)p(l) exp[-c_0(|k|^2+|l|^2)],      (18)

for some fixed c_0>0, with a polynomial enlarged if necessary.
This is the complete triplet average of four products and both
polarized shear terms, not a selected mode/probe sector. The same
Gaussian envelope bounds both coefficients separately. Each omitted
pair has an index >=N. Its polynomially weighted continuum tail is
O(N^(-1)), since its indicator is at most (|k|+|l|)/N and the
resulting full Gaussian series is finite. Thus coefficient matching
and restoration of all omitted labels in (17) cost C_i a, by (5).
This argument retains constant own-direction modes and all components.

For each pair and offset the physical integrand

    (x_1+4)u_(rho(r))(x) F_kl(x;d,n)

is compactly supported in D and has C^1 norm at most
C p(k)p(l)w(d), by the continuum C^2 bound in (12).
L222(5)'s cellwise quadrature bound therefore costs
C a p(k)p(l)w(d). Multiplying by |H_j(d)|, summing all offsets
using (5), and then all heat labels gives C_i a. The cells are
four-dimensional and the weight is exactly a^4; every endpoint
cell is retained. Summing the integrals gives exactly L121(3),
by (13) and its absolutely convergent definitions of A and B.
No additional orientation, color, half or outside factor 3 appears.

### 6. Error budget, source specialization and limits

The normalized errors a^3 times the original remainder are:

| Comparison | Bound |
| --- | --- |
| Original finite P to compressed P_inf, both terms | C_i N^(-1/2)log(eN)^(3/4) |
| Original remote rows and restored derivative/coefficient tails | C_i N^(-1/2) |
| Interior scalar Taylor, raw derivative and displacement matching | C_i sqrt(a) |
| Separate-level matching and min weight | C_i sqrt(a) |
| Complete heat matrices, omitted labels and a^4 quadrature | C_i a |

Since a=8/N and a^(-3)=N^3/512, this proves (1). All estimates
are uniform before the cN cutoffs are selected; none substitutes
a growing cutoff into L121's qualitative convergence theorem.
The compact input never makes the energy output compact. All remote
selectors were controlled before removal, and the projection comparison
retains all its inputs. The two scalar path differences and projection
commutator have been combined in (14), not discarded separately.

The ready assessment is
`drafts/literature/2026-10-24-scalar-placement-coefficient-quantitative-remainder.md`.
This is RESEARCH / REPRODUCTION under SPECIALIZE. The primary Green
input is imported through L267: Lawler--Limic, *Random Walk: A Modern
Introduction* (Cambridge, 2010), section 1.1 pp. 9--11, Theorem 4.3.1
pp. 81--83 and Proposition 4.2.3 p. 79, in the
[author-hosted text](https://www.math.uchicago.edu/~lawler/srwbook.pdf).
Its symmetric finite-range irreducible bipartite four-dimensional
nearest-neighbor walk has covariance I/4 and unnormalized Laplacian
8(I-P_walk); L267's H=G_walk/8 and all mixed shifts are retained.
No new scalar Green theorem or projection pointwise decay is assumed.

The calculus input is Taylor's theorem with remainder, NIST DLMF
v1.2.8 (2026-09-15), section 1.4(vi),
[(1.4.35)--(1.4.37)](https://dlmf.nist.gov/1.4#vi), reused from
the assessment. All applications are on closed interior segments of
the explicit smooth mode/prefix expressions or the fixed smooth
displacement. The source theorem is not reproved. The needed
specialization is the joint all-offset modulus and derivative matching
of the actual unaveraged raw paths; neither the scalar source nor
L248's raw-value conclusion alone supplies those steps.

L109/ATTEMPTS/032's separate absolute-moment obstruction is avoided by
(3), not contradicted. ATTEMPTS/030's nonuniform fixed-parameter limit
is not invoked. The present component rate does not establish the
two other transverse-H coefficient rates, complete quantitative
response cancellation, an interacting reflected error, or any of
the continuum axioms or finite positive mass requirements.


### 7. Separate critical audit — 2026-10-24

This independent audit accepts (1), including the stronger
log(eN)^(3/4) allowance, relative to the stated imported premises.
No correction, new direct input or changed coefficient is required.
The unchanged gate is
`drafts/literature/2026-10-24-scalar-placement-rate-critical-audit.md`:
RESEARCH / REPRODUCTION, actual task proof_audit. This verifies a
local standard-method specialization, not progress beyond the sources
checked or a complete Yang--Mills candidate. The following checks do
not re-audit L121/L114's projection premise, L267's Green premise or
L222/L248's supporting modal and heat premises.

**Joint shifted moments.** L121(1) has only fixed shifts and bounded
matrices, so L267(1) gives (2) uniformly for signed j, including j=0
and all small shifted arguments. For J>=1, the squared weighted
norms have shell numerators (q+1)^4 and (q+1)^6 respectively. The
split q<J and q>=J gives J^(-3) and J^(-1); their square roots are
exactly the first two bounds in (4). For the spatial tail, the shell
bound is C sum_(q>=floor R)(J+q+1)^(-4), hence
C(J+R)^(-3) before the square root. Fixed shifts of p preserve its
ell2 norm. The Frobenius trace bound holds with each actual diagonal
component selector inserted, since each selector has norm at most one.
Thus (3) applies both to H and to the original H_N.

In particular sum_d w m_j<=C J^(-3/2). For the spatial clipped
modulus the *same complete sum* is at most each of
C J^(-3/2) and C a J^(-1/2), so it is at most their minimum.
Summing at J=1/a gives C sqrt(a). The axial clipped modulus is
bounded by C min(1,a|j|)J^(-3/2) before summation and has the same
bound, with its j=0 term zero. The spatial tail sums to
C sum_j(J+R)^(-3/2)<=C(1+R)^(-1/2); the axial tail sums to
C(1+L)^(-1/2). All estimates concern the joint closed trace.
The divergent sum of J^(-1/2) alone is never used. This avoids,
rather than contradicts, L109/ATTEMPTS/032's factorwise obstruction.

**Projection, original remote rows and clearance.** L121 section 2
already gives the quantitative bound (7) for both defining terms.
Its uncollected trace localizes columns of X F_l^T adjacent to P,
so cyclicity uses the output-restricted row estimate in L114(2),
with every projection input retained. Its count is
(a^(-1))(a^2 N^(3/2))(N^2)log(eN)^(3/4), namely
O(N^(5/2)log(eN)^(3/4)). The collected term has L114(3)'s
same allowance. These are counted together once in (7).

For the original remote offsets, L113(3) applies to the actual
clamped coefficients, not a continuum replacement. The exact closed
difference gives |L|<=C a p(k)p(l)w(d), even with partial end-row
selectors. Multiplying L121(11) by a^3 and counting all y and the
weighted levels gives a^5 N^3 N^2, which is bounded independently
of N. Equation (5) therefore bounds the original remote part by
C_i N^(-1/2) at fixed-clearance cN cutoffs. The derivative trace
and final coefficient have the same tail bound. On the retained
region, either b or u restricts t,y to their common compact
interior enlargement. Choosing c using that enlargement's clearance
puts y+d, y+d-n, y-h and their fixed stencil endpoints, and both
levels t and s=t-j, a fixed physical distance from all faces.
The joining segments remain interior since the box is convex.
Hence H_N=H there. No remote coefficient is smoothed before its
original trace is bounded, and no upper pinned value is interpolated.

**Raw C1 matching and C2 envelope.** The raw quotient is exactly
L248(6), in its stored normalization divided by a. For transverse
order q<=2, a prefix cell error is bounded by
C a^2 r_k^q using L222(3) at order q+1. There are at most 8/a
cells; integration of the normalization difference adds
C a^2 r_k^(q+1). This proves (10), including q=2, uniformly over
all retained labels and existing levels. Direct summation of the
prefix derivatives through order 3 separately gives the polynomial
bounds needed in (11). Consequently differentiating the exact
one-sided integral quotient once uses prefix matching through order
2 and yields O(a p(k)) error; differentiating it twice uses prefix
order 3 only for a polynomial envelope. Neither conclusion is
inferred by dividing a raw-value error by a.

Every signed traversal is a fixed shifted raw link. Their first-two
and second-plus-third sums have limits V_mu+V_nu and -V_mu+V_nu,
with their original signs, as in L121. The finite shifts cost O(a)
with polynomial label weights. The continuum axial and mixed
bounds follow from partial_1 Phi_k=A_(k,1); they require no axial
interpolation of a rough or clamped field. The component-1 constant
mode has the exact length-at prefix, and non-1 components have zero
prefix. These facts verify all parts of (12) actually used below.

**Closed difference and two levels.** Expanding (14) gives exactly
phi_l,s(y)phi_k,t(y+d)-phi_l,s(y+d-n)phi_k,t(y+d-n),
so the leading derivatives have n_m and -(d_m-n_m), with h retained
only in its original projection kernel. Integral differences on the
interior segments cost C a p(k)p(l)w^2 after division by a.
The independent value/Lipschitz bound costs C p(k)p(l)w; taking
the minimum gives the spatial clipped term in (15). Matching raw
values and transverse derivatives at their own levels costs
C a p(k)p(l)w. Changing just the continuum l-column from s to t
costs C a|j|p(k)p(l)w, with a separate C p(k)p(l)w alternative.
This gives the axial clipped term. The raw C2 envelope and continuum
mixed derivatives established above are sufficient for every one
of these estimates. Applying (5)--(6) with the full a^5 N^5 count
makes their total normalized cost O(sqrt(a)). Displacement matching
adds O(a), using only its compact smooth support and original shifts.

**Weights, complete heat matching and normalization.** In L121(11)
the original prefactor is a; L supplies a second a, and a^3 scaling
therefore leaves a^5 min(s,t)=a^4[a min(s,t)]. For near offsets,
every t on the compact support admits s=t-j. The exact identity
for this weight is at-a max(j,0). Its error from at has bound
C min(1,a|j|); paired with w m_j and summed before any limit it is
O(sqrt(a)). The restored remote derivative and coefficient tails
have already been bounded, so no growing cutoff enters a qualitative
fixed-offset theorem.

The two full heat matrices in L248(10)--(11) have Gaussian-polynomial
errors O(a), with the triplet's four products and both polarized
shear terms retained. Each omitted label has an index at least N;
its indicator is at most (|k|+|l|)/N, so its entire polynomially
weighted Gaussian tail is O(N^(-1)). Constant own-direction labels
remain included. The continuum integrand for each offset has compact
u support and C1 norm at most C p(k)p(l)w, so L222(5) gives an
O(a) quadrature error after the complete joint moment and heat sums.
The cell weight is a^4 and at=x_1+4. The resulting integral is
precisely (13) contracted with H: summing n_m H and (d_m-n_m)H
gives L121's A and B, hence exactly L121(3). There is no additional
color, orientation, half, box-length or outside factor 3.

The normalized total allowance is
C_i[N^(-1/2)log(eN)^(3/4)+N^(-1/2)+sqrt(a)+a].
For a=8/N, multiplication by a^(-3)=N^3/512 proves the stronger
bound in (1). The separate weaker log(eN)^2 budget is therefore
also met. This audit needs no mathematical script, finite-mesh
measurement or numerical certificate. PROOF.md and DAG.md are
unchanged because neither the argument nor its direct inputs changed;
this canonical verdict supersedes their historical pending-audit
wording. Energy-placement and exterior-circulation rates, quantitative
L011 assembly, unresolved upstream qualifications and all interacting,
continuum and infrared construction requirements remain open.

## Mathlib

Full matching scalar-placement coefficient rate: **not checked**.
Supporting Fourier Plancherel, Hilbert--Schmidt trace estimates,
lattice Green asymptotics, Taylor remainder and quadrature coverage:
**not checked**. Unknown availability is not absence. No numerical
diagnostic, certificate or mathematical script is used as proof.
