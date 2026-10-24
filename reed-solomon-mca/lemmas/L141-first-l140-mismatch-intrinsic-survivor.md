# L141 — Occurrence (199,565) retains one intrinsic plane

## Hypotheses

Use F=F_(97^20), H={x in F_97^*:x^16=1}, k=8, L010's shifted
moments and the pinned same-support event on 1/4<=delta<5/16. The
actual Hankel determinant D and every actual coordinate locator are
nonzero polynomials. Both coefficient syndromes belong to U_S for
S={1,8,12,18,22,27,33}. Assume sixteen original finite events and
L104's represented t=0 class, allowing arbitrary extension-field weights
and a prescribed original chart. Retain L109's inherited
L010/L103/L104/L040/L069/L086/L056 finite-certificate qualifications.

The four supports under test are assumed actual two-overlap errors:

| Row | I subset S | K subset J=H minus S |
| --- | --- | --- |
| 1 | {1,8} | {47,50} |
| 2 | {12,18} | {64,75} |
| 3 | {1,33} | {64,89} |
| 4 | {18,22} | {70,96} |

Use L109's original blocks with z_j=min(S minus I_j), increasing
covector pairs and increasing S-pair exterior columns. Rows three and
four have L125 full-universe indices (199,565), with their order
preserved. Audited L140 records this occurrence as its first literal
mismatch. No universal representation or fixed-pair extraction is assumed.

## Conclusion

The complete original stack has rank nineteen over every extension of
F_97. Its entire homogeneous decomposable locus consists of two points
[s:t]=[1:0] and [1:81]; infinity [0:1] is not decomposable. The first
plane has rank-one projections but lambda zero at all four rows. The
second plane has rank-one projections and all four error weights nonzero
at every selected row. Thus exactly one intrinsic plane survives.

For any pencil meeting the hypotheses, its lift plane must be this
survivor, and its prescribed chart must retain the four explicit finite
directions below. This is a necessary-condition classification. It
neither excludes (199,565) nor constructs actual events or a t=0 equality
pencil. Selected-four-row gate exclusion stops with this survivor.
The global interval stays 11/q–16/q. All historical lists remain intact.
Same-step independent replay passes; the separate step-423 critical audit
below found no defect in this necessary classification.

## Proof

### Scope, sources and original-record binding

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-23-first-l140-mismatch-locus-review.md`.
This is RESEARCH / REPRODUCTION / calculation. It supplies new finite
record evidence and a limitation of the selected-row mechanism, without
claiming a discovery beyond checked sources. The scoped duplicate and
failure comparisons in that assessment are reused. ATTEMPTS/041–044
remain stopped for their recorded reasons; no cheap filter is repeated.

L109 supplies the necessary actual nonzero decomposable wedge and its
projection, weight and original-chart gates. L125 supplies original-record
provenance; L140 supplies the audited mismatch and its L138/L136 history.
L139 is only a method precedent: its kernel or homogeneous locus is not
imported. In particular the present free columns are 2,20 rather than
L139's 2,10, and its infinity behavior differs.

The precise standard coding inputs reused through L109 are J. I. Hall,
*Notes on Coding Theory*, undated GRS chapter,
[Theorem 5.1.1 and proof, pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and I. Marquez-Corbella–R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004,
[accepted manuscript 2016-02-29, section 5, Definitions 5.1–5.2 and
single-coordinate shortening formula after Lemma 5.3, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf).
The sixteen labels are distinct, multipliers nonzero, and k=8. Each row
shortens seven J-minus-K coordinates through positive dimensions eight
to one; the retained label-difference multipliers are nonzero. No stronger
MDS characterization is used.

Exterior bases and independent-wedge/subspace correspondence are covered
by K. Conrad, [*Exterior Powers*, Theorems 4.2, 7.1, 7.5 and proofs,
pp. 11–12,23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf),
undated 47-page author PDF inspected in the saved assessment. These
apply over every field, here in exterior degree two and dimension seven.
L109 supplies the explicit homogeneous criterion and pivot reconstruction.
Polynomial division/Bezout and extension-gcd invariance use J. S. Milne,
[*Fields and Galois Theory*, Kea Books 2022, sections 1.6–1.9,
pp. 5–7, and Proposition 2.17, p. 34](https://www.jmilne.org/math/Books/FT0.pdf).
Saved inspected-primary coverage is reused without fresh retrieval.
No general theorem is reproved: the specialization determines the new
record's coefficients and necessary row dispositions.

The original is `scripts/seven-coordinate/new-pair-filter/third-199.json`
at `/cases/167`, equal to `/overlay/8/complete_original_record` in
`scripts/seven-coordinate/l139-literal-reuse.json`. Both programs below
bind the source and overlay bytes by SHA256, compare the complete record,
regenerate the exact indexed supports, and check all six pair intersections.
They check the unmatched disposition, empty imported point/row bindings,
and source hashes against the passing checks in
`scripts/seven-coordinate/l140-critical-audit.json`. The complete overlay
and audit hash persist in the certificate. Originals are not rewritten.

### Complete original extension kernel

Write exterior coordinates in lexicographic order of increasing pairs
of S. The ordered basis of the full original kernel is

\[
\begin{split}
B_0&=E_1\wedge E_{18},\\
B_1&=(26,69,0,44,76,92,72,85,6,37,63,56,6,78,43,59,66,57,60,63,1).
\end{split}                                                    \tag{1}
\]

All 504 entries of the original 24-by-21 stack are saved. They are formed
directly from c_x=g_j(z_j)E_x^*−g_j(x)E_(z_j)^* and its six exterior
rows per block. Both vectors have all 24 residuals zero and give the
identity on free columns 2,20 (zero-based). The 19-by-19 minor uses rows
0,1,...,16,18,19 and all columns except 2,20. Its integer determinant is

\[
22184838231552325148529662157127680\equiv13\pmod {97}.       \tag{2}
\]

The producer verifies modular and fraction-free integer determinants;
independent rational elimination verifies (2), and independent column
elimination reconstructs the complete ordered null basis. The minor
gives rank at least nineteen and the two independent null vectors give
rank at most nineteen. These coefficient identities and the nonzero
minor persist under every scalar extension, so (1) spans the entire
extension kernel, not just its prime-field points.

### Entire homogeneous decomposable locus

For p=sB_0+tB_1 restrict all 35 Plucker equations
p_ab p_cd−p_ac p_bd+p_ad p_bc coefficientwise. Let
G(s,t)=t(16s+t). The only nonzero restrictions are:

| Quadruple | Restriction |
| --- | --- |
| (1,8,12,18) | 53G |
| (1,8,18,22) | 36G |
| (1,8,18,27) | 28G |
| (1,8,18,33) | 87G |
| (1,12,18,22) | 36G |
| (1,12,18,27) | 80G |
| (1,12,18,33) | 64G |
| (1,18,22,27) | 28G |
| (1,18,22,33) | 10G |
| (1,18,27,33) | 91G |

Every omitted coefficient triple is zero. On s=1 all equations are
divisible by t^2+16t, and the exact Bezout identity is
16*(t+91t^2)=16t+t^2 in F_97[t], using the last displayed row.
Thus their common affine zero set over any extension is exactly
t(t+16)=0. At s=0 the last equation is 91t^2, which is nonzero for
projective t!=0; infinity is excluded directly. The homogeneous ideal
is (G). Its two factors are distinct in characteristic 97, and the
complete projective locus is [1:0],[1:81]. There is no omitted nonsplit,
repeated-root or whole-line component.

For each point reconstruct with L109's first nonzero exterior pivot.
The resulting plane representatives, in increasing S, are

\[
\begin{array}{c|cc}
 &u_i&v_i\\\hline
L_0&(1,0,0,0,0,0,0)&(0,0,0,1,0,0,0)\\
L_*&(1,0,42,90,52,62,61)&(0,69,60,1,72,45,80).
\end{array}                                                     \tag{3}
\]

Their wedges are B_0 and B_0+81B_1 respectively. In particular B_1
itself is not decomposable; importing L139's infinity plane would fail.

### Necessary row gates, including the survivor

For every plane and row all six minors of (Q_j u_i,Q_j v_i) vanish,
while at least one component is nonzero. Thus all eight projections
have rank exactly one. For the first nonzero component n set
alpha=−(Q_j v_i)_n, beta=(Q_j u_i)_n and h=alpha u_i+beta v_i.
L109 then gives lambda=h_z/g_j(z), weights h_x−lambda*g_j(x) on I_j
and −lambda*g_j(x) on K_j. The g_j values on S union K_j are all
nonzero and retained in the certificate. Weights below are ordered as
increasing I_j then K_j.

| Plane | Row | (alpha,beta) | lambda | Four error weights |
| --- | ---: | --- | ---: | --- |
| L_0 | 1 | (53,0) | 0 | (53,0,0,0) |
| L_0 | 2 | (0,12) | 0 | (0,12,0,0) |
| L_0 | 3 | (71,0) | 0 | (71,0,0,0) |
| L_0 | 4 | (0,33) | 0 | (33,0,0,0) |
| L_* | 1 | (63,73) | 23 | (1,83,91,62) |
| L_* | 2 | (63,12) | 28 | (52,89,74,86) |
| L_* | 3 | (23,25) | 85 | (92,31,6,22) |
| L_* | 4 | (31,33) | 28 | (53,65,27,74) |

For all eight tests, extending h by zero off S and e by zero off the
row support gives h−e=lambda*g_j at every label of H. All 128 pointwise
entries and all 64 original shifted moments
sum_(x in H) x^d(h_x−e_x), d=1,...,8, vanish. L_0 fails L109's
necessary full-weight gate in each row. L_* passes all four intrinsic
weight gates. Rank zero would instead contradict actual nonpersistence
by L109; it does not occur in this record.

Independent replay checks every nonzero exterior pivot of both
decomposable tensors (22 choices total) and every nonzero component
of each corresponding row projection (346 tests total). Each recovered
intersection is a checked nonzero scalar multiple of the displayed one,
and lambda and every error weight scale by that same scalar. This
ensures the row classification is independent of pivot choice.

For an arbitrary prescribed basis write
u_original=A u_i+B v_i, v_original=C u_i+D v_i, Delta=AD−BC!=0.
The first coefficient of h in that basis is
(D alpha−C beta)/Delta. If its numerator vanishes the direction is
omitted; otherwise normalization divides h and all weights by this
nonzero coefficient. Accordingly L_0 cannot be repaired by a chart.
For L_* the four remaining necessary finite-direction gates are exactly

\[
63D-73C\ne0,\quad 63D-12C\ne0,\quad
23D-25C\ne0,\quad31D-33C\ne0.                              \tag{4}
\]

All finite-gate coefficients are saved and independently replayed.
No rationality of A,B,C,D or the prescribed omitted direction is assumed.
Thus every actual pencil under the hypotheses must use L_* and satisfy
(4). These calculations supply only its selected projective recovery
identities and necessary gates. They do not verify actual polynomial
nonpersistence, same-support badness, represented t=0, or sixteen events
for a newly constructed pencil. L109's r>=6 converse is not used on four
rows. No added-row census or chart replacement is performed.

### Reproduction, negative route evidence and limitations

Run with assertions enabled from this notebook:

    python3 -E -B scripts/seven-coordinate/first_l140_mismatch_locus_gates.py
    python3 -E -B scripts/seven-coordinate/verify_first_l140_mismatch_locus_gates.py

Full evidence is `scripts/seven-coordinate/first-l140-mismatch-locus-gates.json`
and `scripts/seven-coordinate/first-l140-mismatch-locus-gates-replay.json`.
The initial complete homogeneous extraction is preserved in
`scripts/seven-coordinate/first-l140-mismatch-homogeneous-initial.json`.
The first adapted producer stopped at an inherited no-survivor assertion;
that invalid expectation was removed before certification. The diagnostic
and correction are preserved in
`scripts/seven-coordinate/first-l140-mismatch-development-diagnostic.json`.
The completed evidence explicitly preserves the survivor, with zero
verification discrepancies.

The producer uses direct products for g_j and the inspected polynomial
and gate helpers. The independent verifier imports no producer or helper.
It generates H by powers of 8 and evaluates
g_j(x)=16*x^15/product_(y in (S union K_j) minus {x})(x−y)
on S union K_j, by differentiating X^16−1. Independent normalized ratio
covectors, rescaled by explicit nonzero factors, reproduce all original
entries. Column elimination and rational determinants independently
check the original complete kernel. Every homogeneous coefficient,
division/Bezout identity, infinity test, moment, weight, chart coefficient
and nonzero pivot is replayed. Both paths still share Python and modular
arithmetic; this is no separate critical audit or proof-assistant check.

This is informative negative evidence for excluding this occurrence by
the four selected rows: its complete necessary system retains L_*.
There is no indexed exclusion, third/pair assembly, reference sweep or
global bound improvement. Other kernels, universal representation and
extraction, and certified challenge definitions remain unresolved.

### Separate critical audit, 2026-10-23

Step `2026-10-23-mca-423-l141-critical-audit` completed the exact
invocation-start SPECIALIZE target in
`drafts/literature/2026-10-23-l141-critical-audit-review.md` as
RESEARCH / REPRODUCTION / proof_audit. The entire proof, both complete
programs and all called helpers were inspected. The helper modules
initialize constants without executing their historical searches.
L109's necessary nonzero-wedge/projection/weight/chart argument and its
separate audit, L125's original-kernel provenance/audit and L140's
provenance audit with L138/L136 history were checked. Reuse of the ready
primary assessment retains the precise citations, hypotheses and
finite-certificate qualifications above. No general theorem is reproved.

Reproduce this audit, with assertions enabled:

    python3 -E -B scripts/seven-coordinate/audit_l141.py

Full checks, execution output, input hashes, all row comparisons and all
pivot records are in `scripts/seven-coordinate/l141-critical-audit.json`.
All 431/431 checks pass with zero failures. Both complete programs run
in an isolated tree and reproduce both entire saved outputs byte for byte.
All nine copied files and all 23 bound originals remain byte unchanged.
No historical filter, new locus or added-row census is executed.

The original shard /cases/167 and audited overlay /8 bind to the exact
ordered occurrence (199,565). Independent four-subset generation confirms
the two support indices, and all historical 154/118/100/82/64/46 lists
remain intact. Direct product and derivative/normalized-ratio constructions
give the same 504 original stack entries. Column-relation elimination
independently recovers (1), including the identity on free columns 2,20;
rational determinant elimination verifies the full integer determinant
(2). The nonzero minor and two independent null vectors certify the
entire extension kernel, rather than just rational points.

All 35 homogeneous coefficient triples, every quotient and Bezout
coefficient agree with the displayed table and the initial extraction.
The nonzero last restriction is t(s+91t), equal to 91G. Multiplication
by 16 gives G, since 16*91=1 in F_97. Thus the ideal is precisely (G),
not merely a subset of its affine zero set. Its two factors give the
distinct finite points [1:0],[1:81]; at infinity 91t^2 is nonzero.
The complete coefficient calculation rules out nonsplit, repeated-root
and whole-line branches over every extension. No earlier st=0 locus
or infinity plane is imported.

Both wedges and displayed representatives agree, and all eight projection
ranks, directions, lambdas, error-weight tuples and finite-gate coefficient
pairs are replayed. All 128 pointwise identities and 64 shifted moments
vanish. All 22 nonzero exterior pivots and 346 nonzero projection-component
choices reproduce nonzero multiples of the same intersection lines,
lambdas and weights. No division by lambda or by a canceled error weight
is used. The four L_0 rows fail; all four L_* rows pass intrinsically.

For arbitrary extension-field A,B,C,D with Delta=AD-BC nonzero,
inversion of [[A,C],[B,D]] gives exactly
(D alpha-C beta)/Delta as the first coefficient of h. A zero coefficient
omits the direction; a nonzero coefficient rescales every weight by
the same nonzero factor. Hence L_0 remains rejected, and the survivor's
four necessary inequalities are exactly (4), without rationalizing or
replacing the original chart. L109's r>=6 converse is not applied to
these four rows. In particular the classification constructs no actual
nonpersistent pencil, same-support event, t=0 realization or equality.

The full initial homogeneous extraction and development diagnostic are
bound and preserved. The inherited assertion demanding no survivor was
invalid; the final producer calculates both complete components and
records their gates before counting survivors. The independent verifier
reconstructs their weights before checking the corrected one-survivor
expectation. No component or failed mathematical gate was suppressed to
obtain that count. ATTEMPTS/045's selected-four-row stop is confirmed.

No mathematical defect or changed direct dependency was found. This
establishes a separately reviewed local input, without a new indexed
exclusion or progress beyond checked sources. Shared Python/residue
arithmetic and inherited finite-certificate qualifications remain; this
is not proof-assistant verification. The verdict supersedes historical
pending-audit wording without changing the argument, PROOF.md or DAG.md.
Other kernels, universal representation/extraction and challenge definitions
remain open; the interval stays 11/q–16/q.

## Mathlib

Full matching theorem and supporting coverage were not checked in this
step. Unknown availability is not evidence of absence. The explicit
finite record and necessary-chart classification are justified above
and by the saved complete replay, with the stated computational limits.
