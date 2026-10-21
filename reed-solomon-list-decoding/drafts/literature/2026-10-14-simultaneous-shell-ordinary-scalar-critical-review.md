# Scalar-plus-PSD critical review — source scope approved

TARGET: Critically audit L062's represented ordinary scalar rows, source normalization and reuse of L061's identical complete PSD witness.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the inspected discovery/theorem comparison in drafts/literature/2026-10-14-simultaneous-shell-ordinary-scalars.md and the L061 critical-audit assessment; read canonical foundations/04,09,10,12, L062, L061's imports and completed audit, ATTEMPTS/015,043's recorded scope in the L061 assessment, ATTEMPTS/044 and histories/206,207. No new web search or finite calculation was needed for this unchanged source scope.
SOURCE_EVIDENCE: Schrijver https://homepages.cwi.nl/~lex/files/codes.pdf DOI 10.1109/TIT.2005.851748, III.B (62)–(65) and explanation after (65), p. 7, plus (7), Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), pp. 2,5–7; Kim–Toan https://arxiv.org/pdf/1212.3467v1 III.A Remark 11 and III.B (31)–(35), pp. 8–9; Polak https://arxiv.org/pdf/1703.05171v1 Section 1.1 (1)–(3), Proposition 1.1 and indicator proof, p. 2; Sano https://link.springer.com/article/10.1007/s44146-026-00231-y Section 2 Theorems 2.1,2.6 and Corollary 2.2. Reuse prior primary passage/proof inspections recorded in foundations/04,09,10,12 and the ready assessments; no fresh retrieval is claimed.
COMPARISON: The scalar theorem covers actual nonzero orbits, all source permutations preserving t-s, repeated words and forbidden nonzero distances; mixed-layer algebra and the singular-block criterion cover the retained complete matrix. None certifies L062's finite normalization, orbit closure, scalar extrema or same-assignment claim. L023's different full scalar prescription and L061's PSD-only audit do not duplicate this strengthened manuscript review.
GAP: Independently critically verify the finite application and complete relevant evidence for all 121 represented types, 726 presentations, 2178 scalar rows, pairs through p_12, Boolean/forbidden cases and the identical 49-mode PSD witness; arithmetic reports alone do not constitute that audit.
REASON: Step 208 completes separate source/scope approval of the continuation first proposed during step 207; all essential theorem coverage is reusable, and no mathematical audit is claimed this turn.
LITERATURE_REASON: The supervisor requires separate approval for L062's newly proposed critical review; this turn compares its exact strengthened manuscript obligations with already inspected sources, rather than repeats source browsing or feasibility calculation.
SCOPE: Exactly TARGET with unchanged L021/L053 pairs and positive rho, audited L056 shell, L059 column, audited L060 minimizer and audited L061 28-coordinate witness; represented scalar closure only, no retuning or added global/label constraints.

## Precise imports and applicability

Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE Trans. Inform. Theory 51
(2005), 2859–2866, DOI 10.1109/TIT.2005.851748, author manuscript
III.B (62)–(65), printed p. 7. Cross-check Hyun Kwang Kim and Phan Thanh
Toan, *Improved Semidefinite Programming Bound on Sizes of Codes*,
arXiv:1212.3467v1, 14 December 2012, III.A Remark 11 and III.B (31)–(35),
printed pp. 8–9. Nonempty binary constant-weight codes with even d>=4
and d<2w<=n cover n=1024,w=68,d=10. No field or RS hypothesis is needed.
Foundations/04 records the full normalization, ordinary rows and proof
cases. Only actual positive-multinomial orbits are variables. Distance
zero means repeated words; only nonzero distances below d are forbidden.
Permutation equalities preserve t-s, not merely the distance multiset.
The suspect complement prefactor in Schrijver (61) remains unused.

Import Sven C. Polak, *Semidefinite Programming Bounds for Constant-Weight
Codes*, IEEE Trans. Inform. Theory 65 (2019), 28–38,
DOI 10.1109/TIT.2018.2854800, arXiv:1703.05171v1, Section 1.1 (1)–(3),
Proposition 1.1 and its complete indicator proof, p. 2. This gives the
union-index meaning, not a measure for the proposed moments. The printed
A(n,d) endpoint is qualified by the proof's A(n,d,w). Section 1.2 permits
only constraint-preserving averaging. The notebook claims one invariant
unlabeled assignment, not averaging of labeled feasible points.

Reuse Schrijver (7), Proposition 5 (44)–(47), Theorem 1 (51), III.A
(52)–(59), III.B (64), pp. 2,5–7, as recorded in foundations/09:
unequal layers 0,5,6 and factor sizes 68,956 lie in the source ranges.
The algebra applies to invariant matrices without a code or representing
measure. Principal layer restriction is covered; exhaustiveness and
positive rescalings of the particular blocks remain audit obligations.

Import Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, Acta Scientiarum Mathematicarum, published 27 February 2026,
DOI 10.1007/s44146-026-00231-y, Section 2 Theorem 2.6 and Corollary 2.2,
with Theorem 2.1 and its proof for the finite projection identities.
For a finite Hermitian [A,B;B*,C], PSD requires and is equivalent to
C PSD, ker(C) contained in ker(B), and A-B C^dagger B* PSD.
Singular C and an entire new block are allowed. The retained anchor
congruence, kernel annihilation and full Schur remainder must still be
checked; individual column passes cannot replace them. The corrected
L061 assessment attributes these inputs to Theorems 2.1/2.6, not an
unproved inverse-action attribution to Lemma 2.7.

No imported theorem needs reproof. Local reconstruction is justified to
verify a finite specialization no cited theorem evaluates. Chordal
completion and Dreyer's free-cross-block theorem cannot enforce the
prescribed union equalities and scalar rows; neither is used. Albert's
original proof, Delsarte's restricted thesis and the inaccessible Boyd
book remain nonessential unread leads because inspected sources cover
the needed inputs. Full matching and supporting Mathlib coverage remain
not checked; unknown availability is not evidence of absence.

## Bounded critical-review obligations

Read L062's manuscript and the complete relevant scalar constructor and
independent verification certificates, not just previews or counts:
`scripts/finite-support/simultaneous-shell-ordinary-scalars-results.json`
and `scripts/finite-support/simultaneous-shell-ordinary-scalars-verification.json`.
Check the conversion from ordered orbit counts to conditional y=T/rho
against Schrijver (62)–(63) and L053, retaining the positive orbit factor
and singleton normalization. The five/five, five/six and six/six values
must be the actual conditional moments, rather than their separately
normalized shell coefficients. Review the region-exhaustion argument,
all six presentations, original t-s, cross-type unordered equalities
and closure at anchors outside the retained matrix. Retain pairs through
p_12 and Boolean repetition as a pair coordinate.

Verify every claimed scalar inequality, extremum and Boolean/forbidden
case from complete evidence. Independently confirm that these moments
and all 28 coordinates agree with the *same* audited L061 witness.
Use the complete simultaneous-shell constructor, verification and
critical-audit certificates under `scripts/finite-support/`, and the
L060 energy certificates where normalization is load-bearing. Preserve
all 49 blocks, zero-mode cross equations, positive normalizations and
anchor transport. Reuse the audited PSD proof instead of treating the
new scalar pass and an unrelated PSD pass as compatible. This source
turn has not inspected certificate coordinates or rerun any verifier.

Essential local inputs: L021,L053,L056,L059,L060,audited L061,L062;
foundations/04,09,10,12 and the complete certificates named above.
L054's source reduction is available through those canonical inputs;
its superseded trial is not reused as the current assignment.

## Relevance, duplicates and decision test

Main gap: arbitrary-center safety at 67/68 agreements in the unchanged
955–957 bracket. Intermediate target: critical verification of L062's
strengthened fixed nonexclusion claim. Downstream use: retain or repair
the evidence parking exactly the represented scalar-plus-PSD diagnostic,
so later mechanisms do not rely on an unaudited stop. This is local
verification of assessed methods, not a new general feasibility theorem.

ATTEMPTS/015 concerns L023's different prescription; ATTEMPTS/043 and the
completed L061 audit concern PSD without the new scalar rows. Neither
settles the strengthened manuscript claim. ATTEMPTS/044 preserves the
step-207 stop pending this review. Those stops do not prohibit different
moments, additional restrictions or independent mechanisms.

Continue to exactly this audit. Retain L062 only if normalization, full
represented closure, every scalar case and identical complete singular
PSD witness withstand critical review. A concrete omission, conflicting
coordinate or wrong normalization calls for a canonical repair or scope
qualification. An incomplete review remains unfinished; failure of one
witness alone cannot exclude every completion. No complete solution is
proposed. Unrepresented scalar rows, global PSD/moment consistency,
actual-label constraints, measures, packings, RS realization and both
boundary indices remain unresolved, independently of the audit verdict.
