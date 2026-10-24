# L148 — Two-sided bounds for the actual twisted harmonic metric

## Hypotheses

Retain L146/L147's conditional equality kernel F on the identical
marked K3 product p:S_1 x B -> B, with the fixed common hyperkähler
metric, integral c_1(F)=0 and

\[
             \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D.
\]

Thus F is locally free of rank two and slope-polystable at the given
product class, with its smooth compatible Hermitian connection. Let
c_1(L)=k=(-4,-2,1,2), k.h=0 and k^2=-14. Put
G=F tensor p_1^*L^{-1} and M=R^1p_*G. Give G the tensor product of
the given metric on F with one fixed smooth positive Hermitian metric
on L^{-1}; use the fixed fibre Kähler metric to define harmonic L2
norms. Write H for the resulting metric on M|_U, under its natural
higher-image identification, where U=B minus the finite possibly
empty split set Z. L147 gives concentration in degree one on U and
global local freeness of M of rank 24.

At each z in Z retain L146's actual full Koszul splitting of the
minimal representative of Rp_*G, including its specified derived
identification and identification of the free middle complement with
M. Its derived central dimensions are (1,26,1), not (0,24,0).
No scalar self-duality of G, bounded harmonic projection through z,
metric extension or curvature estimate is assumed. F and a nonempty
Z remain hypothetical.

## Conclusion

For each z in Z there are a coordinate ball D about z, a holomorphic
frame e_1,...,e_24 of M on D, and constants 0<c<=C<infinity such that

\[
 c\sum_{i=1}^{24}|\xi_i|^2
 \le H_b\left(\sum_i\xi_i e_i(b),\sum_i\xi_i e_i(b)\right)
 \le C\sum_{i=1}^{24}|\xi_i|^2                         \tag{1}
\]

for every b in D minus {z} and every xi in C^24. The constants are
independent of the direction of approach, including both coordinate
axes. Any holomorphic frame extending across z satisfies such bounds
after shrinking D and changing the constants. If Z is empty, the
split-point assertion is vacuous.

This is a conditional ADVANCE / REPRODUCTION specialization of known
analytic tools. The separate critical audit below preserves the estimate
without a substantive repair or stronger conclusion. It establishes no
metric limit, derivative or curvature bound, connection extension,
polystability of M, cardinality bound, F or split-locus existence,
algebraic cycle or transport. Universal primitive Hodge realization
remains unresolved.

## Proof

**Imported tools and changed coefficient.** Reuse the unchanged prior
SPECIALIZE assessment
`drafts/literature/2026-10-23-twisted-harmonic-metric-two-sided-bounds.md`.
The primary analytic input is Bismut, Gillet and Soulé, *Analytic
torsion and holomorphic determinant bundles III. Quillen metrics on
holomorphic determinants*, Comm. Math. Phys. 115 (1988), 301–351,
DOI 10.1007/BF01466774, [Section 1(b)–(c), pp. 304–305, Theorem 3.5
and its complete proof through Lemmas 3.6–3.8, pp. 342–345](https://www.imo.universite-paris-saclay.fr/~bismut/Bismut/1988b.pdf#page=42).
These give the natural relative-Dolbeault comparison, derived-fibre
comparison and smooth finite spectral reduction through a cohomology
jump. Import these general results without reproof. The source allows
an arbitrary smooth Hermitian holomorphic bundle: G is such a bundle
on the smooth proper holomorphic product projection, with the given
smooth fibre metrics. Neither positivity in the curvature sense nor
scalar self-duality is required. For stalkwise chain representatives
use [Stacks Lemma 13.19.8, tag 064B](https://stacks.math.columbia.edu/tag/064B),
in modules over the analytic local ring with bounded finite free
source. This does not assert global projectivity of analytic bundles.

L112's comparison construction and its audit are a technique for a
different coefficient, not an input asserting (1). Here the actual
algebraic replacement is L146; no rank-50 complement, Serre form or
Hermitian orthogonality from the adjoint coefficient is imported.

**The actual holomorphic frame.** Fix z. Analytify and spread L146's
finite algebraic splitting, its units and identities to a small
analytic neighborhood. Its parameters x,y are holomorphic coordinates
after shrinking. Write the actual representative in degrees 0,1,2 as

\[
 K:\quad O\xrightarrow{d^0}P\oplus J\xrightarrow{d^1}O,
 \quad P=Oa\oplus Ob_0,\quad J\simeq O^{24},             \tag{2}
\]

where for a holomorphic unit u,

\[
 d^0(1)=xa+yb_0=:v,\qquad
 d^1(\alpha a+\beta b_0+j)=u(y\alpha-x\beta).             \tag{3}
\]

The notation b_0 denotes a basis vector, not a parameter. The full
higher coefficients remain in a,b_0,J and u. L146 identifies the
inclusion of J into this complex with the ordinary middle image;
L147 identifies that image with the actual globally defined M.
Choose the corresponding frame e_i of J and M. Analytification of
coherent proper direct images and of the specified complex preserves
these identifications. In particular every differential of K_z is
zero, while the ordinary fibre of M has dimension 24.

**Natural spectral comparison.** Let A_b^q be smooth G_b-valued
(0,q)-forms on S_1, with vertical Dolbeault differential delta_b.
Take Delta_b=delta_b delta_b^*+delta_b^* delta_b for the given L2
product. Choose epsilon>0 strictly below the first positive central
eigenvalue in each degree. On one smaller neighborhood the orthogonal
spectral cutoff spaces

\[
 E_b^q=\operatorname{im}{\bf1}_{[0,\epsilon)}(\Delta_b)    \tag{4}
\]

are smooth bundles of ranks (1,26,1), with smooth positive L2
metrics. Their central fibres are the harmonic spaces. The cutoff
projection Pi commutes with delta and delta^*, so E is a smooth
finite complex. It need not consist of harmonic forms off z.

We keep the natural frame identification, rather than choosing an
arbitrary cohomology isomorphism. Denote the total Dolbeault
direct-image resolution by D_tot and its natural projection to the
vertical relative complex by D_tot -> A. Projection kills positive
base-form degrees, commutes with the differentials, and is linear
over holomorphic base functions. The vertical differential in A
also commutes with smooth base functions. Thus the composite below
extends smoothly over base scalars; the total differential itself
is not asserted to be smooth-function linear on the base.

Let P' be the finite holomorphic complex with its natural comparison
phi:P' -> D_tot used in the proof of BGS Theorem 3.5. At the analytic
stalk choose chi:K -> D_tot representing K's specified identification
with the actual Rp_*G. By 064B choose alpha:K -> P' representing
[phi]^{-1}[chi]. The same result makes phi alpha-chi nullhomotopic
and makes alpha a chain homotopy equivalence. The bounded finite
free sources specify these maps, an inverse and the relevant
homotopies by finitely many germs. Spread them and their finitely
many identities to one common smaller neighborhood. This also
applies to the homotopy into D_tot: finite freeness is required of
the source, not of that target. Consequently phi alpha induces the
prescribed natural higher-image map throughout this neighborhood.

Project phi alpha to A and extend scalars smoothly to obtain f:K -> A.
BGS Lemma 3.7 supplies its natural derived-fibre comparison, and
Lemma 3.8 contracts the high spectral complement. Hence

\[
                          T=\Pi f:K\longrightarrow E             \tag{5}
\]

is a smooth chain map with T_z a quasi-isomorphism. Both central
complexes have zero differentials: K_z by (3), E_z by harmonicity.
Thus each component T_z^q is an isomorphism of vector spaces, with
all 26 central middle classes retained. In smooth trivializations
the finitely many determinants stay nonzero on one neighborhood.
So T is a degreewise smooth chain isomorphism there. No bound for
an inverse small positive eigenvalue, nor ordinary middle base
change at z, is used in this reasoning.

Pull back the cutoff L2 metric in degree one by T^1, calling it H_K.
It is smooth and positive definite on all of K^1=P plus J, including
z. At b in U, the class of T^1e_i(b) is the natural Dolbeault class
of the ordinary sheaf section e_i. This follows from the specified
comparison and its homotopy above, followed by ordinary base change
only on U, where L147 gives concentration. It is not a freely
chosen identification of the harmonic space with C^24.

**Exact quotient formula for the given metric.** At a fixed b!=z,
the harmonic space of the cutoff complex equals the full Dolbeault
harmonic space: all harmonic forms have eigenvalue zero, and the
cutoff commutes with the differential and adjoint. Its orthogonal
Hodge decomposition consequently gives

\[
 \ker(\delta_b:E_b^1\to E_b^2)
       =\operatorname{Harm}_b^1\mathbin{\oplus^{\perp}}\delta_b E_b^0.
                                                               \tag{6}
\]

In particular the actual harmonic norm of a closed cutoff element's
class is its minimum squared L2 norm modulo delta_b E_b^0. This is
finite-dimensional orthogonal Hodge decomposition (also recalled in
BGS, proof of Theorem 3.14, p. 350), for the original metric. The
statement needs no uniform inverse on the low positive spectrum.

By (3), for b!=z,

\[
 \ker d_b^1=J_b\oplus\mathbb C v(b),\qquad
 \operatorname{im}d_b^0=\mathbb C v(b)\subset P_b.        \tag{7}
\]

Indeed u is nonzero and (x(b),y(b)) is nonzero; the kernel of
(y(b),-x(b)) is its span. Apply the chain isomorphism T and the
natural-frame identification to (6). For j=sum xi_i e_i(b), the
requested, original harmonic metric is exactly

\[
                    H_b(j,j)=\min_{t\in\mathbb C}
                                H_{K,b}(j+tv,j+tv).      \tag{8}
\]

The minimization covers every boundary because T^0 is an isomorphism.
No HE metric on the nearby twisted coefficients, scalar Serre form
on G, or alternative gauge metric has replaced the given one.

**Uniform lower and upper bounds.** Let H_0 make the holomorphic
frame a,b_0,e_1,...,e_24 orthonormal. On a closed coordinate ball
strictly inside the common comparison neighborhood, smooth positive
definiteness of H_K supplies fixed constants 0<c<=C<infinity with

\[
                            cH_0\le H_K\le CH_0.         \tag{9}
\]

Here c is the minimum least eigenvalue and C the maximum greatest
eigenvalue on the compact ball; they include its center. The
reference summands P and J are orthogonal, hence for every t,

\[
 H_{K,b}(j+tv,j+tv)
 \ge c\left(\sum_i|\xi_i|^2+|t|^2(|x(b)|^2+|y(b)|^2)\right)
 \ge c\sum_i|\xi_i|^2.                                 \tag{10}
\]

Taking the minimum in (8) proves the lower bound. Taking t=0 and
using (9) proves the upper bound. Restricting to the interior gives
(1) on a full punctured ball. Neither argument divides by v or by
its length, so even an unbounded minimizing t causes no loss of a
direction or axis. Any other holomorphic frame extending through z
has a transition matrix and inverse bounded on a smaller closed
ball. Substituting these bounds proves the frame assertion.

Both required thresholds c>0 and C<infinity are reached for the
actual metric, with constants depending on the conditional family,
fixed metrics and frame. No effective universal constants are claimed.
The minimum in (8) can still depend on the direction of v; boundedness
does not supply a limit or control derivatives. Thus this result
does not reopen the automatic surface-extension inference in
ATTEMPTS/066, the singular-quotient metric bridge in ATTEMPTS/063,
the strict-Euler mechanism in ATTEMPTS/060 or the duality-only bound
in ATTEMPTS/067. Z empty is allowed. Kernel existence, curvature and
extension, positivity, a useful split-set bound, reconstruction,
transport and the main Hodge gap remain independent unresolved steps.

**Separate critical audit, 2026-10-23 (step 475).** Reuse the unchanged
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-23-twisted-harmonic-metric-bounds-critical-audit.md`
and the precise BGS III and Stacks 064B coverage cited above. The
verdict is EXPLORATION / REPRODUCTION: the conditional estimate survives,
with no substantive error, necessary repair or stronger conclusion.
This is verification of an existing specialization, not a new estimate
or progress beyond the inspected sources. L146's audited splitting
and L147's actual image are retained inputs.

First, the comparison must carry the specified ordinary sections.
At the analytic stalk put R=O_{B,z}. Both K and the BGS representative
P' are bounded finite free R-complexes. Stacks 064B therefore applies
to maps out of either of them into an arbitrary R-complex, including
D_tot; it requires no projectivity of D_tot or of analytic sheaves
as objects in their global category. Choose alpha to represent exactly
[phi]^{-1}[chi]. The same Hom identification represents its inverse
and gives inverse homotopies, as well as a homotopy between phi alpha
and chi. There are finitely many source generators in finitely many
degrees. Images of these generators and all homotopy identities are
therefore finitely many germs, and all spread to one common smaller
neighborhood. The prescribed identification with Rp_*G is retained,
not replaced by an arbitrary automorphism of its middle cohomology.

In the product, the ideal of positive-degree pulled-back base forms
in the total Dolbeault complex is preserved by its differential.
The quotient is the relative complex with vertical differential.
Thus projection D_tot -> A preserves the chain and homotopy identities
over holomorphic base functions. Only the resulting relative maps
are extended over smooth base functions: their vertical differential
annihilates those functions. No such assertion is made for the total
Dolbeault differential. Restricting the inverse homotopies for alpha
to z preserves them, so alpha_z is a homotopy equivalence. Composing
with BGS Lemma 3.7's natural fibre comparison and the cutoff projection
gives the quasi-isomorphism T_z. This use of the derived fibre is
separate from ordinary base change, which is used only on U where
L147 proves concentration. On U the map of each e_i is consequently
its natural coefficient Dolbeault class.

Second, central quasi-isomorphism really gives termwise invertibility
here. The full equations (3) make both central differentials zero.
The positive spectral gap at z and the smooth cutoff construction
give ranks (1,26,1), with zero central cutoff differential because
the cutoff contains only harmonic forms there. Hence cohomology of
each central complex is its entire graded vector space. T_z is thus
invertible in all three degrees. Continuity of the three determinant
functions in smooth trivializations gives one neighborhood of
invertibility. All 26 central middle directions are retained; the
ordinary 24-dimensional fibre does not justify this step. Pullback
of the given cutoff metric by T^1 is smooth and positive at the
center as well. Neither a low-positive-eigenvalue inverse nor a
harmonic projection through the jump has been assumed.

Third, the cutoff quotient uses the original metric. The orthogonal
spectral projection commutes with delta and delta^*. Therefore the
adjoint of delta restricted to E is the restriction of delta^*,
and the finite complex's harmonic space is the full harmonic space.
Every full harmonic element lies in E, while a finite harmonic element
is annihilated by both full operators. Orthogonal decomposition of
ker delta in this finite Hermitian complex gives precisely (6).
It identifies the harmonic norm with the least norm modulo its entire
boundary space, not merely modulo a chosen smaller set of exact forms.
Since T is a chain isomorphism, T^0 maps onto E^0, and this boundary
space is exactly T^1(C v). Equations (3) give ker d^1=J plus C v for
every nonzero (x,y), including either axis. With the natural class
identification already checked, this proves (8) for the given metric.
No scalar self-duality, parallel Serre form, or central Hermitian
orthogonality between the actual summands P and J is used.

Finally, a closed ball inside this common neighborhood is compact.
The least and greatest eigenvalues of the smooth positive H_K relative
to H_0 attain a strictly positive minimum c and a finite maximum C.
Orthogonality of P and J is imposed only for the reference metric H_0.
Thus every j+t v has H_K-norm squared at least c times the coefficient
norm squared of j, uniformly in t and in the base point. Minimization
gives the lower bound; the allowed representative t=0 gives the upper
bound. Even a diverging minimizing t cannot invalidate either step.
The proof divides by neither x nor y nor the length of v. Bounded
transition matrices and inverse matrices on a smaller closed ball
give the assertion for every extending holomorphic frame.

Both thresholds c>0 and C<infinity are met on one full punctured ball.
The constants are family-dependent; this audit gives no effective
universal values, derivative estimate or metric limit. For Z empty
the assertion remains vacuous. The direct inputs remain L146 and L147;
L112 is comparison technique, not an extra mathematical premise.
ATTEMPTS/060/063/066/067 remain in force in their recorded scopes.
Curvature, extension, positivity, a useful split-set bound, F and
nonempty Z, reconstruction, transport and universal primitive Hodge
realization remain unresolved.

## Mathlib

Full matching coverage of this natural actual-family spectral
comparison and harmonic quotient estimate is **not checked**. The
precise supporting analytic and projective-comparison results are
imported above, and L146/L147 supply the algebraic specialization.
Unknown Mathlib coverage is not evidence of absence. This informal
REPRODUCTION is preserved by the separate critical audit and supplies no
general Hodge-conjecture resolution or claim of originality.
