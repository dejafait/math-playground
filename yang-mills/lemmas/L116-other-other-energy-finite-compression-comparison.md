# L116 — Joint energy compression errors vanish at cubic scale

## Hypotheses

Use exactly L115's R_prod for both actual L010 probes i=3,6, SU(2),
straight lower-rooted direction-1 forest, all-face relative fixed-link
box (-4,4)^4, sufficiently fine admitted even N, a=8/N and tau=1/16.
Take the bare small-coupling coefficient at fixed mesh before refinement.
All spaces have ordinary stored-coordinate norms. Retain both axial
levels, all transverse end rows, both generator orientations, all path
and component filters and every exterior heat mode.

Import J_1,J_2,P_inf,P_bulk from L114/L115, and A_r,E_j,b_(r,t)
from L111/L115. On the infinite edge and plaquette Hilbert spaces
H_1,H_2 over Z^3 set Q_q=J_q J_q^* for q=1,2. These are coordinate
selectors, distinct from the co-closed projections used elsewhere.
Let S_alpha^inf be L113(1)'s same two-edge path stencil on the full
grid, with all component selectors and signs unchanged. Define

    f_(kl;alpha,beta;r;st)(x)
      =b_(r,t)(x) phi_(l,alpha,s)(x) phi_(k,beta,t)(x).       (1)

These are the globally extended scalar functions of L111/L113,
multiplied at common lower-vertex indices. They multiply all plaquette
components. No staggered values or the two levels have been identified.
The support of (1) lies a distance delta N from each transverse face,
for a fixed delta>0 independent of labels and levels, by compact
displacement support. Its size is at most C N^3, and
||f||_infinity<=C p(k)p(l), where
sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i as in L111/L115.

## Conclusion

Define the full-grid comparison, in the original filter order, by

    R_inf=a sum_(k,l,s,t,alpha,beta,r) c_(i;kl,a) min(s,t)
       Tr_H1[P_inf S_beta^inf A_r E_(t-s)
                     M_f (S_alpha^inf)^*].                    (2)

Each trace is well-defined: M_f has finite rank and all other factors
are bounded. There is a nonnegative sequence eta_N, independent of
heat labels and coefficient levels, such that eta_N -> 0 and

    |R_prod-R_inf| <= C_i N^3 eta_N=o(N^3).                    (3)

In particular a^3(R_prod-R_inf) -> 0. The retained full-grid expression
also has the exact diagonal form

    R_inf=a sum_(k,l,s,t,alpha,beta,r) c_(i;kl,a) min(s,t)
          kappa_(alpha,beta,r;t-s) sum_(x in Z^3) f(x),         (4)

where, using the unshifted periodic phases of L110,

    kappa_(alpha,beta,r;j)
      = integral tr_3[(S_alpha^inf(theta))^*
            P_inf(theta) S_beta^inf(theta) A_r(theta) E_j(theta)]
                                                   dtheta/(2pi)^3. (5)

The integral is over [-pi,pi]^3. Equation (4) does not assert a
cancellation for arbitrary separate alpha,beta,r or for the actual
coefficient sum. No bound or limit for R_inf itself is established.
Thus no cubic bound or limit for transverse H, no complete other/other
limit, and no comparison with -12 gamma D_i follows here. Earlier
L110/L111/L113/L115 errors remain only O(N^3) and may contribute to
that coefficient. Independent interacting, continuum and mass gaps
remain open.

## Proof

### 1. Lift the finite paths and keep compact support on the input

For the two-edge path maps B_b,B_q in L113(1), each finite plaquette
row is the same signed pair of edge samples as on the full grid;
a pinned tangential boundary edge has zero value and no stored row.
Retained normal end edges are included once with their original sign.
Extending an admissible finite edge array by zero therefore gives
exactly the finite path map after plaquette restriction. Transposing
this identity and applying its plane selector proves

    S_alpha=J_1^* S_alpha^inf J_2.                          (6)

There is no reweighting or identification of boundary rows in (6).
Let R be a fixed integer larger than the ranges of every S_alpha^inf
and A_r and of their products. Since f is supported in the fixed
physical interior, for sufficiently large N every edge sampled by
(S_alpha^inf)^* at a nonzero row of M_f is a retained interior edge.
Every such plaquette row is retained too. Hence, exactly,

    M_f Q_2 (S_alpha^inf)^* Q_1=M_f (S_alpha^inf)^*.         (7)

This is an identity about input columns in the complete trace; it
says nothing about the output support of E_j M_f.

Fix all labels and write j=t-s. Insert P_bulk=J_1^* P_inf J_1
and (6) into the finite trace in L115(2). The identity
Tr_finite(J_1^* B J_1 C)=Tr_H1(B J_1 C J_1^*) and (7) give

    T_fin=Tr_H1[P_inf Q_1 S_beta^inf Q_2
                             A_r E_j M_f (S_alpha^inf)^*]. (8)

All products here have finite rank. In particular trace cyclicity
does not invoke an unbounded infinite Green inverse. P_inf is the
bounded projection defined by its multiplier in L114, and E_j is
the bounded multiplier of L110.

### 2. Isolate precisely the omitted output rows

The difference between (8) and the summand of (2) is

    T_fin-T_inf=Tr_H1[P_inf B E_j M_f (S_alpha^inf)^*],
    B=(Q_1-I) S_beta^inf A_r
                         +Q_1 S_beta^inf (Q_2-I) A_r.     (9)

This follows by inserting and subtracting Q_1 S_beta^inf A_r.
No filter has moved across P_inf, nor across E_j.

Let K_N be one finite set of plaquette component indices containing
the supports of all f, of size at most C N^3. It can be chosen at
distance delta N from all faces. A row omitted by Q_1 is outside
the relative edge index set, including its omitted tangential face
rows. A row omitted by Q_2 is outside the corresponding relative
plaquette index set. For either kind, every index within R steps of
an omitted row has distance at least delta N-R from K_N. Thus for
large N it has distance at least c N, with a fixed c>0.

In the first term of B, restrict the input of the stencil
(Q_1-I) S_beta^inf A_r to the union Lambda_1 of just these R-nearby
plaquette indices; the restriction changes nothing. In the second,
(Q_2-I) A_r similarly samples only a set Lambda_2. Both sets may
be infinite. For h=1,2 every x in Lambda_h and y in K_N obey
|x-y|>=c N. All coordinate restrictions and fixed stencils in (9)
have norms bounded independently of N. The omitted rows are therefore
controlled by the tail of E_j from K_N, without ever declaring its
output compact.

### 3. Use the full quadratic kernel tail

Write e_j(z) for L110's full 3-by-3 kernel and put

    q_j(N)=(sum_(|z|>=c N) |z|^2 ||e_j(z)||_F^2)^(1/2),
    eta_N=sum_(j in Z) q_j(N).                           (10)

L110(2) gives q_j(N)<=Q_j<=C(1+|j|)^(-3/2), and the latter is
summable. For each fixed j, q_j(N)->0 because the full weighted
square sum is finite. To see eta_N->0 explicitly, first choose J
so sum_(|j|>J) Q_j is arbitrarily small, uniformly in N; then take
N large so the finite sum over |j|<=J is arbitrarily small. This
uses no convergence rate or mesh-dependent mass substitution.

For either Lambda_h, entrywise squaring and summing all output rows
gives

    ||R_Lambda_h E_j M_f||_HS^2
      <= ||f||_infinity^2 |K_N|
                              sum_(|z|>=c N) ||e_j(z)||_F^2
      <= C p(k)^2 p(l)^2 N q_j(N)^2.                    (11)

Here R_Lambda_h is its coordinate selector. The Frobenius norm
includes all component pairs, so the counting also covers differing
component index sets. Infinite output rows cause no difficulty:
the complete series is bounded in (11). By the bounded stencils
and selectors in (9),

    ||B E_j M_f||_HS<=C p(k)p(l) N^(1/2) q_j(N).          (12)

Thus the gain comes from the distance of the omitted rows from the
input support and the joint energy kernel's quadratic tail. It
requires neither a first absolute moment of a projected path kernel
nor any small operator commutator with P_inf.

### 4. Close the trace and sum all levels and heat labels

Let R_K be the plaquette coordinate selector of K_N. Since M_f=M_f R_K,
cyclicity of the finite-rank trace in (9) gives

    T_fin-T_inf
      =Tr_H2[R_K (S_alpha^inf)^* P_inf B E_j M_f].         (13)

The operator on the left of B E_j M_f has Hilbert--Schmidt norm
at most C N^(3/2): indeed R_K (S_alpha^inf)^* has O(N^3) rows,
each with a uniformly bounded squared row norm, and ||P_inf||<=1.
Hilbert--Schmidt Cauchy--Schwarz in (13), using (12), yields

    |T_fin-T_inf|<=C p(k)p(l) N^2 q_(t-s)(N).             (14)

For each t, sum over the original s=1,...,N-1; keeping min(s,t)<=N
and at most N values of t gives

    sum_(s,t=1)^(N-1) min(s,t) q_(t-s)(N)<=N^2 eta_N.     (15)

Finally the outside factor a, the fixed finite lists alpha,beta,r,
and the full exterior heat majorant give

    |R_prod-R_inf|<=C_i a N^4 eta_N=8 C_i N^3 eta_N.

This proves (3). No heat mode or axial offset was dropped: the
complete infinite offset sum majorizes the actual finite level sum,
and the full heat majorant justifies absolute summation. The original
two generator orientations are retained in L115's formula, and the
outside factor 3 of the complete other/other assembly is not applied
again. In particular the result remains valid before that assembly.

### 5. Identify the exact retained diagonal, without evaluating it

The bounded operator
(S_alpha^inf)^* P_inf S_beta^inf A_r E_j is translation invariant
on the three-component plaquette space. Its diagonal matrix is
constant in x and is the Fourier integral of its bounded symbol.
Its matrix trace is exactly (5). Cyclically moving M_f to the front
of the finite-rank product in (2) and summing the diagonal proves
(4). Boundedness on the compact torus makes (5) integrable; the
undefined projection direction at theta=0 may be assigned arbitrarily
there without changing the operator or integral. The trace remains
real, since all its real-space operators have real entries.

All r,alpha,beta and both levels still occur in f and in (5). A later
use of L088/L099's frozen cancellation must match these complete
filters and the actual two-level exterior coefficients. Equations
(4)--(5) do not perform that transfer and do not assume it. Even a
bound for the retained expression would not identify the limits of
the earlier O(N^3) placement errors.

This is a specialization of finite-stencil compression, quadratic
kernel tails, and the Hilbert--Schmidt trace inequality to L115's
exact order. L110/L111's kernel estimates, L113's coefficient bounds,
and L114/L115's trace definitions are imported, not rederived. The
needed distinction from those results is the remaining output
compression after collecting the compact input multiplier. Ready
coverage is reused from
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
The completed step is RESEARCH / REPRODUCTION: local standard-method
progress, with no claim of novelty beyond the sources checked.

## Mathlib

Full matching finite-compression comparison: **not checked**.
Supporting finite-rank trace cyclicity, Hilbert--Schmidt trace bounds,
Fourier diagonal identities and summable-tail convergence: **not checked**.
Unknown availability is not absence. No mathematical script or numerical
evidence is used. The proof imports the complete joint kernel moment;
it does not infer it from a numerical preview or finite diagnostic.
