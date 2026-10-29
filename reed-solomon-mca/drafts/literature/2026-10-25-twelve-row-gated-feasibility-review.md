# Twelve-row gated feasibility — completed source comparison

TARGET: Assess source coverage for a uniform twelve-row feasibility test on L153's pair kernels with L109's Plucker, rank-one and full-weight gates and L086's incidence restrictions.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 475 searched exact twelve-row/MCA and common-transversal terminology, finite-field polynomial certificates and Schubert incidence; scoped local searches checked saturation/solver assessments, ATTEMPTS/041–043 and /048, L109/L153/C152a, and L122/L123 for duplicate survivor tests. Exact queries and inspected sources are recorded below; no novelty inference is made.
SOURCE_EVIDENCE: Reuse Hall Theorem 5.1.1 pp. 63–64 https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf ; Marquez-Corbella–Pellikaan 2016-02-29 section 5 pp. 7–8 https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf ; Conrad Theorems 4.2/7.1/7.5 https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf . Freshly read Gao–Platzer–Clarke CAI 2011 Theorems 2.2/3.1/3.2/4.1/5.1/5.2 and relevant proofs https://symbolaris.com/pub/QEfin.pdf ; Rosenthal–Trautmann arXiv:1209.2887v1 pp. 1–4 https://arxiv.org/pdf/1209.2887 ; Alrabiah–Goyal–Guruswami TR26-262 Theorem 1.1, Definition 4.1, Theorems 4.2/3.5 and Corollary 3.7 https://eccc.weizmann.ac.il/report/2026/262/download .
COMPARISON: Exact finite-field formula flattening and ideal certificates are known tools for simultaneous gates, but supply neither this twelve-row exclusion nor feasible computation. Generic Schubert counts and constructed subspace-design codes have unestablished hypotheses here. L123 already exhausts L122's three planes; L151 remains label-specific. Only a bounded certificate-specification specialization is ready, not a solver or uniform theorem.
GAP: Construct and audit the actual finite-field formula and certificate specification, including complete pair/row selection and every nonlinear/chart branch, before deciding whether a solver is computationally justified; feasibility and the twelve-row obstruction remain unproved.
REASON: Essential source coverage supports the separately proposed finite specification/audit in 2026-10-25-twelve-row-certificate-specification-review.md. No local encoding, new lemma, solver, count or obstruction is derived in this literature-only turn; the new ready continuation requires separate supervisor approval.
LITERATURE_REASON: The target changes from a two-row linear census to simultaneous nonlinear twelve-row compatibility; the prior assessment's SCOPE explicitly excludes additional-row sweeps and new gate solvers.
SCOPE: Conditional fixed H/S represented t=0 class over F_(97^20); comparison of twelve-row certificate methods only. The bounded continuation specifies and audits a formula and its size, without running a feasibility solver, changing the chart, assuming rational descent or asserting exclusion.

## Completed comparison — step 475

The main gap is uniform compatibility for C152a's arbitrary extracted
pair. The intermediate target reviewed is a uniform twelve-row test on
L153's complete pair registry. Its plausible use is an eventual exclusion
of the represented equality class; a survivor would instead preserve the
mechanism's limitations. Universal seven-coordinate representation and
challenge identification are independent unresolved gaps. The frozen
interval remains 11/q–16/q.

### Reused results, exact hypotheses and duplicates

Read L109's necessary reduction and complete gate/converse argument,
L153's entire finite-census proof, C152a's actual-family applicability
argument and L086's original-family hypotheses/restrictions. Retain
F_(97^20), the specified order-sixteen H and seven-set S, k=8, the pinned
cell, coefficient syndromes in U_S, sixteen original finite events,
t=0, actual nonzero D/locators, arbitrary weights/original chart and
inherited L056/L069/L040 finite-certificate qualifications. L153 supplies
all 79,380 pair kernels, not a labeled pair chosen by C152a. No saved
kernel was rechecked or mathematical computation performed in this turn.

Reuse the inspected-primary comparison in
`2026-10-20-uniform-disjoint-pair-assembly-review.md` and direct source
repair in `2026-10-25-all-pair-census-calculation-review.md`. Their GRS
field/distinct-label/nonzero-multiplier hypotheses and seven shortening
deletions from dimension eight to one remain unchanged. The exterior
inputs apply in dimension seven, degree two over the base field and its
extensions. These imports through L109 need no reproof. The older
Marquez-Corbella–Pellikaan access problem does not remove saved adequate
coverage. Reuse, rather than freshly re-audit, the recorded BCHKS,
Chojecki and Jeronimo stronger-bound comparisons in the October 20
assessment; this is not a fresh version check of those sources.

ATTEMPTS/041, /042 and /043 respectively preserve deficient four-row
stacks, whole-factor filter failures and passing selected-row planes.
ATTEMPTS/048 ends two-row rank stratification only. The continuation
must add simultaneous row-selection information, not rerun those tests.
In particular L123 already certifies the complete 756-row capacities of
L122's three planes. Repeating those censuses would be a duplicate;
their four-direction counts do not transfer to arbitrary pair kernels.
The existing October 18 exact-ideal assessments cover chosen residual
loci, not uniform twelve-row selection. No matching completed uniform
encoding was located in the scoped local searches.

### Primary method comparison

S. Gao, A. Platzer and E. M. Clarke, *Quantifier Elimination over Finite
Fields Using Gröbner Bases*, CAI 2011, LNCS 6742, pp. 140–157,
DOI 10.1007/978-3-642-21493-6_9,
[author PDF](https://symbolaris.com/pub/QEfin.pdf): Theorem 2.2 p. 143
handles ideals over any F_q after adjoining every variable's field
polynomial. Theorems 3.1–3.2 pp. 144–146 give exact projection/elimination.
Lemmas 4.1–4.2 pp. 146,157 and Theorem 4.1 p. 147 cover nonzero atoms
and disjunctions; read all conjunction/disjunction proof cases, including
the selector outside {0,1}. Theorem 5.1 pp. 149,157 proves the algorithm;
Theorem 5.2 p. 150 gives exponential, not practical, cost guarantees.
Read the finite-field radical argument pp. 143,156 and both projection
inclusions p. 145. The Rabinowitsch proof's printed `p` means the atom's
polynomial. Import the standard result, not that typographical symbol.

Here q must be 97^20 for extension-valued unknowns. Restricting them by
97th-power field equations would change the problem. A unit-ideal
identity without field equations excludes over all extensions; a proper
ideal alone gives no point over the prescribed field. Reuse the October
18 Stacks/Magma certificate and truncation qualifications; no package
installation, cost bound or custom encoding is inferred.

J. Rosenthal and A.-L. Trautmann, *Decoding of Subspace Codes, a Problem
of Schubert Calculus over Finite Fields*,
[arXiv:1209.2887v1, September 13, 2012](https://arxiv.org/pdf/1209.2887),
pp. 1–4: arbitrary-field Plucker coordinates and shuffle equations support
the incidence language already used in L109. Their Theorem 2 concerns
general-position complex subspaces; Example 4 explicitly distinguishes
finite-field points from geometric solutions. These results supply no
count for these fixed characteristic-97 subspaces. No genericity,
transversality, rational descent or expected-dimension exclusion is
established or imported here. Their decoding application is a method
analogy, not the missing gated twelve-row theorem.

O. Alrabiah, R. Goyal and V. Guruswami, *Explicit Reed-Solomon Subspace
Designs: Optimal List and Line Decoding*, ECCC TR26-262, October 20,
2026, [primary PDF](https://eccc.weizmann.ac.il/report/2026/262/download):
read Theorem 1.1 printed p. 4, Definition 4.1/Theorem 4.2 p. 19 and
Theorem 3.5/Corollary 3.7 pp. 18–19. The construction is for sufficiently
large n and specially supplied evaluations; the general design theorem
assumes the displayed automorphism and bounded-dimensional multiplicity
conditions. These are not established for our n=16 fixed H. Its MCA
consequence therefore cannot be substituted for this local obstruction.
No proof or correctness audit of that new preprint is imported. This
precise hypothesis mismatch suffices for the present source comparison.

Full matching Mathlib coverage for the twelve-row certificate is not
checked. Existing supporting coverage qualifications are unchanged;
unknown coverage is not absence.

### Search record and access qualifications

Fresh queries included `Grassmannian line meeting linear subspaces
Schubert problem finite field Groebner incidence`; `finite field
polynomial systems Groebner basis field equations Rabinowitsch nonzero
constraints saturation`; `site.math.clemson.edu Gao finite fields
polynomial systems field equations Groebner basis Nullstellensatz`;
`site.math.tamu.edu sottile decoding subspace codes Schubert calculus
finite fields Rosenthal Trautmann`; `"Quantifier Elimination over Finite
Fields" Gao Platzer Clarke pdf`; `"Explicit Reed-Solomon Subspace
Designs" pdf`; `"Reed Solomon" "twelve" "mutual correlated"`; and
`"Grassmannian" "finite field" "common transversal" polynomial`.
The numerical-homotopy documentation/query was a method lead only;
no numerical algorithm is imported for positive characteristic.

The obsolete Gao /ap/pub/ link timed out; both corrected author mirrors
https://symbolaris.com/pub/QEfin.pdf and
https://logic.kastel.kit.edu/pub/QEfin.pdf succeeded. The ECCC
trailing-slash download failed, while its page's actual `/download`
link succeeded. These are resolved access errors, not source blockers.
Discovery also found a mirror-index entry for Manzur, ePrint 2026/2617;
the primary landing page and PDF were inaccessible. It remains an
unread lead, unimported and not ruled out. ABF26 and the previously
recorded lower-bound lead remain unread. None is an essential missing
input for applying the standard finite-field certificate method to the
conditional frozen model; no challenge-level conclusion is authorized.

### Bounded continuation and discriminating test

The exact proposed research action and its ready coverage are in
`2026-10-25-twelve-row-certificate-specification-review.md`. The next
step should specify and audit the simultaneous finite formula and
certificate contract, and report its actual variable/constraint size,
before selecting any solver. This specializes known algebraic tools;
it does not promise tractability or manufacture a new obstruction.

Continue only if the specification demonstrably covers arbitrary
registered pairs and twelve selected rows on one common plane, with
all gates, incidence restrictions and original-chart branches retained.
Abandon that encoding if this proof obligation fails; preserve its first
missing branch or uncontrolled size obstruction and choose a materially
different bounded test. An equivalent encoding alone does not improve
the bound. No new solver, source-derived local lemma or mathematical
script was written in this literature turn. Separate supervisor approval
of the newly written ready continuation precedes research. Completed
classification: LITERATURE / NOVELTY_UNCHECKED / EXPLORATION; mathematical
exploration usage remains zero.

## Invocation-start proposal — step 474, superseded by the comparison above

This document does not approve a mathematical attempt or claim a new
theorem. The exact target is a source-coverage review. It should reuse
`2026-10-25-all-pair-census-calculation-review.md` and the October 20
uniform-disjoint-pair comparison wherever their hypotheses still match,
then isolate the genuinely missing many-row mechanism. No further
two-row rank census is justified by this proposal.

Essential local inputs are L153's complete pair registry and full
kernels, L109's exact gated interpretation and scalar-extension scope,
and C152a's actual-pair relevance through L086/L152. L104 already supplies
local two-row survivors. L151 supplies only its fixed labeled exclusion.
Retain all original hypotheses: F_(97^20), this H/S, k=8, pinned cell,
coefficient syndromes in U_S, actual nonzero D and locators, t=0,
sixteen original finite events, arbitrary original weights and chart,
and inherited L056/L069/L040 finite-certificate qualifications.
Universal representation and challenge identification are independent
unresolved gaps. Neither a twelve-row relaxed solution nor its absence
is a complete challenge resolution.

A useful review must either identify precise applicable primary results
or approve a bounded mechanism with an explicit success/abandonment
test. An existing label-specific solver, a source snippet, or repetition
of uniform pair ranks is insufficient. Full matching Mathlib coverage
has not been checked. No external source was newly retrieved this turn.
