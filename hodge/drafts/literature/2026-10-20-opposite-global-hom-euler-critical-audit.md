# Whole opposite Hom Euler calculation — separate audit registration

TARGET: Critically audit L136's diagonal trace-line identification and full global Hom Euler-count limit.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared full L136 and the relevant actual two-family comparison in audited L135 with the saved global-Euler and stalk-audit assessments; checked ATTEMPTS/046, 073, 078 and histories/419,421. Targeted Stacks smooth-diagonal/conormal search and primary reads are recorded below; no broad discovery search was repeated.
SOURCE_EVIDENCE: Reused Markman math/0009109v4 Theorem 1, Remark 3(2), proof through (11), Lemma 4 and Section 3; FIM 0904.1301v3 Remark 7.3/Theorem 7.6/Section 8; BW 1309.2264v2 Definitions 3.2–3.8/Proposition 3.10/Lemma 3.11 and saved HRR/spectral-sequence coverage. Read live Stacks 0B91, 0BCC, 0BCD, 00DV, 0FDP, 08S2, 0G81 and 02UO statements and relevant proofs on CHECKED.
COMPARISON: Known tools cover a later audit of top-cokernel base change, diagonal conormal generation, actual two-family reverse-Serre comparison, trace gluing and absolute HRR. Markman's universal diagonal formula does not certify this nonuniversal parameter calculation. No matching count inequality or new theorem is imported.
GAP: Essential theorem coverage is sufficient; a later mathematical audit must verify the actual diagonal and coefficient comparisons and all index terms. This source review supplies no audit verdict, multiplicity or index verification and no upper control on the ordinary middle Euler term.
REASON: Approve the unchanged TARGET for one later RESEARCH / REPRODUCTION critical audit. The supporting theorems are imported; only the actual-family specialization and arithmetic need checking. Keep the exhausted count mechanism parked.
SCOPE: L136 with L071, L118, L121 and audited L135; L120 is retained through L121. Hypothetical locally free Omega-polystable rank-two F on the identical marked K3 product with integral c_1=0 and ch_2=-14e_1-21e_2-tau_D; all opposite fibres stable and natural KS injective; the finite ordered off-diagonal coincidence scheme may be empty.

LITERATURE_REASON: Separate approval is required for the new critical-audit target; inspect the new diagonal conormal case while reusing adequate two-family and global-index coverage.

## Original registration (superseded by the completed scope review below)

The main gap remains universal primitive rational Hodge realization.
This continuation verifies a conditional sheaf/index input and the
exact stopping point of a failed count mechanism. A correct diagonal
identification and index could be reused if a genuinely different
global comparison later supplies new information. Neither a useful
global defect comparison nor an upper middle Euler estimate is known.

The source-scope review should reuse the prior primary coverage wherever
its hypotheses and proof cases match. Check particularly the actual
top-degree base change to the diagonal, the passage from a free diagonal
restriction to I contained in J, the reverse-Hom KS-difference transpose
at equal parameters, the two conormal directions and global trace-line
gluing. For the index, retain the forced fourth character, both parameter
Todd factors, the fibre Todd factor and the full mixed square. Verify
that reverse derived duality and Euler bookkeeping assert no ordinary
middle-sheaf self-duality or sign bound.

After separate approval a later mathematical audit should preserve the
result only if all actual comparisons and index terms survive; repair
any substantive error explicitly or retract the affected conclusion.
Do not use a derived top fibre dimension as a multiplicity, or a model
complex as the actual diagonal sheaf. The script certificate verifies
arithmetic only. Full matching Mathlib coverage remains not checked.

This is a verification continuation, not another attempt at the exhausted
Euler inequality. Preserve ATTEMPTS/078, 046, 073, 061–063 and the parked
order-five evidence. No approval, literature review, new lemma or
mathematical script is supplied by this registration itself.

## Completed source-scope review — step 422, 2026-10-20

This is a literature comparison, not the mathematical audit. The main gap
is universal primitive rational Hodge realization. The intermediate target
is correctness of L136's conditional diagonal sheaf identification and
Euler-count limit. A reliable sheaf/index input could support a later,
materially different global comparison; no useful comparison is known.
F existence and transport remain independent unresolved assumptions.

### Primary hypotheses and essential cases

[Stacks Lemma 36.30.4(1), 0B91](https://stacks.math.columbia.edu/tag/0B91)
requires a proper flat morphism of finite presentation and a perfect
coefficient, and gives perfect pushforward with arbitrary derived base
change. These hypotheses match the product projection and vector Hom
coefficient, including restriction to the diagonal. Its reduction to
36.30.1 is reused with the concrete flat-complex case already inspected
in the stalk-audit assessment (0A1H/0A1D). It gives no ordinary
middle-sheaf base-change assertion.

[Stacks Lemma 15.77.6, 0BCC](https://stacks.math.columbia.edu/tag/0BCC)
requires a pseudo-coherent complex over a local ring. Its representative
has ranks equal to derived residue-field cohomology dimensions; its proof
uses zero residue-field differentials and comparison of free complexes.
[15.77.7, 0BCD](https://stacks.math.columbia.edu/tag/0BCD) spreads the
finite representative for a perfect complex. Both statements and their
proofs were read. The future audit must check the amplitude before using
a last-row cokernel and tensor right-exactness. Neither source makes a
one-dimensional top derived fibre into a reduced diagonal sheaf.

A targeted query, `site:stacks.math.columbia.edu smooth morphism diagonal
regular immersion conormal locally free`, located
[Stacks Lemma 37.62.18, 0FDP](https://stacks.math.columbia.edu/tag/0FDP).
For a finite-type morphism of locally Noetherian schemes, smoothness
implies a regular diagonal immersion. Read its statement and the proof
of this implication using the diagonal as a section of a smooth
projection. It applies to B over C. Also read the statement and proof of
[Lemma 29.33.7, 08S2](https://stacks.math.columbia.edu/tag/08S2): the
conormal sheaf of the diagonal is canonically the differential sheaf.
Its construction uses the difference of the two projection sections and
the affine multiplication-kernel description. These provide standard
coverage for the smooth diagonal's conormal structure; they do not
identify L136's actual last-row ideal with that diagonal ideal.

[Stacks Nakayama Lemma 10.20.1, 00DV](https://stacks.math.columbia.edu/tag/00DV),
parts (6) and (8), applies to a finite module over a local ring and
generation modulo its maximal ideal. Read the determinant proof and
the surjectivity/generator cases. The audit must separately check the
claimed containment I in J from the actual free restriction, the
identification of linear parts with J/mJ, and generation of both normal
directions. The finite ideal module is available in the Noetherian pair
local ring. General Nakayama does not supply those missing comparisons.

For the deformation comparison reuse the precise FIM, BW, connecting-map,
stable-Hom and Serre sources in
`2026-10-20-opposite-hom-stalk-critical-audit.md` and
`2026-10-20-opposite-off-diagonal-relative-hom-stalk.md`.
L135's inspected coefficient-sequence, flat Cech and two-sided Dolbeault
passages do not posit distinct central bundles: the future audit may use
that mechanism at equal parameters with two independently varying
families. It must verify the specialization to the central identity,
the reverse-Serre transpose and the natural KS difference, rather than
import the off-diagonal four-direction rank conclusion. Simplicity and
trace splitting use actual common-H stable fibres, rank two over C,
and the fixed K3 canonical trivialization. Global trace gluing must
still be checked on the actual family.

[Stacks Remark 48.12.6, 0G81](https://stacks.math.columbia.edu/tag/0G81)
assumes a pairing to the relative dualizing complex with invertible
adjoint and pseudo-coherent second coefficient. Read its cup/trace
statement and adjunction proof. Forward/reverse vector Hom coefficients
and the K3 dualizing shift fit this scope. Its conclusion is derived
duality, with no assertion of ordinary middle-sheaf self-duality or
Euler positivity. Reuse the bounded coherent hypercohomology coverage
in 0FLJ from the global-Euler assessment; all terms must be retained.

[Stacks Section 42.66, 02UO](https://stacks.math.columbia.edu/tag/02UO)
states HRR for a finite locally free coefficient on a smooth proper
variety over a field. Read the absolute specialization; its relative
formulation additionally assumes locally free higher images. The
absolute case covers the sixfold coefficient without that assumption.
Reuse Fulton, second edition, Theorem 15.2 and Example 15.2.8 with the
pages recorded in the global-Euler assessment. Reproof is unnecessary.
The later audit must check L071's forced fourth character, the full
mixed square, dual-character signs and all three Todd factors. No
arithmetic was rerun or certified in this literature step.

### Overlap, test and decision

Reuse the saved primary Markman comparison: its universal moduli
rank/codimension and pure-support hypotheses do not match this pair
base. Its stronger diagonal result in its own setting motivates the
mechanism, but does not remove the actual-family specialization. The
unread Mukai Proposition 4.10 lead remains nonessential and unimported.
No novelty is claimed; full matching Mathlib coverage remains not checked.

ATTEMPTS/046 retains the isolated Hom-jump warning; ATTEMPTS/073 supplies
no image-cohomology vanishing; ATTEMPTS/078 parks the whole-complex count
at the unknown ordinary middle Euler term. This audit must not reopen
those inferences. No new lemma, mathematical script, DAG edge or main
argument is written in this turn.

The exact approved action remains: Critically audit L136's diagonal
trace-line identification and full global Hom Euler-count limit.
Continue with its conditional conclusions only if the actual base-change,
conormal, transpose, trace gluing and full index comparisons survive.
Repair or retract any unsupported part; an unevaluated actual comparison
is a stopping condition, not license to substitute a model. A successful
audit need not improve the count bound or establish F. Essential inputs
are L071, L118, L121 (retaining L120) and audited L135; all original F
hypotheses remain conditional, and the off-diagonal locus may be empty.
The next turn defaults to RESEARCH / REPRODUCTION under this SPECIALIZE
assessment, without another literature search on unchanged scope.
