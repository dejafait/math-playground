# Complementary ternary-coordinate ancestors: completed scope assessment

TARGET: Test whether a complementary ternary-coordinate ancestor certificate excludes a nonempty subfamily of least-root candidates with v_3(4n+1)=3, keeping positive-integer guards and every size comparison against the original root.
CHECKED: 2026-10-04
DECISION: IMPORT
SEARCH_EVIDENCE: Seven exact-statement, terminology and stronger-result queries were executed on 2026-10-04; the direct lead was read in full and its essential tail-table and inverse-word references were checked using the ready prior assessment; queries and reuse limits appear below.
SOURCE_EVIDENCE: Read Sodelin, Complementary_Ancestor_Cylinders.md, node B-SECOND-TERNARY-ANCESTOR-001, live main, all 99 web lines, https://raw.githubusercontent.com/Sodelin/Collatz-Conjecture-Work/main/proof-search/lemmas/Complementary_Ancestor_Cylinders.md; reread the refined finite tail table, sections 1–3, and general inverse-word semantics, sections 1–5; reused the previously read retained-branch proof.
COMPARISON: Exact partial coverage is available outside L016's lower-row scope; the original least root and shortcut map match, while whole-class termination remains uncovered.
GAP: The mathematical citation applications are still to be performed; even after them, universal convergence or eventual descent on the complementary infinite domain remains missing.
REASON: Resolve the saved essential unread source before calculation, then reuse the matching theorem rather than reconstructing its selector or claiming a result beyond the checked literature.
SCOPE: Positive shortcut roots in residue 20 modulo 27, the cited complementary-coordinate guard and two stated cylinders, with every size comparison against the original root; no broader return or termination claim is approved.
COVERED_TARGET: Apply by citation the complementary ternary-coordinate ancestor theorem to a least nonconvergent residue-20 root n with v_3(4n+1)=3, recording the necessary bound v_3(128n-157)<=16 and checking positive-integer guards and convergence transfer against the original root.
COVERED_TARGET: Apply by citation the two inspected complementary ancestor cylinders to exclude n=4529+19683s and n=17813+59049s, s>=0, as least nonconvergent residue-20 roots, retaining positive-integer guards and comparing each ancestor with the original root.

## Hypotheses

Use the positive shortcut map and fixed least-root conventions in
foundations/01-target-and-scope.md and L014. This assessment preserves
the saved TARGET exactly. It began as REVIEW_REQUIRED because the
complementary-coordinate source was unread and outside the prior scope.
No nonconvergent start is assumed to exist unconditionally.

## Conclusion

The source comparison passes the requested nonempty-subfamily test.
The two listed citation applications are ready for separate RESEARCH
steps. This is EXPLORATION of previously missing coverage, classified
KNOWN_IMPORTED; no new least-root exclusion is derived in this turn.

## Proof

This section records inspected source statements and their applicability,
not a new mathematical proof.

Sodelin, *Complementary ancestor cylinders and a second ternary-depth
coordinate*, node `B-SECOND-TERNARY-ANCESTOR-001`,
[“A uniform family with unbounded new ternary depth,” web lines 30–63](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Complementary_Ancestor_Cylinders.md#a-uniform-family-with-unbounded-new-ternary-depth),
states that positive r=20 modulo 27 with v_3(128r-157)>=17 has positive
integral m=20 modulo 27, m<r, and T^b(m)=r. The source locates this
family inside v_3(r+7)=4 and v_3(4r+1)=3. Its proof checks a guarded
variable inverse prefix, reuses the exhaustive refined tails, and bounds
the root-relative slope by 768(2/3)^v with negative intercept. The
source's threshold comparison is 768*2^17<3^17. Its valuation-16
selected-endpoint failure limits that selector, not every certificate.

The [preceding section, web lines 9–29](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Complementary_Ancestor_Cylinders.md#two-elementary-infinite-families-missed-by-the-original-selector)
gives two additional all-parameter certificates:

| r, for s>=0 | m | Forward time |
|---|---|---:|
| 4529+19683s | 3179+13824s | 9 |
| 17813+59049s | 16679+55296s | 11 |

Its guard-propagation proof was read. The statement includes positivity,
target membership, strict order and the actual forward identity.
These are named partial conclusions, not exhaustive residual coverage.

### Supporting sources and reuse

Reread *Refined tail certificates lower the uniform ancestor cutoff to
valuation 13*, node `B-RESIDUE20-VALUATION13-ANCESTOR-2026-09-05`,
[sections 1–3](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Residue20_Refined_Ancestor.md#1-common-prefix-and-the-retained-five-branches),
including the retained rows and all five refined guards. Read the
inverse-word map, admissibility and forward-orientation statements in
[*L4 — General inverse-word coalescence semantics*, sections 1–5](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/L4_General_Inverse_Word_Coalescence.md#1-accelerated-collatz-map),
dated 2026-08-23. These supply supporting semantics, not the full new
coordinate theorem by themselves.

Reuse the complete retained-branch proof comparison in the
[prior assessment](2026-10-03-residue20-residual-ancestor-selector.md),
including *Residue20_Valuation_Ancestor.md*, sections 1–4, and the
adequate Rozier and Monks comparisons cited there. No relevant guard or
map change was found. The essential references are covered; no general
inverse-word reproof or repeated published-literature survey is needed.

Provenance: these Markdown notes were read from live `main` on
2026-10-04. The main note has no explicit date or immutable revision
in its header. Its supporting raw views have 239 and 291 web lines.
A read-only GitHub commit-metadata request failed at network resolution;
no commit hash was obtained. The theorem bodies are accessible through
the browser, so this is not SOURCE_BLOCKED. The main note's verification
paragraph separates prose from finite replay and says the new selector
is not Lean formalized. No checker or Lean build was run locally.

### Relevance, comparison and discriminating test

The main gap is universal eventual descent or convergence. The achieved
L014/L016 restrictions leave valuation 3 unexcluded. The inspected
partial coverage therefore addresses a real remaining domain rather
than duplicating the old coordinate's rows. The threshold sought here
is an actual smaller positive allowed ancestor of the original root,
with readable guards and a finite shortcut identity; the cited
statements match that threshold.

The downstream use is a further necessary restriction on a hypothetical
least bad root. Applying the citations, including convergence transfer
if an ancestor hits 1 before its specified root hit, is deferred. Use
L014's fixed-root argument, not a comparison with a larger later return.
Reject an application if any positive-integer, map, residue or strict
original-root guard fails; do not drop the guard or extrapolate finite
replay. Even a successful application leaves other roots and their
transition behavior unresolved.

Attempts 009 and 010 remain parked/stopped. Neither the exhausted paired
invariant search nor the obstructed strict first-return bridge is
reopened. Later finite-spell, bounded-cover and recharge papers linked
from the source are discovery leads only: their proofs were not read
and none is an essential input to the two approved applications. Broader
claimed Collatz resolutions in search hits were not assessed. No
originality claim follows from this bounded search.

Queries executed:

- `Collatz "complementary" "ancestor" "valuation"`
- `Collatz "4n+1" "3" "ancestor"`
- `"Complementary_Ancestor_Cylinders"`
- `Collatz "128r" "157" ancestor`
- `Collatz "4529" "3179"`
- `Collatz "17813" "16679"`
- `Collatz "smaller" "ancestor" "20" "27" theorem`

The [primary target page](https://mathprize.net/posts/collatz-conjecture/),
dated 2021-07-07, was rechecked; its all-positive-integer statement
matches local GOAL.md. Prize terms are not mathematical inputs.
This review spends no mathematical exploration turn and resets no
counter. No lemma, mathematical script or complete candidate was added.

## Mathlib

Full complementary-coordinate ancestor theorem, the two cylinders, and
supporting valuation/congruence/iteration coverage: **not checked**.
No library absence or matching Mathlib declaration is asserted. The
public `CollatzWork.residueAncestor_of_divisibility` declaration linked
in the prior assessment concerns the old uniform coordinate; it does
not establish formal coverage of this new statement.
