# Reed–Solomon grand list-decoding challenge: argument overview

Status: [PROGRESS.md](PROGRESS.md). Graph: [DAG.md](DAG.md). Full proofs: lemmas/. The argument is incomplete.

## Assembly and unresolved gap

The [source audit](foundations/01-target-and-source-audit.md) and [pinned model](foundations/02-pinned-list-model.md) fix the available definitions; comparison with the unavailable July ABF26 PDF remains qualified.

L001 counts common k-subsets for simultaneous closed column-Hamming balls. L011 attains the recorded endpoint for a polynomial-root center; the field condition at that endpoint is not the sharp smaller-field threshold. Safe real radii are right-open at the next grid point, so a grid maximum is not an attained largest safe real radius.

## Partial results

Polynomial/rational-center constructions, coefficient-fiber witnesses and exact resource/SDP relaxations give restricted certificates. The fixed rate-1/16 finite bracket remains 955–957; arbitrary-center 67/68 agreement safety is unresolved. L030's audited actual local families have 2571353 blocks on every 61-core and avoid the entire L020 overlap pattern. Thus the 1532495 cap is false under those local constraints, including for a direct transfer from an ambient configuration budget. Cross-core or additional RS restrictions are essential. Feasibility of scalar, exact-cardinality or selected PSD constraints is not a packing or an RS list.

Audited L125 excludes coupling L030's exact full laws on two 61-cores sharing 60 points: a left event of probability at least 137/963 has no allowed partner. Audited L126 matches all 2552584 nonstar blocks when both full stars are retained and the left distinguished column is 16, giving size-sum <=2590122 and smaller-size <=1295061<1532496. Audited L127 recovers equal ambient stars from 18633 common supports under arbitrary labels, using column recovery and finite-group stability. Audited L128 transfers equal retained indicators to L126's matching: for s>=18633 common retained supports, size-sum <=2552584+2s<=2590122. Lower overlaps, unequal indicators, arbitrary laws and RS lists remain open.

L129 is an UNVERIFIED CANDIDATE for s=18632, with size-sum bound 2589848 and smaller-size bound 1294924. Column recovery, affine completion and transferring L126's matching after an auxiliary relabeling await separate critical audit. Equality of the original ambient stars is not asserted.

Audited L134 preserves L131's actual-label obstructing quadruple in cross-packed families of sizes 2552584 and at least 2346331 by signature-conditioned alteration. Universal occurrence, prescribed laws and RS realization remain open.

Audited L135–L137 and C137a exclude full-sheet span two, retaining degenerate cubics and both pencil cases. L138's audited translation equivalence excludes nontrivial action in dimension <=4; its inclusion is unproved. New L139 bounds proper message fibers by 243 over E or F using certified root propagation and unequal line caps; separate critical audit is pending. Small-fiber span three, retention and RS transfer remain open.

L132's within-budget synchronized cover defeats retention-only forcing. L133's g=f-1 matching has 2571300 edges and size-sum bound 2571406, so one side is at most 1285703<1532496. Full three-shift replay passes; separate critical audit is pending. These fixed maps cannot give a nonvacuous threshold example; arbitrary maps and RS transfer remain open.

L122's line-occupancy reduction, audited C122a and audited L123 certify 2298250371072 whole-subgroup ordered triples, endpoint maximum 67798380 attained exactly by antipodal pairs, and every-61-core Bonferroni survivor upper bound 1600876449624. Audited L124's one-sided spectral bound improves this to 1597620964591, saving 3255485033. Complete histograms, all signed mode bounds and rational enclosures remain canonical. Exact core maxima and threshold saving remain open; ambient counts cannot bypass L030.

The fixed-pair assignment survives the unchanged root-box checks. L121's independent audit accepts its selected fixed-triple fourth-order Boolean/cardinality capacity pass. Full/excluded PSD, other conditioned rows, shared fourth moments and realization remain open. This fixed diagnostic is closed as an exclusion route.

## Known traps checked

- The list threshold uses epsilon times the field size, not the interleaving alphabet size. Simultaneous agreement differs from independent row agreement.
- An optimal relaxation is neither an actual code size nor a realized measure/list; symmetrization cannot impose unproved actual-label equivalence.
- Numerical output needs exact primal/dual/PSD certificates with singular and excluded-anchor cases retained. Passing one fixed triple does not exhaust a joint fourth-moment system.
- The labeled incidence reduction counts unordered endpoints and ordered pair triples; star-line collisions are excluded exactly. Its whole-domain count would still not bound every core or selected support family.
- L123 retains both endpoint-placement cases and every nonidentity ratio, including the antipodal stabilizer. Its deletion upper bound concerns the full configuration set; the singleton union bound is a lower survivor bound, and neither proves selected-family supersaturation.
- L124 uses the largest algebraic nonconstant eigenvalue, zero diagonal and an unordered-pair factor of one half. All modes and exact enclosure branches are retained; a real eigenvector is not assumed to be a core.
- L030 obstructs exact single-core caps as well as their relaxations. Its local families have no asserted common RS center or cross-core compatibility; they do not disprove the RS target.
- L125 retains uniform-bijection pushforward probabilities and arbitrary symbol permutations; prime-field additivity and the exhaustive finite map test justify its star rigidity. A latent event gives only a lower bound on its output probability. L126 requires full-star retention for its stated bound. L127 recovers columns before its functional equation and selects surviving base lines before subtracting constants; its audit verifies the independent-uniform test, integer completion and zero-error case. L128 uses ambient equality for the pairing and counts only the retained stars, twice in the size sum; it assumes their retained indicators agree and claims no sharpness. L129 uses auxiliary star equality only; the packing condition is applied to the original supports after undoing the label correction. These two-core obstructions and L051's different all-core moment obstruction give no universal list bound.

- L130 uses conditional uniformity; residual intersection seven is forbidden since a,b differ. L134's audited four-class law and one-map deletion protect the right witnesses by zero degree. Block images are not independent; no explicit favorable map is given.
- L132 handles wraparound without rank invariance or cross-packing. L133 checks complete distinct supports and uses one shift's matching with tagged sides; arbitrary-map transfer is unproved. C137a uses complete retained directions: an infinite pencil point contradicts an affine intersection, while a finite point forces all messages equal without assuming injectivity.
- L135 retains repeated messages, the exceptional-root case and the auxiliary origin. Both failed omission tests are preserved; its no-exception proof uses all seven directions. L136 uses cyclic index permutations and allows extra incidences and all cubic degeneracies. L137's audit checks its group isotope, all-label propagation and ordinary-net upgrade before exclusion, including the conservative characteristic scope. Its K-form is a line cube, with no uniqueness or factor descent; the source's cuspidal omission remains qualified. L138 retains 1, extension-field cardinality and all 137 labels but assumes inclusion. L139 normalizes only auxiliary closure; three roots require distinct actual labels. Neither yields a retained-family cap.

## Historical overview

The [pre-compaction overview](history/2026-10-24-proof-overview-before-compaction.txt) preserves historical context; canonical proofs govern current claims.
