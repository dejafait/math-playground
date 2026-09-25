# L009 — Automatic ordinary lifting and the remaining strict derivative

## Hypotheses

Retain the full setting of L006, including kappa != 0 and all the
auxiliary hypotheses in [the Castella--Hsieh foundation](../foundations/07-castella-hsieh-nonvanishing.md).
Write F = Q_p, V = V_p E, S_Q = Sel(Q,V), and S = Sel(K,V).
Let tau be complex conjugation. Retain L008's normalized diagonal
anticyclotomic summand and its character

\[
\xi_T=1+Td+O(T^2),\qquad d^\tau=-d\ne0.
\]

Let A = F[epsilon]/(epsilon^2) and V_A = V tensor_F A with G_K-action
rho_A(h) = (1 + epsilon d(h)) rho_V(h). Define its ordinary Selmer
group S_A and complex C_A using the deformed ordinary filtration at
both v | p and the unramified conditions elsewhere, as specified in
[the duality foundation](../foundations/10-selmer-bockstein-duality.md).
Put C = C_f(V). Write

\[
D=H^1_f(K_{\mathfrak p},V)\oplus H^1_f(K_{\overline{\mathfrak p}},V),
\qquad S_{00}=\ker(S\xrightarrow{\operatorname{loc}}D).
\]

Here "strict" means zero localization at both primes, including for
a deformed class. It does not mean the ordinary local condition that
some cited sources also call "strict". Superscripts +/- on S and D
refer to tau-eigenspaces.

## Conclusion

The ordinary first Bockstein beta_f: S -> H^2(C) is zero. Consequently
every x in S has an ordinary lift to S_A, and

\[
d\cup x=0\quad\text{in }H^2(K,V).
\tag{1}
\]

In particular (1) holds for x = res_K(kappa), without assuming its
rational Kummer membership. More precisely,

\[
0\longrightarrow \epsilon S\longrightarrow S_A\longrightarrow S
\longrightarrow0,\qquad S=S^+,\quad\dim_F S=2.
\tag{2}
\]

Give V_A the semilinear tau-action extending that on V and sending
epsilon to -epsilon. Each x in S has a unique tau-invariant ordinary
lift y_x. For x in S_{00}, define

\[
\Delta_d(x)=\epsilon^{-1}\operatorname{loc}(y_x)\in D^-.
\tag{3}
\]

The inverse notation in (3) means the inverse of the injective
cohomology map induced by V -> V_A, v |-> epsilon v, on its image;
it is not division by a unit of A. Both D^+ and D^- have dimension one.
The map Delta_d is F-linear and satisfies

\[
x\text{ has an ordinary lift strict at both primes}
\quad\Longleftrightarrow\quad\Delta_d(x)=0.
\tag{4}
\]

This computes the ordinary obstruction and isolates the additional
strict one. The value Delta_d(res_K(kappa)) and any relation of (4)
to rational Kummer membership are not determined here. Thus ordinary
first-order liftability supplies no additional condition on S_Q;
the existing bound r <= 2 remains short of the required r >= 2.

## Proof

**The minus Selmer space vanishes.** Restriction and the two idempotents
(1 +/- tau)/2 identify

\[
S^+\simeq\operatorname{Sel}(\mathbf Q,V_pE),\qquad
S^-\simeq\operatorname{Sel}(\mathbf Q,V_pE^K).
\]

This is restriction/corestriction (or Shapiro) over the quadratic
extension. It respects the finite local conditions: restriction and
norm respect local Kummer maps, and their composite is multiplication
by 2, invertible over F. Equivalently, apply the decomposition of the
Weil restriction of E/K up to its degree-two isogeny into E and E^K.
The hypothesis L(E^K,1) != 0 and the analytic-rank-zero theorem in
[the standard inputs](../foundations/02-standard-inputs.md) give rank
E^K(Q) = 0 and finite Sha(E^K/Q). Its rationalized Kummer sequence
therefore gives S^- = 0. This uses finite Sha of the auxiliary twist,
not finite Sha of E/Q. L006 gives dim S_Q = 2, proving the assertions
about S in (2). The same conclusion is used in the source's (5.6).

**Local conditions and duality.** At each v | p the ordinary quotient
V_v^- has no invariants, since its unramified Frobenius eigenvalue is
not 1, by the Hasse-bound calculation in the duality foundation.
The subrepresentation V_v^+ has nontrivial cyclotomic action on
inertia and also has no invariants. Local Tate duality, together
with (V_v^+)^*(1) isomorphic to V_v^-, gives H^2(K_v,V_v^+) = 0.
Hence its H^1 injects into H^1(K_v,V) and is the ordinary finite line.
It has dimension one by the local Euler characteristic, or by the
local Kummer map and the formal logarithm. The same invariant
vanishings hold after first-order deformation by the coefficient
exact sequence. That sequence also gives

\[
0\longrightarrow \epsilon H^1_f(K_v,V)
\longrightarrow H^1_{\rm ord}(K_v,V_A)
\longrightarrow H^1_f(K_v,V)\longrightarrow0.
\tag{5}
\]

For a finite place away from p, E(K_v)[p^infinity] is finite, so
H^0(K_v,V) = 0. Self-duality and the local Euler characteristic give
H^2(K_v,V) = H^1(K_v,V) = 0. Thus the rational unramified local
complex is acyclic there; its H^0 and H^1 vanish. These facts persist
for V_A by its coefficient sequence. The complex places contribute
zero modified local cohomology. There are consequently no omitted
exceptional local terms, and the Selmer complex's H^1 is S at the
fiber and S_A after deformation. Global H^0 is zero as well.

The finite local conditions at the fiber are self-orthogonal for
the Weil-pairing local Tate duality. **Poitou--Tate duality for
Selmer complexes**, cited in the duality foundation, therefore gives

\[
H^2(C)\simeq S^\vee
\tag{6}
\]

equivariantly for tau. This perfect duality concerns two different
cohomological degrees; it is not an assumption that an arithmetic
height is nondegenerate. It is valid even when V_p Sha(E/Q) is nonzero.

**The connecting class and its sign.** A continuous cocycle c
representing x has a constant F-linear lift to V_A. Its coboundary
is

\[
(\partial_A c)(h,k)
 =\epsilon d(h)\rho_V(h)c(k).
\tag{7}
\]

After identifying epsilon V_A with V, (7) is d cup c. The connecting
map on the Selmer complex refines this global connecting map and
retains the local cochains. Short exactness on cochains is valid
here: the coefficient maps have continuous F-linear splittings;
the unramified terms also commute with them since d is unramified
away from p. Thus vanishing of beta_f(x) is exactly the condition
for an ordinary lift, by the long exact cohomology sequence.

Because xi^tau = xi^(-1) modulo epsilon^2, the rule
tau(v tensor a) = tau(v) tensor a(-epsilon) gives a semilinear
involution compatible with all global and local complexes.
The target of the connecting map before dividing by epsilon is
H^2(C) tensor epsilon F. Naturality therefore says, after that
identification,

\[
\beta_f(\tau x)=-\tau\beta_f(x).
\tag{8}
\]

Every x belongs to S^+, while (6) and S^- = 0 imply H^2(C)^- = 0.
Equation (8) consequently forces beta_f(x) = 0 for every x. Its
image under the forgetful map is (7), proving (1). The same long
exact sequence, with H^0(C) = 0, proves (2). An inverse-character
convention reverses the sign of (7), with the same vanishing result.
This agrees with the source's already established vanishing of the
first anticyclotomic height on the (2,0) Selmer space.

**Retaining strictness.** Average any ordinary lift of x with its
tau-conjugate. Since x is invariant and 2 is invertible, this gives
a tau-invariant lift y_x. The difference of two such lifts lies in
epsilon S by (2). Tau acts as -1 on epsilon S, so an invariant
difference is zero. This proves existence and uniqueness of y_x.

If x is strict, its lifted localizations reduce to zero. Equation
(5), and the injectivity induced by H^0(K_v,V) = 0, give a unique
z in D with loc(y_x) = epsilon z. Tau-invariance gives z = -tau z,
so z belongs to D^-. Conjugation exchanges the two one-dimensional
local finite spaces; hence dim D^+ = dim D^- = 1. This proves (3).
Uniqueness also proves linearity of x |-> y_x and Delta_d.

Every ordinary lift is y_x + epsilon s with s in S. Its localization
is epsilon(Delta_d(x) + loc(s)). Since loc(S) is contained in D^+
and Delta_d(x) lies in D^-, it is zero only if Delta_d(x) = 0.
Conversely that equality makes y_x itself strict. This proves (4).
Without choosing the invariant lift, the same obstruction is the
class of the local derivative in D/loc(S). Its invariant-lift
representative singles out the anti-invariant line. In particular,
the zero ordinary Bockstein has not silently been substituted for
the obstruction with zero local conditions at p.

**Why the residual scalar is additional data.** As a check on what
the reduction argument alone determines, take abstract A-modules
S_A = A e_1 + A e_2 and D_A = A a_+ + A a_-, with semilinear
tau(e_i) = e_i and tau(a_+) = a_+, tau(a_-) = -a_-. For any c in F,
the equivariant A-linear map

\[
\operatorname{loc}_A(e_1)=a_+,\qquad
\operatorname{loc}_A(e_2)=\epsilon c a_-
\]

has the same fiber map and surjective ordinary reduction. The
strict fiber is F e_2 and its Delta(e_2) is c a_-. Thus c = 0 and
c != 0 give opposite strict-lifting answers with identical fiber
data and ordinary liftability. These are linear diagrams, not
Galois realizations or counterexamples to an arithmetic theorem.
They show precisely why symmetry and the fiber map alone do not
compute Delta_d(kappa). No assertion that strict liftability is
necessary or sufficient for rational Kummer membership is made.

Finally, strictness of kappa over Q from L006 implies strictness
of res_K(kappa) at both split primes by compatibility of restriction
and localization. Therefore all the conclusions apply to the
actual class. Its q(kappa) remains undetermined. The obstruction to
a universal representation map in L008 and the ordinary lifting
of each class in (2) concern different objects and are compatible.

## Mathlib

Coverage of the full arithmetic statement: **not checked**.
Supporting results on cup products, connecting maps, Selmer duality,
and semilinear involutions: **not checked**. The proof above supplies
the deductions; direct links and theorem identifiers for the named
duality, comparison, and height inputs are retained in the foundations.
Those sources are supporting results, not a match for the strict
derivative criterion or the missing Kummer-membership statement.
