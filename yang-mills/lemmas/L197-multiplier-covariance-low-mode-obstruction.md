# L197 — The actual multiplier covariance commutator retains cubic norm

## Hypotheses

Use L182 and L187's SU(2) relative box (-4,4)^4, admitted even
N>=4, a=8/N, straight direction-1 lower-rooted forest, and ordinary
dimensionless full variable-link coordinates. Keep every physical
face, all normal end edges and the constant own-direction modes.
Vertex potentials are pinned on every boundary vertex. In particular

    Sigma_H=(L+DD^T)^(-1), P=I-D(D^T D)^(-1)D^T,
    S=P Sigma_H P, V=q Phi.

Here q adds the two vertex endpoint values, with pinned endpoint
values zero; Phi is the original lower prefix. Let Pi select all
upper direction-1 normal variable edges, without commuting Pi with P.

Take the ordinary normalized component-1 relative product modes

    u=e_(0,1,1,1), v=e_(0,3,1,1), n=S u,
    alpha=Vn,
    Z=P diag(alpha)P,
    Z_b=P diag((I-Pi)alpha)P.                           (1)

These are actual covariance modes and L188's actual multiplier for
the external mode k=(0,1,1,1). No synthetic S, prefix or multiplier
is substituted. The mode pair u,v is a test of an operator estimate;
it is not asserted to be a term with nonzero weight in either actual
probe's complete heat expansion. The commutator convention is
[X,Y]=XY-YX.

## Conclusion

For either Z_*=Z or Z_b,

    lim_(N->infinity) N^(-3) <u,[S,Z_*]v>
       = -8192 sqrt(2)/(13365 pi^7) != 0,              (2)

along admitted meshes. Consequently

    ||[S,Z]||_op=Theta(N^3),
    ||[S,Z_b]||_op=Theta(N^3).                         (3)

In particular a factorwise o(N^3) covariance-commutator estimate,
including O(N^(5/2)), is false for these actual external-mode
multipliers. Deleting only the multiplier's upper normal row does
not fix it. Every covariance input and projection row remains.

This stops a proposed way to recover the half-power missing from
L188's multiplier estimate; it does not stop its signed trace in
L194's joint group. There is no lower bound here for [M,Z], Q_3,
either actual-probe response or their scaled limits. The full joint
bound remains O(N^(7/2)), the sextic retains its logarithmic loss,
and transport is only cubic-bounded by L196. Independent probe jets,
full compensation, finer asymptotics, finite matching, reflected
error <=c_box/2 and continuum/infrared construction remain unresolved.

## Proof

### 1. Exact modes, including the constant axial mode

Label component-1 edges by (s,j), s=0,...,N-1 and
j=(j_2,j_3,j_4) in {1,...,N-1}^3. Their endpoints have axial
vertex levels s and s+1. Put

    w(j)=prod_(r=2)^4 sin(pi j_r/N),
    w'(j)=sin(3 pi j_2/N) sin(pi j_3/N) sin(pi j_4/N),
    c_N=sqrt(8)/N^2.

The two modes are zero on every other link component and satisfy

    u_1(s,j)=c_N w(j), v_1(s,j)=c_N w'(j).             (4)

The axial factor is the normalized constant edge mode N^(-1/2).
Each transverse normalized sine factor is sqrt(2/N) times its sine.
Thus (4) has ordinary norm one, and u,v are orthogonal for N>=4.
This uses the exact relative product spectrum and normalization in
L026(6)–(7), also used in L182 and L187, with the own-direction zero
index retained.

At every interior vertex, the two axial entries in D^T u cancel;
all other components are zero. The same is true for v, including
vertices adjacent to either pinned axial face. Hence Pu=u, Pv=v.
The relative Hodge eigenvalues are exactly

    lambda_u=12 sin^2(pi/(2N)),
    lambda_v=4[sin^2(3 pi/(2N))+2 sin^2(pi/(2N))].      (5)

The eigenvalue formula can also be checked directly: transverse sine
differences give 4 sin^2(k pi/(2N)); the axial edge difference is zero
on the constant mode. End-edge rows impose the same relative axial
condition, not scalar Dirichlet conditions on this component. Since
P commutes with Sigma_H, as in L182, Su=lambda_u^(-1)u and
Sv=lambda_v^(-1)v. In particular

    n_1(s,j)=gamma_N w(j),
    gamma_N=c_N/lambda_u -> 2 sqrt(2)/(3 pi^2).         (6)

### 2. Evaluate the prefix on every upper and lower row

For an interior axial vertex level t=1,...,N-1 the lower prefix is

    (Phi n)(t,j)=t gamma_N w(j).

Its boundary values at t=0 and t=N are both zero. The upper value
is the pinned value, not the continuation N gamma_N w(j).
Endpoint addition on component-1 edges therefore gives

    alpha_1(s,j)=gamma_N w(j) theta_s,
    theta_s=2s+1 for 0<=s<=N-2,
    theta_(N-1)=N-1.                                  (7)

All transverse endpoint rows in alpha are still present in (1).
They do not enter the particular matrix element because u and v
have only component 1. No covariance or projection is restricted
to component 1 by this observation.

Since u,v lie in im P, the two P factors in (1) disappear only
inside <u,Z_* v>. Define the exact finite sums

    A_N=(2/N) sum_(j=1)^(N-1) sin^2(pi j/N) sin(3 pi j/N),
    B_N=(2/N) sum_(j=1)^(N-1) sin^3(pi j/N).

The sums of the axial weights in (7) are

    sum_s theta_s=N(N-1),
    sum_(s=0)^(N-2) theta_s=(N-1)^2.

Multiplying the three transverse sums and using c_N^2=8/N^4
now yields the exact identities

    <u,Zv>=gamma_N (N-1) A_N B_N^2,
    <u,Z_b v>=gamma_N (N-1)^2/N A_N B_N^2.             (8)

Thus the upper-row contribution to this matrix element is only
gamma_N (N-1)/N A_N B_N^2. We have not commuted Pi through P,
and make no operator-norm assertion about that upper-row term alone.

### 3. The nonzero limit and matching operator upper bound

Riemann sums of these continuous trigonometric functions give

    A_N -> 2 integral_0^1 sin^2(pi x)sin(3 pi x) dx
            =-8/(15 pi),
    B_N -> 2 integral_0^1 sin^3(pi x) dx=8/(3 pi).      (9)

For the first integral use
sin^2(t)sin(3t)=sin(3t)/2-[sin(5t)+sin(t)]/4;
the integral before multiplication by two is -4/(15 pi).
For the second, sin^3(t)=[3sin(t)-sin(3t)]/4 gives
4/(3 pi) before multiplication by two. This establishes all signs
and constants without numerical quadrature.

By symmetry of S and its two eigenvector identities,

    <u,[S,Z_*]v>
       =(lambda_u^(-1)-lambda_v^(-1)) <u,Z_*v>.        (10)

Moreover N^2 lambda_u ->3 pi^2 and
N^2 lambda_v ->11 pi^2, so the eigenvalue difference divided by
N^2 tends to 8/(33 pi^2). Equations (6), (8) and (9) show that
<u,Z_*v>/N tends, for both choices, to

    [2 sqrt(2)/(3 pi^2)] [-512/(135 pi^3)].

Their product is precisely (2). Since u,v are unit vectors, (2)
gives a c N^3 lower operator bound for all sufficiently large
admitted N, with a fixed c>0.

For completeness, the full relative spectral gap gives
||S||_op<=C N^2. Equation (6) gives |n|<=C uniformly. Every
interior prefix contains at most N entries, so its supremum is
at most C N, and bounded endpoint addition gives
||alpha||_infinity<=C N on every component and face. Hence
||Z||_op+||Z_b||_op<=C N. The elementary commutator estimate
||[S,Z_*]||_op<=2||S||_op ||Z_*||_op proves the upper bounds
in (3). This also verifies that the test saturates the product
order rather than exhibiting growth beyond the established bound.

### 4. What this rules out in the joint trace

For the actual supported residual A with both insertion subtractions,
M=2SAS obeys the exact identity

    [M,Z]=2SA[S,Z]+2[S,Z]AS+2S[A,Z]S.                 (11)

Expanding the three brackets verifies it in the displayed order;
the two middle products cancel. No positivity or commutation of A
is used. The attempted shortcut was to estimate the covariance
brackets separately with a half-power improvement over their
O(N^3) product bound, before using the remaining rough residual
form estimate. Equations (2)–(3) forbid that uniform improvement,
even after the multiplier's upper row is removed. The responsible
matrix element connects distinct fixed physical frequencies: local
small neighboring differences do not force a small covariance
commutator at these low modes.

This does not prohibit bounds that use J_y, A, the action slices
or cancellations among (11)'s terms before taking norms. In
particular L194(5) retains both rough placements 2s_n S together
with U_n^T; they have not been evaluated, removed or bounded by
this test. No claim about nonzero actual-probe heat weights or
a signed response follows from an operator-norm test. The correct
next mechanism must retain that joint structure rather than repeat
the ruled-out factorwise covariance gain. All existing work and
ATTEMPTS/039–043 remain intact. No script or finite numerical
diagnostic is required for the exact formulas and limits above.

## Mathlib

Full matching actual-multiplier asymptotic and supporting relative
box spectrum: **not checked**. Supporting finite matrix commutators,
trigonometric sums and Riemann integration coverage: **not checked**;
unknown coverage is not an absence claim. The standard inputs are
the finite tensor-product spectral decomposition already justified
in L182/L187 and Riemann-sum convergence for continuous functions.
The necessary local specialization is the exact mode normalization,
the pinned upper prefix and the nonzero matrix element (8)–(10).
No general spectral or renormalization theorem is reproved. The
unchanged [approved assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
covers this bounded test within the original joint-group target.
This is local standard-method obstruction evidence, with no claim
of novelty beyond the checked literature or of a negative answer
to the selected response-limit question.
