# Equality split fibre — proposed local ASD slice comparison

TARGET: Assess whether the fixed-h ASD deformation slice at L direct sum L^{-1}, with c_1(L)=k, admits a nonconstant smooth quaternionic surface germ through the reducible point that could come from the (14,21) equality kernel.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L071/L093 and scoped line-twist/index stops; inspected Diez--Rudolph's all-point ASD chart and its proof, Buchdahl--Schumacher's non-simple slice/moment construction, and Verbitsky's coefficient quaternionic action; no matching germ-existence or no-germ theorem was established by the bounded searches.
SOURCE_EVIDENCE: Diez--Rudolph (2022), Definition 5.1, Theorems 4.13/5.3/5.8, Section 5.3 equations (5.14)--(5.23); Buchdahl--Schumacher (2022), Theorem 1, Lemma 2.5, Proposition 2.6/(2.4), Corollary 5.3/(5.1), pp. 78--84,92--93; Verbitsky alg-geom/9307008v1, Section 4/Theorem 4.1/Corollary 4.3, pp. 12--15, and stable scope of Section 6--7, pp. 21--24.
COMPARISON: Known results give a smooth equivariant ASD obstruction chart even at reducibles, an analytic fixed-Kahler bundle slice, and quaternionic coefficient harmonic cohomology. They do not identify the reducible quotient with a smooth hyperkahler manifold or realize the proposed surface germ.
GAP: Compute the actual stabilizer representation and necessary second-order obstruction, and justify the hypothetical product family's harmonic tangent comparison at the reducible fibre. Nonconstant maps with zero first derivative and higher-order realization remain separate.
REASON: Coverage permits one bounded necessary second-order compatibility attempt within the saved target, without assuming regularity or generic stability; it does not approve an exact hyperkahler quadratic normal form, analytic germ existence or kernel exclusion from a formal tangent alone.
LITERATURE_REASON: Gate-required comparison for the changed reducible rank-two scope; the ready rank-five and stable-fibre sources did not cover the essential all-point ASD chart.
SCOPE: L071 and audited L093; identical marked K3 factors at fixed h, hypothetical locally free Omega-polystable rank-two F with c_1=0 and ch_2=-14e_1-21e_2-tau_D, one split charge-fourteen fibre L plus L^{-1}, c_1(L)=k. One attempt may test necessary second-order compatibility of its actual smooth connection family and harmonic quaternionic tangent. No F, immersion, generic stability, smooth target quotient or exact quadratic normal form is assumed.

Essential inputs are L071's actual conditional connection and exact-h
line classification, audited L093's equality limitation, and the
preceding line-twist and index assessments' preserved stops. No
cross-notebook input is used. The rank-five seed assessments may provide
leads only: different stabilizers, representations and metric hypotheses
must be compared before reuse.

The main gap is algebraic realization of arbitrary primitive rational
Hodge classes, including on arbitrary fourfolds. The intermediate target
is local compatibility of a quaternionic surface germ with this split
fibre. An obstruction could narrow split equality kernels. Compatibility
would leave actual F, all-stable equality kernels, the prescribed full
mixed action, transport and the universal gap unresolved.

## Primary coverage and precise limits

**ASD chart at a reducible point.** Tobias Diez and Gerd Rudolph,
*Normal form of equivariant maps in infinite dimensions*, Annals of
Global Analysis and Geometry **61** (2022), 159--213,
[published Section 5.3/Theorem 5.8](https://link.springer.com/article/10.1007/s10455-021-09777-2#Sec12),
DOI 10.1007/s10455-021-09777-2. Read Definition 5.1, Theorems
4.13/5.3 with their proofs, and the complete ASD specialization through
(5.23). For a principal bundle with compact semisimple group over a
compact oriented Riemannian four-manifold, every ASD point has a
finite-dimensional Kuranishi chart. It uses the compact connection
stabilizer, the first and second ASD-complex cohomologies, a smooth
equivariant obstruction map, and its zero set modulo that stabilizer.
Section 5.3 verifies properness, Coulomb slices, linear target action
and ellipticity; irreducibility and generic metrics are not hypotheses.
Theorem 5.3's proof retains a smooth equivariant slice/tube before
taking the quotient homeomorphism. Thus one need not infer a smooth
lift from a quotient homeomorphism. Its specialization to SU(2) on
the compact K3 at the given metric is covered. The theorem claims
neither a quadratic obstruction map nor a quaternionic normal-form
diffeomorphism. Import it; no reproof is needed.

**Analytic bundle slice and one moment component.** Nicholas Buchdahl
and Georg Schumacher, *Polystable bundles and representations of their
automorphisms*, Complex Manifolds **9** (2022), 78--113,
[published text](https://d-nb.info/1262812674/34), DOI
10.1515/coma-2021-0131. Reuse the rank-five realization assessment's
general coverage; reread Theorem 1, Lemma 2.5, Proposition 2.6 and
(2.4), and Section 5 through Corollary 5.3 with its differentiation
proof. The central bundle is polystable on a fixed compact Kahler
manifold; neither simplicity nor rationality of its Kahler class is
required. For Sobolev p>2 dim_C X, the slice correction has quadratic
size and the harmonic obstruction is analytic and automorphism-equivariant.
Equation (5.1)/Corollary 5.3 give the quadratic moment map for the
unitary determinant-one parallel automorphisms on harmonic (0,1)-forms.
The construction removes gauge directions using the orthogonal
complement of parallel automorphisms, retaining the residual stabilizer.
Apply only after checking the central split metric and determinant.
This is supporting analytic/moment coverage, not a statement that the
actual ASD obstruction map equals this finite-dimensional moment map
to all orders. The next attempt must identify only the necessary
second-order comparison it uses. The rank-five representation and its
chosen direction are outside this application.

**Quaternionic harmonic coefficients versus stable coarse moduli.**
Misha Verbitsky, *Hyperholomorphic bundles*,
[alg-geom/9307008v1, 29 July 1993](https://arxiv.org/pdf/alg-geom/9307008v1#page=12).
Read the Section 4 setup, Theorem 4.1 and proof, and Corollary 4.3
and proof, pp. 12--15. A hyperholomorphic coefficient bundle with a
parallel real structure has harmonic cohomology preserved by the
specified SU(2) operators; in degree one this gives a quaternionic
action. These coefficient statements do not assume simplicity. Their
application to the central adjoint coefficients must retain the
skew-adjoint real structure and trace-free summand. This does not
by itself make a family's derivative quaternionic. That bridge must
use the actual mixed connection curvature and harmonic projection.
Read Section 6--7's hypotheses, pp. 21--24: the coarse deformation
theorems concern stable/simple bundles. They cannot be applied to
the reducible central bundle. Reuse stable-fibre L067 coverage only
as a comparison, not as a theorem at this point.

## Bounded test approved for a separate research invocation

Import the general inputs above. Derive only their specialization:
the determinant-fixed compact stabilizer and its harmonic representation,
the necessary quadratic ASD obstruction, and the tangent comparison for
an actual smooth family of restricted connections. Do not calculate
these during this source review. Check the diagonal sector, both off-diagonal
sectors and all three quaternionic directions at the exact metric.
Any claim of nonzero tangent must be justified for this equality input;
L067's charge-seven immersion is not an input for it.

Continue toward a local obstruction only if this necessary test fails
for every admissible nonzero quaternionic tangent and the actual-family
bridge is established. A compatible tangent is an informative stop for
this first-order/second-order exclusion test, not a constructed germ.
If the bridge fails, record the precise failed hypothesis. A germ with
zero derivative or higher-order leading term is not excluded by testing
only nonzero tangents. Do not assume such a germ is immersed, infer
convergence from a formal tangent, or derive a complete hyperkahler
quotient model from a complex analytic slice.

## Search, duplicate and access record

Queries included “K3 ASD reducible U1 instanton local moduli hyperkahler
quotient line bundles quaternionic submanifold”, “instantons reducible
local Kuranishi model d_A plus obstruction quadratic hyperkahler moment
map K3”, “Verbitsky hyperholomorphic bundles singularities moduli space
local hyperkahler reduction reducible connection K3”, and the exact
Diez--Rudolph title. Scoped comparisons covered the preceding line-twist
and jumping-index assessments, histories 235--236, ATTEMPTS/059--060,
and the ready orthogonal-seed realization assessment. No earlier local
reducible quaternionic-germ test was identified in those records. This
is not a novelty claim or an exhaustive literature census.

Mitsuhiro Itoh, *Gauge fields and quaternion structure*, Kodai Math.
J. **11** (1988), 344--360, DOI 10.2996/kmj/1138038932, and
*Geometry of anti-self-dual connections and Kuranishi map*, J. Math.
Soc. Japan **40** (1988), 9--33, DOI 10.2969/jmsj/04010009, were
located as primary leads. Initial PDF retrieval returned their opening
pages; later required ranges and screenshots repeatedly timed out.
Indexed later-page passages are discovery evidence only. No later
theorem or special low-charge existence claim is imported from them.
Diez--Rudolph supplies the accessible all-point chart, so these access
failures do not block the bounded necessary test. HKLR's full relevant
passage was not retrieved and is not an input. An unrelated arXiv PDF
opened during discovery is excluded from the evidence and was not used.

The pure-dimension-one Arbarello--Sacca theorems remain a scope mismatch,
as recorded in the line-twist assessment. No global IT, index-effectivity
or strict-Euler stop is reopened. Full matching Mathlib coverage for
this reducible germ test: not checked. No new lemma, mathematical
script, local model, germ, kernel or Hodge resolution was produced.
