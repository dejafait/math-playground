# Proposed deletion-stability test — completed source comparison

TARGET: Test whether every ordinary (965,9,5,1) packing on H minus a 59-core can be made L041-admissible by deleting at most 1024 blocks.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped L041/C040a statements, the prior 59-core assessment and ATTEMPTS/019,021,024 were compared; targeted searches for finite forbidden-configuration deletion, packing designs, and hypergraph transversals led to the primary sources inspected below, without an exact matching 1024-block theorem.
SOURCE_EVIDENCE: Reuse Bailey–Burgess arXiv:1107.4120v2 p. 2 Definitions 1.1.1/1.1.3; inspect Chernikov's Topics in Combinatorics (updated 2017-02-28) Definition 4.1 and Remark 4.5 pp. 21–22, Tao arXiv:math/0503572v2 Definitions 1.4/1.6 and Corollary 1.14 pp. 3/6, and Anstee–Barekat–Pellegrin arXiv:1909.11602v1 Theorem 1.6 p. 4.
COMPARISON: Finite hitting-set and packing uniqueness tools cover the method; asymptotic removal and design-avoidance results do not furnish this numerical deletion guarantee. The fixed ordered labels and private completions require an application argument, not a reproof of the general tools.
GAP: Prove or refute the universal 1024-block deletion bound using L041's exact ordered common shifts, every core and every private completion; no deletion bound or comparison of maxima is established in this literature turn.
REASON: Essential source coverage is now adequate for one finite specialization attempt; the changed assessment receives separate supervisor approval next turn, without invoking mathematics here.
SCOPE: C001a's fixed H of order 1024, every 59-core C, ordinary nine-set packings on H minus C, exactly L041 condition (A) with C040a's fixed ordered edges and common shifts; no independent shifts or arbitrary-label rank symmetry.

## Mechanisms compared and selected test

The main gap is a useful actual-label cap for 68-agreement safety.
Three prospective mechanisms have different obligations:

1. **Deletion stability (selected).** Test the stated 1024-block loss
   for an arbitrary ordinary packing. This compares the strength of
   the currently retained restrictions with ordinary packing and can
   succeed without a large explicit packing, a new rank certificate,
   cross-core consistency or RS realization. It is a target, not a
   claimed fact; the ordered configurations and all private choices
   must be accounted for.
2. **Finite ordinary-packing construction.** Seek an explicit packing
   above L041's sufficient cap, then check labeled exclusions. This
   requires a large finite construction not supplied by the nested
   upper bound. The earlier failed cubic avoidance constructions in
   ATTEMPTS/023,025 cannot be reused as avoidance certificates, and
   asymptotic existence without an effective cutoff is insufficient.
3. **Broader algebraic exclusions.** Seek new full-rank overlap label
   assignments beyond common shifts. This changes the assessed
   algebraic scope and would still need a quantitative cap mechanism;
   no arbitrary permutation or independent shift is authorized by
   C040a. It is not chosen for this continuation.

The selected test differs from ATTEMPTS/019–021's stopped 61-core
moment model and ATTEMPTS/024's sharp anchored neighborhood graph.
It concerns the maximum effect of L041's specific labeled exclusions,
not an attempt to tighten either unchanged stopped relaxation.

Plausible downstream use: a proved deletion bound would compare the
ordinary and labeled maxima and quantify the finite packing lower
bound needed for an obstruction to this certificate. It would not
alone supply that lower bound, show that L041's cap is impossible,
or produce an unsafe list. Continue this mechanism only if a universal
deletion statement with all quantifiers survives source comparison
and proof; abandon or correct the 1024 bound if the multiplicity of
ordered configurations or private completions defeats it. No count,
deletion proof or maximum inequality is derived in this step.

Essential inputs for future work: L041's precise admissibility and
threshold, C040a's pattern scope, C001a's instance, and the named
ordinary packing definition. A useful finite packing lower bound,
cross-core consistency, common-center realization and 67/68 safety
remain unresolved. Full matching Mathlib coverage is not checked.
The completed comparison below supplies coverage for a mathematical
attempt after separate supervisor approval; it does not certify the
proposed bound.

## Primary statements and applicability

Artem Chernikov, [Topics in Combinatorics, MATH 285N, UCLA Winter
2016](https://www.math.ucla.edu/~chernikov/teaching/Combinatorics285N/CombinatoricsNotes.pdf),
last updated 28 February 2017, Definition 4.1 and Remark 4.5,
printed pp. 21–22: a transversal meets every set; a packing consists
of pairwise disjoint sets. For a finite r-uniform hypergraph,
nu<=tau<=r*nu. The upper inequality is justified there by taking
the union of a maximal matching. Definitions and that complete
proof sentence were inspected. This is a general finite tool,
not the numerical statement sought. A possible application has
blocks as vertices and violating five-block collections as edges;
constructing a suitably small transversal remains the application
obligation. Isolated vertices cause no difficulty for these definitions.
Only this elementary part is imported as coverage; no Ryser conjecture
or partiteness assertion is used.

Terence Tao, [A variant of the hypergraph removal lemma,
arXiv:math/0503572v2](https://arxiv.org/pdf/math/0503572v2),
16 November 2005, Definitions 1.4/1.6, printed p. 3, and
Corollary 1.14, printed p. 6, were inspected, including the displayed
copy and removal bounds. Finite nonempty vertex parts V_j, a fixed
d-uniform pattern H_d on J, and relations E_e on the corresponding
products are required. At most delta*product_j|V_j| copies, with
0<delta<=1, permit copy-free modified relations with each deletion
size o_(delta->0;|J|)(product_(j in e)|V_j|). This statement supplies
neither a numerical modulus useful here nor a certified 1024-block
bound. Encoding the common-shift label relation would also need
justification. It is therefore a comparison source, not an essential
proof input; its long regularity proof is not needed for the selected
finite approach. The earlier PMC removal-paper retrieval returned a
CAPTCHA page and is not counted as theorem evidence.

R.P. Anstee, Farzin Barekat and Zachary Pellegrin,
[Design Theory and some Forbidden Configurations,
arXiv:1909.11602v1](https://arxiv.org/pdf/1909.11602v1),
23 September 2019 (manuscript date 26 September), Theorem 1.6,
printed p. 4, was inspected. For fixed t>ell and lambda, sufficiently
large m, an m-rowed binary matrix with column sums from t+1 through
m-1 avoiding (lambda+1) identical columns 1_t0_ell on selected rows
has at most lambda/(t+1)*binomial(m,t) columns; equality corresponds
to a t-(m,t+1,lambda) design. This forbidden submatrix is different
from L041's actual-label pattern, and the theorem concerns extremal
size rather than deletion. It does not import the target bound.
Its quoted design-existence Theorem 1.1 is not used as primary
evidence for a finite ordinary packing construction.

## Discovery record and permitted specialization

Queries included `hypergraph packing forbidden configurations deletion
transversal finite removal lemma`, `packing designs forbidden
configurations bounded deletion fixed labelled configurations`,
`hypergraph transversal maximal matching theorem`, `"packing design"
"deletion" "forbidden"`, and `"Reed Solomon" "deleting" "packing"
"configuration"`. An instance-number query returned irrelevant cargo
packing results; it establishes no mathematical absence. Broader
searches located removal, sunflower and design-avoidance leads. The
three inspected sources above, plus the reused ordinary-packing
assessment, suffice for the selected elementary application; unread
sunflower papers, survey links and anti-Pasch constructions are not
claimed as assessed theorem coverage. No novelty is inferred.

Bailey–Burgess's lambda=1 packing definition fixes the relevant
uniqueness input; reuse its prior full retrieval rather than repeat
the packing-source search. The task is to specialize finite
transversal selection to L041's explicitly prescribed configuration.
The next proof attempt may test a designated vertex's overlap-union
as a fixed subset for each shift, checking whether ordinary packing
uniqueness controls all of its private completions and whether the
resulting choices hit every ordered violation. These are unproved
proof obligations, not a deletion argument supplied in this review.
Duplicated selected blocks across shifts, inactive shifts, cores
meeting overlap labels, empty families and additional surviving
violations must all be handled. No arbitrary-label transport or
independent edge shifts are permitted. Reprove neither the finite
transversal tool nor the ordinary nested bound; give only the needed
application argument. If that mechanism fails, record the precise
multiplicity obstruction before changing the target.

The prior local failures concern different unchanged 61-core and
anchored 60-core models. They do not decide this deletion question.
Even a successful bound would leave a large finite ordinary packing,
cross-core consistency, common-center realization, ABF equivalence
and safety at 67/68 agreements unresolved. Matching Mathlib coverage
for the full deletion statement is not checked; no absence is asserted.
