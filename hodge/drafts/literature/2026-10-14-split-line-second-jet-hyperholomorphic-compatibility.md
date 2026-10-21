# Prescribed second jet — product hyperholomorphic compatibility

TARGET: Test whether L105's prescribed harmonic second jet is compatible with a smooth product hyperholomorphic connection germ.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: New targeted searches for product hyperholomorphic curvature, reducible universal connections, quaternionic maps and second derivatives; compared L094/L095/L101/L105, ATTEMPTS/061, history/286 and the existing split-slice, raw-harmonicity, integration and cubic-audit assessments. No inspected theorem settles this prescribed second jet; no novelty inference is made.
SOURCE_EVIDENCE: Fresh primary reads: Li 1908.05017v1 Section 2.2, Section 2.3 (3)/(4), Lemma 2.12/Proposition 2.13/Theorem 2.14 and Section 3.2 Remark 12, complete Lemmas 3.5/3.6 proofs and following qualifications, PDF pp. 5--8,11--13; Buchdahl--Schumacher (2022) Section 1/(1.1), Lemma 2.5 and its implicit-function construction, Proposition 2.6 setup, complete Proposition 4.5 proof and Corollary 4.6's actual-isomorphism argument, printed pp. 80--84,88--89. Reuse the previously inspected remaining slice proof cases, Diez--Rudolph Theorems 5.3/5.8 and Meazzini--Onorati 2204.04075v2 connection-functor comparison, as specified below.
COMPARISON: Primary curvature identities and fixed-central gauge fixing cover the tools for a finite second-order necessary test without a smooth moduli point. They do not provide this jet's verdict, a smooth central HE gauge for L105, or product integration. L095's global norm formula is outside the local hypotheses.
GAP: Specialize the full curvature and Bianchi equations through the order determining the second harmonic jet; compare with the actual complex slice while retaining horizontal coefficients, the residual stabilizer and source Levi-Civita terms. This calculation and gauge comparison remain unproved, rather than missing imported existence theorems.
REASON: Approve one separate bounded RESEARCH attempt classified REPRODUCTION using known coefficient and slice tools. No essential source-access gap remains for this necessary test; neither an exact quaternionic normal form nor a universal connection through the reducible point is required or approved.
LITERATURE_REASON: The saved target adds real product-connection and second-jet hypotheses absent from the complex audit; its required source comparison was explicitly REVIEW_REQUIRED. Existing formality and approximation coverage is reused rather than searched again.
SCOPE: Fixed S,I,g,h,k,E,A and ell from L094/L101/L105; prescribed harmonic jet alpha=ell+s^2u+O((s,t)^3), with u in L105's annihilator K outside span(a_1,a_2). A hyperkahler source surface germ may vary, with I-holomorphic coordinates s,t and the same normalized quaternionic tangent identification at zero.

## Bounded target approved for a separate mathematical turn

Ask whether that two-jet can be the fixed complex harmonic slice jet of
an I-holomorphic family induced by a smooth determinant-one unitary
connection on S times a hyperkahler surface germ, whose curvature is
of type (1,1) for every simultaneous induced complex structure. Its
central fibre connection must be A. Allow horizontal connection
components and determinant-one complex gauges with the prescribed
central marking. Do not identify a holomorphic slice representative
with a unitary ASD representative or assume smooth central HE gauges.
The source metric is not assumed flat; its tangent normalization is
fixed. The test concerns existence of compatible second-order data for
some admissible u, not convergence or full product-kernel existence.

The main gap remains universal primitive rational Hodge realization.
The intermediate question tests whether the audited degree-one complex
construction can be a local prerequisite for the separate quaternionic
route. A rigorous obstruction would stop that particular prescribed-jet
recipe; compatible data would justify one later integration question,
without establishing it. This would be a different test from
ATTEMPTS/061's already compatible quadratic ASD obstruction.

Step 287 completes source comparison only. No assertion of compatibility
or incompatibility is made, and no second-order coefficient equation has
been solved. The narrower necessary test can be conducted directly on a
hypothetical smooth product connection; an existence theorem for that
connection is neither available here nor needed for this test.

Continuation test: proceed to the bounded mathematical test only when
complete second-order equations and their actual slice/gauge comparison
are covered. A genuine incompatible coefficient stops this prescribed
jet; compatibility alone permits no existence claim. Persistent essential
source blockage requires an independently testable target, rather than
repeated access retries.

Essential existing inputs: audited L094 and L101–L105. L095's audited
local coefficient argument is supporting coverage only, with the scope
restriction below. No global F, nonempty global split locus,
W=r(TB), prescribed global mixed action, coarse comparison, global
separation, reconstruction, transport or new Hodge class is assumed.
Matching Mathlib coverage is not checked; unknown availability is not
absence. This approves a test, not a mathematical conclusion.

## Primary hypotheses, proof cases and applicability

**Product curvature, including the reducible opposite family.** Yang Li,
*Mukai duality on K3 surfaces from the differential geometric perspective*,
[1908.05017v1, 14 August 2019](https://arxiv.org/pdf/1908.05017v1),
Section 2.2, Section 2.3 and Section 3.2, PDF pp. 5--8,11--13.
Read the affine quaternionic action, curvature-block calculation and
all three block cases of Proposition 2.13's proof. Section 3.2's
Remark 12 and the qualifications after Lemma 3.6 separate opposite-fibre
irreducibility from the mixed-curvature argument. Lemma 3.5's complete
proof uses total and fibre Yang--Mills equations to obtain Coulomb
harmonicity; Lemma 3.6 uses simultaneous curvature type to identify
quaternionic variation. These are local coefficient tools for an already
smooth connection, not a construction of such a connection at our A.

The same paper's universal-connection construction is substantially
narrower: its original moduli K3 is compact, nonempty and irreducible,
with isotropic Mukai vector. Formula (3), Lemma 2.12 and (4) use an
inverse scalar Laplacian on irreducible projective connections.
Theorem 2.14 additionally handles the determinant curvature. Do not
extend that inverse through A's circle stabilizer, or import a smooth
universal connection for the present germ. Li's dual-transpose convention
must also be translated to our fixed E convention.

Reuse [the L095 audit coverage](2026-10-12-split-equality-raw-harmonicity-critical-audit.md)
for coefficient Bianchi and the adjoint identities. The local test keeps
the defining condition R(Qv,Qw)=R(v,w), for Q=I,J,K, on the entire
product curvature, together with the connection Bianchi identity.
Both pure blocks and the mixed block must be retained. This is the
known curvature/type system to specialize; no differentiated consequence
for L105's jet is asserted here. Since the source is hyperkähler,
its own parallel quaternionic triple and Levi-Civita connection enter
covariant differentiation. Its curvature and coordinate Christoffel
terms are not set to zero by assuming a flat source.

L095 assumes a global F with a specified full ch_2 and identical K3
metrics. Those hypotheses fail for an unspecified source germ. Its
global pairing 2lambda g therefore cannot be cited here. Its local
coefficient reasoning, already audited without irreducibility, can be
specialized only after checking the actual smooth germ hypotheses.
L105's prescribed differential itself fixes the tangent scale.

**Actual complex slice and allowed gauge comparison.** Nicholas
Buchdahl and Georg Schumacher, *Polystable bundles and representations
of their automorphisms*, Complex Manifolds 9 (2022), 78--113,
DOI 10.1515/coma-2021-0131,
[published primary text](https://d-nb.info/1262812674/34).
Read Section 1's Hermitian/semiconnection conventions and curvature
formula, Lemma 2.5's full fixed-central implicit-function construction,
Proposition 2.6's setup, and the complete Proposition 4.5 and relevant
Corollary 4.6 proof cases. Reuse the remaining analytic correction and
equivariance coverage from
[the L105 audit assessment](2026-10-14-split-line-cubic-invariant-critical-audit.md).

The fixed compact Kähler metric and its central HE connection are the
data; Sobolev exponent p>4 suffices on S. Lemma 2.5 restricts the gauge
variable to the orthogonal complement of ker bar-partial_A before
inverting the central Laplacian. It does not assume that kernel is zero.
Its Banach implicit-function construction is the appropriate source
for dependence on a smooth input family. Proposition 2.6 gives the
actual harmonic coordinates and coexact correction. Corollary 4.6's
proof compares isomorphic small slice operators using actual Hom
sections and the central parallel automorphism group; its quotient
homeomorphism alone is not a smooth family lift.

E is already split HE at the fixed real h, not merely semistable, so
these central assumptions apply. Determinant restriction and the actual
harmonic contraction are already justified in L101/L105. The future
test must explicitly expand the smooth gauge comparison through the
required order. It must distinguish the semiconnection transformation
from the paper's extension to Hermitian connections: conjugating a full
unitary connection by an arbitrary complex gauge does not preserve
its fixed Hermitian curvature equations. Residual determinant-one
parallel scalars and parameter-dependent gauges preserving the central
marking remain allowed; second jets are not automatically invariant.
No smooth choice of HE metrics for the given L105 complex family is
being constructed or assumed. Under the hypothetical product connection
one starts with its own smooth unitary representatives instead.

For real unitary slices, reuse the fully inspected
[split-local-slice assessment](2026-10-12-equality-split-local-slice.md):
Diez--Rudolph, *Normal form of equivariant maps in infinite dimensions*,
Ann. Global Anal. Geom. 61 (2022), 159--213,
[Theorems 5.3/5.8 and Section 5.3 (5.14)--(5.23)](https://link.springer.com/article/10.1007/s10455-021-09777-2#Sec12).
Compact semisimple SU(2) on the compact oriented four-manifold S meets
the hypotheses even at a reducible connection. Only the actual slice
and stabilizer treatment are available, not an exact quaternionic
quadratic chart. No reproof of either slice theorem is needed.

**Stronger results and limits of formality/geodesy.** Reuse
[the completed analytic-integration comparison](2026-10-14-equality-split-line-analytic-integration.md),
including Meazzini--Onorati, Math. Z. 303 (2023), article 17,
[2204.04075v2](https://arxiv.org/pdf/2204.04075v2), Definition 2.8,
Theorem 4.3, Definition 5.1, Theorem 5.8 and Corollary 5.9, and its
inspected 2025 follow-up. Holomorphic formality and infinitesimal
complex autodual deformation results do not identify real smooth
product-connection jets. The unversioned arXiv PDF was located during
this search, but the exact v2 comparison above is reused; it was not
newly audited in full. No further formality derivation is authorized.

The stable-moduli geodesy results used in L100 also do not apply at A.
The primary statement of Verbitsky,
[alg-geom/9610010v1, Definition 5.3/Corollary 5.4, PDF p. 30](https://arxiv.org/pdf/alg-geom/9610010v1#page=30),
requires a hyperkähler embedding. No smooth target at the split class
is provided. Quaternionic-map/Obata searches produced leads but no
inspected theorem resolving the marked second-jet/gauge problem.
Those leads are not mathematical inputs. The bounded connection-level
test must supply its own specialized tensor comparison, without
declaring a map into the affine connection space quaternionic merely
from a quotient statement.

## Search record, approved specialization and stopping test

Queries included `hyperholomorphic connections product quaternionic maps
universal connection reducible connections second fundamental form`,
`hyperholomorphic universal connection reducible gauge moduli product
quaternionic maps second derivatives`, and `triholomorphic maps
hyperkahler totally geodesic Obata connection proposition`. Primary
source retrieval, not snippets or secondary summaries, supports the
comparison. Access to the essential Li and Buchdahl--Schumacher cases
succeeded. No cross-notebook theorem was read.

ATTEMPTS/061 remains the stop for the already compatible quadratic ASD
obstruction on W. L101--L105 already establish complex realization and
degree information; repeating them would not answer this target.
The new discriminating test uses the next harmonic jet and the full
product curvature, including horizontal directions. The known sources
cover these tools but do not state the resulting prescribed-jet answer.
Only that specialization is justified; reproduction does not mean the
sources certify its outcome or that originality has been established.

The next mathematical attempt should start from the complete known
curvature/type and Bianchi system, keep horizontal connection terms,
and compare its second-order necessary data with L105's actual slice
using the fixed-central gauges above. Retain all admissible u, source
metric freedom, smooth marked determinant-one complex gauge freedom
and the central stabilizer. If a proposed normal harmonic coefficient
is used, prove that it is unchanged by the allowed freedoms; do not
silently assume that raw second derivatives are intrinsic. These are
the specialized calculation obligations, not results derived here.

A genuine unavoidable incompatible coefficient stops this prescribed
second-jet recipe. A missing gauge bridge must be reported as unresolved,
not as an obstruction. Compatibility of the necessary equations alone
does not construct a second-order solution unless all those equations
are satisfied, and even full second-order compatibility proves no
integrated germ. No conclusion about other jets, global F, global mixed
action, coarse comparison, separation, reconstruction, transport or
primitive Hodge realization follows. No lemma, script, DAG or PROOF
change is made in this literature-only step.
