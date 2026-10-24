# L145 — Literal L144 import excludes occurrence (239,647)

## Hypotheses

Use F=F_(97^20), H={x in F_97^*:x^16=1}, k=8, shifted moments
of orders one through eight, and the pinned same-support event on
1/4<=delta<5/16. Assume sixteen actual original finite events,
L104's represented t=0 class with coefficient syndromes in U_S for
S={1,8,12,18,22,27,33}, and actual nonzero Hankel determinant and
coordinate-locator polynomials. Original coefficients, weights and
prescribed charts are arbitrary over F. Retain L109's inherited
finite-certificate qualifications.

The assumed actual supports, in order, are
{1,8,47,50}, {12,18,64,75}, {8,12,70,85}, {18,33,89,96}.
Use L109's original covectors, z=min(S minus I), and increasing exterior
coordinates. In L125's full zero-based lexicographic universe these are
occurrence (239,647), original `scripts/seven-coordinate/new-pair-filter/third-239.json`
at `/cases/182` and L143's audited
`scripts/seven-coordinate/l141-l142-literal-reuse.json` at `/overlay/1`.
No universal representation or fixed-pair extraction is assumed.

## Conclusion

This one indexed occurrence cannot belong to the hypothesized equality
pencil in any prescribed original chart. Its original stack has rank
nineteen and exactly the complete ordered kernel of separately audited
L144. Both exhaustive decomposable points, including infinity, import
L144's unchanged second-row lambda-zero rejection.

This is a restricted reproduction, not a result beyond the checked
sources. Same-step independent replay and the separate step-439 critical
audit below pass. Historical 154/44 lists are unchanged. No third/pair
assembly, event construction or global improvement follows.

## Proof

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-23-l144-single-record-reuse-review.md`.
Its exact-statement, stronger-result and duplicate comparisons are reused.
ATTEMPTS/045–046 remain valid: the exhausted L141/L142 sweep is not
reopened. No new locus, basis conversion or changed-row gate is derived.

Through L109 and L144 import J. I. Hall, *Notes on Coding Theory*,
[Theorem 5.1.1 and proof, pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and I. Marquez-Corbella–R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004,
[accepted manuscript 2016-02-29, section 5, Definitions 5.1–5.2 and
formula after Lemma 5.3, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf).
The labels are distinct, multipliers nonzero, and each seven-coordinate
shortening passes through positive dimensions eight to one. No stronger
parameter assertion of Lemma 5.3 is used. K. Conrad,
[*Exterior Powers*, Theorems 4.2/7.1/7.5 and proofs,
pp. 11–12,23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf),
covers ordered bases and independent wedges in dimension seven over all
fields. J. S. Milne, [*Fields and Galois Theory*, Kea Books 2022,
sections 1.6–1.9, pp. 5–7, Proposition 2.17, p. 34](https://www.jmilne.org/math/Books/FT0.pdf),
covers the extension-invariant division/Bezout tools already applied in
L144. These tools are imported; the new work is their exact finite binding.

Reproduce from this notebook with assertions enabled:

    python3 -E -B scripts/seven-coordinate/l144_single_record_reuse.py
    python3 -E -B scripts/seven-coordinate/verify_l144_single_record_reuse.py

The complete certificates are `scripts/seven-coordinate/l144-single-record-reuse.json`
and `scripts/seven-coordinate/l144-single-record-reuse-replay.json`.
The original shard is hash-bound to L125's passing audit and L143's
passing audit. The entire original record equals overlay/1, not just its
basis. The L144 source, replay and all inputs in its step-435 audit
manifest are byte-bound before importing any subresult. The four original
supports are distinct and pairwise linear; the full universe fixes their
indices without quotienting row exchanges.

For each row construct g_K(X)=product_(y in J minus K)(X-y),
c_x=g_K(z)E_x^*−g_K(x)E_z^* for x in (S minus I) minus {z},
and the six pairwise exterior covectors. Rebuild all 504 entries of the
original 24-by-21 stack, including the changed third row. Column elimination
gives exactly the saved two ordered vectors and all 48 null residuals zero.
The original minor with zero-based rows

    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,21

and columns all except 7,14 has determinant 73 modulo 97, freshly computed
on this stack. This is not L144's residue 84. The two vectors have identity
coordinates on free columns 7,14. Thus rank is at least nineteen by the
minor and at most nineteen by two independent null vectors. Their span
is the entire kernel after any scalar extension.

Independent replay constructs g_K(x) on S union K as
16*x^15/product_(y in (S union K) minus {x})(x-y), using the derivative
of X^16−1 at x. Every denominator and g_K value is nonzero. Normalized
ratio covectors are scaled back to the original convention, reproducing
all 504 entries. Row elimination independently gives both complete
ordered vectors, and row-pivoted determinant evaluation gives residue 73.
The producer uses column elimination and a column-pivoted determinant.

In the same increasing exterior convention the entire ordered basis is
literally L144's:

    B0 = e_8 wedge e_18,
    B1 = 15 e_1 wedge e_12 + 84 e_8 wedge e_12
         + 73 e_12 wedge e_18 + 63 e_12 wedge e_22
         + 62 e_12 wedge e_27 + e_12 wedge e_33.

Only after this equality import L144's complete homogeneous locus
s*t=0, including its coefficient/division/Bezout certificates and direct
infinity inclusion. It has exactly [1:0] and [0:1] over every extension.
No assertion about another kernel's locus is needed.

The second row is unchanged in I,K,z, the entire polynomial g_K,
all values, covectors and original block. Its I={12,18}, K={64,75}, z=1,
and ascending g_K coefficients are [75,10,43,58,96,17,66,1].
Both plane representatives are exactly L144's representatives, so the
entire second-row gate records import unchanged:

| Point | (alpha,beta) | lambda | Weights in order 12,18,64,75 |
| --- | --- | --- | --- |
| [1:0] | (0,75) | 0 | (0,75,0,0) |
| [0:1] | (0,44) | 0 | (78,0,0,0) |

Each projection has rank exactly one. The complete input, representative,
gate, original-moment record and all nonzero exterior/projection-pivot
records are saved for each point and compared to the audited source.
Independent replay recomputes both projections and all six zero minors,
directions, intersection vectors, lambda, four weights and failed gates.
All 16 original shifted moments and all 32 pointwise entries vanish.
All 25 second-row projection-component choices across the seven nonzero
exterior pivots are replayed, with nonzero proportionality factors.
Thus an alternative pivot cannot remove the zero outside weights.

For u_original=A*u+B*v and v_original=C*u+D*v, with AD−BC nonzero,
the first original coefficient of the intersection vector is
(D*alpha−C*beta)/(AD−BC), as in audited L144. Its zero case omits the
direction. Otherwise normalization divides every weight by this same
nonzero coefficient; lambda and the two outside weights stay zero.
This includes arbitrary nonrational prescribed charts. No changed-third-row
gate or full four-row converse is required.

By L109's necessary direction an actual equality pencil supplies an
independent nonzero wedge in this entire kernel and must pass the rank-one
and full-weight gates at every actual selected row. Both exhaustive points
fail row two, a contradiction. This excludes only (239,647).

All checks pass with zero failures. The programs share Python and residue
arithmetic; same-step independent replay is not a separate critical audit
or proof-assistant verification. No historical list is shortened, no
other occurrence is tested, and universal representation/extraction and
challenge-definition qualifications remain unresolved. The global interval
stays 11/q–16/q.

### Separate critical audit, 2026-10-24

Step `2026-10-24-mca-439-l145-critical-audit` used the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-24-l145-critical-audit-review.md`.
The complete proof and both complete programs, every called helper and
all import initialization were inspected. L109's necessary independence,
projection, full-weight and prescribed-chart proof and audit were checked;
L125's original-kernel certification, L143's original-record binding and
L144's complete locus and gate audit were reused with their qualifications.
No mathematical defect or changed direct dependency was found. This
validates the existing restricted reproduction, without progress beyond
the sources checked.

Reproduce with assertions enabled:

    python3 -E -B scripts/seven-coordinate/audit_l145.py

The full report is `scripts/seven-coordinate/l145-critical-audit.json`.
All 124/124 checks pass with zero failures. Both entire outputs reproduce
byte for byte in an isolated notebook-shaped tree; all 25 bound originals
remain unchanged. Only the two L145 programs execute. Imported historical
main routines are guarded, and no filter, reference sweep, other occurrence
or support census runs. Complete evidence is checked, not summary previews.

The entire L125/L143 audit manifests are hash-bound, their verdicts checked,
and their selected original/master/helper/overlay hashes verified. Every
input in L144's fourteen-file audit manifest is also bound. The complete
original third-239 `/cases/182` equals L143 `/overlay/1`, with full-universe
indexing and all four exact supports checked independently. Product and
derivative reconstruction agree on all 504 original entries, including
the changed third row. Column and row elimination give the same two entire
ordered null vectors. Their free coordinates 7,14 form the identity and
all 48 original residuals vanish. Additional exact rational elimination
gives original minor determinant

    -58305165420515507527311966579720192

whose residue is 73 modulo 97. Thus the nonzero minor and two independent
null vectors certify rank nineteen and the entire extension kernel. The
same ordered exterior convention is checked before literal equality with
L144 imports its complete homogeneous coefficient/division/Bezout evidence
and both points, including infinity. No other kernel's locus is imported.

For both exhaustive points the full unchanged second-row input, polynomial,
values, covectors, original block, representative, rejecting gate and
original-moment replay bind exactly to audited L144. Independent replay
reconstructs rank one, the direction and all weights: (0,75,0,0) and
(78,0,0,0), respectively, each with lambda zero. All sixteen shifted
moments, thirty-two pointwise entries and twenty-five alternative
projection-component records across the seven nonzero exterior pivots
are checked. Every proportionality factor is nonzero. Label differences,
g-values, elimination pivots and selected nonzero components justify each
division; no failed full-weight gate is discarded.

For arbitrary extension-field prescribed charts, solving the invertible
two-by-two basis change gives (D*alpha-C*beta)/(AD-BC) as the first
coefficient. Its zero case omits the direction. Otherwise all error
weights are divided by this nonzero coefficient, retaining their zeros.
This is an algebraic statement for every chart, not a finite chart test.
L109 supplies the actual independent nonzero wedge before the exhaustive
locus and necessary full-weight gates are used. Both possible planes fail
row two; no changed-third-row gate or r>=6 converse is needed.

Shared Python/residue arithmetic and inherited finite certificates remain
qualifications; no proof-assistant verification is claimed. Historical
154/44 lists and ATTEMPTS/045–046 persist. No third/pair assembly, universal
representation/extraction or global bound follows. This section supersedes
historical pending-audit wording in the unchanged overview and certificates;
the argument and DAG inputs are unchanged.

## Mathlib

Full matching and supporting coverage were not checked; unknown availability
is not evidence of absence. This result uses the cited standard tools,
audited local inputs and explicit complete finite certificates above.
