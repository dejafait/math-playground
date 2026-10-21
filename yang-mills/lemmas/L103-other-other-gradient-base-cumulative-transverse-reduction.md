# L103 — Cumulative transverse reduction of the gradient-base reverse trace

## Hypotheses

Use exactly L102's G_R and R_gx: SU(2), both actual L010 probes
i=3,6, the straight lower-rooted direction-1 forest, relative all-face
fixed-link box (-4,4)^4, sufficiently fine admitted even N, a=8/N,
tau=1/16, and the bare small-coupling coefficient at fixed mesh before
refinement. All coordinates, transposes and norms are ordinary stored
ones. Retain every transverse end row, interior axial level, ordered
plaquette pair including coincidences, and exterior heat mode.

On a single transverse layer put Delta=T^T T, G=Delta^-1,
P=T G T^T, Q=I-P and D=D_T. T has tail-minus-head orientation;
D is the relative transverse circulation and DT=0. Use L088's
actual alternating matrices Omega_k(s) and real symmetric heat
coefficients c_(i;kl,a). Separate their exact terms as

    F_k=Bb^T M_(f_k) Bq-Bq^T M_(f_k) Bb,
    Zeta_k=M_(b_k) Bq-M_(q_k) Bb,
    Omega_k=F_k+Zeta_k^T D-D^T Zeta_k.                 (1)

All these matrices are level diagonal. Import L087's signed vertex
layer Xi_(k,s)=T^T Omega_k(s) T. Define its upper cumulative value

    X_(k,t)=sum_(s=t+1)^(N-1) Xi_(k,s)+Xi_(k,t)/2.     (2)

For clarity distinguish the transverse centered forward differences
T_mu=C_mu D_mu of L065 from the incidence T above. Define the
vertex-to-transverse-edge map

    (W_t phi)_mu=-C_mu^T M_(u_(a,1)(t)) T_mu phi,
                       mu=2,3,4.                    (3)

It keeps the actual vertex displacement and both endpoint/clover
filters. In particular it is not an unfiltered gradient transport.

## Conclusion

The reverse trace has the exact scalar transverse formula

    G_R=a^-1 sum_(k,l)c_(i;kl,a) sum_(t=1)^(N-1) t
      Tr[G X_(k,t) G W_t^T Q Omega_l(t)^T T].         (4)

Let

    P_(i,N)=a^-1 sum_(k,l)c_(i;kl,a) sum_t t
      Tr[G X_(k,t) G W_t^T D^T Zeta_l(t) T].         (5)

Then

    |G_R-P_(i,N)|<=C_i N^2,  |P_(i,N)|<=C_i N^3,
    |R_gx-P_(i,N)|<=C_i N^(5/2).                    (6)

The last estimate imports L102's removal of the other orientation
and curvature subtraction. No outside factor 3 is included.

There is also a uniform transverse inverse approximation. Let
G_epsilon=(Delta+epsilon I)^-1 and let P_(i,N,epsilon) be (5)
with both occurrences of G replaced by G_epsilon, changing no
other matrix or coefficient. For 0<epsilon<=1 and N sqrt(epsilon)>=1,

    |P_(i,N)-P_(i,N,epsilon)|<=C_i N^3 epsilon^(1/4).  (7)

Thus the scaled limsup error is at most C_i epsilon^(1/4). This
supplies a uniform cubic-scale removal of transverse regularization,
not a fixed-epsilon limit theorem. The cumulative X_(k,t) and its
half-weight remain; neither a local replacement nor coefficient
freezing has been made. Existence and value of a^3 P_(i,N,epsilon)
for fixed epsilon, and hence the limit of G_R, remain unproved here.

The plausible downstream use is a finite-range transverse trace
analysis with an already controlled inverse error and an exact axial
sum. Co-closed-base R_R and transverse H still lack cubic control;
the E/H functionals and required joint compensation -4 gamma D_i
before factor 3 remain unevaluated. No complete other/other coefficient,
finer remainder, interacting error bound or Yang--Mills candidate follows.

## Proof

### 1. Keep the generator stencil and perform only the exact axial sum

L065(2), obtained from L009(3), gives on a pure component-1 input

    G_T1=a^-1 W C_1.                                 (8)

Here C_1 averages axial edges to interior vertices, and W is level
diagonal with blocks (3). This is a stencil identity, not an application
of L065's scalar residual bound to transverse inputs. Compact support
of u_a makes every nonzero stencil interior. Zero pinned values and
the actual relative endpoint averages apply on every other row.

L092 gives C=Tcal G_v B and K_g=M tensor P, M_st=min(s,t).
L093(5)'s exact interval matrix is

    S=B C_1^T,  S_st=1_(t<s)+delta_st/2,
    M_ts S_st=t[1_(t<s)+delta_st/2].                  (9)

This uses all N axial edges in B and C_1, including their endpoint
rows. In particular t=N-1 still has its half-weight; t=1 has all
the indicated higher rows. There is no periodic or infinite-interval
substitution. The reverse block has (s,t) entry
a^-1 S_st T G W_t^T Q.

Since P Omega_k(s) P=T G Xi_(k,s) G T^T, multiplication by
T G on its right gives T G Xi_(k,s) G. Insert this identity and
(9) into L102(1)'s actual trace, and cycle the final T to the right
of the vertex trace. The t,s block of K_g is M_ts P; PT=T
removes only that adjacent projection. Summing s gives precisely
(2) and (4). W_t and Omega_l(t) stay at level t in their original
order. No variable coefficient has been commuted through an inverse.

### 2. Bounds for the cumulative signed layer

L087(11)--(13) proves on each full pinned layer

    Xi_(k,s)=T^T M_(d_(k,s)) E-E^T M_(d_(k,s)) T,
    ||d_(k,s)||_infinity<=C a^3 p(k), Tr G<=C N^3.    (10)

E selects the initial endpoint of each transverse relative edge,
zero at a pinned endpoint, and has uniformly bounded norm. End-edge
wedges with a pinned vertex are zero. These are exact signed sums,
not estimates on separate plaquettes. Summing with (2)'s weights gives

    X_(k,t)=T^T M_(d^>_(k,t)) E-E^T M_(d^>_(k,t)) T,
    d^>_(k,t)=sum_(s>t)d_(k,s)+d_(k,t)/2,
    ||d^>_(k,t)||_infinity<=C a^2 p(k).               (11)

The last bound uses Na=8, uniformly even near either axial end.
Since ||T G^(1/2)||=1, (10)--(11) imply

    ||G^(1/2) X_(k,t) G^(1/2)||_HS
                              <=C a^2 p(k) N^(3/2). (12)

Furthermore, T_mu=C_mu D_mu and sum_mu D_mu^T D_mu=Delta,
so ||T_mu G^(1/2)||<=1. Formula (3) therefore proves

    ||W_t||+||W_t G^(1/2)||<=C.                      (13)

This estimate leaves coefficients on their displayed side of T_mu.
It neither bounds the full reverse prefix block by O(N) nor asserts
that W_t maps into gradients. Import L088(5) and bounded multiplicity
of its exact paths to obtain, uniformly in t,

    ||F_l(t)||<=C a^2 p(l), ||Zeta_l(t)||<=C a p(l),
    ||D||<=C, sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i.      (14)

One fixed enlarged polynomial p suffices for all these bounds.

### 3. Remove only the exterior-circulation terms

From (1), DT=0, and QD^T=D^T,

    Q Omega_l(t)^T T=-Q F_l(t) T+D^T Zeta_l(t) T.     (15)

The second term gives (5) exactly. For the first, cycle (4)'s
vertex trace into the product of G^(1/2) X G^(1/2) and
G^(1/2) W_t^T Q F_l T G^(1/2). The latter matrix has operator
norm at most C a^2 p(l) by (13)--(14), hence Hilbert--Schmidt
norm at most C a^2 p(l) N^(3/2), since the vertex dimension is
(N-1)^3. With (12), trace Cauchy--Schwarz gives a bound
C a^4 p(k)p(l) N^3 per (k,l,t). The positive prefactors satisfy
a^-1 sum_t t<=C N^3, so (14) yields O_i(a^4 N^6)=O_i(N^2).

For the retained term replace QF_l by D^T Zeta_l in the same
argument. Its corresponding operator norm is C a p(l), giving
C a^3 p(k)p(l)N^3 per trace and therefore O_i(N^3) after the
weighted t sum. This proves the first two assertions of (6).
L102(2) and the triangle inequality prove its final assertion.
All estimates are summable over the full exterior series by (14).

### 4. Control both singular inverse replacements before taking limits

Write H=G-G_epsilon, which is positive and commutes with Delta.
The full pinned three-dimensional spectrum obeys
lambda_m>=c|m|^2/N^2, m in {1,...,N-1}^3. For
M=N sqrt(epsilon)>=1, shells max m_j=r contain at most C r^2
indices. Split their sums at r=M (or at the endpoint N-1 if
smaller). The exact scalar multipliers give

    ||Delta^(1/2) H||_HS^2
       =sum_lambda epsilon^2/[lambda(lambda+epsilon)^2]
       <=C N^3 sqrt(epsilon),
    ||Delta H||_HS^2
       =sum_lambda epsilon^2/(lambda+epsilon)^2
       <=C N^3 epsilon^(3/2).                        (16)

For the first sum the low shells cost at most C N^2 M, and the
high shells at most C epsilon^2 N^6 sum_(r>M) r^-4
<=C epsilon^2 N^6 M^-3. For the second they cost at most C M^3
and C epsilon^2 N^4 sum_(r>M) r^-2
<=C epsilon^2 N^4/M. These are exactly (16)'s powers. If the
high range is empty its contribution is zero. Thus no continuum
spectral-density assertion or omitted low eigenvalue is needed.

Fix k,l,t temporarily. Put d=M_(d^>_(k,t)) and
Z=D^T Zeta_l(t). For either inverse J=G or G_epsilon, (11)
and cyclicity express the principal trace as

    Phi(J)=Tr[(T J T^T) d (E J W_t^T) Z]
           -Tr[(T J E^T) d (T J W_t^T) Z].           (17)

These are ordinary transverse-edge traces, so dimensions agree
even though E has a vertex input. For both choices of J, spectral
calculus, (10), and (13) give

    ||T J T^T||+||T J W_t^T||<=C,
    ||E J W_t^T||_HS+||T J E^T||_HS<=C N^(3/2),
    ||d||<=C a^2 p(k),
    ||Z||<=C a p(l), ||Z||_HS<=C a p(l)N^(3/2).     (18)

For example J W_t^T=G^(1/2)(Delta J)(G^(1/2) W_t^T),
where ||Delta J||<=1. The Hilbert--Schmidt bound follows from
Tr G<=CN^3; no coefficient enters spectral calculus. Similarly,
T G^(1/2) is an isometry on vertices. Formula (16) gives

    ||T H T^T||_HS+||T H W_t^T||_HS
                               <=C N^(3/2)epsilon^(3/4),
    ||E H W_t^T||_HS+||T H E^T||_HS
                               <=C N^(3/2)epsilon^(1/4).          (19)

For the first line factor T H W_t^T as
(T G^(1/2))(Delta H)(G^(1/2) W_t^T), and likewise for
T H T^T. For the second line use H Delta^(1/2) and its transpose
with the bounded factors E, T G^(1/2), and G^(1/2) W_t^T.

Expand the difference of each product in (17) by replacing its
first inverse, then its second, once each. In the first trace,
pair T H T^T with E G W_t^T in Hilbert--Schmidt norms and bound
d,Z in operator norm; this costs
C a^3 p(k)p(l) N^3 epsilon^(3/4). For its second replacement
pair E H W_t^T with Z in Hilbert--Schmidt norms and bound
T G_epsilon T^T and d in operator norm; the cost is the same
expression with epsilon^(1/4). In the second trace pair
T H E^T with Z for its first replacement, and pair
T G_epsilon E^T with T H W_t^T for its second replacement.
Equations (18)--(19) give respectively the epsilon^(1/4) and
epsilon^(3/4) costs. Consequently

    |Phi(G)-Phi(G_epsilon)|
       <=C a^3 p(k)p(l) N^3 epsilon^(1/4).            (20)

Multiplication by a^-1 sum_t t<=CN^3 and the full heat sum
(14) proves (7), since a^3 N^6=512 N^3. This verifies the
complete relevant evidence for the inverse approximation. It does
not select epsilon depending on N in an unproved localization
argument, or assume an operator-norm approximation to G.

### 5. What this step establishes

The signed complete layer, exact triangular prefix sum and controlled
O(N^2) removal reduce G_R to (5). Only its two transverse inverses
need regularization, and (7) controls their joint error uniformly at
the desired cubic scale. A future proof must still establish the
fixed-epsilon finite-trace limit with the actual cumulative coefficient,
pinned rows and exterior heat sum before removing epsilon. No frozen
symbol, continuum coefficient, vanishing or compensation is asserted.

This is local standard-method progress, classified REPRODUCTION under
the unchanged EXPLORE assessment
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
The finite contraction is imported from L102; L065's stencil, L087's
signed identity and L093's exact prefix are specialized in a different
actual order. Their existing conclusions do not supply (4)--(7), which
is why the short algebra and spectral estimates are given here.
There is no claim of originality beyond the checked sources and no
new external theorem invocation. L094/ATTEMPTS/028's norm obstruction
remains intact. Other jets, finer powers/logarithm, finite matching,
interacting error <=c_box/2, continuum axioms, reflection positivity,
infrared control and finite positive mass remain independent gaps.
Any numerical comparison with L084 retains L082's IEEE qualifications.

## Mathlib

Full matching cumulative transverse reduction and inverse approximation:
**not checked**. Supporting finite trace cyclicity, Hilbert--Schmidt
ideal inequalities and finite tensor spectral sums: **not checked**.
Unknown availability is not evidence of absence. The exact matrix
identities and estimates above are the mathematical verification;
documentation validation is not proof verification.
