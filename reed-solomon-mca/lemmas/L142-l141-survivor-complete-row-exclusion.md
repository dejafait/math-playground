# L142 — Complete two-overlap capacity excludes L141's plane

## Hypotheses

Use F=F_(97^20), H={x in F_97^*:x^16=1}, k=8, L010's shifted
moments of orders one through eight and the pinned same-support event on
1/4<=delta<5/16. Assume sixteen actual original finite bad parameters,
actual nonzero Hankel determinant and coordinate-locator polynomials,
L104's represented t=0 class, and both coefficient syndromes in U_S for
S={1,8,12,18,22,27,33}. Retain L109's inherited
L010/L103/L104/L040/L069/L086/L056 finite-certificate qualifications.
Weights and the prescribed original chart are arbitrary over F.

Consider exactly L141's separately audited surviving lift plane L_*,
with basis, in increasing S order,

    u=(1,0,42,90,52,62,61), v=(0,69,60,1,72,45,80).

For the indexed application assume L141's four supports
{1,8,47,50}, {12,18,64,75}, {1,33,64,89}, {18,22,70,96}
are actual equality errors. Their ordered third/fourth indices are
(199,565). No universal seven-coordinate representation or fixed-pair
extraction is assumed.

## Conclusion

Among all 756 supports I union K with I a two-subset of S and K a
two-subset of J=H minus S, exactly four have rank-one projections on
L_* and all pass the intrinsic full-weight gates. The other 752 have
rank-two projections and no recovery. There are no rank-zero projections,
failed-weight rank-one rows or duplicate full directions. The complete
successful list is:

| I | K | (alpha,beta) | Normalized direction | lambda | Weights on increasing I then K |
| --- | --- | --- | --- | --- | --- |
| 1,8 | 47,50 | (63,73) | (1,92) | 23 | (1,83,91,62) |
| 12,18 | 64,75 | (63,12) | (1,51) | 28 | (52,89,74,86) |
| 1,33 | 64,89 | (23,25) | (1,77) | 85 | (92,31,6,22) |
| 18,22 | 70,96 | (31,33) | (1,48) | 28 | (53,65,27,74) |

Thus every prescribed original chart has at most four full finite
two-overlap directions, eight below L109's necessary twelve. L_* cannot
occur at equality. L141 already rejects the other exhaustive plane, so
the single ordered occurrence (199,565) is excluded. This excludes no
entire third or fixed pair and gives no global improvement to 11/q–16/q.
All historical lists remain preserved. Complete same-step independent
replay passes; the separate step-427 critical audit below found no defect
in this restricted exclusion.

## Proof

### Reused sources and exact binding

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-23-l141-survivor-capacity-review.md`.
This is RESEARCH / REPRODUCTION / calculation. L109 supplies the
necessary all-row projection/weight/chart criterion and the count
r=12+n_0>=12. L141 supplies this exact plane, its exhaustive other-point
rejection and its separate step-423 audit. L121/L123 are inspected method
precedents only; their counts on different planes are not imported.
The new programs are necessary to certify this record's finite count,
which no checked source supplies. No new general theorem or progress
beyond checked sources is claimed.

Standard inputs reused through L109 and L141 are J. I. Hall,
*Notes on Coding Theory*, undated GRS chapter,
[Theorem 5.1.1 and proof, pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf);
I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004,
[accepted manuscript 2016-02-29, section 5, Definitions 5.1–5.2 and
GRS shortening formula after Lemma 5.3, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf);
and K. Conrad, [*Exterior Powers*, Theorems 4.2, 7.1, 7.5 and proofs,
pp. 11–12,23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf),
undated 47-page author PDF. The ready assessment's inspected primary
coverage is reused. Sixteen labels are distinct and multipliers nonzero.
Each row shortens exactly seven labels J minus K, reducing dimension
eight to one through positive dimensions and nonzero label differences.
The exterior degree is two in dimension seven over a field. These
unchanged hypotheses require no standard-theorem reproof.

Both programs check all 431 successful L141 audit checks, its two
successful isolated executions, its unchanged-originals assertion and
the audit program hash. Every one of its 23 bound input hashes is
rechecked, including its full classification/replay programs and helper
files, both classification certificates, original shard
`new-pair-filter/third-199.json` at `/cases/167`, L140's audited overlay
in `l139-literal-reuse.json` at `/overlay/8`, L125/L140/L138/L136 audit
provenance, initial homogeneous extraction and development diagnostic.
Paths in this paragraph are relative to `scripts/seven-coordinate/`.
All 25 inputs including the audit certificate/program are bound before
and after the calculation. No original is rewritten.

The source's only intrinsically passing point must have exactly the
displayed u,v. The ordered occurrence, source/overlay pointers and the
two exhaustive point dispositions are checked. All four source rows
are regressions: their raw directions, lambdas, weights and prescribed
finite-gate coefficients match the new calculation entrywise. This
binding imports L141's classification, not a four-row converse.

### Complete quotient census

Enumerate all 21 increasing I pairs and all 36 increasing K pairs,
I outermost, without incidence filters. For each set
g_K(X)=product_(y in J minus K)(X-y), z=min(S minus I), and use
the four covectors c_x(w)=g_K(z)w_x-g_K(x)w_z for
x in S minus (I union {z}). Save Q, Qu, Qv, all six two-by-two
projection minors, all sixteen g_K values and the projection rank.
Every g_K value on S union K is nonzero by distinctness.

A nonzero projection minor proves rank two and no nonzero direction
in L_* intersect ker Q. When all minors vanish but some entry is
nonzero, the projection has rank one. For a nonzero component m put
(alpha,beta)=(-(Qv)_m,(Qu)_m) and h=alpha*u+beta*v. Then h is nonzero,
Qh=0 and its line is the whole intersection. Recover

    lambda=h_z/g_K(z),
    e_i=h_i-lambda*g_K(i) for i in I,
    e_k=-lambda*g_K(k) for k in K.

Retain lambda zero and either canceled overlap weight as explicit failed
gates; no division by them occurs. Extend h by zero off S and e by zero
off I union K. Save and check all sixteen identities h-e=lambda*g_K
on H and all eight shifted moments sum_(x in H)(h_x-e_x)x^d=0.
A rank-zero branch is also retained explicitly: L109 shows that the
whole plane would have representatives on this four-support, forcing
persistent actual locators, even with deficient weights. It cannot be
silently treated as an optional failed row.

The complete census gives rank two at 752 rows, rank one at exactly
the four displayed rows, and no rank zero. All four rank-one rows have
nonzero lambda and all four weights nonzero. Grouping successes by
normalized projective (alpha,beta) gives four singleton groups and
no duplicates. These are the only possible two-overlap directions
before any prescribed-chart deletion.

### Independent original-moment verification and extension completeness

Reproduce from the notebook, with assertions enabled:

    python3 -E -B scripts/seven-coordinate/l141_survivor_full_rows.py
    python3 -E -B scripts/seven-coordinate/verify_l141_survivor_full_rows.py

The complete outputs are
`scripts/seven-coordinate/l141-survivor-full-rows.json` and
`scripts/seven-coordinate/l141-survivor-full-rows-replay.json`.
Both finish with zero failures and zero unresolved branches. No failed
development run or mathematical exception occurred during this census.

The verifier imports neither producer nor producer helpers. It generates
H by powers of eight, checks the entire ordered universe of 756 distinct
supports, and reconstructs g_K by polynomial coefficient multiplication
and Horner evaluation rather than direct evaluation products. Every
saved quotient entry, projection, minor and disposition agrees.

For every support, including all 752 rejections, it independently forms
the original eight-by-six homogeneous moment matrix in variables
(alpha,beta,e_i1,e_i2,e_k1,e_k2), with row d=1,...,8

    (sum_(x in S)u_x*x^d, sum_(x in S)v_x*x^d,
     -i1^d,-i2^d,-k1^d,-k2^d).

Reverse-column-pivot Gauss–Jordan elimination saves the entire reduced
matrix R, pivot columns and nonzero pivot values, the eight-by-eight
left multiplier E, and every null-basis vector. It checks E*M=R,
identity pivot columns, zero remaining rows, original-matrix residuals
of every null vector, and identity free coordinates of those vectors.
Independent exact integer Bareiss elimination, checking every division,
computes det(E) with nonzero residue modulo 97 at every row. A saved
four-by-four minor using the first four moment rows and the error columns
also has nonzero determinant, excluding pure-error nonzero kernels.
Thus each saved basis is complete, of dimension six minus rank.

The original ranks are six on exactly 752 rows and five on exactly
four, equal to quotient rank plus four. Every rejection has zero kernel.
Each remaining kernel is one line, agreeing up to a single nonzero
scale with all six quotient recovery coefficients. All lambdas, weights,
sixteen pointwise identities, eight moments and chart coefficients agree.
The replay checks every nonzero projection component in the fixed basis
(16 records), with directions, lambdas and weights scaling together.
It additionally reconstructs the plane at every nonzero exterior pivot,
verifies its full wedge, and checks every nonzero projection component
there (336 complete records), including nonzero proportionality of h,
lambda and all weights to the displayed recovery.

All entries and nonzero determinants are in F_97. Hence E remains
invertible over every extension, the full ranks persist and each complete
kernel only extends scalars. No extension can add a rejected support
or a second projective recovery at a rank-five support. The complete
four-direction count is therefore valid over F_(97^20), indeed over
every extension. This is exact linear algebra, not sampling prime-field
points. Shared Python, modular arithmetic and the moment convention
remain computational qualifications; no separate audit or formal
verification is claimed in this step.

### Prescribed chart, indexed application and limits

For arbitrary extension-field A,B,C,D with Delta=AD-BC nonzero, write
u_original=A*u+B*v and v_original=C*u+D*v. L141's audited inversion
gives alpha_original=(D*alpha-C*beta)/Delta. If its numerator vanishes,
the direction is omitted. Otherwise normalization divides h, lambda
and every error weight by this same nonzero coefficient. All four
necessary finite gates remain explicit:

    63D-73C!=0, 63D-12C!=0, 23D-25C!=0, 31D-33C!=0.

An invertible basis change preserves distinct projective directions;
deleting the omitted one can only lower their number. Thus any
prescribed chart has at most four full finite directions. L109 requires
at least twelve actual distinct finite two-overlap directions at t=0
equality. The shortfall excludes L_*. Under the four actual-support
hypotheses L141 forces either L_* or its already rejected lambda-zero
plane, so the single occurrence (199,565) is excluded.

This completes only the approved one-plane test. ATTEMPTS/045's failure
of selected-four-row exclusion remains valid: this argument uses all
756 supports and a separate necessary capacity threshold. Every
historical 154/118/100/82/64/46 list and exchanged-row occurrence stays
unchanged. No third/pair assembly, sufficient-filter reopening, other
kernel classification, actual-event construction, nonpersistence
construction or L109 r>=6 converse is used. Universal representation,
extraction, other kernels and certified challenge definitions remain
open. The global interval stays 11/q–16/q and STATUS stays IN_PROGRESS.

### Separate critical audit, 2026-10-23

Step `2026-10-23-mca-427-l142-critical-audit` completed the exact
invocation-start SPECIALIZE target in
`drafts/literature/2026-10-23-l142-critical-audit-review.md` as
RESEARCH / REPRODUCTION / proof_audit. The complete proof, both complete
programs and every called helper were inspected. The two programs use
only standard-library imports and contain their mathematical helpers
locally. L109's necessary count, projection/weight/chart proof and prior
audit, and L141's full classification and separate step-423 audit were
checked. The ready primary source assessment and the precise imported
hypotheses above are reused; no new standard theorem is reproved.

Reproduce this audit with assertions enabled:

    python3 -E -B scripts/seven-coordinate/audit_l142.py

The complete evidence is `scripts/seven-coordinate/l142-critical-audit.json`.
All 4,363/4,363 checks pass with zero failures. Both original programs
execute in an isolated notebook-shaped tree, preserving the inherited
relative paths, and reproduce both entire saved outputs byte for byte.
All 30 bound originals, including every one of the 25 inherited inputs,
remain unchanged. The complete original shard /cases/167, overlay /8,
L141 classification/audit, initial extraction and diagnostic retain their
bindings. All historical 154/118/100/82/64/46 lists remain intact.

An independent generation of four-subsets of H with intersection size
two with S agrees with the entire ordered 756-row universe. For every
row the audit reconstructs the eight-by-six original moment matrix and
all quotient entries. It checks E*M=R entrywise, the identity pivot
columns and zero remaining rows, and the complete null basis through
its original residuals and identity free coordinates. Rational Gaussian
elimination, independently of the verifier's Bareiss method, reproduces
each full integer determinant of E and each error-column minor. Every
determinant residue is nonzero. Thus the certificates prove ranks six
on 752 rows and five on four, and complete extension kernels of dimensions
zero and one respectively. This is not inference from base-field sampling.

All four nonzero recovery lines, all sixteen pointwise identities and
eight original moments per recovery, all weight and prescribed-chart
coefficients agree. All sixteen nonzero fixed-basis projection pivots
and all 336 exterior/projection pivot records are checked completely;
every changed representative has the same nonzero scaling factor for
its lift, lambda and four weights. All four successful direction groups
are distinct singletons. There are no rank-zero branches, failed-weight
rows or duplicate directions. The four selected rows agree entrywise
with L141's audited survivor gates.

The field-extension conclusion uses invertibility of the saved E and
the complete RREF/kernel identities over F_97. These identities persist
under scalar extension; no rejected row can acquire a kernel and no
accepted row can acquire another projective direction. For any original
basis, inversion of [[A,C],[B,D]] gives the first coefficient
(D alpha-C beta)/(AD-BC), with nonzero determinant. Its vanishing omits
the direction; otherwise all weights are divided by the same nonzero
coefficient. Consequently an arbitrary extension-field chart can only
delete directions from the four already counted, not create new ones.

L109's necessary equality argument first establishes independent lift
coefficients and full activity, then gives 2n_0+n_1=4 and r=12+n_0>=12
actual distinct two-overlap directions. This threshold applies under the
stated represented t=0 hypotheses, including actual nonpersistence. Four
is eight below twelve before any chart deletion, excluding L_* in every
prescribed chart. L141's complete homogeneous locus is precisely
t(16s+t)=0, with two finite points and no point at infinity. Its other
point has lambda zero on all four selected rows, as confirmed by its
unchanged audited evidence. Therefore these two exhaustive alternatives
exclude exactly the ordered occurrence (199,565) under its actual-support
hypotheses. The four-success converse is neither needed nor invoked.

No mathematical defect or changed direct dependency was found. This is
a separately reviewed local reproduced input, not a new result beyond
the checked sources or an improvement to the global interval. The finite
certificates, shared Python/residue arithmetic and inherited audited
inputs remain qualifications; this is not proof-assistant verification.
ATTEMPTS/045's four-selected-row stop remains valid because the exclusion
uses complete additional-row capacity. No new support family, kernel
classification, event construction or third/pair assembly was performed.
This verdict supersedes historical pending-audit wording without changing
the argument, PROOF.md or DAG.md. Universal representation/extraction,
other residuals and challenge definitions remain unresolved.

## Mathlib

Full matching coverage of this record-specific census and supporting
finite-field linear algebra was not checked, and is not asserted absent.
The standard coding/exterior inputs are imported with the precise
citations and unchanged hypotheses above. The complete certificates
are explicit computational proof inputs, now separately audited with
the qualifications above.
