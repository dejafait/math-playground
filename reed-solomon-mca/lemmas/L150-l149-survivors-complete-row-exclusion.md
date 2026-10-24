# L150 — Complete two-overlap capacity excludes L149's two survivors

## Hypotheses

Use F=F_(97^20), H={x in F_97^*:x^16=1}, k=8, L010's shifted
moments of orders one through eight, and the pinned same-support event
on 1/4<=delta<5/16. Assume sixteen actual original finite bad parameters,
actual nonzero Hankel determinant and coordinate-locator polynomials,
L104's represented t=0 class, and both coefficient syndromes in U_S for
S={1,8,12,18,22,27,33}. Retain L109's and audited L149's inherited
finite-certificate qualifications. Weights and the prescribed original
chart are arbitrary over F. Universal seven-coordinate representation,
fixed-pair extraction and challenge equivalence are not assumed.

Consider exactly audited L149's planes, in increasing S coordinates:

    P: u=(1,0,40,56,96,57,34), v=(0,45,56,59,65,18,55),
    R: u=(1,0,31,55,34,85,3), v=(0,47,67,90,86,57,18).

For an indexed application assume L149's four selected supports are
actual equality errors: A1={1,8,47,50}, A2={12,18,64,75} and the
two supports at ordered indices (467,750), (750,467), (608,695) or
(695,608) in L125's full 756-support universe. Both orders are retained.

## Conclusion

For each plane exactly four of all 756 supports I union K, with
I in binom(S,2) and K in binom(H minus S,2), have rank-one projections.
All four pass the intrinsic full-weight gates and give distinct directions.
The other 752 have rank-two projections and no recovery. There are no
rank-zero projections, failed-weight rank-one rows or duplicate full
directions. The entire successful list is below. All residues are in
F_97; weights are in increasing I order followed by increasing K order.

| Plane | Index | I; K | (alpha,beta) | Normalized direction | lambda | Error weights |
| --- | ---: | --- | --- | --- | ---: | --- |
| P | 0 | 1,8; 47,50 | (74,22) | (1,37) | 60 | (43,65,94,31) |
| P | 412 | 12,18; 64,75 | (20,12) | (1,20) | 52 | (15,74,82,35) |
| P | 467 | 12,22; 89,96 | (39,54) | (1,76) | 52 | (58,7,31,69) |
| P | 750 | 27,33; 79,85 | (59,6) | (1,56) | 52 | (18,65,57,84) |
| R | 0 | 1,8; 47,50 | (12,6) | (1,49) | 22 | (75,56,28,34) |
| R | 412 | 12,18; 64,75 | (64,12) | (1,79) | 50 | (85,93,49,15) |
| R | 608 | 18,27; 79,96 | (5,78) | (1,35) | 50 | (90,23,29,35) |
| R | 695 | 22,33; 50,79 | (77,11) | (1,14) | 50 | (75,66,96,80) |

Each plane therefore has at most four full finite two-overlap directions
in any prescribed chart, eight below L109's necessary twelve. Neither
plane can occur at equality. Audited L149 binds them to exactly the four
ordered occurrences above, which are consequently excluded under their
actual-support hypotheses. This is no entire-third or fixed-pair assembly
and gives no global improvement to 11/q–16/q. All historical lists stay
preserved. Same-step complete independent replay and the separate critical audit
below pass.

## Proof

### Ready coverage and exact inputs

Step `2026-10-24-mca-457-l149-survivor-capacity` uses the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-24-l149-survivor-capacity-review.md`.
This is RESEARCH / REPRODUCTION / calculation. The needed new work is
the record-specific finite count, not a general theorem reproof or a
claim of progress beyond checked sources. L109 supplies independent-wedge
necessity, r=12+n_0>=12 actual two-overlap directions and the complete
projection, weight and prescribed-chart criterion. Audited L149 supplies
exactly these two planes and their four ordered occurrences. L142's
programs supply a method precedent, not an imported count or theorem
about these different planes. ATTEMPTS/045–047 preserve the failure of
selected-four-row exclusion; the present test covers all supports.

Standard inputs reused through L109 and L149 are J. I. Hall,
*Notes on Coding Theory*, undated GRS chapter,
[Theorem 5.1.1 and full proof, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf);
I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004,
[accepted manuscript 2016-02-29, section 5, Definitions 5.1–5.2 and
the GRS shortening formula after Lemma 5.3, printed pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf);
and K. Conrad, [*Exterior Powers*, Theorems 4.2, 7.1, 7.5 and full
proofs, printed pp. 11–12,23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf),
undated 47-page author PDF. The saved inspected-primary assessment is
reused, without new retrieval or a source-currentness claim. The sixteen
labels are distinct, multipliers nonzero and k=8. Each row shortens
exactly seven labels J minus K, reducing positive dimensions eight to
one with nonzero label-difference multipliers. The separate parameter
assertion in Lemma 5.3 is not used outside its hypotheses. Exterior
degree two in a seven-dimensional space over a field is unchanged.
No general coding or exterior result needs reproving.

Both new programs bind all 4,476 passing checks of L149's separate
step-455 audit, its two successful isolated executions, unchanged-input
verdict and audit-code hash. Every one of its 502 input hashes is checked,
including the complete classification/replay and original L125/L148
provenance. Including the L149 audit certificate and code, all 504 bound
originals are checked before and after; none is rewritten. The retained
classification records are exactly the four intrinsic survivors.

Paths here are relative to `scripts/seven-coordinate/`. The source
`l148-rank20-gates.json` binds P to `new-pair-filter/third-467.json`
at `/cases/249`, minor residue 78, and `third-750.json` at `/cases/128`,
residue 57. It binds R to `third-608.json` at `/cases/212`, residue 18,
and `third-695.json` at `/cases/200`, residue 29. These are the complete
original kernels and unique planes certified by audited L149, not
newly inferred from four compatible recoveries. Both representatives
match literally. All sixteen ordered selected-row regressions match
raw directions, lambdas, four weights and prescribed-chart coefficients.

### Complete support and quotient test

Put J=H minus S. Enumerate all 21 increasing I pairs and all 36
increasing K pairs, I outermost, with no incidence pruning. For each put

    g_K(X)=product_(y in J minus K)(X-y), z=min(S minus I),
    c_x(w)=g_K(z)w_x-g_K(x)w_z  (x in S minus (I union {z})).

Let Q be the resulting four-by-seven matrix. Save all sixteen g_K values,
Q, Qu, Qv and the six two-by-two projection minors. Every g_K value
on S union K is nonzero by distinctness. A nonzero minor proves rank
two and no nonzero intersection of the plane with ker Q. If every minor
vanishes but some entry of (Qu,Qv) is nonzero, choose such a component m:

    (alpha,beta)=(-(Qv)_m,(Qu)_m), h=alpha*u+beta*v,
    lambda=h_z/g_K(z),
    e_i=h_i-lambda*g_K(i) for i in I,
    e_k=-lambda*g_K(k) for k in K.

Independence of u,v makes h nonzero; rank one makes its line the entire
intersection. Keep lambda zero and either canceled overlap weight as
explicit failed gates; no division by these weights occurs. Save and
check h-e=lambda*g_K at every H coordinate (h extended by zero off S)
and all eight original shifted moments of h-e. The lambda test is also
the outside-weight test because g_K(k) is nonzero on K.

Rank zero is retained as its own branch: L109 rejects a whole plane
inside ker Q by actual polynomial nonpersistence, including deficient
weights. The producer records both coefficient recoveries in that branch;
the verifier would leave it unresolved for full coefficient replay
instead of issuing a capacity verdict. No such branch occurs here.

The full census yields 752 rank-two and four rank-one projections on
each plane, with no failed-weight rows. Grouping successful rows by
normalized projective (alpha,beta) gives the four singleton groups in
the conclusion for each plane, with no duplicate directions. Thus all
756 supports are classified, including every rejected support.

### Independent original moments and complete extension kernels

Reproduce from the notebook with assertions enabled:

    python3 -E -B scripts/seven-coordinate/l149_survivor_full_rows.py
    python3 -E -B scripts/seven-coordinate/verify_l149_survivor_full_rows.py

The complete certificates are
`scripts/seven-coordinate/l149-survivor-full-rows.json` and
`scripts/seven-coordinate/l149-survivor-full-rows-replay.json`.
Both finish with zero failures and zero unresolved branches. The compact
`scripts/seven-coordinate/l149-survivor-full-rows-summary.json` is a
derived inspection aid, not an independent proof input. No mathematical
execution failed. An initial adaptation-generation assertion caught an
unreplaced historical label before it wrote either new program; no
failed mathematical certificate or original was discarded.

The verifier imports neither the producer nor its helpers. It generates
H by powers of eight, checks equality with the producer's root-defined H,
and checks the complete ordered 756-support universe. It independently
forms every g_K through polynomial multiplication and Horner evaluation
rather than direct evaluation products. All saved quotient entries,
minors, weights and dispositions agree.

For each support, including every rejection, it forms the original
eight-by-six homogeneous moment matrix in variables
(alpha,beta,e_i1,e_i2,e_k1,e_k2). Row d, for d=1,...,8, is

    (sum_(x in S)u_x*x^d, sum_(x in S)v_x*x^d,
     -i1^d,-i2^d,-k1^d,-k2^d).

Reverse-column-pivot elimination saves the entire reduced matrix R,
its pivot columns and nonzero pivot values, an eight-by-eight left
multiplier E and every null-basis vector. Check E*M=R entrywise,
identity pivot columns, all remaining rows zero, original residuals
of every null vector and its identity free coordinates. Exact integer
Bareiss elimination checks every division and supplies det(E) with
nonzero residue modulo 97 for every support. A four-by-four minor from
the first four moment rows and error columns also has nonzero residue,
excluding a nonzero pure-error kernel. Thus the displayed null bases
are complete, of dimension six minus rank, rather than sampled lines.

On each plane the original ranks are six at 752 supports and five at
four, exactly projection rank plus four. All 752 rejected kernels are
zero. Every remaining kernel is one line whose six coefficients are
proportional by one nonzero scalar to the quotient direction and four
error weights. All sixteen pointwise identities and eight moments of
each of the eight full rows agree. Both ordered occurrences of each
plane retain all their selected-row regressions.

The verifier checks every nonzero component used as a projection pivot:
fifteen fixed-basis choices per plane. For every nonzero exterior pivot
it reconstructs u'_x=p_xb/p_ab, v'_x=p_ax and checks the entire wedge.
Each plane has twenty such exterior pivots; all nonzero projection
components in those representatives give 300 records per plane. Every
new h, lambda and all four weights have the same explicitly nonzero
scale relative to the fixed recovery. Zero projection components are
retained as zeros and never inverted. No alternative pivot changes a
gate or creates another direction.

Every matrix, invertible E, nonzero determinant and complete kernel is
over F_97. The identities persist over every extension: E remains
invertible, R has the same pivots and zero rows, and its free coordinates
still parametrize the full kernel. Hence no rejected support acquires
a recovery and no rank-five support acquires a second direction over
F_(97^20). This proves the complete extension-field count, rather than
inferring it from prime-field point sampling. Shared Python, residue
arithmetic, the moment convention and inherited finite certificates
remain computational qualifications. This is same-step independent
replay, not a separate critical audit or formal verification.

### Prescribed chart and necessary-threshold contradiction

For arbitrary extension-field A,B,C,D with Delta=AD-BC nonzero, let
u_original=A*u+B*v and v_original=C*u+D*v. Solving for the original
coefficient of h=alpha*u+beta*v gives

    alpha_original=(D*alpha-C*beta)/Delta.

A zero numerator omits that direction. Otherwise h, lambda and all
four weights divide by this same nonzero coefficient. Thus each raw
direction in the table retains its exact gate D*alpha-C*beta!=0, with
no rationality restriction on the original chart. An invertible basis
change preserves projective distinctness; deleting the omitted direction
can only decrease the four-direction count. No prescribed chart can
increase it or repair a failed weight.

At t=0 equality L109 first proves lift independence and full activity,
then gives 2n_0+n_1=4 and r=12+n_0>=12 actual distinct finite
two-overlap rows. Equality supplies full weights, so each such row
must appear in this complete census as one of its full directions.
Four is less than twelve before any prescribed-chart deletion, a
contradiction on either plane. Audited L149 forces precisely P or R
for the four surviving ordered occurrences stated in the hypotheses;
each is therefore excluded individually. No other occurrence is added
to this application and no assembly is inferred.

The selected-four-row stop remains valid: those four intrinsic tests
alone pass, and the contradiction uses the separate all-support count
and actual-equality threshold. No r>=6 converse, nonpersistence
construction, represented t=0 attainment, additional-event construction,
recursive deletion or sixteen-event completion is used. All historical
154/44/26/eight-mismatch domains remain unchanged. Other residuals,
third/pair assembly, universal representation/extraction and certified
challenge definitions remain open; the global interval is 11/q–16/q.

### Separate critical audit, 2026-10-24

Step `2026-10-24-mca-459-l150-critical-audit` completed the invocation-start
SPECIALIZE target in
`drafts/literature/2026-10-24-l150-critical-audit-review.md` as
RESEARCH / REPRODUCTION / proof_audit. The entire proof and both complete
standalone programs were read. They import only standard-library modules;
no historical mathematical main routine runs. The necessary threshold,
independent-wedge, projection, weight and chart arguments in L109, the
exact P/R classification and separate audit in L149, and the relevant
L125/L148 original-kernel provenance and audit scopes were checked.
Ready primary coverage and the recorded duplicate/failure comparison were
reused. No general theorem was reproved and no new target was calculated.

Reproduce this separate audit with assertions enabled:

    python3 -E -B scripts/seven-coordinate/audit_l150.py

The complete audit evidence is
`scripts/seven-coordinate/l150-critical-audit.json`.
All 14,307/14,307 checks pass with zero failures. Both complete programs
execute in an isolated notebook-shaped tree and reproduce both full
outputs byte for byte. All 508 bound original files remain unchanged:
504 inherited bindings plus the two programs and their two outputs.
All 502 L149 input hashes, its 4,476 passing checks, both successful
isolated runs and unchanged-original verdict bind. These inherited
certificates retain their qualifications; their historical searches
are not rerun.

An independent four-subset enumeration gives exactly the same complete
756-support universe, without incidence pruning. Each of the four
ordered occurrences matches its entire original L125 record and audited
L149 plane. Exact rational determinant evaluation also confirms the
four original rank-20 minor residues 78,57,18,29. Both orders retain the
same original support labels and all sixteen selected-row regressions.
No unique plane is inferred merely from four compatible recoveries.

For all 1,512 supports the audit reconstructs the full original eight-by-six
moment matrix and checks every entry of E*M=R. Exact rational elimination,
separate from the verifier's integer Bareiss procedure, confirms each
saved integer determinant of E and its nonzero residue. Identity pivot
columns, every zero remaining row, all null-vector residuals and identity
free coordinates establish each complete kernel. The four error columns
have an independently checked nonzero original four-by-four minor.
Consequently there is no pure-error solution or missing extension direction:
the same invertible E and complete normal form hold over every extension.
All 1,504 rejected matrices have rank six and zero kernel; the other eight
have rank five and a single full recovery line.

The derivative of X^16-1 gives a third construction of g_K on S union K,
with nonzero denominators; zero values on J minus K are retained. Every
quotient, projection and minor agrees. All eight published rows bind to
the full evidence, including their actual weights, 128 pointwise entries,
64 shifted moments and prescribed finite-gate coefficients. The complete
nonzero-pivot domains contain 30 fixed projection choices and 600
exterior/projection choices. Their reconstructed wedges agree, and each
h, lambda and error vector has the same explicitly nonzero scale as its
fixed recovery. Every rank/weight branch is checked; there are no rank-zero
rows, failed full-weight rows or duplicate successful directions.

The inverse basis formula gives original first coefficient
(D*alpha-C*beta)/(AD-BC). It applies to every invertible basis change over
the extension field: a zero numerator omits that projective line, and a
nonzero numerator only rescales its weights. Thus the four distinct
full directions on each plane remain an upper bound in every prescribed
chart. L109 supplies at least twelve actual distinct two-overlap rows
only after equality and lift independence. Every such row must occur in
the complete census, giving four versus twelve and a shortfall of eight.
This validates exactly the four indexed applications. It uses no r>=6
converse, actual-event construction, t=0 realization or pair assembly.

The initial audit wrapper rejected a valid notebook-local lemma path
because it incorrectly confined bindings to the scripts directory. It
stopped before mathematical checking. Its unchanged code and diagnostic
are preserved in `scripts/seven-coordinate/l150-critical-audit-initial-wrapper.py`
and `scripts/seven-coordinate/l150-critical-audit-initial-wrapper.json`.
The path check was corrected to the active notebook boundary; the complete
subsequent audit above passes. No mathematical defect or changed direct
dependency was found, and no original calculation artifact was modified.

This validates an existing restricted input, not a new exclusion beyond
L150 or progress beyond the checked sources. Shared Python/residue
arithmetic, inherited finite certificates and unchecked Mathlib coverage
remain qualifications. ATTEMPTS/045–047 and all historical domains persist.
The argument and DAG are unchanged; this verdict supersedes historical
pending-audit wording without changing PROOF.md. Assembly, universal
representation/extraction and certified challenge definitions remain open;
the global interval stays 11/q–16/q.

## Mathlib

Full matching coverage for this exact two-plane census and supporting
finite-field linear algebra was not checked, and is not asserted absent.
The precise coding/exterior citations and unchanged hypotheses above
are reused. The complete finite certificates are qualified computational
proof inputs, with the separate critical audit above and no formal verification.
