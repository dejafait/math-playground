# C999w: A sufficient shared-residual quadratic certificate template

## Hypotheses

Keep C744v/w/z's actual real cosine operators D,S,T,T*,U, neutral
space and closed restricted form, and C999k's reference R. Thus
ell=log(3)/2, L=D+S+256C*C, R has the exact rational head H on0:511
and diagonal h(k_n)/2 thereafter, and H>=h0 I with h0=.239999.
Retain all analytic-response, IEEE754/Decimal, whole-neutral-core and
unreplayed original c_* qualifications. No RH, H2 or sign of S3 is assumed.

Set J=1024, d=1022, m=2044, N=512 and K=65536. Z is precisely
C999q's exact neutral completion from C^d to raw0:J-1. Both endpoints
are independent complex vectors: x=(alpha,beta), f=Zalpha, h=Zbeta.
Keep the exact map Y=(Z*LZ)^-1 Z*[TZ,T*Z] of attempt598 and g=ZYx.
The desired threshold is mu=999/1000000 in this ORIGINAL free metric.
There is no energy-image congruence, reflection constraint or band restriction.

Use the uniform entry bounds and entire-tail estimates of C999q
Sections2,5,8, with both endpoint maps equal to the full Z. Use its
Section1 strong-trial/reference inequality, not its band numerical totals.
The finite entry centers are the original square and the higher-row
formulas recorded598; their exact dyadic values are proposals enclosed
by those bounds. Source paths are `scripts/separation-seven/`:
`original-galerkin-586.npz`, `joint-galerkin-family-certificate-598.py`,
and the pinned reference `complete-covariance-532.npz`.

The componentwise exact-Y enclosure (Yc,Yr) is the
`galerkin_solution_center/radius` in `joint-entrywise-600.npz`.
Its use retains600's verified matrix-RHS inclusion and arithmetic
contracts; this symbolic step does not independently replay them.
An implementation must validate the saved inclusion and input pins,
or obtain a valid enclosure before using this template. The mathematical
requirement is |Y-Yc|<=Yr entrywise, Yr>=0, not a solver success flag.
No failed final-order claim from598 or600 is an input.

Import the following inspected results, without reproof:

- Stolfi–de Figueiredo, *An Introduction to Affine Arithmetic*, TEMA4(3)
  (2003),297–312, Sections3/3.1–3.3.4 pp300–304 and3.5–3.6 pp306–307,
  DOI10.5540/tema.2003.04.03.0297,
  [journal PDF](https://tema.sbmac.org.br/tema/article/download/352/291).
  The simultaneous-assignment invariant requires fresh paid nonlinear
  and coefficient-rounding errors; common identifiers must mean common
  quantities. It supplies enclosure, not positivity or statistical covariance.
- Rump, *Verification methods: Rigorous results using floating-point
  arithmetic*, Acta Numerica19(2010),287–449, corrected author version,
  Section9.3, Algorithm9.1/(9.10)–(9.14), author pp42–44, and
  Theorems10.6/10.8, Algorithm10.7 and matrix-RHS remark, pp57–59,
  [PDF](https://www.tuhh.de/ti3/paper/rump/Ru10.pdf). Strict residual
  inclusion verifies the real coefficient solves; it does not preserve
  dependencies automatically.
- Van Waarde–Camlibel–Mesbahi, *From Noisy Data to Feedback Controllers:
  Nonconservative Design via a Matrix S-Lemma*, IEEE TAC67(1)(2022),
  162–175, Theorem9/proof and Corollary10 p166; Theorem11/proof and
  Corollary12 p167, DOI10.1109/TAC.2020.3047577,
  [version of record](https://pure.rug.nl/ws/portalfiles/portal/206606333/From_Noisy_Data_to_Feedback_Controllers_Nonconservative_Design_via_a_Matrix_S_Lemma.pdf).
  Only the sufficient congruence implication is used below. Necessity
  for one full matrix variable with one QMI and strict feasibility,
  or the bounded-set strict theorem, is NOT imported for our structured
  variables and equalities.
- Rump, *Verification of positive definiteness*, BIT46(2006),433–452,
  Theorem2.3, Corollaries2.4/2.7 and Lemma2.6, author pp4–6,
  [PDF](https://www.tuhh.de/ti3/paper/rump/Ru06c.pdf), supplies an
  optional fully paid numerical factor verification. The definition
  below instead permits exact rational coefficient/factor arithmetic.

Teschl, GSM99 author version12February2009, Theorems2.13/2.18
pp71–72/77, [PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
and Behrndt–Hassi–de Snoo–Wietsma, arXiv:1403.5704v1,
Proposition2.1 p4, Theorem3.4's nonnegative sufficient case p11 and
Corollary3.5 p12, [PDF](https://arxiv.org/pdf/1403.5704v1), enter through
C999k/q's existing restricted-form application. No new unbounded
inverse or domain theorem is asserted here.

## Conclusion

Sections1–5 specify a finite simultaneous affine enclosure, a real
symmetric quadratic m-square matrix polynomial P(theta), affine equality
constraints, and an explicit sufficient positive-semidefinite matrix
certificate. If that certificate is supplied and rigorously verified,
then, under the hypotheses above,

    Q_actual(f,ZYx,h)-<R^-1(Tf+T*h-LZYx),Tf+T*h-LZYx>
        >= .000999 ||x||_2^2,                              (1)

and C999q's strong-trial inequality gives the same lower bound for Q_min.
All outputs, including n>=65536, are covered by this implication.

**No certificate satisfying the matrix condition is supplied.** Step626
establishes the symbolic construction only, as standard-method
REPRODUCTION. The separate conceptual audit628 in Section7 upholds
this conditional construction under its stated hypotheses. Neither(1), any new
numerical margin, nor feasibility/practical tractability of the large
matrix condition has been established. This is not a candidate RH proof.

## Proof

### 1. Primitive identifiers and a fixed arithmetic graph

All stored floating values are regarded as exact dyadic rationals.
All interval endpoints and outward scalar upper bounds below are rational.
Coefficient arithmetic in THIS template is exact rational arithmetic.
Thus no unrecorded floating operation is part of its definition.

For a primitive scalar a enclosed by c+[-r,r], write a=c+r theta_a,
|theta_a|<=1. Different entries receive different identifiers except for
proved identities: the symmetric raw0:J square of M=D+S uses one entry
in both transposed positions; the two T orientations use the same
identifier for T_nm and (T*)_mn. Repeated reads of an entry reuse that
identifier. A bound of the same size for two different entries does NOT
identify their errors. No probability or independent random variables occur.

The registry consists of the d nonzero uncertain ratios defining Z;
M on rows0:K-1, columns0:J-1; the union of T on that rectangle and its
transposed rectangle; U on the full J-square; all d*m entries of Y;
and t0=1/sqrt(2), used for boundary functionals. Enclose the ratios and
t0 using the existing directed Decimal/Machin/sqrt contract (e.g.600's
80-digit ratio construction), with rational outward endpoints.
M uses the distinct off-diagonal/diagonal bounds of C999q Section2;
T and U use its1e-6 entry bound, including complete continuous suffixes.
Exact zero entries may retain zero radius. These boxes need only CONTAIN
the actual entries; arbitrary choices need not define neutral operators.

The Y identifiers refer to the entries of the already enclosed exact
solution. They do not assert affine dependence of A^-1 B on its input
errors. Its finite regularity is part of the verified inclusion hypothesis.
In particular the same Y entry is used in every node below, and its
Galerkin equation will be retained as an additional equality.

For clarity, fix this instance of the imported AA multiplication rule.
If affine matrices X=X0+sum Xi theta_i and Z'=Z0'+sum Zi' theta_i
are multiplied, define the affine output with constant X0 Z0',
coefficients X0 Zi'+Xi Z0', and, for each output entry(a,b), one
fresh coefficient

    r_ab=sum_k (sum_i |(Xi)_ak|)(sum_j |(Zj')_kb|).         (2)

That coefficient multiplies a fresh theta in just this output entry.
Allocate a symbol also when r_ab=0. Formula(2) pays the entire omitted
quadratic product. This is the source's nonlinear-remainder rule applied
to each dot product; no term is silently discarded. Exact additions,
transposes, concatenations and symmetrization reuse existing coefficients.
For a fixed actual assignment to old symbols, each new symbol can be
chosen in[-1,1] to give the exact dot product. Induction in the following
acyclic graph therefore yields ONE assignment reproducing every actual
node simultaneously, not a separately chosen assignment for each matrix.

Write AA for this operation, F=[Fplus,Fminus], and subscript J or P for
the first J or N rows. Construct in this order:

    V=AA(M Z)                         K by d
    Fplus=AA(T Z), Fminus=AA(T* Z)     K by d each
    A=sym AA(Z^t V_J)                 d by d
    B=AA(Z^t F_J)                     d by m
    UZ=AA(U Z), U0=AA(Z^t UZ)         J by d; d by d
    G=AA(Z Y)                         J by m
    JY=AA(A Y)                        d by m
    VY=AA(V Y), rho=F-VY              K by m each.          (3)

At the actual simultaneous assignment these are respectively MZ,
TZ,T*Z,A=Z^tMZ,B=Z^t[TZ,T*Z],UZ,Z^tUZ,ZY,AY,MZY and the full
finite lifted residual. The penalty vanishes on actual Z; R is unchanged.
M includes actual D on ALL rows0:1023, including512:1023. For higher
rows D vanishes by finite support, so M there is S. Both T orientations
and U retain their original signs and complete data.

At the actual assignment JY-B=0. Its d*m scalar entries are affine
constraints, not assumed identities throughout the box. This retains
the solve equation without inventing an affine inverse. No equality
between distinct AA remainders is introduced.

### 2. Reference-head action from that same residual

Take the fixed dyadic W=`head_reference_W` of600; it is an approximate
inverse proposal only. H is defined exactly from C999k's rational data.
Set D_H=I-HW exactly. If rho_P(theta)=rho0+sum rhoi theta_i, let

    u_bj=|(rho0)_bj|+sum_i |(rhoi)_bj|,
    e_j=h0^-1 sum_(a,b=0)^(N-1) |(D_H)_ab| u_bj.          (4)

All quantities in(4) are computable rational numbers. Append N*m
DISTINCT symbols eta_aj and define

    Delta_aj=e_j eta_aj,  X=W rho_P+Delta.                 (5)

For the actual residual, X_actual=H^-1rho_P satisfies
X_actual-Wrho_P=H^-1 D_H rho_P. Each entry is bounded in absolute
value by h0^-1 ||D_H rho_:j||_2, which is at most(4), since the
Euclidean norm is at most the sum of absolute coordinates. Thus there
is a simultaneous choice of the new eta making X=X_actual. This
separately pays reconstruction of the fixed rational head action.
W is never assumed exact, and no independently boxed head covariance
is substituted for rho_P^t X. Retain also the N*m affine equalities
HX-rho_P=0; they hold at the actual assignment.

### 3. Complete tail with the same predictor

Let rplus,rminus,re,ro be the raw J-row functionals with coefficients
t_n, (-1)^n t_n, 1_even(n)t_n, 1_odd(n)t_n, where t0 above is shared
and t_n=1 for n>0. Form AA(rminus Z), AA(rplus Z), AA(re G), AA(ro G),
and assemble the six-row affine map B_tail on the ORIGINAL m coordinates:

    [(rminus Z,0); (rplus Z,0); (0,rplus Z); (0,rminus Z);
                         re G; ro G].                    (6)

The repeated endpoint rows reuse their identifiers; each product is
formed once. This is exactly C999q's six functionals for full Z at both
endpoints and actual g=ZYx. It is not the old dyadic-trial tail map.

For an explicit computable norm bound choose a rational ybar satisfying

    ybar^2 >= sum_(i,j) (|(Yc)_ij|+(Yr)_ij)^2, ybar>=0.    (7)

For example the upward rational square root, rounded to the next unit
of10^-20, suffices. This bounds actual ||Y||_2 by its Frobenius norm.
Use z=1.008 from the exact-ratio bound in C999q/598. Choose rational
upper bounds for all the following positive C999q Section5 quantities,
using its formulas and the original complete shift list:

    jrem=(2/pi)/(1-((J-1)/K)^2)
       [sqrt(sum_(n=1)^(J-1)n^4)/sqrt(5(K-1)^5)
        +sqrt(sum_(n=1)^(J-1)n^2)/sqrt(3(K-1)^3)],
    srem=sqrt(sum_(n=0)^(J-1)(4n+16ell/pi^2)^2)/sqrt(3(K-1)^3),
    b=4ell[1+(3/2)3^(-1/4)]/pi^2,
    kappa=1/[2187 sqrt(3) (5/2)(1-1/729)],
    trem=sqrt(2)z[(a_plus+a_minus)jrem+kappa]+srem z ybar.

Here a_plus and a_minus are the positive weight sums over the two delay
signs of ALL16 separation7 shifts; kappa bounds the COMPLETE continuous
operator, not a finite suffix sample. Take positive rational w_j above
the six weights of C999q Section5, in this order:

    [2a_plus/pi, 2a_minus/pi, 2a_plus/pi, 2a_minus/pi,
                      sqrt(2)(1+b/K), 1+b/K]/sqrt(K-1).

Let Wb=(sum_j w_j)diag(w_j).
Increasing positive weights preserves the weighted Cauchy–Schwarz
majorant used there. With d_K=log(K/(2ell))-2ell^2/(9K^2)>0, take
rational omega_K>=2/d_K from that same monotone diagonal bound and
rational tbar>=trem. Then the ENTIRE tail
covariance at the actual assignment obeys

    Cov_(n>=K) <= omega_K [(11/10) B_tail^t Wb B_tail
                                      +11 tbar^2 I_m].   (8)

This is exactly the existing dominated-remainder/Young estimate with
the present maps and norm, not a new analytical tail bound. Each remainder
and the predictor's contribution is paid in tbar. Exact coefficient
arithmetic needs no extra six-row multiplication allowance. If rounded
arithmetic is used later, its error must be separately enclosed. No old
598/C999v accumulated tail total or old whole-LZ predictor correction
is transferred. The predictor is already the same enclosed Y in(3),(6).

### 4. The quadratic matrix and dimensions

Write sym(B)=(B+B^t)/2. Put E0=[[A,-U0^t],[-U0,A]]. Form the
real symmetric polynomial

    P(theta)=E0-B^tY-Y^tB+sym(Y^t JY)
             -sym(rho_P^t X)
             -sum_(n=N)^(K-1) omega_n rho_n^t rho_n
             -omega_K[(11/10)B_tail^t Wb B_tail+11 tbar^2 I_m]
             -mu I_m,                                  (9)

where EVERY omega_n is a positive rational upper bound for2/h(k_n)
from C999k/q's verified diagonal intervals. All nodes in(9) are affine
in one registry. Thus(9) is quadratic, and its cross coefficients are
retained, including energy/residual/predictor and both endpoint couplings.
Neither the finite covariance nor the predictor change is replaced by
an isotropic norm allowance. No final entry-radius norm test is used.

For explicit dimensions, allocate the primitive symbols described in
Section1 even if their radius is zero. Their number is

    p0=d+1+[J(J+1)/2+(K-J)J]+[2KJ-J^2]+J^2+dm.

The T count is the union of its rectangle and transpose, sharing the
J-square intersection. The product nodes(3) add
3Kd+2d^2+2dm+Jd+Jm+Km symbols. The four boundary products add
2d+2m; the head remainder adds Nm. Therefore fix

    p=p0+3Kd+2d^2+2dm+Jd+Jm+Km+2d+2m+Nm.               (10)

There are p real variables, m=2044 complex endpoint coordinates, and
(d+N)m listed scalar affine equalities, with redundancies allowed.
All products in(9) are polynomial coefficient operations; they add
no further symbols. This is a finite but extremely large construction.
No sparse compression, feasible implementation cost or dimension-free
bound is claimed. Removing unused zero-radius symbols is optional and
cannot change the polynomial or the required order.

Let theta_* be the single actual assignment constructed above. It is
in[-1,1]^p and satisfies every listed equality. Equations(3),(5) give
the exact signed energy and exact head inverse action there. In particular
sym(Y^t JY)=Y^t A Y at that assignment; neither the middle energy nor
its uncertainty has been omitted. Denote the left side of(1) before its
inequality sign by F_joint(x). Equations(8),(9) and the upward finite
weights consequently give

    F_joint(x)-mu||x||^2 >= x*P(theta_*)x.                 (11)

Only disjoint REFERENCE output spaces were summed:0:511,512:1023,
1024:65535 and n>=65536. Within each residual row all terms were
combined before squaring. There is no omitted mixed reference output
term because R is block diagonal on precisely these spaces.

### 5. One sufficient coefficient certificate; no losslessness

Expand P=P00+sum Pi theta_i+sum Pii theta_i^2+
sum_(i<j) Pij theta_i theta_j with real symmetric m-square coefficients.
Let C be the symmetric block matrix of size (p+1)m with
C00=P00, C0i=Ci0=Pi/2, Cii=Pii and Cij=Cji=Pij/2 (i,j>0).
For v(theta)=(1,theta_1,...,theta_p)^t,

    P(theta)=(v(theta) tensor I_m)^t C (v(theta) tensor I_m).

For each affine scalar equality l_a(theta)=0 define the symmetric
(p+1)-square L_a by (L_a)00=(l_a)0 and
(L_a)0i=(L_a)i0=(l_a)i/2, with other entries zero. Let
N_i=e0 e0^t-ei ei^t, so v^t N_i v=1-theta_i^2.

A certificate is a collection of rational symmetric matrices
Lambda_i>=0 and arbitrary rational symmetric Gamma_a, each m-square,
such that the following matrix is positive semidefinite:

    C_cert=C-sum_i N_i tensor Lambda_i
                         +sum_a L_a tensor Gamma_a >=0.  (12)

Every Lambda_i order and the ENTIRE matrix(12) must be verified.
An exact rational LDL^t identity with nonnegative rational diagonal
is one sufficient witness; a complete Rump-style reconstruction with
all conversion/assembly/roundoff debts paid is another. A numerical
optimizer status, a locator or a successful Cholesky call is insufficient.

Congruence in(12) gives
P(theta)-sum_i(1-theta_i^2)Lambda_i+sum_a l_a(theta)Gamma_a>=0.
At theta_* the equality terms vanish and the box terms are nonnegative.
Thus P(theta_*)>=0, which proves(1) by(11). This explicitly checks the
sufficient implication used from the source; it is not a new S-lemma
necessity theorem. The affine equality constraints, structured repetitions
and nonlinear AA remainders have all been retained or overenclosed.
Strict feasibility, bounded full-matrix uncertainty and equality with
a single-QMI set are not claimed, so Theorems9/11's converses are unused.

For any real symmetric m-square P, x=a+ib gives
x*Px=a^tPa+b^tPb. Hence the real certificate proves order for EVERY
original complex endpoint pair with the same mu||x||_2^2. It does not
replace the physical metric by an energy-image coordinate identity.
The C999q strong-trial conclusion applies because the actual finite
neutral g lies in Dom(A0), with A0g=P0Lg; this fact was not asserted
for arbitrary nonphysical points of the containing uncertainty box.

### 6. Error ledger, outcome and limits

Analytic coordinate/operator errors are the primitive intervals in
Section1, including the separate diagonal case and complete continuous
suffixes. Predictor-solve uncertainty is Yr, reused throughout(3),(9).
Every nonlinear product debt is its explicit(2) fresh symbol, reused
whenever that output is read. The separate head reconstruction debt is
(4)–(5). All finite Gram errors are zero in the defined exact rational
coefficient arithmetic, as are final assembly and factor arithmetic
errors when exact rational identities are used. A floating replacement
must add verified coefficient-rounding errors or a paid matrix shift;
rounding a shared coefficient outward alone violates the AA invariant.
The only infinite-output debt is the complete formula(8), with fresh
predictor-dependent functionals and tbar, not a sampled tail or old total.

This is a simultaneous, computable sufficient template and therefore
passes the representation-only test of assessment625. It does NOT
establish that(12) is feasible, that a useful margin survives its AA
overenclosure, or that the very large coefficient representation is
practical. It cannot authorize a numerical rerun merely by existing.
At step626 the independent conceptual audit was pending. Section7 now
supplies that audit; implementation still requires separate concrete
admission and a verified witness for the matrix condition.

The598 scalar loss,600 finite box-radius stop and unfinished603 proposal
are unchanged. No claim of an actual negative direction or progress
beyond the inspected methods follows. The main L030-L032/C032a gap,
higher endpoints/couplings, C744q, H2, non-neutral coverage, original
source/core/c_* verification and global actual-Xi assembly remain open.

### 7. Separate conceptual audit — 12 November2026, step628

**Verdict and scope.** Under the invocation-start SPECIALIZE assessment626,
separately approved627, the simultaneous-enclosure construction and
the implication (12) => (1) are sound, conditional on all the stated
input enclosures and analytic/form contracts. No change to the formula,
predictor, reference, output partition or metric is necessary. This
audit establishes the usability of a conditional standard-method input;
it supplies no feasible multipliers, numerical floor, actual violating
direction or advance beyond the inspected methods. In particular it
does not independently replay600's solve certificate or the original
source/core/c_* computations.

**Source scope.** Reuse the primary passages specified in Hypotheses:
Stolfi--de Figueiredo Sections3/3.1--3.3.4 and3.5--3.6 for simultaneous
enclosure, Rump2010 Section9.3 and Theorems10.6/10.8 for conditional
input inclusion, and van Waarde--Camlibel--Mesbahi Theorems9/11 for
the sufficient congruence direction only. The exact rational witness
option in Section5 needs no floating factor theorem. Its optional
floating replacement retains every Rump2006 reconstruction hypothesis
and error debt. C999k Sections1--2 and C999q Section1/Section8 supply
the cited Teschl/Behrndt restricted-form application. No necessity,
strict-feasibility, single-full-block or sparse-reduction theorem is
being applied to this multiple-constraint construction. The checks
below concern the local specialization, not reproofs of those sources.

**One actual assignment, independent of the endpoint vector.** For each
primitive actual scalar choose its normalized error in its rational
box; if its radius is zero choose0. These are real coefficient errors,
not choices made separately for each complex x. Repeated M/T entries
are identified only by the stated symmetry/adjoint identities. The
actual Z ratios, t0 and exact real Y choose their own entries in their
containing boxes. Possible correlations omitted from these boxes
enlarge the set; none is asserted without proof. A nonphysical box
point need not be neutral or define an inverse.

At a product node the omitted (a,b) entry is

    sum_k (sum_i (Xi)_ak theta_i)(sum_j (Zj')_kb theta_j).

Its absolute value is at most (2). Assigning this actual remainder
divided by r_ab to the fresh symbol reproduces that entry; if r_ab=0
the remainder is exactly zero. Do this after the preceding nodes have
been fixed. Each new symbol has only its prescribed new occurrence
until that node is subsequently reused, so it does not alter any
earlier node. Induction over (3), then the head and boundary products,
gives a single assignment reproducing all their actual matrices.
Symmetrization of Z^t V_J retains the actual A because M_J is real
symmetric. The separately formed G=ZY and VY=(MZ)Y agree with the
same physical middle at this assignment, without identifying their
distinct nonlinear remainder symbols elsewhere in the box.

Y is an enclosed solution, not an affine formula for A^-1B. At the
actual assignment A=Z^t LZ, B=Z^t[TZ,T*Z] and JY=AY=B, hence all
dm scalar solve equalities hold. Exact CZ=0 gives LZ=MZ on EVERY
output, including the moment-penalty outputs outside the trial support.
It does not remove D on512:1023. The primitive M rectangle therefore
contains exactly the required local action, and its off-diagonal,
diagonal, zero-frequency and complete-suffix bounds have the ranges
specified in C999q Section2. The T rectangle and its transpose cover
both orientations; U is the complete signed J-square compression.

**Head reconstruction and output order.** For actual residual column j,
write r=(rho_P)_:j. The required discrepancy is

    H^-1 r-Wr=H^-1(I-HW)r.

H>=h0 I implies ||H^-1||<=1/h0. The absolute value of any coordinate
of this discrepancy is bounded by

    h0^-1 ||(I-HW)r||_2
      <= h0^-1 sum_(a,b) |(I-HW)_ab| u_bj=e_j.

Thus the distinct eta symbols can realize all entries of H^-1rho_P
simultaneously, including the zero-bound case. HX-rho_P=0 then holds
for all Nm entries. No inverse accuracy of W is needed. At that
assignment sym(rho_P^t X)=rho_P^t H^-1rho_P, the exact head covariance.

The complementary reference is diagonal, with positive weights2/h(k_n).
Each replacement by omega_n is upward and multiplies a positive
semidefinite row Gram. Consequently its sign in (9) is downward as
required for a lower bound. The disjoint output sets0:511,512:1023,
1024:65535 and n>=65536 exhaust R's inverse action. This is a reference
orthogonality statement only; the corresponding projections need not
preserve the neutral subspace. Within a residual row both endpoints
and the middle were added before taking its Gram, so none of their
cross terms has been discarded.

**Entire tail for this predictor.** C999q Section5's argument uses
input indices below J and norms of the endpoint and middle maps, not the
band restriction in that lemma's numerical conclusion. Both full Z
endpoint maps satisfy ||Z||<1.008 by its exact-ratio calculation.
Equation(7) bounds ||Y||_2 through ||Y||_F, so ||ZY||_2<=z*ybar.
At the common assignment (6) gives exactly its six functionals in the
stated order, with the same t0 and the actual middle ZY. The leading
tail satisfies the same weighted Cauchy--Schwarz bound, since increasing
any positive w_j increases each coefficient (sum_k w_k)w_j.

The jrem and srem expressions cover every n>=K and every input index below J,
including the constant-mode/parity cases inherited from C999q. The
complete continuous norm is exactly C744v(2)'s kappa; restricting it
to these output rows can only decrease its norm. Thus the unweighted
remainder is bounded by tbar||x||, with the new ybar, and Young's
inequality with coefficients11/10 and11 gives (8). Monotonicity of
d_n and h(k_n)>=d_n>0 give2/h(k_n)<=2/d_K<=omega_K on the whole
tail. Dg vanishes there by finite support. This checks the entire
infinite sum, rather than a finite sample. No old band tail total,
dyadic-predictor total or separate whole-LZ predictor correction is
needed or transferred: the enclosed exact Y occurs in all finite nodes
and in both the tail functionals and its remainder norm. Exact rational
coefficient operations justify omitting C999q's old floating six-row
assembly allowance only for this exact template.

**Signed energy and dimensions.** At the actual assignment, expansion
of C744z(5) on f=Zalpha, h=Zbeta and g=ZYx gives precisely

    Q_actual=x*[E0-B^tY-Y^tB+Y^t A Y]x.

The lower-left remote block is -Z^tUZ=-U0 and the upper-right block
its transpose. The second forcing block is Z^tT*Z. Thus the two
adjacent couplings, the remote coupling and the positive middle energy
have their original signs. JY=AY makes the quadratic replacement
sym(Y^t JY) equal Y^t A Y at this assignment. Subtracting the head
covariance and the upward finite/tail majorants proves (11).

The primitive count in (10) uses d ratios and t0, one symmetric
J-square plus the remaining (K-J)J entries of M, a union of two T
rectangles with overlap J^2, J^2 entries of U and dm entries of Y.
The products V,Fplus,Fminus contribute3Kd symbols; A,U0 contribute
2d^2; B,JY contribute2dm; UZ,G,VY contribute Jd,Jm,Km respectively.
The four boundary products add2d+2m and the head adds Nm. Thus (10)
counts every declared symbol exactly once, even if some radii vanish
or symmetrization leaves redundancy. The listed equality count is
dm+Nm. Each energy, covariance and tail term in (9) is m-square;
their degrees are at most two because every graph node is affine.
Taking the exact polynomial products at this last stage adds no new
uncertainty symbol or unbounded higher-degree remainder.

**Lift, multipliers, complex metric and domain.** In the coefficient
lift, each off-diagonal block is encountered twice under congruence,
which accounts for the factors1/2 in C0i and Cij. Likewise v^tL_a v
is exactly l_a(theta), with its constant and linear coefficients, and
v^tN_i v=1-theta_i^2. Thus (12) gives at the actual assignment

    P(theta_*)=(v_* tensor I_m)^t C_cert (v_* tensor I_m)
                 +sum_i (1-theta_*i^2)Lambda_i >=0.

The equality-multiplier terms vanish; Gamma_a has no sign requirement.
Every Lambda_i and the whole C_cert must be verified, not selected
principal blocks. The implication uses neither a converse S-lemma
nor independence of the box variables. A complete exact rational
LDL^t identity with nonnegative diagonal suffices even if singular;
mere factorization success does not. No rational witness existence is
asserted when the sufficient condition has not been solved.

All coefficients are real symmetric, and the actual assignment is
fixed for every x. Writing x=a+ib therefore proves Hermitian order
with the original ||a||^2+||b||^2 metric. There is no energy-coordinate
congruence or endpoint reflection restriction. Finally actual g is
a finite neutral cosine vector in Dom(L); testing its form against
all V0 gives g in Dom(A0) and A0g=P0Lg. C999k's positive reference
and restricted-relation inverse order apply to this lifted residual.
C999q(2) then gives Q_min>=F_joint. Nothing about arbitrary nonphysical
box points is needed for this domain argument.

**Remaining certificate and route limits.** The conditional implication
passes; (12) has not been shown feasible or practical. The Y inclusion
and data pins from600 must still be validated by an implementation,
or replaced by another valid enclosure under its own admitted scope.
That step's full solves did not establish its failed final comparison
or compute its higher outputs. Likewise598's negative lower certificate
does not give an upper bound on the actual comparison. Both stops and
unfinished603 remain intact. No numerical or sparse-reduction run is
authorized by this audit, and no change to the main RH argument follows.
The independent limitations listed in Section6 and the Mathlib status
below are unchanged.

### 8. Exact saved-image recentering audit — 12 November2026, step637

**Hypotheses and scope.** Keep all Hypotheses above, including600's
original inclusion/arithmetic contracts. Use exactly the pinned600
proposal, saved z center, saved image radius and saved solution center
and radius. Assessment635, separately approved636, permits this ordinary
audit only. Neither635's parked point prescription nor its JY/head/scalar
work is resumed. This section does not independently replay the matrix
products of the original solve or the analytic-response/core/c_* inputs.

**Conclusion.** Every one of the1022*2044=2,088,968 saved image intervals,
after addition of the exact dyadic proposal, is contained in the saved
solution box. For each entry write p,z,i,c,r for the proposal, residual
image center/radius, and solution center/radius respectively. Exactly,

    r-i-|p+z-c| >= 541770495279/2^113 > 0.                (13)

The minimum occurs at zero-based position(358,415). The decimal
5.2170600992166485e-23 describes that exact rational, not a rounded
substitute for the required nonnegative threshold. Thus635's failed
additional recentering test is verification excess, not a failure to
contain the saved image. Conditional on the retained original solve
certificate, the actual Y remains in the same boxes. No point, scalar
obstruction, numerical floor, actual signed coupling or RH result follows.

**Complete arithmetic evidence and proof.** The reproduction command is

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/separation-seven/exact-recentering-audit-637.py

The report is `scripts/separation-seven/exact-recentering-audit-637.json`;
the full all-entry exact evidence is
`scripts/separation-seven/exact-recentering-audit-637.jsonl.gz`.
The report pins19 inputs, including all14 inherited635 pins, the complete
stopped archive, executed635 source and current metadata-corrected source.
The arithmetic audit reads all1050 recorded checks, all1022 directed-ratio
metadata pairs, and every entry of all four stopped arrays. K/z margins
and strict-inclusion margins have no negative entries;635's saved
Y-recentering array has2,088,934 negative entries. These checks inspect
the complete saved evidence; they do not reevaluate the large matrix
products producing those first three arrays.

Every relevant binary64 input is finite, dimensioned1022-by2044, and
both radii are nonnegative. Convert the saved finite floats directly
with `float.as_integer_ratio`, using the exact-conversion contract
inspected in approval636, [Python documentation](https://docs.python.org/3/library/stdtypes.html#float.as_integer_ratio).
No decimal display conversion, tolerance or denominator approximation
enters the calculation. Each conversion is checked to have a power-of-two
denominator. A common denominator2^1126 contains every input used in the
comparison; the per-entry conversion checks this fact, rather than
trusting the preliminary floating exponent estimate. Exact signed integer
addition/subtraction/absolute value therefore evaluates the numerator of
r-i-|p+z-c| for EVERY entry. There are no negative or zero numerators,
and the complete minimum reduces to(13). Evidence stores each integer
divided by its denominator after losslessly removing powers of two;
every storage inverse conversion is checked. All entries are retained.

Trace600's `verified_solve` return expression
`Ball(proposal)+Ball(z.c,image_radius)`. Set

    e=nextup((|p|+|z|)*1e-15+1e-280),
    c_saved=fl(p+z),  r_saved=nextup(nextup(i)+e).

Here the expression for e denotes precisely the executed floating
operations, not a new analytic error estimate. The audit reproduces all
center and radius BITS of these expressions from600, with no matrix
solve, changed box or updated predictor. Independently, exact integer
comparison on every entry verifies e-|p+z-c|>0 and r-i-e>0.
Their respective exact minima are

    7237180290236885/2^136 > 0,
    3298535501781/2^116 > 0.

Thus the original saved addition pays its actual recentering shift.
For any value in the saved image interval, the triangle inequality gives
|(p+z+delta)-c|<=|p+z-c|+i<=r, |delta|<=i. This is the
applicability argument for the saved interval, not a reproof of Rump's
inclusion theorem. The latter's original hypotheses and qualification
remain exactly those in Hypotheses/Section7 above.

Finally reproduce every BIT of635's two-operation Ball recentering
array. Its shift bound s comes from `abs_upper(Ball(p)+Ball(z)-Ball(c))`,
which pays both generic additions. Exact comparison gives s-|p+z-c|>0
on every entry, with minimum2831833247498417/2^133. The exact margin
minus635's saved lower comparison is also positive everywhere, minimum
8966757698417025/2^128. These comparisons explain why the extra
sufficient test failed although(13) holds. They supply no converse
infeasibility conclusion. Full failure lists are empty and all19 input
pins are unchanged at completion.

This is local ADVANCE/REPRODUCTION: it establishes the previously
unverified saved-image recentering input, using known exact arithmetic
and the existing conditional solve framework. It is no advance beyond
the inspected sources and does not alter the conditional main argument.
The original635 stop and unfinished reasoning remain recorded. Every
independent obligation in Section6 remains open; in particular do not
infer approval to resume635 merely from this audit.

## Mathlib

Full matching coverage for this shared-error construction, actual response
operators and complete-output certificate has not been checked. The
primary sources above supply mathematical methods, not a matching
Mathlib theorem. No absence or formal verification claim is made.
