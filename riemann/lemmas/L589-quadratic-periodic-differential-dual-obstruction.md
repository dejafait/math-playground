# Lemma 589: quadratic periodic differential certificates miss the threshold

## Hypotheses

Use the real six-coordinate vector

    v=(x_0,y_0,z_0,x_1,y_1,z_1),
    Q(v)=max(0,x_0 z_0-y_0^2).

The exact matrix K, spectral matrices A(u), interval I=[-1/2,1/2],
jet J_h, covariance C(h) and finite cone C_I are those of L586.
In particular, with a=(r,j), b=(s,k), r,s in {0,1}, j,k in {0,1,2},

    K_ab=integral_I (iu)^j(-iu)^k exp(i(r-s)u) du,
    K=integral_I A(u) du.                                    (1)

The complex integral in (1) is real; it is not an entrywise modulus.
Let T={ (0,0),(0,1),(1,0),(1,1) } in that order, and write
a+=(r,j+1) for a=(r,j) in T. For any real symmetric four-by-four
matrix S define the homogeneous quadratic storage and its chain-rule
derivative by

    V(w)=sum_(a,b in T) S_ab w_a w_b,
    D V(v)=sum_(a,b in T) S_ab
                      (v_(a+) v_b+v_a v_(b+)).               (2)

Thus the four state coordinates are (x_0,y_0,x_1,y_1), and their
derivatives are (y_0,z_0,y_1,z_1). Every real homogeneous quadratic
polynomial in these four states has this form.
Indeed its diagonal coefficients are S_aa and the coefficient of
w_a w_b for a!=b is 2S_ab. Allowing arbitrary symmetric S therefore
loses no cross term and imposes no positivity condition on the storage.

Consider real symmetric six-by-six H and four-by-four S satisfying both global
pointwise branches

    v^T H v-D V(v)>=0                         for every v in R^6,
    v^T H v-D V(v)-(x_0 z_0-y_0^2)>=0          for every v in R^6.
                                                               (3)

For a sufficient periodic upper-bound certificate also impose

    trace(H A(u))>=0 for every u in the closed interval I.     (4)

There is no Fourier cutoff, prescribed period, common pointwise state
bound, fixed autonomous flow, probability normalization of the cone,
or sharp-duality/attainment assumption. No actual-Hardy or Xi path is
assumed to have the finite law used below. L473 Section 4 is used only
for its explicitly constructed bounded vector B, not its arithmetic
moment inputs or its corrected height-dependent total law.

## Conclusion

For every smooth real P-periodic h, P>0, with K-C(h) in C_I, a pair
satisfying (3)--(4) gives the sufficient bound

    P^(-1) integral_0^P Q(J_h(t)) dt <= trace(H K).            (5)

But every pair satisfying (3) alone necessarily has

    trace(H K)>=1/144=2*(1/288).                             (6)

Consequently this entire quadratic certificate class cannot establish
a bound strictly below 1/288. The lower bound already holds before
imposing (4); no sampled or approximate cone test is involved.
No optimal cost or above-threshold periodic path is asserted. This
does not obstruct higher/nonlinear storage classes, other methods of
periodic clipping control, fourth/probability assembly or actual-Xi
signs. It is a local specialization and obstruction under the saved
SPECIALIZE assessment, not a claim of novelty beyond the sources checked.
The independent conceptual audit in Section 4 passes without correction
to this statement or its bound.

## Proof

### 1. Imported sufficient method and its exact periodic specialization

The method is the sufficient pointwise-dual bound of A. Chernyavsky,
J. J. Bramburger, G. Fantuzzi and D. Goluskin, *Convex relaxations of
integral variational problems: pointwise dual relaxation and
sum-of-squares optimization*,
[arXiv:2110.03079v1, Lemma 2.1 and (2.4)--(2.11), printed pp.8--10](https://arxiv.org/pdf/2110.03079v1).
The relevant input is the chain-rule divergence identity and its
one-sided bound when the integrated divergence is zero. We check that
boundary condition here. We do not import a sharp-duality, convergence
or realization theorem, and do not reprove the general variational result.

For a fixed h as in (5), put

    w_h(t)=(h(t),h'(t),h(t+1),h'(t+1)).

This is a smooth periodic state, and its derivative uses precisely
the second derivatives already in J_h. On the compact interval [0,P]
the state and its derivative are bounded and square integrable; the
polynomial V is C1, and its chain-rule derivative is integrable. Its
endpoint values agree. The source's zero-flux condition is therefore
verified explicitly by

    integral_0^P D V(J_h(t)) dt
       =V(w_h(P))-V(w_h(0))=0.                              (7)

In particular h(P+1)=h(1) and h'(P+1)=h'(1), as well as the
unshifted endpoint equalities. No integrality or commensurability
condition on P and the lag one is used.
No common compact box over all h or P is needed for this identity.
The two branches of (3) say exactly that

    v^T H v-D V(v)>=max(0,x_0 z_0-y_0^2)=Q(v).              (8)

All these observables are continuous and integrable along this path.
Integrating (8) and using (7) gives

    average Q(J_h)<=trace(H C(h)).                          (9)

For clarity, trace is the full matrix trace: symmetry gives
trace(H vv^T)=v^T H v, including both off-diagonal contributions.
Since K-C(h) is in the actual finite cone C_I, it has a representation
sum_l alpha_l A(u_l) with alpha_l>=0 and u_l in I. The necessary
cone-dual inequality used in L588 Section 1, specialized to
f_H(u)=trace(H A(u)), gives explicitly

    trace(H(K-C(h)))=sum_l alpha_l f_H(u_l)>=0.              (10)

This is the elementary finite-cone implication, with no ambient PSD
substitute or cone-closure premise. Equations (9)--(10) prove (5).

### 2. Every allowed quadratic derivative has zero K-expectation

For any a=(r,j), b=(s,k) in T, both successor indices are among the
six allowed coordinates. Formula (1) gives the exact relation

    K_(a+,b)+K_(a,b+)
      =integral_I (iu)^j(-iu)^k exp(i(r-s)u)(iu-iu) du=0.   (11)

This covers every same-lag and cross-lag pair, including j=k=1;
no third derivative is introduced. The integrals are continuous on
the compact interval I, so no limiting or infinite interchange is
needed. As checks, a=b=(r,0) gives K_((r,0),(r,1))=0;
a=(r,0), b=(r,1) gives K_((r,0),(r,2))=-K_((r,1),(r,1));
and a=b=(r,1) gives K_((r,1),(r,2))=0. Cross-lag relations follow
from the very same factor cancellation, retaining exp(i(r-s)u).

For any real random vector B with E BB^T=K, each quadratic monomial
is integrable: Cauchy--Schwarz bounds E|B_a B_b| by its finite second
moments. Consequently the finite sum (2) has expectation

    E D V(B)=sum_(a,b in T) S_ab
                    (K_(a+,b)+K_(a,b+))=0.                (12)

This is a covariance calculation, not differentiation of an
expectation, stationarity of B, or a path-realization assertion.

### 3. Exact finite-law witness against the whole class

L473 Section 4 (11)--(13) constructs a bounded finite vector B in R^6
with

    E BB^T=K,          E Q(B)=1/144.                        (13)

We import that established construction, without reproving its
Schur-complement extension. Its first marginal is
B_0=(epsilon,v,k epsilon), with epsilon uniform on {+1,-1},
k=1/12 with probability 1/6 and k=-7/60 with probability 5/6,
and v=0 with probability 1/2 and v=+/-1/sqrt(6) with probability
1/4 each, independently. To make the precise clipped observable
transparent, Q(B)=max(0,k-v^2) is nonzero exactly when k=1/12
and v=0, with probability (1/6)(1/2)=1/12. Its value is then
1/12, giving exactly 1/144 as in (13). This check of applicability
does not claim a new finite-law construction. The other marginal
and all cross covariances are supplied by L473's extension (12).

Apply the global inequality (8) to every atom of this B. The law is
bounded, so every expectation exists. By (12)--(13),

    trace(H K)=E[B^T H B]
       >=E Q(B)+E D V(B)=1/144.                            (14)

This proves (6) for every possible H and S obeying (3), even those
failing (4). In particular no solver search or proof of the full-I
dual can evade this obstruction within the stated class.

The finite B need not come from a periodic path to test a global
pointwise inequality. L580's quartic stationarity failure for this
uncorrected law is compatible with (12): it uses a higher-degree
observable not determined by K. It is a failure comparison, not an
input to (14). No conclusion about the corrected total law nu_H,
the true periodic supremum or actual Hardy/Xi clipping follows.

### 4. Independent conceptual audit, 31 October 2026

The separate audit reuses the approved sufficient-method source scope
in `drafts/literature/2026-10-31-l589-independent-audit-scope.md`.
The source input remains only the sufficient chain-rule/divergence
method cited in Section 1; no sharpness or realization is imported.
The following complete finite checks verify this existing argument.

**All storage entries and successor signs.** Set

    g_m(d)=integral_I (iu)^m exp(i d u) du.

These integrals are real, by conjugation followed by u -> -u, and
K_((r,j),(s,k))=(-1)^k g_(j+k)(r-s). The ten unordered state
pairs have the following two successor terms. Here x_r=(r,0),
y_r=(r,1), and successors are coordinate labels, not random indices.

| a,b | K_(a+,b) | K_(a,b+) |
| --- | --- | --- |
| x_0,x_0 | g_1(0) | -g_1(0) |
| x_0,y_0 | -g_2(0) | g_2(0) |
| x_0,x_1 | g_1(-1) | -g_1(-1) |
| x_0,y_1 | -g_2(-1) | g_2(-1) |
| y_0,y_0 | -g_3(0) | g_3(0) |
| y_0,x_1 | g_2(-1) | -g_2(-1) |
| y_0,y_1 | -g_3(-1) | g_3(-1) |
| x_1,x_1 | g_1(0) | -g_1(0) |
| x_1,y_1 | -g_2(0) | g_2(0) |
| y_1,y_1 | -g_3(0) | g_3(0) |

Symmetry of K interchanges the two terms on reversing a,b, so
this table covers all sixteen ordered pairs in (2). Each successor
coordinate has derivative order at most two, even when g_3 occurs
in the product integral. In particular no third-derivative state
is being assumed. Directly g_1(0)=g_3(0)=0 and g_2(0)=-1/12,
agreeing with L473's same-height block. Both off-diagonal copies in
the full S sum cancel separately. Thus every allowed quadratic
storage, including all lag-cross and first-derivative cross terms,
has exactly the zero expectation in (12).

**Finite-law applicability, including the other lag.** The covariance
in (13) is an uncentered second matrix E BB^T, just as C(h) is an
uncentered path average. L473 Section 4 and its Section 8 audit give
E k=-1/12, E k^2=1/80, E v^2=1/12 and the exact K_0 block.
Its extension uses D_0=E B_0 B_1^T and

    B_1=D_0^T K_0^(-1) B_0+R^(1/2)e,
    R=K_0-D_0^T K_0^(-1)D_0>0.

Here e is independent, centered and has E ee^T=I_3. Replaying
the interface gives E B_0 B_1^T=K_0 K_0^(-1)D_0=D_0 and
E B_1 B_1^T=D_0^T K_0^(-1)D_0+R=K_0, with zero mixed
noise terms. L473's strict Gram positivity supplies the inverse and
positive square root; no lower numerical eigenvalue is needed.
This verifies use of all cross-lag entries rather than a replacement
by independent lag copies. It does not reconstruct or alter L473.

For the exact clipped observable, epsilon^2=1 makes x_0 z_0=k.
Combining the two nonzero v values, the exhaustive marginal table is:

| k | v^2 | probability | k-v^2 | Q(B) |
| --- | --- | --- | --- | --- |
| 1/12 | 0 | 1/12 | 1/12 | 1/12 |
| 1/12 | 1/6 | 1/12 | -1/12 | 0 |
| -7/60 | 0 | 5/12 | -7/60 | 0 |
| -7/60 | 1/6 | 5/12 | -17/60 | 0 |

The probabilities total one, and their clipped expectation is exactly
1/144. This test does not use the arithmetic moment theorems, the
height-dependent correction, or a periodic realization of B.

**Sufficient direction and scope.** The first branch of (3) covers
the zero clipping branch, and the second covers x_0 z_0-y_0^2;
both are essential to (8). In quadratic-matrix notation the latter
form has off-diagonal entries (x_0,z_0) and (z_0,x_0) equal to 1/2
and diagonal (y_0,y_0) equal to -1. This agrees with the full-trace
convention in (9) and (14). The endpoint identity (7), now explicitly
checked also at lag one, is valid for every P>0. The required cone
direction is trace(H C(h))<=trace(HK), exactly (10), using a finite
nonnegative representation with nodes in the closed I. No PSD
relaxation, missing closure argument or limiting endpoint is used.

Finally (8) holds at every atom of B because its domain is all R^6.
Its expectation plus (12) therefore yields (14) independently of
condition (4). The achieved lower bound 1/144 exceeds the required
upper-certificate cost 1/288 by 1/288. The audit passes without any
change of hypotheses, constants or direct inputs. It verifies an
existing class obstruction, not a new bound, optimality claim,
periodic feasibility result or advance toward actual-Xi signs.

## Mathlib

Full matching Mathlib coverage for this finite-law obstruction and
periodic certificate class has not been checked. The supporting chain
rule, fundamental theorem of calculus, finite sums, trace identities
and Cauchy--Schwarz are standard inputs, not a claimed formalization
of the full result. No quadratic/PSD conversion or spectral-theorem
reproof is needed. Unknown matching coverage is not evidence of absence.
