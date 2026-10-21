# Affine fixed-block neighborhood sharpness — proposed ready test

TARGET: Test whether the prescribed 56-slope affine construction attains the ordinary fixed-block neighborhood cap while avoiding pair conflicts and every L033-forbidden triple containing the distinguished block.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed fixed-block neighborhood comparison in 2026-10-07-sixty-core-fixed-block-neighborhood.md; scoped searches of L029/L030, the sixty-core assessments, history/073–082 and ATTEMPTS/019–021,023 found no completed matching 56-slope test. No novelty claim follows.
SOURCE_EVIDENCE: Agrell–Vardy–Zeger, Upper Bounds for Constant-Weight Codes, June 24, 2000 manuscript (https://publications.lib.chalmers.se/records/fulltext/local_14986.pdf), definition (5), p. 3, Theorem 8 (37), p. 6, Theorem 32, p. 16, Theorem 36 (142)–(145), p. 17; reused the inspected ST/AGL dictionary underlying audited L033. L029's complete affine intersection construction, proof section, supplies the local method to adapt, not a result on eight-point blocks.
COMPARISON: Known shortening bounds cover T(3,8,5,956,10) without labels; L029 covers 21 pair classes with five-point affine graphs, not the new 56 triple classes. The changed incidence and the sharpness comparison need a later mathematical verification; neither is supplied by citation alone.
GAP: Determine the exact ordinary benchmark and whether this fixed construction reaches it in the graph containing pair conflicts and all L033-forbidden triples anchored at A. Full L034 neighborhood admissibility and conversion to its family cap are outside this diagnostic.
REASON: One finite specialization can stop a potentially vacuous graph improvement before optimization, or reject the proposed obstruction. This is reproduction of assessed counting/construction methods, with no new general theorem sought.
SCOPE: C001a's actual H; arbitrary 60-core C and residual eight-set A disjoint from C; all outside bijections in the construction below. Graph relaxation only, with complete L033 anchored incidence hypotheses and actual coefficient labels. Separate supervisor approval is required before this newly written ready continuation is invoked.

The main gap is arbitrary-center 68-agreement safety. A strict improvement
in a necessary neighborhood relaxation could justify a later whole-family
counting test. Conversely sharpness at the ordinary benchmark would stop
this graph mechanism alone. L034's sufficient uniform cap 184665717 is
not a neighborhood cap, and no conversion to it is assumed.

For X=H minus (C union A), let V consist of all eight-subsets B of
H minus C with |A intersect B|=3. Define a graph on V with an edge
between distinct B,B' if either |B intersect B'|>=4, or the triple
A,B,B' has empty triple intersection, all three pair intersections
of size three, and the actual overlap-cubic matrix has rank three.
This states the intended test, not an independence or extremal theorem.
L033's disjoint-root qualification is essential. Rank-two triples are
retained. Actual full neighborhoods must additionally satisfy L033 on
triples not containing A and every applicable L031 restriction; this
graph does not certify either requirement.

Prescribed candidate: order A increasingly by its E-residues, order its
three-subsets lexicographically, and assign slopes 0,...,55 in F_191.
Let Omega=({0,1,2,3,4} times F_191) disjoint union {*}. For each triple
T subset A and b in F_191, take R_(T,b)={(x,s_T*x+b):x=0,...,4}.
For any bijection sigma:Omega -> X consider B_(T,b)=T union sigma(R_(T,b)).
All independence, cardinality, and all-bijection claims are to be tested
next turn. F_191 is only an auxiliary point system, not a subfield of E.
The slopes and evaluation set are fixed; no search over alternatives is
approved by this scope.

Import AVZ's ordinary T bound with exact weights and distance ten;
verify its applicability and octant conditions. For the upper benchmark
use three head shortenings by (142), followed by zero-head deletion and
the disjoint-support base. Evaluate every floor exactly in the research
turn. The source omits these elementary proofs; a brief local justification
is appropriate if needed to check this finite implementation. Do not
reprove an unrelated general packing, theta or RS-rank theorem.

For the lower diagnostic, adapt L029's affine intersection method to
the changed triple classes and inspect all anchored L033 incidence cases,
including nonempty triple intersection. If symbolic avoidance succeeds,
actual labels require no rank computation on nonexistent incidence cases;
justify this rather than assume label symmetry. If a requisite pattern
occurs, test its actual matrix or retain it as an unresolved case.
Do not infer avoidance among neighbors or of quadruples from the anchored
calculation. A finite certificate should store full exact evidence and
print only cardinality, actual/required bounds, failures and artifact paths.

Continuation/abandonment test: a proved ordinary upper bound together
with an equal-size graph-independent construction parks every stricter
cardinality claim for this graph. A proved violation rejects only this
candidate; it permits further work only after a new concrete discriminating
test. An incomplete construction proof is EXPLORATION, not a cap or stop.
No unsafe list or boundary improvement follows from either result.

Essential inputs: L034, audited L033, L001 and C001a; L029 supplies the
construction method. L031 is an unresolved retained restriction in the
full problem, not a premise of this graph certificate. Preserve L030
and ATTEMPTS/019–021,023 as scope comparisons. Independent gaps remain
full labeled neighborhoods, whole-family counting, cross-core consistency,
large-list realization, 67-agreement safety and ABF equivalence.
Mathlib: matching sharpness result and supporting double-weight code
bounds not checked. This assessment derives no new result and runs no
mathematical script.
