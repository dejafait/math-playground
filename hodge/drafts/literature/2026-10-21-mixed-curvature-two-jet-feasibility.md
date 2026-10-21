# Mixed curvature — two-jet feasibility source comparison

TARGET: Assess whether L143's exact negative-energy curvature tuple admits a covariant curvature two-jet satisfying quaternionic type, differentiated Bianchi and Ricci commutation on the fixed K3 product.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped duplicate/failure comparison retained L071/L131/L143, ATTEMPTS/083–084 and the earlier prescribed-family-jet assessment; new searches located Janyška's formal curvature spaces and Devchand–Pontecorvo–Spiro's hyperkähler-instanton construction. Exact queries, primary reads and scope differences are recorded below; no theorem settling this precise tuple was identified in those reads.
SOURCE_EVIDENCE: Read Janyška arXiv:math/0304042v1, Proposition 3.3, Definition 4.1, Theorems 4.6–4.7 and Example 4.9, PDF pp. 6–8; arXiv:math/0405488v1, section 3 (3.5)–(3.6), formal curvature map and complete Lemma 3.1 statement/proof, PDF pp. 8–9. Read Devchand–Pontecorvo–Spiro arXiv:1812.06498v1, Theorem 5.1 and its proof including Lemma 5.2, PDF pp. 25–28, and section 5.3 (5.19), p. 30; compact/complex conventions in section 3 opening, p. 11.
COMPARISON: Known Bianchi/Ricci identities specify a finite necessary test retaining both bundle and base curvature. Unrestricted linear-connection finite-jet surjectivity and prepotential existence do not supply the prescribed real quaternionic tuple. The remaining work is a specialization and feasibility calculation, not a reproof of those general results.
GAP: Determine consistency for L143's fixed tuple with both actual hyperkähler curvature blocks kept symbolic; obtain a uniform answer or an explicit residual condition and identify unavailable actual data. No consistency, obstruction, SU(2)-jet sufficiency or local/global connection realization is proved in this review.
REASON: Essential identity and finite-order coverage is now adequate for one separate bounded necessary-compatibility attempt classified REPRODUCTION. Keep the saved target unchanged; approve no higher-order prolongation, prepotential interpolation or favorable-sign conclusion.
LITERATURE_REASON: The supplied gate required this review because formal compatibility and evaluability were unassessed. The earlier Weitzenböck and variational assessments cover different equations and do not replace it.
SCOPE: The exact TARGET only, with L143's (r,s)=(2,1) tuple, actual product Levi-Civita connection and hypothetical L071/L131 equality kernel; formal necessary curvature derivatives through order two only. Symbolic parameter dependence is permitted; arbitrary choices of base curvature are not assignments to actual K3 points.

## Relevance, inputs and stop test

The main gap is universal primitive rational Hodge realization. The
intermediate target is the differential consistency of one particular
pointwise witness against a proposed mixed-curvature obstruction. A
failure could expose an additional necessary constraint; compatibility
could delimit this finite differential mechanism. Neither supplies a
cycle or excludes the global equality kernel.

Essential inputs are L071's equality data, L131's actual conditional
SU(2) connection, L143's full conventions and exact tuple, and
ATTEMPTS/083–084. The bundle remains hypothetical: locally free rank two,
Omega-polystable at the identical common K3 metric, integral c_1=0 and
ch_2=-14e_1-21e_2-tau_D. Do not change pure coefficients or the full
tensor, set curvature derivatives to zero, or assume a flat base.

L143 fixes A_0=T_1, A_1=T_2, A_2=A_3=0, p_1=2T_3, q_1=T_3,
with the other pure coefficients zero, in its displayed M_s/T_i frames.
Its energy -32 and mixed norm squared eight are established inputs;
this review does not recompute them. Their pointwise algebraic role
remains valid regardless of the new test's outcome.

Continue for a finite symbolic necessary system whose uniform answer
can be checked. If elimination leaves a condition on unavailable actual
factor curvature values, record that condition and park point evaluation.
An existential answer after allowing arbitrary base curvature is not an
answer at the fixed K3 metric. Do not prolong to uncontrolled higher
jets in this attempt. Even a uniform compatible two-jet is not a local
connection, a global F, or a restoration of the abandoned universal sign.

## Primary statements and applicability

**Bianchi and Ricci identities.** Josef Janyška, *On the curvature of tensor
product connections and covariant differentials*,
[arXiv:math/0304042v1, 3 April 2003](https://arxiv.org/pdf/math/0304042v1),
Proposition 3.3 and Definition 4.1 use a smooth vector-bundle connection
and a torsion-free base connection on tensor bundles. Theorem 4.6 is the
cyclic covariant Bianchi identity. Theorem 4.7 identifies antisymmetrized
second covariant differentiation with induced curvature; Example 4.9
applies it to bundle curvature and retains both endomorphism actions
and both covector-slot base-curvature actions. Its right side has no
base-curvature derivative. These hypotheses apply to the conditional
smooth coefficient connection and product Levi-Civita connection.

The proofs use the tensor-product connection and its explicit curvature
formula; no flat-base or Yang–Mills hypothesis enters. Import these
identities, not a new proof. Source coefficients and derivative-slot
ordering differ from a convention defined by [nabla_i,nabla_j]; the
future calculation must fix that translation explicitly. In particular,
Example 4.9's displayed factor -1/2 belongs to its Alt convention and
must not be inserted unexamined into an unnormalized commutator.
Theorem 4.7's displayed bundle label appears interchanged relative to
Definition 4.1; Proposition 3.3 and the explicit Example 4.9 specify the
intended two connections. No proposed calculation relies on that label.

**Finite formal curvature spaces.** Janyška, *Higher order reduction
theorems for general linear connections*,
[arXiv:math/0405488v1, 26 May 2004](https://arxiv.org/pdf/math/0405488v1),
section 3, equations (3.5)–(3.6), PDF pp. 8–9, defines admissible
curvature derivatives by differentiated Bianchi and derivative
antisymmetrization equations. The order-i formal curvature map uses
an (i-1)-jet of the torsion-free base connection and an (i+1)-jet of
the bundle connection. Lemma 3.1, under s>=r-2, k_1>=k_2-2,
s+1>=k_1, r+1>=k_2, is a surjective-submersion statement with retained
lower jets. Its proof fixes the base-connection jet before the affine
successive lifting argument; it does not replace the base by flat space.

This is general linear connection theory. Its surjectivity is not
imported as SU(2) or quaternionic-instanton sufficiency. We need only
its finite necessary identity framework. The references [4]–[5] behind
the unrestricted surjectivity proof were not independently reopened;
that sufficiency conclusion is unnecessary here. For the present
second-derivative test, Example 4.9 already specifies the entire
commutator right side in terms of the order-zero curvature tensors.
There is no essential unread realization theorem for a necessary test.

**Stronger construction screened.** Chandrashekar Devchand, Massimiliano
Pontecorvo and Andrea Spiro, *Instantons on hyperkähler manifolds*,
[arXiv:1812.06498v1, 16 December 2018](https://arxiv.org/pdf/1812.06498v1),
Theorem 5.1, PDF pp. 25–28: on simply connected open V, a holomorphic
g-valued prepotential on V x SL_2(C) with H_0 A_{--}=-2A_{--}
determines an instanton in an analytic gauge. The proof constructs a
bridge and a second potential, checks descent and both type sectors
using Bianchi and Lemma 5.2. Section 5.3, equation (5.19), expresses
curvature through second derivatives of that second potential.

The opening of section 3 distinguishes complex gauge fields from
complexifications of compact-group fields. Theorem 5.1 does not state
arbitrary real prescribed-curvature interpolation. No prepotential with
the required curvature, jet and compact reduction has been identified.
Therefore it is not a direct realization import for L143, and solving
that different inverse problem is outside this approved finite test.
The journal version is Annali di Matematica Pura ed Applicata 199
(2020), 533–561, DOI 10.1007/s10231-019-00890-5; the repository copy
returned 403, so theorem numbering and actual reads here refer only to
the explicit arXiv v1, not an asserted comparison with the final version.

## Precisely bounded necessary problem for the next attempt

This is a specification to specialize the cited identities next turn,
not a derivation or solution of the specialized equations in this turn.
Write R^0 for L143's complete fixed two-form tuple and reserve R^g for
the base Riemann tensor. Introduce prospective tensors U=nabla_A R and
V=nabla_A^2 R at one point, with all eight real derivative directions.
Use the source's full tensor covariant derivative, including all form
slots. Require:

1. Real su(2) coefficients and antisymmetry in the curvature slots;
   quaternionic invariance in those slots for R^0, U and V under each
   of I,J,K. The underlying type subbundle is parallel; no type
   condition is imposed on a derivative slot merely by naming it a
   curvature slot.
2. Theorem 4.6's cyclic identity for U and its first covariant derivative
   for V, in every index combination, including mixed combinations.
3. Theorem 4.7/Example 4.9's full derivative commutator for V, with the
   coefficient curvature R^0 acting on End(F) and R^g acting on both
   curvature covector slots. No replacement by Ricci contraction alone.

For sign translation the standard reference convention can be fixed as
R^g(u,v)=[nabla^g_u,nabla^g_v]-nabla^g_[u,v] and likewise for the
coefficient connection. The imported tensor-product curvature action is
then the adjoint coefficient action together with the negative actions
on the two covector arguments. The next attempt must implement that
same convention throughout, and compare its contracted equation with
L143 as a check. Covariant derivatives are tensors, not ordinary partial
derivatives in a frame with artificially constant quaternion matrices.

Retain R^g=R^{g_1} direct-sum R^{g_2} with the product mixed terms zero
and both pure tensors satisfying the actual hyperkähler curvature
symmetries. Keep their point values symbolic. Example 4.9 shows where
those values enter; it does not require their derivatives at this order.
This makes a parameter-dependent necessary test available without
inventing numerical K3 data. It does not certify that its elimination
will be independent of those parameters.

A useful output is a uniform compatible choice of prospective U,V, a
uniform inconsistency certificate, or a precise residual base-curvature
condition. Verify every original equation after any reduction, retain
both pure blocks, and distinguish all three kinds of output. A complex
solution alone is insufficient for this real test. Unrestricted jet
surjectivity cannot establish quaternionic or compact realization; even
if the necessary system is consistent, its sufficiency is not claimed.

## Search, duplicates and qualifications

Queries included `linear connection curvature covariant derivatives jets
generalized Bianchi identities reduction theorem Janyska`; `Yang Mills
curvature jet formal integrability Bianchi Ricci commutation prescribed
curvature`; `Janyska reduction theorems general linear connections Ricci
identities curvature formal curvature spaces`; `curvature jets Bianchi
gauge realization theorem`; `hyperkahler instanton prescribed curvature
jet formal integrability Bianchi quaternionic instanton`; `quaternionic
instantons prolongation`; `hyperholomorphic curvature jets`; and `Sp(n)
instanton local curvature existence`. Search results served discovery;
the cited primary theorem and proof ranges, not snippets, support this
assessment. No novelty inference follows from the search.

The scoped comparison found no previous evaluation of L143's tuple
under this system. ATTEMPTS/083 stops a universal algebraic sign;
ATTEMPTS/084 stops specified variational imports. Neither decides this
jet question. The older
[prescribed-family-jet assessment](2026-10-14-split-line-second-jet-hyperholomorphic-compatibility.md)
concerns L105's harmonic family jet and an actual gauge comparison,
not pointwise coefficient-curvature derivatives; reuse its warning
against a flat-source substitution, not its verdict. No sibling notebook
was read or used.

Full matching Mathlib coverage of the prescribed real invariant
curvature-two-jet feasibility statement has not been checked. Supporting
Bianchi or connection APIs would not establish that statement. This
literature-only step changes no lemma, mathematical script, DAG or proof
assembly, and proves no compatibility verdict or Hodge-class algebraicity.
The separate next-turn approval of newly completed coverage remains a
supervisor task; this assessment records source scope, not a performed
mathematical attempt.
