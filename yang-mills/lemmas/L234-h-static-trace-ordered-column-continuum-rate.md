# L234 — H static-trace continuum rate by ordered column comparison

## Hypotheses

Use exactly L097's finite static expression (4), denoted T_(i,N) in
L233, and its continuum functional K_(i,Q) in (5). The setting is the
SU(2) relative all-face pinned cube (-4,4)^4, the straight lower-rooted
direction-1 forest, sufficiently large admitted even N, a=8/N,
tau=1/16, ordinary stored coordinates and actual probes i=3,6. The
bare small-coupling coefficient is taken at fixed mesh first. All
relative end rows, interior axial levels, constant component modes,
both clovers and the complete exterior heat sum are retained.

Write P_N=P and S_N=S_T for L097's transverse gradient and curvature
projections, and zeta_(k,N)=Zeta_k/a. Import L224 sections 2–4 and
their separate audit for the same relative transverse cube: nested
zero-extended energy projections, dipole column decay, buffered
projection-column errors, and the actual Bb/Bq coefficient and heat
estimates (12)–(13). These are the same Zeta and c_(i;kl,N) as here.
Its cumulative E insertion, dipole decomposition and E rate are not
inputs. L008 specifies the actual curvature forms; L028(4) gives
their compactly supported coefficient consistency. L097's inherited
finite contraction and spectral hypotheses remain imported; this
proof does not recursively audit them.

## Conclusion

For both actual probes, uniformly for sufficiently large admitted N,

    |T_(i,N)-a^(-3)K_(i,Q)| <= C_i N^2.              (1)

This meets the approved N^(5/2)log(eN)^2 threshold. With L233,

    |R_H,Q-a^(-3)K_(i,Q)| <= C_i N^(5/2).            (2)

The positive-definition R_H,Q still enters the assembled H component
with a minus sign. No coefficient value or cancellation is required
for (1)–(2). This is a RESEARCH / REPRODUCTION specialization under
the pre-invocation EXPLORE assessment
`drafts/literature/2026-10-18-h-curvature-static-continuum-rate.md`.
It is local progress using assessed methods, without a claim of
originality beyond the sources checked. The separate critical audit in
proof section 5 accepts this rate relative to the stated imported inputs.
Other L011 rates, its complete remainder,
interacting reflected error <=c_box/2, continuum axioms, infrared
control and finite positive mass remain unresolved. There is no
complete-solution candidate.

## Proof

### 1. Available column estimates and the precise ordered quantity

Extend each finite transverse relative cochain space isometrically by
zero into its full-grid oriented-cell space. All finite operators below
mean their zero-extended versions. L224's relative boundary check
intertwines the forward gradient and curl, including normal end rows;
it makes no analogous assertion about their adjoints. Their ranges
are subspaces of the corresponding full-grid energy ranges. Thus

    P_N P_infinity=P_N, S_N S_infinity=S_N,
    E_N=P_infinity-P_N, F_N=S_infinity-S_N

are orthogonal projections and have norm at most one. Uniformly for
unit edge sources e_b and plaquette sources e_p a distance at least
b_0 N from every transverse face, with any fixed b_0>0, L224 gives

    ||E_N e_b||_2+||F_N e_p||_2 <= C_(b_0) N^(-3/2). (3)

For the first bound choose L224's path j_d to be the single oriented
edge b, whose divergence is the corresponding endpoint dipole. The
second is L224(11). Its proof allows any buffered source, not only
the E insertion centers: the cutoffs fit into a ball whose radius is
a fixed fraction of that buffer. This is the only specialization of
the source locations in (3).

In particular, uniformly in the component and center p,

    |(S_infinity e_p)(y)| <= C(1+dist(y,p))^(-3),
    sum_y (1+dist(y,p))^2 |(S_infinity e_p)(y)|^2 <= C. (4)

The scalar input for (3)–(4), already specialized and audited in
L224, is Lawler–Limic, *Random Walk: A Modern Introduction* (2010),
Theorem 4.3.1 and Corollary 4.3.3, printed pp. 81–84, and Theorem
6.3.8(a), p. 131, in the inspected author-hosted version
<https://www.math.uchicago.edu/~lawler/srwbook.pdf>.
Here the three-dimensional nearest-neighbor scalar operator is
Delta=6(I-P_walk). L224 applies harmonic first differences to each
dipole potential to obtain the mixed differences in (4), and cuts
off those potentials in gradient or curl energy for (3). No scalar
Green theorem or relative projection estimate is reproved here.

For a fixed axial level s and heat pair k,l, set

    A_(k,N)=P_N zeta_(k,N)(s)^* S_N.

This is a map from transverse plaquettes to transverse links, with
norm <=Cp(k), for one fixed polynomial p. L097(18) is exactly

    a^3 T_(i,N)=sum_(k,l)c_(i;kl,N) a^4 sum_(s=1)^(N-1) (as)
                                  Tr[A_(k,N) M_T(s) A_(l,N)^*]. (5)

The trace here is on the link space. Cyclicity can equivalently put
it on the plaquette space. Both S factors, both P occurrences and
the indefinite M_T remain in their original order.

### 2. Localize the ordered column at the insertion, not at its output

Let n be a vertex in the fixed stencil enlargement of the strain
support at level s, and x=(-4+as,-4+an). All plaquette sources p
within a fixed lattice distance of n have a transverse buffer b_0 N
for some b_0>0, uniformly in s and N large. Put z_(k,x)=z_(v_k(x)),
the constant path operator of L097(5), and

    A_(k,x)=P_infinity z_(k,x)^* S_infinity.

We claim, uniformly for all these sources and all retained labels,

    ||A_(k,N)e_p-A_(k,x)e_p||_2
        <=C p(k)[a+N^(-3/2)log(eN)] <= C' a p(k).   (6)

For clarity the complete telescoping identity is

    A_(k,N)e_p-A_(k,x)e_p
      =P_N zeta_(k,N)^*(S_N-S_infinity)e_p
       +P_N(zeta_(k,N)^*-z_(k,x)^*)S_infinity e_p
       +(P_N-P_infinity)z_(k,x)^*S_infinity e_p.     (7)

The first term has norm <=Cp(k)N^(-3/2) by (3) and the full operator
bound on zeta. No restriction is placed on its output or input rows.

For the second, write the path matrix as a finite list of incidence
slots connecting edge b to plaquette y, with dist(b,y)<=r_0 fixed.
Every slot has bounded multiplicity. On finite rows L224(12) gives
coefficient error <=Ca p(k)(1+dist(y,n)) relative to z_(k,x),
including its O(a p(k)) modal value error. The coefficient of the
adjoint is the same slot coefficient, now in the transposed slot;
no derivative or smoothness of a projection is involved. A slot
missing from the finite matrix is near or outside a physical face.
If it contributes to this comparison then dist(y,n)>=cN for a fixed
c>0, up to the bounded path offsets. Its frozen coefficient is
bounded by Cp(k), which is also <=C'a p(k)(1+dist(y,n)), since aN=8.
This accounts for missing edge inputs and plaquette outputs even
though no adjoint extension identity is assumed. Applying the finite
slot multiplicity inequality and (4) gives

    ||(zeta_(k,N)^*-z_(k,x)^*)S_infinity e_p||_2
                                                        <=Ca p(k). (8)

For the last term of (7) set f=z_(k,x)^*S_infinity e_p. Since z_(k,x)
is a fixed finite-range operator,

    |f(b)|<=Cp(k)(1+dist(b,p))^(-3).

Split f into edges within distance c_1 N of p and the complement,
where c_1>0 is chosen small enough that all near sources retain a
uniform buffer. The three-dimensional shell counts give

    ||f_near||_1<=Cp(k)log(eN),
    ||f_far||_2<=Cp(k)N^(-3/2).

Apply (3) separately to every near edge source and use ||E_N||<=1
on the far part. This yields

    ||(P_N-P_infinity)f||_2
                             <=Cp(k)N^(-3/2)log(eN). (9)

The cutoff is applied only to this error estimate; every finite
boundary source remains in (5). Equations (7)–(9) prove the first
inequality in (6). The second follows from boundedness of
log(eN)/sqrt(N) and a=8/N. Both column norms are <=Cp(k), independently
of N. Consequently, for any two sources p,q in the same bounded
stencil about n,

    |<A_(l,N)e_q,A_(k,N)e_p>
         -<A_(l,x)e_q,A_(k,x)e_p>| <=Ca p(k)p(l).   (10)

This compares the complete ordered columns. It neither commutes a
coefficient through P nor requires a first absolute kernel moment.

### 3. Expand the complete local M_T, keeping both clovers

The exact finite-range insertion may be written

    M_T(s)=sum_n sum_(t in J) m_(t,N)(s,n)
                       |e_(n+r_t,alpha_t)><e_(n+t_t,beta_t)|. (11)

Here J is fixed and finite, independent of N. Repetitions are allowed
and are summed with their actual signs. The following explicit rule
specifies all terms and their normalizations directly from L008(2).
Only transverse curvature inputs are kept, as in L097:

* For each transverse plane mu<nu, take its four plaquettes through n.
  For each take the diagonal rank-one matrix with coefficient
  (w_(a,mu)+w_(a,nu))(s,n)/4. This is the average of four squares.
* For each 2<=mu<nu<=4 and alpha in {2,3,4} distinct from mu,nu,
  take the four positively oriented plaquettes through n in plane
  {mu,alpha} and the four in plane {nu,alpha}. For every pair p,q
  include both |e_p><e_q| and |e_q><e_p|, each with coefficient
  s_(a,mu nu)(s,n) sigma_(mu alpha)sigma_(nu alpha)/32, where
  sigma_(ij)=1 for i<j and -1 for i>j. The factor is (1/2)(1/4)^2.

Terms with an axial curvature input vanish under the transverse
restriction; alpha=mu or nu has a zero curvature entry. These rules
exhaust M_T. In particular the shear is not replaced by a pointwise
product of unaveraged curvatures. The offsets in (11) are bounded.
All nonzero coefficients and their corresponding rows have a fixed
physical buffer for large N, by L028(4) and the compact cutoff in L008.

Let m_t(x) be exactly the same coefficients with w_a,s_a replaced by
w,s. Uniformly in s,n,t,

    |m_(t,N)(s,n)-m_t(x)|<=Ca^2,
    |m_(t,N)(s,n)|+||m_t||_(C^1)<=C.                (12)

Both families vanish outside one fixed compact interior set, enlarged
by the finite stencils. No sign condition on these coefficients is
needed. Include every n in the union of these supports when using
(12), even where one of the two coefficients is zero.

For a rank-one term in (11), the exact trace in (5) equals

    m_(t,N)(s,n)<A_(l,N)e_(n+t_t,beta_t),
                           A_(k,N)e_(n+r_t,alpha_t)>.

There are O(N^3) such centers at each level and only finitely many
slots per center. Apply (10) before summing and then (12). Translation
invariance of A_(k,x) makes the resulting frozen density

    H_kl(x)=sum_(t in J) m_t(x)
       <A_(l,x)e_(t_t,beta_t),A_(k,x)e_(r_t,alpha_t)> (13)

independent of the integer center. The per-level trace error is at
most Ca N^3 p(k)p(l), not a count of all pairs of nonlocal rows.
All those rows were already included in the column norms.

### 4. Actual heat coefficients, quadrature and density identification

The coefficients here are precisely L224(13)'s c_(i;kl,N) and c_(i;kl),
with the same Bb/Bq exterior paths. In particular, for fixed polynomials
p,q and c>0, uniformly on retained labels,

    |c_(i;kl,N)|+|c_(i;kl)|<=C_i exp[-c(|k|^2+|l|^2)],
    |c_(i;kl,N)-c_(i;kl)|
        <=C_i a q(k)q(l) exp[-c(|k|^2+|l|^2)].      (14)

This imported modal estimate includes normal transverse end edges,
both actual probe forms and the constant axial prefix. All errors
above have polynomial label dependence, so they can be summed against
(14). The estimates also hold when their high-label upper bound is
larger than one; no label-dependent localization radius is chosen.

Since a^4 sum_s(as)N^3<=C, equations (5), (10)–(14) show that replacing
the normalized full static trace by

    sum_(retained k,l)c_(i;kl) a^4 sum_(s,n)(as)H_kl(-4+as,-4+an)

costs at most C_i a. In particular the axial distance is as, and no
factor 3, color multiplicity or cell-volume correction has been added.

The physical modes and their lower-prefix integrals defining v_k
are smooth on the closed box, with polynomial C^1 bounds, including
axial derivatives and the constant axial mode. Therefore

    ||H_kl||_(C^1)+||H_kl||_infinity<=Cp(k)p(l).

This follows directly from (13), the bounded full-grid projections
and the finite path operators; it does not differentiate their
singular Fourier symbols. Compact strains make H_kl compactly
supported. Rectangle quadrature for (x_1+4)H_kl on the fixed box
has error <=Ca p(k)p(l). The omitted axial endpoint strips have
width O(a) and bounded density (and, for this insertion, zero
density eventually by compact strain support). No forest value at
the upper pin s=N is used. Transverse boundary strips are treated
the same way. Omitted continuum heat labels have an index at least
N; their full exponential-polynomial tail is O_i(exp(-c'N^2)), hence
O_i(a). This proves the complete normalized error is O_i(a).

It remains to check which continuum coefficient has been obtained.
For fixed x, sum the translated constant-coefficient slots in (11)
to get a full-grid convolution operator m_x. Its centered Fourier
symbol is exactly

    m_T(x,theta)=W_T(x)+C_T(theta)^* S_6,T(x) C_T(theta).

The four diagonal triplet slots add to W_T. Each shear clover gives
eta_mu eta_nu on its own side of the polarized strain form, by the
sixteen pairs in (11); the two transpose slots implement S_6,T.
These are the exact frozen symbols checked in L097 section 5.

By full-grid Plancherel and the finite sum over slots, (13) is the
trace density per vertex of A_(k,x) m_x A_(l,x)^*. Its value is

    integral_(torus) Tr[P z_(v_k(x))^* S m_T(x,theta)
                              S z_(v_l(x))P] dtheta/(2pi)^3. (15)

Indeed the Fourier transform of each source e_(r,alpha) contributes
its translation phase; summing the rank-one slots produces m_T
in exactly that position. Unitary staggered component phases cancel
in the closed trace. The projections have norm at most one, so all
integrals are absolutely finite; values at theta=0 are immaterial.
No infinite-rank operator trace is used without this density
interpretation. Multiplying (15) by x_1+4, integrating and taking
the full heat sum gives precisely L097(5), with the k,l orientation
in (5) unchanged. Thus

    |a^3 T_(i,N)-K_(i,Q)|<=C_i a.

Division by a^3 yields (1), since a^-2=N^2/64. The triangle inequality
with L233's accepted dynamic-to-static error proves (2). The same
calculation applies to each actual probe through its own unchanged
coefficients c_i; no positivity or value of either probe is used.

The relevant recorded failures are not invoked as global bans.
ATTEMPTS/029's termwise generator commutation is absent from (7).
ATTEMPTS/030's varying-parameter qualitative limit is avoided by the
uniform finite-N inequalities (3)–(14). ATTEMPTS/032's absolute-first-
moment shortcut is replaced by the squared moment (4) and the
explicit logarithmic near l1 count in (9). No H dipole decomposition
or upstream E rate is assumed. These checks concern this component
only and do not constitute the separate critical audit of the result.

### 5. Separate critical audit, 2026-10-18

**Verdict: accepted relative to L008, L028, L097, L224 and L233.**
The unchanged pre-invocation EXPLORE assessment is
`drafts/literature/2026-10-18-h-static-trace-column-rate-critical-audit.md`.
L224's L222-supported modal bounds and L097's inherited finite
contraction/spectral hypotheses remain imported, not recursively
audited. The checks below verify the new ordered-column argument,
complete insertion and normalization. They do not establish a new
rate beyond (1)–(2), or a Yang–Mills construction.

**Entire extended-space comparison.** Denote the isometric extensions
in transverse degrees 0,1,2 by E_0,E_1,E_2. L224 section 3 and its
audit establish E_1 T=T_infinity E_0 and
E_2 D_T=C_infinity E_1, including every normal end edge. Thus the
extended finite gradient and curl ranges are subspaces of the full
energy ranges. For nested orthogonal projections, both products equal
the smaller projection, so their difference is an orthogonal
projection. This justifies the contraction bound used on f_far in
(9). No identity for E_1 D_T^T or for adjoint path extension follows
or is needed.

The single-edge path has divergence an endpoint dipole, with either
orientation covered by L224's signed estimates. Its potential cutoff
and the curl-potential cutoff fit about every source with a fixed
fractional buffer. The energy tail and cutoff-derivative squared
norms are both O(N^-3), so (3) holds uniformly for the sources used
here. The mixed Green difference bound gives (4): in dimension three
the weighted shell sum is bounded by C sum_(r>=1) r^-2. These are
applications of L224's audited estimates, not an import of its E
dipole decomposition.

Regard zeta_N^* as E_1 zeta_N^* E_2^* on the full plaquette space.
Insert successively S_infinity and the frozen z_x^*; the difference
is exactly (7) on that full space. Its first summand is bounded by
Cp(k)N^-3/2. In the second summand, each link output is the sum of
a fixed number of plaquette inputs. The square of that sum is at
most its slot count times the sum of squared summands; each input
occurs in a bounded number of slots. For present slots, L224(12)
and the bounded source offset give coefficient difference at most
Ca p(k)(1+dist(y,p)). For absent slots the coefficient is bounded
by Cp(k), and dist(y,p)>=cN, so the same inequality holds. This
also covers all outside outputs, not only the finite link space.
Summing the squared slot errors using (4) proves (8).

For the third summand, finite path shifts preserve the decay
Cp(k)(1+dist(b,p))^-3. Up to radius c_1 N its l1 shell sum is
O(p(k)log(eN)); beyond that radius its squared l2 tail is
O(p(k)^2 N^-3). All near edge sources still have a fractional
buffer. Applying (3) column by column there and contraction on the
entire far part proves (9). Hence the three-term bound (6) holds;
N^-3/2 log(eN)<=C/N<=Ca is sufficient. All finite and frozen
columns have norm at most Cp(k). Expanding a difference of two
inner products and applying Cauchy–Schwarz proves (10), without
compactness of either column's output or projection commutation.

**Full signed curvature insertion.** In stored coordinates the two
curvatures contribute a^-4 and L008(2) contributes a^4, so no mesh
factor remains in M_T. Restriction to transverse curvatures removes
every term with an axial plane on either side. In a shear term this
means mu,nu,alpha are all transverse and distinct. In the ordered
plane basis (23,24,34), the unaveraged restricted shear matrix is

    S_6,T = (1/2) [[0, s_34, -s_24],
                   [s_34, 0, s_23],
                   [-s_24, s_23, 0]].

Indeed its three products are s_23 F_24 F_34,
-s_24 F_23 F_34 and s_34 F_23 F_24. Each clover contributes 1/4;
polarizing a product contributes 1/2 to each transposed matrix
entry. The sixteen pairs therefore have coefficient s sigma sigma/32
in each orientation, exactly as in (11). The triplet instead has
four separate diagonal entries of weight (w_mu+w_nu)/4. It is an
average of squares, with no cross terms. These are all terms of
the transverse restriction of M_0 in L097(2).

L028(4) and its subsequent coefficient paragraph give O(a^2)
consistency and uniform smoothness of w_a,s_a on their fixed
compact support enlargement. Consequently (12) holds also at
centers present in only one support. All insertion source cells
are buffered; no physical-boundary trace rows are discarded.

**Density, labels and normalization.** A rank-one slot |p><q| has
trace <A_l e_q,A_k e_p>. Thus (10) gives O(a p(k)p(l)) per slot
before summing the O(N^3) centers at each level. The O(a^2)
coefficient discrepancy is smaller. Starting from L097(4), the
two Zeta factors supply a^2; multiplication by a^3 and the level
weight s give a^5 s=a^4(as), precisely (5). In particular
a^4 N^3 sum_(s=1)^(N-1)(as) is uniformly bounded. The total
normalized column/stencil error is therefore O(a p(k)p(l)).

L224(13), as verified in its separate modal audit, concerns exactly
c_(i;kl,N)=exp[-tau(lambda_(k,a)+lambda_(l,a))]B_(i,a;kl)
and the same normalized Bb/Bq columns. Its polynomially weighted
exponential bound sums all errors above, including retained high
labels. The component mode with zero own-direction index and all
normal end rows remain included. Omitted continuum labels have at
least one index >=N, so their polynomial-exponential tail is
O(exp(-c'N^2)); no low-mode deletion is involved.

For each frozen slot, full-grid Plancherel gives the source phase
exp[i theta.(t_t-r_t)] between A_l^* and A_k. Summing translated
slots gives exactly m_x in the A_k m_x A_l^* order. The four
triplet translations contribute the same diagonal and sum to W_T;
the two clover averages contribute eta_mu eta_alpha and
eta_nu eta_alpha on the two sides of the appropriate shear entry.
Thus this symbol is precisely W_T+C_T^* S_6,T C_T, not a symbol
with one clover omitted. The resulting finite integral is (15).
Unitary cell-center phases cancel in this closed trace. There is
one trace density per vertex, with no new color or assembly factor.

The physical frozen coefficients v_k and their first derivatives,
including the lower-prefix integral and its constant axial mode,
have polynomial bounds. Only these coefficients are differentiated
in H_kl, not P or S. Therefore rectangle quadrature of
(x_1+4)H_kl has error O(a p(k)p(l)); compact strain support
handles endpoint strips without extending the pinned upper
potential. The full heat sum preserves this error. The resulting
integral is exactly L097(5). This independently checks
|a^3 T_(i,N)-K_(i,Q)|<=C_i a, hence (1). L233 and the triangle
inequality give (2); the subtraction sign in the assembled H
component is unchanged.

This is local validation of the existing standard-method result,
classified REPRODUCTION. The audited argument uses no failed
termwise commutation, absolute first kernel moment or varying-mass
qualitative limit. No numerical certificate is required. Other
component rates, the complete interacting comparison and all
construction requirements remain unresolved.

## Mathlib

Full matching theorem for this ordered relative H trace: **not
checked**. Supporting orthogonal projections, Fourier Plancherel,
trace/rank-one identities, Cauchy–Schwarz and quantitative quadrature:
**not checked**. Unknown availability is not evidence of absence.
The precise scalar citations and their local applicability are given
above; no numerical certificate or mathematical script is needed.
