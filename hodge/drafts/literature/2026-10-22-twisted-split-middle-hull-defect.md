# Twisted split middle stalk — proposed source comparison

TARGET: Determine the ordinary middle stalk and whether its canonical map to its reflexive hull is an isomorphism at a selected split equality fibre for Rp_2*(F tensor p_1^*L^{-1}).
CHECKED: 2026-10-22
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched three-term free-complex middle cohomology, Koszul regular sequence, reflexive hull and regular-local-surface module terminology; compared L145, the necessary L111 module argument and the October 12 IT/index stops. No matching family-specific theorem was identified; general primary local-algebra coverage is available.
SOURCE_EVIDENCE: Reuse the completed 2026-10-21 twisted top-stalk assessment for BW fixed-coefficient comparison, perfect/base-change, connecting maps and true dual trace. Inspected live Stacks 0BCC, 00NQ, 062D Lemma 15.31.2, 00NX, 00JJ and 0AV2 statements and relevant proofs on 2026-10-22.
COMPARISON: Known results cover minimal representatives, regular-parameter Koszul syzygies, direct summands, local projective freeness and the canonical reflexivity criterion. They do not identify this actual incoming differential or its position in the last-row kernel; L111 scalar self-duality does not transfer.
GAP: Specialize the actual degree-zero coefficient connecting map to the minimal incoming column, then use the established last-row ideal and the complete chain relation to determine the whole middle quotient and canonical double-dual map. Any needed unit or splitting condition must be proved from actual-family inputs, not assumed.
REASON: The changed middle-module scope now has sufficient source coverage for one bounded known-tool specialization. No middle-module value or new theorem is derived in this review; this can supply local corrections for later global bookkeeping only.
SCOPE: Same hypothetical locally free Omega-polystable rank-two F on identical marked K3 factors with common metric, integral c_1=0 and ch_2=-14e_1-21e_2-tau_D; fixed c_1(L)=k=(-4,-2,1,2) and selected actual split p_2 fibre L plus L^{-1}. No global IT, effectivity, middle freeness, scalar self-duality or nonempty split locus is assumed.

The main gap remains universal primitive rational Hodge realization;
existence of this F is independently unresolved. The proposed
intermediate target concerns one entire ordinary middle stalk, not a
new global exclusion. Its plausible downstream use is to determine
which local corrections would enter a later global comparison. A
metric extension, positivity theorem and useful global inequality would
remain separate even if the local calculation succeeds.

Essential inputs for the proposed review are L145's audited actual
minimal complex and last-row ideal, L071's exact kernel/line data,
L094/L095's actual KS identification and L134's two weight ranks.
L111 is a comparison only: inspect only the necessary module argument
and cited theorem hypotheses when assessing applicability. Its adjoint
self-pairing is not a mathematical input for this twist. The correct
dual coefficient remains F^vee tensor p_1^*L, not G itself.

Reuse the existing top-stalk literature while checking the changed
middle-module scope. Search exact middle-cohomology, local perfect
complex, reflexive-hull defect and relevant stronger statements before
approving a calculation. The continuation test is whether available
results and these actual differentials determine the whole stalk and
whether the canonical hull map is an isomorphism. If a missing higher
coefficient or pairing is essential, identify it and retain a qualified
or negative result rather than assuming freeness. A countermodel must
respect all established actual-family constraints, not only fibre ranks.
No middle-stalk result, expected rank or defect value is derived here.

The October 12 IT and automatic index-effectivity stops, ATTEMPTS/060's
untwisted strict-Euler exclusion and the necessary two-jet stop remain
unchanged. This proposal addresses the missing actual middle-sheaf
input; it does not repeat an IT argument or assign positivity to a
virtual index. F, a selected split point, global realization,
reconstruction, transport and the universal target remain unresolved.
Full matching Mathlib coverage is not checked. No cross-notebook input
is proposed. Approval must occur in a separate turn.

LITERATURE_REASON: The prior ready top-stalk assessment expressly excluded the changed middle-module scope; essential regular-sequence, module-splitting and canonical-reflexivity coverage had to be compared before research.

## Completed source comparison — step 464, 2026-10-22

The proposal above records the starting missing-coverage gate. This
completion supersedes that gate only: SPECIALIZE approves a subsequent
attempt on the unchanged TARGET, subject to separate supervisor approval.
It does not assert middle freeness, a rank, a hull-defect value or a
normal form for the actual complex. No lemma or mathematical script was
written in this literature-only step.

### Reused coefficient coverage and overlap

Reuse `2026-10-21-twisted-split-top-stalk-length.md`, especially its
completed BW arbitrary-bundle comparison and derived-presentation/duality
sections. Budur–Wang, *Cohomology jump loci of differential graded Lie
algebras*, Compositio Math. 151 (2015), 1499–1528, DOI
10.1112/S0010437X14007970, arXiv:1309.2264v2, Definitions 3.2/3.8,
Proposition 3.10, Lemma 3.11, Theorem 6.4 proof (9)–(10) and Remark 6.5
cover the actual fixed-tensor Dolbeault-module comparison. That coverage
is unchanged: the same compact K3, actual locally free coefficient and
fixed line twist are used. No new formality or zero-Chern hypothesis is
imported. The earlier assessment's Stacks 0A1H/0117 and exact GAGA
comparison apply to both connecting degrees of the same coefficient
sequence; establishing the degree-zero comparison explicitly remains a
proof obligation, rather than a result of this review. Its actual dual
remains F^vee tensor p_1^*L.

Read L145's actual coefficient sequence, minimal presentation and top-row
rank/ideal argument; read only L111's imported-tools and actual-middle
module passages for comparison. L145 retains the full two differentials
and proves the last-row ideal, but does not compute their middle quotient.
L111 uses a nondegenerate alternating scalar middle form and its
orthogonal splitting for End_0(F). That mechanism is not available by
citation for this defining coefficient. Its conclusion is not a duplicate
of the new target. A calculation using only the row and derived fibre
ranks would leave the incoming map unexamined.

The October 12 line-twist and jumping-index assessments preserve the
IT and automatic-effectivity stops. ATTEMPTS/060 preserves the strict
untwisted Euler stop and leaves equality open. The present test seeks an
actual local module, not a new IT or effectivity inference. Necessary
jet compatibility remains separate. No other notebook was read.

### Primary local algebra inspected

All following Stacks statements and the proof cases described were read
in their live versions on 2026-10-22; tags are stable citation identifiers.

- [Lemma 15.77.6, 0BCC](https://stacks.math.columbia.edu/tag/0BCC)
  constructs a representative of a pseudo-coherent object over a local
  ring whose term ranks are its derived residue-field cohomology
  dimensions. Its proof lifts a zero-differential residue complex and
  uses reduction of a chain isomorphism to obtain uniqueness. Apply to
  the already perfect actual pushforward; this does not assert ordinary
  middle base change.
- [Lemma 10.106.3, 00NQ](https://stacks.math.columbia.edu/tag/00NQ)
  makes minimal maximal-ideal generators of a regular local ring a
  regular sequence. Its proof passes to successive regular local
  quotients and uses the domain property for the first nonzerodivisor.
  The base here is a smooth K3 surface, hence its stalk is regular local
  of dimension two. This applies to actual minimal generators, not to
  arbitrary two entries without a generation check.
- [Lemma 15.31.2 in 062D](https://stacks.math.columbia.edu/tag/062D)
  gives positive-degree Koszul exactness when each successive element
  acts injectively on the previous quotient of the module. The proof
  uses the multiplication cone and induction. With the ring as module,
  a verified regular parameter pair meets these hypotheses. Applying
  its syzygy information to the actual two maps, including all higher
  coefficients and the relation d^1 d^0=0, remains the specialization.
- [Lemma 10.78.2, 00NX](https://stacks.math.columbia.edu/tag/00NX)
  identifies finite projective modules with direct summands of finite
  free modules. Its splitting proof in both directions was inspected.
  [Lemma 10.55.8, 00JJ](https://stacks.math.columbia.edu/tag/00JJ)
  proves finite projective modules over a local ring are free using
  a residue-basis lift, a splitting and Nakayama. These apply if an
  actual finite direct-summand description is established; neither
  source supplies that description for this middle quotient.
- [Lemma 15.24.6, 0AV2](https://stacks.math.columbia.edu/tag/0AV2)
  characterizes a finite reflexive module over a Noetherian domain by
  a free-module embedding with torsion-free cokernel. The proof uses
  double duality of a presentation and notes finite free modules are
  reflexive. The base satisfies the domain hypothesis. Merely embedding
  a module in a free module is insufficient: its cokernel condition
  must be checked. This theorem concerns the canonical double-dual
  map, not an arbitrary isomorphism with a free hull.

No standard theorem is to be reproved. The needed additional work is
the family-specific identification and module computation under these
hypotheses. Full matching Mathlib coverage has not been checked;
unknown coverage is not absence.

### Discovery limits and bounded continuation

Queries used: “site.stacks.math.columbia.edu regular local ring dimension
2 reflexive module free double dual torsion free”; “cohomology three term
free complex middle cohomology Koszul regular sequence minimal
differentials reflexive hull”; “site.stacks.math.columbia.edu finite
projective module local ring free direct summand”; and
“site.stacks.math.columbia.edu reflexive module regular local dimension
at most two free”. These identified the primary general results above.
Search-returned MathOverflow discussions, secondary encyclopedias and
unrelated syzygy papers were not used as theorem evidence. No exhaustive
absence or originality claim follows from this bounded discovery.

The approved attempt must compare the actual degree-zero boundary on
the central section with the incoming minimal column, using the same
coefficient-sequence naturality already assessed. It must then compute
its position inside the entire kernel of the established last row.
Test whether regular-sequence syzygies and actual first variation suffice
to split the relevant quotient over the original local ring; verify any
required residue minor or unit rather than infer it from KS injectivity
alone. Retain all higher coefficients. If that test fails, isolate the
specific missing coefficient, rank or pairing and do not assume a
scalar self-duality or middle base change. A countermodel must respect
the actual incoming first variation and every established family relation.

Continue on this exact target only after separate approval next turn.
The target is independently useful even if it produces a qualified or
negative answer: it can determine the local terms still missing from
later twisted-cohomology bookkeeping. F existence, a selected split
point, global positivity, a useful defect inequality, reconstruction,
transport and universal primitive Hodge realization remain unresolved.
This review establishes source readiness, not progress beyond the
inspected known mathematics.
