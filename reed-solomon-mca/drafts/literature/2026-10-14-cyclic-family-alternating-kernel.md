# Cyclic-family alternating moment test — source comparison

TARGET: Determine whether L087's full alternating moment system has zero kernel for every bijective H-labeling.
CHECKED: 2026-10-14
DECISION: EXPLORE
SEARCH_EVIDENCE: October 14 exact-ruler, Vandermonde/exterior-kernel, rational-normal-curve transversal and fixed-evaluation higher-order-MDS searches found no inspected theorem deciding this target; reused the ready October 5–6 theorem comparisons and inspected the local pattern restrictions and stopped sampling routes.
SOURCE_EVIDENCE: Reused Conrad Theorems 4.2/5.1/5.4 and Corollary 5.9, Lovett Theorem 1.2, BGM Definitions 1.4/1.8 and Theorem 1.12/Corollary 1.15, BDG Definitions 1.2/1.3/6.1 and Theorems 4.1/6.4; rechecked BDG's generic-point hypotheses and Conrad's exterior-basis and isomorphism statements in the primary texts.
COMPARISON: Exterior functoriality supplies existing machinery, whereas selectable/generic evaluations do not cover fixed H; L027/L029 prove rank only for their different patterns, and L073–L079 retain the exact L072 plane incidence and cannot be imported as cyclic-family conclusions.
GAP: Zero common kernel for every bijective H-labeling, or one certified deficient labeling, remains unknown for L087; no rank, tensor-rank restriction, equality exclusion or realization is established here.
REASON: Essential source and failure comparison is sufficient for one bounded uniform quotient proof attempt on this unchanged target; no essential matching theorem or persistent source blocker was identified, and the search does not establish novelty.
SCOPE: Exactly L087's sixteen cyclic blocks, fixed H and F_(97^20), on the entire exterior square; one analytic quotient attempt with all coefficient-zero branches retained, no positive-only rank sampling, fixed-label sweep or family census.

## Proposed target and limits

Use precisely L087's sixteen translates of {0,1,4,6} in Z/16Z,
F=F_(97^20), and the fixed order-sixteen subgroup H of F_97^*.
For a bijection h:Z/16Z -> H, write V=F^8 and
v_x=(1,h(x),...,h(x)^7). For each block B let U_B be the span of
its four columns and pi_B:V -> V/U_B the quotient. The proposed
full alternating system is the intersection of the kernels of
Lambda^2(pi_B) on Lambda^2(V), over all sixteen blocks.
The exact target asks whether that intersection is zero uniformly in h.
These definitions specify a proposed test, not a derived result.

The main gap is exclusion of sixteen actual errors. A uniform zero
kernel could supply a moment obstruction to this particular family;
its actual-error applicability, including dependent syndrome directions,
would still need justification. A nonzero kernel alone supplies neither
a decomposable tensor nor full error weights, finite distinct parameters,
nonpersistent locators or same-support failure. Original charts remain
arbitrary. No general equality-family classification follows either way.

The essential proposed input is audited L087. L010 supplies prospective
actual-error context; L026/L027/L029 and L073–L079 are comparisons to
review, not silently imported premises. Review their precise quotient
and moment-index conventions before using them. No cross-notebook input
is proposed. Mathlib coverage is not checked.

This assessment was REVIEW_REQUIRED at invocation start. Step 220 is
the separate literature-only review requested there. The completed
comparison below licenses no mathematics within this invocation and does
not repeat the blocked configuration census. The exact TARGET is retained.

Prospective discriminating test after approval: either give an exact
uniform kernel-zero proof, or a rigorously verified rank-deficient
bijection as a negative answer to this target. A sample of zero kernels
cannot prove the uniform assertion. Failure of the target would require
another mechanism, not an inference of RS realization. The completed
comparison supports one bounded analytic quotient attempt after this
literature-only invocation and supervisor approval of the updated record.

## Completed comparison, step 220

### Ready literature reused and primary hypotheses rechecked

Reuse the source coverage in
[the arbitrary-label review](2026-10-05-cyclic-0125-arbitrary-label-rank.md),
[the 0135 review](2026-10-06-cyclic-0135-full-rank.md), and
[the broader rank review](2026-10-06-matching-two-uniform-rank.md).
Their general theorem comparisons remain relevant; their old support
patterns, matching-number hypotheses and calculation approvals do not
transfer to L087. No matching number is assumed for this target.

Keith Conrad, [*Exterior Powers*](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf),
undated author-hosted 47-page PDF, retrieved October 14, 2026:
Theorem 4.2, printed pp. 11–12, gives the exterior basis for a free
module; Theorem 5.1, pp. 15–16, gives induced maps and composition;
Theorem 5.4, p. 17, preserves isomorphisms and surjections;
Corollary 5.9, p. 18, preserves injections of vector spaces.
The prior review inspected the latter proofs. This turn rechecked the
exterior-basis statement and proof and the isomorphism statement.
Finite-dimensional spaces over F_(97^20) satisfy the field/free
hypotheses. These are machinery already represented in L026/L027,
not a theorem about intersections of sixteen kernels. No reproof is needed.

Joshua Brakensiek, Manik Dhar and Sivakanth Gopi,
[*Generalized GM-MDS: Polynomial Codes are Higher Order MDS*](https://arxiv.org/html/2310.12888v3),
arXiv:2310.12888v3, June 4, 2025: rechecked Definition 1.3,
Theorem 4.1 with its displayed monomial matrix and base cases, and
Definition 6.1 with Theorem 6.4. Theorem 4.1 requires generic points
over an algebraically closed field and strictly increasing integer
exponents. Definition 6.1's variety property uses generic columns;
Theorem 6.4 concerns irreducible MDS varieties in that sense. It does
not assert the property for every finite selection on the variety.
The prescribed subgroup labels are not the generic evaluations of
these statements. Their column-span intersection conclusion is also
not an identified theorem for this stack of exterior quotient maps.
The prior assessment read the monomial induction through Case 2 and
the power-series reduction; Case 3 and the full power-series proof
remain unread and unused. This is a scope rejection, not an import
or a claimed counterexample to those theorems.

The reused reviews also record inspected statements of:

- Shachar Lovett, *MDS Matrices over Small Fields: A Proof of the
  GM-MDS Conjecture*, FOCS 2018, Theorem 1.2, pp. 194–195,
  [primary paper](https://ieee-focs.org/FOCS-2018-Papers/pdfs/59f194.pdf).
  It permits selection of evaluations for admissible prescribed zeros;
  it does not certify this matrix at fixed H.
- Brakensiek–Gopi–Makam, *Generic Reed-Solomon Codes Achieve
  List-decoding Capacity*, [arXiv:2206.05256v4](https://arxiv.org/html/2206.05256v4),
  Definitions 1.4/1.8, Theorem 1.12 and Corollary 1.15 with proof.
  Its generic evaluations and span-intersection conclusions do not
  answer the fixed-H exterior question.

The [overlap-factor review](2026-10-05-overlap-factor-universal-rank.md)
records Gandini, arXiv:1810.11694v3, Theorem 1.1, Proposition 6.1
and Theorems 7.3/7.5, and Boito–Ruatta, SNC 2011, section 3.2,
Proposition 2/Corollary 1, p. 76. Its characteristic-zero arrangement
regularity and single-quotient multiplication-corank comparisons do
not give this simultaneous exterior rank. The broader rank review
also inspected Scott–Wilmer's May 11, 2021 author PDF, Theorem 2.3,
pp. 4–5, Lemma 3.4 and Corollary 3.5, pp. 16–17: the self-annihilation,
characteristic-zero and generic-projection conditions there are not
supplied here. These comparisons are reused without reopening their
proofs. No such theorem is imported into a new mathematical argument.

### Target-specific searches and lead screening

Queries issued October 14, 2026 included:

- `"cyclic" "0,1,4,6" "Reed"`
- `"0,1,4,6" "kernel"` and `"0,1,4,6" "moment"`
- `"Vandermonde" "exterior" "subspaces"`
- `"rational normal curve" "secant" "common transversal"`
- `"rational normal curve" "secant" "transversal" finite field`
- `"higher order MDS" "arbitrary" "evaluation points"`
- `"higher order MDS" "fixed" "roots of unity"`
- `"cyclic configuration" "exterior" rank`
- `"Reed-Solomon" "alternating" "kernel"`
- `"polynomial subspaces" "exterior square"`

The exact-ruler searches produced no inspected matching theorem.
Other hits included superspace coinvariants, alternant parity checks,
configuration spaces with a different meaning of configuration, and
real/complex secant-curve existence problems. These are screened leads,
not coverage of the target. Secondary roots-of-unity claims and snippets
were not used as mathematical facts or novelty evidence.

A new primary-hosted lead was Kumar–Ron-Zewi,
[*Advances in List Decoding of Polynomial Codes*](https://eccc.weizmann.ac.il/report/2026/032/),
ECCC TR26-032, February 28, 2026. Only its primary landing-page abstract
was read; it identifies a survey, not a theorem with hypotheses for
this kernel. The search excerpt points to random-evaluation RS results.
The PDF's theorems and proofs were not inspected or imported, and this
lead is not counted as theorem-level coverage. No essential matching
claim was identified behind it. ABF26 definitions and the previously
blocked configuration census remain separate parked work, not source
prerequisites for this independently specified matrix question.

### Local duplicates, conventions and failed mechanisms

Read audited L087's full proof and qualifications. Its published ruler
construction and noncollinearity invariant provide the abstract family
only. Reuse its ready construction assessment
[here](2026-10-14-linear-sixteen-family-rigidity.md); no construction
search, configuration classification or new incidence calculation is needed.

Read L010's hypotheses, conclusion and moment-kernel argument, L026's
moment and annihilator conventions, L027's complete seven-block quotient
proof, and L029's complete eight-block quotient elimination. The latter
two establish full exterior rank uniformly for their explicitly stated
0125 and 0135 families. Their residual bases and nonvanishing checks
are tied to those supports. They are examples of a viable method, not
answers for L087; no kernel dimension for L087 was computed here.

The proposed question uses v_x=(1,h(x),...,h(x)^7), whereas those lemmas
use m_x=(h(x),...,h(x)^8). Their displayed formulas give m_x=h(x)v_x;
h(x) is nonzero. Thus the four-column spans being compared are the
same, with no change of ambient coordinates. This is only the necessary
convention check for reusing the existing quotient machinery. It does
not assign syndrome weights, prove a kernel bound or verify an actual
equality pencil. In unshifted coordinates annihilator pairing is the
ordinary evaluation of the coefficient polynomial; the shifted formula
in L026 must not be copied with its extra h(x) factor unexamined.

Read L073's hypotheses and rank-restriction argument through its
parallel-class reduction, and the precise hypotheses and conclusions
of L074–L079. L073's rank-six argument uses L072's complete multipartite
collinearity graph; its rank-four argument and L074–L076 use the
selected parallel classes. L077–L079 retain those exact quadrilaterals
and singleton-ratio tables. L087 already disproves an isomorphism to
L072. These hypotheses have not been supplied for L087, so neither
their tensor-rank restrictions nor L079's equality exclusion transfers.
The unaudited alternative rank/fullness chain remains unaudited.
No claim that L079 itself proves full exterior rank is made.

Read ATTEMPTS/020,029,031 in full. The first stops repeated positive
finite rank sampling, not a uniform analytic proof. The second excludes
four linear anchors for one saved assignment; it is not a theorem about
this cyclic family. The third stops abstract uniqueness and explicitly
retains independent moment approaches. None is deleted or reopened.
There is no fixed-label sweep, labeling census or cross-notebook input.

### Bounded next attempt and decision test

The unchanged TARGET has EXPLORE coverage for one subsequent mathematical
attempt, subject to the supervisor's separate approval of this updated
assessment. Attempt one analytic pass through the sixteen actual quotient
constraints, choosing bases justified by L010's eight-column independence
and the cited exterior machinery. Retain the entire exterior square,
every coefficient that could vanish, and all corresponding exceptional
branches. Do not substitute cyclic labeling, genericity, decomposability,
parallel-class structure or a prior family's residual kernel basis.

Continue with a complete uniform zero-kernel proof or a rigorously proved
intermediate restriction that has an explicit remaining kernel gap and
a discriminating continuation. If a branch yields a deficient labeling,
verify the bijection, all sixteen quotient constraints, the complete
matrix and a nonzero kernel tensor independently; that refutes this
target and abandons the uniform zero-kernel criterion for the family.
An exact diagnostic calculation may check one stated inference in this
same attempt with full evidence saved. Another batch of positive rank
samples is excluded. If no useful restriction or concrete residual test
emerges, preserve the unfinished equations, report EXPLORATION and
reassess the mechanism rather than silently repeat the pass.

A zero kernel would be a family-specific prospective obstruction, still
requiring a separate actual-error applicability argument, including
dependent syndrome directions. A nonzero tensor need not be decomposable
or supply any full errors, original parameters, nonpersistent locators
or same-support failure. Neither outcome classifies arbitrary families
or resolves the uniform triangle twelve bound or ABF26 qualifications.
Full matching Mathlib coverage is not checked. This source turn produced
no mathematical result, modified no lemma or mathematical script, ran
no rank computation and used zero mathematical exploration turns.
