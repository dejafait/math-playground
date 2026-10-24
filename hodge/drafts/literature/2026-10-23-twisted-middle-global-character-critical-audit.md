# Global twisted middle character — critical-audit source coverage

TARGET: Critically audit L147's whole-base endpoint support, local freeness, signed coherent GRR and integral determinant calculation for the twisted equality family.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step 468 exact-target discovery and compared L147 scope against that assessment, the L145/L146 audit records, October 12 line-twist and jumping-cycle assessments, and ATTEMPTS/060. Reopened Stacks 0A1H/0BDK/0BCC/0BCD statements and relevant proofs, plus SGA 6 Expose 0 Section 1; no repeated broad search or novelty inference.
SOURCE_EVIDENCE: Reinspected live Stacks Lemmas 36.30.1 (0A1H), 36.31.3 (0BDK), 15.77.6 (0BCC), 15.77.7 (0BCD), and SGA 6 Expose 0 Section 1 formulas (1.1)-(1.3). Reused inspected Fulton second edition (1998), Theorem 15.2 pp. 286-287 and Example 15.2.8 pp. 291-292, and Huybrechts K3 author draft Chapter 1 pp. 11-15 and Chapter 9 Section 3.1 pp. 175-176, with source qualifications in step 468.
COMPARISON: General theorems cover perfectness, concentration, coherent alternating GRR and Picard injection; L145/L146 supply audited local multiplicities and freeness. L147's whole-base assembly and signs require a separate critical check rather than a second derivation treated as verification.
GAP: No essential source gap remains for the exact critical audit; independent verification of L147 ordinary-sheaf assembly, signs, chamber specialization and integral recovery remains. No image positivity theorem or bound on the split set is covered.
REASON: Separate theorem-scope comparison approves the saved audit under unchanged hypotheses; import the standard results and audit only their family specialization next turn, without rederiving or certifying it in this literature turn.
SCOPE: L147's identical marked K3 factors/common metric, hypothetical locally free Omega-polystable rank-two F with integral c_1=0 and ch_2=-14e_1-21e_2-tau_D, fixed class k and finite possibly empty split set; no positivity or scalar self-duality of the twisted middle image.

The main gap is universal primitive Hodge realization. The intermediate
audit target is the actual whole-base sheaf character in L147. Its
downstream use is reliable bookkeeping for a later separately assessed
geometric constraint. Continue if all ordinary-sheaf bridges and signs
survive; repair and record any substantive failure. Passing supplies
neither a bound on the split set nor existence or nonexistence of F.

Essential local inputs are L044's numerical chamber only, L071's full
character and factor classification, L094's line cohomology, L096's
finite possibly empty set, and the audited stalks L145/L146. Preserve
the distinction between derived dimensions (1,26,1) and ordinary
rank 24 at a split parameter. Check that the stable line twist has
both endpoints zero, the degree-zero ordinary kernel has no supported
torsion, and all closed-point freeness neighborhoods cover B.

Check the coherent identity [Rp_*G]=-[M]+[W], the full rank-two
fourth character, the entire relative Todd exponential, and the
transpose convention in p_*(tau_D k_1)=Dk. Verify that the fixed
chamber has k in ker(A_c), hence Dk=4k, using only the numerical
construction rather than the excluded presentation. Picard injection
and integral torsion-freeness must recover the determinant with the
same sign. The recorded formulas are claims for audit, not new
independent evidence in this assessment.

The October 12 line-twist IT and automatic-index-effectivity stops,
ATTEMPTS/060's strict-Euler boundary and the necessary-jet stop remain
unchanged. No positivity hypothesis for M or nonempty split set may
be added. Full matching Mathlib coverage is not checked. No
cross-notebook input is proposed. The preceding proposal was saved as REVIEW_REQUIRED at invocation start.
The separate source comparison below now approves its exact scope; no
mathematical audit or new derivation has been performed here.


## Completed source comparison — step 470

LITERATURE_REASON: The invocation-start audit target required separate approval of its whole-base scope; reuse adequate prior discovery and theorem coverage rather than open a new research target.

**Perfectness and ordinary sheaves.** Reinspected [Stacks 0A1H](https://stacks.math.columbia.edu/tag/0A1H), statement and its applicable Noetherian proof reduction. Finite presentation, a perfect first factor, and bounded finitely presented base-flat coefficients with proper support are required. The proposed projection and locally free twist fall within that scope with first factor O. This covers perfect derived pushforward and base change, not ordinary middle base change at a jump.

Reinspected [0BDK](https://stacks.math.columbia.edu/tag/0BDK), including removal of the other fibre degrees and passage to fixed-rank open pieces. Its scope is one-degree derived concentration. It cannot certify whole-base concentration when split-fibre endpoints survive. Reinspected [0BCC](https://stacks.math.columbia.edu/tag/0BCC) and [0BCD](https://stacks.math.columbia.edu/tag/0BCD): the former gives the local minimal representative using derived-fibre ranks; the latter spreads a finite representative to a principal neighborhood for a perfect complex. These supply precisely the framework for auditing the claimed degree-zero kernel argument. They do not identify its ordinary cohomology with the central derived fibre. L145/L146 already supply the conditional ordinary split stalks and were separately audited; do not duplicate their proofs here. Whole-base assembly and the closed-point coverage argument remain proof-audit obligations.

**Coherent GRR.** Reopened [Grothendieck, SGA 6, Expose 0, Section 1](https://grothendiecksga.com/read/sga6/fr/0.html), formulas (1.1)-(1.3), online text edition accessed 2026-10-23. The statement concerns a proper morphism of smooth quasi-projective schemes over a field and a coherent coefficient; its K-theory pushforward is the alternating sum of coherent higher images. It also states the relative virtual-tangent formula. This is a primary statement check in a text edition, not a fresh inspection of the general GRR proof. Reuse Fulton Theorem 15.2 and Example 15.2.8 with the second-edition page references and scan-host qualification in `2026-10-22-twisted-middle-global-character.md` and `2026-10-05-six-charge-surface-character-filter.md`. The smooth projective complex schemes meet the theorem's scope; no local freeness of the top higher image is required. The restricted Stacks 02UO formulation alone remains insufficient. Import GRR without reproof. The alternating sign, actual point contribution and full rank-two character still require independent checking; source coverage certifies none of L147's numerical evaluations.

**Surface and integral scope.** Reuse the inspected Huybrechts author draft: Chapter 1 (2.5)-(2.6), Proposition 2.4, pp. 11-13; Chapter 9 Section 3.1, pp. 175-176; Chapter 1 Section 3.2 (3.1), printed p. 15. Exact links and prior inspections are in the global-character assessment. Stability and duality must be applied at the actual real h. The Picard injection and torsion-free integral second cohomology are the correct framework for determinant recovery after a rational calculation; slope zero alone does not identify a determinant. The numerical-chamber assertion is a local input from L044, not an external presentation-existence theorem. Its compatibility with L071's operator and the claimed transpose convention remains for the audit. No new chamber calculation is made here.

**Reuse, limits and decision.** Step 468 already checked exact terminology and stronger coherent-GRR results; its discovery scope has not changed. L147 is the completed specialization to audit, not a missing theorem to rediscover. October 12 line-twist IT and automatic-effectivity assessments and ATTEMPTS/060 remain relevant failures; the newer local stalk information does not supply the missing global positivity hypothesis. L145/L146 audit notices were checked in their canonical files and history/467. No new lemma, calculation, mathematical script, or independent proof audit was undertaken. Full matching Mathlib coverage remains not checked; that is not an absence claim.

Approve SPECIALIZE for exactly TARGET. Continue with one independent mathematical audit using L147, L044 numerical chamber only, L071, L094, L096 and audited L145/L146. Preserve hypothetical F, identical markings/common metric, integral first class, fixed k and possibly empty split locus. Passing supports reliable bookkeeping for a later separately reviewed geometric test; a substantive failure requires a canonical repair and an honest changed verdict. F existence, positivity or polystability of M, any cardinality bound, reconstruction, transport and universal primitive Hodge realization remain unresolved. No cross-notebook result is used. This literature step is EXPLORATION / NOVELTY_UNCHECKED, not verification or mathematical progress beyond the sources checked.
