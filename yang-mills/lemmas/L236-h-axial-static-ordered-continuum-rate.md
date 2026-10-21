# L236 — Ordered static comparison for the complete H axial generator

## Hypotheses

Use precisely L235's T_(i,ax,N), R_H,ax and L098(2)'s K_(i,ax),
for the actual probes i=3,6. Thus the gauge group is SU(2), the box
is (-4,4)^4 with all-face relative pinned links, the direction-1 forest
is straight and lower-rooted, N is sufficiently large, admitted and
even, a=8/N, tau=1/16, and coordinates are ordinary dimensionless
stored coordinates. Take the bare coefficient at fixed mesh first.
Keep both original generator orientations, every relative end row,
covariance source, allowed constant index and exterior heat label.

Import L095/L098's finite contraction, L088's complete alternating
matrix, L097's Zeta and frozen path symbol, L028's exact forest lift,
and L008's specified smooth displacement. Use only L222's supporting
product-mode estimates (2)--(3) and L224's supporting scalar decay,
nested projection, path-value and heat-coefficient estimates (5)--(13),
with their recorded qualifications. The E response rate and L234's
different H-curvature response rate are not inputs. L235's reduction
is imported; its separate audit is recorded in L235 proof section 5.

## Conclusion

For both actual probes there is a mesh-independent C_i such that

    |a^3 T_(i,ax,N)-K_(i,ax)| <= C_i N^(-1/2),
    |T_(i,ax,N)-a^(-3)K_(i,ax)| <= C_i N^(5/2).        (1)

Consequently L235 gives

    |R_H,ax-a^(-3)K_(i,ax)|
        <= C_i[N^(5/2)+N^2 log(eN)] <= C'_i N^(5/2).   (2)

This meets the approved O(N^(5/2)log(eN)^2) threshold, without evaluating
K_(i,ax) or using cubic-coefficient cancellation. It is a component
estimate only: other L011 rates, the interacting reflected error
<=c_box/2, continuum axioms, infrared control and finite positive mass
remain independent gaps. This is local RESEARCH / REPRODUCTION using
assessed scalar and energy-projection methods, without a claim of
originality beyond the checked sources. The separate critical audit in
proof section 6 accepts this argument and its combination with L235
relative to imported inputs. There is no complete-solution candidate.

## Proof

### 1. Quantitative differentiated coefficients in the actual order

At a fixed axial level write C_N for transverse curl, G_N=Delta_T^(-1),
P_N for the gradient projection, Q_N=I-P_N and
zeta_(k,N)=Zeta_k/a. Let alpha_(k,N)=A_k/a as in L235(18).
L088(3) and C_N P_N=0 give exactly

    alpha_(k,N)=P_N zeta_(k,N)^* C_N+E_(k,N),
    E_(k,N)=P_N F_k Q_N/a,                            (3)

where F_k=Bb^* M_(f_k) Bq-Bq^* M_(f_k) Bb. Stars denote real
adjoints here and complex adjoints in Fourier formulas below.
The Q_N following C_N was removed using C_N Q_N=C_N, not by
commuting a coefficient through Q_N.

For an axial sequence X set

    dot X_s=(X_(s+1)-X_(s-1))/(2a),
    bar X_s=(X_(s+1)+X_(s-1))/2.

Only levels in a fixed interior collar of the displacement support
need these expressions. No value of the forest potential at s=N is
introduced. For one fixed polynomial p, enlarged throughout as needed,

    ||E_(k,N)||+||dot E_(k,N)|| <= C a p(k),
    ||zeta_(k,N)||+||dot zeta_(k,N)|| <= C p(k).       (4)

Here is the derivative specialization, including its error rate.
Let A_(k,a) be L222's smooth physical normalized product mode. The
normalized transverse exterior link, before the fixed Bb/Bq sums,
is L028(9), (11)'s sampled A_(k,a),mu minus the transverse quotient of

    phi_(k,a)(s,y)=a sum_(r=0)^(s-1)
                       A_(k,a),1(-4+(r+1/2)a,y).

Its centered axial quotient is exactly

    dot phi_(k,a)(s,y)
       =[A_(k,a),1(x_1-a/2,y)+A_(k,a),1(x_1+a/2,y)]/2,
       x_1=-4+as.                                    (5)

In particular no error in a prefix value is differentiated. Compare
(5), after its actual transverse quotient, with partial_mu A_(k,1).
The integral formula for a transverse difference and Taylor remainder
give error at most Ca times a fixed C^3 norm of A_(k,a), plus the
C^2 normalization error between A_(k,a) and A_k. The centered axial
quotient of the direct transverse component has the same bound against
partial_1 A_(k,mu). L222(2)--(3) bound all these norms and errors by
polynomials in k, uniformly on the entire retained spectrum. Fixed
endpoint shifts and the Bb/Bq slots change evaluations by O(a p(k)).
Taking one further transverse derivative in these formulas gives a
polynomial Lipschitz bound, using one further fixed mode derivative.
Thus the coefficients of dot zeta_(k,N) differ from those of
z_(partial_1 v_k(x)) by O(a p(k)) at the corresponding physical point.
The coefficients of bar zeta_(k,N) and zeta_(k,N) have the same value
rate against z_(v_k(x)), by L224(12) and their level-difference bound.

All these statements include transverse normal end rows: the finite
quotient uses its two existing endpoints and the exact tangential
sine zeros. Smooth product modes exist on the closed physical box.
The formulas never continue the upper-pinned forest field. The axial
constant mode in (5) contributes its full constant A_1; its prefix
value remains the physical length as times that constant.

Also f_k=C_N(a R_F A_(k,a))=a C_N A_(k,a), since the transverse
prefix is an exact gradient. Consequently ||f_k||_infinity<=Ca^2 p(k)
and ||f_k(s+1)-f_k(s-1)||_infinity<=Ca^3 p(k). Bounded selector
multiplicity proves the E assertions in (4), including dot E.

L008 defines u_a by central differences of the fixed smooth compact
Psi. Regard those same differences as functions of continuous x.
Their integral difference formulas and Taylor remainder show bounded
C^r norms for each fixed r, and ||u_a-u||_(C^r)<=C_r a^2. It follows
that U_s=C_nu^* M_(u_(a,1)(s,.)) C_nu on each component has bounded
norm together with dot U_s, and

    U_s, bar U_s -> u_1(x) diag_nu eta_nu^2,
    dot U_s -> partial_1 u_1(x) diag_nu eta_nu^2       (6)

at the coefficient level with O(a) error, including each fixed
endpoint shift. All three insertions have compact support enlarged
only by a fixed number of mesh steps.

The calculus imports are the previously assessed NIST DLMF, version
1.2.8, section 1.4(vi), (1.4.35)--(1.4.37),
<https://dlmf.nist.gov/1.4#vi>. The functions used are the smooth
product modes and fixed compact Psi, with the required derivatives
bounded above. No derivative of a rough projection is taken.

The exact product identity, including both differentiated factors, is

    dot omega_k=dot(alpha_k U)
                  =dot alpha_k bar U+bar alpha_k dot U. (7)

L235(18), (3)--(7) therefore reduce the normalized static expression to

    -a^4 sum_(k,l)c_(i;kl,N) sum_s
       [ T_N(zeta_l,zeta_k;U_s)/2
        +(as)T_N(zeta_l,dot zeta_k;bar U_s)
        +(as)T_N(zeta_l,bar zeta_k;dot U_s) ]+O_i(a), (8)

where, for two link-to-plaquette path matrices z_l,z_h,

    T_N(z_l,z_h;V)=Tr[G_N C_N^* z_l P_N z_h^* C_N V]. (9)

Indeed Tr G_N<=CN^3 by L095's full transverse shell count. Each
discarded term in (8) contains an E or dot E of norm O(a p), while
all other factors except G_N are bounded polynomially in k,l.
Its trace is at most Ca N^3 p(k)p(l). Multiplication by a^4 and
summation over N-1 levels gives O(a p(k)p(l)). L224(13)'s complete
heat majorant sums it. This retains, rather than freezes away, every
exterior-circulation term. No mass or boundary restriction is used.

### 2. An inverse-curl column on the entire relative space

All operators in this section are transverse and dimensionless.
Write I_j for isometric zero extension of finite relative j-cochains
to full-grid oriented j-cells. L224's checked relative domains give

    I_1 D_N=D_infinity I_0,
    I_2 C_N=C_infinity I_1,                           (10)

including normal end rows. Use the extended finite energy projections
P_N,S_N and their full-grid counterparts P_infinity,S_infinity.
Their ranges are nested, so P_infinity-P_N and S_infinity-S_N are
orthogonal projections. For every edge source b with a fixed physical
buffer from the transverse boundary, the single-edge dipole case of
L224(10) gives

    ||(P_infinity-P_N)e_b||_2 <= C N^(-3/2).          (11)

The same bound holds uniformly for any sources in a sufficiently
small fixed fractional N-neighborhood of b. This uses its remaining
buffer, not a deletion of other sources.

Let g be the scalar three-dimensional full-grid Green kernel in the
normalization Delta=6(I-P_walk), and define

    v_b=C_infinity(g e_b).

The scalar imports are Lawler--Limic, Random Walk: A Modern Introduction
(2010), Theorem 4.3.1, Corollary 4.3.3, pp. 81--84, and Theorem
6.3.8(a), p. 131, in the inspected author-hosted version
<https://www.math.uchicago.edu/~lawler/srwbook.pdf>, as specialized
in L224. The nearest-neighbor walk is symmetric, irreducible and
transient in dimension three. The fundamental kernel and its first
differences give

    |g(y-b)|<=C(1+dist(y,b))^(-1),
    |v_b(y)|<=C(1+dist(y,b))^(-2),  ||v_b||_2<=C.     (12)

This does not identify any finite vector inverse with killed scalar
Green. Fourier Plancherel on the full grid gives
C_infinity^* v_b=Q_infinity e_b, Q_infinity=I-P_infinity.
The multiplier C/lambda defining v_b is square integrable in three
dimensions. The potential g e_b itself need not be in l2.

We prove the specific finite inverse-curl comparison

    || I_2 C_N G_N e_b-v_b ||_2 <= C N^(-1/2).        (13)

Choose chi equal to one in a ball of radius cN about b and zero
outside radius 2cN, with first differences O(1/N). The source buffer
makes chi g e_b an admissible compact finite edge field. The curl
of its discarded tail satisfies

    ||C_infinity[(1-chi)g e_b]||_2^2 <= C/N.          (14)

Specifically the differentiated Green tail is bounded by
C sum_(r>=cN) r^2 r^(-4)<=C/N, while the cutoff derivative contributes
C N^(-2) sum_(cN<=r<=2cN) r^2 r^(-2)<=C/N. Fixed incidence shifts
alter constants only. Cutting off at increasing radii also proves
v_b belongs to the closed full-grid curl range. Best approximation
by the finite curl range implies, with q_b=S_N v_b,

    ||q_b-v_b||_2<=C N^(-1/2).                      (15)

There is a projection correction; q_b is not silently equated with
the finite inverse column. Take the adjoint of the composed identity
(10), obtaining C_N^* I_2^*=I_1^* C_infinity^*. Orthogonality of
v_b-q_b to finite curls gives

    C_N^* I_2^* q_b=I_1^* Q_infinity e_b.

On the finite relative co-closed space the exact Hodge identity is
C_N^* C_N G_N=Q_N. Hence

    C_N^*[C_N G_N e_b-I_2^* q_b]
          =Q_N e_b-I_1^* Q_infinity e_b
          =I_1^*(P_infinity-P_N)e_b.                (16)

The left bracket belongs to im C_N. The smallest nonzero singular
value of C_N^* on that space is at least c/N: its square is a
co-closed edge Hodge eigenvalue, and L095's complete relative spectrum
has lambda>=c/N^2. This spectrum includes normal end edges and
constant own-component indices; there are no relative harmonic
one-forms on this cube. Thus (11), (16) give a bound
CN times CN^(-3/2)=CN^(-1/2) for the bracket. Together with (15)
this proves (13). No forward extension identity for C_N^* was used;
the adjoint identity above is only the adjoint of (10).

### 3. Ordered columns with variable path coefficients

Fix a source center n in the compact support of V in (8), set
x=(-4+as,-4+an), and take edge sources b,c within a fixed lattice
distance of n. They have a uniform transverse buffer. Let z_(h,x)
be respectively z_(v_h(x)), z_(partial_1 v_h(x)), or z_(v_h(x))
when z_h in (8) is zeta_h, dot zeta_h, or bar zeta_h.
Section 1 and L224(12) give bounded path coefficients, bounded fixed
slot multiplicity and, on every present slot at transverse y,

    |coefficient of z_h-coefficient of z_(h,x)|
                  <=Ca p(h)(1+dist(y,n)).           (17)

There is also the uniform bound Cp(h). Regard z_h^* as its full
zero-extended map. Missing finite slots have dist(y,n)>=cN, up to
fixed shifts, since n is buffered. Their frozen coefficients obey
the same bound with adjusted C, since aN=8. Thus (17) on all slots
can be bounded by Cp(h) min(1,a(1+dist(y,n))).

Define the two full-space ordered columns

    L_(l,N;c)=I_1 P_N z_l^* C_N G_N e_c,
    R_(h,N;b)=I_1 P_N z_h^* C_N e_b,
    L_(l,x;c)=P_infinity z_(l,x)^* v_c,
    R_(h,x;b)=P_infinity z_(h,x)^* C_infinity e_b.    (18)

In (18), P_N inside the finite expressions denotes its finite matrix;
elsewhere it denotes its zero extension. We claim

    ||L_(l,N;c)-L_(l,x;c)||_2<=Cp(l)N^(-1/2),
    ||R_(h,N;b)-R_(h,x;b)||_2<=Cp(h)a.              (19)

All four column norms are bounded by the corresponding Cp.
For L, insert successively v_c and z_(l,x)^*. The inverse-column
difference costs Cp(l)N^(-1/2) by (13). The coefficient difference
acting on v_c costs at most Cp(l)sqrt(a), since by (12), (17) its
squared norm is bounded by a constant times

    p(l)^2 sum_(r>=0) min(1,a(1+r))^2/(1+r)^2
                                                      <=Cp(l)^2 a. (20)

Bounded path multiplicity justifies passing from slots to the l2
norm. Here a=8/N. This uses a truncated squared moment, not a false
finite second moment for the inverse-curl column.

For the last projection difference put f=z_(l,x)^* v_c, whose entries
decay at most Cp(l)(1+dist(.,c))^(-2). Split at radius c_1 N small
enough to preserve a source buffer on the near part. Then

    ||f_near||_1<=Cp(l)N, ||f_far||_2<=Cp(l)N^(-1/2).

Apply (11) separately to each near edge source and use the contraction
norm of P_infinity-P_N on the far part. The cost is at most
Cp(l)[N N^(-3/2)+N^(-1/2)]. This proves the L estimate.
Every nonlocal output is included in these norms.

For R, (10) makes C_N e_b exactly the full-grid local curl column.
Its finitely many slots lie near n, so coefficient replacement costs
O(a p(h)). The remaining projection difference is applied to a
bounded finite list of buffered edge sources; (11) gives O(p(h)N^(-3/2)).
Their sum is O(a p(h)), proving the second estimate. Norm bounds
follow at once from these estimates, (12) and the bounded projections.
Thus, without any reordering of variable factors,

    |<L_(l,N;c),R_(h,N;b)>
          -<L_(l,x;c),R_(h,x;b)>|
                         <=Cp(l)p(h)N^(-1/2).       (21)

### 4. Complete compact insertion and the exact frozen density

For every transverse component nu, let

    t_(n,nu)=[e_(n-hat nu,nu)+e_(n,nu)]/2.

These are precisely C_nu^* e_n. The insertion V in (8) is exactly

    V=sum_(n,nu) v_N(s,n) |t_(n,nu)><t_(n,nu)|,      (22)

where v_N is u_(a,1), its centered axial average, or its centered
physical axial quotient. In particular all four endpoint slots of
each term in (22) have coefficient v_N/4. The supports are compact,
and all four slots are present for sufficiently large N. No source
of G_N, P_N or C_N is restricted by (22).

For a rank-one slot |e_b><e_c| in (22), the exact trace (9) is

    <P_N z_l^* C_N G_N e_c, P_N z_h^* C_N e_b>.       (23)

This follows by cyclicity and G_N^*=G_N, with every intermediate
factor in its original order. Apply (21) to (23) and sum the finite
slots. There are O(N^3) centers per level, bounded coefficients, and
N-1 axial levels. Since a^4 N^4 is constant, the error in (8) is at
most CN^(-1/2)p(k)p(l) per heat pair. Replacing the coefficients in
(22) by u_1(x), u_1(x), partial_1 u_1(x), respectively, costs O(a)
in the normalized sum by (6) and the uniform column bounds.

For fixed x the full-grid translated slot density is obtained by
Plancherel. Put

    a_h(x,theta)=P(theta) z_(h,x)(theta)^* C(theta) Q(theta).

Here z_(h,x) is the appropriate value or axial derivative above.
The density of (9), (22) is exactly

    integral_(torus) Re Tr[
        (Q/lambda) a_l^* a_h
          v(x) diag_nu eta_nu^2] dtheta/(2pi)^3.    (24)

The two endpoint averages give eta_nu^2: their /4 weights have not
been replaced by a single endpoint. In (24), C Q=C and Q C^*=C^*,
as in the finite contraction. Plancherel is legitimate for the column
pairing: C g e_c is l2 by (12), and the other column has a local curl
followed by a bounded projection. This is a density per vertex cell,
not the trace of an infinite-volume operator. Fixed staggered phases
cancel in the closed density, with the same z and C as L097/L098.

For the three terms in (8), a_h is respectively alpha_k,
partial_1 alpha_k, alpha_k. Their v are u_1/2, (x_1+4)u_1,
(x_1+4)partial_1 u_1 after including the weights in (8).
Their sum is exactly

    Re Tr[(Q/lambda) alpha_l^*
                 (omega_k/2+(x_1+4)partial_1 omega_k)],
    omega_k=alpha_k u_1 diag_nu eta_nu^2.             (25)

Thus both coefficient derivatives, the kink half and the physical
lower distance as are present. The minus sign in (8) gives precisely
L098(2), with no new factor 1/2, color count or outside factor 3.

### 5. Physical quadrature and every heat label

The column bounds used in (24) also bound each physical first
derivative of its density by Cp(k)p(l), enlarging p to include the
fixed extra mode derivatives. Only smooth coefficient values are
differentiated; the full-grid kernels are fixed. The u and partial_1 u
factors make the density compactly supported in the physical box.
Rectangle quadrature, including all endpoint cells, consequently costs
Ca p(k)p(l). This is the previously assessed first-order Taylor
quadrature consequence used in L222(5). No upper forest value is used.

L224(13) applies to exactly the same actual coefficients here:

    |c_(i;kl,N)|+|c_(i;kl)|<=C_i exp[-c(|k|^2+|l|^2)],
    |c_(i;kl,N)-c_(i;kl)|
        <=C_i a q(k)q(l) exp[-c(|k|^2+|l|^2)].       (26)

It retains the actual triplet products and both shear polarizations.
All preceding estimates have one fixed polynomial label envelope,
independent of N and of the source center. The full sums of those
polynomials against (26) are finite. Omitted continuum labels have
an index at least N, and their polynomial-Gaussian tail is
O_i(exp(-c'N^2)). This separately includes constant component and
axial indices among the retained labels; they have never been deleted.

Equations (8), (21)--(26) give the first estimate of (1). Dividing
by a^3=512/N^3 gives the second. Add L235(3) to get the first bound
in (2); log(eN)/sqrt(N) is bounded for N>=1, giving its second bound.
No mesh-dependent mass, qualitative-limit substitution or coefficient
cancellation is involved. The stronger selected rate is accepted by the
separate audit below relative to imported inputs, without verification
of those inputs or of the complete Yang--Mills argument.

### 6. Separate critical audit, 2026-10-19

**Verdict: accept (1)--(2), relative to L008, L028, L088, L095,
L097, L098, L222, L224 and L235.** The unchanged prior EXPLORE
assessment is
`drafts/literature/2026-10-18-h-axial-complete-rate-critical-audit.md`.
L235's reduction was checked in its proof section 5. Upstream finite
contractions, spectra, scalar decay and modal estimates remain imported.
The present audit checks their applicability and this new inverse-curl,
ordered-column and derivative argument; it is not an upstream reproof.

**Differentiated coefficients and all three terms.** L028(9)--(10),
after division by the stored-field factor a, writes the exterior
coefficient as A_(k,a),mu minus the transverse quotient of phi_(k,a).
At existing interior levels its exact centered axial quotient is

    [phi(s+1)-phi(s-1)]/(2a)
      =[A_(k,a),1(x_1+a/2)+A_(k,a),1(x_1-a/2)]/2.

Taking the transverse quotient commutes with this finite axial
quotient. Its continuum value is partial_mu A_(k,1); subtracting
it from the direct axial quotient gives partial_1 v_(k,mu).
L222(2)--(3) and the integral difference formula give O(a) error
times a fixed mode polynomial. One further transverse derivative
bounds the Lipschitz coefficients in (17). No prefix value error
is differentiated. The constant axial mode contributes its full A_1.
Tangential face samples are the actual sine zeros; normal end links
use their two existing endpoints. The differentiated insertions are
axially interior, so no upper-pinned forest value enters.

In L088(3), P C_N^*=0 and C_N Q=C_N prove (3) exactly. The residual
E comprises both exterior-circulation terms. Transverse curl deletes
the prefix: f_k=O(a^2 p(k)), with axial difference O(a^3 p(k)).
Thus E and dot E are O(a p(k)), with bounded selector multiplicity.
L008's actual u_a is the central difference of fixed smooth compact
Psi. Its continuous difference formula bounds every needed C^r norm
and gives u_a-u=O(a^2) in those norms. This proves (6) slot by slot,
including dot U. The exact product identity

    dot(alpha U)=dot alpha bar U+bar alpha dot U

proves the three ordered terms in (8). Each omitted E term costs
Ca p(k)p(l) Tr G_N per level. Since Tr G_N<=CN^3, multiplying by
a^4 and summing O(N) levels gives O(a p(k)p(l)). This checks (4)--(8)
with both coefficient derivatives and every exterior-circulation term.

**Inverse-curl column on the complete relative domain.** L224 section
3 and its separate audit justify (10): new outside curl rows have
only zero tangential face inputs; normal end rows keep their actual
differences. The adjoint of this composition is exactly
C_N^* I_2^*=I_1^* C_infinity^*. It does not assert an extension
identity for the forward use of the finite adjoint.

For a buffered edge b, its scalar divergence is a bounded two-vertex
dipole. L224(10)'s single-edge specialization therefore gives (11).
All nonlocal output rows are in that norm. The full-grid column
v_b=C_infinity(g e_b) has squared tail at most
C sum_(r>=R)r^2 r^(-4)=O(R^(-1)); Fourier calculus gives
C_infinity^*v_b=Q_infinity e_b. Its potential need not be l2.
Cutting off that potential gives curl-tail energy O(N^(-1)), and
the cutoff derivative contributes
O(N^(-2) sum_(r~N)r^2 r^(-2))=O(N^(-1)). Its support lies inside
the buffered finite relative domain. Best approximation by finite
curls proves (15); increasing cutoff radii separately verifies
membership of v_b in the closed full-grid curl range.

Orthogonality gives C_N^* I_2^* q_b=I_1^* Q_infinity e_b.
Subtracting from C_N^* C_N G_N e_b=Q_N e_b leaves precisely
I_1^*(P_infinity-P_N)e_b in (16), with its stated positive sign.
The bracket is in im C_N. On that space the least singular value
of C_N^* is at least c/N: its square is a co-closed edge Hodge
eigenvalue in the complete relative spectrum. Every edge component
has two positive transverse indices, including normal end rows
and zero own-direction indices; there is no harmonic one-form.
The correction is therefore bounded by CN times CN^(-3/2), not zero.
Together with (15), this proves (13) with all output and source rows.

**Both ordered columns and missing slots.** Telescope the left
column first in C_N G_N, then in its path coefficients, then in P_N.
The first error is O(N^(-1/2)) by (13). The squared coefficient
error is at most

    C p(l)^2 sum_(r>=0) min(1,a(1+r))^2/(1+r)^2
      <= C p(l)^2 a.

Splitting at r of order 1/a proves the last inequality. Missing
finite adjoint path slots lie at distance at least cN from the
buffered center, so their bounded coefficients satisfy the same
bound. No adjoint path-extension identity or finite untruncated
second moment of the inverse-curl kernel is assumed.

The final projection error acts on f=z_(l,x)^*v_c, with decay
O(p(l)(1+r)^(-2)). Its near l1 norm is O(p(l)N), and its far l2
norm is O(p(l)N^(-1/2)). Every near source remains buffered.
Using (11) edge by edge there costs O(p(l)N N^(-3/2)); contraction
of the nested projection difference handles the far part. This
proves the left estimate in (19), including every nonlocal output.
For the right column, (10) exactly extends the local curl C_N e_b.
There are finitely many nearby buffered path slots. Their coefficient
errors are O(a p(h)) and projection errors O(N^(-3/2)p(h)), proving
the other estimate and both norm bounds. Cauchy--Schwarz yields
(21) in the original order, with no coefficient commutation.

**Complete insertion and exact L098 density.** C_nu^* e_n is the
two-edge average t_(n,nu). Hence C_nu^* M_v C_nu has all four slots
with coefficient v/4, exactly (22). Insertion support buffers those
sources; it never restricts covariance outputs. Cyclicity gives
(23) for each slot. There are O(N^3) centers per level and O(N)
levels; after a^4, (21)'s total error is O(N^(-1/2)p(k)p(l)).
The smooth value replacements cost O(a).

In the closed frozen density,
alpha_l^*alpha_h=Q C^* z_l P z_h^* C Q. The identities C Q=C
and Q C^*=C^* identify (24) with the Fourier trace of (9), retaining
the complete path symbols and phases. Both endpoint averages give
eta_nu^2. The three weights from (8) are u_1/2, (as)u_1 and
(as)partial_1 u_1, and their second arguments are respectively
v_k, partial_1 v_k and v_k. Their sum is exactly (25), with
the derivative on the full alpha_k U and ell=as=x_1+4.
Restoring the minus sign and unchanged c_(i;kl) gives L098(2).
The cell normalization is a^4, and the derivative weight is a^4(as).
No new half, orientation/color count or outside factor 3 is present.

**Quadrature, heat and final bound.** Differentiating only the smooth
frozen coefficients bounds the C^1 density by a fixed polynomial in
k,l, since the fixed column kernels have bounded l2 norms. Support
comes from u or partial_1 u. Rectangle quadrature includes endpoint
strips and costs O(a) with that envelope. L224(13), including its
separate modal audit, applies to these same whitened triplet products
and both shear polarizations. Its Gaussian majorant sums every
polynomial error uniformly. Omitted continuum labels have an index
at least N and a separate exponentially small tail; all constant
indices remain among retained labels. This proves (1) for both
probes. L235's accepted O(N^2 log(eN)) reduction then gives (2),
since log(eN)/sqrt(N) is bounded.

This validates the claimed local standard-method rate, without a
claim beyond the checked sources. ATTEMPTS/029, 030, 032 and 045
stop different termwise commutations, varying-mass substitutions,
absolute-moment estimates and rough-prefix Taylor assumptions; none
is used. No numerical premise or script is needed. Full matching
and supporting Mathlib coverage remain not checked. Other component
rates, a complete L011 remainder, interacting reflected error
<=c_box/2, continuum axioms, infrared control and finite positive
mass remain unresolved.

## Mathlib

Full matching ordered-response rate: **not checked**. Supporting
finite Hodge spectral calculus, orthogonal projection best approximation,
full-grid Green differences, trace ideals, Taylor remainder, Plancherel
and polynomial-Gaussian summability: **not checked**. The precise scalar
and calculus imports are cited above; unknown Mathlib availability is
not evidence of absence.
