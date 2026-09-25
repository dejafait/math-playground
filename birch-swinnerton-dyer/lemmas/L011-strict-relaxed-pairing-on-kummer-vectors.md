# L011 — The strict/relaxed pairing on a rational Kummer vector

## Hypotheses

Retain the full hypotheses and notation of L009: F = Q_p, p > 3,
V = V_p E, the imaginary quadratic field K with p split, the
anticyclotomic tangent d, and A = F[epsilon]/(epsilon^2). In particular
S = Sel(K,V) = S^+ has dimension two, its ordinary first Bockstein
vanishes, and each s in S has a unique tau-invariant ordinary lift
y_s for V_A = V(1 + epsilon d). Keep all the auxiliary hypotheses;
no existence statement for arbitrary E is added.

At both primes v | p put D_v = H^1_f(K_v,V), D = D_p direct-sum
D_bar, and S_00 = ker(S -> D). Subscripts p and bar denote the two
primes of K; superscripts +/- denote conjugation eigenspaces.
Let R = Sel_rel(K,V) have unrestricted local conditions at both
primes over p and the same unramified conditions elsewhere. Its
complex is C_rel. The complex C_00 has zero local conditions at
both primes over p. Strict means zero localization, as in L009.

Use the Weil pairing, local Tate pairings, and **Poitou--Tate duality
for Selmer complexes**, Nekovar, *Selmer complexes*, Theorem 6.3.4,
with the local-condition and Bockstein conventions recorded in
[the duality foundation](../foundations/10-selmer-bockstein-duality.md).
The dual of the deformation has character 1 - epsilon d.

Only for the rational-point test, assume that P,Q are independent
points in E(Q) modulo torsion. Write j_K for restriction to K of
L005's Kummer injection, and ell(s) for the logarithm of the
localization of s at p. Then ell(j_K(P)) = log_p(P), and similarly
for Q. These points are supplied test inputs, not constructed here.

## Conclusion

There is an exact local-condition sequence

\[
0\longrightarrow S_{00}\longrightarrow S\xrightarrow{\rm loc}D
\xrightarrow{b}R^\vee\longrightarrow S^\vee\longrightarrow0,
\qquad b(a)(z)=\sum_{v\mid p}\langle a_v,\operatorname{loc}_v z\rangle_v.
\tag{1}
\]

Here b uses the boundary sign fixed in the proof. Consequently the
pairing between D^- and R^- in (1) is perfect, and dim_F R^- = 1.
This conclusion does not require loc(S) != 0 or finite Sha.

Let beta_00,d be the first Bockstein for C_00. For x in S_00 and
z in R its mixed pairing satisfies

\[
\langle\beta_{00,d}(x),z\rangle_{\rm PT}
 =\sum_{v\mid p}\langle\Delta_d(x)_v,\operatorname{loc}_v z\rangle_v.
\tag{2}
\]

Choose a_p in D_p with logarithm 1 and put
a_+ = (a_p,tau a_p), a_- = (a_p,-tau a_p). There is a unique
z^- in R^- such that b(a_-)(z^-) = 1. After choosing any invariant
ordinary local lift of a_+, there is an F-linear functional t_d on S
such that, on S_00,

\[
\Delta_d(x)=t_d(x)a_-,\qquad
\langle\beta_{00,d}(x),z^-\rangle_{\rm PT}=t_d(x).
\tag{3}
\]

A change of that local lift replaces t_d by t_d - c ell for some
c in F. In particular, for

\[
x_{P,Q}=\log_p(Q)j_K(P)-\log_p(P)j_K(Q)
\]

the well-defined strict obstruction is the determinant

\[
\boxed{\Delta_d(x_{P,Q})=
 \bigl(\log_p(Q)t_d(j_K(P))-\log_p(P)t_d(j_K(Q))\bigr)a_-.}
\tag{4}
\]

Under the rational-point hypothesis, x_(P,Q) is nonzero and spans
S_00. It has a strict first-order lift exactly when the determinant
in (4) is zero. Equivalently, the normalized z^- has a relaxed
first-order lift for the inverse deformation 1 - epsilon d.

The minus relaxed space survives even though the minus ordinary
space vanishes. Its mixed pairing with a plus strict vector is not
killed by the anticyclotomic conjugation sign. The formal local maps,
dual complexes, Kummer-space dimensions, and injectivity of the
logarithm on a rational point lattice allow either value in (4), as
the model below proves. This rules out a proof of automatic vanishing
from those data alone. It does **not** prove that an actual rational
Kummer vector has nonzero derivative. Arithmetic necessity of strict
lifting, its sufficiency for Kummer membership, and q(kappa) = 0 all
remain unresolved. No rational-rank bound has been improved.

## Proof

**The correct dual local condition.** At v | p the local finite line
is its own annihilator. The annihilator of the zero local condition
is instead the whole local H^1. Thus the dual of C_00 is C_rel, not
the ordinary complex C_f. At the fiber, duality gives

\[
H^2(C_{00})\simeq R^\vee,\qquad H^2(C_f)\simeq S^\vee.
\tag{5}
\]

L009 checks that H^0(K_v,V), H^0(K_v,V_v^-), and H^2(K_v,V_v^+)
vanish. In particular H^1 of the ordinary local complex is D_v,
and its H^0 and H^2 vanish. The strict and relaxed H^1 therefore
identify with the stated classical groups, without extra H^0 terms.
The unramified complexes away from p are acyclic after inverting p,
as also checked in L009. These assertions persist to first order.

Let U be the sum of the ordinary local complexes at p. Changing from
zero to ordinary conditions gives the exact triangle
C_00 -> C_f -> U -> C_00[1]. Its long exact sequence and H^0(U) =
H^2(U) = 0, followed by (5), give (1). The duality boundary map is
adjoint to localization on R, giving the displayed local-pairing
formula. It vanishes on loc(S) by global reciprocity; on the other
side it annihilates S because each finite local line is self-orthogonal.

For clarity, fix the sign as follows. Suppress the common local
conditions away from p. Represent a strict cochain by (g,h), with
differential (partial g, res g - partial h). An ordinary cochain is
(g,u,h), with differential
(partial g, partial u, res g - i u - partial h).
For a local cocycle a in U, define b(a) to be the class represented
by (0,i a) in degree two of C_00. It is the negative of the connecting
map for the projection (g,u,h) |-> u. Normalize the Poitou--Tate
pairing so this boundary has the positive local-invariant formula
in (1). The opposite global cone sign changes both boundary and
pairing signs and none of the vanishing statements.

Conjugation preserves the local invariant maps and interchanges the
two primes. All maps in (1) are equivariant. Taking minus parts,
S^- = 0 gives

\[
D^-\xrightarrow{\sim}(R^-)^\vee.
\tag{6}
\]

Since D^- is one-dimensional, (6) proves the assertion about R^-
and the existence and uniqueness of its normalized z^-. Notice the
two local terms add on a_- and z^-: each changes sign when transported
to the other prime. In particular b(a_-)(z^-) is twice the pairing
at p, so the normalization uses a nonzero scalar since p is odd.

**The strict connecting class.** For x in S_00, L009 supplies the
invariant ordinary lift y_x, with loc(y_x) = epsilon Delta_d(x).
Represent x in C_00 by (g,h). Represent y_x by (g_A,u_A,h_A) reducing
to (g,0,h); this is possible by adjusting a coboundary after reduction.
The zero finite local class at reduction is represented by a boundary,
which can be removed in the same adjustment. Thus u_A = epsilon a
for a local cocycle a, with class Delta_d(x).

Forget u_A to obtain a cochain lift (g_A,h_A) in the strict complex.
Because y_x is a cocycle, its strict differential is
(0,i u_A) = epsilon(0,i a). The coefficient connecting homomorphism
therefore gives beta_00,d(x) = b(Delta_d(x)), with exactly the sign
fixed above. Pairing proves (2). This also explains why the zero
ordinary Bockstein supplies no vanishing for the additional boundary.

**Computing the determinant.** Let D_A be the sum of the two deformed
ordinary local H^1 spaces. L009's local coefficient sequence gives
0 -> epsilon D -> D_A -> D -> 0, with injective multiplication from
the fiber. Average any lift of a_+ under the semilinear tau-action
to obtain an invariant lift a_(+,A). For each s in S, loc(s) =
ell(s)a_+, since S = S^+. Hence

\[
\operatorname{loc}(y_s)-\ell(s)a_{+,A}
 =\epsilon\,t_d(s)a_-.
\tag{7}
\]

Indeed the left side reduces to zero and is invariant; after removing
epsilon its coefficient lies in D^-. Uniqueness of y_s and of this
coefficient proves linearity of t_d. Any two choices of a_(+,A)
differ by epsilon c a_-, proving the stated change of t_d. On strict
vectors ell(x) = 0, so (7) proves (3), and linearity proves (4).
The change -c ell cancels in the determinant.

By L005 the local logarithm of every nontorsion rational point is
nonzero. Its Kummer map is injective, so the independent P,Q give
a two-dimensional subspace of S. As dim S = 2 this is all of S.
Localization has rank one; thus S_00 is one-dimensional. The
coefficient of j_K(Q) in x_(P,Q) is nonzero, so x_(P,Q) spans it.
L009's strict-lifting criterion now gives precisely the zero
determinant threshold, without assuming it holds.

**Equivalent relaxed obstruction.** Pair the strict complex for
V(1 + epsilon d) with the relaxed complex for its dual
V(1 - epsilon d). The Weil pairing cancels the two characters.
Their coefficient Bocksteins are adjoint up to sign. One way to
check this last assertion is to take finite free complexes for the
duality, write their differentials as D_0 + epsilon D_1, and use
the identity that the differential of a pairing of cochains is the
signed sum of the pairings with their differentials. On fiber
cocycles the coefficient of epsilon says exactly that the maps
induced by D_1 in the two dual complexes are adjoint up to the
degree sign. Thus their kernels are the annihilators of each other's
images; no nondegeneracy of an arithmetic height is assumed.

It follows that beta_rel,-d(z^-) vanishes if and only if
<beta_00,d(x),z^->_PT = 0 for every x in S_00. Under the rational
point hypothesis x_(P,Q) spans S_00, giving the claimed equivalence.
The relaxed coefficient exact sequence identifies this vanishing
with a relaxed first-order lift of z^-. Since the relaxed complex
has unrestricted conditions at p and acyclic conditions elsewhere,
its H^2 is global H^2(G_(K,Sigma),V). In the cocycle convention of
L009 this last obstruction is -d cup z^-. In particular a cyclotomic
lift would not answer the anticyclotomic question.

**What conjugation and rationality do not establish formally.**
Equation (2) satisfies
h(tau x,tau z) = -h(x,z), where h denotes its mixed pairing.
For x plus and z minus this is an identity, not a reason for h = 0.
Testing only z in S would instead give zero because the local
arguments would both be finite; that loses the whole space in (6).

Here is a model also retaining the dual complexes. It is a test of
these formal implications, not a Galois or elliptic-curve realization.
Let S_A = A e_1 + A e_2 with invariant basis, and D_A = A a_+ + A a_-
with tau(a_+) = a_+, tau(a_-) = -a_- and tau(epsilon) = -epsilon.
For c in F put

\[
L_c(e_1)=a_+,\qquad L_c(e_2)=\epsilon c a_-.
\tag{8}
\]

Take the ordinary complex [S_A -> S_A^vee] in degrees 1 and 2 with
zero differential, and its local map to D_A in degree 1 to be L_c.
Its strict mapping fiber is the complex

\[
[S_A\xrightarrow{s\mapsto(0,L_c s)}S_A^\vee\oplus D_A].
\tag{9}
\]

Use the inverse-parameter dual of (9), shifted to degrees 1 and 2,
as the relaxed dual complex. Explicitly it is

\[
[S_A\oplus D_A^\vee
 \xrightarrow{(s,\phi)\mapsto L_c(-\epsilon)^t\phi}S_A^\vee].
\tag{10}
\]

Evaluation gives perfect complex duality; the transposed differential
is exactly the adjoint relation just used. All differentials and maps
are equivariant. At the fiber the strict H^1 is F e_2, the ordinary
H^1 is S = F e_1 + F e_2, and the relaxed H^1 is
R = S direct-sum F b_-, where b_- is dual to a_- and is anti-invariant.
The boundary sends a_+ to zero and a_- to the functional dual to b_-.
This verifies the entire sequence (1), including its signs, dimensions,
and pairings. The ordinary Bockstein is zero, while
beta_00(e_2) = c a_- and beta_rel(b_-) = -c e_2^vee. Thus strict
liftability holds for c = 0 and fails for c = 1, compatibly with
the dual obstruction, with identical fiber data.

To retain the rational-logarithm test, choose lambda in F transcendental
over Q and use the abstract rational lattice generated by
P = e_1 and Q = lambda e_1 + e_2. Such a lambda exists because F is
uncountable and the elements algebraic over Q form a countable set.
Set W = S, j the identity, and ell(e_1) = 1, ell(e_2) = 0.
Then ell(aP+bQ) = a+b lambda is nonzero for all nonzero rational
pairs (a,b). Thus this model has no nontorsion rational lattice
vector of logarithm zero, respecting L005's necessary injectivity
property. Nevertheless x_(P,Q) = -e_2, and its determinant is -c.
It can be nonzero even in this formal full-Kummer model.

This is stronger than ignoring the dual local condition, but it
still does not include the additional geometry of actual rational
points. In particular it cannot refute arithmetic necessity of
strict lifting. Formula (4) isolates what that claim would require:
t_d restricted to the actual rational Kummer space must be proportional
to ell. Neither the ordinary height vanishing nor the formal duality
data prove this proportionality. For the original unknown kappa,
the bound remains r <= 2, with r >= 2 still missing.

The exact check `python3 scripts/strict-relaxed/check_model.py`
verifies the fiber sequence, epsilon-linearity, conjugation, inverse
dual differentials, and coefficient-sequence dimensions for c = 0,1.
It checks the formal model only; the proof of logarithm injectivity
on its rational lattice is the irrationality argument above.

## Mathlib

Full coverage of the arithmetic strict/relaxed pairing and rational
point determinant: **not checked**. Supporting mapping-fiber, dual
complex, exact-sequence, and eigenspace results: **not checked**.
Nekovar's Theorem 6.3.4 and Section 11.1.3, and Buyukboduk's
Definitions 2.1--2.2 and Section 2.1.3, are retained with direct links
in the duality foundation. They support the duality and Bockstein
formalism, not a theorem asserting the determinant vanishes or a
Mathlib match for this statement. The deductions and the scope of
the formal model are proved here.
