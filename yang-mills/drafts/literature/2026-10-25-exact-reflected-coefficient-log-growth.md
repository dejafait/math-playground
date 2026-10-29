# Exact reflected coefficient — completed logarithmic-growth coverage review

TARGET: Test whether L279's full coefficient satisfies |kappa_a|<=C log(eN) for all sufficiently large even N with a=8/N, retaining the exact forest measure, both insertions, all action/Haar terms and the full oriented-plaquette tensor content.
CHECKED: 2026-10-25
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the September 26–27 flow/matching/locality assessments and exact-coefficient assessments; checked L004, L279, the ultraviolet draft, ATTEMPTS/005 and /046 for duplicates and failures. New searches for lattice composite plaquette correlations, uncontracted gluonic tensor mixing, all-face boundary renormalization and stronger power-counting results found no inspected theorem giving this exact bound; precise queries and leads are below.
SOURCE_EVIDENCE: Reopened Adams–Lee 0709.0781v3 section I (1), section II (7)–(15), Appendix A theorem (A1), preparations (A2)–(A10) and split (A11), printed pp. 2, 5–7, 19–22; newly read Detmold–Shanahan 1606.04505v3 section III.B (16)–(19), the qualification immediately after (19), and Appendix A (A1)–(A3), pp. 3–4, 9. Reopened Lüscher et al. hep-lat/9207009v1 sections 2.1 and 3.3; reused the previously inspected sections 3.4–3.5 and the other primary readings in the September assessments.
COMPARISON: Known logarithmic one-loop momentum-integral asymptotics require a justified reduction and summation control; they do not classify L279's full coefficient. The new tensor source supplies hypercubic representatives but explicitly does not compute their renormalization factors. Existing stress matching and slab effective-action results cover neither the complete bare oriented pair nor the all-face covariance. Kirwin remains fixed-dimensional only.
GAP: The full signed sum's mesh bound, cancellation of possible power growth, uncontracted-tensor matching if used, and all-face boundary control remain mathematical obligations. No inspected source settles them; no bound, divergence or sign is established.
REASON: The bounded discovery and theorem comparison are now complete for a direct exploratory attempt on L279 (7)–(9), without assuming a new renormalization or boundary theorem. Approve one bounded complete-coefficient cancellation test, not direct import or a repeat of the stopped bulk-only shortcut; any later use of an unread theorem needs separate coverage.
LITERATURE_REASON: The saved REVIEW_REQUIRED target asks for mesh uniformity beyond the ready fixed-mesh assessment, and requires comparison for an unflowed oriented two-insertion observable and all physical faces.
SCOPE: L279's SU(2) model, fixed physical cube, real f_*, even N, boundary-contained links pinned and normal links variable, ordinary trace, exact forest quotient and bare 4/g^2 insertions; no flow, Ward substitution, new gauge measure, or scalar-only reduction.

## Target and downstream use

The proposed test concerns the full signed coefficient, not separate
absolute bounds on individual forest-gauge terms. A constant C may
depend on the fixed cube and f_*, but not N. The threshold is logarithmic
growth, and no sign or leading logarithmic coefficient is assumed.
Such control could determine whether the first correction is compatible
with a later interacting comparison and which mixing estimates are
needed. Even success would not control the higher-order remainder on a
physical coupling trajectory or meet the c_box/2 threshold by itself.

Essential mathematical inputs for the proposed continuation are L279
and L003. L011 supplies the already used method, not an identity with
its Ward coefficient. L004 is a scope warning; no counterterm or
renormalization theorem is assumed. The continuum axioms, limiting
physical sector, infinite-volume limit and finite positive mass remain
unresolved.

## Review and continuation test

First compare precise primary hypotheses for lattice power counting and
composite-operator mixing with this exact coefficient and boundary
geometry. Reuse
`2026-09-27-fixed-box-one-loop-locality.md` and
`2026-09-26-current-target.md` where their inspected results apply;
do not repeat their unsupported bulk-only or scalar-only imports.
The latter assessment was not reopened in this audit, and its sources
are leads for comparison, not new premises here. The high-order Laplace
theorem alone cannot supply a constant uniform in lattice dimension.

Approve only a bounded test with explicit handling of the complete
coefficient and any needed cancellation or boundary comparison.
Continue the mathematical route if it obtains the stated bound or a
specific, independently testable obstruction to it. An uncontrolled
individual diagram is not a counterexample to a signed-sum bound.
An uncovered essential hypothesis requires literature work before
calculation. Persistent source obstruction requires a different
independently testable target, preserving the original stop evidence.

The original registration approved no calculation. This completed
literature review approves only the bounded direct attempt specified
below. It performs no growth calculation and changes no lemma or
mathematical script. Mathlib coverage is not checked.

## Completed primary comparison (step 481)

D. H. Adams and W. Lee, *Structure of logarithmically divergent one-loop
lattice Feynman integrals*, Phys. Rev. D 77 (2008), 045010,
[0709.0781v3, 5 December 2007](https://arxiv.org/pdf/0709.0781v3):
section II requires a single Brillouin-zone integral with smooth scaled
numerator and denominator, polynomial continuum limits, prescribed
denominator growth, no additional zeros, and infrared convergence.
For degree zero the structure is (1); Appendix A (A1) treats negative
degree with a momentum-dependent convergence bound. Its preparations
and three-region split (A11) use that denominator control. These are
conditional results, not a classification of arbitrary composite
correlations. Neither reduction of (7) to this class nor uniformity
under remaining sums has been established. Perturbative order alone
does not verify the single-loop hypothesis. No inference about the
full cutoff growth is imported.

W. Detmold and P. E. Shanahan, *Gluonic transversity from lattice QCD*,
Phys. Rev. D 94 (2016), 014507; erratum D 95 (2017), 079902,
[1606.04505v3, 23 March 2017](https://arxiv.org/pdf/1606.04505v3):
section III.B distinguishes uncontracted gluonic tensor representations
from the contracted stress operator. Equations (16)–(19) use clover
fields and representation-dependent matching factors; immediately
after (19) the authors state that they do not compute these factors.
Appendix A (A2)–(A3) displays two diagonal four-index representatives.
This provides a concrete lead for the sector left open by L004, not
its anomalous dimension or a bound for the exact plaquette pair.
No identification of these representatives with a complete interacting
box insertion is made here. A common scalar factor and stress protection
alone still cannot discharge the full tensor obligation.

M. Lüscher, R. Narayanan, P. Weisz and U. Wolff,
*The Schrödinger functional — a renormalizable probe for non-abelian
gauge theories*, Nucl. Phys. B 384 (1992), 168–228,
[hep-lat/9207009v1, 9 July 1992](https://arxiv.org/pdf/hep-lat/9207009v1):
sections 2.1 and 3.3 specify periodic spatial directions and an
effective-action determinant with strictly positive fluctuation
operators (zero modes explicitly excluded). The earlier inspected
sections 3.4–3.5 concern that problem. An effective-action subtraction
on this slab is not a composite-pair estimate in the all-face box.
The September 27 assessment's corner and general-boundary comparisons
are reused with their stated restrictions; no boundary constant or
corner contribution is assigned to L279.

The September 26 assessment's Suzuki and general-color clover matching
readings remain adequate for their contracted sectors. Reproving them
would be redundant, but transferring them to a single bare plaquette
would require additional work. Kirwin's fixed-dimensional theorem and
L279's seven-term extraction are already audited. Repeating the
extraction is not the proposed growth test.

## Bounded search, duplicate and failure decision

New queries included `lattice gauge theory composite operators plaquette
correlation one loop logarithmic divergence tensor mixing boundary
renormalization`, `lattice Yang Mills Fmunu Frhosigma operators hypercubic
renormalization one loop four index tensor`, `Detmold Shanahan gluon
transversity lattice hypercubic operator renormalization 2016`,
`Caracciolo Menotti Pelissetto 1992 energy momentum tensor lattice general
discretization renormalization`, `lattice Yang-Mills rectangular
renormalization boundary correlation one loop`, and `plaquette-plaquette
perturbation two-loop`. Broader composite/boundary searches were screened
against this exact observable rather than treated as theorem evidence.

The Caracciolo–Menotti–Pelissetto 1992 general-discretization paper remains
an abstract-only lead, as already recorded in the September 26 assessment;
the new search again found metadata, not its hypotheses. Original Reisz
all-orders results and scalar-gluonium correlator references are also
uninspected leads, not premises. Access to these is not required for
the direct test below, which invokes none of their missing conclusions.
Any switch to a theorem-based reduction must review the exact theorem
first. This search is bounded, not exhaustive, and establishes no novelty.

L004 already records the scalar/stress mismatch and remaining tensor
sector. ATTEMPTS/005 stops an unsupported bulk-only import for a
different Ward/flow pair, and ATTEMPTS/046 stops a nonperturbative source
import. Neither is a disproof of this coefficient bound. The materially
different mechanism here is the complete audited reflected sum itself,
with its exact finite matrices and no asserted bulk replacement. No
duplicate growth estimate was located in the specified local records.

## Approved direct test and stopping condition

Use essential inputs L279 and L003; L011 is only the existing connected
expansion method and L004 a scope warning. Start from all seven terms
of L279 (7), with the jets (8)–(9) and the inverse quadratic form on
the same forest slice. One research invocation may attempt a signed
connected-contraction organization and estimates for this whole sum.
Combine cancellations before absolute summation. Both insertions,
moving means, cubic/quartic action terms and M_2 must be represented;
no new coefficient extraction is needed.

Retaining the exact matrix jets preserves the oriented insertion rather
than projecting to scalar/stress channels. If a continuum mixing basis
is used instead, every remaining tensor channel and its cross terms
must be matched, not assumed. All plaquettes and all variable normal
links on the box remain in the action/measure sums. A bulk/boundary
split is permitted only as an exact identity with its full boundary
remainder retained; dropping it on grounds of separated interior
supports is not approved. Higher jets cannot be transferred to the
Hodge law using L003's quadratic comparison.

The success threshold remains one N-independent C with
|kappa_a| <= C log(eN) for all sufficiently large even N. A bounded
partial attempt may instead isolate a precise, complete signed
contraction family and the concrete estimate blocking control of the
whole sum; it must label that bound unproved. A numerical fit, a
divergent individual diagram or an omitted tensor/boundary family is
neither proof nor refutation. If the complete cancellation test cannot
be formulated without an unverified replacement, stop that mechanism
and preserve the obstruction rather than restart the old import.

This approves an exploratory proof attempt on an exact finite input,
not a theorem application with missing hypotheses silently supplied.
No essential unread source is assumed in that attempt. Any new
intermediate target outside this full-sum test needs its own assessment.
Higher-order uniform remainder, physical running-coupling trajectory,
continuum axioms/positivity, nonzero physical sector and finite positive
infinite-volume mass remain independent gaps even if the bound holds.

Completed kind/classification: LITERATURE / NOVELTY_UNCHECKED.
Outcome: EXPLORATION; new bounded source comparison, no new mathematical
input or beyond-source progress claimed. No mathematical exploration
budget was spent. Full bound and supporting Mathlib coverage: not checked.
