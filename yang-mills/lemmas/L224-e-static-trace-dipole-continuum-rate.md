# L224 — A dipole-energy rate for the cumulative E static trace

## Hypotheses

Use exactly L101's finite static trace T_(i,N), as named in L223,
and continuum functional K_(i,E), for both actual probes i=3,6.
The group is SU(2), the box is (-4,4)^4 with relative pinned links,
the forest is straight and lower-rooted in direction 1, N is admitted
and even, a=8/N, and tau=1/16. Coordinates below are ordinary stored
coordinates. The small-coupling coefficient is taken at fixed mesh.
Keep all interior axial levels, normal transverse end edges, actual
triplet averages of squares, shear clovers and the entire heat spectrum.

Import L101(13), (15), (16), its exact transverse cochain operators,
and its identification of the limiting stencil m_E. Import L028's
smooth coefficient construction and exact interior forest lift, L097's
path maps and exterior normalization, and L222(2), (3), (7), (9)'s
quantitative product-mode, probe-form and prefix estimates. These are
supporting estimates, not an import of the present trace rate.

## Conclusion

There is C_i independent of sufficiently large admitted N such that

    |a^3 T_(i,N)-K_(i,E)| <= C_i/N,
    |T_(i,N)-a^(-3)K_(i,E)| <= C_i N^2.                (1)

In particular this meets the requested O(N^(5/2) log(eN)^2) threshold.
The constants are not evaluated. The comparison retains the full
cumulative insertion, including its moving-cut endpoint and nonzero
upper axial tail. Together with L223, it gives
|R_E-a^(-3)K_(i,E)|=O_i(N^(5/2)); the slower replacement error remains.

This is a local standard-method quantitative specialization, with no
claim of originality beyond the saved source assessment. Its new
projection-cutoff and ordered-trace argument has passed the separate
critical audit in proof section 7 relative to the stated imported inputs.
Other component rates, a complete quantitative response remainder,
L220's separate audit, interacting reflected error <=c_box/2, continuum
axioms and finite positive mass remain unresolved. There is no candidate
solution of the Yang–Mills problem.

## Proof

### 1. The exact cumulative stencil is a signed local dipole energy

Write C_(s,N)=a A_<s. Use transverse vertex coordinates n in
{1,...,N-1}^3, with their physical positions x_T=-4+a n.
L101(13), (15) imply the following facts, uniformly in 1<=s<N:

* C_(s,N) is real symmetric, of a fixed transverse range h.
* Its nonzero rows and columns are in a fixed compact transverse
  subset of (-4,4)^3, with a fixed positive buffer from every face.
* Its entries are bounded, and C_(s,N) 1=0 exactly.

Here the compact set includes the fixed neighboring stencil enlargement;
it is independent of s, even when the cumulative coefficient survives
above the displacement support. To check the last assertion, k_j 1=0
on its coefficient-supported rows. In k_j^T Delta 1, Delta 1 is supported
next to the pinned faces, separated from those rows. Thus L_j 1=0.
Every other term of (13) has a transverse difference on its right,
which annihilates 1 on the supported stencil. This also verifies the
claim at rows outside the coefficient support. It never assigns a
nonzero constant boundary value to a pinned vertex.

Choose once and for all one of each pair d,-d of nonzero integer
displacements of range at most h. Set

    b_(d,N)(s,n)=-(C_(s,N))_(n,n+d),
    h_(n,d)=e_n-e_(n+d).

Only pairs with both endpoints in the vertex set occur. Symmetry and
the zero row sums give the exact identity

    C_(s,N)=sum_(n,d) b_(d,N)(s,n) h_(n,d) h_(n,d)^T. (2)

There is no positivity assertion about b. The off-diagonal entries of
the right side agree with C; its diagonal at n is minus the sum of
that row's off-diagonal entries, proving (2).

There are smooth real limiting functions b_d(x_1,x_T), compactly
supported in the transverse variables, such that

    |b_(d,N)(s,n)-b_d(-4+as,-4+an)| <= C a,
    ||b_d||_(C^1(D)) <= C.                           (3)

For clarity, these are coefficient estimates for the actual stencil,
not a consequence of convergence of its quadratic forms. In L101(15)
each coefficient is a fixed linear combination of divided differences
of u_a and smooth shear coefficients. Taylor's integral remainder and
L028(4) bound its difference from its frozen derivative coefficient by
O(a), with the same bound after one physical derivative. Multiplication
by a and summation over at most N axial layers costs a N=8, so the
accumulated error is O(a). The remaining axial rectangle sum differs
from its integral by O(a), uniformly in its cut s. The quarter layer
has size O(a). In the last term of (13), endpoint averaging changes
the smooth w by O(a), again followed by a length-at-most-8 rectangle
sum. The moving-cut term becomes exactly
(1/2) sum_mu T_mu^T M_(u_(a,1)(s)) T_mu after multiplication by a;
its coefficient error is O(a^2). These bounds prove (3), including
the cuts near either axial end. The limiting functions can be defined
by these explicit limiting coefficient expressions; their C^1 bounds
follow from the bounded derivatives and integrals of the fixed smooth
u,w,s. Their frozen Laurent symbol is precisely L101(4)'s m_E:

    sum_d b_d(x)|1-exp(i d dot theta)|^2=m_E(x,theta). (4)

Indeed (2) freezes to its left side, and the coefficient-by-coefficient
calculation in L101 section 4 identifies that same stencil. Thus (4)
retains both the cumulative W_mu and the endpoint u_1, rather than
substituting a local insertion times s.

### 2. Scalar dipole decay, with the mixed difference justified

Let T_infinity be gradient on Z^3, C_infinity its curl, and
Delta_infinity=T_infinity^T T_infinity. Use the transient scalar
Green kernel g for Delta_infinity. For normalization, the nearest-
neighbor walk has Delta_infinity=6(I-P_walk), hence g=G_walk/6.
Import Lawler–Limic, *Random Walk: A Modern Introduction* (2010),
Theorem 4.3.1 and Corollary 4.3.3, printed pp. 81–84, and
Theorem 6.3.8(a), p. 131, from the inspected author-hosted version:
<https://www.math.uchicago.edu/~lawler/srwbook.pdf>.
Their first Green differences and harmonic interior difference estimate
apply to this symmetric, irreducible nearest-neighbor walk in d=3.
No relative vector inverse is identified with scalar killed Green.

For a fixed bounded displacement d put phi_d=g*(e_0-e_d). The first
difference estimate, telescoped along a path of bounded length, gives
|phi_d(y)|<=C(1+|y|)^(-2). Away from that path's fixed neighborhood,
phi_d is harmonic. Apply Theorem 6.3.8(a) in a ball of radius a fixed
fraction of |y| to phi_d, whose supremum there is O(|y|^(-2)). This
gives its first differences O(|y|^(-3)). It justifies the needed mixed
Green differences without inferring them from a repeated-coordinate
bound. Increasing C covers the fixed neighborhood. Consequently

    |T_infinity phi_d(y)| <= C(1+|y|)^(-3),
    sum_y (1+|y|)^2 |T_infinity phi_d(y)|^2 <= C.      (5)

There are finitely many d, so the constants can be common. The second
sum converges since its radial tail is bounded by C sum_(r>=1) r^(-2).

Let P_infinity be projection onto the l2 closure of gradients of
finitely supported vertex fields. Choose a fixed edge path j_d with
T_infinity^T j_d=e_0-e_d. Then

    k_d=T_infinity phi_d=P_infinity j_d.              (6)

One justification is Fourier Plancherel: the gradient projection
multiplier is t t*/lambda, bounded by one, and its product with
j_d is the Fourier transform of the displayed Green differences.
Equivalently, summation by parts gives the projection equation on
every compact gradient test, and cutting off phi_d in the energy
norm proves membership in the closure. In particular ||k_d||_2<=C.
No bounded inverse of Delta_infinity on all l2 is assumed.

The full-grid curl projection S_infinity is similarly the multiplier
C(theta)C(theta)*/lambda from L097, with the zero-frequency value
irrelevant. For a unit plaquette source e_p its potential

    alpha_p=g*C_infinity^T e_p

has |alpha_p(y)|<=C(1+|y-p|)^(-2), and
|C_infinity alpha_p(y)|<=C(1+|y-p|)^(-3), by the same first-difference
and harmonic argument. Moreover C_infinity alpha_p=S_infinity e_p.
The identity C* C+T T*=lambda I on edge Fourier fibers proves this
projection formula; cutoff in curl energy proves that its range is
the closure of compact curls. These arguments derive only the needed
cochain specialization, not the imported scalar Green estimates.

### 3. Nested finite energy spaces retain every relative end row

Extend finite relative cochains by zero to Z^3. This extension is
isometric in ordinary coordinates and intertwines both gradient
and curl with their full-grid counterparts. Here is the boundary
check. Finite vertex values vanish on all faces, so a gradient on
each normal end edge is its actual difference to zero. Outside
edges have two zero vertex endpoints. A relative one-cochain has
zero tangential links on a face. Every outside plaquette adjacent
to that face therefore has all its possible nonzero tangential
edges zero; the normal edges used by an inside plaquette remain
inside. The same check works at face intersections. Thus outside
curls vanish, while all inside curls, including normal end rows,
are unchanged. No normal component is assigned Dirichlet boundary
conditions in this argument.

Let P_N and S_N denote the resulting extended orthogonal projections
onto finite gradients and finite curls. Thus S_N is exactly L101's
S_T on its finite space. The subspaces are nested inside the
corresponding full-grid energy spaces. In particular

    P_N P_infinity=P_N,  S_N S_infinity=S_N,
    Q_N=S_infinity-S_N is an orthogonal projection.   (7)

For a dipole centered at n in the support of b_(d,N) or b_d, translate
j_d to j_(n,d). Its fixed path lies inside the box for large N.
Then the exact finite column is

    k_(N;n,d)=T G h_(n,d)=P_N j_(n,d).                (8)

Choose a cutoff chi equal to one in a ball of radius cN around n,
zero outside radius 2cN, with first differences <=C/N. The fixed
transverse buffer permits a common c>0 for all these n and all s.
The gradient of chi phi_d is a finite pinned gradient. By (5),

    ||T_infinity[(1-chi)phi_d]||_2^2 <= C N^(-3).     (9)

Indeed the gradient tail contributes sum_(r>=cN) O(r^2 r^(-6))
=O(N^(-3)), and the cutoff-derivative term contributes
N^(-2) sum_(cN<=r<=2cN) O(r^2 r^(-4))=O(N^(-3)).
Discrete products shift indices only by a bounded amount. The best
approximation property of P_N, (6) and (7), therefore imply

    ||k_(N;n,d)-k_d(. - n)||_2 <= C N^(-3/2).         (10)

The identical cutoff argument for alpha_p and curl gives

    ||Q_N e_p||_2 <= C N^(-3/2)                      (11)

for every plaquette p in a ball of radius c'N around n, with c'>0
small enough that such sources keep a common transverse buffer.
In this case the best approximation space is finite curls: cutting
off the edge potential gives a compact edge field in the relative
domain. Formula (9)'s two counts apply to curl alpha and alpha as
well. Thus (11) handles the relative curvature projection without a
Neumann Green theorem, boundary-input deletion or a mass parameter.

### 4. Quantify the actual exterior paths and the complete heat sum

Write zeta_(k,N)=Zeta_k/a, as in L101(16), and let z_(v_k(x)) be
the fixed-coefficient path map in L097. A single polynomial p(k)
can be chosen so that, for every retained label, all levels 1<=s<N,
and rows in the finite transverse cube,

    ||zeta_(k,N)|| <= C p(k),
    |path coefficient at y - frozen coefficient at x|
                  <= C a p(k)(1+|y-n|),              (12)

where x=(-4+as,-4+an) is a dipole center and lattice distance is
used on the right. The coefficients of zeta are precisely b_k/a
and q_k/a, the fixed Bb,Bq path sums of the retracted exterior column.
This assertion includes normal transverse end rows.

To verify the rate, use L028(9), (11): divided by a, the column is
the sampled A_(k,a),mu minus the transverse difference quotient of

    Phi_(k,a)(s,y)=a sum_(r=0)^(s-1)
                            A_(k,a),1(-4+(r+1/2)a,y).

L222(2), (3), (9) give its normalization and first transverse prefix
derivative error, uniformly in s. A difference quotient differs from
that derivative by at most Ca times the second derivative norm of
Phi_(k,a), bounded by a fixed polynomial in |k| since sa<=8.
This proves O(a p(k)) value error against
v_(k,mu)=A_(k,mu)-partial_mu integral_(-4)^(x_1) A_(k,1).
Differentiating the same finite prefix formula transversely once
gives a polynomial C^1 bound. Integrating that derivative along a
segment inside the transverse cube and including the fixed path
offsets proves (12). Tangential boundary values are the actual sine
zeros. No value at the upper axial pin s=N is used. The axial zero
cosine contributes its full length sa, with no decay assumption.

Let c_(i;kl,N) and c_(i;kl) be L097/L101's coefficients. For some
common polynomial q and c>0,

    |c_(i;kl,N)|+|c_(i;kl)| <= C_i exp[-c(|k|^2+|l|^2)],
    |c_(i;kl,N)-c_(i;kl)|
       <= C_i a q(k)q(l) exp[-c(|k|^2+|l|^2)]         (13)

on retained labels. Here L222(7) applies to exactly L008's two
whitened probe forms. Its proof keeps the triplet's four products
and both polarized shear products. The physical energy error in
L222(2) is O(a^2 |k|^4), while both energies are >=|k|^2/16.
The mean value theorem for exp(-tau t) gives the second estimate
after multiplying the two heat factors. Their coefficient formula
is the one in L097; no diagnostic normalization factor is inserted.
All polynomials in what follows may be enlarged to this same p,q.
The sums of their products against the exponential are finite.

### 5. Compare each ordered dipole contraction without commuting factors

Fix s,n,d,k,l as above. Extend all finite maps by zero. Set

    f_(k,N)=zeta_(k,N)(s) k_(N;n,d),
    f_k=z_(v_k(x)) k_d(. - n).

The constant path map applied to a finite relative edge field also
extends by zero exactly: every excluded plaquette has its four
candidate edges zero, by the boundary check in section 3.
On finite rows, (12), finite path multiplicity and (5) imply

    ||[zeta_(k,N)-z_(v_k(x))] k_d(. - n)||_2
                                                   <= C a p(k).

For rows outside the finite space the finite map is zero. The
full-grid comparison field there has norm <=Cp(k)N^(-3/2), since
these rows have distance at least cN from n and k_d decays as in
(5). A missing input edge in an otherwise retained path row is
also at distance at least cN from n. Its coefficient discrepancy is
bounded by Cp(k)<=Ca p(k)(1+|y-n|), so the same weighted estimate
includes every such boundary input, rather than deleting it.
Combining this observation with (10) and the first bound in
(12) gives

    ||f_(k,N)-f_k||_2 <= C p(k)(a+N^(-3/2)),
    ||f_(k,N)||_2+||f_k||_2 <= C p(k).               (14)

In particular the first estimate uses the *squared* spatial moment
of the differentiated column, not an absolute first kernel moment.
The estimate remains valid when high-label polynomial errors exceed
one; its role is a heat-summable error bound.

The frozen path field obeys |f_k(y)|<=Cp(k)(1+|y-n|)^(-3).
Split it at radius c'N. Its outside l2 norm is <=Cp(k)N^(-3/2),
and its inside l1 norm is <=Cp(k)log(eN), by the shell count in
dimension three. Equation (11) and ||Q_N||<=1 therefore give

    ||Q_N f_k||_2 <= C p(k)N^(-3/2)log(eN).          (15)

Since Q_N is an orthogonal projection, not an arbitrary difference
of bounded inverses,

    |<f_k,(S_N-S_infinity)f_l>|
      =|<Q_N f_k,Q_N f_l>|
      <=C p(k)p(l)N^(-3)log(eN)^2.                 (16)

Now telescope the two exterior factors using (14) and ||S_N||<=1,
and then use (16). This proves, in the original order,

    |<f_(k,N),S_N f_(l,N)>-<f_k,S_infinity f_l>|
      <=C p(k)p(l)[a+N^(-3/2)+N^(-3)log(eN)^2]
      <=C' a p(k)p(l).                              (17)

No scalar multiplier has been commuted through G or S_N. The signs
of the dipole coefficients and of c_(i;kl,N) have not been changed.

### 6. Identify the frozen density and do physical quadrature

Define the real bilinear density

    H_kl(x)=sum_d b_d(x)
      <z_(v_k(x)) k_d,S_infinity z_(v_l(x)) k_d>.

It has compact transverse support and satisfies
||H_kl||_(C^1(D))<=C p(k)p(l). Translation of the centered dipole
does not change its full-grid inner product. These bounds follow
from (3), ||k_d||_2<=C, bounded path multiplicity and the smooth
continuum v_k. An axial derivative of v_k differentiates its full
prefix integral and is bounded by a polynomial as well. Compact
axial support of H_kl is neither asserted nor needed.

Insert (2) into L101(16). Per dipole the exact trace is

    Tr[k_(N;n,d) k_(N;n,d)^T zeta_k^T S_N zeta_l]
                   =<f_(k,N),S_N f_(l,N)>.

There are O(N^3) possible centers per level and N-1 levels, with
finitely many d. Equations (3), (13), (17), and a^4 N^4=8^4 show
that replacing the full normalized static expression by

    sum_(retained k,l)c_(i;kl) a^4
                       sum_(s,n) H_kl(-4+as,-4+an)

costs at most C_i a. Absolute values are taken only after the exact
ordered dipole contraction; the heat sum of every error is finite.

Rectangle quadrature on the fixed four-dimensional box now costs
at most Ca times the C^1 norm and supremum of H_kl. Include the
missing lower axial strip of width a separately using its supremum;
the upper last strip is handled by the same bound. This accounts
for the possible nonzero upper cumulative tail. Transverse boundary
strips have zero density for fine meshes because b_d is compactly
supported. After the heat sum the quadrature error is C_i a.
Omitted continuum labels have at least one index >=N. Their
exponential-polynomial tail is O_i(exp(-c'N^2)), in particular O_i(a).

Finally apply full-grid Fourier Plancherel to H_kl. Equation (4)
and k_d=T_infinity Delta_infinity^(-1)h_d give

    H_kl(x)=integral_(torus) [m_E(x,theta)/lambda]
            Tr[P z_(v_k)^* S z_(v_l) P] dtheta/(2pi)^3.

The fixed finite sum over d is harmless. The symbol of its energy
sum between the two gradient inverses is (m_E/lambda)P; trace
cyclicity and P^2=P put it in precisely the displayed order.
Unitary staggered center phases cancel in this closed trace, as in
L097. Also |m_E|<=C lambda, so the integrand is bounded by
Cp(k)p(l); its value at zero frequency is immaterial. This identifies
the complete spatial and heat sum as exactly L101(5), with no color,
cell-volume or outside factor 3 added. Thus

    |a^3 T_(i,N)-K_(i,E)|<=C_i a=8C_i/N.

This proves (1). Combining it with L223's separate replacement
estimate is a triangle inequality only; it does not give a rate for
any other component or for a coupling-dependent interacting remainder.

### 7. Separate critical audit, 2026-10-17

**Verdict: accepted relative to L008, L028, L097, L101, L222 and
L223.** This is an audit of (1), not a recursive verification of these
inputs. The relative-cell definition in L003, L097's path formulas
from L088, and the normalization already used by L222
from L080/L026 were checked narrowly to settle the boundary and modal
questions below. No additional mathematical dependency is introduced.
The unchanged pre-invocation EXPLORE assessment is
`drafts/literature/2026-10-17-e-static-trace-rate-critical-audit.md`.

**Signed stencil and rate.** In L101(13), each right transverse
difference annihilates the constant vector on its supported stencil.
For its symmetrized transport term, k_j 1=0 and k_j^T Delta 1=0:
Delta 1 has rows only adjacent to a transverse face, whereas every
nonzero row of k_j is separated from those faces. The shear and
triplet terms, and the moving-cut T_mu^T M_u T_mu term, have right
differences as well. This proves C_(s,N)1=0 on *all* vertex rows.
Symmetry then makes the diagonal exactly the negative off-diagonal
row sum. Selecting one of d,-d counts every off-diagonal pair once
in (2), including rows in the fixed stencil enlargement. No positive
form assertion is needed for this signed decomposition.

For (3), one must cancel the nominal 1/a transport coefficients
before estimating them. The exact commutator identity L101(15) does
this: each coefficient is a fixed sum of smooth coefficient differences
divided by a. L028(4) gives C^r errors O(a^2) for u_a,w_a,s_a;
the integral first-difference formula and bounded second derivatives
give O(a) error for each resulting single-layer coefficient. In
a sum_(j<s)L_j, at most N such errors are multiplied by a, giving
O(a), since aN=8. The coefficientwise rectangle error is O(a)
uniformly in its moving cut. The quarter layer contributes O(a).
The triplet endpoint averages have the same uniform coefficient bound.
Finally a times the explicit 1/(2a) cut term is precisely the retained
T_mu^T M_(u_(a,1)(s)) T_mu/2. Its comparison uses smooth u_a at the
actual cut, not a zero upper boundary value. These facts verify (3)
and the coefficient-level identification (4), including the upper
cumulative tail. Only the limiting b_d needs the stated C^1 bound;
no derivative of a rough inverse or projection is taken.

**Relative extension and both best approximations.** A degree-I
relative component uses N edge positions in directions I and N-1
interior vertex positions in the other directions. Extend it by zero
on the full lattice of oriented cells. For the forward differential,
each new outside row either has entirely outside inputs or has a
tangential face input, which is zero. Inside normal end rows use the
actual difference to the zero face value. At a corner the same argument
applies coordinate by coordinate. Thus E_1 T=T_infinity E_0 and
E_2 C=C_infinity E_1, with isometric E_r. There is no assertion about
intertwining their adjoints. In particular the finite curl range is
the range of the extended finite relative curl, exactly the S_T range
specified in L097(1), rather than the range of a scalar Dirichlet
inverse on all link components. This proves the inclusions used in
(7). Nested means inclusion in the corresponding full-grid range;
no comparison between two different physical meshes is required.

The scalar citations in section 2 apply to each component dipole of
alpha_p as well as to phi_d. Outside a ball containing the finitely
many source points, take a harmonic ball of radius comparable to the
source distance. The first-difference Green bound is O(r^-2) there,
so the harmonic difference estimate gives O(r^-3) for its gradient
or curl. This verifies the mixed differences in (5). The shell counts
are sum_(r>=R) r^2 r^-6=O(R^-3) for energy tails, and
R^-2 sum_(R<=r<=2R) r^2 r^-4=O(R^-3) for cutoff derivatives.
Cutoff supports fit entirely inside the cube by the fixed transverse
buffer, uniformly over every dipole center and all axial cuts.
They are admissible finite relative potentials in degrees zero and
one respectively. Orthogonal best approximation therefore gives
(10) and (11) with norm error O(N^-3/2). In particular the second
comparison approximates S_infinity e_p by a *curl*, as required;
it does not approximate its potential in an unrelated scalar space.

For (15), the near part has l1 norm O(p(k)log(eN)) and every one of
its plaquette sources has the same buffer. The triangle inequality
and (11) bound its Q_N image. The far part has l2 norm
O(p(k)N^-3/2), and Q_N is a contraction. Since Q_N is itself an
orthogonal projection, its bilinear error is the product of these
two image norms, exactly as in (16). Both this squaring and the
finite second spatial l2 moment in (5) are legitimate; an absolute
first spatial moment is neither asserted nor needed.

**Actual modal paths and heat coefficients.** For a component label k
write r=|k|. The smooth pre-retraction mode is A_(k,a)=f_k/sqrt(lambda_(k,a)),
with constant axial factor 1/sqrt(8) when present. L222(2)--(3) give
||A_(k,a)||_(C^m)<=C_m r^(m-1) and mode normalization error
O(a^2 r^(m+1)). At an interior axial level s, on a transverse
mu-edge with tail y, the exact retracted value divided by a is

    A_(k,a),mu(s,y+a e_mu/2)
       -[phi_(k,a)(s,y+a e_mu)-phi_(k,a)(s,y)]/a.

This formula also holds on a *normal transverse end edge*: at its
boundary endpoint A_1 is a tangential component, hence has exact sine
value zero on every axial input level. The prefix there equals the
prescribed pinned vertex value zero. Tangential face links themselves
are zero for the same reason. No assertion from L028 restricted to
two interior endpoints has been extended by fiat. No formula at s=N
has been used. At axial label zero the prefix is its full length sa
times the transverse factor; it satisfies the same derivative bounds.

L222(9) compares the transverse derivative of this prefix with its
continuum counterpart with error C(ar+a^2 r^2). Comparing its edge
quotient with that derivative costs at most Ca times its transverse
C^2 norm, bounded by Cr. The direct term and the fixed path shifts
have polynomially bounded error as well. Differentiating the smooth
finite prefix in transverse coordinates gives a C^1 bound for the
entire displayed edge coefficient, since its physical length is at
most 8. Thus the two actual Bb/Bq sums have the value error and
within-cube Lipschitz bounds in (12), uniformly in s and every retained
label. Their fixed number of edge slots gives the operator norm bound.
Excluded input slots in a boundary path are at distance at least cN
from the compact dipole center. Their bounded coefficient error is
therefore also bounded by Ca p(k)(1+distance), since aN=8. Together
with (5) and (10), this verifies (14) on the complete extended space.
The assertion about an excluded plaquette row is valid because all
its candidate relative input edges vanish on that row.

The heat coefficient is exactly
c_(i;kl,N)=exp[-tau(lambda_(k,a)+lambda_(l,a))]B_(i,a;kl),
as in the normalization imported by L097. L222(7) applies to that
same whitened form: it retains all four triplet products and both
shear polarizations from L008. Both physical energies are bounded
below by |k|^2/16. The exponential mean value theorem, together with
|lambda_(k,a)-lambda_k|<=Ca^2|k|^4, bounds the heat difference by
Ca^2(|k|^4+|l|^4)exp[-c(|k|^2+|l|^2)]. Add the L222(7) form error
to obtain (13), for a<=1. Enlarging fixed polynomials covers every
retained label, even when its upper error estimate exceeds one.
The exponential times every such polynomial is summable over the
four-dimensional component labels. Omitted labels have an index at
least N and an exponentially small polynomially weighted tail.
This checks the *full* heat sum, rather than only fixed-mode convergence.

**Ordered trace and physical normalization.** In (16) of L101,
insert (2) into T G C_(s,N) G T^T before taking a trace. Each term is
exactly b_(d,N)<f_(k,N),S_N f_(l,N)> with the order in section 6.
The errors (3), (13), (17) are O(a) after multiplication by a^4
and counting O(N^4) centers and levels. The C^1 bounds for H_kl
give the same quadrature error; its potentially nonzero axial endpoint
strips have volume O(a) and bounded density. No axial compact support
of the cumulative insertion is used. The finite d sum has Fourier
matrix sum_d b_d k_hat_d k_hat_d^*=(m_E/lambda)P. Hence its closed
trace has exactly L101(5)'s integrand, with the staggered unitary
phases canceled in the closed trace. There is no color factor, cell
factor or other/other assembly factor 3 to insert. These checks yield
|a^3 T_(i,N)-K_(i,E)|<=C_i a and hence the O(N^2) unnormalized error.

This validates the existing standard-method rate and its triangle
inequality with L223, not a new rate beyond the checked sources.
ATTEMPTS/024--025/030 concern profile replacements, absolute-norm
gains or uncontrolled varying-mass limits; none is used here. Other
component rates, the complete response and interacting construction
remain outside this audit. No numerical premise or script is required.

## Mathlib

Full matching cumulative-trace rate: **not checked**. Supporting
orthogonal projections, Fourier Plancherel, finite-dimensional
quadratic forms, cutoff energy estimates and quantitative rectangle
quadrature: **not checked**. No absence of a matching theorem is
asserted. The scalar Green inputs are the precise Lawler–Limic
citations above; the local cochain specialization and trace comparison
are proved here under the saved EXPLORE assessment.
