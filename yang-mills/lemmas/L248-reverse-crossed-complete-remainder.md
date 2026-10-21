# L248 — Raw heat matching and the complete reverse-crossed remainder

## Hypotheses

Keep precisely L105--L107's co-closed-base reverse trace R_R, L247(1)'s
F_i^raw, and L245(7)'s continuum density f_(i;epsilon,h,delta). The
group is SU(2), the box is D=(-4,4)^4 with relative all-face boundary
conditions, the forest is lower-rooted in direction 1, N is sufficiently
large and admitted even, a=8/N, tau=1/16, and i=3,6 are both actual
probes. The bare expansion is taken at fixed mesh first. Use ordinary
stored coordinates and the exact raw symbols of L104(4)--(5), as
imported in L107(1). All constant component indices remain allowed.
There is no outside factor 3.

Use L228's extensions only where specified by L247: they preserve the
existing component-link samples. On the fixed compact support of the
raw displacement, and every fixed stencil enlargement of it, these
samples are genuine interior forest links for sufficiently large N.
No choice of extension outside that region enters the density below.
All upstream comparisons and their recorded audit qualifications are
imported; this lemma does not critically audit them. In particular the
supporting modal and probe bounds of L222 are inputs, not its diagnostic
conclusion, and L242--L247 retain their separate-audit qualifications.

## Conclusion

Uniformly for epsilon,h,delta in (0,1],

    |F_i^raw(epsilon,h,delta)
           -a sum_(t=1)^(N-1) sum_(j in {1,...,N-1}^3)
                      f_(i;epsilon,h,delta)(x_(t,j))|
                                                   <= C_i N^2. (1)

The sums and coefficients are exactly those in L247(1) and L245(7),
respectively. At the existing schedule epsilon=N^-1, h=N^(-4/3),
delta=N^(-2/3), it follows that

    |R_R-a^-3 K_(i,R)| <= C_i N^(5/2) log(eN),           (2)

where K_(i,R) is exactly L107(2), including its factor 1/2. This is
stronger than the approved O(N^(5/2)log(eN)^2) component threshold.
The complete finite-mesh heat sum and omitted continuum labels are
included. No sign or evaluation of K_(i,R) is needed.

This is local REPRODUCTION under the unchanged saved reverse-remainder
assessment, without a claim of progress beyond the sources checked.
The separate critical audit in proof section 5 accepts this specialization
relative to its imported inputs; it does not discharge upstream audits.
Other component rates, quantitative
L011 assembly, interacting reflected error <=c_box/2, continuum axioms,
infrared control and finite positive mass remain unresolved. This is
not a candidate solution of the Yang--Mills problem.

## Proof

### 1. Match each raw forest link before taking path combinations

Use the component-labeled relative modes and physical normalization of
L080(4)--(6). For a retained label k put r=|k|>=sqrt(3),

    A_(k,a)=f_k/sqrt(lambda_(k,a)), A_k=f_k/sqrt(lambda_k).

L222(2)--(3) gives, for fixed nonnegative m,

    ||A_(k,a)||_(C^m)+||A_k||_(C^m)<=C_m r^(m-1),
    ||A_(k,a)-A_k||_(C^m)<=C_m a^2 r^(m+1).            (3)

These are bounds for every retained label, not fixed-label limits.
The stored square-root covariance column is a A_(k,a) before forest
retraction, exactly L080(5). Thus there is no additional power of a
in the normalized raw exterior value used in L247.

At interior level t<N, with y a transverse vertex, define the exact
prefix and its continuum counterpart by

    phi_(k,a)(t,y)=a sum_(ell=0)^(t-1)
                    A_(k,a,1)(-4+(ell+1/2)a,y),
    Phi_k(x_1,y)=integral_(-4)^(x_1) A_(k,1)(b,y) db,
    x_1=-4+at.                                         (4)

This is L080(8), not the separately pinned value at t=N. From (3),
or L222(9)'s midpoint estimate before endpoint averaging, for each
transverse beta with |beta|<=1,

    ||partial_y^beta(phi_(k,a)(t,.)-Phi_k(x_1,.))||_infinity
                      <=C[a r^|beta|+a^2 r^(|beta|+1)],
    ||phi_(k,a)(t,.)||_(C_y^2)<=C r.                    (5)

For clarity, the first term is the sum of the midpoint errors over
t intervals of length a: its bound is C a times the supremum of
partial_1 partial_y^beta A_(k,a,1), since ta<=8. The second term
integrates the normalization discrepancy in (3) over length at most
8. The second line follows directly by summing the second transverse
derivatives over that length. Thus (5) does not assume smoothness of
a rough projection or prefix kernel.

For the positive mu-link from y to y+a e_mu, mu=2,3,4, the exact
forest retraction in L028(9) gives its normalized raw value

    v^r_(k,a,mu)(t,y)
      =A_(k,a,mu)(x_1,y+(a/2)e_mu)
             -[phi_(k,a)(t,y+a e_mu)-phi_(k,a)(t,y)]/a. (6)

Indeed divide the stored retraction of a A_(k,a) by a and group
its axial sum into (4). Equation (6) is unaveraged. It is not
L080(9)'s endpoint-averaged diagnostic V_(k,a).

Compare (6) at the common vertex (x_1,y) with

    v_(k,mu)(x)=A_(k,mu)(x)-partial_mu Phi_k(x),          (7)

which is L104(1). The direct term's shift costs C a by the C^1
bound in (3), and its normalization change costs C a^2 r. For the
prefix, its one-sided quotient is the integral average of partial_mu
phi along the link. Changing this average to partial_mu phi(t,y)
costs at most C a r by (5). Changing that derivative to partial_mu
Phi costs C(a r+a^2 r^2) by (5). With a<=1 and r>=sqrt(3),

    |v^r_(k,a,mu)(t,y)-v_(k,mu)(x)|<=C a r^2,
    |v^r_(k,a,mu)(t,y)|+|v_(k,mu)(x)|<=C.             (8)

The value bound is independent of the error bound: the direct term
is bounded by (3), and the prefix quotient is an average of first
transverse derivatives, bounded by 8||A_(k,a,1)||_(C^1)<=C.
The same reasoning bounds the continuum derivative of the prefix.
First physical derivatives of (7) are at most C(1+r), using the
length-8 integral for transverse derivatives and partial_1 Phi=A_1
for the axial derivative. Consequently shifting any common sample
by a bounded number of cells costs at most C a(1+r), and (8), with
an enlarged constant, covers the component shifts in L247's chosen
common-index raw values v_(k,a)(t,j).

This verifies all four traversal slots explicitly. The positive
mu nu path has signed stored values

    a v^r_mu(t,j), a v^r_nu(t,j+e_mu),
                 -a v^r_mu(t,j+e_nu), -a v^r_nu(t,j).

Its first-two-edge sum divided by a therefore matches v_mu+v_nu,
and its second-plus-third sum divided by a matches v_nu-v_mu,
each with error <=C a r^2. The corresponding rough path rows are
exactly b,q of L104(4); hence their frozen stencil is z_v, with
the signs used in L247(1). L247 already estimated the operator error
of replacing the bounded-offset coefficients by these common values.
That error is neither repeated nor omitted here: only its retained
raw values are now compared with (7).

If the own-direction axial index is zero, the prefix in (4) is
exactly (at)/sqrt(8) times its transverse factor and normalization.
If the mode component is not 1, both prefixes vanish. Positive axial
indices are the exact cosine sums of L080(10), also covered by (5).
Thus no constant mode or physical lower distance is dropped. Every
sample used in (6) and its bounded shifts lies in the compact interior
region under consideration; no value at t=N or upper forest jump
is compared with an interior continuation.

Finally L222(4), equivalently L028(4)'s coefficient estimate, gives
for the common raw displacement in L247

    |u_(a,t)(j)-u_1(x_(t,j))|<=C a,
    |u_(a,t)(j)|+|u_1(x_(t,j))|<=C.                   (9)

A bounded sample shift costs O(a); at identical vertices the stronger
O(a^2) estimate applies. Their supports and the finite stencil
enlargements lie in a single fixed compact subset of D. At its rows
the L228 extensions are the original samples, so their arbitrary
values elsewhere have no role in (8)--(9).

### 2. Match both complete heat coefficient matrices

Let r=|k|, s=|l|. Use exactly L080(6)'s coefficients

    c_(i;kl,a)=exp[-tau(lambda_(k,a)+lambda_(l,a))] B_(i,a;kl),
    c_(i;kl)=exp[-tau(lambda_k+lambda_l)] B_(i;kl).

Here B_(i,a;kl)=q_(i,a)(A_(k,a),A_(l,a)), and B_(i;kl) is its
continuum counterpart. L222(7) proves, for both i=3,6,

    |B_(i,a;kl)-B_(i;kl)|<=C_i a(1+r+s)^2,
    |B_(i,a;kl)|+|B_(i;kl)|<=C_i.                     (10)

Its applicability concerns exactly these matrices, without the upper
curvature or diagnostic weight: for i=3 it compares the four separate
curvature products in L008(2)'s average of squares, retaining its 1/4.
For i=6 it compares both terms in the symmetric polarization of the
two clovers, retaining its 1/2 and every alpha and strain component.
The fixed smooth strains, transition region and all incident plaquettes
are those here. L080(6) supplies the exact stored-to-physical conversion;
there is no new probe normalization, selected-sector removal or color
factor in (10). These supporting estimates can therefore be imported
although L222's diagnostic conclusion is a different statement.

Put c0=tau/16>0. The lower spectral bound in (3)'s normalization
and L222(2)'s dispersion estimate give

    |c_(i;kl,a)|+|c_(i;kl)|<=C_i exp[-c0(r^2+s^2)],
    |c_(i;kl,a)-c_(i;kl)|
                  <=C_i a(1+r+s)^4 exp[-c0(r^2+s^2)]. (11)

Indeed the exponential mean value theorem bounds the heat difference
by C a^2(r^4+s^4) exp[-c0(r^2+s^2)]. Telescope it with (10),
using the separate uniform B value bound and a<=1. No convergence
only for fixed pairs is substituted for (11).

### 3. Compare the complete frozen densities without mass loss

Write J_delta(v,v',u;theta) for exactly L247(1)'s two ordered
numerators. Its dependence on v,v',u is bilinear and linear,
respectively. On the entire torus the raw finite stencils satisfy

    ||z_v||<=C|v|, ||w_u||<=C|u|sqrt(lambda),
    ||c||<=C sqrt(lambda), ||tau||=sqrt(lambda),
    ||q_delta||<=1.

Each numerator has two circulations and one each of tau and w.
Thus, retaining the sole q_delta at its original position,

    |J_delta(v,v',u;theta)|<=C |v||v'||u| lambda^2.    (12)

Apply multilinearity and (8)--(9), using their independent value
bounds rather than multiplying two large high-mode error estimates.
For a retained pair and a common cell on the union of displacement
supports, (12) gives

    |J_delta(v_(k,a),v_(l,a),u_a;theta)
              -J_delta(v_k(x),v_l(x),u_1(x);theta)|
                                 <=C a(1+r+s)^2 lambda^2. (13)

At other cells both are zero. Telescope the coefficient as well,
using (11)--(13). Since

    lambda^2/[(lambda+epsilon)(lambda+h)]<=1,

the absolute difference of the pair integrands, including their
coefficients and denominators, is bounded by

    C_i a(1+r+s)^4 exp[-c0(r^2+s^2)].                  (14)

This holds uniformly in every positive mass under consideration;
no inverse alone has been assigned its operator supremum.

The right side divided by a has a finite full mode-pair sum: bound
the polynomial by finitely many coordinate powers and factor the
sum into eight one-dimensional polynomially weighted Gaussian
series, with four choices of component per label. Each converges,
including its allowed zero own-direction index. This proves a
uniform O_i(a) error after integrating over the normalized torus
and summing every retained pair.

For omitted continuum pairs, at least one index is >=N, so r+s>=N.
The continuum pair integrand is at most C_i exp[-c0(r^2+s^2)] by
(8),(9),(11),(12). Its entire omitted sum is consequently at most

    (C_i/N) sum_(all k,l)(r+s)exp[-c0(r^2+s^2)]<=C_i'/N. (15)

The same eight-series argument verifies finiteness. This includes
all allowed constant indices; none is called an omitted zero mode.
Because a=8/N, (14)--(15) give an O_i(a) error in the full local
density. There are at most C N^4 common cells on the union of
supports. The prefactor of F_i^raw is a/2, exactly matching the
half in f. For sufficiently large N those cells have t,j in
{1,...,N-1}; all other infinite-grid terms vanish. Hence

    |F_i^raw-a sum_(t,j) f_(i;epsilon,h,delta)(x_(t,j))|
                                <=C_i a^2 N^4<=C_i' N^2,

which is (1). This count retains the entire axial level sum, not a
single-slice normalization. No spatial quadrature has been applied
to the raw samples.

### 4. Assemble only the reverse component

L245(14)--(16), with its exact identification (15) of the zero-mass
density integral as L107(2), gives

    |a sum_(t,j) f_(i;epsilon,h,delta)(x_(t,j))-a^-3 K_(i,R)|
                         <=C_i[N^2+N^3(epsilon+h+delta)]. (16)

This follows from a sum f=a^-3(a^4 sum f); the physical integral
of f at zero mass has precisely L107's 1/2. We compare directly
with that sampled density, so L245(2)'s finite axial expression is
not identified with L247's half-summed one. Its endpoint difference
is unnecessary in (16). The actual finite axial tail has already
been bounded in L247(2); no endpoint error is deleted.

At epsilon=N^-1, h=N^(-4/3), delta=N^(-2/3), (16) is
O_i(N^(7/3)), while (1) is O_i(N^2). Import L247(3), which
includes the complete inverse/projection, boundary, axial and
transverse comparisons once, with error O_i(N^(5/2)log(eN)).
The triangle inequality proves (2). Every estimate receiving this
schedule is a uniform finite inequality. No fixed-mass limit is
evaluated at varying mass, no R_L bound is transposed, and the
gradient-base G_R is not substituted for R_R.

The achieved error is only for this component. It neither audits
the imported comparisons nor establishes a quantitative remainder
for all of L011, an interacting reflected bound or a continuum
theory. The original proof was submitted for separate review; section 5
records that review without changing the estimates or imported premises.

### 5. Separate critical audit, 2026-10-19

The audit accepts (1)--(2) relative to the hypotheses above. It checks
the new raw/heat specialization and assembly, not L247's ordered trace
comparison or L245's underlying coefficient theorem. In particular
L242--L247 keep their independent audit qualifications. No new exponent,
coefficient evaluation, or full-response conclusion is established.

**Raw normalization, signs and support.** L080(5) gives the ordinary
square-root covariance column as a A_(k,a), not A_(k,a) or a^2 A_(k,a).
Substitution into L028(9), followed by division by a, gives exactly

    A_(k,a,mu)(x_1,y+a e_mu/2)
       -sum_(ell<t)[A_(k,a,1)(x_(ell+1/2),y+a e_mu)
                                  -A_(k,a,1)(x_(ell+1/2),y)].

This is (6), since phi in (4) contains one factor a. The minus sign
therefore agrees with L104(1). With positive plane orientation, the
four signed links are respectively +mu at j, +nu at j+e_mu, -mu at
j+e_nu and -nu at j. Their first/second and second/third sums yield
v_mu+v_nu and v_nu-v_mu. On rough variables their rows are precisely
b=e_mu^T+exp(i theta_mu)e_nu^T and
q=-exp(i theta_nu)e_mu^T+exp(i theta_mu)e_nu^T. Thus the exterior
contraction is (v_mu+v_nu)q-(v_nu-v_mu)b, the z_v in L107(1), with
no transpose or traversal sign change.

For transverse derivatives of order beta=0,1, the prefix quadrature
cost is C a r^beta and the normalization cost is C a^2 r^(beta+1).
The quotient-versus-derivative error is bounded by
a sup|partial_mu^2 phi|<=C a r. Together with the direct sample
shift, these give C(a+a^2 r+a r+a^2 r^2)<=C' a r^2. The value
bound instead follows directly from the length-8 prefix of bounded
first derivatives. It therefore remains uniform for modes with
a r^2 large. The continuum neighbor-shift bound uses C(1+r), so
bounded component-grid offsets do not change this conclusion.
The axial constant mode has the exact prefix at/sqrt(8), with its
transverse factor and normalization retained; other component modes
have zero prefix. Only displacement-supported cells and fixed stencil
enlargements are compared. Their physical clearance excludes the
separately pinned upper value and every ambiguity in the extensions.

**Both complete probe matrices.** Writing F^a_k=d_a A_(k,a), the
actual bilinear polarizations from L008(2),(6) are

    B_(3,a;kl)=(a^4/4) sum_(x,mu<nu)
        (w_(a,mu)+w_(a,nu))(x) sum_(p in C_(mu nu)(x))
                                             F^a_(k,p) F^a_(l,p),
    B_(6,a;kl)=(a^4/2) sum_(x,mu<nu,alpha) s_(a,mu nu)(x)
        [bar F^a_(k,mu alpha) bar F^a_(l,nu alpha)
                        +bar F^a_(l,mu alpha) bar F^a_(k,nu alpha)].

L222(6)--(7) applies to exactly these forms: all four products in
the first line and both placements in the second remain, with the
antisymmetric curvature convention, all alpha values and the full
strain transition region. The continuum versions replace the
averages by their same-point curvatures and a^4 sum by the integral.
No diagnostic-sector cancellation from L080's conclusion is imported.
L080(6) identifies these B entries with the heat coefficients of the
stored trace, so their application supplies neither an extra color
factor nor a changed field normalization.

The lower dispersion bound is r^2/16, and the eigenvalue discrepancy
is C a^2 r^4. Thus the exponential mean value estimate uses
min(lambda_(k,a)+lambda_(l,a),lambda_k+lambda_l)
>= (r^2+s^2)/16. Together with the independent B value bound it gives
exactly the Gaussian envelope (11). In particular no high-mode error
is substituted for a value bound in a product. The full polynomial
envelope is summable over two four-index labels and their component
choices. Omitting any continuum label outside the finite mesh forces
r+s>=N; multiplication by (r+s)/N bounds its entire tail as in (15).
Allowed own-direction zero indices are present in the retained and
continuum sums, while the other three positive indices prevent an
all-zero eigenvalue. These facts justify the complete heat sum before
any mesh limit or choice of masses.

**Uniformity in the three masses.** The two ordered numerators are

    tr[c* z_v tau w_u* q_delta z_v'* c],
    tr[c* z_v tau w_u* c* z_v'].

Each has exactly two c or c* factors, one tau and one w_u. The raw
w_mu=-u[(1+exp(i theta_mu))/2] i sin(theta_mu) satisfies
||w_u||<=C|u|sqrt(lambda), since |sin(theta_mu)|<=|tau_mu|.
Also ||c||<=C sqrt(lambda), ||tau||=sqrt(lambda),
||z_v||<=C|v| and ||q_delta||<=1. Fixed matrix dimension therefore
gives (12) for each word in its original order, with lambda^2 and
no h, epsilon or delta loss. Multilinear telescoping uses two
uniform values and one error in each term; the coefficient
telescoping uses the same uniform numerator bound. Dividing by
(lambda+epsilon)(lambda+h) leaves the summable envelope (14).
At lambda=0 the specified value affects no integral. The argument
does not commute q_delta or use it as an idempotent matrix.

**Half, cell count and exact subtraction.** After both heat sums,
including the omitted continuum labels, the difference before the
common half has size C_i a at every supported cell. The common
prefactor is a/2 in L247(1), whereas L245(7) puts the same 1/2
inside f. At most (N-1)^4 cells contribute. The total error is
therefore C_i a^2 N^4=O(N^2), proving the audited count in (1).
All cells outside the union of the two compact displacement supports
have zero numerator; support differences do not delete any cell.

For the remaining comparison the imported L245(14)--(16) apply
directly to a sum f=a^-3(a^4 sum f). Its zero-mass integral is
L107(2), with exactly one half. In its identifying algebra,
alpha_k*=c* z_k p and beta_l=q0 z_l* c-c* z_l q0; using p tau=tau
and q0 c*=c* gives the two displayed numerators with their original
minus sign. This checks the precise functional being subtracted,
not merely a coefficient with a similar name. L245's finite axial
expression (2) is not substituted for L247(1), and its endpoint
comparison is unnecessary here. L247(3) already retains its own
finite axial tail and is used once.

At the stated schedule the three error allowances are O(N^2),
O(N^(7/3)) and O(N^(5/2)log(eN)). Their sum proves (2), below the
requested O(N^(5/2)log(eN)^2) threshold. Every mass-dependent
inequality is uniform before substitution. This audit uses neither
an R_L transpose estimate nor a fixed-mass limit at varying mass.
No first failed assertion was found within this specialization.
The accepted input remains conditional on all explicitly imported
upstream estimates; the independent interacting and construction gaps
are unchanged.

## Mathlib

Full matching raw-heat comparison or complete reverse-crossed remainder:
**not checked**. Supporting finite-difference calculus, exponential
mean value bounds, Gaussian-series summability and finite-dimensional
trace/norm coverage: **not checked**. Unknown is not absence.
The calculus input is the Taylor theorem already cited in L222,
NIST DLMF version 1.2.8, section 1.4(vi), (1.4.35)--(1.4.37),
<https://dlmf.nist.gov/1.4#vi>. Its smoothness hypotheses hold for
the finite trigonometric modes and the fixed smooth cutoff on every
compact stencil interval. That source and the approved assessment
are reused without a new retrieval. No reproof of Taylor's theorem
or general literature decay theorem is needed; the raw unaveraged
specialization and full heat/normalization count are proved above
because no matching theorem was identified in the saved assessment.
