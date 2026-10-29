# Positive-z trace exclusion — critical-audit coverage

TARGET: Critically audit L160's W-retaining degree-one edge and conclusion m_-1*m_1=0 for 0<=z<=119.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused steps 521/523/525 exact-target and terminology searches and their known-tool comparison; newly searched Stacks for regular-local parameters, Koszul resolution, dual Koszul shifts and residue-field Ext; inspected 00NQ and 062F rather than treating search snippets as theorem evidence.
SOURCE_EVIDENCE: Fresh full statements/proofs: Stacks 10.106.3 (00NQ), 15.31.2 (062F), https://stacks.math.columbia.edu/tag/00NQ and https://stacks.math.columbia.edu/tag/062F, accessed 2026-10-24; refreshed 01F2/0A1H/0BRT statements and initial proof passages; reuse complete prior reads and qualifications for 0BDK/0AAB/0B6J/0FP3/0FP6/0H99/0FLN, Verbitsky alg-geom/9307008v1 Section 4 pp. 15–17 and Demailly alg-geom/9410022v3 Section 4.A pp. 27–28.
COMPARISON: Known results cover regular-parameter Koszul resolutions, smooth-proper derived duality, general Leray/base change and the same harmonic coefficient operators without projection IT; none imports L160's positive-z degree-one detection, strictness or multiplicity exclusion. These remain explicit specialization-audit obligations.
GAP: Audit L160's contravariant shifts, dual Koszul differential and sheaf Ext passage, the unknown connecting map, degree-one restriction off Z, both actual strict traces and the quartic contradiction; no mathematical audit verdict is established here.
REASON: Separate comparison finds adequate general source coverage for exactly the saved critical audit under SPECIALIZE; the new residue-field calculation has standard supporting sources and an explicit local proof to audit, with no essential inaccessible theorem identified.
SCOPE: Exactly L160 and its retained conditional hypotheses for 0<=z<=119, with ordinary W and its connecting map retained; audit only, without a new spectrum test, positive IT, kernel construction, lower bound or transport.

The proposed audit uses L160 and its exact direct inputs L071, L147,
L157, L158 and audited L159. L093's untwisted concentration, L153's
same-metric polystability and L156's endpoint bounds are retained
through L157, not new conclusions to derive. Keep the identical marked
K3 factors, common metric and triple, preferred dual HE lines with
k=(-4,-2,1,2), k.h=0, k^2=-14 eta, integral eta=1, and hypothetical
locally free Omega-polystable rank-two F with integral c_1=0 and
ch(F)=2-14e_1-21e_2-tau_D+62P. Allow every 0<=z<=119 and retain
the actual ordinary W as a sum of one residue field at each point of Z.

Reuse the source register in
[the positive-z assessment](2026-10-24-positive-z-opposite-coefficient-trace-obstruction.md)
and [the L159 audit assessment](2026-10-24-dual-coefficient-trace-sign-critical-audit.md).
These analytic/product inputs are reused primary reads, not fresh retrievals here.
The proof of Stacks 0H99 was previously recorded as omitted; no claim
to have inspected it is added. No full matching Mathlib coverage has
been checked and no absence claim is made.

The audit's discriminating checks are the shifts in
P_+=RHom(P_-,O)[-2], the exact sequence with the unknown connecting
map M^vee -> Ext^2(W,O), injectivity and detection on B-Z, and the
actual same-class restriction and harmonic norm comparison for both
projections. It must preserve the top term and may not assume positive
IT or infer strictness from abstract perfection. Check both negative
spaces have the full multiplicities in L157 and that adjacent-target
vanishing and the quartic signs remain independent of z. Pass means
the stated conditional restriction survives with every hypothesis;
failure means a specific mathematical error and its correction or
withdrawal, preserving the attempted proof.

This target is only a critical audit of the completed specialization,
not another spectrum calculation. F existence, other stable summands,
lower control on z, transport and universal primitive Hodge realization
remain unresolved. ATTEMPTS/069,/089,/090 are retained. No
cross-notebook input is proposed. Step 527 completes coverage approval; this
does not reject or reclassify the completed step 526.

## Completed source-scope comparison — step 527

This is LITERATURE / EXPLORATION / REPRODUCTION, actual task type
literature_comparison. The full L160 proof was read to locate its source
uses and changed hypotheses, not to carry out the mathematical audit.
No lemma, mathematical script, argument overview or DAG is changed.
LITERATURE_REASON: The newly proposed positive-z audit requires a
separate scope approval, including the point-supported dual calculation
absent from the old zero-z audit; no repeat discovery of the ready
harmonic machinery is needed.

The main gap is universal primitive rational Hodge realization. The
intermediate target is exactly TARGET above. Its downstream use is to
decide whether the conditional exclusion can serve as an audited
constraint on the actual line spectrum of M with W nonzero. It supplies
no cycle construction and need not resolve the independent gaps above.

**Point term: newly inspected primary support.**
[Stacks Lemma 10.106.3, 00NQ](https://stacks.math.columbia.edu/tag/00NQ)
assumes a regular local ring and minimal generators of its maximal
ideal; they form a regular sequence, with regular successive quotients.
Its proof uses the dimension estimate for the first quotient and the
domain property. L160's stalk at a closed point of the smooth complex
surface is precisely a regular local ring of dimension two; its chosen
regular parameters meet this hypothesis. This concerns the actual
residue-field stalk, not arbitrary point-supported sheaves.

[Stacks Lemma 15.31.2, 062F](https://stacks.math.columbia.edu/tag/062F)
requires successive multiplication to be injective on the successive
module quotients and concludes Koszul regularity. Read the full proof:
the length-one case, the short exact sequence after the first
nonzerodivisor, its cone identification and the induction on length.
With the regular parameters and module R in L160 this is the supporting
resolution theorem. The exact dual differential, its cohomological
placement and passage to sheaf Ext are still checks of L160's explicit
calculation. We neither redo them nor approve their result in this
literature turn. That small coefficient/shift check is justified; a
general reproof of Koszul exactness or duality is unnecessary. No claim
that these two citations alone state the full global exclusion is made.

**Derived comparison scope.** The refreshed statements of
[01F2](https://stacks.math.columbia.edu/tag/01F2),
[0A1H](https://stacks.math.columbia.edu/tag/0A1H) and
[0BRT](https://stacks.math.columbia.edu/tag/0BRT) agree with step 525's
complete-read register. Leray allows bounded-below coefficients;
0A1H assumes finite presentation, a perfect input and a bounded
finitely presented base-flat coefficient with proper support; 0BRT
assumes a smooth proper map of fixed relative dimension over a
Noetherian base. The smooth projective K3 projections, relative
dimension two, and locally free Q_(e,d) retain these hypotheses even
when W is nonzero. Set the separate perfect input in 0A1H to O_X.
These refreshed reads covered the statements and initial proof
passages; the complete proof-case coverage is reused from step 525.
The earlier general trace/counit source scopes also allow derived
objects without IT. The proof of 0H99 remains omitted, not newly read.
None of these results permits deleting W, evaluating delta or asserting
ordinary base change at a jumping point. The audit must instead check
L160's proposed restriction to B-Z and its actual counit comparison.

**Harmonic and multiplicative scope.** Reuse Verbitsky,
*Hyperholomorphic bundles over a hyperkähler manifold*,
[alg-geom/9307008v1](https://arxiv.org/pdf/alg-geom/9307008v1),
29 July 1993, Theorem 4.1/Corollary 4.3 pp. 15–16 and the
Theorem 4.2.A doubled-dual proof p. 17; Demailly,
*L2 vanishing theorems for positive line bundles and adjunction theory*,
[alg-geom/9410022v3](https://arxiv.org/pdf/alg-geom/9410022v3),
28 February 1995, Section 4.A (4.3)–(4.4') pp. 27–28, with the
setup in Section 1.A pp. 4–5. Their inspected operator and integral
cases concern the actual compact hyperkähler manifold and locally
free coefficients; they do not require IT of a projection. The
parallel-real doubled coefficient, actual dual line connections,
common metric and fixed determinant normalization remain mandatory.
Neither theorem itself states L160's two strict signs. Its raw fibre
restrictions, closedness, same-class trace ratios and separate
strictness arguments must pass the later audit. No restriction
harmonicity or real structure on an individual twist may be assumed.

The earlier coefficient-product/Kunneth read register covers the
adjacent targets and polarized determinant identity. L158's global
positive concentration and perfect section pairing start at z=0 and
are excluded as positive-z inputs. L159's audited operator/frame
argument can be checked for reuse, but its z=0 strictness conclusion
is likewise not an imported positive-z theorem. L157 supplies the
retained negative and opposite edges only within its canonical scope.

**Duplicates, failures and decision.** The prior searches found general
machinery without an inspected matching multiplicity theorem; no
novelty claim follows. The fresh searches address only the newly
explicit local calculation. Search-only leads from step 525 remain
unread and unused. ATTEMPTS/069,/089,/090 were checked: the unknown
actual global cup entry and compatible additive/multiplicative
relaxations are still valid obstructions to their respective tests.
They neither imply nor refute the actual restriction/strictness bridge.
The completed L159 audit, history/524, remains scoped to z=0.

Approve exactly one subsequent critical audit under SPECIALIZE. Pass
means all shifted-triangle, point-Ext, actual edge, both strict-sign
and quartic checks pass with W retained; retain or repair only the
stated conditional restriction. A failed bridge requires a specific
canonical correction or withdrawal and preservation of the attempted
proof; an irreparable bridge parks this extension. There is no new
mathematical conclusion here. Mathematical exploration usage remains
zero after step 526; this literature turn spends none. Mathlib matching
coverage is not checked, not absent. No cross-notebook input is used.
