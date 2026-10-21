# L178 — Cubic-scale control of finite transverse polynomial approximation

## Hypotheses

Keep L177's exact hypotheses and conventions: SU(2), relative box
(-4,4)^4, a=8/N through admitted even meshes, the straight direction-1
lower-rooted forest, the complete compact displacement and both actual
L010 probes i=3,6 at tau=1/16. The bare expansion is at fixed mesh
before refinement. All matrices use ordinary stored coordinates.
Keep L175's full symmetric A^gen, signed J_j, endpoint-sum S,
action multipliers m_(j,l), exterior columns h_k and heat coefficients
c_(i;kl). All action faces, normal end links and heat modes remain.

Write T_N for nearest-neighbor adjacency on the transverse interior
vertices {1,...,N-1}^3. The scalar Dirichlet Laplacian is
Delta_T=6I-T_N, including its end-edge diagonal contributions. For
fixed 0<epsilon<=1 and integer d>=0 set

    rho=6/(6+epsilon),    B_N=T_N/(6+epsilon),
    Q_(d,N)=(6+epsilon)^(-1) sum_(n=0)^d B_N^n,
    G_(epsilon,N)=(Delta_T+epsilon I)^(-1).             (1)

For two transverse vertex matrices Q_1,Q_2 define exactly

    W_i[Q_1,Q_2]=-6 sum_(k,l) c_(i;kl) sum_(j=2)^4
      Tr[(M tensor Q_1) m_(j,l) J_j
             (P tensor Q_2) E_1 A^gen M_(h_k) S],      (2)

where M_st=min(s,t), 1<=s,t<N, and P_(t,r)=1_(0<=r<t)
for component-1 edge levels 0<=r<N. In particular L177(4) is
W_i^(epsilon,epsilon)=W_i[G_(epsilon,N),G_(epsilon,N)].
Equation (2) is a bilinear trace definition, not a replacement field
law. Its coefficients and axial profiles are not frozen or commuted.

## Conclusion

There is C_i independent of N,epsilon,d such that

    |W_i[Q_1,Q_2]|<=C_i N^3 ||Q_1||_abs ||Q_2||_abs,
    |a^3(W_i^(epsilon,epsilon)-W_i[Q_(d,N),Q_(d,N)])|
                    <=C_i epsilon^(-2) rho^(d+1).       (3)

Here ||Q||_abs is the maximum of the absolute row and column sums.
The first inequality holds for arbitrary real Q_1,Q_2. The second
is uniform over every admitted mesh. Each Q_(d,N) has transverse
range at most d; neither axial profile is shortened. Thus the
polynomial approximation error can be removed after a mesh limit,
at fixed mass, without a mesh-dependent approximation degree.

If, separately, a^3 W_i[Q_(d,N),Q_(d,N)] has a limit for every fixed
d at a given epsilon, then a^3 W_i^(epsilon,epsilon) has a finite
limit, and the polynomial limits converge to it with the error in
(3). This is a conditional transfer only: convergence of the actual
finite-range traces, their signed coefficient and mass removal still
need proof. No V_i limit or complete-response vanishing is asserted.
This is local standard-method REPRODUCTION, without a novelty claim.

## Proof

### 1. Actual local stencil bounds before absolute values

The two orders in A^gen=(L K_a+K_a^T L)/2 use the unscaled
L=D_1^T D_1 and K_a=a^(-1) E M_u C D_1. L028's complete
endpoint/clover compositions, including the reversed adjoint order,
have a fixed number of shifts and uniformly bounded coefficients
u_a. Consequently there are constants R,b,C, independent of N,
such that A^gen has range R, at most b nonzero entries in each row
and column, and

    |(A^gen)_(ef)|<=C/a.                               (4)

The entire input and output support lies in a fixed compact interior
enlargement of displacement support for sufficiently fine meshes.
This includes coefficient differences in the adjoint; it is not a
constant-coefficient assertion. Enlarge C to cover the finitely many
remaining admitted meshes if needed. The endpoint map S has at
most two nonzero entries per row and bounded incidence per column.

L159(6) gives the global action extension, including normal end links,
and L175(8)'s supported exterior bound gives, with one fixed enlarged
polynomial p,

    ||m_(j,l)||_infinity<=C a^3 p(l),
    |(h_k)_f|<=C a p(k) when column f of A^gen is nonzero.
                                                               (5)

The second bound is used only on compact residual input links. It
does not extend the forest lift smoothly across its pinned upper
jump. All upper action terms remain in the first bound.

### 2. Count the two long profiles in the original trace order

Fix k,l,j and put x=(s,X), y=(t,Y), z=(t,Z) for interior vertices,
where capitals denote transverse coordinates. An expanded summand
of the trace in (2) has factors in precisely the order

    M_st (Q_1)_(XY) m_(j,l)(t,Y) (J_j)_(YZ)
        P_(t,r) (Q_2)_(ZU) (A^gen)_(ef) (h_k)_f S_(fx),
                                                               (6)

with e the component-1 edge at axial level r and transverse vertex U.
The equal axial level in J_j is because j=2,3,4; E_1 has selected
exactly this component-1 edge, including both end levels. This
expansion retains m at t, h at its actual link f, and A^gen between
the second prefix and h. It moves none of these factors.

Whenever (A^gen)_(ef) S_(fx) is nonzero, stencil locality and the
endpoint condition imply |r-s|<=R' for one fixed R'. For given
x,r,U there are at most b' choices of f, independent of N. The
transverse positions U are also close to X, but no estimate needs
that further restriction. The omitted cases have zero summand.

Bound (A^gen)_(ef) (h_k)_f and m by (4)-(5), giving the total scalar
factor C a^3 p(k)p(l). Keep M_st and P_(t,r) as their exact
nonnegative numbers. The absolute row sum of J_j is at most two,
including rows adjacent to transverse boundary vertices. For each
fixed X, summing over Y,Z and enlarging the allowed U set to all
transverse interior vertices gives

    sum_(Y,Z,U) |(Q_1)_(XY)| |(J_j)_(YZ)| |(Q_2)_(ZU)|
                         <=2 ||Q_1||_abs ||Q_2||_abs.   (7)

This is a row-sum inequality for a product of absolute matrices,
not a commutation or localization of the original trace.

There are (N-1)^3 closing transverse vertices X. Its exact axial
weight is bounded by

    sum_(s,t=1)^(N-1) sum_(0<=r<N, |r-s|<=R')
                         min(s,t) 1_(r<t)
       <=(2R'+1) sum_(s,t=1)^(N-1) min(s,t)
       =(2R'+1) (N-1)N(2N-1)/6
       <=C N^3.                                       (8)

The equality follows from min(s,t)=sum_(v=1)^(N-1)
1_(v<=s)1_(v<=t), so its sum is sum_(v=1)^(N-1)(N-v)^2.
Using 1_(r<t)<=1 in an upper bound removes no row from (2); both
profiles and their true endpoint values remain in its definition.
In particular (8) is not a bounded-operator claim about P or M.

Equations (4)-(8) bound one trace by
C a^3 N^6 p(k)p(l) ||Q_1||_abs ||Q_2||_abs, which equals
C N^3 p(k)p(l) ||Q_1||_abs ||Q_2||_abs since aN=8.
Sum the three transverse directions and the absolute heat weights.
L156(8) gives the full-spectrum summability
sum_(k,l)|c_(i;kl)|p(k)p(l)<=C_i. This proves the first inequality
of (3), with the original -6 included once. No color or pairing
factor is added, and no exterior mode is cut off.

### 3. Finite Neumann approximation with pinned end rows

T_N is real symmetric and nonnegative entrywise. Each row and column
sum is at most six, with smaller sums at the Dirichlet boundary.
Thus ||B_N||_abs<=rho<1. Absolute row/column sum norm is
submultiplicative, by the finite triangle inequality, so the geometric
matrix series converges absolutely in this norm. Multiplication of
its finite partial sums by I-B_N gives I-B_N^(d+1); the remainder
tends to zero. Since Delta_T+epsilon I=(6+epsilon)(I-B_N), this
proves the exact Neumann resolvent identity and

    G_(epsilon,N)-Q_(d,N)=B_N^(d+1) G_(epsilon,N),
    ||G_(epsilon,N)||_abs<=epsilon^(-1),
    ||Q_(d,N)||_abs<=epsilon^(-1),
    ||G_(epsilon,N)-Q_(d,N)||_abs
                       <=epsilon^(-1) rho^(d+1).       (9)

Every matrix in (9) is nonnegative entrywise. The geometric estimate
uses the killed finite-box adjacency, rather than a periodic kernel
or infinite-grid extension. In particular its diagonal remains six
at transverse end rows. A power B_N^n connects only vertices of
Manhattan distance at most n, proving the stated finite range.

Use bilinearity of (2) to telescope in the original order:

    W_i[G,G]-W_i[Q,Q]
                  =W_i[G-Q,G]+W_i[Q,G-Q].              (10)

The first inequality of (3) and (9) bound the right side by
2 C_i N^3 epsilon^(-2) rho^(d+1). Multiplication by a^3=512/N^3
and enlargement of C_i prove the second inequality of (3).
This estimate is uniform in N at each fixed mass and degree, and
tends to zero as d tends to infinity at that fixed mass. It does
not supply a bound uniform as epsilon tends to zero; L177's
independent mass-removal estimate remains necessary.

### 4. What the estimate transfers and what it does not

Let E_d=C_i epsilon^(-2)rho^(d+1). If each polynomial trace has
a scaled mesh limit L_d, (3) implies
|L_d-L_e|<=E_d+E_e by comparing both finite traces to the same
massive trace before taking their limits. Thus L_d is Cauchy and
converges to a finite L. For any fixed d,

    limsup_N |a^3 W_i^(epsilon,epsilon)-L|
                                      <=E_d+|L_d-L|.

Let d tend to infinity to prove the conditional convergence and its
error bound. No existence of any L_d has been used as an established
input elsewhere in this result.

The meaningful check here is the complete analytic count (6)-(10):
the transverse row sums, the exact axial min/prefix weights, and the
actual supported coefficient scales give precisely N^3, rather than
an above-threshold error. No numerical certificate or new mathematical
script is needed. L175-L177 previously left polynomial approximation
unproved, so this is not a repeated mass-removal argument. All signed
finite-range limits, actual coefficient evaluation and the comparison
lim a^3 V_i=6K_(i,R)-K_(i,T) remain unresolved. Other response jets,
finer powers/logarithm, full compensation, interacting reflected error,
continuum axioms and infrared finite mass are independent remaining gaps.

### 5. Separate critical audit of the uniform polynomial transfer

The 2026-10-21 audit accepts (3) and its conditional transfer relative
to the imported L028/L156/L175 bounds. No correction is required.
This validates the existing specialization, not a new mathematical
discovery or an independent audit of those imports.

The rectangular spaces in (6) are compatible: x and y are interior
vertices, J_j changes only the transverse vertex, and P maps all N
component-1 edge levels to the N-1 vertex levels. Closing through S
and the local generator permits only boundedly many r-s, f and U-X.
Dropping the latter restriction enlarges the absolute sum and makes
(7) valid for arbitrary real Q_1,Q_2. In particular no positivity,
commutation or common eigenbasis of these matrices is required.
The bound on h is used only at the compact generator input f; the
global bound on m retains the upper action rows. L175(7)--(8) and
L156(8) have exactly the supported exterior and heat conventions used
here, and L028's two ordered compositions give (4).

For the full count, each summand's deterministic scale is
a^3*a^(-1)*a=a^3, the closing transverse count is O(N^3), and
the weighted axial count in (8) is O(N^3). Its exact uncut value is
sum_(v=1)^(N-1)(N-v)^2=(N-1)N(2N-1)/6. Thus the resulting
a^3 N^6 is O(N^3). The actual cut and all end rows remain in the
defined trace; bounding their indicator by one is only an inequality.
The three transverse directions and sole -6 enter the constant once.

The killed adjacency is symmetric, nonnegative, and has row/column
sums <=6 even at end rows, while Delta_T retains diagonal six.
Hence (9) follows in the stated submultiplicative norm, including
d=0. Applying the first bound of (3) separately to the two placements
in (10) gives 2 C_i N^3 epsilon^(-2)rho^(d+1); multiplication by
a^3 removes N^3 with the fixed factor 512. The constant is uniform
in N,epsilon,d after retaining the displayed mass loss. L156(8)'s
polynomially weighted Gaussian bound sums every exterior label for
both probes, including allowed constant edge indices.

Finally the conditional transfer uses two polynomial traces compared
to the same massive finite trace, then a mesh limit at fixed degrees.
Their limits are Cauchy as d increases, and the displayed limsup
estimate proves convergence of the massive sequence. It neither
assumes that conditional premise nor supplies a varying-degree or
zero-mass theorem. L179 supplies the premise separately. The audit
adds no direct mathematical input and changes no rate or argument.

## Mathlib

Full matching theorem: **not checked**. Supporting finite Neumann
series, absolute matrix row/column sums and finite trace inequalities:
**not checked**. Unknown coverage is not absence. Reuse the unchanged
[assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md).
No external theorem is imported or reproved. The elementary matrix
identities are proved above because the needed specialization must
control a trace with two different long axial profiles, variable
coefficients and the exact pinned-generator order at cubic scale.
