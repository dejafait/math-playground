# General six-coordinate pencils: completed source comparison

TARGET: Assess whether every nonpersistent pencil with both coefficient syndromes in a six-coordinate moment space at the fixed H has at most fifteen original bad parameters.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Ten targeted queries on 2026-10-17 found no inspected exact general-six-coordinate bound; compared L015/L032/L033/L040/L069, the L070 pair-lift proof and L082 application, and preserved failures ATTEMPTS/006,007,017,027; reused the October 7 shortening and October 11/13 pair source assessments.
SOURCE_EVIDENCE: Read Chojecki author TeX v9.2, dated July 17, 2026, retrieved 2026-10-17, lem:independent-union-rays and thm:bounded-residual-kernel-ray with complete proofs, lines 1339–1421, and thm:single-mds-circuit-ray with proof, lines 1422–1460, at https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex; reused inspected Hall Theorem 5.1.1 pp. 63–64 and Marquez-Corbella–Pellikaan section 5 pp. 7–8 as specified below.
COMPARISON: L040 requires three actual finite full errors and paired coordinate roots; L015/L069 require a five-set. The primary independent-union/residual-kernel bounds require confinement of every counted error support, which the coefficient-syndrome hypothesis does not supply. Existing distance, injectivity and equality-incidence tools cover a later specialization but do not state its missing extraction implication.
GAP: Under hypothetical sixteen-count equality, prove or refute that the unique affine lift on the six-set contains three actual finite full errors with union six and L033's paired-root form; handle a lift using fewer than six coordinates separately before applying the existing bounds.
REASON: Essential standard-source coverage and the audited local counting mechanism are ready for a bounded hypothesis extension; this review establishes neither the extraction implication nor the general fifteen bound and makes no originality claim.
SCOPE: F=F_(97^20), fixed order-sixteen H subset F_97^*, RS dimension eight, pinned event on 1/4<=delta<5/16; some six-set S subset H contains moment representatives of both coefficient syndromes; actual D and every coordinate locator are nonzero polynomials; arbitrary original finite chart and extension-field weights.
LITERATURE_REASON: The general coefficient-syndrome-space target drops the actual-three-error and paired-root hypotheses in the older six-coordinate assessment; their essential applicability comparison was missing.

## Completed review, 2026-10-17, step 285

The main gap is still exclusion or realization of L010's sixteen-count
equality, against an allowable count of fifteen. The global interval is
11/q–16/q. The selected intermediate target is the GAP above, conditional
on equality, for this representable class only. If established, its
downstream use would be to verify L033's explicit-triple hypotheses and
import audited L040, rather than enumerate another configuration. There
is no asserted universal extraction of a six-set from arbitrary pencils.
Uniform triangle twelve, cyclic feasibility and challenge-definition
qualifications remain independent unresolved questions.

This is a literature-only scope comparison. No extraction proof,
incidence calculation, lemma, mathematical script or certificate was
created. SPECIALIZE approves coverage for a later attempt; it does not
approve the truth of the proposed bridge. A newly completed ready
assessment receives separate supervisor approval before mathematics.

## Precise known inputs and applicability

J. I. Hall, *Notes on Coding Theory*, undated author-hosted GRS chapter,
[Theorem 5.1.1 and complete proof, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf).
Reuse the inspected extraction in
`2026-10-05-two-block-moment-obstruction.md`, Primary theorem and
applicability, and its October 13 reuse in
`2026-10-13-mixed-nine-union-six-label-application.md`.
The theorem allows any field, distinct evaluation labels, nonzero
multipliers and 0<k<=n. Here F is a field, H has sixteen distinct labels,
all multipliers are one and k=8; its distance conclusion is nine.
Import this standard theorem, without reproof. L010 separately supplies
the shifted-moment kernel, injectivity on up to eight coordinates,
same-support badness, the full finite-parameter bound and equality
balance. Those moment facts are not substituted for the distance theorem.

I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
[DOI 10.1016/j.ffa.2016.04.004](https://doi.org/10.1016/j.ffa.2016.04.004),
[accepted manuscript dated February 29, 2016](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
section 5, Definitions 5.1–5.2, Lemma 5.3 and the following unnumbered
GRS shortening formula, printed pp. 7–8. Reuse the inspected extraction
in `2026-10-07-six-coordinate-triple-equality-obstruction.md`, Primary
shortening input, and the explicit iteration already justified in L033.
Shortening imposes zeros before deletion and changes retained multipliers
by label differences. No fresh source retrieval is claimed here and no
new shortening calculation is needed: the proposed attempt would import
L040 only after checking its exact hypotheses. Its audited finite checks
and the five-set census retain their computational qualifications.

P. Chojecki, *Shortening Bounds for Reed–Solomon MCA*,
[author TeX v9.2](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
dated July 17, 2026; retrieved October 17. Read the complete statements
and proofs at lines 1339–1460: `lem:independent-union-rays`,
`thm:bounded-residual-kernel-ray` and `thm:single-mds-circuit-ray`.
The first requires the union of all counted witnessing supports to have
size at most the redundancy; the second requires every support inside
one fixed U and gives (t+1)|F|^kappa(U); its proof groups chosen error
lifts by their residual kernel elements, retaining both active-support
cases. The circuit theorem requires confinement to R+1 columns and gives
binom(R+1,2). The present target asserts coefficient-syndrome membership,
not confinement of all actual errors. Thus neither confinement premise
can be assumed. The source is a mutable author manuscript; identity with
ePrint 2026/1463 is not certified. No theorem from it is an essential
premise of the proposed bridge.

Reuse the stronger-result comparison in
`2026-10-07-six-coordinate-triple-equality-obstruction.md`, Reused
coverage and quantitative comparison, and the inspected pair comparison
in `2026-10-11-triangle-six-label-recovery-pair.md`. BCHKS,
*Improved Proximity Gaps for Reed–Solomon Codes*, November 11, 2025
author version, [Theorems 1.3 and 4.6, printed pp. 8 and 28–29](https://www.math.toronto.edu/swastik/rs-proximity-gaps-2025.pdf),
has the saved sharp-range endpoint 7/32 below this cell and a wider
coefficient exceeding sixteen. No changed numerical hypothesis warrants
repeating its full proof. The fixed-core and generic-domain comparisons
also remain inapplicable without their missing hypotheses. Unread July
ABF26 and ePrint 2025/1712 are not proof inputs; their historical retrieval
stops are preserved and no progress beyond their claims is asserted.

## Local duplicates, remaining difference and bounded attempt

L015's full analytic proof covers coefficient-syndrome membership in a
five-set, arbitrary extension-field weights and dependent syndromes.
Only L069's universal M<=6 conclusion is needed for a five-set application;
its triangle assumptions cannot be used to subtract three base events
here. ATTEMPTS/007 records why that entire generator cannot attain
sixteen. A later attempt must account for inactive coordinates of the
proposed six-set rather than assume six active coordinate polynomials.

L032 classifies three already selected actual equality errors with union
at most eight; it does not assert that such errors lie in a proposed
syndrome representative set. L033 requires its explicit original-chart
three-error lift. L040 bounds that entire full bad set by fifteen,
including its separate lower-weight case. Neither supplies the missing
implication merely from coefficient-syndrome membership in a six-set.
Their inspected hypotheses therefore do not directly import the TARGET.

L070's proof, Actual pair lift and the nonzero-codeword alternative through
All cancellations at the extracted parameter, retains the equal-vector
exception in the distance argument. It derives its incidence deficit
from two actual errors with union six. Its statement is restricted to
an L057 triangle's additional pair. L082's audited mixed-row application
extends that argument to a specified base pair, but still starts with
two actual errors on the six-set. These are ready proof mechanisms to
adapt, not statements covering an arbitrary coefficient-syndrome lift.
Any repetition is justified only to remove this missing actual-error
premise; it is reproduction of the mechanism, not a new distance result.

The independently testable missing claim is: if the reviewed pencil has
sixteen bad parameters and its lift has six active coordinates, then
there are three distinct original finite bad parameters whose actual
errors equal that lift and have union exactly S, with paired-root form
as required by L033. This is a proposed claim, not a conclusion of this
review. A later attempt should test it using the fixed-set distance
alternative and L010's equality incidences, preserving the exception
when an error equals the lift. It must handle inactive coordinates,
constant coordinates, dependent coefficient syndromes, cancellations,
singular parameters and the entire original finite chart. L015/L069
and L032 are available only after their hypotheses are checked.

Continue if a bounded proof attempt establishes this bridge (or another
fully justified exclusion within the same TARGET) and permits the
existing full-event bounds to apply. Abandon the proposed bridge on a
verified gated counterexample or a specific unrepairable missing premise;
a locally compatible triple or a rational projective intersection is
insufficient evidence either way. Do not repeat a finite configuration
census or reopen incidence-only extraction. ATTEMPTS/006 concerns the
prescribed two-block generator, ATTEMPTS/017 refutes a different universal
small-union criterion, and ATTEMPTS/027 refutes useful-pair extraction
from balance plus a triangle alone. None supplies a counterexample to
this additional syndrome-space hypothesis; all stops remain intact.

Essential continuation inputs are L010/L015/L069 and L032/L033/L040;
L070/L082 are proof comparisons, without an out-of-scope application.
No cross-notebook input is used. Full matching Mathlib coverage for the
general six-coordinate bound and extraction bridge is **not checked**;
canonical inputs retain their own supporting-coverage qualifications.

## Bounded search record

Queries on October 17, 2026:

- `"Reed Solomon" "six" "syndrome" "pencil"`
- `"mutual correlated agreement" "six" support`
- `"Shortening Bounds for Reed–Solomon MCA" residual kernel`
- `"Reed-Solomon" "six-coordinate"`
- `"MCA" "syndrome" "six" "pencil"`
- `"MDS" "affine" "sparse" "pencil" syndrome`
- `"Reed-Solomon" "coefficient syndromes" support`
- `"Reed-Solomon" "independent-union" rays`
- `"Reed-Solomon" "six-coordinate" "fifteen"`
- `"Reed-Solomon" "affine pencil" "sparse"`

Searches found the author repository, decoding implementations and
unrelated acronym matches. Only the primary theorem passages identified
above were used for fresh theorem comparison. Repository summaries,
secondary overviews and snippets are discovery leads, not theorem
evidence. No inspected exact match was found; this bounded search does
not establish novelty or literature absence. Ready standard coverage
was reused instead of reopening parked access routes. The outcome is
EXPLORATION: a new scope comparison and a bounded continuation, without
a new mathematical bound or a source import resolving the target.

## Original proposed scope (preserved; review completed above)

The proposed downstream use is an exclusion of L010 equality within a
larger representable class. No universal extraction of such a six-set,
global bound, sharpness or challenge-level identification is assumed.
The next turn should compare the exact target with existing local results
and primary sources before authorizing any new proof or calculation.

Essential starting inputs are L010, L015 and L069 for the established
event and smaller class, and L032/L033/L040 for the relevant special
six-coordinate results. Their exact applicability is an unresolved
obligation, not a premise. Search only the relevant local claims and
recorded failures, and reuse source assessments if their hypotheses
actually cover this target. In particular the new review must distinguish
an arbitrary coefficient-syndrome lift from an actual selected error
triple; the completed L102 audit establishes no bridge between them.

Continuation test: identify either a fully covered existing bound or one
precise missing intermediate statement with a discriminating test for
the fifteen threshold. If the target is already settled, import it with
exact hypotheses rather than reproduce a search. If a recorded
obstruction defeats this class reduction, preserve it and choose a
materially different target. No dependent mathematics is approved by
this note.
