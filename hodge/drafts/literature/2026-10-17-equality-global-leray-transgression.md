# Equality family — global Leray transgression source assessment

TARGET: Determine the actual Leray transgression H^0(B,W)->H^2(B,M) and test whether it strengthens |Z|<=800.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact/global transgression, hypercohomology/truncation, coherent Leray and Serre-duality searches completed; compared L108/L109/L111/L115 and ATTEMPTS/047/067. Queries and inspected primary passages are recorded below; no matching family-specific theorem was identified.
SOURCE_EVIDENCE: Inspected live Stacks 20.13.1--4 (01EY), 13.21.3 (015J), 13.22.2 (015N), 13.12.4 (08J5), 12.24.2--4 and preceding differential formulas (012K), 12.25.1--3 (012X), 48.3.6 (0A9Q), 48.12.6 (0G81), 48.15.7 (0BRT), and 48.27.1--4,6 (0FVU/0FVV); reuse the saved local-duality assessment for finite-length duality and L109's actual trace adjoint.
COMPARISON: Known Leray, canonical truncation and derived Serre duality cover the required framework and natural-map comparisons, including non-locally-free W. They supply no stated value of this family's global differential or cardinality improvement; L109's stalkwise gamma is a different map. The actual specialization remains a separate mathematical task, with no originality claim.
GAP: Identify d_2 through the actual truncation triangle, compare its adjoint using the specified trace form, and test the resulting full cohomology constraints against L115; no differential value, section count, new bound or contradiction is established by this review.
REASON: Essential source coverage is now sufficient for the unchanged saved target; approve one separate mathematical specialization, with no additional literature required unless a new hypothesis or essential comparison appears.
SCOPE: Hypothetical equality F of L108/L111/L114/L115, full negative tensor, original metrics, p:S_1 x B->B, V=End_0(F), C=Rp_*V, M=R^1p_*V=E and finite-length W=R^2p_*V; Z finite and possibly empty. No acyclicity, strict stability of N, prescribed section multiplicity, global derived splitting or transgression value is included as an assumption.

## Relevance and bounded test

The main gap is algebraic realization of every primitive rational Hodge
class, already unresolved on arbitrary fourfolds. This intermediate
question concerns only the hypothetical equality kernel. A genuine
additional necessary condition could narrow its allowed split locus;
a compatibility result would park this global cohomological mechanism.
Independent kernel existence, reconstruction, transverse transport and
universal realization gaps remain.

The approved test is to identify the actual global differential and its
natural duality constraints, then determine whether they exclude any
part of the presently allowed 0<=|Z|<=800. If all values remain compatible,
record that limitation and stop this bounded mechanism. A dimension
match, static normal-bundle index or arbitrary self-dual model is not
an identification of an actual map. This review performs no such test.

## Primary statements and applicability

All sources below are the live primary Stacks HTML versions inspected
on 2026-10-17; stable tags identify the passages. General theorems are
imported, not reproved. The permitted specialization is needed because
the sources do not evaluate this particular conditional relative-Ext
complex or its global boundary.

**Coherent Leray.** [20.13.1--4, 01EY](https://stacks.math.columbia.edu/tag/01EY)
identify derived global sections after derived pushforward and give
E_2^{a,b}=H^a(Y,R^bf_*K) converging to H^{a+b}(X,K) for a morphism of
ringed spaces and bounded-below coefficient complex. Read the injective
resolution explanation and acyclicity proof, as well as the theorem.
Here the algebraic structure sheaves and V in degree zero meet these
hypotheses. This is coherent sheaf cohomology, not the etale or singular
Leray spectral sequence. Smooth properness does not by itself authorize
coherent E_2 degeneration with these coefficients.

**Construction and the actual boundary.**
[13.22.2, 015N](https://stacks.math.columbia.edu/tag/015N)
constructs the Grothendieck spectral sequence using a Cartan--Eilenberg
resolution and gives differential bidegree (r,1-r). Its proof refers to
[13.21.3, 015J](https://stacks.math.columbia.edu/tag/015J), whose full
second-spectral-sequence computation, including its sign, was read.
The acyclicity assumptions for this use are checked in 01EY.
[13.12.4, 08J5](https://stacks.math.columbia.edu/tag/08J5)
constructs canonical truncation triangles using a short exact sequence
and a quasi-isomorphism; the whole construction was inspected. Apply
this to the actual bounded C, retaining its natural arrows. Comparing
the resulting global boundary with d_2 is authorized work for the next
turn, not a result of this assessment.

[12.24.2--4, 012K](https://stacks.math.columbia.edu/tag/012K)
and the immediately preceding formulas specify differentials by lifting
a representative in the filtered complex and applying its differential;
they give functoriality and the first-boundary comparison. Read those
formulas and proofs. [12.25.1--3, 012X](https://stacks.math.columbia.edu/tag/012X)
specify both double-complex filtrations, their signs, E_2 pages and
finite-diagonal convergence criterion. Together with 015J these permit
a chain-level check if the truncation comparison needs one. No reproof
of the general spectral-sequence theorem is needed. In particular,
selecting a convenient split complex without proving compatibility
with C would not compute the desired map.

**Derived relative duality.**
[48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT)
identifies the right-adjoint value on O for a smooth proper relative
d-dimensional morphism over a Noetherian base with omega[d]. Read its
statement and diagonal/Koszul proof. The projection here has relative
dimension two and the chosen fibre form trivializes its relative
canonical line. [48.12.6, 0G81](https://stacks.math.columbia.edu/tag/0G81)
pushes a perfect coefficient pairing to the derived cup/trace adjoint;
read its pseudo-coherence hypotheses and explanation of the actual
cup-product map. [48.3.6, 0A9Q](https://stacks.math.columbia.edu/tag/0A9Q)
was also inspected with its projection-formula proof and DQ qualification.
L108 supplies perfectness of C and V is locally free; the trace pairing
on End_0 of a rank-two bundle in characteristic zero is nondegenerate.
Reuse L109's established normalized adjoint, rather than postulating
another self-duality or a new scalar normalization. Ordinary local
freeness of W is not a hypothesis of derived duality.

**Global Serre comparison.**
[48.27.1(5),(7), 0FVV](https://stacks.math.columbia.edu/tag/0FVV)
gives functorial Ext/cohomology duality on proper schemes over a field,
compatible with shifts and distinguished triangles, and identifies
the dualizing complex in the smooth case. Read the adjunction proof.
[48.27.2--4,6, 0FVU](https://stacks.math.columbia.edu/tag/0FVU)
identify the pairing as evaluation followed by trace, state the finite
bounded-coherent qualification for two-sided perfectness, and give
the perfect-complex cup/evaluation version with its proof. B and X
are smooth projective over C with the specified trivial canonical
forms; M is locally free by L111 and C is perfect by L108. These are
the required scopes. The finite-length duality in the unchanged
[local assessment](2026-10-15-equality-local-duality-defect-sequence.md)
remains usable. Any resulting adjoint or rank statement for this
family must still be checked from the actual arrows in a research turn.
In particular one must distinguish sheaf Ext from global Ext and
finite-length local dual from vector-space dual.

## Discovery, duplicates and limits

Queries included:
- `site.stacks.math.columbia.edu hypercohomology spectral sequence truncation boundary map cohomology`
- `site.stacks.math.columbia.edu Leray spectral sequence cup product duality proper smooth`
- `site.stacks.math.columbia.edu "truncation" "distinguished triangle" "13.12"`
- `"Leray" "transgression" "Serre duality" vector bundle K3 endomorphism`
- `site.stacks.math.columbia.edu "Duality for proper schemes over fields" "perfect pairing"`
- `site.stacks.math.columbia.edu "spectral sequence" "truncations" "13.22"`
- `site.stacks.math.columbia.edu "dimension of the support" "H^i" "vanishing"`
- `site.stacks.math.columbia.edu "Serre duality" "compatible" "cup" "48.27"`

Searches also returned etale Leray, relative de Rham duality and
Leray--Hirsch results. Their coefficient categories do not supply a
value of this coherent differential. Uninspected general web results,
including secondary Serre-duality summaries, are not evidence.
No absence or novelty claim follows from these searches.

Scoped local comparison used L108's hypotheses/conclusions, L109's
actual dual-truncation construction through its hyper-Ext indexing
check, L111's hypotheses/conclusions and L115's updated bound.
ATTEMPTS/047 concerns another rank-twenty complement and shows why
polystability does not determine section counts. ATTEMPTS/067 preserves
unbounded local duality-only models, which are not the actual global
family. The supplied overview records ATTEMPTS/063/066 and the later
metric-extension repair; this step does not reopen those invalid
metric inferences or repeat the local length test. The global target
retains the actual C, canonical M=E, length-one W and original connection.
No recorded exact global differential computation was found in these
specific inputs. Full matching Mathlib coverage was not checked;
unknown coverage is not evidence of absence.

## Separate continuation

The exact TARGET is now SPECIALIZE. The next turn may construct the
canonical truncation maps for C, identify the global d_2 and compare
its dual using the actual trace adjoint and Serre pairings. It may then
check full Leray/cohomology constraints against L115's bound, without
assuming a section count, acyclicity, strict normal stability or a
global derived splitting. Essential local inputs are L108, L109,
L111 and L115, with L114/L100/L095/L094/L071 retained through them.
The conclusion may be negative compatibility rather than a stronger
bound. New mathematical proofs belong in canonical lemma files in
that later research turn. No lemmas, mathematical scripts or proof
assembly were changed in this literature-only step.
