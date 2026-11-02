# Lemma 649: exact power-sum deweighting retains only the inner-input response

## Hypotheses

Let n>=5, x=-d=-5/4, R=11/8, U=R^2, eta=1/100 and
t_j=j/n for 0<=j<n. Let Z be a finite set of distinct points with
Re(a)=x, |a|<=R-eta, and x in Z. Assign positive integer original
simple-pole residues r_a, with M=sum_a r_a<=n/3. The poles and
residues are common to every |u|=1; no separation or symmetry is assumed.
Retain the conjugated denominator angle in

    B_u(v)=product_(j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    q_u(zeta)=sum_a r_a W_a(u)/(R*zeta-a).

Use C645g's normalized circle spaces and C645o's complete spatial
coefficient convention. For k>=0 define

    c_k(u)=R^(-1) sum_a r_a W_a(u) (a/R)^k,
    h_k=R^(-1) sum_a r_a (a/R)^k,
    p_k=sum_a r_a (a/x)^k.

Both c(u) and h are in l2(N_0); h is independent of u. Write

    b_u(z)=B_u(R*z)=sum_(ell>=0) beta_ell(u) z^ell,
    (T_u v)_k=sum_(ell>=0) beta_ell(u) v_(k+ell),
    E_n=mean_u ||q_u||_2^2,
    D_single,n=sum_a r_a^2 mean_u |W_a(u)|^2/(U-|a|^2).

The definition of T_u extends to all of l2, as proved below. This
ambient extension does not assert that arbitrary l2 data come from
the prescribed integer-residue family.

## Conclusion

The complete, untruncated power-sum transformation is

    T_u c(u)=B_u(x) h,
    p_k=R*(R/x)^k/B_u(x) * (T_u c(u))_k.                 (1)

The operator T_u is a coisometry: T_u T_u^*=I. In particular it is
a contraction of norm one. For each k, the functional on all of l2
on the right of the second identity in (1) has exact norm

    R*(R/d)^k/|B_u(x)|.                                  (2)

For any fixed h, the minimum of ||v|| over all ambient solutions of
T_u v=B_u(x)h is |B_u(x)| ||h||. For the actual family put
kappa_u=(I-T_u^*T_u)c(u). Then

    ||q_u||_2^2=|B_u(x)|^2 ||h||^2+||kappa_u||^2,
    E_n=mean_u |B_u(x)|^2 ||h||^2+mean_u ||kappa_u||^2.    (3)

Thus even knowing every pure power sum, and hence every Newton-Girard
relation among them, does not improve this *ambient inverse-transfer*
bound. Additional control of the permitted preimages is essential.

Biro's theorem applies to p_1,...,p_M and gives

    ||q_u||_2 > |B_u(x)|/(2R) * (d/R)^M.                 (4)

This is weaker than the zeroth-coefficient estimate

    ||q_u||_2 >= M |B_u(x)|/R.                            (5)

More strongly, the entire recovered response J_u=|B_u(x)| ||h||
satisfies, with rho=273/275 and C645n's lambda>47/1000,

    J_u <= n/[3R sqrt(1-rho^2)] * exp(-lambda*n),
    exp(n/16) mean_u J_u^2 / D_single,n -> 0             (6)

uniformly over admissible families. Here 2lambda-1/16>63/2000>0.
Consequently the exact transformation (1), Biro's lower bound, and
the sharp ambient inverse norm do not prove the requested comparison.

This is a route-specific identification with a recorded stop, not a
counterexample to E_n>=c exp(-n/16)D_single,n. The minimizing ambient
preimage is not claimed admissible. A family-restricted nonlinear
argument can use information discarded by T_u; it is not excluded.
No Xi realization, sign conclusion, certified novelty or RH candidate
is supplied. The specialization has not had a separate critical audit.

## Proof

### 1. Source scope and overlap

The invocation-start [EXPLORE assessment](../drafts/literature/2026-11-02-positive-mass-angular-propagation.md)
explicitly covers this exact full-sequence test. Its Biro and Fourier
source comparisons are reused without another literature search.
C645g supplies the spaces; C645o supplies the full coefficient expansion;
C645n supplies the anchor-product bound used in (6). Only the latter's
product estimate and elementary unweighted norm bound are used, not
an upper bound for the original symbol or operator. The relevant
C645n proof, including its angular maximum, left Riemann sum, exact
logarithm expression and rational rate comparison, was inspected.
Its general audit status is not changed by this use.

Import scalar Fourier orthogonality and Parseval from A. Levitt,
*Analyse de Fourier et applications*, version retrieved 2 November 2026,
[Theorem 1.3/Exercise 1.2 and Theorem 1.11/Corollary 1.12,
printed pp.6,8](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf).
The projection convention is that of L. Baratchart, S. Chevillard and
T. Qian, *Minimax principle and lower bounds in H2-rational
approximation*, J. Approx. Theory 206 (2016), 17--47, preprint v2,
24 March 2015, [Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2).
These inputs were inspected in the reused assessment chain.

Import A. Biro, *An improved estimate in a power sum problem of Turan*,
Indagationes Mathematicae (N.S.) 11(3) (2000), 343--358,
[unnumbered Theorem, p.344](https://users.renyi.hu/~biroand/pdfs/Turan1.pdf),
[DOI](https://doi.org/10.1016/S0019-3577(00)80003-8).
For N complex nodes z_1=1,z_2,...,z_N, repetitions allowed and with
no modulus or spacing restriction, it asserts
max_(1<=j<=N)|sum_k z_k^j|>q_* for an absolute q_*>1/2.
We use only the weaker explicit consequence >1/2. Its proof is not
reproduced here; the Newton-Girard portions inspected in the source
review do not remove the weights from our sequence automatically.

The product-specific calculation below is needed to identify exactly
which information the proposed transfer retains. It specializes the
known Fourier/projection identities; it does not reprove a general
Hardy-space theorem. The scoped duplicate check found C645n's full
inner-input stop and C645y's full-grid decomposition/prefix stop.
The latter, C645x/z and L646--L648 are comparisons, not premises of
(1)--(6). In particular no initial spatial or grid prefix is substituted.

### 2. All coefficients, convergence, and the coisometry

Each grid factor of b_u is

    (z-t_j*u/R)/(1-t_j*z/(R*u)).

It is holomorphic near the closed disk and has modulus one on its
boundary. Thus b_u has these properties, and Parseval gives
sum_ell |beta_ell(u)|^2=1. All B_u(a) and B_u(x) are nonzero:
|a|>=d>1>t_j, while |U-t_j*a/u|>=U-t_j|a|>0.
The pole clearance gives |a/R|<=rho<1. Consequently the expansions
for c and h converge absolutely and uniformly on the spatial circle,
uniformly in u for each fixed n,Z,(r_a). C645o's full expansion gives
||q_u||_2=||c(u)||. No bound uniform in n is needed for these identities.

Identify v in l2 with sum_(k>=0) v_k zeta^(-k-1) in H^2_-.
Multiplication by b_u is an isometry on circle L2. Its strictly
negative Fourier projection has coefficients T_u v, first for finite
sequences and then by density. This proves ||T_u||<=1 and the stated
extension. Each row sum is also absolutely convergent by
Cauchy--Schwarz. Evaluation of the power series at a/R gives

    (T_u c(u))_k
      =R^(-1) sum_a r_a W_a(u) (a/R)^k b_u(a/R)
      =B_u(x) h_k.

Interchange with the sum over a is finite; the remaining series is
absolutely convergent. This proves (1) without dropping any mode.

The kth row of T_u has zeros in positions below k and entries
beta_0,beta_1,... afterwards. Its norm is one. For h>=1, the inner
product of rows whose indices differ by h is, up to conjugation,

    sum_(ell>=0) beta_(ell+h) conjugate(beta_ell)=0.

This is the hth Fourier coefficient of |b_u|^2=1; convergence follows
from Cauchy--Schwarz (or the analyticity already noted). Thus the
rows are orthonormal. The bounded operator T_u T_u^* has the identity
matrix on the standard basis, so equals I. This also proves norm one.
The norm of its kth row, multiplied by the scalar in (1), proves (2).
Equality in that individual functional norm is attained by the
conjugated row, rescaled to unit length, in the ambient l2 space.

Since T_u T_u^*=I, T_u^* is an isometry, T_u^*T_u is an orthogonal
projection, and its orthogonal complement is ker T_u. Every solution
of T_u v=B_u(x)h has the unique orthogonal decomposition

    v=T_u^*(B_u(x)h)+k,      k in ker T_u.

Pythagoras proves the minimum assertion and (3). This also establishes
the precise limitation of imposing further equations solely on h:
once h is fixed, the minimum preimage already has that same complete
sequence. Constraints on the poles or residues of v are additional
information, and may rule that preimage out. We do not discard those
constraints when discussing the original target.

All actual angular terms in (3) are continuous, or equivalently have
continuous norms via this identity and the finite rational symbols.
Integration of (3) is therefore legitimate. No uniform limit in n or
uncontrolled infinite angular expansion is used.

### 3. Integer mass, the source theorem, and the exact rate mismatch

Form M nodes by repeating a/x exactly r_a times. A node equals one
because x is included with r_x>=1. These are genuine unweighted pure
powers, so Biro's theorem supplies j in {1,...,M} with |p_j|>1/2.
Using (2) and d/R<1 yields

    ||c(u)|| > |B_u(x)|/(2R) * (d/R)^j
              >= |B_u(x)|/(2R) * (d/R)^M.

The same j can be used for every u, since p is independent of u;
no interchange of maximum and angular integration is necessary.
The k=0 instance of (1) instead has p_0=M. Its row norm gives (5),
which is strictly stronger than the lower quantity in (4). Positive
integer multiplicity is used exactly where required for Biro, not
to declare the original complex amplitudes positive.

For the full recovered sequence, the geometric-series norm and the
triangle inequality give

    M/R <= ||h|| <= M/[R sqrt(1-rho^2)].

C645n gives |B_u(x)|<=exp(-lambda*n) at every angle, where

    lambda=log(11/10)+(201/80)log(201/121)-(9/4)log(9/5)
           >47/1000.

Together with M<=n/3 this proves the first part of (6). The single
anchor diagonal term gives D_single,n>=1/(U-d^2)=64/21. Therefore

    exp(n/16) mean_u J_u^2 / D_single,n
      <= 21*n^2/[64*9*R^2*(1-rho^2)]
                         *exp(-(2lambda-1/16)*n) -> 0.

The exponent satisfies
2lambda-1/16>94/1000-1/16=63/2000. Every constant is independent
of Z, its separation and its integer residues. This is an upper bound
on the *recovered lower-bound quantity*, not on E_n. In (3), the
uncontrolled kernel term may be large; C645y's retained-grid analysis
is relevant comparison, not permission to omit it.

Thus the tested full-sequence deweighting mechanism does not reach
the requested squared rate 1/16. It leaves the full angular comparison
and every Xi transfer/sign requirement unresolved.

## Mathlib

Full matching coverage for this exact transfer and quantified method
limitation has not been checked. Supporting Parseval and Hilbert-space
orthogonal-projection facts are the cited standard inputs. Biro's
theorem's Mathlib coverage is also not checked; unknown is not absence.
