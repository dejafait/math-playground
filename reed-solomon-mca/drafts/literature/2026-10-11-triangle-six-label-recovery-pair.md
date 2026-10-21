# Six-label additional-error pair — completed source comparison

TARGET: Bound the number of additional recoveries by twelve for a gated L057 triangle containing two distinct full-weight additional recoveries whose supports have union size six.
CHECKED: 2026-10-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Nine bounded exact-statement/terminology queries on 2026-10-11 found no matching inspected primary bound; compared L015/L069, L032/L033 and L057 with the pair hypotheses and retained ATTEMPTS/007,025,026; precise searches and limits below.
SOURCE_EVIDENCE: Reused Hall Theorem 5.1.1 and full proof pp. 63–64 and Marquez-Corbella–Pellikaan section 5 pp. 7–8 from their inspected assessments; retrieved Chojecki author TeX v9.2 and read thm:bounded-residual-kernel-ray with full proof lines 1370–1421 and DR6–DRC with full proof lines 2883–2935; reused DR2 and stronger-count comparisons cited below.
COMPARISON: L033 assumes an actual third error and a prescribed three-root lift, and proves no twelve estimate even there; L015/L069 require five labels. The primary residual-kernel bound confines every counted support to one fixed set, whereas this target confines only the selected pair. Recurrence supplies exact recovery tests but no count of their simultaneous fibers.
GAP: Exclude sixteen total bad parameters, equivalently thirteen additional relaxed parameters after L057's three base events, under the six-label-pair hypothesis without assuming a third clustered error, rational descent or confinement of other supports.
REASON: Essential distance, moment, shortening and recovery coverage permits one bounded compatibility/count proof attempt, but no matching bound was found; EXPLORE records adequacy for that attempt, not correctness or novelty. This newly completed assessment receives separate supervisor approval before research.
SCOPE: Fixed F_(97^20), order-sixteen H, gated L057 tau=0 triangle, arbitrary extension-field weights and original finite chart; distinct additional parameters u,v with full supports K_u,K_v and |K_u union K_v|=6. Count every distinct additional relaxed recovery, retaining both-zero lifts and zero fourth weights.

## Completed comparison, step 163

Main gap: uniform triangle twelve. The intermediate target is the exact
conditional pair bound in TARGET. It could remove one concentrated-support
branch in a later case split. Larger unions, useful-pair existence, other
triple patterns, arbitrary extraction and the challenge definitions remain
independent gaps. No universal pair existence is asserted.

Read L057's complete hypotheses and recovery statement, L069's application,
L015's analytic reduction, L032's hypotheses/classification and affine-lift
proof, and L033's hypotheses and complete shortening/incidence proof.
L057 supplies independent syndrome directions, nonzero D and locators,
three full base events and the complete relaxed recovery set. These facts
hold over the stated extension field and original chart. L010's bound and
equality conditions remain established inputs, not new derivations here.

L015's cancellation-plus-rational-point bound has exactly five coordinates.
The read L069 proof uses that hypothesis explicitly. Its completed census
cannot be extended to six coordinates by relabeling its points.
L032 classifies **three** actual errors with small union under equality;
it does not produce a third error from two. L033 alternatively assumes an
explicit six-coordinate affine lift whose coordinates are nonzero slopes
times T-gamma_i on three two-element classes. Its proof that the lift has
weight six at every other parameter uses exactly those three prescribed
roots. A pair supplies no stated hypothesis fixing the two common
coordinates in that way. Whether an applicable third error can be forced,
and how other cancellations affect counting, are proof obligations.
Moreover L033 stops at 210+720 indexed projective lines and the unproved
twelve-incidence threshold. It is a useful reduction lead, not an import
of the target. Rational configuration lines do not rationalize the pencil.

## Primary coverage and source qualifications

Reuse J. I. Hall, *Notes on Coding Theory*, GRS chapter,
[Theorem 5.1.1 and proof](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
printed pp. 63–64, interpolation p. 65, undated author copy inspected
October 5 and retrieved again October 11. The saved primary extraction in
`2026-10-05-two-block-moment-obstruction.md` and its ready reuse in
`2026-10-11-triangle-five-label-recovery-cluster.md` cover any field,
distinct evaluations, nonzero multipliers and 0<k<=n. Here n=16,k=8,
unit multipliers and distinct H labels give distance nine. L010, rather
than Hall, supplies the shifted-moment kernel and sparse uniqueness.
No generic distance or interpolation reproof is needed.

Reuse I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS
codes that have an error correcting pair*, FFAA 40 (2016), 224–245,
[DOI 10.1016/j.ffa.2016.04.004](https://doi.org/10.1016/j.ffa.2016.04.004),
[2016-02-29 accepted manuscript](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
section 5, Definitions 5.1–5.2, Lemma 5.3 and the following unnumbered
GRS shortening formula, pp. 7–8. Read the saved primary extraction in
`2026-10-07-six-coordinate-triple-equality-obstruction.md` and L033's
specialization: zero coordinates are imposed before deletion; deleting
y reduces dimension by one and multiplies retained multipliers by z-y.
Each later use must identify its actual deleted labels, positive dimension,
parameter condition and nonzero differences. The source is adequate for
such applications over F; it neither selects the relevant support cases
nor bounds their simultaneous parameters. No shortening reproof is needed.

P. Chojecki, *Shortening Bounds for Reed–Solomon MCA*,
[author TeX v9.2](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
dated July 17, 2026 in the reused assessment, retrieved October 11.
Read `thm:bounded-residual-kernel-ray`, lines 1370–1421, including its
complete proof and both active-support cases. It requires every counted
error support inside one fixed U and transversality for every slope;
its bound is (t+1)|F|^kappa(U). The six-label **pair** condition does not
assert that confinement for other errors. Its proof lifts all counted
errors in U and groups their differences by ker(H_U); that step cannot
be imported for supports outside U. Read `drc:thm-exact-compiler`,
DR6–DRC, lines 2883–2935 with full proof; reused DR2, lines 2785–2850,
from `2026-10-10-triangle-twelve-recovery-bound.md`. Distinct weighted
columns, R=8,t=4 and multiplier x match L057. These characterize transverse
recoveries but leave their fiber sizes unbounded. The full-vector common
case does not erase L057's both-zero projected lifts. This mutable source
is not certified identical to ePrint 2026/1463.

Reuse the same ready assessment's inspected fixed-circuit, fixed-core,
BCHKS, Tamo and subspace-design comparisons. The fixed-circuit result
confines all witnesses to a nine-set and gives 36; the fixed-core result
requires a core for every counted witness. Neither premise follows from
the chosen pair. BCHKS's saved sharp-range endpoint is below this cell,
and its wider coefficient exceeds sixteen; generic-domain or structured
design conclusions have no supplied fixed-H identification. No relevant
changed hypothesis warrants reopening their full proofs. The twisted-cubic
lead in the five-label assessment concerns a different code and remains
an unread full-proof lead, not an essential input or imported bound.

## Bounded searches and prior failures

Queries performed October 11:

- `"Reed Solomon" "two" "error supports" "six"`
- `"mutual correlated agreement" "six" "support"`
- `"Shortening Bounds" "Reed" pair affine lift`
- `"Reed-Solomon" "affine pencil" "support"`
- `"MDS" "sparse" "projective line" error supports`
- `"Reed-Solomon" "shortening" "mutual" "pair"`
- `"Reed-Solomon" "support union" "six"`
- `"MDS code" "two" "sparse representatives" pencil`
- `"Reed-Solomon" "secant" "syndrome" "line"`

Results included the author repository, the already compared shortening
paper and twisted-cubic lead, plus irrelevant decoding/index hits. No
additional matching primary theorem was inspected. Searched the author
TeX for six, pair, two-error, two-anchor, small-union, union of two and
support union; inspected the relevant residual-kernel statement/proof
and exact-compiler statement/proof before accepting any comparison.
This bounded search establishes no novelty or exhaustive literature claim.
No source-access blocker prevents the proposed attempt.

Read ATTEMPTS/007,025,026. The five-coordinate sixteen-generator stop is
preserved; it does not prohibit reuse of an upper bound. Formal triangle
common roots and unstructured selected-label samples remain exhausted;
the false two-antipodal isolated bound three remains refuted. The proposed
test uses an actual six-union full-error pair, not any of those mechanisms.
It neither enlarges a sampled sweep nor assumes an isolated maximum.

## One bounded mathematical continuation

Keep TARGET unchanged. The concrete mechanism to test is compatibility of
the selected pair's affine moment interpolation on its six-set with all
three original L057 errors and L010's sixteen-count equality constraints.
Assume thirteen additional **distinct original finite parameters** only
inside the contradiction attempt; use L010 to justify fullness and
coordinate balance before counting their supports. Test whether these
constraints force an applicable third clustered error or directly prevent
equality through the exact cancellation/shortened recovery equations.
Every implication from a pair to a six-coordinate lift, every possible
extra cancellation, and every claimed count must be proved in that later
turn. No such implication or bound is derived or approved mathematically
here. If a third error is obtained, L033 is available only after its
explicit lift hypotheses are checked, and its missing count remains.

Essential input IDs: L010, L041, L057. L032/L033 are conditional comparison
and application leads; L015/L069 cover only five labels. Arbitrary F
weights, original infinity exclusions, lower-weight relaxations, both-zero
lifts and scalar deduplication are retained. Do not assume rational descent,
all-support confinement or a third error. This six-set is the pair union,
not L057's nine-label base union.

Continue only with a new count-relevant restriction or a contradiction
covering every case of the pair scope, sufficient for twelve after the
three base events. An exact gated counterexample would be informative
negative evidence. If the attempt yields only an affine lift, indexed-line
reformulation, unproved third-error extraction or repeated capacity bound,
park this mechanism and select a different independently testable target.
No enlarged sweep is authorized by this assessment. Research may be
REPRODUCTION if it only specializes established results, or POTENTIALLY_NEW
for an uncovered compatibility/count argument; search absence certifies
neither originality nor a result. Mathlib matching and supporting coverage
are **not checked**. No cross-notebook mathematical input is used.

## Original proposed scope (before this source review; preserved)

Main gap: uniform triangle twelve. A bound for this adjacent concentrated
support branch could support a later case split. It would leave pairs with
larger union, existence of useful clusters, other triple patterns, arbitrary
extraction and challenge definitions unresolved. Universal six-label-pair
existence is not assumed. This is a proposed target, not work completed in
the L069 audit.

Essential prospective inputs are audited L057 and inherited L010/L041;
L015/L069 are the exact five-label comparison, not six-label premises.
L033 is named solely as a narrow local lead. Its overview requires an actual
union-six triple; whether a pair gives any usable replacement is unresolved.
Read only its relevant hypotheses/reduction and the associated assessment
before treating it as an input. No cross-notebook theorem is proposed.

The next literature step should compare the exact statement with those
local results and inspected primary distance/shortening/recurrence inputs,
search the changed support-pair scope and record a precise decision. Reuse
unchanged primary assessments; refresh only missing essential coverage.
Do not reprove distance, invent a third error, assume a rational chart, or
discard lower-weight and both-zero recoveries. No enlarged sampled sweep
or reuse of ATTEMPTS/025–026's exhausted mechanisms is proposed.

Continuation test: approve one bounded applicability/count test only if
coverage identifies a concrete mechanism retaining the exact gates. Import
an exact known bound if found. Otherwise record the specific hypothesis
mismatch or obstruction and select a materially different target; a formal
six-coordinate reformulation alone is insufficient. No new lemma,
mathematical script, derived six-label bound or approval occurs in this note.
Mathlib coverage for this changed target is not checked.
