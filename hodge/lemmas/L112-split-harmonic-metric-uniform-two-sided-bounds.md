# L112 — Uniform two-sided bounds for the actual split harmonic metric

## Hypotheses

Retain all hypotheses and conclusions of audited L111. Thus the
conditional locally free rank-two F on p:S_1 x B -> B has integral
c_1(F)=0, ch_2(F)=-14e_1-21e_2-tau_D and the given smooth compatible
connection at the identical marked hyperkähler metrics. The full tensor
and its action D[sigma]=2lambda[sigma], 1<lambda<5/4, are retained.
Put V=End_0(F), M=R^1p_*V=E. The split locus Z is finite, possibly
empty; U=B minus Z has stable fibres. Use the smooth Hermitian metric
on V induced by this connection, including over Z, and the fixed fibre
Kähler metric. Let G be the resulting fibrewise harmonic L2 metric
on M|_U, with its natural higher-image identification.

At each z in Z use L111's actual minimal complex of ranks (1,52,1),
its convergent Koszul-plane splitting and its natural identification
of the rank-fifty middle summand with M. In particular this is an
actual representative of Rp_*V, not merely a complex with matching
cohomology dimensions. No ordinary middle base change at z, bound on
the varying harmonic projection, metric extension, curvature estimate
or semistability of E is assumed. F and a nonempty Z remain hypothetical.

## Conclusion

For every z in Z there is a coordinate ball D about z, containing no
other point of Z, a holomorphic frame e_1,...,e_50 of M on D and constants
0<c<=C<infinity such that

\[
 c\sum_{i=1}^{50}|\xi_i|^2
 \ \le\ G_b\left(\sum_i\xi_i e_i(b),\sum_i\xi_i e_i(b)\right)
 \ \le\ C\sum_{i=1}^{50}|\xi_i|^2                         \tag{1}
\]

for every b in D minus {z} and every xi in C^50. Both constants are
independent of b, including its direction of approach to z. The same
assertion holds, with changed constants and possibly a smaller ball,
in any holomorphic frame extending across z. If Z is empty, the
assertion at split points is vacuous.

This is a conditional ADVANCE / REPRODUCTION under the prior SPECIALIZE
assessment. The separate critical audit below preserves the result, with
outcome EXPLORATION / REPRODUCTION: no substantive error or stronger
conclusion is found. It supplies a quantitative prerequisite only: no continuous or smooth extension of G, curvature
integrability, connection extension, semistability, bound on |Z|,
existence of F, algebraic cycle or transport is concluded. The universal
primitive rational Hodge gap remains unresolved.

## Proof

**Imported comparison and its applicability.** Use the unchanged prior
assessment `drafts/literature/2026-10-16-split-harmonic-metric-two-sided-bounds.md`.
The analytic input is Bismut--Gillet--Soulé, *Analytic torsion and
holomorphic determinant bundles III*, Comm. Math. Phys. 115 (1988),
301--351, DOI 10.1007/BF01466774, [section 1(b)--(c), pp. 304--305,
and Theorem 3.5 with Lemmas 3.6--3.8 and its proof, pp. 342--345](https://www.imo.universite-paris-saclay.fr/~jean-michel.bismut/Bismut/1988b.pdf#page=42).
These supply the natural relative-Dolbeault comparison, its derived-fibre
compatibility, and smooth finite spectral reduction. Here p is smooth
proper holomorphic and V is holomorphic locally free; its given metric
and the fibre metric are smooth through z. The product is Kähler.
No positivity of V is needed. These general tools are imported; the
specialization below is the norm estimate, not a determinant-metric
argument. For maps between finite free representatives use the
bounded-projective comparison in [Stacks Lemma 13.19.8, 064B](https://stacks.math.columbia.edu/tag/064B),
already used in L111, over the analytic local ring.

**Actual frame and full complex.** Work near one z. Analytify L111's
actual representative and splitting. All its finitely many coefficients
and inverses of units are holomorphic on a sufficiently small neighborhood;
the identities there remain exact. In coordinates x,y centered at z,
write this complex as

\[
 K:\quad \mathcal O\xrightarrow{d^0}
       P\oplus J\xrightarrow{d^1}\mathcal O,
 \quad P=\mathcal O a\oplus\mathcal O b_0,
 \quad J\simeq\mathcal O^{50},                           \tag{2}
\]

where, for a holomorphic unit u,

\[
 d^0(1)=x a+y b_0=:v,\qquad
 d^1(\alpha a+\beta b_0+j)=u(y\alpha-x\beta).             \tag{3}
\]

Here b_0 denotes a basis vector, not a base parameter. Equations (2)--(3)
include every higher coefficient of the actual complex, through a,b_0,J
and u. Their differentials vanish at z. Choose a holomorphic frame
e_i of J; taking cohomology identifies it with a frame of the actual M,
by L111. We use the same notation for these cohomology classes.

**Smooth spectral comparison that retains this frame.** Let
A^q_b be the space of smooth V_b-valued (0,q)-forms on S_1 and write
delta_b=bar-partial_{V_b}. Put
Delta_b=delta_b delta_b^*+delta_b^* delta_b. Choose epsilon>0 below
the first positive eigenvalue of Delta_z in every degree. On a smaller
neighborhood the spectral spaces

\[
 H^q_b=\operatorname{im}{\bf1}_{[0,\epsilon)}(\Delta_b)
                                                               \tag{4}
\]

form smooth finite-dimensional bundles of ranks (1,52,1). Indeed their
central fibres are precisely the harmonic spaces with those dimensions,
and the ranks are locally constant at this spectral cutoff. They form
a complex under delta. Let Pi be their smooth orthogonal spectral
projection; it commutes with delta. The L2 metric on H^q is smooth
and positive definite across z. These H^q are cutoff spaces, and need
not equal the harmonic spaces away from z.

We require more than an abstract cohomology-module isomorphism. To
construct the needed map, choose the finite holomorphic representative
P' and its map to the total Dolbeault direct-image complex as in the
proof of BGS Theorem 3.5. Both P' and K represent the same actual
analytic Rp_*V. At the analytic stalk choose a chain homotopy equivalence
alpha:K -> P' implementing these specified identifications, using
064B. Both complexes are bounded finite free locally, so the finitely
many maps, homotopies and their identities spread to a smaller
neighborhood. In particular alpha remains a homotopy equivalence.

Compose alpha with the BGS map to relative smooth Dolbeault forms,
and call the resulting smooth chain map f:K -> A. Lemma 3.7 gives
the natural derived-fibre comparison for the BGS map. It therefore
also does so for f, because alpha is a homotopy equivalence before
and after taking any fibre. Thus f_z is a quasi-isomorphism, and f
induces the natural higher-image comparison, with the prescribed
identification of K with Rp_*V.

Now set

\[
                         T=\Pi f:K\longrightarrow H^\bullet.
                                                               \tag{5}
\]

This is a smooth chain map. The spectral inclusion and projection are
inverse on cohomology: BGS Lemma 3.8 gives a smooth homotopy on the
high spectral complement. In particular T_z is a quasi-isomorphism.
The differentials of K_z are zero by minimality, and those of H_z
are zero because its elements are harmonic. Consequently each

\[
                        T_z^q:K_z^q\longrightarrow H_z^q
                                                               \tag{6}
\]

is a vector-space isomorphism. This uses the derived dimensions
(1,52,1), including the two extra central middle classes. It does
not identify M_z/m_z M_z with H^1(S_1,V_z).

The determinants in (6) remain nonzero on a smaller neighborhood.
Hence T is a degreewise smooth chain isomorphism there. In degree one
pull back the actual cutoff L2 metric by T^1, obtaining a smooth
positive-definite metric H_K on K^1=P+J through z. By construction
the cohomology class of T^1 e_i at a stable parameter is precisely
the natural class of the ordinary sheaf section e_i in H^1(S_1,V_b).
The natural BGS comparison, rather than an arbitrary choice of a
cohomology isomorphism, ensures this assertion. Ordinary base change
is used only on the stable open, where cohomology is concentrated
in degree one, as retained in L111's hypotheses.

**The actual harmonic norm is this quotient norm.** Fix b!=z in this
neighborhood. The delta_b-harmonic representative of a closed element
of H^1_b lies in H^1_b, since every harmonic form has eigenvalue zero.
Moreover the orthogonal complement of the harmonic space inside
ker(delta_b|H^1_b) is delta_b H^0_b. This is finite-dimensional Hodge
decomposition for the cutoff complex: the restricted adjoint is the
restriction of delta_b^*, because the cutoff commutes with delta_b
and delta_b^*. Equivalently the positive-eigenvalue exact part is
contracted by delta_b^* Delta_b^{-1} on that part, for this fixed b.
No bound for that inverse as b tends to z is asserted or used.
It follows that the squared harmonic norm of a class represented by
c in ker(delta_b|H^1_b) is exactly

\[
                    \min_{w\in H^0_b}\|c+\delta_b w\|_{L^2}^2.
                                                               \tag{7}
\]

This is the original fibrewise harmonic norm: both the harmonic
representative and the inner product are those of the given full
Dolbeault complex and given coefficient metric. A complex gauge
change or a newly chosen Hermite--Einstein metric has not replaced it.

For b!=z at least one of x(b),y(b) is nonzero. Thus (3) gives

\[
 \ker d^1_b=J_b\oplus\mathbb C v(b),\qquad
 \operatorname{im}d^0_b=\mathbb C v(b)\subset P_b.        \tag{8}
\]

Since T is a chain isomorphism, (7) translates for
j=\sum_i\xi_i e_i(b) into the exact formula

\[
              G_b(j,j)=\min_{t\in\mathbb C}
                          H_{K,b}(j+t v(b),j+t v(b)).    \tag{9}
\]

**Both uniform inequalities.** Declare the holomorphic frame
a,b_0,e_1,...,e_50 of K^1 to be orthonormal for a reference metric
H_0. Choose a closed coordinate ball contained in the neighborhood
where T is invertible. Relative to H_0 the least eigenvalue of H_K
has a positive minimum c there and the greatest eigenvalue a finite
maximum C. Indeed H_K is smooth positive definite on the entire
closed ball, including its center. Hence

\[
                         c H_0\le H_K\le C H_0.         \tag{10}
\]

The spaces P_b and J_b are orthogonal for H_0 by its definition, so
for every t and every b!=z,

\[
 H_{K,b}(j+t v,j+t v)
 \ge c\left(\sum_i|\xi_i|^2+|t|^2(|x(b)|^2+|y(b)|^2)\right)
 \ge c\sum_i|\xi_i|^2.                                 \tag{11}
\]

Minimizing proves the lower bound in (1). Choosing t=0 in (9) and
using (10) gives the upper bound C sum_i|xi_i|^2. Restricting to the
interior D proves (1) on one full punctured ball. Neither estimate
divides by |x|^2+|y|^2, so no direction or axis is omitted. A change
to any holomorphic frame extending across z has a smooth invertible
matrix through z; on a smaller closed ball its norm and inverse
norm are bounded. This proves the stated frame independence.

The achieved constants meet exactly the positive finite threshold
requested. They depend on this local conditional family, metric and
frame; no effective universal values are claimed. The possible
directional behavior of the minimizing boundary term is not controlled
by these inequalities, so no metric limit or derivative estimate follows.
This does not revive the automatic extension inference parked in
ATTEMPTS/066, nor the metric/degree or duality-only mechanisms in
ATTEMPTS/063/067. For Z empty there is no local split-point test.
All independent global existence, transport and Hodge gaps remain.

**Separate critical audit, 2026-10-16.** Reuse the unchanged prior
SPECIALIZE assessment
`drafts/literature/2026-10-16-split-harmonic-metric-bounds-critical-audit.md`.
The input is audited L111, including its actual derived identification,
not a newly chosen complex with the same ranks. The checks below preserve
(1) and the existing dependency. They do not assert another estimate.

First check the natural map, before comparing norms. Write
D_tot=p_*Dol_{S_1 x D}(V) and A=p_*Dol_{(S_1 x D)/D}(V).
The former has the total Dolbeault differential and is a complex of
holomorphic-function modules representing the analytic Rp_*V. The
latter has the vertical differential and is a complex of smooth-function
modules. Projection of forms to vertical covectors gives the natural
chain map D_tot -> A. It kills the pulled-back positive-degree base
forms; the projected total differential is exactly the vertical one.
It is holomorphic-function linear. Extending scalars in the composite
P' -> D_tot -> A makes it smooth-function linear, since the vertical
differential commutes with multiplication by smooth functions on D.
This is the map in the proof of BGS Theorem 3.5, pp. 343--344, whose
fibre is tested in Lemma 3.7. It is not a claim that the total
Dolbeault differential is smooth-function linear on the base.

Naturality can be kept after spreading the stalkwise comparison.
At the analytic stalk, represent the specified identification of K
with D_tot by a chain map chi, and denote the BGS map by phi:P' -> D_tot.
Such representatives exist by 064B in modules over O_{D,z}: the sources
are bounded finite free. Choose alpha to represent
[phi]^{-1}[chi], not an arbitrary isomorphism K -> P'. Then
phi alpha-chi is nullhomotopic at the stalk. Choose also an inverse
of alpha and its two inverse homotopies, using the same theorem for
the finite free complexes. Each map and homotopy from these bounded
finite free sources is specified by finitely many germs. All those
germs and the finitely many chain-map and homotopy identities spread
to a common smaller neighborhood. This applies also to chi and the
homotopy into D_tot, whose target need not be finite free. Thus alpha
is a homotopy equivalence there and phi alpha induces the prescribed
natural higher-image map on that neighborhood. No claim that locally
free analytic sheaves are globally projective objects is needed.
Projection to A and smooth scalar extension preserve these identities.
On the stable open their map is the natural Dolbeault/base-change
identification of each ordinary section e_i. At the center Lemma 3.7
instead compares the full derived fibre, so no ordinary split base
change has entered the argument.

Second check invertibility at the jump. L111's full differential is
(x,y,0) into the plane and u(y,-x,0) out of it, so every central
differential vanishes. A single positive cutoff below the first
positive central eigenvalue in every degree retains central harmonic
dimensions (1,52,1). BGS section 1(b)--(c) and Lemma 3.8 supply the
smooth cutoff complex and the high-spectrum homotopy. In particular
Pi_z f_z is a quasi-isomorphism. Both source and target central
complexes have zero differentials, so its components themselves are
isomorphisms; there are no acyclic central summands to discard.
In smooth local trivializations their determinants remain nonzero
on one neighborhood. Shrinking once for the finitely many degrees
makes T a degreewise smooth chain isomorphism. The two additional
central middle classes are retained throughout; the fifty-dimensional
ordinary fibre of M is never substituted for this fifty-two-dimensional
space. Pullback by T^1 therefore gives a smooth positive metric on all
of K^1, including the center. This uses the original coefficient metric.
It neither constructs a bounded inverse for the low nonzero eigenvalues
nor extends the jumping harmonic projection.

Third check the metric identification at each b different from z.
The cutoff is orthogonal and commutes with delta and delta^*, so the
adjoint of its finite differential is the restricted full adjoint.
Its harmonic space is consequently exactly the full harmonic space.
Finite-dimensional orthogonal Hodge decomposition gives
ker(delta|H^1)=Harm^1 direct sum delta H^0, an orthogonal sum for the
given L2 product. The harmonic representative of any class is its
unique least-norm representative modulo this boundary space. Under T,
the boundary space is the image of d^0, precisely C v(b), and the
closed middle space is J_b direct sum C v(b). The class of T^1 j is
the natural class of j by the first check. This proves (9) for the
actual metric, with no unspecified cohomology automorphism, gauge
renormalization or surrogate Hermitian product. Minimization over all
of H^0_b is exactly minimization over t in C, because T^0 is an
isomorphism. A possible unbounded minimizing coefficient t as b tends
to z is harmless for the following inequalities.

Finally take a closed ball strictly inside the common neighborhood of
invertibility. Smooth positive definiteness makes the minimum eigenvalue
of H_K relative to H_0 strictly positive and its maximum finite on this
compact ball. These are fixed constants, independent of b. In the
chosen reference product J and P are orthogonal, so every representative
j+t v has H_0-norm squared at least the coefficient norm squared of j.
This proves the lower bound even if t diverges. The admissible choice
t=0 proves the upper bound with the same fixed maximum eigenvalue.
These arguments use neither x nor y as a denominator and include both
coordinate axes and every direction in the punctured ball. For another
frame extending holomorphically across z, its transition matrix and
inverse are uniformly bounded after shrinking; substituting these
bounds gives the stated frame independence. If Z is empty there is
no split-point assertion to check.

Both required thresholds, c>0 and C<infinity on a full punctured ball,
survive. This audit is EXPLORATION / REPRODUCTION: it verifies the
existing conditional specialization and finds no substantive repair,
stronger obstruction or existence statement. The formula can still
have direction-dependent minimizing boundary terms; the proof provides
no derivative bound or metric limit. In particular curvature
integrability, connection or metric extension, semistability, |Z|,
existence of F, transport and universal primitive Hodge realization
remain unresolved. ATTEMPTS/063/065/066/067 stay in force in their
recorded scopes. No argument or DAG change is required.

## Mathlib

Full matching coverage for this actual-family spectral comparison and
harmonic quotient-norm estimate has not been checked. The supporting
analytic input is the precise BGS result cited above; the finite-free
comparison uses the cited Stacks lemma and L111's already established
actual splitting. No absence claim or formal verification is made.
The proof is an informal specialization of these known tools preserved
by the separate critical audit above; it is not a candidate Hodge resolution.
