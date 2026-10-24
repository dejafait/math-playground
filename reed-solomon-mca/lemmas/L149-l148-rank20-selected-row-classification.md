# L149 — Eight L148 rank-20 records: four exclusions and two retained planes

## Hypotheses

Use F=F_(97^20), H={x in F_97^*:x^16=1}, C=RS[F,H,8],
L010's shifted moments and the pinned same-support event for
1/4<=delta<5/16. The actual Hankel determinant D and every actual
coordinate locator are nonzero polynomials. Both coefficient syndromes
belong to U_S for S={1,8,12,18,22,27,33}. Assume sixteen actual original
finite bad parameters, represented t=0, arbitrary extension-field
weights and an arbitrary prescribed original finite chart. Retain the
inherited finite-certificate qualifications of L109 and L125. Neither
universal seven-coordinate representation, fixed-pair extraction nor
equivalence with the uncertified challenge definitions is asserted.

Fix the actual supports A1={1,8,47,50}, A2={12,18,64,75}.
Use exactly the eight ordered mismatches preserved by L148:

    (467,750), (499,668), (608,695), (668,499),
    (678,749), (695,608), (749,678), (750,467).

Indices are L125's zero-based indices in the full lexicographic universe
binom(S,2) times binom(J,2), J=H minus S. Both orders remain separate.
For an equality application all four selected supports must be actual
error supports. Use L109's original 24-by-21 exterior stack, increasing
S-pair columns, z_j=min(S minus I_j) and lexicographic covector pairs.

## Conclusion

Every selected original stack has rank twenty and a complete
one-dimensional kernel. Its unique projective kernel point is
decomposable over F_97 and every extension. All 32 selected-row
projections have rank exactly one. The complete dispositions are:

| Ordered indices | Plane below | Original maximal-minor residues | Disposition |
| --- | --- | --- | --- |
| (467,750), (750,467) | P | 78,57 | All four intrinsic gates pass |
| (499,668), (668,499) | Q | 54,52 | First-row lambda zero; excluded |
| (608,695), (695,608) | R | 18,29 | All four intrinsic gates pass |
| (678,749), (749,678) | T | 67,19 | First-row lambda zero; excluded |

The four distinct planes have the following representatives in increasing
S coordinates. Their wedges are the complete original kernel generators,
normalized to one on the sole original free coordinate.

| Plane | u | v |
| --- | --- | --- |
| P | (1,0,40,56,96,57,34) | (0,45,56,59,65,18,55) |
| Q | (1,0,74,77,45,42,87) | (0,68,53,25,65,93,61) |
| R | (1,0,31,55,34,85,3) | (0,47,67,90,86,57,18) |
| T | (1,0,48,9,44,54,1) | (0,96,12,75,11,62,73) |

Here is every distinct selected-row gate. All residues are in F_97;
h=alpha*u+beta*v, and weights are unscaled in the order I increasing,
then K increasing. Within each pair of ordered occurrences only rows
three and four exchange.

| Plane | I; K | (alpha,beta) | lambda | Error weights |
| --- | --- | --- | ---: | --- |
| P | 1,8; 47,50 | (74,22) | 60 | (43,65,94,31) |
| P | 12,18; 64,75 | (20,12) | 52 | (15,74,82,35) |
| P | 12,22; 89,96 | (39,54) | 52 | (58,7,31,69) |
| P | 27,33; 79,85 | (59,6) | 52 | (18,65,57,84) |
| Q | 1,8; 47,50 | (89,13) | 0 | (89,11,0,0) |
| Q | 12,18; 64,75 | (41,12) | 29 | (9,65,42,96) |
| Q | 12,27; 79,89 | (61,56) | 29 | (4,28,9,53) |
| Q | 22,27; 64,96 | (35,40) | 29 | (60,78,69,22) |
| R | 1,8; 47,50 | (12,6) | 22 | (75,56,28,34) |
| R | 12,18; 64,75 | (64,12) | 50 | (85,93,49,15) |
| R | 18,27; 79,96 | (5,78) | 50 | (90,23,29,35) |
| R | 22,33; 50,79 | (77,11) | 50 | (75,66,96,80) |
| T | 1,8; 47,50 | (20,17) | 0 | (20,80,0,0) |
| T | 12,18; 64,75 | (75,12) | 1 | (2,90,65,10) |
| T | 22,27; 79,85 | (3,6) | 1 | (48,74,44,24) |
| T | 27,33; 75,96 | (14,87) | 1 | (62,17,4,62) |

For any prescribed basis u_original=A*u+B*v,
v_original=C*u+D*v with AD-BC nonzero, each listed direction additionally
requires D*alpha-C*beta nonzero. Keep all four conditions for each retained
plane; its convenient displayed chart is not substituted for the original
one. Thus (467,750),(750,467),(608,695),(695,608) are intrinsic survivors
with explicit chart qualifications, not actual-event constructions.

Exactly four indexed occurrences are excluded. Historical 154/44/26
lists and L148's eight-mismatch list stay preserved as original domains.
No third/pair assembly, added-row census, four-row converse, nonpersistence
construction, t=0 attainment, sixteen-event completion or global-bound
improvement follows. The interval stays 11/q–16/q. Complete same-step
independent replay and the separate critical audit below pass.

## Proof

### Imported tools, coverage and bounded purpose

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-24-l148-rank20-loci-review.md`.
Reuse its checked source statements, stronger-result comparison,
record-specific duplicate search and recorded failures. This is a
REPRODUCTION calculation using existing tools, not a new general theorem
or a claim of progress beyond the checked literature. L122's different
fixed pair supplies a survivor warning, not a transferable disposition.
ATTEMPTS/045–046 remain valid; L147's different two-dimensional kernel
locus is not imported or recomputed.

Through L109 import J. I. Hall, *Notes on Coding Theory*,
[Theorem 5.1.1 and proof, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and I. Marquez-Corbella–R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004,
[accepted manuscript 2016-02-29, section 5, Definitions 5.1–5.2 and
formula after Lemma 5.3, printed pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf).
There are sixteen distinct evaluations, unit multipliers and k=8.
Each row shortens precisely the seven distinct labels J minus K,
decreasing positive dimensions eight to one with nonzero label-difference
multipliers. No additional parameter assertion of Lemma 5.3 is used.
K. Conrad, [*Exterior Powers*, Theorems 4.2/7.1/7.5 and proofs,
printed pp. 11–12,23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf),
undated 47-page author PDF inspected October 18, supports the ordered
exterior bases and elementary wedges in dimension seven, exterior degree
two, over F_97 and its extensions. L109 already proves the homogeneous
criterion and pivot reconstruction needed here. These standard theorems
are imported with unchanged hypotheses; no general reproof is needed.

L109's necessary direction supplies an independent actual lift and its
nonzero wedge, the rank-zero rejection and all full-weight/chart gates.
L125 supplies the complete original indexed records and their audited
provenance. L148 supplies the exact ordered eight-mismatch domain and
its separately audited original-kernel bindings. The present calculation
binds those originals afresh before deriving these eight dispositions.

### Complete originals and extension kernels

Reproduce from this notebook with assertions enabled:

    python3 -E -B scripts/seven-coordinate/l148_rank20_gates.py
    python3 -E -B scripts/seven-coordinate/verify_l148_rank20_gates.py

Full evidence is `scripts/seven-coordinate/l148-rank20-gates.json` and
`scripts/seven-coordinate/l148-rank20-gates-replay.json`.
The producer verifies all passing checks and complete input manifests of
L148's step-451 audit. It binds L125's master, each selected original
shard and complete record at its saved pointer, retaining L125's older
`full_saved_replay_identical` verdict and exact 100,764/100,764 scope.
The eight selected records equal the complete originals, not a preview,
summary or a new filter. All 496 bound prior files remain byte unchanged.
Neither program executes any historical main routine.

Both programs independently reconstruct the 756-support universe, the
two fixed rows and all indexed third/fourth labels. Four distinct supports
and all six pairwise intersections are checked for every occurrence.
The producer directly evaluates

    g_K(X)=product_(y in J minus K)(X-y)

and constructs each original covector
c_x=g_K(z)E_x^*−g_K(x)E_z^*. Its six exterior products give each
original block. The replay instead multiplies the polynomial factors
and uses Horner evaluation on all H. Elementary symmetric sums also
independently check every saved polynomial coefficient. Every covector,
block and original stack agrees with the L125 master and L148 overlay;
all 4,032 original entries are checked. Distinct labels ensure every
g_K value on S union K is nonzero.

Column elimination tracking relations reconstructs each complete ordered
null basis. A sole free coordinate equal to one makes its vector p
nonzero. All 24 original residuals vanish. Independently, forward-row,
reverse-column Gauss–Jordan elimination reconstructs a one-dimensional
kernel proportional to p; separate column-rank elimination gives rank
twenty. For each occurrence a saved original 20-by-20 minor, with its
specified original rows and columns, has the nonzero residue in the
conclusion. Every determinant is evaluated afresh and independently
replayed, rather than copied from another occurrence.

The nonzero minor proves rank at least twenty, and the nonzero null
vector proves rank at most twenty. Hence p spans the complete kernel.
These witnesses persist over every extension of F_97: the minor stays
nonzero and the vector stays nonzero/null, so the entire extension kernel
is exactly {s*p:s in the extension}. This is not base-field point sampling.

### Complete homogeneous loci and every necessary row gate

For each generator extend p antisymmetrically and check all 35 values

    p_ab*p_cd-p_ac*p_bd+p_ad*p_bc, a<b<c<d.

Every value is zero, for 280 homogeneous checks in total. Every nonzero
extension-kernel tensor is s*p with s nonzero, and its quadratic values
are s^2 times these zeros. L109's criterion therefore proves that its
entire projective locus is the single decomposable point. Choosing the
first nonzero exterior coordinate p_ab reconstructs

    u_x=p_xb/p_ab,  v_x=p_ax,  u wedge v=p.

These are exactly the representatives in the conclusion; u and v are
independent since u_a=1,u_b=0,v_a=0,v_b=p_ab!=0. Every row-exchanged
pair has the same whole normalized vector, hence the same plane. The
four planes are distinct: their first exterior pivot is (1,8), and their
canonical vectors with coordinate 1 equal to one and coordinate 8 zero
are the four different u vectors displayed above. Such a vector is unique
in each plane because the two pivot coordinates restrict isomorphically
to F^2. Thus the eight occurrences retain four planes, two surviving.

For every selected row compute q_u=Q*u and q_v=Q*v. All six two-by-two
minors vanish, while q_u and q_v are not both zero; the restriction has
rank exactly one, including at every failed row. For any component m
with (q_u[m],q_v[m]) nonzero, take

    alpha=-q_v[m], beta=q_u[m], h=alpha*u+beta*v.

Then h is nonzero and Q*h=0. With z=min(S minus I), compute

    lambda=h_z/g_K(z),
    e_i=h_i-lambda*g_K(i) for i in I,
    e_k=-lambda*g_K(k) for k in K,
    e_x=0 otherwise.

The table records every resulting gate, including zeros. The complete
certificate verifies h−e=lambda*g_K at all sixteen H coordinates,
with h extended by zero outside S, and all eight original shifted moments

    sum_(x in H)(h_x-e_x)*x^d=0, d=1,...,8.

There are 512 pointwise entries and 256 moment residuals, all zero.
No row projection is rank zero, no overlap weight is zero, and the only
failed gates are the four first-row lambda zeros shown. Those failures
have two nonzero overlap weights and two zero outside weights. All other
selected rows have nonzero lambda and all four nonzero error weights.

The replay additionally constructs every original eight-by-six moment
matrix whose columns are sigma(u),sigma(v) and the negatives of the
four support moment columns. All 32 matrices have rank five and their
complete null lines are proportional to (alpha,beta,e_I,e_K), even in
the lambda-zero rows. This restores original moment compatibility
independently of the quotient equations. The four directions on each
surviving plane are checked pairwise distinct.

Every one of the 124 nonzero exterior pivots is replayed, reconstructing
the identical wedge. Across them all 1,882 nonzero projection-component
choices are retained. Each alternative intersection vector is a recorded
nonzero scalar multiple of its original h, and its lambda and all four
weights are independently evaluated and checked to have that same scale.
Thus every necessary gate is invariant under these choices. No nonzero
denominator, zero weight, extension direction or projection branch is
silently discarded.

### Arbitrary charts, indexed exclusions and the stopping boundary

For u_original=A*u+B*v, v_original=C*u+D*v, AD-BC!=0, write
h=a*u_original+b*v_original. Inverting this basis change gives

    a=(D*alpha-C*beta)/(AD-BC),
    b=(-B*alpha+A*beta)/(AD-BC).

The original finite gate is exactly a!=0. If it fails the direction is
omitted. Otherwise its parameter is b/a and its error and lambda divide
by a. This proves the displayed arbitrary-chart inequalities over all
extensions, including nonrational prescribed charts. In particular no
chart repairs a zero lambda or either zero outside weight.

For each Q or T occurrence, equality would supply by L109 a nonzero
decomposable wedge in its complete kernel. Its only possible plane fails
the necessary first-row full-weight test in every prescribed chart.
This proves exactly the four indexed exclusions. The other four occurrences
pass every selected intrinsic test and must be preserved with their
chart inequalities. Four projective compatible recoveries do not satisfy
L109's r>=6 converse hypotheses and do not establish nonpersistent actual
locators, represented t=0 attainment, same-support badness or sixteen
events. Even the three passing rows on Q and T are not event constructions.

This stops the selected-four-row exclusion attempt on P and R; its failure
is recorded in ATTEMPTS/047. No added row or assembly is tested. The
remaining actual-event count, universal representation/extraction and
challenge-definition qualifications are independent unresolved gaps.
All historical domains and unfinished work are preserved. Both complete
programs finish with zero failures and agree; they still share Python and
residue arithmetic. This same-step replay is not a separate critical audit
or proof-assistant verification. Inherited finite-computation qualifications
remain; the separate critical review below validates this restricted input.

### Separate critical audit, 2026-10-24

Step `2026-10-24-mca-455-l149-critical-audit` completed the invocation-start
SPECIALIZE target in
`drafts/literature/2026-10-24-l149-critical-audit-review.md` as
RESEARCH / REPRODUCTION / proof_audit. The full proof, both complete
programs, every called mathematical helper and import initialization were
read. The producer uses `l139_literal_reuse`'s input construction and
`verify_new_pair_filter`'s column kernel/determinant, with the guarded
initialization import `verify_fixed_three_row_extensions`;
`residual_kernel_gates` and `zero_anchor_support_filter` supply homogeneous,
plane and row calculations. The verifier uses
`verify_active_rank19_complete_loci`'s polynomial, rank, determinant and
plane operations and `verify_rank20_selected_gates`'s independent nullspace
and proportionality operations. Historical main routines do not execute.
L109's independent-wedge and necessary locus/projection/weight/chart
arguments, L125's original records and extension-kernel/audit scope, and
L148's exact eight-mismatch domain and separate audit were checked.
The ready primary assessment and duplicate/failure comparison were reused;
no general theorem was reproved.

Reproduce this separate audit with assertions enabled:

    python3 -E -B scripts/seven-coordinate/audit_l149.py

Full evidence is `scripts/seven-coordinate/l149-critical-audit.json`.
All 4,476/4,476 checks pass with zero failures. Both complete programs
execute in an isolated notebook-shaped tree and reproduce their entire
outputs byte for byte. All 502 bound original files remain unchanged.
The complete L125/L148 manifests bind, including L125's older
`full_saved_replay_identical` verdict and 100,764/100,764 scope. No
historical search or main routine runs. Every complete certificate record
and replay disposition is checked, not a preview or sample.

An additional enumeration by four-subsets of H with exactly two S labels
recovers the same full 756-entry universe and fixed pair. The exact eight
ordered records bind at their original unique shard/pointer, including
both orders and all historical lists. All 4,032 original entries, the
eight nonzero maximal minors and the complete normalized null lines
replay. Exact rational elimination additionally evaluates all eight
integer determinants and their nonzero residues, saved in the audit.
A nonzero rank-20 minor and a nonzero null vector prove rank exactly
twenty and the entire one-dimensional kernel over every extension.

All 280 homogeneous identities vanish coefficientwise on these lines.
Reconstruction gives the four distinct displayed planes; normalization
on the first two coordinates proves their distinctness. Every displayed
plane and all sixteen distinct gate-table rows are compared with the
complete numerical evidence, covering all 32 ordered row occurrences.
Each projection has rank one. All 512 pointwise entries and 256 original
shifted moments vanish. Independent reconstruction of every eight-by-six
moment matrix gives rank five and its complete null line, proportional
to the claimed direction and four weights, including the failed rows.

The entire alternative-pivot domains agree: 124 nonzero exterior pivots
and 1,882 nonzero projection-component choices. Each reconstructed wedge
is the original tensor. Every alternative intersection has a nonzero
proportionality scalar, and its lambda and all four error weights have
that same scalar. Nonzero g values follow from distinct retained labels;
every inverted exterior or projection pivot is explicitly retained.
Thus there is no missing extension direction, rank-zero case or canceled
overlap branch. The only failures are the four first-row lambda zeros,
each with two nonzero overlap weights and two zero outside weights.
All other selected rows pass; on each retained plane the four directions
are distinct.

The inverse prescribed-basis formula gives first coefficient
(D*alpha-C*beta)/(AD-BC) with AD-BC nonzero. Its zero numerator omits
the direction; otherwise normalizing divides every weight by the same
nonzero coefficient. This retains arbitrary, including nonrational,
original charts and proves that none repairs the failed outside weights.
The nonzero actual wedge is supplied by L109 before any kernel is used.
Exactly the four Q/T occurrences are excluded; the four P/R occurrences
retain two planes with all four original finite-gate inequalities.
L109's r>=6 converse is not applied to four rows, and no actual event,
nonpersistence, represented t=0 attainment or equality witness is inferred.

No mathematical defect, failed audit execution or changed direct
dependency was found. This validates an existing restricted input, with
no additional indexed exclusion or progress beyond the checked sources.
Shared Python/residue arithmetic, inherited finite certificates and
unchecked Mathlib coverage remain qualifications. ATTEMPTS/045–047 and
all historical domains persist. No added row or assembly was tested.
The argument and DAG are unchanged; this verdict supersedes pending-audit
wording in historical overviews and certificates. Survivor capacity,
assembly, universal representation/extraction and certified challenge
definitions remain unresolved, with interval 11/q–16/q.

## Mathlib

Full matching coverage for this exact eight-record classification:
**not checked**. Supporting coding, exterior, Plucker, rank and finite-field
coverage is not newly checked. The precise standard inputs above and
L109's proved gates are reused within the ready assessment. Unknown
availability is not evidence of absence. No formal verification or
mathematical originality is claimed.
