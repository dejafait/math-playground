# L131 — The third-59 actual seed is excluded at represented t=0 equality

## Hypotheses

Let F=F_(97^20), H={x in F_97^*:x^16=1}, C=RS[F,H,8], and
S={1,8,12,18,22,27,33}, J=H minus S. Use L010's shifted moments
and the pinned same-support bad event on 1/4<=delta<5/16. Fix original
words a,b over F. Their actual Hankel determinant D and every actual
coordinate locator are nonzero polynomials. Both coefficient syndromes
belong to U_S, with unique lift f(T)=u+Tv supported on S. Assume sixteen
distinct original finite bad parameters and L104's represented t=0:
no actual error equals f at its parameter. Original weights and the
prescribed affine chart are arbitrary over F.

Retain the hypotheses and finite-certificate qualifications of L086/L109,
including L040/L069 through L103/L104 and L086's L056 counting inputs.
The following three supports are actual errors of this same pencil:

| Row | I subset S | K subset J | Support |
| --- | --- | --- | --- |
| 1 | {1,8} | {47,50} | {1,8,47,50} |
| 2 | {12,18} | {64,75} | {12,18,64,75} |
| 3 | {1,12} | {70,85} | {1,12,70,85} |

No universal representation on S or extraction of this seed is assumed.

## Conclusion

These hypotheses are inconsistent. This excludes exactly the displayed
actual three-support seed in the stated represented t=0 equality class.
The full fourth-domain comparison passes, and the separate step-382
critical audit below found no defect. It excludes neither the fixed pair nor other
thirds, and supplies no universal representation/extraction or global
improvement. All 154 historical L125 residuals remain preserved. The
global interval stays 11/q–16/q and challenge-definition gaps remain.

This is REPRODUCTION of assessed tools and audited restricted inputs,
with local assembly progress only; no result beyond the checked general
literature or complete challenge candidate is claimed.

## Proof

### Complete domain and audited partition binding

Use L125's full lexicographic universe
U=binom(S,2) times binom(J,2), with increasing pairs, S-pair first.
Each two-overlap four-support has exactly one such representation.
There are 21*36=756 rows. The three displayed supports have zero-based
indices 0,412,59. They are distinct with pairwise intersection sizes
0,1,1. A fourth index d is eligible precisely when it differs from
these three and its support meets each in at most one label. Thus
this is L125's exact ordered domain at third 59, without a disjoint-third
condition, row-exchange quotient or historical deletion.

Reproduce the complete comparison from this notebook:

    python3 -B scripts/seven-coordinate/assemble_third59.py

The full certificate is `scripts/seven-coordinate/third59-assembly.json`.
The comparison imports only Python's standard library. It reconstructs
H by x^16=1 modulo 97, S, J, all 756 rows and every fourth-screen entry,
including all ineligible entries. The entire screen equals the saved
`scripts/seven-coordinate/new-pair-filter/third-059.json`. This shard has
SHA256 `df53d2429ea83f9c85777da586b1b89be4005f11ad6f8d36ca4edae7025415cb`.
The complete increasing eligible list equals the shard's entire case
list, with exactly 282 distinct fourths and no missing or repeated index.

The unique matching master and complete-replay manifest entries have
this exact shard path and hash. The shard and eight common source files
match L125's separate step-358 audit manifest. The audit program and
complete replay log also match their recorded hashes; its full success,
unchanged-input and identical-replay fields pass. The master, replay and
audit summaries agree, and the replay binds the exact master hash.
No other shard is read and no new partition is computed.

For each eligible case the saved basis has dimension 21-rank, with 21
entries per vector and nonzero original maximal-minor residue. The
comparison recomputes every complete-basis factor and omission predicate
and every recorded failed-coefficient witness: all eight selected-row
factor choices and all seven coordinate choices when rank is deficient.
Rank-21 cases have empty bases and empty predicate lists. These priority
dispositions agree with the audited records:

| L125 disposition at third 59 | Fourths |
| --- | ---: |
| Rank 21 | 96 |
| Whole-kernel selected-row factor | 175 |
| Coordinate omission after neither preceding filter | 9 |
| Residual | 2 |

Their sum is 282. The complete residual list is [355,647], equal to the
shard list and the matching entries of the unchanged master residual
list. L125 therefore excludes the first 280 cases under the present
hypotheses. Its complete original-matrix rank and kernel proofs and
separate audit are imported, not replaced by basis-size inspection here.
Its factor exclusion uses actual nonpersistence and necessary full weights;
its omission exclusion uses L104/L103 full activity. All extension-field,
arbitrary-chart and finite-certificate qualifications are retained.

### Exact bindings of the remaining two fourths

For fourth 355, U gives I={8,27}, K={79,89}. The unique record is
at /cases/75 of the same shard. Its rank nineteen, original minor rows,
columns, residue 54, both complete ordered null vectors and all 48 null
residual entries equal L129's full certificate. For fourth 647, U gives
I={18,33}, K={89,96}; the unique record at /cases/182 similarly agrees
with L130's rank nineteen, original minor rows, columns, residue 85,
complete basis and all 48 residual entries. Exterior column order,
field, H, S, J, all four support labels, source shard/hash and full-universe
indices agree in each case. No changed-label conclusion of L128 is used.

L129/L130's source pointers /kernel_basis refer to their imported
L126/L127 certificates, respectively. The comparison checks each source
file hash and selected pointer value, and equality of that full value
to both the present certificate basis and the selected shard basis.
Their import records specify the already proved locus and unchanged rows
one, two and four, with changed third row three. This does not import
L126/L127's inconsistent four-support hypotheses for changed labels:
L129/L130 already prove the precise new-label exclusions.

Every hash in both separate audit input manifests, every audit check
and both successful isolated execution records is checked. Both complete
replays bind their corresponding certificate hashes and have no failures.
The canonical L129 step-374 and L130 step-378 audits cover the entire
homogeneous loci, including infinity, all original-row gates and arbitrary
prescribed charts. Each has exactly two complete points and zero passing
points or unresolved branches. L129 excludes both planes by first-row
lambda zero. L130 excludes one by first-row lambda zero and the other
by second-row lambda zero. Their changed third rows are already covered
by those audited results. No new locus or extension-point sample is used.

All 898/898 comparison checks pass: 756/756 screen entries, 282/282
eligible cases, both required residual bindings and zero uncovered cases.
Every original input remains byte unchanged. This is same-step complete
binding of audited exclusions, not a separate critical audit of this
assembly or proof-assistant verification. Python/residue arithmetic and
the inherited finite-certificate qualifications remain shared limitations.

### Actual fourth selection and contradiction

Suppose all hypotheses hold. L109's necessary equality conclusion gives
r=12+n_0 in [12,14] distinct actual two-overlap error supports in the
same pencil. Each of the three assumed seeds meets S and J in two
labels, so each belongs to this collection. There is an actual fourth
support outside these three; indeed at least nine choices remain.
Select it before applying any exclusion. L086 applies to every pair
of actual errors of this same equality pencil, so this fourth meets
each seed in at most one label. Its unique index d in U is therefore
one of the 282 eligible fourths just covered.

If d has rank, factor or omission disposition, L125 contradicts its
actual occurrence. Otherwise d=355 or d=647. The four supports then
satisfy exactly L129 or L130, respectively, giving a contradiction.
In each application the field, code, seven-set, original cell, sixteen
finite events, represented t=0, actual nonzero D/locators and arbitrary
weights and prescribed chart are unchanged. L109 supplies independent
lift directions and a nonzero decomposable necessary tensor, together
with the actual full-weight gates. Only its necessary implication is
used. This proves the stated seed exclusion.

No kernel is promoted to an actual event and no four-row converse is
invoked. Recorded exclusions do not shrink the fourth-domain predicate;
selection does not depend on recursive deletion. All 154 residuals stay
saved, including these now separately covered occurrences. ATTEMPTS/041–044
remain failures of their stated shortcuts; assembly adds the separately
audited residual exclusions rather than repeating those searches.

### Literature import and specialization

The unchanged invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-20-third59-assembly-review.md`.
Reuse its primary coverage and duplicate/failure comparison. L128 is
only a method comparison for a different third label. Standard inputs
are imported through the stated canonical results with precise citations:

* J. I. Hall, *Notes on Coding Theory*, [Theorem 5.1.1 and proof,
  printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf).
* I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS codes
  that have an error correcting pair*, FFAA 40 (2016), 224–245,
  DOI 10.1016/j.ffa.2016.04.004, [accepted manuscript 2016-02-29,
  section 5, Definitions 5.1–5.2 and shortening formula after Lemma 5.3,
  pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf).
* Keith Conrad, [*Exterior Powers*, Theorems 4.2, 7.1, 7.5 and full
  proofs, pp. 11–12,23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf),
  undated author PDF, inspected in the reused assessment.
* J. S. Milne, [*Fields and Galois Theory*, Kea Books 2022,
  sections 1.6–1.9 pp. 5–7 and Proposition 2.17 p. 34](https://www.jmilne.org/math/Books/FT0.pdf).

The labels are sixteen distinct elements, multipliers are nonzero units,
and k=8. Each selected row shortens the seven distinct labels J minus K,
through positive dimensions from eight to one; retained differences and
multiplier products are nonzero. Exterior degree two is used in dimension
seven over F_97 and its extensions. Complete homogeneous loci and chart
failures are imported from audited indexed inputs. This assembly changes
none of the standard hypotheses and needs no reproof of these theorems.

### Separate critical audit, 2026-10-20

Step `2026-10-20-mca-382-third59-assembly-critical-audit` used the unchanged
invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-20-third59-assembly-audit-review.md`.
The entire proof and comparison program were inspected. L125/L129/L130's
exact hypotheses, conclusions and separate audits 358/374/378 were checked,
as were L109's necessary proof and audit, L086's actual-pair argument and
audit scope, and L104's full-activity and equality-counting passage.
No mathematical defect, missing hypothesis or new dependency was found.
This is RESEARCH / REPRODUCTION: separate validation of this restricted
assembly, not a new exclusion or result beyond the assessed literature.

**Closed domain and program.** The comparison has no local mathematical
imports: its only functions are `run` and the nested `check`, `digest`,
`read`, with standard-library imports. A false check raises an exception,
records failure, writes its evidence and exits nonzero. A failure before
the summary cannot be mistaken for successful complete coverage.
The residual-audit conditional checks target [59,355] in the first branch
and L130's exact scope string in the second; both branches are exercised.
The audit wrapper below was also inspected in full.

The isolated run reproduces the entire original comparison certificate
byte for byte, including all 898 successful checks, every screen/coverage
record, both complete residual bindings and all 27 recorded input digests.
An independent domain path enumerates four-subsets of H, splits those
having two S labels, sorts their two pairs, and uses bit masks for every
intersection. It agrees on all 756 ordered rows and screen entries, and
on the entire ordered list of 282 eligible fourths. Distinctness from all
three seeds is explicit. The seed indices are exactly 0,412,59.

Every eligible coverage record is compared in full, including its support,
status and shard-case pointer. Every saved deficient-basis coefficient
is a canonical residue, and every factor/omission predicate and its first
nonzero failure witness is compared on the complete basis. The original
comparison additionally checks all eight row/label choices and all seven
omission choices in their proper order; an omitted predicate cannot pass
merely because a shorter list has no failed test. The priority counts are
96 rank, 175 factor, 9 omission and 2 residual, totaling 282.

The unique master/replay manifest entry, unchanged third-059 shard and
nine selected L125 audit inputs bind by exact hashes, as do the L125 audit
code and complete replay log. Successful complete replay and unchanged-file
flags agree with the canonical step-358 audit. Complete ranks and kernels
are imported from that audit, not inferred from vector counts here.
Only the selected shard is read; the old partition search is not repeated.

**Residual provenance.** The entire binding records agree at shard
positions 75 and 182, for fourth indices 355 and 647. Both ordered bases,
original minor row/column lists, residues 54/85, all 48 null residual
entries, exterior-column order, field and labels agree with L129/L130.
Their `/kernel_basis` source pointers are into the imported L126/L127
certificates, not into the shard. The pointed values and source hashes
match both the new certificates and the selected shard records.
This distinguishes provenance from transporting an old four-support
contradiction to changed labels.

Both complete residual-audit check lists and their four successful
producer/verifier execution records were inspected. Every input hash in
both audit manifests matches, including each complete output/replay and
imported locus certificate. Their full replays bind the certificate hashes.
The canonical audits supply complete homogeneous loci including infinity,
changed-third-row gates and arbitrary prescribed-chart checks. L129's
two exhaustive planes fail at row one; L130's fail at rows one and two,
respectively. There are no unclassified extension components. These
audited algebraic subresults are reused without a new locus calculation.

**Actual selection and inherited hypotheses.** In L104, t counts errors
equal to the lift; its other errors have at most two S labels. Equality
gives full activity via L103 and the balances
`n_0+n_1+n_2=16`, `n_1+2n_2=28` when t=0. Thus L109's collection has
r=n_2=12+n_0>=12 distinct actual supports of this same pencil. All three
assumed seeds have two S labels and hence are members of that collection.
Select one of the at least nine remaining actual supports first. L086
then makes it pairwise linear with every seed, so its unique full-universe
index is among the 282 covered cases. No kernel or projected candidate
is substituted for this actual fourth.

All five direct inputs apply to the unchanged field, H, dimension, seven-set,
cell, sixteen original finite events, represented t=0 and actual nonzero
D/locators. L109's independence proof makes the actual wedge nonzero;
its necessary direction applies to any selected subfamily and does not
require the six-row converse. L125's factor test rejects rank zero by
nonpersistence and rank one by failed full weights. Its omission test
uses the actual decomposable wedge and L104/L103 full activity.
L129/L130's necessary lambda failures persist over extensions. In a
prescribed chart an omitted direction supplies no event; a finite
direction only rescales the failed zero weights. The inherited
L010/L103/L104/L040/L069 and L086/L056 computational qualifications
remain essential. Neither rationality of the chart nor four-row
sufficiency, recursive deletion or universal pair extraction is used.

Reproduce this separate bounded audit with

    python3 -B scripts/seven-coordinate/audit_l131.py

The full report is `scripts/seven-coordinate/l131-critical-audit.json`.
All 4,463/4,463 audit checks pass, including 756/756 screens, 282/282
eligible covered cases, 2/2 residual bindings, zero uncovered cases,
one byte-identical complete reproduction and 29/29 unchanged original
files. Full records are checked, not previews. Python arithmetic and
the inherited finite certificates remain shared limitations; this is
not proof-assistant verification. All 154 historical residuals and
ATTEMPTS/041–044 remain unchanged.

The argument and direct inputs are unchanged, so PROOF.md and DAG.md
are unchanged. This canonical section supersedes the overview's historical
pending-audit wording for L131. Other thirds, fixed-pair coverage, universal
representation/extraction and challenge definitions remain unresolved;
the global interval stays 11/q–16/q.

## Mathlib

Full matching coverage for this exact labeled assembly: **not checked**.
Supporting coding, exterior, finite-field and rank coverage: **not newly
checked**, not asserted absent. The precise standard citations and audited
finite inputs retain their qualifications after the separate step-382
critical audit; no formal verification is claimed.
