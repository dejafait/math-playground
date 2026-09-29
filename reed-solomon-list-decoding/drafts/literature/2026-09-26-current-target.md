# Center-dependent Riccati multiplicity: literature assessment

TARGET: Derive and test a center-dependent multiplicity weight at simple zeros of a from a'(x)t+2b(x)y(x)+c(x)=0, to see whether L010 can improve the e=n regime.
CHECKED: 2026-09-27
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Reuse the earlier exact-title, repository, institutional, Riccati, weighted-decoding and indicial-equation searches below. The second 2026-09-27 review tried author-owned website repositories and raw source files, with targeted author/repository searches; no readable ABF26 text was recovered. Queries, inspected files and failed asset-enumeration paths are recorded in the author-repository assessment below.
SOURCE_EVIDENCE: Reuse the theorem-level readings of Kopparty (2015), Theorems 4.3-4.4 and Corollary 4.5; Guruswami-Sudan (2001), Theorem 5; Fürnsinn-Hauser, arXiv:2307.01712v2, Section 2.1, Lemma 3.7, Theorem 3.17 and Remark 3.18; Peikert-Veliche Hostetler (ITCS 2026), Theorem 3.3, and the earlier primary metadata/challenge-page readings. Newly inspected Arnon and Fenzi website source entries link only to ePrint/ia.cr; no ABF26 definition or theorem was read. Direct links, retrieved branch versions and access limits are recorded below.
COMPARISON: Weighted list counting and positive-characteristic indicial equations are established mechanisms. Kopparty covers nonlinear differential polynomials, but its local lifting hypothesis fails at the targeted zeros of a. None of the inspected statements directly supplies the proposed center-dependent interleaved Riccati bound.
GAP: The July ABF26 definitions and known-bound comparison remain unread; the positive integer column weights and an improvement over L010 at e=n have not been established. No full-statement literature match is certified.
REASON: Keep SOURCE_BLOCKED because the distinct author-repository access test also failed to recover the essential challenge text. This is a second consecutive STALLED source review, with no import, reproduction or mathematical advance. Stop repeated retrieval through the checked paths, preserve the exact target and its test, and leave dependent specialization gated; the external runner owns the stop state.

## Scope, relevance, and discriminating test

The initial 2026-09-26 assessment superseded the migration note's unread
Kopparty lead while preserving its ABF26 access qualification. The
2026-09-27 source-recovery reassessment below reuses that theorem comparison
for the unchanged target. No new multiplicity formula, list inequality, or
example is derived in these literature steps.

The immediate gap is L010's exceptional-column cost: at e=n its established
condition is only A^2>n(k-1). The proposed intermediate target is a valid
center-dependent multiplicity weight at simple evaluation zeros of a,
using the relation named in TARGET. Such a weight could make agreement
filtering useful for a nonlinear differential family even when all columns
are exceptional. It would not supply a cover of a general interpolant.

The eventual discriminating test is an admissible odd-characteristic,
smooth-domain family with e=n and simple evaluation zeros of a, together
with a center and an explicit improved agreement cutoff and list bound.
The weights must work for every candidate pair and for simultaneous
interleaved agreement, with all row qualifications stated. Continue a
conditional refinement if it improves L010 in a specified nonempty regime;
abandon a proposed uniform improvement if admissible centers force the old
cutoff. This is a test specification, not a completed calculation.

Even a successful family bound J must be compared with epsilon* q for the
given field. Neither polynomial dependence on q nor a bound on one
differential family determines the sharp full-code boundary. Interpolant
coverage, control across all centers, and the field-existence proviso remain
separate gaps. The prior September comparisons in the
[source audit](../../foundations/01-target-and-source-audit.md) are reused.

## Search and access record

Searches on 2026-09-26 included:

- `"Open Problems in List Decoding and Correlated Agreement" filetype:pdf`
- `"Open Problems in List Decoding and Correlated Agreement" Arnon Boneh Fenzi pdf`
- `site:crypto.stanford.edu "2026" "Correlated Agreement"`
- `"2026/680" "pdf"` with metadata aggregators excluded
- `"Riccati" "list decoding" multiplicity` and `"Riccati" "list-decoding"`
- `weighted Johnson bound Reed Solomon soft decision Koetter Vardy theorem`
- `Guruswami Sudan 2001 "Extensions" "Johnson" pdf`
- `"Riccati" "positive characteristic" "residue"`
- `"regular singular" "characteristic p" "exponents" differential equation residue`
- `"Normal forms of ordinary linear differential equations in arbitrary characteristic" arxiv`

The Riccati searches did not locate a matching theorem. That is bounded
search evidence, not evidence of novelty. Followed the differential-equation
lead to its journal PDF and the weighted-Johnson lead to the original
Guruswami-Sudan manuscript. An author-hosted Fürnsinn-Hauser draft led to the
versioned arXiv source; the comparison below uses v2, not the older title.

The [prize page](https://proximityprize.org/) still gives the base-field
threshold and existence proviso recorded in foundations. The
[ABF26 record](https://eprint.iacr.org/2026/680) still identifies July 6,
2026 as the latest of three revisions. Opening the
[PDF](https://eprint.iacr.org/2026/680.pdf) returned a restricted-URL fetch
failure; the linked version archive and
[archive endpoint](https://eprint.iacr.org/archive/2026/680) returned errors.
The [short URL](https://ia.cr/2026/680) also failed. A local read-only
`curl -I -L --max-time 15 https://eprint.iacr.org/2026/680.pdf` attempt failed
with curl exit 6, unresolved hostname. No PDF snapshot or hash was obtained.

[Arnon's page](https://galarnon42.github.io/) and
[Fenzi's page](https://gfenzi.io/) link back to ePrint/ia.cr; neither supplied
a readable independent copy. A search of the retrieved
[Boneh publication page](https://crypto.stanford.edu/~dabo/pubs.html) found no
matching title. No ABF theorem or definition number is inferred from this
metadata. The existing
[pinned ArkLib model](../../foundations/02-pinned-list-model.md) remains a
qualified substitute, not a completed comparison with ABF26.

## Inspected results and applicability

**Kopparty, List-Decoding Multiplicity Codes**, Theory of Computing 11(5),
2015, pp. 149-182, final journal version published May 29, 2015.
Read [Theorems 4.1-4.3, pp. 159-160](https://theoryofcomputing.org/articles/v011a005/v011a005.pdf#page=11),
and [Theorem 4.4 and Corollary 4.5, pp. 163-165](https://theoryofcomputing.org/articles/v011a005/v011a005.pdf#page=15).
Theorem 4.4 applies over characteristic p when the highest-variable partial
is nonzero at the anchor and p does not divide its specified binomial
coefficient; it gives a unique next lifting coefficient. Corollary 4.5
bounds fixed-initial-data degree-d solutions by |F|^(r floor(d/p)+r).
These statements allow nonlinear Q. For the Riccati equation, the required
partial is a(x), so this local theorem excludes the very columns being
investigated. Its field-power count also does not certify epsilon* q.
Theorem 4.3's global enumeration result is distinct from a bound after
agreement filtering. Thus the earlier warning about importing a linear
theorem was too narrow: the decisive issue here is the anchor hypothesis,
not merely nonlinearity.

**Guruswami and Sudan, Extensions to the Johnson bound**, February 2001
manuscript, [Section 2.4 and Theorem 5, pp. 5-6](https://web.stanford.edu/class/cs250/restricted/guruswami_sudan.pdf#page=6).
Read all three parts of the theorem and its proof comparison with Theorem 1.
It treats a q-ary code of specified minimum Hamming distance and
nonnegative symbol weights. Parts (i)-(ii) give n(q-1) and nq-1 bounds under
their weighted-score conditions; part (iii) gives a requested list bound L
under a stronger explicit condition. Thus arbitrary symbol weights and
adjustable list bounds are already known. These are input scores, not a
certificate of extra vanishing multiplicity for Riccati differences.
Application here still needs that certificate and the appropriate pair
budget. A raw nq bound would not meet the prize threshold, and the alphabet
parameter for tuples must not be confused with the base-field q.

**Fürnsinn and Hauser, Fuchs' theorem on linear differential equations in
arbitrary characteristic**, [arXiv:2307.01712v2, October 29, 2023](https://arxiv.org/html/2307.01712v2).
Read Section 2.1 and Remark 2.1 (initial operator and indicial polynomial),
Lemma 3.7 (positive-characteristic Euler action), Theorem 3.17
(regular-singular solutions), and Remark 3.18 (field extensions).
These supply the standard local-exponent framework in characteristic p.
Theorem 3.17 describes solutions in an enlarged differential ring over its
constants, not a finite list of degree-bounded polynomials over F.
The proposed simple-zero relation should therefore be checked as an
indicial-equation specialization, with integer multiplicities distinguished
from their residues in the prime field. This is an applicability direction;
the Riccati weights and their interleaved counting consequence are not
stated in these passages. A reproof of the general normal-form theorem
would not be justified by this target.

**Peikert and Veliche Hostetler, List Decoding Reed-Solomon Codes in the Lee,
Euclidean, and Other Metrics**, ITCS 2026, article 106,
[Section 3.1, Definition 3.2 and Theorem 3.3](https://drops.dagstuhl.de/storage/00lipics/lipics-vol362-itcs2026/html/LIPIcs.ITCS.2026.106/LIPIcs.ITCS.2026.106.html).
For a GRS code over a prime-power field, the cited soft decoder lists words
whose normalized correlation with a supplied weight vector is at least
sqrt((k-1)/n)+tau, for tau>0. Its time bound is polynomial in n, q and
1/(tau ||W||). This is a readable modern score formulation of known
soft decoding. It does not construct the exceptional-column weights or
give the required direct interleaved family bound.

The [Koetter-Vardy 2003 paper](https://www.site.uottawa.ca/~zhcheng/RS_soft_decision.pdf#page=5),
Theorem 3 and Corollary 5, p. 2813, was also located and opened. The extracted
prose identifies score versus interpolation cost, but omits key displayed
formulas; the screenshot call supplied no readable image in this session.
No exact quantitative conclusion is imported from that rendering. The
readable statements above suffice for the present soft-decision comparison.
ABF26 is the essential unread source; these other papers do not replace it.

## Redundancy, decision, and limits

The [existing draft](../2026-09-26-weighted-riccati-agreement.md) and L010
already contain the incidence argument with weights p and 1. Local search
found the center-dependent refinement only as a proposal, not as an
established lemma. The
[unfiltered-count failure](../../ATTEMPTS/002-riccati-unfiltered-polynomial-count.md)
remains relevant: a formal solution-space description is not a polynomial
bound on all Riccati solutions. That failure does not rule out filtering.

The new comparison removes an unread differential-decoding lead and
identifies standard indicial and weighted-counting inputs. It supplies no
new list bound and no progress beyond the inspected literature. If source
access is resolved, any research should cite these mechanisms and justify
only the missing simple-zero, center-dependent, simultaneous-agreement
specialization. The full target is not covered by a checked citation, and
its originality remains unchecked. The completed-step classification is
NOVELTY_UNCHECKED; retaining SOURCE_BLOCKED does not authorize a derivation.

## 2026-09-27 source recovery and reassessment

The existing supporting-theorem comparison was sufficient to avoid repeating
its searches. The essential unresolved item was the July ABF26 primary text.
The access test was to recover an attributable version and read its code,
smooth-domain, interleaving, list and radius conventions and relevant bounds.
A title, abstract, citation or formal-library paraphrase would not pass it.

Source-discovery queries included:

- `"Open Problems in List Decoding and Correlated Agreement" pdf` and the
  exact title with `filetype:pdf`, including a search excluding ePrint.
- `"Arnon" "Boneh" "Fenzi" "2026" list decoding`.
- `"2026/680.pdf"` and `"2026/680" "pdf" site:crypto.stanford.edu`.
- `"Open Problems in List Decoding" site:github.com` and the same phrase
  restricted to arXiv.
- `"Arnon" "Fenzi" "correlated" site:crypto.stanford.edu`.
- The exact title restricted to `infoscience.epfl.ch`,
  `iris.unibocconi.it`, `arxiv.org` and `crypto.stanford.edu`; this
  domain-filtered query returned no results.

Inspected access paths and their outcomes:

| Source/path | What was actually accessible |
| --- | --- |
| [ABF26 primary record](https://eprint.iacr.org/2026/680) | Title, authors, abstract, July update note, and history listing July 6, 2026 as the latest of three revisions. No theorem or definition text. |
| [Current PDF](https://eprint.iacr.org/2026/680.pdf), its record-page PDF link, and [download-query variant](https://eprint.iacr.org/2026/680.pdf?download=1) | Web reader returned internal errors; no PDF pages were supplied. |
| Record-page version link and [archive endpoint](https://eprint.iacr.org/archive/2026/680) | Web reader returned internal errors; no dated version URL was recovered. |
| [Short URL](https://ia.cr/2026/680) | Redirected to readable primary metadata, not a readable PDF. This differs from the earlier short-URL failure without resolving text access. |
| [Arnon](https://galarnon42.github.io/) and [Fenzi](https://gfenzi.io/) | Read the matching report/publication entries; their paper links point to ePrint/ia.cr. |
| [Boneh publication page](https://crypto.stanford.edu/~dabo/pubs.html) | Retrieved page had no match for `Correlated` or `List Decoding`; no independent ABF26 copy was identified there. |
| [eprint-classic 2026 index](https://eprint-classic.github.io/2026.html) | Inspected the 2026/680 entry: both record and PDF links lead to eprint.iacr.org. It is an index, not an independent full-text copy. |

A read-only local `curl -I -L --max-time 15` request to the primary PDF
again failed with exit 6, unresolved hostname. A filename search within the
active notebook found no matching PDF/ABF26 cache. No source snapshot or
hash was obtained. These are access observations, not evidence that the
paper or an independent copy does not exist.

The [challenge page](https://proximityprize.org/) was read again: the
designated rates, constant interleaving order, base-field threshold
epsilon* q and field-existence proviso remain as recorded in foundations.
No theorem number, concrete field restriction or smooth-domain definition
is inferred from the ABF26 metadata. Search results containing third-party
claims or citations were treated only as discovery leads; they do not
replace the authors' paper, and their mathematical claims were not imported.

**Decision and stopping assessment.** The access test failed. No additional
applicable theorem was read, no result was imported or reproduced, and the
prior SOURCE_BLOCKED decision is unchanged. This is a STALLED review, with
no claimed progress beyond the checked literature. The existing exploration
count is not reset. Repeating these same endpoints or metadata checks is
not a productive continuation; another access attempt needs a distinct
source path, such as inspection of author-owned repository assets, or a
change in source availability. This stops identical retrieval attempts,
not the mathematical target or research in general.

The center-dependent simple-zero target remains exactly the one in TARGET.
Its plausible use, admissible e=n test and conditional continuation criterion
are retained above. L010's established all-exceptional condition remains
A^2>n(k-1); no improved weights or filtered list bound have been tested.
Even a successful refinement still needs a comparison with epsilon* q,
general-interpolant coverage and the sharp boundary. A recovered ABF26
source must first be compared in a literature turn; retrieval would not
authorize a derivation in that same turn.

## 2026-09-27 author-repository assessment

This second review on the same date tests the distinct access mechanism
specified in the preceding reassessment: inspect author-owned website
repositories for a paper asset or an independent full-text link. The pass
criterion remains readable, attributable ABF26 definitions and relevant
bounds, with a version that can be compared to the July revision. It is
not enough to locate another citation to the paper. Supporting theorem
comparisons above were reused, not newly read or re-proved.

Discovery queries were `"galarnon42" "github" publications`,
`"Giacomo Fenzi" "github" website`,
`site:github.com/WizardOfMenlo/wizardofmenlo.github.io "2026/680"`, and
`site:gfenzi.io "Open Problems" pdf`. Results identified the author
accounts and publication entries, but no attributable full-text copy.
Unrelated and third-party results were not used as mathematical evidence.

| Inspected source | Version/scope and result |
| --- | --- |
| [Arnon repository root](https://github.com/galarnon42/galarnon42.github.io) and [raw index](https://raw.githubusercontent.com/galarnon42/galarnon42.github.io/main/index.html) | Retrieved `main` branch, 2026-09-27; no immutable commit was recovered. The report entry at raw source lines 49-54 points to ePrint 2026/680. No independent paper link appears in that entry. |
| [Arnon publication data](https://raw.githubusercontent.com/galarnon42/galarnon42.github.io/main/data.js) and [old index](https://raw.githubusercontent.com/galarnon42/galarnon42.github.io/main/Old/index.html) | Read the publication data and searched the old index's links. Neither supplied an ABF26 full-text link; the old index has no `680` match. This is a file-level observation, not a claim about all repository history. |
| [Fenzi repository root](https://github.com/WizardOfMenlo/wizardofmenlo.github.io) and [raw index](https://raw.githubusercontent.com/WizardOfMenlo/wizardofmenlo.github.io/main/index.html) | Retrieved `main` branch, 2026-09-27; no immutable commit was recovered. Raw source lines 64-70 and 151-158 point to ia.cr/2026/680 and the prize site, without an independent paper asset. |
| [Fenzi submodule configuration](https://raw.githubusercontent.com/WizardOfMenlo/wizardofmenlo.github.io/main/.gitmodules) | The inspected entry is a website theme, not a manuscript repository. |

The GitHub tree reader failed on Arnon's `Old` directory and Fenzi's
`assets`, `papers`, and `presentations` directories. GitHub API requests for
Arnon's recursive `main` tree and `Old` contents, and Fenzi's root contents,
also failed. The jsDelivr package-list endpoints for both repositories
returned internal errors. Thus recursive asset inspection was incomplete;
no absence claim about unlisted files or history is warranted. Raw-file
access succeeded for the named files above but did not recover a paper.
The previously exhausted ePrint PDF/archive and local HTTP requests were
not repeated. No ABF26 snapshot, versioned PDF or hash was obtained.

**Assessment completed.** The access test did not pass. The newly inspected
files supply publication pointers, no theorem-level input or source-scope
comparison. The outcome is **STALLED**, the decision remains
**SOURCE_BLOCKED**, and the classification is **NOVELTY_UNCHECKED**. No
result was imported or reproduced, and no progress beyond the checked
literature is claimed. This is the second consecutive stalled review;
exploration remains 1/3 since L010 without a reset. The shared runner's
two-stall rule now applies; no launcher or stop-state file was changed.

Stop repeated use of these access paths. A readable attributable source
or a change in access would justify reopening source recovery; this access
stop neither refutes the simple-zero target nor bans other research.
The exact target, relevance and admissible e=n test above are preserved.
L010's A^2>n(k-1) cutoff is unchanged, and center-dependent weights,
general-interpolant coverage and the comparison with epsilon* q remain
missing. No calculation, new multiplicity claim or candidate proof was
produced. Resolving source access still requires its own literature
comparison before a later research turn.

## Mathlib

Full center-dependent Riccati statement: **not checked**. Formal versions
of the cited indicial, lifting, and weighted-decoding results: **not
checked**. The primary theorems above are supporting results, not claimed
Mathlib matches. No library search or formal verification was performed.
